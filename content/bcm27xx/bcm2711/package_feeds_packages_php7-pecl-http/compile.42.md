---
title: "compile.42"
date: 2021-06-29 09:32:34.505918
hidden: false
draft: false
weight: -42
---

build number: `42`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/php7-pecl-http/compile -j$(nproc) || make package/feeds/packages/php7-pecl-http/compile V=s
```

#### Compile.txt

``` bash
bash: /openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/bin/phpize7: No such file or directory
make[3]: *** [Makefile:67: /openwrt/build_dir/target-aarch64_cortex-a72_musl/pecl-php7/pecl_http-3.2.3/.prepared_20dfe5d6f40565268898b3ab5f71b82d_18f1e190c5d53547fed41a3eaa76e9e9] Error 127
```
