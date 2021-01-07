from pathlib import Path
from ..bash import run

_worked_inited = False
_BLD_dir = Path('/tmp/WorkerPyramid')

def __init__():
    if _worked_inited:
        return
    SRC_dir = Path(__file__).parent
    cmd = ' '.join([
        "cmake -DCMAKE_EXPORT_COMPILE_COMMANDS:BOOL=TRUE", "-DCMAKE_BUILD_TYPE:STRING=DEBUG",
        "-H%s" % SRC_dir.as_posix(),
        "-B%s" % _BLD_dir.as_posix()])
    print(cmd)
    run(cmd)
    cmd = 'make -C %s' % _BLD_dir.as_posix()
    print(cmd)
    run(cmd)
    # _worked_inited = True


def BuildWorkerPyramid(tree_json_path: str, output_path: str):
    __init__()
    exec_bin = _BLD_dir.joinpath('BuildWorkerPyramid')
    run('%s "%s" "%s"' % (exec_bin.as_posix(), tree_json_path, output_path))
