---
title: "compile.40"
date: 2021-06-22 10:45:15.514886
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
make package/feeds/packages/php7-pecl-krb5/compile -j$(nproc) || make package/feeds/packages/php7-pecl-krb5/compile V=s
```

#### Compile.txt

``` bash
bash: /openwrt/staging_dir/target-mips_24kc_musl/usr/bin/phpize7: No such file or directory
make[3]: *** [Makefile:46: /openwrt/build_dir/target-mips_24kc_musl/pecl-php7/krb5-1.1.4/.prepared_b9a064d22fcbfb46da0422d179436611_18f1e190c5d53547fed41a3eaa76e9e9] Error 127
```
