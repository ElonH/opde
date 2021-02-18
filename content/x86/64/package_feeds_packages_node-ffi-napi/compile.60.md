---
title: "compile.60"
date: 2021-02-18 15:10:27.214417
hidden: false
draft: false
weight: -60
---

build number: `60`

path: `package/feeds/packages/node-ffi-napi/compile`


``` bash
npm info it worked if it ends with ok
npm info using npm@6.14.11
npm info using node@v12.20.2
npm timing stage:loadCurrentTree Completed in 38ms
npm timing stage:loadIdealTree:cloneCurrentTree Completed in 0ms
npm timing stage:loadIdealTree:loadShrinkwrap Completed in 3ms
npm timing stage:loadIdealTree:loadAllDepsIntoIdealTree Completed in 18ms
npm timing stage:loadIdealTree Completed in 25ms
npm timing stage:generateActionsToTake Completed in 3ms
npm info lifecycle ffi-napi@3.1.0~preuninstall: ffi-napi@3.1.0
npm info lifecycle ffi-napi@3.1.0~uninstall: ffi-napi@3.1.0
npm info lifecycle ffi-napi@3.1.0~postuninstall: ffi-napi@3.1.0
npm timing action:unbuild Completed in 3ms
npm timing action:remove Completed in 1ms
npm timing action:finalize Completed in 1ms
npm timing action:refresh-package-json Completed in 1ms
npm info lifecycle ffi-napi@3.1.0~preinstall: ffi-napi@3.1.0
npm timing action:preinstall Completed in 0ms
npm info linkStuff ffi-napi@3.1.0
npm timing action:build Completed in 1ms
npm info lifecycle ffi-napi@3.1.0~install: ffi-napi@3.1.0

> ffi-napi@3.1.0 install /openwrt/build_dir/target-x86_64_musl/node-ffi-napi-3.1.0/ipkg-install/usr/lib/node_modules/ffi-napi
> node-gyp-build

gyp info it worked if it ends with ok
gyp info using node-gyp@5.1.0
gyp info using node@12.20.2 | linux | x64
gyp info find Python using Python version 3.8.5 found at "/openwrt/staging_dir/host/bin/python"
gyp info spawn /openwrt/staging_dir/host/bin/python
gyp info spawn args [
gyp info spawn args   '/openwrt/staging_dir/hostpkg/lib/node_modules/npm/node_modules/node-gyp/gyp/gyp_main.py',
gyp info spawn args   'binding.gyp',
gyp info spawn args   '-f',
gyp info spawn args   'make',
gyp info spawn args   '-I',
gyp info spawn args   '/openwrt/build_dir/target-x86_64_musl/node-ffi-napi-3.1.0/build/config.gypi',
gyp info spawn args   '-I',
gyp info spawn args   '/openwrt/staging_dir/hostpkg/lib/node_modules/npm/node_modules/node-gyp/addon.gypi',
gyp info spawn args   '-I',
gyp info spawn args   '/openwrt/staging_dir/target-x86_64_musl/usr/include/node/common.gypi',
gyp info spawn args   '-Dlibrary=shared_library',
gyp info spawn args   '-Dvisibility=default',
gyp info spawn args   '-Dnode_root_dir=/openwrt/staging_dir/target-x86_64_musl/usr/',
gyp info spawn args   '-Dnode_gyp_dir=/openwrt/staging_dir/hostpkg/lib/node_modules/npm/node_modules/node-gyp',
gyp info spawn args   '-Dnode_lib_file=/openwrt/staging_dir/target-x86_64_musl/usr/$(Configuration)/node.lib',
gyp info spawn args   '-Dmodule_root_dir=/openwrt/build_dir/target-x86_64_musl/node-ffi-napi-3.1.0',
gyp info spawn args   '-Dnode_engine=v8',
gyp info spawn args   '--depth=.',
gyp info spawn args   '--no-parallel',
gyp info spawn args   '--generator-output',
gyp info spawn args   'build',
gyp info spawn args   '-Goutput_dir=.'
gyp info spawn args ]
gyp info spawn make
gyp info spawn args [ 'BUILDTYPE=Release', '-C', 'build' ]
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/node-ffi-napi-3.1.0/build'
  CXX(target) Release/obj.target/ffi_bindings/src/ffi.o
../src/ffi.cc:4:10: fatal error: fficonfig.h: No such file or directory
 #include "fficonfig.h"
          ^~~~~~~~~~~~~
compilation terminated.
make[4]: *** [ffi_bindings.target.mk:117: Release/obj.target/ffi_bindings/src/ffi.o] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/node-ffi-napi-3.1.0/build'
gyp ERR! build error 
gyp ERR! stack Error: `make` failed with exit code: 2
gyp ERR! stack     at ChildProcess.onExit (/openwrt/staging_dir/hostpkg/lib/node_modules/npm/node_modules/node-gyp/lib/build.js:194:23)
gyp ERR! stack     at ChildProcess.emit (events.js:314:20)
gyp ERR! stack     at Process.ChildProcess._handle.onexit (internal/child_process.js:276:12)
gyp ERR! System Linux 5.8.0-43-generic
gyp ERR! command "/openwrt/staging_dir/hostpkg/bin/node" "/openwrt/staging_dir/hostpkg/lib/node_modules/npm/node_modules/node-gyp/bin/node-gyp.js" "rebuild"
gyp ERR! cwd /openwrt/build_dir/target-x86_64_musl/node-ffi-napi-3.1.0
gyp ERR! node -v v12.20.2
gyp ERR! node-gyp -v v5.1.0
gyp ERR! not ok 
npm info lifecycle ffi-napi@3.1.0~install: Failed to exec install script
npm timing action:install Completed in 396ms
npm timing stage:rollbackFailedOptional Completed in 1ms
npm timing stage:runTopLevelLifecycles Completed in 478ms
npm ERR! code ELIFECYCLE
npm ERR! errno 1
npm ERR! ffi-napi@3.1.0 install: `node-gyp-build`
npm ERR! Exit status 1
npm ERR! 
npm ERR! Failed at the ffi-napi@3.1.0 install script.
npm ERR! This is probably not a problem with npm. There is likely additional logging output above.
npm timing npm Completed in 691ms

npm ERR! A complete log of this run can be found in:
npm ERR!     /openwrt/tmp/npm-cache-iJKpnlmG9s/_logs/2021-02-18T14_19_10_311Z-debug.log
make[3]: *** [Makefile:92: /openwrt/build_dir/target-x86_64_musl/node-ffi-napi-3.1.0/.built] Error 1
```
