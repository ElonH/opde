---
title: "compile.30"
date: 2021-06-09 21:54:28.981093
hidden: false
draft: false
weight: -30
---

build number: `30`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/base/rtl8188eu/compile -j$(nproc) || make package/feeds/base/rtl8188eu/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-use-kernel-byteorder.patch using plaintext: 
patching file include/drv_types.h

Applying ./patches/010-disable-default-build-x86.patch using plaintext: 
patching file Makefile

Applying ./patches/020-remove-repeat-flies.patch using plaintext: 
patching file include/drv_conf.h
patching file include/linux/old_unused_rtl_wireless.h (renamed from include/linux/wireless.h)
patching file include/rtl_autoconf.h (renamed from include/autoconf.h)

Applying ./patches/030-wireless-5.8.patch using plaintext: 
patching file os_dep/linux/ioctl_cfg80211.c
make[3]: *** No rule to make target '/openwrt/staging_dir/target-x86_64_musl/usr/include/mac80211-backport/backport/autoconf.h', needed by '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/rtl8188eu-2021-02-06-1e7145f3/.configured_68b329da9893e34099c7d8ad5cb9c940'.  Stop.
```
