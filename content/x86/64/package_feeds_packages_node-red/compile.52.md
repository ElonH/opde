---
title: "compile.52"
date: 2021-03-09 13:47:09.082339
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
make package/feeds/packages/node-red/compile -j$(nproc) || make package/feeds/packages/node-red/compile V=s
```

#### Compile.txt

``` bash
npm info it worked if it ends with ok
npm info using npm@6.14.11
npm info using node@v12.21.0
npm timing stage:loadCurrentTree Completed in 11ms
npm timing stage:loadIdealTree:cloneCurrentTree Completed in 0ms
npm timing stage:loadIdealTree:loadShrinkwrap Completed in 1ms
npm timing stage:rollbackFailedOptional Completed in 0ms
npm timing stage:runTopLevelLifecycles Completed in 632233ms
npm WARN optional SKIPPING OPTIONAL DEPENDENCY: bcrypt@3.0.6 (node_modules/node-red/node_modules/bcrypt):
npm WARN network SKIPPING OPTIONAL DEPENDENCY: request to https://registry.npmjs.org/bcrypt failed, reason: Client network socket disconnected before secure TLS connection was established

npm ERR! code ECONNRESET
npm ERR! errno ECONNRESET
npm ERR! network request to https://registry.npmjs.org/@node-red%2fruntime failed, reason: Client network socket disconnected before secure TLS connection was established
npm ERR! network This is a problem related to network connectivity.
npm ERR! network In most cases you are behind a proxy or have bad network settings.
npm ERR! network 
npm ERR! network If you are behind a proxy, please make sure that the
npm ERR! network 'proxy' config is set properly.  See: 'npm help config'
npm timing npm Completed in 632444ms

npm ERR! A complete log of this run can be found in:
npm ERR!     /openwrt/tmp/npm-cache-muXAf8pW3t/_logs/2021-03-08T21_08_27_705Z-debug.log
make[3]: *** [Makefile:99: /openwrt/build_dir/target-x86_64_musl/node-red-1.2.9/.built] Error 1
```
