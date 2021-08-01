---
title: "compile.37"
date: 2021-06-20 22:23:59.883042
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
make package/feeds/base/rtl8192du/compile -j$(nproc) || make package/feeds/base/rtl8192du/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-missing-header-in-ipv6.patch using plaintext: 
patching file core/rtw_br_ext.c

Applying ./patches/020-wireless-5.8.patch using plaintext: 
patching file os_dep/ioctl_cfg80211.c
make[3]: *** No rule to make target '/openwrt/staging_dir/target-mips_24kc_musl/usr/include/mac80211-backport/backport/autoconf.h', needed by '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/rtl8192du-2020-12-12-331ec03d/.configured_68b329da9893e34099c7d8ad5cb9c940'.  Stop.
```