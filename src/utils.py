import sys
import subprocess as sp


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
        cwd = kwargs.pop('cwd', None)
        if cwd:
            cmd = "cd '%s' && %s" % (cwd, cmd)
        from IPython import get_ipython
        get_ipython().system('{cmd}')
    else:
        print(kwargs)
        check = kwargs.pop('check', True)
        stdout = kwargs.pop('stdout', sys.stdout)
        stderr = kwargs.pop('stderr', sys.stderr)
        shell = kwargs.pop('shell', True)
        executable = kwargs.pop('executable', '/bin/bash')
        sp.run([cmd], check=check, stdout=stdout, stderr=stderr, executable=executable,
               shell=shell, *args, **kwargs)
