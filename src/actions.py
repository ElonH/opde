import json
from pprint import pprint
from pathlib import Path
import yaml


def str_presenter(dumper, data):
    def is_multiline(s): return len(s.splitlines()) > 1
    # print(data, is_multiline(data))
    if is_multiline(data):  # check for multiline string
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
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

    def _gen_cache_step(self, path: str, key: str, step_id: str = None):
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

    def _gen_var_step(self, kv: object):
        'generate variable'
        ans = []
        for k in kv:
            ans.append(
                '{0}={1}\necho ${0}\necho "::set-output name={0}::${0}"'.format(
                    k, kv[k])
            )
        return '\n'.join(ans)

    def apt_job(self):
        'cache apt'
        job_apt = self._gen_empty_job()
        stps: list = self._gen_empty_steps()
        job_apt['outputs'] = {
            "dataDot": "${{ steps.var.outputs.dataDot }}",
            "dataDash": "${{ steps.var.outputs.dataDash }}",
            "tag": "${{ steps.var.outputs.tag }}",
        }
        stps.extend([
            # {'run': '[[ "${{secrets.RELEASE_TOKEN}}" ]] || false'},
            {
                'id': 'var',
                'run': self._gen_var_step({
                    'dataDot': "$(date +'%y.%m')",
                    'dataDash': "$(date +'%y-%m')",
                    'tag': "v$dataDot.${{github.run_number}}"
                })
            },
            self._gen_cache_step(
                './cache/apt',
                "apt-${{steps.var.outputs.dateDash}}-${{ hashFiles('./cache/apt.list.txt') }}",
                'cache-apt'
            ),
            self._gen_cache_step(
                './cache/python',
                "python-${{steps.var.outputs.dateDash}}-${{ hashFiles('./poetry.lock') }}",
                'cache-python'
            ),
            {
                'if': "steps.cache-apt.outputs.cache-hit != 'true' || steps.cache-python.outputs.cache-hit != 'true'",
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
sudo -E apt-offline install ./cache/apt/opde-bundle.zip --skip-bug-reports --skip-changelog # --allow-unauthenticated
sudo -E apt-get upgrade
sudo -E apt-get install ${APT_PACKS[@]}
'''
            },
            {
                'if': "steps.cache-python.outputs.cache-hit != 'true'",
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
                './cache/apt',
                "apt-${{needs.APT.outputs.dateDash}}-${{ hashFiles('./cache/apt.list.txt') }}"
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
sudo -E apt-offline install ./cache/apt/opde-bundle.zip --skip-bug-reports --skip-changelog # --allow-unauthenticated
sudo -E apt-get -yq upgrade
sudo -E apt-get -yq install ${APT_PACKS[@]}
sudo -E ln -sf /usr/bin/gcc-8 /usr/bin/gcc
sudo -E ln -sf /usr/bin/g++-8 /usr/bin/g++
sudo -E ln -sf /usr/include/asm-generic /usr/include/asm # https://github.com/project-openwrt/openwrt-isco/issues/181
'''
            },
            self._gen_cache_step(
                './cache/python',
                "python-${{needs.APT.outputs.dateDash}}-${{ hashFiles('./poetry.lock') }}",
            ),
            {
                'run': r'''
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
        stps.extend([
            {'run': 'git submodule update --init --recursive'},
            {'run': 'poetry run python3 builder.py init'},
            {'run': 'poetry run python3 builder.py feeds'},
            {'run': 'poetry run python3 builder.py config -sdk -ib -ke'},
            self._gen_cache_step(
                './cache/openwrt',
                # TODO: extract a packs hash metadata from packageinfo
                "openwrt-sdk-test-${{needs.APT.outputs.dateDash}}",
            ),
            {'run': 'poetry run python3 builder.py download'},
            {'run': 'poetry run python3 builder.py build'},
            {'run': 'poetry run python3 builder.py assign'},
            # collect all openwrt's source bundles
            {'run': 'poetry run python3 builder.py config -sdk -ib -ke -a'},
            {'run': 'poetry run python3 builder.py download'},
            # self._gen_debugger_step(),
        ])
        job_apt['steps'] = stps
        return job_apt
        pass

    def __init__(self):
        self.branches = ['python']
        # self.own_token = '${{secrets.RELEASE_TOKEN}}'
        self.bot_token = '${{ secrets.GITHUB_TOKEN }}'
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
