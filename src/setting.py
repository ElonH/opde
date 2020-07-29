
from pathlib import Path
from git import Repo
from .parser import PackageInfoParser
import re
import json


class OpdeSetting:
    'Opde Common settings'

    def __init__(self):
        self.opde_dir = Path(__file__).parent.parent.absolute()
        self.opde_repo = Repo(self.opde_dir)
        # feeds path
        feeds_dir = [
            'feeds/ctcgfw/packages',
            'feeds/ctcgfw/luci',
            'feeds/openwrt/routing',
            'feeds/openwrt/telephony',
            'feeds/openwrt/freifunk',
        ]
        self.feeds_dir = [self.opde_dir.joinpath(i) for i in feeds_dir]
        # OpenWRT Source Path
        self.openwrt_dir = self.opde_dir.joinpath('ctcgfw')
        # (target, subtarget) same as tree structure of src.configer
        self.targets = ('x86', '64')
        # cache directory
        self.cache_dir = self.opde_dir.joinpath('cache')
        # ast json file
        self._packageinfo_ast_file = self.openwrt_dir.joinpath(
            'logs', 'package.ast.json')
        self._packageinfo_ast_file_loaded = False
        self._targetinfo_ast_file = self.openwrt_dir.joinpath(
            'logs', 'target.ast.json')
        self._logs_ast_file_loaded = False
        self._logs_ast_file = self.openwrt_dir.joinpath('logs', 'logs.ast.json')
        self._deps_dag_file_loaded = False
        self.deps_dag_file = self.openwrt_dir.joinpath('logs', 'deps.dag.json')
        self._tasks_list = self.openwrt_dir.joinpath('logs', 'tasks.list.json')
        self._sdk_buildin_ast_file = self.openwrt_dir.joinpath(
            'logs', 'sdk.buildin.ast.json')
        # worker config directory
        self.worker_conf_dir = self.openwrt_dir.joinpath('logs', 'task')

    # def submodule(self, sub_path: str):
    #     'get submodule class by path'
    #     sms = self.opde_repo.submodules
    #     exp_path = Path(sub_path)
    #     for sm in sms:
    #         if sm.abspath == exp_path.absolute():
    #             return sm
    #     return None

    @ property
    def openwrt_repo(self):
        'return submodule of openwrt'
        sms = []
        for sm in self.opde_repo.submodules:
            if self.openwrt_dir.samefile(sm.abspath):
                return sm
        return None

    @ property
    def feeds_repos(self):
        'return submodules of feeds'
        sms = []
        for sm in self.opde_repo.submodules:
            for feed in self.feeds_dir:
                if feed.samefile(sm.abspath):
                    sms.append(sm)
                    break
        return sms

    @ property
    def feeds_conf(self):
        'return text of feeds.conf or feeds.default.conf'
        sms = self.feeds_repos
        feeds_conf = []
        for sm in sms:
            feed_name = Path(sm.abspath).name
            feeds_conf.append('src-link %s %s' % (feed_name, sm.abspath))
        return '\n'.join(feeds_conf)

    @ property
    def packageinfo_ast(self):
        'return text of package.ast.json'
        if self._packageinfo_ast_file_loaded:
            return json.loads(self._packageinfo_ast_file.read_text())
        ctx = self.openwrt_dir.joinpath('tmp', '.packageinfo').read_text()
        # hack some code to pass through laxer
        ctx = re.sub('\t\t\t/sys/module/iwlwifi/parameters/debug',
                     '\t\t  /sys/module/iwlwifi/parameters/debug', ctx)
        ctx = re.sub('\t\t\t  % echo 0x43fff > /sys/module/iwlwifi/parameters/debug',
                     '\t\t    % echo 0x43fff > /sys/module/iwlwifi/parameters/debug', ctx)
        ctx = re.sub('\t\t\t  drivers/net/wireless/intel/iwlwifi/iwl-debug.h',
                     '\t\t    drivers/net/wireless/intel/iwlwifi/iwl-debug.h', ctx)

        p = PackageInfoParser()
        packageInfoAst = p.gen_ast(ctx)
        self._packageinfo_ast_file.write_text(json.dumps(
            packageInfoAst, indent=2, sort_keys=True))
        self._packageinfo_ast_file_loaded = True
        return packageInfoAst

    @ property
    def logs_ast(self):
        'return text of logs.ast.json'
        if self._logs_ast_file_loaded:
            return json.loads(self._logs_ast_file.read_text())
        raise RuntimeError('Please set context first')

    @ logs_ast.setter
    def logs_ast(self, logsAst: object):
        self._logs_ast_file.write_text(
            json.dumps(logsAst, indent=2, sort_keys=False))
        self._logs_ast_file_loaded = True

    @property
    def linux_embedded_module(self):
        'return kernel modules which will be removed in SDK'
        linux_source = [source for source in self.packageinfo_ast
                        if source['Source-Makefile'] == 'package/kernel/linux/Makefile'][0]
        linux_modules = [i['Package'] for i in linux_source['packages']]
        return linux_modules

    @property
    def deps_dag(self):
        'return text of deps.dag.json'
        if self._deps_dag_file_loaded:
            return self.deps_dag_file.read_text()
        raise RuntimeError('Please set context first')

    @deps_dag.setter
    def deps_dag(self, ctx: str):
        self.deps_dag_file.write_text(ctx)
        self._deps_dag_file_loaded = True

    @property
    def tasks_list(self):
        'return text of tasks.list.json'
        return json.loads(self._tasks_list.read_text())

    @tasks_list.setter
    def tasks_list(self, ctx: object):
        self._tasks_list.write_text(json.dumps(ctx, indent=2, sort_keys=True))

    @property
    def sdk_buildin_ast(self):
        'return text of tasks.list.json'
        return json.loads(self._sdk_buildin_ast_file.read_text())

    @sdk_buildin_ast.setter
    def sdk_buildin_ast(self, ctx: object):
        self._sdk_buildin_ast_file.write_text(
            json.dumps(ctx, indent=2, sort_keys=True))
