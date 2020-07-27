
def KconfigDumper(kconfigAst: object, indent='\t'):
    '''
    transform kconfigAst ack to kconfig
    '''
    ans = []
    for item in kconfigAst:
        ans_item = []
        ans_item.append('%s %s' % (item['type'], item['sym']))
        ans_item.append('%s%s' % (indent, item['value-type']))
        if item['value-type'] != 'string':
            ans_item.append('%sdefault %s' % (indent, item['default']))
        else:
            ans_item.append('%sdefault "%s"' % (indent, item['default']))
        ans.append('\n'.join(ans_item))
    ans.append('\n')
    return '\n\n'.join(ans)
