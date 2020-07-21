import sys
import subprocess as sp
from pathlib import Path


def in_notebook():
    try:
        from IPython import get_ipython
        if get_ipython() == None or 'IPKernelApp' not in get_ipython().config:  # pragma: no cover
            return False
    except ImportError:
        return False
    return True


def run(cmd: str, *args, **kwargs):
    '''
    run bash command
    '''
    if in_notebook():
        from IPython import get_ipython
        get_ipython().system('{cmd}')
    else:
        check = kwargs.pop('check', True)
        stdout = kwargs.pop('stdout', sys.stdout)
        stderr = kwargs.pop('stderr', sys.stderr)
        shell = kwargs.pop('shell', True)
        sp.run([cmd], check=check, stdout=stdout, stderr=stderr,
               shell=shell, *args, **kwargs)


def __init__():
    SRC_dir = Path(__file__).parent
    BLD_dir = SRC_dir.joinpath('build')
    cmd = ' '.join([
        "cmake -DCMAKE_EXPORT_COMPILE_COMMANDS:BOOL=TRUE", "-DCMAKE_BUILD_TYPE:STRING=Release",
        "-H%s" % SRC_dir.as_posix(),
        "-B%s" % BLD_dir.as_posix()])
    print(cmd)
    run(cmd)
    cmd = 'make -C %s' % BLD_dir.as_posix()
    print(cmd)
    run(cmd)


def BuildWorkerPyramid(tree_json_path: str, output_path: str):
    exec_bin = Path(__file__).parent.joinpath('build', 'BuildWorkerPyramid')
    run('%s "%s" "%s"' % (exec_bin.as_posix(), tree_json_path, output_path))


__init__()
