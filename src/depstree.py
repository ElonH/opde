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
                self.dg.add_node(pack['Package'], pack=pack,
                                 makefile=makefile, type=pack['Type'], cost=0)
                # TODO: parse provides
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
            self.dg.add_node(source, type='source',
                             cost=self._default_cost, makefile=makefile)
            variants = set()
            packs = set()
            for pack in makefile['packages']:
                packs.add(pack['Package'])
                if 'Build-Variant' in pack and pack['Build-Variant'] != '':
                    variant = Path(source).joinpath(
                        pack['Build-Variant']).as_posix()
                    variants.add(variant)
                    self.dg.add_node(variant, makefile=makefile,
                                     type='variant', cost=self._default_cost)
                    # self.dg.nodes[source]['cost'] = 0
                    self.dg.add_edge(variant, pack['Package'])
                else:
                    self.dg.add_edge(source, pack['Package'])
                # if 'Build-Variant' not in pack and pack['Provides'] != '':
                #     print(pack['Package'])
            # debug only
            # n1 = 'wpa-supplicant-mesh-wolfssl'
            # n2 = 'package/network/services/hostapd'
            # if self.dg.has_edge(n1, n2):
            #     raise BaseException('1')
            # source depends on variants
            for variant in variants:
                self.dg.add_edge(source, variant)
            # if self.dg.has_edge(n1,n2):
            #     raise BaseException('2')
            for pack in makefile['packages']:
                for edge in self.dg.in_edges(pack['Package']):
                    # avoid to create cycle path
                    if (edge[0] == source) | (edge[0] in variants) | (edge[0] in packs):
                        continue
                    if 'Build-Variant' in pack and pack['Build-Variant'] != '':
                        variant = Path(source).joinpath(
                            pack['Build-Variant']).as_posix()
                        if self.dg.has_edge(variant, edge[0]):
                            continue
                        self.dg.add_edge(edge[0], variant)
                        # if self.dg.has_edge(n1,n2):
                        #     raise BaseException('4')
                    else:
                        if self.dg.has_edge(source, edge[0]):
                            continue
                        self.dg.add_edge(edge[0], source)
                        # if self.dg.has_edge(n1,n2):
                        #     raise BaseException('5')
            # if self.dg.has_edge(n1,n2):
            #     raise BaseException("3")
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
