from pathlib import Path
from .worker import BuildWorkerPyramid
import networkx as nx
import json
from .depstree import DependsTree


class WorksDistributor:
    '''
    Divide tasks
    '''
    json_deps = Path('graph.json')
    json_workers = Path('workers.json')

    dg = nx.DiGraph()
    packs_transformer = {}
    boss: int
    root_packs: list = []

    def build(self, tree: DependsTree, skip: bool = False):
        'build worker pyramid'
        with open(self.json_deps, 'w') as f:
            f.write(tree.to_json())
        for pack in tree.dg.nodes():
            self.packs_transformer[tree.dg.nodes[pack]['numid']] = pack
        if not skip or (not self.json_workers.exists() and not self.json_workers.is_file()):
            BuildWorkerPyramid(
                self.json_deps.as_posix(), self.json_workers.as_posix())
        else:
            print('%s file exist, skip generation' %
                  self.json_workers.as_posix())
        with open(self.json_workers.as_posix(), 'r') as f:
            j = json.loads(f.read())
        for w in j:
            # print(w)
            self.dg.add_node(w['id'], totalCost=w['totalCost'])
            for to in w['out']:
                self.dg.add_edge(w['id'], to)
        for w in self.dg.nodes():
            # print(w, self.dg.in_degree(w))
            if self.dg.in_degree(w) == 0:
                self.boss = w
            if self.dg.out_degree(w) == 0:
                self.root_packs.append(w)

    def divide(self, num: int):
        '''
        divided into num tasks
        '''
        workers = []
        packs = []
        workers.append(self.boss)
        # workers.append(8655)
        while len(workers) < num:
            # print(workers)
            w = workers[0]
            workers = workers[1:]
            sub_worker = self.dg.out_edges(w)
            # print(sub_worker)
            if len(sub_worker) == 0:  # w is root packs
                packs.append([self.packs_transformer[w]])
                num -= 1
                continue
            for sub in sub_worker:
                # print(sub[1])
                workers.append(sub[1])
            # break
        # print(workers+packs)
        # print(len(workers+packs))
        for w in workers:
            packs_set = self.parseWorker(w)
            # print(packs_set)
            packs.append([self.packs_transformer[i] for i in packs_set])
        return packs

    def parseWorker(self, w: int):
        '''
        get all root packs which picked by worker w
        '''
        ans = []
        que = []
        que.append(w)
        while len(que) != 0:
            w = que[0]
            que = que[1:]
            sub_worker = self.dg.out_edges(w)
            if len(sub_worker) == 0:  # w is root packs
                ans.append(w)
                continue
            for sub in sub_worker:
                # print(sub[1])
                que.append(sub[1])
        return ans
