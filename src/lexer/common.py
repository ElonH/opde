import ply.lex as lex


class InfoLexer():
    '''
    a common lexer
    '''

    # Build the lexer
    def __init__(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Test it output
    def test(self, row_data: str):
        'Test it output'
        self.lexer.input(row_data)
        self.lexer.lineno = 1
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)

    def testSlient(self, row_data: str):
        'Test it output'
        self.lexer.input(row_data)
        self.lexer.lineno = 1
        while True:
            tok = self.lexer.token()
            if not tok:
                break

    def saveTo(self, row_data: str, path: str):
        'Save tokens to somewhere'
        self.lexer.input(row_data)
        self.lexer.lineno = 1
        with open(path, 'w') as f:
            while True:
                tok = self.lexer.token()
                if not tok:
                    break
                f.write('%s\n' % tok)
