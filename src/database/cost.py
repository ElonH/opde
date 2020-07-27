from pathlib import Path

import tinydb
from tinydb.middlewares import CachingMiddleware
from tinydb.storages import JSONStorage


class CostDb:
    'A database to storage packages cost'
    _default_db_path = Path(__file__).parent.joinpath('cost.db.json').as_posix()

    def __init__(self, db_path=_default_db_path):
        self.db = tinydb.TinyDB(db_path,
                                storage=CachingMiddleware(JSONStorage),
                                sort_keys=True, indent=2, separators=(',', ': '))

    def _Append(self, kv: object):
        'append result to list'
        def transform(doc: tinydb.table.Document):
            for key in ['exit-code', 'user-time', 'system-time', 'time']:
                doc.get(key).append(kv[key])
        return transform

    def query(self, logAst: object, arch: str, board: str = None):
        'generate Query instance'
        Item = tinydb.Query()
        return ((Item.subdir == logAst['subdir']) &
                (Item.target == logAst['target']) &
                (Item['build-type'] == logAst['build-type']) &
                (Item['build-variant'] == logAst['build-variant']) &
                (Item.arch == arch) &
                (Item.board == board))

    def upsert(self, logAst: object, arch: str, board: str = None):
        'update or insert an item'
        Item = self.query(logAst, arch, board)
        # print(Item)
        if not self.db.search(Item):
            self.db.insert({
                'subdir': logAst['subdir'],
                'target': logAst['target'],
                'build-type': logAst['build-type'],
                'build-variant': logAst['build-variant'],
                'arch': arch,
                'board': board,
                'exit-code': [logAst['exit-code']],
                'user-time': [logAst['user-time']],
                'system-time': [logAst['system-time']],
                'time': [logAst['time']],
            })
        else:
            self.db.update(self._Append(logAst), Item)

    def search(self, logAst: object, arch: str, board: str = None):
        'searching database'
        return self.db.search(self.query(logAst, arch, board))

    def cost(self, logAst: object, arch: str, board: str = None):
        'caculate cost'
        Item = self.query(logAst, arch, board)
        lst = self.db.search(Item)
        if not lst:
            return []
        costs = []
        for i in lst:
            cost = 0
            if i['exit-code'] == 0:
                for j in range(len(i['time'])):
                    # print(i['time'], j, len(i['time']))
                    cost += i['time'][j] / (len(i['time']) - j)
            costs.append(cost)
        return costs, lst

    def close(self):
        'close dabase'
        self.db.close()
