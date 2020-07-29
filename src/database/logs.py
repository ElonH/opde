
import tinydb
from tinydb.middlewares import CachingMiddleware
from tinydb.storages import JSONStorage


class LogsDb(tinydb.TinyDB):
    '''
    A database to storage build log
    Item
    {
        "exit-code": 0,
        "user-time": 0.46,
        "system-time": 0.28,
        "time": 3.74,
        "subdir": "package/utils/e2fsprogs",
        "target": "",
        "build-type": "",
        "build-variant": "compile",
        'arch': 'x86',
        'board': '64',
        'run-number': 123,
        'issue-id': 13432,
        'banned': False,
    }
    '''

    def __init__(self, db_path):
        super().__init__(db_path,
                         storage=CachingMiddleware(JSONStorage),
                         indent=2, separators=(',', ': '))

    @classmethod
    def query(cls, **kwargs):
        'generate common Query instance'
        Item = tinydb.Query()
        ans = ((Item.subdir == kwargs['subdir']) &
               (Item.target == kwargs['target']) &
               (Item['build-type'] == kwargs['build-type']) &
               (Item['build-variant'] == kwargs['build-variant']) &
               (Item.arch == kwargs['arch']) &
               (Item.board == kwargs['board']))
        # run_id = kwargs.pop('run-number', 0)
        # if run_id != 0:
        #     ans = (ans & (Item['run-number'] == run_id))
        return ans

    @classmethod
    def merge(cls, logAst: object, arch: str, board: str = None, run_number: int = 0):
        'merge everything together'
        ans = {}
        ans.update(logAst)
        ans['arch'] = arch
        ans['board'] = board
        ans['run-number'] = run_number
        return ans

    @classmethod
    def cost_func(cls, docs: list):
        'a function to caculate cost'
        cost = 0
        l = len(docs)
        for i in range(l):
            if docs[i]['exit-code'] != 0:
                continue
            #
            # lim(i=1,+\infinty) 1/1 + 1/2 + ... + 1/i < 2
            #
            cost += docs[i]['time'] / (l - i)
        return cost
