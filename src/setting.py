
from pathlib import Path

from yaml.loader import Loader
from src.lexer.packageinfo import PackageInfoLexer
from .parser import PackageInfoParser
import re
import json
import yaml


class Cache:
    '''interal cache system'''

    def __init__(self, path: str, enable=True):
        self._enabled = enable
        self._path = Path(path)
        self._path.mkdir(parents=True, exist_ok=True)

    def Enable(self, val: bool = None):
        if val is not None:
            self._enabled = val

    def _IsCached(self, name: str) -> bool:
        return self._path.joinpath(name).exists() if self._enabled else False

    def LoadCached(self, name: str) -> str:
        return self._path.joinpath(name).read_text() if self._IsCached(name) else None

    def StoreCache(self, name: str, content: str = '') -> int:
        self._path.joinpath(name).touch(exist_ok=True)
        return self._path.joinpath(name).write_text(content)


class OpdeSetting:
    'Opde Common settings'

    def __init__(self, openwrt_source: str, cahce_enable: bool):
        """
        Args:
            openwrt_source (str): path to OpenWRT source code
        """
        # OpenWRT Source Path
        self.openwrt_dir = Path(openwrt_source).absolute()
        # Opde cache directory
        self.cache_dir = self.openwrt_dir.joinpath('.opde')
        # (target, subtarget) same as tree structure of src.configer
        self.targets = ('x86', '64')

        # Opde cache system
        self.cache = Cache(self.cache_dir, cahce_enable)
        # openWRT log dirs
        self.logs_dir = self.openwrt_dir.joinpath('logs')
        self.deps_dag_file = self.cache_dir.joinpath('.deps.dag.json')
        # worker config directory
        self.worker_conf_dir = self.cache_dir.joinpath('worker')
        # # feeds path
        # feeds_dir = [
        #     'feeds/ctcgfw/packages',
        #     'feeds/ctcgfw/luci',
        #     'feeds/openwrt/routing',
        #     'feeds/openwrt/telephony',
        #     'feeds/openwrt/freifunk',
        # ]
        # self.feeds_dir = [self.opde_dir.joinpath(i) for i in feeds_dir]
        # # OpenWRT Soure will move to here in SDK
        # self.openwrt_dir_in_sdk = self.opde_dir.joinpath('base')
        # # ast json file
        # self._targetinfo_ast_file = self.openwrt_dir.joinpath(
        #     'logs', 'target.ast.json')
        # self._logs_ast_file_loaded = False
        # self._logs_ast_file = self.openwrt_dir.joinpath('logs', 'logs.ast.json')
        # self._deps_dag_file_loaded = False
        # self.deps_dag_file = self.openwrt_dir.joinpath('logs', 'deps.dag.json')
        # self._metadata_hash_file = self.openwrt_dir.joinpath(
        #     'logs', 'metadata.hash.json')
        # self._tasks_list = self.openwrt_dir.joinpath('logs', 'tasks.list.json')
        # self._sdk_buildin_ast_file = self.openwrt_dir.joinpath(
        #     'logs', 'sdk.buildin.ast.json')

    # @property
    # def opde_repo(self):
    #     'return openwrt source repo instance'
    #     return Repo(self.opde_dir)

    # def submodule(self, sub_path: str):
    #     'get submodule class by path'
    #     sms = self.opde_repo.submodules
    #     exp_path = Path(sub_path)
    #     for sm in sms:
    #         if exp_path.absolute().as_posix() == sm.abspath:
    #             return sm
    #     return None

    # @property
    # def openwrt_repo(self):
    #     'return submodule of openwrt'
    #     sms = []
    #     for sm in self.opde_repo.submodules:
    #         if self.openwrt_dir.samefile(sm.abspath):
    #             return sm
    #     return None

    # @property
    # def feeds_repos(self):
    #     'return submodules of feeds'
    #     sms = []
    #     for sm in self.opde_repo.submodules:
    #         for feed in self.feeds_dir:
    #             if feed.samefile(sm.abspath):
    #                 sms.append(sm)
    #                 break
    #     return sms

    # def feeds_conf(self, sms: list):
    #     '''
    #     sms: submodules list
    #     return text of feeds.conf or feeds.default.conf
    #     '''
    #     feeds_conf = []
    #     for sm in sms:
    #         feed_name = Path(sm.abspath).name
    #         feeds_conf.append('src-link %s %s' % (feed_name, sm.abspath))
    #     return '\n'.join(feeds_conf)

    # @property
    # def metadata_hash(self):
    #     'return  object of hashes of openwrt source bundle and filepath'
    #     metadata = {}
    #     for makefile in self.packageinfo_ast:
    #         for pack in makefile['packages']:
    #             metadata[pack['Package']] = '/'.join(
    #                 [pack[i] for i in ['Package-Source-Version',
    #                                    'Package-Hash', 'Package-Mirror-Hash']]
    #             )
    #     self._metadata_hash_file.write_text(
    #         json.dumps(metadata, indent=2, sort_keys=True,
    #                    separators=(",", ":"))
    #     )
    #     return metadata

    @ property
    def packageinfo_ast(self):
        'return text of package.ast.json'
        cache_name = '.package.ast.json'
        ctx = self.cache.LoadCached(cache_name)
        if ctx:
            return json.loads(ctx)
        packages_raw_files = [self.openwrt_dir.joinpath('tmp', '.packageinfo')]
        packages_raw_files.extend(
            self.openwrt_dir.joinpath('feeds').glob('*.index'))
        packageInfoAst = []
        for i in packages_raw_files:
            ctx = i.read_text()
            # hack some code to pass through laxer

            # for tmp/.packageinfo
            ctx = re.sub('\t\t\t/sys/module/iwlwifi/parameters/debug',
                         '\t\t  /sys/module/iwlwifi/parameters/debug', ctx)
            ctx = re.sub('\t\t\t  % echo 0x43fff > /sys/module/iwlwifi/parameters/debug',
                         '\t\t    % echo 0x43fff > /sys/module/iwlwifi/parameters/debug', ctx)
            ctx = re.sub('\t\t\t  drivers/net/wireless/intel/iwlwifi/iwl-debug.h',
                         '\t\t    drivers/net/wireless/intel/iwlwifi/iwl-debug.h', ctx)
            ctx = re.sub('          Select one TLS module below if you enable the SSL engine in',
                         '\t        Select one TLS module below if you enable the SSL engine in', ctx)
            ctx = re.sub('          [(]mod_gnutls, mod_mbedtls, mod_nss, mod_openssl, mod_wolfssl[)]',
                         '\t        (mod_gnutls, mod_mbedtls, mod_nss, mod_openssl, mod_wolfssl)', ctx)
            # for feeds/[package].index
            # Nothing here currently

            p = PackageInfoParser()
            # # export lexer result
            # l = PackageInfoLexer()
            # l.test(ctx)
            # exit(0)
            packageInfoAst.extend(p.gen_ast(ctx))

        newAST = []
        for makefile in packageInfoAst:
            if 'Source-Makefile' in makefile and str(makefile['Source-Makefile']).startswith('feeds/'):
                continue
            newAST.append(makefile)
        packageInfoAst = newAST
        self.cache.StoreCache(cache_name, json.dumps(packageInfoAst))
        # human-readable file, but yaml parser is too slow
        self.cache.StoreCache('package.ast.yaml', yaml.dump(
            packageInfoAst, Dumper=yaml.CDumper, indent=2, sort_keys=True))
        return packageInfoAst

    def StoreSDKBuildInAst(self, ctx: object):
        self.cache.StoreCache('sdk.build-in.ast.yaml', yaml.dump(
            ctx, Dumper=yaml.CDumper, indent=2, sort_keys=True))

    # @ property
    # def logs_ast(self):
    #     'return text of logs.ast.json'
    #     if self._logs_ast_file_loaded:
    #         return json.loads(self._logs_ast_file.read_text())
    #     raise RuntimeError('Please set context first')

    # @ logs_ast.setter
    # def logs_ast(self, logsAst: object):
    #     self._logs_ast_file.write_text(
    #         json.dumps(logsAst, indent=2, sort_keys=False))
    #     self._logs_ast_file_loaded = True

    @ property
    def linux_embedded_module(self):
        'return kernel modules which will be removed automatically in SDK'
        linux_source = [source for source in self.packageinfo_ast
                        if source['Source-Makefile'] == 'package/kernel/linux/Makefile'][0]
        linux_modules = [i['Package'] for i in linux_source['packages']]
        return linux_modules

    @property
    def packages(self):
        'return packages name list (include kernel modules)'
        lst = []
        for source in [source['packages'] for source in self.packageinfo_ast]:
            lst.extend([i['Package'] for i in source])
        return lst

    def StoreDepsDAG(self, ctx: str):
        'Store content to .deps.dag.json'
        self.deps_dag_file.touch(exist_ok=True)
        self.deps_dag_file.write_text(ctx)

    @property
    def tasks_list(self):
        'return text of tasks.list.json'
        cache_name = '.tasks.list.json'
        ctx = self.cache.LoadCached(cache_name)
        return json.loads(ctx) if ctx is not None else None

    @tasks_list.setter
    def tasks_list(self, ctx: object):
        cache_name = '.tasks.list.json'
        self.cache.StoreCache(cache_name, json.dumps(
            ctx, indent=2, sort_keys=True))
        self.cache.StoreCache('tasks.list.yaml', yaml.dump(
            ctx, Dumper=yaml.CDumper, indent=2, sort_keys=True))

    @property
    def sources_list(self):
        'return text of sources.list.json'
        cache_name = '.sources.list.json'
        ctx = self.cache.LoadCached(cache_name)
        return json.loads(ctx) if ctx is not None else None

    @sources_list.setter
    def sources_list(self, ctx: object):
        cache_name = '.sources.list.json'
        self.cache.StoreCache(cache_name, json.dumps(
            ctx, indent=2, sort_keys=True))
        self.cache.StoreCache('sources.list.yaml', yaml.dump(
            ctx, Dumper=yaml.CDumper, indent=2, sort_keys=True))

    @property
    def vices_list(self):
        'return text of vices.list.json'
        cache_name = '.vices.list.json'
        ctx = self.cache.LoadCached(cache_name)
        return json.loads(ctx) if ctx is not None else None

    @vices_list.setter
    def vices_list(self, ctx: object):
        cache_name = '.vices.list.json'
        self.cache.StoreCache(cache_name, json.dumps(
            ctx, indent=2, sort_keys=True))
        self.cache.StoreCache('vices.list.yaml', yaml.dump(
            ctx, Dumper=yaml.CDumper, indent=2, sort_keys=True))

    @property
    def nodes_list(self):
        'return text of nodes.list.json'
        cache_name = '.nodes.list.json'
        ctx = self.cache.LoadCached(cache_name)
        return json.loads(ctx) if ctx is not None else None

    @nodes_list.setter
    def nodes_list(self, ctx: object):
        cache_name = '.nodes.list.json'
        self.cache.StoreCache(cache_name, json.dumps(
            ctx, indent=2, sort_keys=True))
        self.cache.StoreCache('nodes.list.yaml', yaml.dump(
            ctx, Dumper=yaml.CDumper, indent=2, sort_keys=True))
