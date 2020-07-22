import networkx as nx
import json
import sys
from pathlib import Path


class DependsTree():
    '''
    Packages dependence tree
    build from targetinfo and packageinfo ast
    '''

    _default_cost = 1

    dg = nx.DiGraph()

    # node names through list
    names: list

    def draw(self):
        'draw dag, very slow, not recommand'
        import matplotlib.pyplot as plt
        plt.subplot(111)
        nx.draw_shell(self.dg, with_labels=True, font_weight='normal',
                      font_size=10, node_color="#F4D03F")

    def inject_package_info(self, packageInfoAst):
        '''
        build depends graph from packageinfo ast, this is dag
        '''
        for makefile in packageInfoAst:
            for pack in makefile['packages']:
                # self.dg.add_node(pack['Package'])
                # weight: build(compiled) time
                self.dg.add_node(pack['Package'], pack=pack,
                                 makefile=makefile, type=pack['Type'], cost=0)
                for dep in pack['Depends']:
                    # TODO: more depends
                    if dep[0] == 'DEPENDS_SELECT_OTH' or dep[0] == 'DEPENDS_WAIT_OTH_SELECTED':
                        self.dg.add_node(dep[1], cost=0)
                        self.dg.add_edge(pack['Package'], dep[1])
                    # if dep[0] == 'DEPENDS_SELECT_OTH_IF': # TODO: check condiction
                    #     self.dg.add_node(dep[2])
                    #     self.dg.add_edge(pack['Package'],dep[2])
        # some packages in same makefile are build in the same time, just like: golang, golang-doc, golang-src
        # let's make a virtual package to bundle together
        # TODO: consider condiction
        for makefile in packageInfoAst:
            source = Path(makefile['Source-Makefile']).parent.as_posix()
            # if source == 'package/libs/toolchain':
            # pprint(makefile)
            self.dg.add_node(source, type='source',
                             cost=self._default_cost, makefile=makefile)
            for pack in makefile['packages']:
                self.dg.add_edge(source, pack['Package'])
            for pack in makefile['packages']:
                for edge in self.dg.in_edges(pack['Package']):
                    # avoid to create cycle path
                    if edge[0] == source or self.dg.has_edge(source, edge[0]):
                        continue
                    self.dg.add_edge(edge[0], source)
        # pprint(dep)
        # print(self.dg.nodes().data())
        idx = 0
        for node in self.dg.nodes():
            # record index in each node for reverse-quering
            self.dg.add_node(node, numid=idx)
            idx += 1
        # print(self.dg['base-files'])
        if not nx.is_directed_acyclic_graph(self.dg):
            print('Ring detect! This is not DAG!!', file=sys.stderr)
            print(nx.find_cycle(self.dg))

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
