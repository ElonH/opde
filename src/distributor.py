from pathlib import Path
from .worker import BuildWorkerPyramid
import networkx as nx
import json
from .depstree import DependsTree


class WorksDistributor:
    '''
    Divide tasks
    '''

    def __init__(self):
        self.dg = nx.DiGraph()

    def build(self, tree_file: str, skip: bool = False):
        'build worker pyramid'
        tree_file = Path(tree_file)
        worker_file = tree_file.parent.joinpath('workers.pyramid.json')
        tree_dg = nx.readwrite.json_graph.jit_graph(
            tree_file.read_text(), create_using=nx.DiGraph())

        if not skip or (not tree_file.exists() and not tree_file.is_file()):
            BuildWorkerPyramid(tree_file.as_posix(), worker_file.as_posix())
        else:
            print('%s file exist, skip generation' % worker_file.as_posix())
        worker_dg = nx.readwrite.json_graph.jit_graph(
            worker_file.read_text(), create_using=nx.DiGraph())
        self.dg = nx.compose(tree_dg, worker_dg)

    def to_json(self):
        'output graph with jit json format data'
        return nx.readwrite.json_graph.jit_data(self.dg, indent=2)

    @property
    def boss(self):
        'return a worker at the top of worker-pyramid'
        for node in self.dg.nodes:
            if self.dg.in_degree(node) == 0:
                return node

    def deduce(self, n: int):
        '''
        jurisdiction is deduced from boss to n vice-bosses,
        depends tree will covered by jurisdictions of these vice-bosses
        vice-boss can be worker or type of depends node
        '''

        workers = [self.boss]
        vice_bosses = []
        while len(vice_bosses) + len(workers) != n:
            if len(workers) == 0:
                print('not enought worker, only %s' % len(vice_bosses))
                break
            node = workers[0]
            workers = workers[1:]
            data = self.dg.nodes[node]
            if data['type'] != 'worker':
                vice_bosses.append(node)
                continue
            # this is binary tree, edge counts: 0, 1 or 2
            for edge in self.dg.out_edges(node):
                workers.append(edge[1])
        return vice_bosses + workers

    def deduce_depends(self, n: int):
        '''
        simailar with deduce
        btw vice-boss type can not be worker
        so, use list to represant a vice-boss
        '''
        pre_bosses = self.deduce(n)
        post_bosses = []
        for boss in pre_bosses:
            replacer = []
            workers = [boss]
            while len(workers) != 0:
                node = workers[0]
                workers = workers[1:]
                if self.dg.nodes[node]['type'] != 'worker':
                    replacer.append(node)
                    continue
                for edge in self.dg.out_edges(node):
                    workers.append(edge[1])
            post_bosses.append(replacer)
        return post_bosses

    def deduce_depends_all(self, n: int):
        '''
        simailar with deduce_depends
        btw vice-boss will contain all depends node in its jurisdiction
        vice-boss type is list
        '''
        pre_bosses = self.deduce_depends(n)
        post_bosses = []
        for workers in pre_bosses:
            replacer = []
            for node in workers:
                if self.dg.nodes[node]['type'] == 'ipkg':
                    replacer.append(node)
                for child in nx.dfs_preorder_nodes(self.dg, node):
                    if self.dg.nodes[child]['type'] == 'ipkg':
                        replacer.append(child)
            post_bosses.append(list(set(replacer)))
        return post_bosses
