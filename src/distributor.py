from pathlib import Path
from .worker import BuildWorkerPyramid
import networkx as nx
import json
import sys


class DependsTree():
    '''
    Packages dependence tree
    build from targetinfo and packageinfo ast
    '''

    _default_cost = 1

    dg = nx.DiGraph()

    packageInfoAst: object
    leaf_nodes: list
    # node names through list
    names: list

    def draw(self):
        import matplotlib.pyplot as plt
        plt.subplot(111)
        nx.draw_shell(self.dg, with_labels=True, font_weight='normal',
                      font_size=10, node_color="#F4D03F")

    def _build_dag(self):
        '''
        build depends graph from packageinfo ast, this is dag
        '''
        for makefile in self.packageInfoAst:
            for pack in makefile['packages']:
                # self.dg.add_node(pack['Package'])
                # weight: build(compiled) time
                self.dg.add_node(pack['Package'], pack=pack,
                                 makefile=makefile, cost=self._default_cost)
                for dep in pack['Depends']:
                    # TODO: more depends
                    if dep[0] == 'DEPENDS_SELECT_OTH' or dep[0] == 'DEPENDS_WAIT_OTH_SELECTED':
                        self.dg.add_node(dep[1], cost=self._default_cost)
                        self.dg.add_edge(pack['Package'], dep[1])
                    # if dep[0] == 'DEPENDS_SELECT_OTH_IF': # TODO: check condiction
                    #     self.dg.add_node(dep[2])
                    #     self.dg.add_edge(pack['Package'],dep[2])
        # pprint(dep)
        # print(self.dg.nodes().data())
        idx = 0
        self.names = []
        for node in self.dg.nodes():
            # record index in each node for reverse-quering
            self.dg.add_node(node, numid=idx)
            self.names.append(node)
            idx += 1
        # print(self.dg['base-files'])
        if not nx.is_directed_acyclic_graph(self.dg):
            print('Ring detect! This is not DAG!!', file=sys.stderr)

    def to_json(self):
        '''
        output json to represent dag
        '''
        ans = {
            'nodes': [],
            'edges': []
        }
        for node in self.dg.nodes():
            data = self.dg.nodes[node]
            ans['nodes'].append(
                {'name': node, 'cost': data['cost'], 'id': data['numid']})
        for edge in self.dg.edges():
            ans['edges'].append(
                {'from': self.dg.nodes[edge[0]]['numid'], 'to': self.dg.nodes[edge[1]]['numid']})
        return json.dumps(ans, indent=2)

    def build(self, packageInfoAst):
        self.packageInfoAst = packageInfoAst
        self._build_dag()


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
