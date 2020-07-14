from ply.lex import LexToken, TOKEN
from .common import InfoLexer


class TargetInfoLexer(InfoLexer):
    '''
    a lexer for file tmp/.targetinfo
    '''

    # A regular expression rule with some action code
    # Note addition of self parameter since we're in a class

    t_DELIMITER = r'@@'

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore = ' \t'

    # Error handling rule
    def t_error(self, t):
        print("Illegal character \n%s" % t.value[0:100])
        raise
        # t.lexer.skip(1)

    def t_end2line_string(self, t):
        r'(.*)\n'
        t.value = [t.lexer.lexdata[t.lexer.line_start:t.lexer.lexpos - 1]]
        t.lexer.lineno += t.value[0].count('\n') + 1
        if len(t.value[0]) != 0:
            t.value[0] = t.value[0][1:]
        t.type = "PARAMS"
        t.lexer.pop_state()
        return t

    # A string containing ignored characters (spaces and tabs)
    t_end2line_ignore = ''

    # Error handling rule
    def t_end2line_error(self, t):
        t.lexer.skip(1)

    def t_DESCRIPTION(self, t: LexToken):
        r'Target(\-Profile)?\-Description'
        t.lexer.doc_start = t.lexer.lexpos
        t.type = "DERIVATE"
        t.lexer.push_state('end2aa')
        return t

    def t_end2aa_string(self, t):
        r'(?:(?!@@)(.|\r|\n))+'
        t.value = [t.lexer.lexdata[t.lexer.doc_start + 1:t.lexer.lexpos]]
        t.lexer.lineno += t.value[0].count('\n')
        if len(t.value[0]) != 0:
            t.value[0] = t.value[0][1:]
        t.type = "PARAMS"
        t.lexer.begin('INITIAL')
        return t

    # A string containing ignored characters (spaces and tabs)
    t_end2aa_ignore = '\n'

    # Error handling rule
    def t_end2aa_error(self, t):
        t.lexer.skip(1)

    packageNameRule = r'[a-zA-Z-_\d.]+'
    # packageSymbolRule = r'([a-zA-Z-_\d.!()]|[|]{2}|[&]{2})+'
    packageItemRule = r'(?=[ \n])'

    def t_depends_exit(self, t):
        r'\n'
        t.lexer.pop_state()
        t.lexer.lineno += len(t.value)
        t.type = 'ITEMEND'
        return t

    @TOKEN(r'({}){}'.format(packageNameRule, packageItemRule))
    def t_depends_wait_other_selected(self, t):
        t.type = 'ITEM'
        # print([t.value])
        return t

    # A string containing ignored characters (spaces and tabs)
    t_depends_ignore = ' '

    # Error handling rule
    def t_depends_error(self, t):
        print("Illegal character \n%s" % t.value[0:100])
        print([t.value[0:100]])
        raise
        t.lexer.skip(1)

    # Declare the state
    states = (
        ('end2line', 'exclusive'),
        ('end2aa', 'exclusive'),
        # ('config', 'inclusive'),
        # ('helpline', 'exclusive'),
        ('depends', 'exclusive'),
    )

    # List of token names.   This is always required
    tokens = (
        'DERIVATE',
        'PARAMS',
        'SOURCE',
        'DELIMITER',
        'DEFAULTPACKAGES',
        'TARGETPROFILEPACKAGES',
        'TARGETFEATURES',
        'ITEM',  # <pkg>
        'ITEMEND',
        'TARGETID',
        'PROFILEID',
    )

    def t_DERIVATE(self, t: LexToken):
        r'(Target[-](Board|Name|Arch|Arch-Packages|Depends|Optimization)|Target[-]Profile([-](Priority|Name|hasImageMetadata|SupportedDevices|Default))|CPU-Type|Linux-(Version|Release|Kernel-Arch|Testing-Version)):'
        t.lexer.line_start = t.lexer.lexpos
        t.value = t.value[:-1]
        t.lexer.push_state('end2line')
        return t

    def t_TARGETID(self, t: LexToken):
        r'Target:'
        t.lexer.line_start = t.lexer.lexpos
        t.value = t.value[:-1]
        t.lexer.push_state('end2line')
        return t

    def t_PROFILEID(self, t: LexToken):
        r'Target[-]Profile:'
        t.lexer.line_start = t.lexer.lexpos
        t.value = t.value[:-1]
        t.lexer.push_state('end2line')
        return t

    def t_SOURCE(self, t: LexToken):
        r'Source[-]Makefile:'
        t.lexer.line_start = t.lexer.lexpos
        t.value = t.value[:-1]
        t.lexer.push_state('end2line')
        return t

    def t_DEFAULTPACKAGES(self, t: LexToken):
        r'Default[-]Packages:'
        t.lexer.push_state('depends')
        t.value = t.value[:-1]
        return t

    def t_TARGETPROFILEPACKAGES(self, t: LexToken):
        r'Target\-Profile\-Packages:'
        t.lexer.push_state('depends')
        t.value = t.value[:-1]
        return t

    def t_TARGETFEATURES(self, t: LexToken):
        r'Target\-Features:'
        t.lexer.push_state('depends')
        t.value = t.value[:-1]
        return t
