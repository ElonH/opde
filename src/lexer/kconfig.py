from ply.lex import TOKEN
from src.lexer.common import InfoLexer


class KconfigLexer(InfoLexer):
    '''
    a lexer for kernel config
    '''

    # Declare the state
    states = (
        ('variable', 'inclusive'),
        ('value', 'inclusive'),
    )

    # List of token names.   This is always required
    tokens = (
        'EOL',
        'CONFIG',
        'TYPE',
        'DEFAULT',
        'SYM',
        'VALUE'
    )

    t_TYPE = r'(bool|string|int|tristate)'

    # Define a rule so we can track line numbers
    def t_EOL(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        return t

    def t_CONFIG(self, t):
        r'config'
        t.lexer.push_state('variable')
        return t

    def t_variable_SYM(self, t):
        r'[a-zA-z\d\-_.]+'
        t.value = t.value.strip('"')
        t.lexer.pop_state()
        return t

    @TOKEN(r'default')
    def t_DEFAULT(self, t):
        t.lexer.push_state('value')
        return t

    def t_value_VALUE(self, t):
        r'([a-zA-z\d]+|"[^(\")]*")'
        t.value = t.value.strip('"')
        t.lexer.pop_state()
        return t

    # A string containing ignored characters
    t_ignore = ' \t'

    # Error handling rule
    def t_error(self, t):
        raise BaseException("Illegal character \n%s" % t.value[0:100])
