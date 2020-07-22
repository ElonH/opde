from ..lexer.targetinfo import TargetInfoLexer
import ply.yacc as yacc


class TargetInfoParser():
    'parser of .targetinfo'
    tokens = TargetInfoLexer.tokens
    lexer: TargetInfoLexer
    parser: yacc.LRParser

    # Build the lexer
    def build(self, lexer: TargetInfoLexer, **kwargs):
        self.lexer = lexer
        self.parser = yacc.yacc(
            module=self, tabmodule="targetParseTab", debugfile="targetParse.out", **kwargs)

    def gen_ast(self, data: str):
        return self.parser.parse(input=data, lexer=self.lexer)

    precedence = ()

    start = 'archs'

    def p_empty(self, p):
        'empty :'

    def p_bind_params(self, p):
        '''
        kv      : DERIVATE PARAMS
                | TARGETFEATURES packs
                | DEFAULTPACKAGES packs
                | TARGETPROFILEPACKAGES packs
        targetid  : TARGETID PARAMS
        source  : SOURCE PARAMS
        profileid : PROFILEID PARAMS
        '''
        p[0] = {p[1]: p[2]}

    def p_pack(self, p):
        '''
        properties : kv kv
                   | properties kv
                   | properties DELIMITER
        targetComb : targetid properties
        '''
        p[0] = dict()
        for i in range(1, len(p)):
            if p[i] == '@@':
                continue
            p[0].update(p[i])
        # print(p[0])

    def p_arch(self, p):
        '''
        arch       : source targetComb subtargets
                   | source targetComb profiles1 subtargets
        '''
        #    | source targetComb profiles
        p[0] = dict()
        p[0].update(p[1])
        p[0].update(p[2])
        if len(p) > 4:
            p[0]['profiles'] = p[3]
            p[0]['subtargets'] = p[4]
        else:
            p[0]['subtargets'] = p[3]

    def p_arch2(self, p):
        '''
        arch       : source targetComb profiles1
                   | source targetComb profiles0
        '''
        p[0] = dict()
        p[0].update(p[1])
        p[0].update(p[2])
        p[0]['profiles'] = p[3]

    def p_subtar(self, p):
        '''
        subtar     : targetComb profiles1
                    | targetComb profiles0
        '''
        p[0] = dict()
        p[0].update(p[1])
        p[0]['profiles'] = p[2]

    def p_profile(self, p):
        'profile    : profileid properties'
        p[0] = dict()
        p[0].update(p[1])
        p[0].update(p[2])

    def p_listInit(self, p):
        '''
        archsext : arch
        subtargetsext : subtar
        packsext : ITEM
        profilesext : profile
        '''
        if len(p) == 3:
            p[0] = [p[1], p[2]]
        else:
            p[0] = [p[1]]

    def p_listAppend(self, p):
        '''
        archsext : archsext arch
        subtargetsext : subtargetsext subtar
        packsext      : packsext ITEM
        profilesext   : profilesext profile
        '''
        p[0] = p[1] + [p[2]]

    def p_listEnd(self, p):
        '''
        packs : packsext ITEMEND
              | ITEMEND
        archs : archsext
        subtargets  : subtargetsext
        profiles1   : profilesext
        profiles0   : empty
        '''
        if len(p) == 2 or len(p) == 3:
            p[0] = p[1]
        else:
            p[0] = []

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
