---
title: "compile.11"
date: 2021-05-07 23:27:17.243241
hidden: false
draft: false
weight: -11
---

build number: `11`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/base/rtl8821cu/compile -j$(nproc) || make package/feeds/base/rtl8821cu/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-use-kernel-byteorder.patch using plaintext: 
patching file include/drv_types.h

Applying ./patches/010-remove-extra-cflags.patch using plaintext: 
patching file Makefile

Applying ./patches/020-remove-repeat-flies.patch using plaintext: 
patching file include/drv_conf.h
patching file include/linux/old_unused_rtl_wireless.h (renamed from include/linux/wireless.h)
patching file include/rtl_autoconf.h (renamed from include/autoconf.h)

Applying ./patches/030-change-value-of-vht-enable.patch using plaintext: 
patching file os_dep/linux/os_intfs.c

Applying ./patches/040-wireless-5.4.patch using plaintext: 
patching file os_dep/linux/os_intfs.c
make[3]: *** No rule to make target '/openwrt/staging_dir/target-x86_64_musl/usr/include/mac80211-backport/backport/autoconf.h', needed by '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/rtl8821cu-2020-12-19-428a0820/.configured_68b329da9893e34099c7d8ad5cb9c940'.  Stop.
```
