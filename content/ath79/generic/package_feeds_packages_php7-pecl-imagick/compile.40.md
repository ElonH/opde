---
title: "compile.40"
date: 2021-06-22 10:51:50.608616
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
make package/feeds/packages/php7-pecl-imagick/compile -j$(nproc) || make package/feeds/packages/php7-pecl-imagick/compile V=s
```

#### Compile.txt

``` bash
bash: /openwrt/staging_dir/target-mips_24kc_musl/usr/bin/phpize7: No such file or directory
make[3]: *** [Makefile:44: /openwrt/build_dir/target-mips_24kc_musl/pecl-php7/imagick-3.4.4/.prepared_92f34ff1f35e9b527acae28e67a3fdeb_18f1e190c5d53547fed41a3eaa76e9e9] Error 127
```
