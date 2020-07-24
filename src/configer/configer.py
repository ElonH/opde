from pathlib import Path

ConfDir = Path(__file__).parent


class Configer:
    '''
    manage common configuration
    '''

    def mkdir_all(self, targetInfoAst: object):
        '''
        generate all config for new arch/board
        '''
        for target in targetInfoAst:
            target_path = ConfDir.joinpath(target['Target-Board'])
            target_path.mkdir(parents=True, exist_ok=True)
            target_confs = [target_path.joinpath(
                'pre.conf'), target_path.joinpath('post.conf')]
            for conf in target_confs:
                if not conf.exists():
                    conf.write_text('# target: %s' % target['Target-Board'])
                conf.touch()
            if 'subtargets' not in target:
                continue
            for subtar in target['subtargets']:
                subtar_path = ConfDir.joinpath(subtar['Target'])
                subtar_path.mkdir(parents=True, exist_ok=True)
                subtar_confs = [subtar_path.joinpath(
                    'pre.conf'), subtar_path.joinpath('post.conf')]
                for conf in subtar_confs:
                    if not conf.exists():
                        conf.write_text('# subtarget: %s' % subtar['Target'])
                    conf.touch()

    def compose(self, target: str, subtarget=None):
        '''
        generate pre and post config for target
        '''
        pre = []
        post = []
        it: Path = ConfDir.joinpath(target)
        if subtarget != None:
            it = it.joinpath(subtarget)
        while it != ConfDir:
            pre.append(it.joinpath('pre.conf').read_text())
            post.append(it.joinpath('post.conf').read_text())
            it = it.parent
        pre.append(it.joinpath('pre.conf').read_text())
        post.append(it.joinpath('post.conf').read_text())
        print(it)
        return '\n'.join(pre), '\n'.join(post)
