
import ply.yacc as yacc
from ..lexer.packageinfo import PackageInfoLexer


class PackageInfoParser(PackageInfoLexer):
    'parser of .packageinfo'

    # Build the lexer
    def __init__(self, **kwargs):
        super(PackageInfoParser, self).__init__(**kwargs)
        self.parser = yacc.yacc(
            module=self, tabmodule="packageParseTab", debugfile="packageParse.out", **kwargs)

    def gen_ast(self, data: str):
        return self.parser.parse(input=data, lexer=self.lexer)

    precedence = ()

    start = 'root'

    def p_list_init(self, p):
        '''
        root : source
             | root source
        packs : pack
              | packs pack
        depsext : depend
             | depsext depend
        confx : configItem
              | confx configItem
        helpx : CONFIG_HELP_LINE
              | helpx CONFIG_HELP_LINE
        providx : PROVIDES_ITEM
              | providx PROVIDES_ITEM
        '''
        if len(p) == 3:
            p[0] = p[1] + [p[2]]
        else:
            p[0] = [p[1]]

    def p_list_end(self, p):
        '''
        deps   : depsext DEPENDS_END
        helpdoc : helpx CONFIG_HELP_END
        provides : providx PROVIDES_END
        '''
        p[0] = p[1]

    def p_list_singular(self, p):
        '''
        deps : DEPENDS_END
        helpdoc : CONFIG_HELP_END
        provides : PROVIDES_END
        '''
        p[0] = []

    def p_bundle(self, p):
        '''
        properties : kv
                    | properties kv
        sourceComb : sourceid properties
                   | sourceid
        packageComb : packageid properties
                    | packageid properties configComb
        '''
        p[0] = dict()
        for i in range(1, len(p)):
            if p[i] == '@@':
                continue
            p[0].update(p[i])

    def p_kv(self, p):
        '''
        kv : DERIVATE PARAMS
           | DESCRIPTION PARAMS DELIMITER
           | PROVIDES provides
           | DEPENDS deps
        sourceid : SOURCE PARAMS
        packageid : PACKAGEID PARAMS
        configComb : CONFIG confx DELIMITER
        configItem : CONFIG_ITEM PARAMS
                   | CONFIG_HELP helpdoc
        '''
        #    CONFIG_HELP_LINE
        p[0] = {p[1]: p[2]}
        # print(p[0])

    def p_source(self, p):
        '''
        source : sourceComb packs
        '''
        p[0] = dict()
        p[0].update(p[1])
        p[0]['packages'] = p[2]

    def p_pack(self, p):
        '''
        pack : packageComb
        '''
        p[0] = dict()
        p[0].update(p[1])
        # p[0]['config'] = p[2]

    def p_depend(self, p):
        '''
        depend : DEPENDS_SELECT_OTH
               | DEPENDS_SELECT_OTH_IF
               | DEPENDS_WAIT_SYMBOL
               | DEPENDS_WAIT_OTH_SELECTED
               | DEPENDS_WAIT_OTH_SELECTED_IF
               | DEPENDS_SELECT_SYMBOL
        '''
        p[0] = p[1]

    def p_error(self, t):
        print("Syntax error at \n%s" % t)
        if not t:
            print("End of File!")
            return
        # Read ahead looking for a closing '}'
        for _ in range(1, 10):
            tok = self.parser.token()             # Get the next token
            print(tok)
            if not tok:
                break
        # print(self.parser.__dir__())
        print(self.parser.state)
        raise
        # self.parser.errok()
