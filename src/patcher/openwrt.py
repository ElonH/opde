
from git import Repo
from pathlib import Path


def patchOpenwrt(repo_path: str, dry=False):
    'patch to openwrt source to export some necessery infomation'
    repo = Repo(repo_path)
    patches = [
        Path(__file__).parent.joinpath('export-some-info-to-logs.patch')
    ]
    for i in patches:
        if dry:
            repo.git.apply('--check', i)
            print('the patch is applicable to the openwrt source tree')
        else:
            repo.git.apply(i)
