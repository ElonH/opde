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
            "uses": "mxschmitt/action-tmate@v1",
            "if": "always()"
        }

    @classmethod
    def _gen_cache_step(cls, path: str, key: str, step_id: str = None):
        'cache step'
        stp = {}
        if step_id:
            stp['id'] = step_id
        # refs: https://help.github.com/en/actions/configuring-and-managing-workflows/caching-dependencies-to-speed-up-workflows
        stp['uses'] = 'actions/cache@v1'
        stp['with'] = {
            'path': path,
            'key': key
        }
        return stp

    @classmethod
    def _hit_cached(cls, step_id: str, rst: bool = True):
        'a condition of hit cache'
        ans = "steps.%s.outputs.cache-hit == 'true'" % step_id
        if not rst:
            ans = "steps.%s.outputs.cache-hit != 'true'" % step_id
        return ans

    @classmethod
    def _gen_var_step(cls, kv: object):
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

    def apt_job(self):
        'cache apt'
        job_apt = self._gen_empty_job()
        stps: list = self._gen_empty_steps()
        job_apt['outputs'] = {
            "dateDot": self._in_var('var', 'dateDot'),
            "dateDash": self._in_var('var', 'dateDash'),
            "tag": self._in_var('var', 'tag'),
        }
        stps.extend([
            # {'run': '[[ "${{secrets.RELEASE_TOKEN}}" ]] || false'},
            {
                'id': 'var',
                'run': self._gen_var_step({
                    'dateDot': "$(date +'%y.%m')",
                    'dateDash': "$(date +'%y-%m')",
                    'tag': "v$dateDot.${{github.run_number}}"
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
                'if': "%s || %s" % (self._hit_cached('cache-apt', False), self._hit_cached('cached-python', False)),
                'run': r'''
                    docker rmi $(docker images -q)
                    sudo -E apt-get remove -y --purge azure-cli ghc zulu* hhvm llvm* firefox google* dotnet* powershell openjdk* mysql* php*
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
                    '''
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
        job_apt['steps'] = stps
        return job_apt

    def _opde_init_steps(self):
        'initilize opde common environment'
        return [
            self._gen_cache_step(
                self.cache_apt,
                "apt-%s-%s" % (self._out_var('APT', 'dateDash'), self.hash_apt),
            ),
            {
                'env': {'DEBIAN_FRONTEND': 'noninteractive'},
                'run': r'''
                    docker rmi $(docker images -q)
                    sudo -E apt-get -yq remove --purge azure-cli ghc zulu* hhvm llvm* firefox google* dotnet* powershell openjdk* mysql* php*
                    sudo -E apt-get -yq update || ( sleep 1m && sudo -E apt-get update -y) || ( sleep 1m && sudo -E apt-get update -y)
                    sudo -E apt-get -yq autoremove --purge
                    sudo -E apt-get -yq clean
                    sudo -E rm -rf /usr/share/dotnet /etc/mysql /etc/php
                    sudo -E apt-get -yq install apt-offline
                    APT_PACKS=($(tr '\n' ' ' < ./cache/apt.list.txt))
                    # https://blog.sleeplessbeastie.eu/2014/01/30/how-to-manage-packages-on-an-off-line-debian-system/
                    # --allow-unauthenticated
                    sudo -E apt-offline install ./cache/apt/opde-bundle.zip --skip-bug-reports --skip-changelog
                    sudo -E apt-get -yq upgrade
                    sudo -E apt-get -yq install ${APT_PACKS[@]}
                    sudo -E ln -sf /usr/bin/gcc-8 /usr/bin/gcc
                    sudo -E ln -sf /usr/bin/g++-8 /usr/bin/g++
                    # https://github.com/project-openwrt/openwrt-isco/issues/181
                    sudo -E ln -sf /usr/include/asm-generic /usr/include/asm
                    '''
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

    def sdk_job(self):
        'building sdk, imagebuilder and firmware'
        job_apt = self._gen_empty_job()
        stps: list = self._gen_empty_steps()
        stps.extend(self._opde_init_steps())
        db_path = '%s/logs.db.json' % self._in_var('sdk-var', 'logs')
        stps.extend([
            {'run': 'git submodule update --init --recursive'},
            {'run': self.builder + ' init'},
            {'run': self.builder + ' feeds'},
            {'run': self.builder + ' config -sdk -ib -ke'},
            self._gen_cache_step(
                './cache/openwrt',
                # TODO: extract a packs hash metadata from packageinfo
                "openwrt-sdk-test-${{needs.APT.outputs.dateDash}}",
                'cache-openwrt'
            ),
            {
                'if': self._hit_cached('cache-openwrt', False),
                'run': self.builder + ' download'
            },
            {'run': self.builder + ' build'},
            {
                'id': 'sdk-var',
                'run': self._gen_var_step({
                    'openwrt': '$(%s @output opdir)' % self.builder,
                    'logs': '$(%s @output logdir)' % self.builder,
                    'sdk-path': '$(find ${openwrt}/bin -name "*sdk*")',
                    'image-builder-path': '$(find ${openwrt}/bin -name "*imagebuilder*")',
                })
            },
            {
                'run': self.builder + ' extract %s %s ${{github.run_number}}' %
                (self._in_var('sdk-var', 'logs'), db_path)
            },
            {'run': self.builder + ' check %s ${{github.run_number}})' % db_path},
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
            {
                'id': 'sdk-var2',
                'run': self._gen_var_step({
                    'openwrt': '$(%s @output opdir)' % self.builder,
                    'sdk-path': '$(find ${openwrt}/bin -name "*sdk*")',
                    'image-builder-path': '$(find ${openwrt}/bin -name "*imagebuilder*")',
                })
            },
            self._gen_upload_artifact_step(
                'SDK', self._in_var('sdk-var2', 'sdk-path')),
            self._gen_upload_artifact_step(
                'ImageBuilder', self._in_var('sdk-var2', 'image-builder-path')),
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
                    sdk=self._in_var('sdk-var2', 'sdk-path'),
                    ib=self._in_var('sdk-var2', 'image-builder-path')
                )
            },
            self._gen_upload_artifact_step(
                'Firmware', self._in_var('sdk-var', 'openwrt') + '/bin/targets'),
            {
                'working-directory': self._in_var('sdk-var', 'openwrt'),
                'run': '''rm bin/targets -rf\ntar -xf tmp.tar'''
            },
            self._gen_upload_artifact_step(
                'Packages-base', self._in_var('sdk-var', 'openwrt') + '/bin'),
            # collect all openwrt's source bundles
            {
                'if': self._hit_cached('cache-openwrt', False),
                'run': self.builder + ' config -sdk -ib -ke -a\n' +
                self.builder + ' download'
            },
            # self._gen_debugger_step(),
        ])
        job_apt['steps'] = stps
        return job_apt
        pass

    def __init__(self):
        self.branches = ['python']
        # self.own_token = '${{secrets.RELEASE_TOKEN}}'
        self.bot_token = '${{ secrets.GITHUB_TOKEN }}'
        self.opde_dir = '${{github.workspace}}'
        self.cache_apt = '%s/cache/apt' % self.opde_dir
        self.cache_python = '%s/cache/python' % self.opde_dir
        self.hash_apt = "${{ hashFiles('./cache/apt.list.txt') }}"
        self.hash_python = "${{ hashFiles('./poetry.lock') }}"
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
            'SDK': self.sdk_job(),
        }
        data['jobs']['SDK']['needs'] = 'APT'
        self.data = data
        pass


work_flow = WorkFlow()
# print(json.dumps(work_flow.data, indent=2))
# pprint(work_flow.data)
print(yaml.dump(work_flow.data))
Path(__file__).parent.parent.joinpath(
    '.github/workflows/python.yml').write_text(yaml.dump(work_flow.data))
