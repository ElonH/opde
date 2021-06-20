---
title: "compile.37"
date: 2021-06-20 22:24:36.850443
hidden: false
draft: false
weight: -37
---

build number: `37`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/php7-pecl-krb5/compile -j$(nproc) || make package/feeds/packages/php7-pecl-krb5/compile V=s
```

#### Compile.txt

``` bash
bash: /openwrt/staging_dir/target-mips_24kc_musl/usr/bin/phpize7: No such file or directory
make[3]: *** [Makefile:46: /openwrt/build_dir/target-mips_24kc_musl/pecl-php7/krb5-1.1.4/.prepared_9a71df7e8d1f05dfd2b150dcc5a5dce6_18f1e190c5d53547fed41a3eaa76e9e9] Error 127
```
