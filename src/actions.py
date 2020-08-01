import json
from pprint import pprint
from pathlib import Path
import yaml
import re


def str_presenter(dumper, data):
    def is_multiline(s): return len(s.splitlines()) > 1
    # print(data, is_multiline(data))
    if is_multiline(data):  # check for multiline string
        return dumper.represent_scalar('tag:yaml.org,2002:str', re.sub(r'\n[ ]+', '\n', data), style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)


yaml.add_representer(str, str_presenter)


class WorkFlow:
    'github action workflow'

    def _gen_empty_job(self):
        'generate empty job frame work'
        job = {}
        job['runs-on'] = 'ubuntu-18.04'  # build system
        job["strategy"] = {
            "fail-fast": False
        }
        return job

    def _gen_empty_steps(self):
        'initilize steps'
        return [
            {'uses': 'actions/checkout@v2'}
        ]

    def _gen_debugger_step(self):
        'gengerate remote ssh to debug'
        return {
            "uses": "mxschmitt/action-tmate@v2",
            "if": "always()"
        }

    @classmethod
    def _gen_cache_step(cls, path: str, key: str, step_id: str = None, restore_keys: list = []):
        'cache step'
        stp = {}
        if step_id:
            stp['id'] = step_id
        # refs: https://help.github.com/en/actions/configuring-and-managing-workflows/caching-dependencies-to-speed-up-workflows
        stp['uses'] = 'actions/cache@v2'
        stp['with'] = {
            'path': path,
            'key': key
        }
        if len(restore_keys) > 0:
            stp['with']['restore-keys'] = '\n'.join(restore_keys)
        return stp

    @classmethod
    def _hit_cached(cls, step_id: str, rst: bool = True):
        'a condition of hit cache'
        ans = "steps.%s.outputs.cache-hit == 'true'" % step_id
        if not rst:
            ans = "steps.%s.outputs.cache-hit != 'true'" % step_id
        return ans

    @classmethod
    def _gen_vars(cls, kv: object):
        'generate variable'
        ans = []
        for k in kv:
            ans.append(
                '{0}={1}\necho ${0}\necho "::set-output name={0}::${0}"'.format(
                    k, kv[k])
            )
        return '\n'.join(ans)

    @classmethod
    def _out_var(cls, jobid: str, key: str):
        'get variable from other job'
        return '${{needs.%s.outputs.%s}}' % (jobid, key)

    @classmethod
    def _in_var(cls, stepid: str, key: str):
        'get variable from same job'
        return '${{steps.%s.outputs.%s}}' % (stepid, key)

    @classmethod
    def _gen_upload_artifact_step(cls, name: str, path: str, addon: object = {}):
        'upload artifact'
        ans = {
            "uses": "actions/upload-artifact@v2",
            "with": {
                "name": name,
                "path": path,
            }
        }
        ans.update(addon)
        return ans

    @classmethod
    def _gen_download_artifact_step(cls, name: str, path: str, addon: object = {}):
        'download artifact'
        ans = {
            "uses": "actions/download-artifact@v2",
            "with": {
                "name": name,
                "path": path,
            }
        }
        ans.update(addon)
        return ans

    @classmethod
    def _gen_install_transfer_step(cls):
        'gengerate step to install https://github.com/Mikubill/transfer'
        return {
            'run': r'''
            curl -sL https://git.io/file-transfer | sh
            sudo mv ./transfer /usr/bin
            '''
        }

    @classmethod
    def _gen_upload_file_step(cls, path: str, step_id: str = None):
        'upload file to cow'
        ans = {
            'run': r'''
            TRANS_RST=$(transfer cow %s)
            %s
            ''' % (path, cls._gen_vars(
                {'links': "$(echo $TRANS_RST | grep -Pe 'Download Link: ' | sed 's/Download Link: //g')"}
            ))
        }
        if step_id:
            ans['id'] = step_id
        return ans

    @classmethod
    def _gen_fast_clone_submodules(cls):
        'fast clone submodules'
        return {
            'run': 'git submodule update --init --recursive --recommend-shallow'
        }

    @property
    def useless_packages(self):
        'useless dpkg packages'
        return 'azure-cli ghc zulu* hhvm llvm* firefox google* dotnet* powershell openjdk* mysql* php* msodbc*'

    def apt_job(self):
        'cache apt'
        job = self._gen_empty_job()
        stps: list = self._gen_empty_steps()
        job['outputs'] = {
            "dateDot": self._in_var('var', 'dateDot'),
            "dateDash": self._in_var('var', 'dateDash'),
            "tag": self._in_var('var', 'tag'),
        }
        stps.extend([
            # {'run': '[[ "${{secrets.RELEASE_TOKEN}}" ]] || false'},
            {
                'id': 'var',
                'run': self._gen_vars({
                    'dateDot': "$(date +'%y.%m')",
                    'dateDash': "$(date +'%y-%m')",
                    # TODO: test
                    'tag': "python-v${dateDot}.${{github.run_number}}"
                })
            },
            self._gen_cache_step(
                self.cache_apt,
                "apt-%s-%s" % (self._in_var('var', 'dateDash'), self.hash_apt),
                'cache-apt'
            ),
            self._gen_cache_step(
                self.cache_python,
                "python-%s-%s" % (self._in_var('var', 'dateDash'),
                                  self.hash_python),
                'cache-python'
            ),
            {
                'if': "%s || %s" % (self._hit_cached('cache-apt', False), self._hit_cached('cache-python', False)),
                'name': 'opde init',
                'run': r'''
                    # docker rmi $(docker images -q)
                    sudo -E apt-get remove -y --purge %s
                    sudo -E apt-get update -y || ( sleep 1m && sudo -E apt-get update -y) || ( sleep 1m && sudo -E apt-get update -y)
                    sudo -E apt install -y apt-offline
                    APT_PACKS=($(tr '\n' ' ' < ./cache/apt.list.txt))
                    echo "opde install packages list:"
                    echo ${APT_PACKS[@]}
                    # https://blog.sleeplessbeastie.eu/2014/01/30/how-to-manage-packages-on-an-off-line-debian-system/
                    sudo -E apt-key exportall | sudo -E gpg --no-default-keyring --import --keyring /etc/apt/trusted.gpg
                    sudo -E apt-offline set ./cache/apt/opde-apt.sig --update --upgrade --install-packages ${APT_PACKS[@]}
                    apt-offline get cache/apt/opde-apt.sig --bundle ./cache/apt/opde-bundle.zip -t $(($(nproc)*2))
                    echo "testing intall..."
                    # --allow-unauthenticated
                    sudo -E apt-offline install ./cache/apt/opde-bundle.zip --skip-bug-reports --skip-changelog
                    sudo -E apt-get upgrade
                    sudo -E apt-get install ${APT_PACKS[@]}
                    ''' % self.useless_packages
            },
            {
                'if': self._hit_cached('cache-python', False),
                'run': r'''
                    cd ./cache/python
                    curl -SL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -o get-poetry.py
                    # https://github.com/python-poetry/poetry/issues/2106#issuecomment-644471434
                    sed -i 's/allowed_executables = \["python", "python3"\]/allowed_executables = \["python3", "python"\]/' get-poetry.py
                    curl -SL https://github.com/python-poetry/poetry/releases/download/1.0.10/poetry-1.0.10-linux.tar.gz -o poetry.tar.gz
                    python3 get-poetry.py --file poetry.tar.gz -y
                    source $HOME/.poetry/env
                    cd ${{ github.workspace }}
                    python3 -m venv .venv
                    source .venv/bin/activate
                    poetry export -f requirements.txt -o ./cache/python/requirements.txt
                    cd ./cache/python
                    pip3 download -r requirements.txt -d wheelhouse
                    # testing pip install
                    pip3 install --no-index --find-links="./wheelhouse" -r requirements.txt
                    '''
            },
        ])
        # TODO: debuging
        # stps.extend([
        #     {
        #         'uses': 'meeDamian/github-release@2.0',
        #         'with': {
        #             'token': "${{secrets.GITHUB_TOKEN}}",
        #             'tag': self._in_var('var', 'tag'),
        #             'name': 'Release ' + self._in_var('var', 'tag'),
        #             'allow_override': True,
        #             'draft': True,
        #             'body': r'''
        #             Activate `ootoc` in `latest`
        #             ``` bash
        #             bash <(wget -qO- https://cdn.jsdelivr.net/gh/${{github.repository}}@${{steps.tag.outputs.tagName}}/feeds/scripts/activate-ootoc.sh) ${{github.repository}} latest ${{steps.tag.outputs.tagName}}
        #             ```
        #             Activate `ootoc` in `ctcgfw`
        #             ``` bash
        #             bash <(wget -qO- https://cdn.jsdelivr.net/gh/${{github.repository}}@${{steps.tag.outputs.tagName}}/feeds/scripts/activate-ootoc.sh) ${{github.repository}} ctcgfw ${{steps.tag.outputs.tagName}}
        #             ```
        #             '''
        #         }
        #     }
        # ])
        job['steps'] = stps
        return job

    def _opde_init_steps(self, fast=False):
        'initilize opde common environment'
        return [
            self._gen_cache_step(
                self.cache_apt,
                "apt-%s-%s" % (self._out_var('APT', 'dateDash'), self.hash_apt),
            ),
            {
                'env': {'DEBIAN_FRONTEND': 'noninteractive'},
                'run': r'''
                    sudo -E apt-get -yq update || ( sleep 1m && sudo -E apt-get update -y) || ( sleep 1m && sudo -E apt-get update -y)
                    %s
                    sudo -E apt-get -yq install apt-offline
                    APT_PACKS=($(tr '\n' ' ' < ./cache/apt.list.txt))
                    # https://blog.sleeplessbeastie.eu/2014/01/30/how-to-manage-packages-on-an-off-line-debian-system/
                    # --allow-unauthenticated
                    sudo -E apt-offline install ./cache/apt/opde-bundle.zip --skip-bug-reports --skip-changelog
                    %s
                    sudo -E apt-get -yq install ${APT_PACKS[@]}
                    sudo -E ln -sf /usr/bin/gcc-8 /usr/bin/gcc
                    sudo -E ln -sf /usr/bin/g++-8 /usr/bin/g++
                    # https://github.com/project-openwrt/openwrt-isco/issues/181
                    sudo -E ln -sf /usr/include/asm-generic /usr/include/asm
                    ''' % (r'''
                    docker rmi $(docker images -q)
                    sudo -E apt-get -yq remove --purge {}
                    sudo -E apt-get -yq autoremove --purge
                    sudo -E apt-get -yq clean
                    sudo -E rm -rf /usr/share/dotnet /etc/mysql /etc/php
                    '''.format(self.useless_packages) if not fast else '',
                           'sudo -E apt-get -yq upgrade' if not fast else '')
            },
            self._gen_cache_step(
                self.cache_python,
                "python-${{needs.APT.outputs.dateDash}}-${{ hashFiles('./poetry.lock') }}",
            ),
            {
                'run': r'''
                    sed -i 's/allowed_executables = \["python", "python3"\]/allowed_executables = \["python3", "python"\]/' ./cache/python/get-poetry.py
                    python3 ./cache/python/get-poetry.py --file ./cache/python/poetry.tar.gz -y
                    source $HOME/.poetry/env
                    sudo -E ln -sf $HOME/.poetry/bin/poetry /usr/bin/poetry
                    python3 -m venv .venv
                    source .venv/bin/activate
                    pip3 install --no-index --find-links="./cache/python/wheelhouse" -r ./cache/python/requirements.txt
                    '''
            },
        ]

    def _gen_download_db_steps(self):
        'download issues database'
        return [
            {
                'uses': 'actions/checkout@v2',
                'with': {
                    'ref': 'gh-pages',
                    'path': '${{github.workspace}}/opde-issues',
                }
            },
            {
                'id': 'issues-var',
                'run': self._gen_vars({
                    'DB_PATH': '${{github.workspace}}/opde-issues/logs.db.json',
                })
            },
        ]

    def sdk_job(self):
        'building sdk, imagebuilder and firmware'
        job = self._gen_empty_job()
        stps: list = self._gen_empty_steps()
        stps.extend(self._opde_init_steps())
        db_path = self._in_var('issues-vars', 'DB_PATH')
        stps.extend([
            self._gen_fast_clone_submodules(),
            {'run': self.builder + ' init'},
            {'run': self.builder + ' feeds'},
            {'run': self.builder + ' config -sdk -ib -ke'},
            {'run': self.builder + ' metadata > %s' % self.hash_openwrt_path},
            {
                'id': 'cache-var',
                'run': self._gen_vars({
                    'OPENWRT_KEY': "'openwrt-sdk-test-${{needs.APT.outputs.dateDash}}-%s'" % self.hash_openwrt,
                })
            },
            self._gen_cache_step(
                './cache/openwrt',
                self._in_var('cache-var', 'OPENWRT_KEY'),
                'cache-openwrt',
                ["openwrt-sdk-test-${{needs.APT.outputs.dateDash}}"]
            ),
            # self._gen_debugger_step(),
            {
                'if': self._hit_cached('cache-openwrt', False),
                'run': self.builder + ' download'
            },
            {'run': self.builder + ' build'},
            {
                'id': 'sdk-var',
                'if': 'always()',
                'run': self._gen_vars({
                    'openwrt': '$(%s @output opdir)' % self.builder,
                    'logs': '$(%s @output logdir)' % self.builder,
                    'tasks': '$(%s @output taskdir)' % self.builder,
                })
            },
        ])
        stps.extend( self._gen_download_db_steps())
        db_path = self._in_var('issues-vars', 'DB_PATH')
        stps.extend([
            {
                'run': self.builder + ' extract %s %s ${{github.run_number}}' %
                (self._in_var('sdk-var', 'logs'), db_path)
            },
            {'run': 'cp -rf %s %s' % (db_path, self._in_var('sdk-var', 'logs'))},
            {'run': self.builder + ' check %s ${{github.run_number}}' % db_path},
            # TODO: workflow_dispatch
            {
                'run': self.builder + ' assign %s %s' % (
                    self.worker_num, db_path)
            },
            self._gen_upload_artifact_step(
                'Kernel-Log', self._in_var(
                    'sdk-var', 'logs'),
                {'if': 'always()'}
            ),
            self._gen_upload_artifact_step(
                'Tasks', self._in_var('sdk-var', 'tasks')),
            {
                'id': 'sdk-var2',
                'run': self._gen_vars({
                    'SDK_PATH': '$(find %s/bin -name "*sdk*")' % self._in_var('sdk-var', 'openwrt'),
                    'SDK_NAME': '$(basename $SDK_PATH)',
                    'IMAGE_BUILDER_PATH': '$(find %s/bin -name "*imagebuilder*")' % self._in_var('sdk-var', 'openwrt'),
                    'IMAGE_BUILDER_NAME': '$(basename $IMAGE_BUILDER_PATH)',
                })
            },
            self._gen_upload_artifact_step(
                'SDK', self._in_var('sdk-var2', 'SDK_PATH')),
            self._gen_upload_artifact_step(
                'ImageBuilder', self._in_var('sdk-var2', 'IMAGE_BUILDER_PATH')),
            {
                'working-directory': self._in_var('sdk-var', 'openwrt'),
                'run': '''
                    tar -cf tmp.tar bin/targets/*/*/packages
                    rm bin/targets/*/*/packages -rf
                    rm {sdk} -rf
                    rm {ib} -rf
                    ls -lh bin/targets/*/*/ || true
                    ( ls bin/targets/*/*/*.vdi >/dev/null 2>&1 ) && gzip -9n bin/targets/*/*/*.vdi || true
                    ( ls bin/targets/*/*/*.vmdk >/dev/null 2>&1 ) && gzip -9n bin/targets/*/*/*.vmdk || true
                    '''.format(
                    sdk=self._in_var('sdk-var2', 'SDK_PATH'),
                    ib=self._in_var('sdk-var2', 'IMAGE_BUILDER_PATH')
                )
            },
            self._gen_upload_artifact_step(
                'Firmware', self._in_var('sdk-var', 'openwrt') + '/bin/targets'),
            {
                'working-directory': self._in_var('sdk-var', 'openwrt'),
                'run': '''rm bin/targets -rf\ntar -xf tmp.tar'''
            },
            self._gen_upload_artifact_step(
                'Packages-00', self._in_var('sdk-var', 'openwrt') + '/bin'),
            # collect all openwrt's source bundles
            {
                'if': self._hit_cached('cache-openwrt', False),
                'run': self.builder + ' config -sdk -ib -ke -a\n' +
                self.builder + ' download'
            },
            self._gen_install_transfer_step(),
            self._gen_upload_file_step(db_path, 'transfer'),
            # self._gen_debugger_step(),
        ])
        job['steps'] = stps
        job['outputs'] = {
            "SDK_NAME": self._in_var('sdk-var2', 'SDK_NAME'),
            "IMAGE_BUILDER_NAME": self._in_var('sdk-var2', 'IMAGE_BUILDE_NAME'),
            "CACHE_OPENWRT_KEY": self._in_var('cache-var', 'OPENWRT_KEY'),
        }
        return job
        pass

    def worker_job(self):
        'a worker job to massive packages'
        job = self._gen_empty_job()
        job['strategy']['matrix'] = {
            'worker': ['{:0>2}'.format(i) for i in range(1, 1 + self.worker_num)]
        }
        worker_id = '${{matrix.worker}}'
        stps: list = self._gen_empty_steps()
        stps.extend(self._opde_init_steps())
        worker_builder = self.builder + ' -sdk'
        stps.extend([
            self._gen_fast_clone_submodules(),
            self._gen_download_artifact_step('SDK', '~/artifacts'),
            {'run': worker_builder +
                ' init --sdk-archive ~/artifacts/%s' % self._out_var('BASE', 'SDK_NAME')},
            {'run': worker_builder + ' feeds'},
            self._gen_download_artifact_step('Tasks', '~/artifacts/tasks'),
            {'run': worker_builder +
                ' config -i ~/artifacts/tasks/%s.worker.conf' % worker_id},
            self._gen_cache_step(
                './cache/openwrt',
                self._out_var('BASE', 'CACHE_OPENWRT_KEY'),
                'cache-openwrt',
            ),
            {
                'if': self._hit_cached('cache-openwrt', False),
                'run': worker_builder + ' download'
            },
            {'run': worker_builder + ' build'},
            {
                'id': 'worker-var',
                'if': 'always()',
                'run': self._gen_vars({
                    'openwrt': '$(%s @output opdir)' % worker_builder,
                    'logs': '$(%s @output logdir)' % worker_builder,
                })
            },
            self._gen_upload_artifact_step(
                'Packages-%s' % worker_id, self._in_var('worker-var', 'openwrt') + '/bin'),
            self._gen_upload_artifact_step(
                'Worker%s-Log' % worker_id,
                self._in_var('worker-var', 'logs'),
                {'if': 'always()'}
            ),
        ])
        job['steps'] = stps
        return job

    def bundle_job(self):
        'bundle all workers prodution'
        job = self._gen_empty_job()
        stps: list = self._gen_empty_steps()
        stps.extend(self._opde_init_steps(True))
        bundler_builder = self.builder
        stps.append(
            {
                'id': 'bundle-var',
                'if': 'always()',
                'run': self._gen_vars({
                    'openwrt': '$(%s @output opdir)' % bundler_builder,
                    # 'logs': '$(%s @output logdir)' % bundler_builder,
                })
            }
        )
        stps.extend([
            self._gen_download_artifact_step(
                'Packages-{:0>2}'.format(i),
                '%s/bin' % self._in_var('bundle-var', 'openwrt'))
            for i in range(self.worker_num, -1, -1)
        ])
        stps.extend([
            self._gen_download_artifact_step(
                'Worker{:0>2}-Log'.format(i+1),
                '~/artifacts/logs/Worker{:0>2}-Log'.format(i+1)
                )
            for i in range(self.worker_num)
        ])
        stps.append(
            self._gen_download_artifact_step( 'Kernel-Log', '~/artifacts/logs/Kernel-Log')
        )
        db_path = self._in_var('issues-vars', 'DB_PATH')
        stps.extend( self._gen_download_db_steps())
        stps.extend([
            {
                'run': bundler_builder + ' extract %s %s ${{github.run_number}}' %
                ('~/artifacts/logs', db_path)
            },
            self._gen_install_transfer_step(),
            self._gen_upload_file_step(db_path, 'db'),
        ])
        job['steps'] = stps
        return job

    def __init__(self):
        self.branches = ['python']
        # self.own_token = '${{secrets.RELEASE_TOKEN}}'
        self.bot_token = '${{ secrets.GITHUB_TOKEN }}'
        self.opde_dir = '${{github.workspace}}'
        self.cache_apt = '%s/cache/apt' % self.opde_dir
        self.cache_python = '%s/cache/python' % self.opde_dir
        self.hash_apt = "${{ hashFiles('./cache/apt.list.txt') }}"
        self.hash_python = "${{ hashFiles('./poetry.lock') }}"
        self.hash_openwrt_path = "./cache/openwrt.hash.json"
        self.hash_openwrt = "${{ hashFiles('%s') }}" % self.hash_openwrt_path
        self.builder = 'poetry run python3 builder.py'
        self.worker_num = 20
        data = {}

        data['name'] = 'Python'
        data['on'] = {
            'push': {
                "branches": self.branches
            }
        }
        data['jobs'] = {
            'APT': self.apt_job(),
            'BASE': self.sdk_job(),
            'WORKER': self.worker_job(),
            'BUNDLE': self.bundle_job(),
        }
        data['jobs']['BASE']['needs'] = 'APT'
        data['jobs']['WORKER']['needs'] = ['BASE', 'APT']
        data['jobs']['BUNDLE']['needs'] = ['BASE', 'APT', 'WORKER']
        self.data = data
        pass


work_flow = WorkFlow()
# print(json.dumps(work_flow.data, indent=2))
# pprint(work_flow.data)
ctx = yaml.dump(work_flow.data)
ctx = re.sub(r'[-] 08', "- '08'", ctx)
ctx = re.sub(r'[-] 09', "- '09'", ctx)
print(ctx)
Path(__file__).parent.parent.joinpath(
    '.github/workflows/python.yml').write_text(ctx)
