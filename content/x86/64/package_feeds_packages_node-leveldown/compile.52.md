---
title: "compile.52"
date: 2021-03-09 13:47:09.082595
hidden: false
draft: false
weight: -52
---

build number: `52`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/node-leveldown/compile -j$(nproc) || make package/feeds/packages/node-leveldown/compile V=s
```

#### Compile.txt

``` bash
npm info it worked if it ends with ok
npm info using npm@6.14.11
npm info using node@v12.21.0
npm timing stage:loadCurrentTree Completed in 12ms
npm timing stage:loadIdealTree:cloneCurrentTree Completed in 0ms
npm timing stage:loadIdealTree:loadShrinkwrap Completed in 1ms
npm timing stage:rollbackFailedOptional Completed in 1ms
npm timing stage:runTopLevelLifecycles Completed in 316089ms
npm ERR! code ECONNRESET
npm ERR! errno ECONNRESET
npm ERR! network request to https://registry.npmjs.org/node-gyp-build failed, reason: Client network socket disconnected before secure TLS connection was established
npm ERR! network This is a problem related to network connectivity.
npm ERR! network In most cases you are behind a proxy or have bad network settings.
npm ERR! network 
npm ERR! network If you are behind a proxy, please make sure that the
npm ERR! network 'proxy' config is set properly.  See: 'npm help config'
npm timing npm Completed in 316293ms

npm ERR! A complete log of this run can be found in:
npm ERR!     /openwrt/tmp/npm-cache-vfuOpE44PB/_logs/2021-03-08T20_40_49_654Z-debug.log
make[3]: *** [Makefile:89: /openwrt/build_dir/target-x86_64_musl/node-leveldown-5.6.0/.built] Error 1
```
