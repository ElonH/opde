from ..bash import run
from git import Repo
from pathlib import Path

_patches_dir = Path(__file__).parent.absolute()

_patches = [_patches_dir.joinpath(name) for name in [
    'export-some-info-to-logs.patch',
    'export-packages-hash.patch'
]]

# patch not workaround in SDK Archive
_sdk_patches = [_patches_dir.joinpath(name) for name in ['hack-sdk.patch']]


def patchOpenwrt(repo_path: str, mode: str, dry=False):
    'patch to openwrt source to export some necessery infomation'
    p = Path(repo_path).absolute()
    patches = []
    patches.extend(_patches)
    if mode == 'BASE':
        patches.extend(_sdk_patches)
    for i in patches:
        if dry:
            print('patch -d %s -p1 -f --dry-run < %s' %
                  (p.as_posix(), i.as_posix()))
            run('patch -d %s -p1 -f --dry-run < %s' %
                (p.as_posix(), i.as_posix()))
        else:
            run('patch -d %s -p1 -f < %s' % (p.as_posix(), i.as_posix()))


def revertPatchOpenwrt(repo_path: str, mode: str, dry=False):
    'revert patch to openwrt source'
    p = Path(repo_path).absolute()
    patches = []
    patches.extend(_patches)
    if mode == 'BASE':
        patches.extend(_sdk_patches)
    for i in patches:
        if dry:
            print('patch -d %s -p1 -R -f --dry-run < %s' %
                  (p.as_posix(), i.as_posix()))
            run('patch -d %s -p1 -R -f --dry-run < %s' %
                (p.as_posix(), i.as_posix()))
        else:
            run('patch -d %s -p1 -R -f < %s' % (p.as_posix(), i.as_posix()))
