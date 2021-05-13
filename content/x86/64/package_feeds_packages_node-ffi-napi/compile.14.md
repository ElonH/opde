---
title: "compile.14"
date: 2021-05-13 00:27:03.927085
hidden: false
draft: false
weight: -14
---

build number: `14`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/node-ffi-napi/compile -j$(nproc) || make package/feeds/packages/node-ffi-napi/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/0001-do_not_build_libffi.patch using plaintext: 
patching file binding.gyp

Applying ./patches/0002-support_mips.patch using plaintext: 
patching file src/ffi.cc
npm info it worked if it ends with ok
npm info using npm@6.14.12
npm info using node@v14.16.1
npm timing stage:loadCurrentTree Completed in 29ms
npm timing stage:loadIdealTree:cloneCurrentTree Completed in 1ms
npm timing stage:loadIdealTree:loadShrinkwrap Completed in 1ms
npm http fetch GET 200 https://registry.npmjs.org/debug 126ms
npm http fetch GET 200 https://registry.npmjs.org/ref-struct-di 120ms
npm http fetch GET 200 https://registry.npmjs.org/ref-napi 133ms
npm http fetch GET 200 https://registry.npmjs.org/node-addon-api 136ms
npm http fetch GET 200 https://registry.npmjs.org/node-gyp-build 137ms
npm http fetch GET 200 https://registry.npmjs.org/debug/-/debug-4.3.1.tgz 59ms
npm http fetch GET 200 https://registry.npmjs.org/ref-struct-di/-/ref-struct-di-1.1.1.tgz 59ms
npm http fetch GET 200 https://registry.npmjs.org/node-gyp-build/-/node-gyp-build-4.2.3.tgz 120ms
npm http fetch GET 200 https://registry.npmjs.org/node-addon-api/-/node-addon-api-3.1.0.tgz 145ms
npm http fetch GET 200 https://registry.npmjs.org/ref-napi/-/ref-napi-3.0.2.tgz 148ms
npm http fetch GET 200 https://registry.npmjs.org/get-uv-event-loop-napi-h 495ms
npm http fetch GET 200 https://registry.npmjs.org/get-uv-event-loop-napi-h/-/get-uv-event-loop-napi-h-1.0.6.tgz 18ms
npm http fetch GET 200 https://registry.npmjs.org/ms 23ms
npm http fetch GET 200 https://registry.npmjs.org/ms/-/ms-2.1.2.tgz 24ms
npm http fetch GET 200 https://registry.npmjs.org/get-symbol-from-current-process-h 381ms
npm http fetch GET 200 https://registry.npmjs.org/get-symbol-from-current-process-h/-/get-symbol-from-current-process-h-1.0.2.tgz 33ms
npm http fetch GET 200 https://registry.npmjs.org/node-addon-api/-/node-addon-api-2.0.2.tgz 59ms
npm http fetch GET 200 https://registry.npmjs.org/debug/-/debug-3.2.7.tgz 19ms
npm timing stage:loadIdealTree:loadAllDepsIntoIdealTree Completed in 1118ms
npm timing stage:loadIdealTree Completed in 1125ms
npm timing stage:generateActionsToTake Completed in 5ms
npm timing action:extract Completed in 145ms
npm timing action:finalize Completed in 17ms
npm timing action:refresh-package-json Completed in 30ms
npm info lifecycle get-symbol-from-current-process-h@1.0.2~preinstall: get-symbol-from-current-process-h@1.0.2
npm info lifecycle ms@2.1.2~preinstall: ms@2.1.2
npm info lifecycle debug@4.3.1~preinstall: debug@4.3.1
npm info lifecycle node-gyp-build@4.2.3~preinstall: node-gyp-build@4.2.3
npm info lifecycle node-addon-api@2.0.2~preinstall: node-addon-api@2.0.2
npm info lifecycle debug@3.2.7~preinstall: debug@3.2.7
npm info lifecycle get-uv-event-loop-napi-h@1.0.6~preinstall: get-uv-event-loop-napi-h@1.0.6
npm info lifecycle node-addon-api@3.1.0~preinstall: node-addon-api@3.1.0
npm info lifecycle ref-napi@3.0.2~preinstall: ref-napi@3.0.2
npm info lifecycle ref-struct-di@1.1.1~preinstall: ref-struct-di@1.1.1
npm info lifecycle ffi-napi@4.0.3~preinstall: ffi-napi@4.0.3
npm timing action:preinstall Completed in 2ms
npm info linkStuff get-symbol-from-current-process-h@1.0.2
npm info linkStuff ms@2.1.2
npm info linkStuff debug@4.3.1
npm info linkStuff node-gyp-build@4.2.3
npm info linkStuff node-addon-api@2.0.2
npm info linkStuff debug@3.2.7
npm info linkStuff get-uv-event-loop-napi-h@1.0.6
npm info linkStuff node-addon-api@3.1.0
npm info linkStuff ref-napi@3.0.2
npm info linkStuff ref-struct-di@1.1.1
npm info linkStuff ffi-napi@4.0.3
npm timing action:build Completed in 9ms
npm info lifecycle get-symbol-from-current-process-h@1.0.2~install: get-symbol-from-current-process-h@1.0.2
npm info lifecycle ms@2.1.2~install: ms@2.1.2
npm info lifecycle debug@4.3.1~install: debug@4.3.1
npm info lifecycle node-gyp-build@4.2.3~install: node-gyp-build@4.2.3
npm info lifecycle node-addon-api@2.0.2~install: node-addon-api@2.0.2
npm info lifecycle debug@3.2.7~install: debug@3.2.7
npm info lifecycle get-uv-event-loop-napi-h@1.0.6~install: get-uv-event-loop-napi-h@1.0.6
npm info lifecycle node-addon-api@3.1.0~install: node-addon-api@3.1.0
npm info lifecycle ref-napi@3.0.2~install: ref-napi@3.0.2

> ref-napi@3.0.2 install /openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3/node_modules/ref-napi
> node-gyp-build

gyp info it worked if it ends with ok
gyp info using node-gyp@5.1.0
gyp info using node@14.16.1 | linux | x64
gyp info find Python using Python version 3.8.5 found at "/openwrt/staging_dir/host/bin/python"
gyp info spawn /openwrt/staging_dir/host/bin/python
gyp info spawn args [
gyp info spawn args   '/openwrt/staging_dir/hostpkg/lib/node_modules/npm/node_modules/node-gyp/gyp/gyp_main.py',
gyp info spawn args   'binding.gyp',
gyp info spawn args   '-f',
gyp info spawn args   'make',
gyp info spawn args   '-I',
gyp info spawn args   '/openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3/node_modules/ref-napi/build/config.gypi',
gyp info spawn args   '-I',
gyp info spawn args   '/openwrt/staging_dir/hostpkg/lib/node_modules/npm/node_modules/node-gyp/addon.gypi',
gyp info spawn args   '-I',
gyp info spawn args   '/openwrt/staging_dir/target-x86_64_musl/usr/include/node/common.gypi',
gyp info spawn args   '-Dlibrary=shared_library',
gyp info spawn args   '-Dvisibility=default',
gyp info spawn args   '-Dnode_root_dir=/openwrt/staging_dir/target-x86_64_musl/usr/',
gyp info spawn args   '-Dnode_gyp_dir=/openwrt/staging_dir/hostpkg/lib/node_modules/npm/node_modules/node-gyp',
gyp info spawn args   '-Dnode_lib_file=/openwrt/staging_dir/target-x86_64_musl/usr/$(Configuration)/node.lib',
gyp info spawn args   '-Dmodule_root_dir=/openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3/node_modules/ref-napi',
gyp info spawn args   '-Dnode_engine=v8',
gyp info spawn args   '--depth=.',
gyp info spawn args   '--no-parallel',
gyp info spawn args   '--generator-output',
gyp info spawn args   'build',
gyp info spawn args   '-Goutput_dir=.'
gyp info spawn args ]
gyp info spawn make
gyp info spawn args [ 'BUILDTYPE=Release', '-C', 'build' ]
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3/node_modules/ref-napi/build'
  CC(target) Release/obj.target/nothing/node_modules/node-addon-api/src/nothing.o
rm -f Release/obj.target/node_modules/node-addon-api/src/nothing.a Release/obj.target/node_modules/node-addon-api/src/nothing.a.ar-file-list; mkdir -p `dirname Release/obj.target/node_modules/node-addon-api/src/nothing.a`
x86_64-openwrt-linux-musl-gcc-ar crs Release/obj.target/node_modules/node-addon-api/src/nothing.a @Release/obj.target/node_modules/node-addon-api/src/nothing.a.ar-file-list
  COPY Release/nothing.a
  CXX(target) Release/obj.target/binding/src/binding.o
  SOLINK_MODULE(target) Release/obj.target/binding.node
  COPY Release/binding.node
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3/node_modules/ref-napi/build'
gyp info ok 
npm info lifecycle ref-struct-di@1.1.1~install: ref-struct-di@1.1.1
npm info lifecycle ffi-napi@4.0.3~install: ffi-napi@4.0.3

> ffi-napi@4.0.3 install /openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3/ipkg-install/usr/lib/node_modules/ffi-napi
> node-gyp-build

gyp info it worked if it ends with ok
gyp info using node-gyp@5.1.0
gyp info using node@14.16.1 | linux | x64
gyp info find Python using Python version 3.8.5 found at "/openwrt/staging_dir/host/bin/python"
gyp info spawn /openwrt/staging_dir/host/bin/python
gyp info spawn args [
gyp info spawn args   '/openwrt/staging_dir/hostpkg/lib/node_modules/npm/node_modules/node-gyp/gyp/gyp_main.py',
gyp info spawn args   'binding.gyp',
gyp info spawn args   '-f',
gyp info spawn args   'make',
gyp info spawn args   '-I',
gyp info spawn args   '/openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3/build/config.gypi',
gyp info spawn args   '-I',
gyp info spawn args   '/openwrt/staging_dir/hostpkg/lib/node_modules/npm/node_modules/node-gyp/addon.gypi',
gyp info spawn args   '-I',
gyp info spawn args   '/openwrt/staging_dir/target-x86_64_musl/usr/include/node/common.gypi',
gyp info spawn args   '-Dlibrary=shared_library',
gyp info spawn args   '-Dvisibility=default',
gyp info spawn args   '-Dnode_root_dir=/openwrt/staging_dir/target-x86_64_musl/usr/',
gyp info spawn args   '-Dnode_gyp_dir=/openwrt/staging_dir/hostpkg/lib/node_modules/npm/node_modules/node-gyp',
gyp info spawn args   '-Dnode_lib_file=/openwrt/staging_dir/target-x86_64_musl/usr/$(Configuration)/node.lib',
gyp info spawn args   '-Dmodule_root_dir=/openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3',
gyp info spawn args   '-Dnode_engine=v8',
gyp info spawn args   '--depth=.',
gyp info spawn args   '--no-parallel',
gyp info spawn args   '--generator-output',
gyp info spawn args   'build',
gyp info spawn args   '-Goutput_dir=.'
gyp info spawn args ]
gyp info spawn make
gyp info spawn args [ 'BUILDTYPE=Release', '-C', 'build' ]
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3/build'
  CXX(target) Release/obj.target/ffi_bindings/src/ffi.o
../src/ffi.cc:4:10: fatal error: fficonfig.h: No such file or directory
 #include "fficonfig.h"
          ^~~~~~~~~~~~~
compilation terminated.
make[4]: *** [ffi_bindings.target.mk:117: Release/obj.target/ffi_bindings/src/ffi.o] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3/build'
gyp ERR! build error 
gyp ERR! stack Error: `make` failed with exit code: 2
gyp ERR! stack     at ChildProcess.onExit (/openwrt/staging_dir/hostpkg/lib/node_modules/npm/node_modules/node-gyp/lib/build.js:194:23)
gyp ERR! stack     at ChildProcess.emit (events.js:315:20)
gyp ERR! stack     at Process.ChildProcess._handle.onexit (internal/child_process.js:277:12)
gyp ERR! System Linux 5.4.0-1046-azure
gyp ERR! command "/openwrt/staging_dir/hostpkg/bin/node" "/openwrt/staging_dir/hostpkg/lib/node_modules/npm/node_modules/node-gyp/bin/node-gyp.js" "rebuild"
gyp ERR! cwd /openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3
gyp ERR! node -v v14.16.1
gyp ERR! node-gyp -v v5.1.0
gyp ERR! not ok 
npm info lifecycle ffi-napi@4.0.3~install: Failed to exec install script
npm timing action:install Completed in 3042ms
npm WARN rollback Rolling back get-symbol-from-current-process-h@1.0.2 failed (this is probably harmless): /openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3/node_modules/get-symbol-from-current-process-h is not a child of /openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3/ipkg-install/usr/lib
npm WARN rollback Rolling back ms@2.1.2 failed (this is probably harmless): /openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3/node_modules/ms is not a child of /openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3/ipkg-install/usr/lib
npm WARN rollback Rolling back debug@4.3.1 failed (this is probably harmless): /openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3/node_modules/debug is not a child of /openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3/ipkg-install/usr/lib
npm WARN rollback Rolling back node-gyp-build@4.2.3 failed (this is probably harmless): /openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3/node_modules/node-gyp-build is not a child of /openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3/ipkg-install/usr/lib
npm WARN rollback Rolling back node-addon-api@2.0.2 failed (this is probably harmless): /openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3/node_modules/ref-napi/node_modules/node-addon-api is not a child of /openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3/ipkg-install/usr/lib
npm WARN rollback Rolling back debug@3.2.7 failed (this is probably harmless): /openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3/node_modules/ref-struct-di/node_modules/debug is not a child of /openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3/ipkg-install/usr/lib
npm WARN rollback Rolling back get-uv-event-loop-napi-h@1.0.6 failed (this is probably harmless): /openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3/node_modules/get-uv-event-loop-napi-h is not a child of /openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3/ipkg-install/usr/lib
npm WARN rollback Rolling back node-addon-api@3.1.0 failed (this is probably harmless): /openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3/node_modules/node-addon-api is not a child of /openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3/ipkg-install/usr/lib
npm WARN rollback Rolling back ref-napi@3.0.2 failed (this is probably harmless): /openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3/node_modules/ref-napi is not a child of /openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3/ipkg-install/usr/lib
npm WARN rollback Rolling back ref-struct-di@1.1.1 failed (this is probably harmless): /openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3/node_modules/ref-struct-di is not a child of /openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3/ipkg-install/usr/lib
npm timing stage:rollbackFailedOptional Completed in 7ms
npm timing stage:runTopLevelLifecycles Completed in 4426ms
npm ERR! code ELIFECYCLE
npm ERR! errno 1
npm ERR! ffi-napi@4.0.3 install: `node-gyp-build`
npm ERR! Exit status 1
npm ERR! 
npm ERR! Failed at the ffi-napi@4.0.3 install script.
npm ERR! This is probably not a problem with npm. There is likely additional logging output above.
npm timing npm Completed in 4757ms

npm ERR! A complete log of this run can be found in:
npm ERR!     /openwrt/tmp/npm-cache-mXjfK6RO0s/_logs/2021-05-12T22_16_36_943Z-debug.log
make[3]: *** [Makefile:92: /openwrt/build_dir/target-x86_64_musl/node-ffi-napi-4.0.3/.built] Error 1
```
