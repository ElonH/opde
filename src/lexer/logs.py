from ply.lex import LexToken, TOKEN
from src.lexer.common import InfoLexer
import re


class LogLexer(InfoLexer):
    '''
    a lexer for file logs/**.txt
    '''

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters
    t_ignore = ''

    def t_DETAIL(self, t):
        r'(.|\n)+(?=(\ntime: [^\n]+?$))'
        t.lexer.lineno += t.value.count('\n')
        # print(t)
        return t

    # Error handling rule
    def t_error(self, t):
        print("Illegal character \n%s" % t.value[0:100])
        raise
        # t.lexer.skip(1)

    # Declare the state
    states = (
        ('time', 'inclusive'),
    )

    # List of token names.   This is always required
    tokens = (
        'CMDARRAY',
        'DETAIL',
        'CODEANDTIME'
    )

    def t_TIME(self, t: LexToken):
        r'time: '
        t.lexer.push_state('time')

    def t_time_array(self, t: LexToken):
        r'.*? \[.*\]'
        t.type = 'CMDARRAY'
        t.value = re.findall(r'\[.*\]', t.value)[0]
        # print(t)
        return t

    def t_time_codeandtime(self, t: LexToken):
        r'(\#[0-9.]*){4}'
        t.type = 'CODEANDTIME'
        array = re.findall(r'[0-9.]+', t.value)
        t.value = {
            'exit-code': int(array[0]),
            'user-time': float(array[1]),
            'system-time': float(array[2]),
            'time': float(array[3]),
        }
        # print(t)
        t.lexer.pop_state()
        return t

    t_time_ignore = ' '
