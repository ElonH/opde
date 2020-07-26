
import ply.yacc as yacc
from ..lexer.logs import LogLexer
import re


class LogParser(LogLexer):
    'parser of logs/**.txt'

    # Build the lexer
    def __init__(self, **kwargs):
        super(LogParser, self).__init__(**kwargs)
        self.parser = yacc.yacc(
            module=self, tabmodule="logParseTab", debugfile="logParse.out", **kwargs)

    def gen_ast(self, data: str):
        return self.parser.parse(input=data, lexer=self.lexer)

    precedence = ()

    start = 'root'

    def p_all(self, p):
        '''
        root : DETAIL info
             | info
        '''
        p[0] = dict()
        if len(p) == 3:
            p[0]['detail'] = p[1]
            p[0].update(p[2])
        else:
            p[0]['detail'] = ''
            p[0].update(p[1])

    def p_info(self, p):
        '''
        info : CMDARRAY CODEANDTIME
        '''
        p[0] = dict()
        p[0].update(p[2])
        ary = re.findall("'(.*?)'", p[1])
        p[0]['subdir'] = ary[0]
        p[0]['target'] = ary[1]
        p[0]['build-type'] = ary[2]
        p[0]['build-variant'] = ary[3]

    # def p_source(self, p):
    #     '''
    #     source : sourceComb packs
    #     '''
    #     p[0] = dict()
    #     p[0].update(p[1])
    #     p[0]['packages'] = p[2]

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
