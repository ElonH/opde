---
title: "compile.62"
date: 2021-05-05 13:47:41.267910
hidden: false
draft: false
weight: -62
---

build number: `62`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/base/rtl8192du/compile -j$(nproc) || make package/feeds/base/rtl8192du/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-missing-header-in-ipv6.patch using plaintext: 
patching file core/rtw_br_ext.c
make[3]: *** No rule to make target '/openwrt/staging_dir/target-x86_64_musl/usr/include/mac80211-backport/backport/autoconf.h', needed by '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/rtl8192du-2019-06-01-54c95aaa/.configured_68b329da9893e34099c7d8ad5cb9c940'.  Stop.
```
