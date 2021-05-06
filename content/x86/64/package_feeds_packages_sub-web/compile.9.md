---
title: "compile.9"
date: 2021-05-06 11:38:33.960080
hidden: false
draft: false
weight: -9
---

build number: `9`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/sub-web/compile -j$(nproc) || make package/feeds/packages/sub-web/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-dist-support-run-in-curdir.patch using plaintext: 
patching file src/router/index.js
patching file vue.config.js

Applying ./patches/020-views-add-examples-from-ACL4SSR-and-Subconverter.patch using plaintext: 
patching file src/views/Subconverter.vue
yarn install v1.22.10
[1/4] Resolving packages...
[2/4] Fetching packages...
error An unexpected error occurred: "https://registry.npmjs.org/@vue/babel-sugar-composition-api-render-instance/-/babel-sugar-composition-api-render-instance-1.2.4.tgz: Request failed \"404 Not Found\"".
info If you think this is a bug, please open a bug report with the information provided in "/openwrt/build_dir/target-x86_64_musl/sub-web-1.0.0/yarn-error.log".
info Visit https://yarnpkg.com/en/docs/cli/install for documentation about this command.
yarn run v1.22.10
$ vue-cli-service build
/bin/sh: 1: vue-cli-service: not found
error Command failed with exit code 127.
info Visit https://yarnpkg.com/en/docs/cli/run for documentation about this command.
make[3]: *** [Makefile:58: /openwrt/build_dir/target-x86_64_musl/sub-web-1.0.0/.built] Error 127
```
