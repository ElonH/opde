from pathlib import Path


class Configer:
    '''
    manage common configuration
    '''
    _conf_dir = Path(__file__).parent

    @classmethod
    def mkdir_all(cls, targetInfoAst: object):
        '''
        generate all config for new arch/board
        '''
        for target in targetInfoAst:
            target_path = cls._conf_dir.joinpath(target['Target-Board'])
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
                subtar_path = cls._conf_dir.joinpath(subtar['Target'])
                subtar_path.mkdir(parents=True, exist_ok=True)
                subtar_confs = [subtar_path.joinpath(
                    'pre.conf'), subtar_path.joinpath('post.conf')]
                for conf in subtar_confs:
                    if not conf.exists():
                        conf.write_text('# subtarget: %s' % subtar['Target'])
                    conf.touch()

    def __init__(self):
        self.pre = []
        self.internal = []
        self.post = []
        self.addon = {}

    def compose(self, target: str, subtarget=None):
        '''
        generate pre and post config for target
        '''
        self.pre = []
        self.post = []
        it: Path = self._conf_dir.joinpath(target)
        if subtarget != None:
            it = it.joinpath(subtarget)
        while it != self._conf_dir:
            self.pre.append(it.joinpath('pre.conf').read_text())
            self.post.append(it.joinpath('post.conf').read_text())
            it = it.parent
        self.pre.append(it.joinpath('pre.conf').read_text())
        self.post.append(it.joinpath('post.conf').read_text())
        self.pre.reverse()
        self.post.reverse()

    def inject(self, conf: str):
        'inject configuration into internal'
        self.internal.append(conf)

    def download_dir(self, path):
        "Store Openwrt's downloaded source bundles in this directory."
        self.addon['dl'] = 'CONFIG_DOWNLOAD_FOLDER="%s"' % path

    def build_bot_mode(self, val=True):
        '''
        This option changes several defaults to be more suitable for                                                                                                                          │  
        automatic builds. This includes the following changes:                                                                                                                                │  
        - Deleting build directories after compiling (to save space)                                                                                                                          │  
        - Enabling per-device rootfs support                                                                                                                                                  │  
        ...
        '''
        self.addon['build_bot'] = 'CONFIG_BUILDBOT=%s' % ('y' if val else 'n')

    def select_all(self, val=True):
        'Prompt: Select all userspace packages by default'
        self.addon['all'] = 'CONFIG_ALL=%s' % ('y' if val else 'n')

    def build_image_builder(self, val=True):
        'Build the OpenWrt Image Builder'
        self.addon['image'] = 'CONFIG_IB=%s\nCONFIG_IB_STANDALONE=n' % (
            'y' if val else 'n')

    def build_sdk(self, val=True):
        self.addon['sdk'] = 'CONFIG_SDK=%s' % ('y' if val else 'n')

    def commit(self):
        'generate whole configuration'
        return '\n'.join(self.pre + self.internal + self.post + ['# addon'] + list(self.addon.values()))
