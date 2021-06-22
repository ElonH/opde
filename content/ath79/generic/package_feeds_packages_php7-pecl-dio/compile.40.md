---
title: "compile.40"
date: 2021-06-22 10:45:15.548208
hidden: false
draft: false
weight: -40
---

build number: `40`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/php7-pecl-dio/compile -j$(nproc) || make package/feeds/packages/php7-pecl-dio/compile V=s
```

#### Compile.txt

``` bash
bash: /openwrt/staging_dir/target-mips_24kc_musl/usr/bin/phpize7: No such file or directory
make[3]: *** [Makefile:41: /openwrt/build_dir/target-mips_24kc_musl/pecl-php7/dio-0.2.0/.prepared_8dea7ca0e4398674898598ae050d73bb_18f1e190c5d53547fed41a3eaa76e9e9] Error 127
```
