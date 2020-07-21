from ply.lex import LexToken, TOKEN
import re
from .common import InfoLexer


class PackageInfoLexer(InfoLexer):
    '''
    a lexer for file tmp/.packageinfo
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
        t.lexer.skip(1)

    def t_end2line_string(self, t):
        r'(.*)\n'
        t.value = t.lexer.lexdata[t.lexer.line_start:t.lexer.lexpos - 1]
        t.lexer.lineno += t.value.count('\n') + 1
        t.value = t.value[1:]
        t.type = "PARAMS"
        t.lexer.pop_state()
        return t

    # A string containing ignored characters (spaces and tabs)
    t_end2line_ignore = ''

    # Error handling rule
    def t_end2line_error(self, t):
        t.lexer.skip(1)

    def t_DESCRIPTION(self, t: LexToken):
        r'Description'
        t.lexer.doc_start = t.lexer.lexpos
        t.lexer.push_state('end2aa')
        return t

    def t_end2aa_string(self, t):
        r'(?:(?!@@)(.|\r|\n))+'
        t.value = t.lexer.lexdata[t.lexer.doc_start + 1:t.lexer.lexpos - 1]
        t.lexer.lineno += t.value.count('\n') + 1
        t.value = t.value[1:].splitlines(keepends=False)
        t.type = "PARAMS"
        t.lexer.begin('INITIAL')
        return t

    # A string containing ignored characters (spaces and tabs)
    t_end2aa_ignore = '\n'

    # Error handling rule
    def t_end2aa_error(self, t):
        t.lexer.skip(1)

    def t_DERIVATE(self, t: LexToken):
        r'((Submenu|Menu)[-]Depends|Build[-](Types|Depends|Variant|Only)|Kernel[-]Config|Build[-]Depends/host|Default[-]Variant|Prereq[-]Check|Require[-]User|Menu|Version|Conflicts|Provides|Section|Category|Repository|Title|Maintainer|Source|License|LicenseFiles|Type|Submenu|Default|Hidden|ABIVersion):'
        t.lexer.line_start = t.lexer.lexpos
        t.lexer.push_state('end2line')
        t.value = t.value[:-1]
        return t

    def t_SOURCE(self, t: LexToken):
        r'Source[-]Makefile:'
        t.lexer.line_start = t.lexer.lexpos
        t.lexer.push_state('end2line')
        t.value = t.value[:-1]
        return t

    def t_PACKAGEID(self, t: LexToken):
        r'Package:'
        t.lexer.line_start = t.lexer.lexpos
        t.lexer.push_state('end2line')
        t.value = t.value[:-1]
        return t

    def t_CONFIG(self, t: LexToken):
        r'Config:'
        t.lexer.doc_start = t.lexer.lexpos
        t.lexer.push_state('config')
        return t

    def t_config_exit(self, t: LexToken):
        r'@@'
        t.type = 'DELIMITER'
        t.lexer.pop_state()
        return t

    def t_config_item(self, t):
        r'(depends[ ]on|source|config|bool|default|menu|tristate|endmenu|comment|prompt|select|choice|endchoice|if|endif|string|int)'
        t.lexer.line_start = t.lexer.lexpos
        t.lexer.push_state('end2line')
        t.type = "CONFIG_ITEM"
        return t

    def t_config_comment(self, t):
        r'\#.*?\n'
        t.lexer.lineno += 1

    def t_config_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_config_ignore = ' |\t'

    # Error handling rule
    def t_config_error(self, t):
        print("Illegal character \n%s" % t.value[0:100])
        raise
        t.lexer.skip(1)

    def t_config_help(self, t: LexToken):
        r'(help|\-{3}help\-{3})\n'
        t.lexer.help_indent = None
        t.lexer.push_state('helpline')
        t.type = "CONFIG_HELP"
        t.value = t.value[0:-1]
        t.lexer.lineno += 1
        return t

    def t_helpline_line(self, t: LexToken):
        r'[ \t]*.+\n'
        if t.lexer.help_indent == None:
            t.lexer.help_indent = re.findall('^[ \t]*', t.value)[0]
        else:
            if not t.value.startswith(t.lexer.help_indent):
                t.lexer.skip(-len(t.value))
                t.lexer.pop_state()
                t.type = 'CONFIG_HELP_END'
                return t
        t.type = "CONFIG_HELP_LINE"
        t.lexer.lineno += 1
        return t

    def t_helpline_blank(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_helpline_ignore = ''

    # Error handling rule
    def t_helpline_error(self, t):
        print("Illegal character \n%s" % t.value[0:100])
        print([t.value[0:100]])
        raise
        t.lexer.skip(1)

    # Declare the state
    states = (
        ('end2line', 'exclusive'),
        ('end2aa', 'exclusive'),
        ('config', 'inclusive'),
        ('helpline', 'exclusive'),
        ('depends', 'exclusive'),
    )

    # List of token names.   This is always required
    tokens = (
        'DERIVATE',
        'PARAMS',
        'PACKAGEID',
        'SOURCE',
        'DESCRIPTION',
        'DELIMITER',
        'CONFIG',
        'CONFIG_ITEM',
        'CONFIG_HELP',
        'CONFIG_HELP_LINE',
        'CONFIG_HELP_END',
        'DEPENDS',
        'DEPENDS_SELECT_OTH',  # +<pkg>
        'DEPENDS_SELECT_OTH_IF',  # +<symbol>:<pkg>
        'DEPENDS_WAIT_SYMBOL',  # @<symbol>
        'DEPENDS_WAIT_OTH_SELECTED',  # <pkg>
        'DEPENDS_WAIT_OTH_SELECTED_IF',  # @<symbol>:<pkg>
        'DEPENDS_SELECT_SYMBOL',  # +@<symbol>
        'DEPENDS_END',
    )

    packageNameRule = r'[a-zA-Z-_\d.]+'
    packageSymbolRule = r'([a-zA-Z-_\d.!()]|[|]{2}|[&]{2})+'
    packageItemRule = r'(?=[ \n])'

    def t_DEPENDS(self, t: LexToken):
        r'Depends:'
        t.lexer.doc_start = t.lexer.lexpos
        t.lexer.push_state('depends')
        t.value = t.value[:-1]
        return t

    def t_depends_exit(self, t):
        r'\n'
        t.lexer.pop_state()
        t.lexer.lineno += len(t.value)
        t.type = 'DEPENDS_END'
        return t

    # @TOKEN(r'(\+[a-zA-Z-_]+)(?=[ \n])')
    @TOKEN(r'(\+{}){}'.format(packageNameRule, packageItemRule))
    def t_depends_select_other(self, t):
        t.type = 'DEPENDS_SELECT_OTH'
        t.value = [t.value[1:]]
        t.value = [t.type] + t.value
        # print([t.value])
        return t

    @TOKEN(r'(\+{}:{}){}'.format(packageSymbolRule, packageNameRule, packageItemRule))
    def t_depends_select_other_if(self, t):
        t.type = 'DEPENDS_SELECT_OTH_IF'
        t.value = t.value[1:].split(':')
        t.value = [t.type] + t.value
        # TODO: laxer for symbol
        # print([t.value])
        return t

    @TOKEN(r'(\@{}){}'.format(packageSymbolRule, packageItemRule))
    def t_depends_wait_symbol(self, t):
        t.type = 'DEPENDS_WAIT_SYMBOL'
        t.value = [t.value[1:]]
        t.value = [t.type] + t.value
        # TODO: laxer for symbol
        # print([t.value])
        return t

    @TOKEN(r'({}){}'.format(packageNameRule, packageItemRule))
    def t_depends_wait_other_selected(self, t):
        t.type = 'DEPENDS_WAIT_OTH_SELECTED'
        t.value = [t.type, t.value]
        # print([t.value])
        return t

    @TOKEN(r'(\+\@{}){}'.format(packageSymbolRule, packageItemRule))
    def t_depends_select_symbol(self, t):
        t.type = 'DEPENDS_SELECT_SYMBOL'
        t.value = [t.value[2:]]
        t.value = [t.type] + t.value
        # TODO: laxer for symbol
        # print([t.value])
        return t

    # issue: https://github.com/openwrt/packages/issues/12802https://github.com/openwrt/packages/issues/12802
    @TOKEN(r'(\@?{}:{}){}'.format(packageSymbolRule, packageNameRule, packageItemRule))
    def t_depends_wait_other_selected_if(self, t):
        t.type = 'DEPENDS_WAIT_OTH_SELECTED_IF'
        t.value = t.value.lstrip('@').split(':')
        t.value = [t.type] + t.value
        # TODO: laxer for symbol
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
