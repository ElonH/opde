from ..utils import run
from git import Repo
from pathlib import Path


_patches = [
    Path(__file__).parent.joinpath('export-some-info-to-logs.patch').absolute(),
    Path(__file__).parent.joinpath('export-packages-hash.patch').absolute(),
]
# patch not workaround in SDK Archive
_sdk_patches = [
    Path(__file__).parent.joinpath('hack-sdk.patch').absolute(),
]


def patchOpenwrt(repo_path: str, dry=False, sdk=True):
    'patch to openwrt source to export some necessery infomation'
    p = Path(repo_path).absolute()
    patches = []
    patches.extend(_patches)
    if sdk:
        patches.extend(_sdk_patches)
    for i in patches:
        if dry:
            print('patch -d %s -p1 -f --dry-run < %s' %
                  (p.as_posix(), i.as_posix()))
            run('patch -d %s -p1 -f --dry-run < %s' %
                (p.as_posix(), i.as_posix()))
        else:
            run('patch -d %s -p1 -f < %s' % (p.as_posix(), i.as_posix()))


def revertPatchOpenwrt(repo_path: str, dry=False, sdk=True):
    'revert patch to openwrt source'
    p = Path(repo_path).absolute()
    patches = []
    patches.extend(_patches)
    if sdk:
        patches.extend(_sdk_patches)
    for i in patches:
        if dry:
            print('patch -d %s -p1 -R -f --dry-run < %s' %
                  (p.as_posix(), i.as_posix()))
            run('patch -d %s -p1 -R -f --dry-run < %s' %
                (p.as_posix(), i.as_posix()))
        else:
            run('patch -d %s -p1 -R -f < %s' % (p.as_posix(), i.as_posix()))
