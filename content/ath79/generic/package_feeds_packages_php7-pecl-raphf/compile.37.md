---
title: "compile.37"
date: 2021-06-20 22:25:23.597353
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
make package/feeds/packages/php7-pecl-raphf/compile -j$(nproc) || make package/feeds/packages/php7-pecl-raphf/compile V=s
```

#### Compile.txt

``` bash
bash: /openwrt/staging_dir/target-mips_24kc_musl/usr/bin/phpize7: No such file or directory
make[3]: *** [Makefile:50: /openwrt/build_dir/target-mips_24kc_musl/pecl-php7/raphf-2.0.1/.prepared_04a3d95f6a95a84d08a15da9a235c4bb_18f1e190c5d53547fed41a3eaa76e9e9] Error 127
```
