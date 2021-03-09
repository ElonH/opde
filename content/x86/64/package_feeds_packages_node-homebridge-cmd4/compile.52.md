---
title: "compile.52"
date: 2021-03-09 13:47:09.082849
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
make package/feeds/packages/node-homebridge-cmd4/compile -j$(nproc) || make package/feeds/packages/node-homebridge-cmd4/compile V=s
```

#### Compile.txt

``` bash
npm info it worked if it ends with ok
npm info using npm@6.14.11
npm info using node@v12.21.0
npm timing stage:loadCurrentTree Completed in 11ms
npm timing stage:loadIdealTree:cloneCurrentTree Completed in 0ms
npm timing stage:loadIdealTree:loadShrinkwrap Completed in 1ms
npm http fetch GET 200 https://registry.npmjs.org/latest-version 1270ms
npm http fetch GET 200 https://registry.npmjs.org/command-exists 1280ms
npm http fetch GET 200 https://registry.npmjs.org/fakegato-history 1535ms
npm http fetch GET 200 https://registry.npmjs.org/github-version-checker 1553ms
npm http fetch GET 200 https://registry.npmjs.org/chalk 2037ms
npm http fetch GET 200 https://registry.npmjs.org/moment 2325ms
npm http fetch GET 200 https://registry.npmjs.org/latest-version/-/latest-version-5.1.0.tgz 1181ms
npm http fetch GET 200 https://registry.npmjs.org/github-version-checker/-/github-version-checker-2.2.0.tgz 1155ms
npm http fetch GET 200 https://registry.npmjs.org/fakegato-history/-/fakegato-history-0.6.1.tgz 1250ms
npm http fetch GET 200 https://registry.npmjs.org/command-exists/-/command-exists-1.2.9.tgz 1666ms
npm http fetch GET 200 https://registry.npmjs.org/chalk/-/chalk-4.1.0.tgz 1101ms
npm http fetch GET 200 https://registry.npmjs.org/moment/-/moment-2.29.1.tgz 1879ms
npm http fetch GET 200 https://registry.npmjs.org/ansi-styles 1237ms
npm http fetch GET 200 https://registry.npmjs.org/supports-color 1374ms
npm http fetch GET 200 https://registry.npmjs.org/ansi-styles/-/ansi-styles-4.3.0.tgz 1186ms
npm http fetch GET 200 https://registry.npmjs.org/supports-color/-/supports-color-7.2.0.tgz 1248ms
npm http fetch GET 200 https://registry.npmjs.org/color-convert 1258ms
npm http fetch GET 200 https://registry.npmjs.org/color-convert/-/color-convert-2.0.1.tgz 1301ms
npm http fetch GET 200 https://registry.npmjs.org/color-name 1233ms
npm http fetch GET 200 https://registry.npmjs.org/color-name/-/color-name-1.1.4.tgz 1220ms
npm http fetch GET 200 https://registry.npmjs.org/has-flag 1225ms
npm timing stage:rollbackFailedOptional Completed in 0ms
npm timing stage:runTopLevelLifecycles Completed in 401815ms
npm ERR! code ECONNRESET
npm ERR! errno ECONNRESET
npm ERR! network request to https://registry.npmjs.org/has-flag/-/has-flag-4.0.0.tgz failed, reason: Client network socket disconnected before secure TLS connection was established
npm ERR! network This is a problem related to network connectivity.
npm ERR! network In most cases you are behind a proxy or have bad network settings.
npm ERR! network 
npm ERR! network If you are behind a proxy, please make sure that the
npm ERR! network 'proxy' config is set properly.  See: 'npm help config'
npm timing npm Completed in 402025ms

npm ERR! A complete log of this run can be found in:
npm ERR!     /openwrt/tmp/npm-cache-uZxO3wdShs/_logs/2021-03-08T20_35_32_853Z-debug.log
make[3]: *** [Makefile:86: /openwrt/build_dir/target-x86_64_musl/node-homebridge-cmd4-3.2.2/.built] Error 1
```
