---
title: "compile.42"
date: 2021-06-29 09:25:37.109982
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
make package/feeds/packages/php7-pecl-libevent/compile -j$(nproc) || make package/feeds/packages/php7-pecl-libevent/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-libevent2.patch using plaintext: 
patching file libevent.c
bash: /openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/bin/phpize7: No such file or directory
make[3]: *** [Makefile:46: /openwrt/build_dir/target-aarch64_cortex-a72_musl/pecl-php7/libevent-ce255e7e1e293030951fd68d5df06b2a4c077a89/.prepared_ff1215360c5be5e59742d6b9c79e7ad6_18f1e190c5d53547fed41a3eaa76e9e9] Error 127
```
