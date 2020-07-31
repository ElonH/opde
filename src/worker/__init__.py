from pathlib import Path
from ..utils import run


_worked_inited = False


def __init__():
    if _worked_inited:
        return
    SRC_dir = Path(__file__).parent
    BLD_dir = SRC_dir.joinpath('build')
    cmd = ' '.join([
        "cmake -DCMAKE_EXPORT_COMPILE_COMMANDS:BOOL=TRUE", "-DCMAKE_BUILD_TYPE:STRING=DEBUG",
        "-H%s" % SRC_dir.as_posix(),
        "-B%s" % BLD_dir.as_posix()])
    print(cmd)
    run(cmd)
    cmd = 'make -C %s' % BLD_dir.as_posix()
    print(cmd)
    run(cmd)


def BuildWorkerPyramid(tree_json_path: str, output_path: str):
    __init__()
    exec_bin = Path(__file__).parent.joinpath('build', 'BuildWorkerPyramid')
    run('%s "%s" "%s"' % (exec_bin.as_posix(), tree_json_path, output_path))
