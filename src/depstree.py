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
    # node names through list
    names: list

    def draw(self):
        'draw dag, very slow, not recommand'
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
        for node in self.dg.nodes():
            # record index in each node for reverse-quering
            self.dg.add_node(node, numid=idx)
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
        'build tree'
        self.packageInfoAst = packageInfoAst
        self._build_dag()
