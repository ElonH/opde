
import ply.yacc as yacc
from ..lexer.kconfig import KconfigLexer


class KconfigParser(KconfigLexer):
    'parser of kernel config'

    def __init__(self, **kwargs):
        super(KconfigParser, self).__init__(**kwargs)
        self.parser = yacc.yacc(
            module=self, tabmodule="kconfParseTab", debugfile="kconfParse.out", **kwargs)

    def gen_ast(self, data: str):
        return self.parser.parse(input=data, lexer=self.lexer)

    precedence = ()

    start = 'root'

    def p_list(self, p):
        '''
        root : config
             | root config
        '''
        if len(p) == 3:
            # print(p[1], p[2])
            p[1].append(p[2])
            p[0] = p[1]
        else:
            p[0] = [p[1]]
            # print(p[1])

    def p_config(self, p):
        '''
        config : CONFIG SYM EOL TYPE EOL properities
        '''
        p[0] = dict()
        p[0]['type'] = p[1]
        p[0]['sym'] = p[2]
        p[0]['value-type'] = p[4]
        p[0].update(p[6])

    def p_dict(self, p):
        '''
        properities : properity
                    | properities properity
        '''
        p[0] = p[1]
        if len(p) == 3:
            p[1].update(p[2])

    def p_properity(self, p):
        '''
        properity : DEFAULT VALUE EOL
        '''
        p[0] = dict()
        p[0][p[1]] = p[2]

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
