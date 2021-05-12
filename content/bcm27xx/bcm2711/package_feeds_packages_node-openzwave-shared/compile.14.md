---
title: "compile.14"
date: 2021-05-12 23:05:59.589317
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
make package/feeds/packages/node-openzwave-shared/compile -j$(nproc) || make package/feeds/packages/node-openzwave-shared/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/999-node_v16_support.patch using plaintext: 
patching file binding.gyp
npm info it worked if it ends with ok
npm info using npm@6.14.12
npm info using node@v14.16.1
npm timing stage:loadCurrentTree Completed in 16ms
npm timing stage:loadIdealTree:cloneCurrentTree Completed in 0ms
npm timing stage:loadIdealTree:loadShrinkwrap Completed in 1ms
npm timing stage:rollbackFailedOptional Completed in 1ms
npm timing stage:runTopLevelLifecycles Completed in 190811ms
npm ERR! code ECONNRESET
npm ERR! errno ECONNRESET
npm ERR! network request to https://registry.npmjs.org/nan failed, reason: Client network socket disconnected before secure TLS connection was established
npm ERR! network This is a problem related to network connectivity.
npm ERR! network In most cases you are behind a proxy or have bad network settings.
npm ERR! network 
npm ERR! network If you are behind a proxy, please make sure that the
npm ERR! network 'proxy' config is set properly.  See: 'npm help config'
npm timing npm Completed in 191217ms

npm ERR! A complete log of this run can be found in:
npm ERR!     /openwrt/tmp/npm-cache-qm6oi4aQF8/_logs/2021-05-12T15_56_34_218Z-debug.log
make[3]: *** [Makefile:89: /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-openzwave-shared-1.7.2/.built] Error 1
```
