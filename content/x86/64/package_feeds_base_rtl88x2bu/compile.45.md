---
title: "compile.45"
date: 2021-09-01 09:23:40.567682
hidden: false
draft: false
weight: -45
---

build number: `45`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/base/rtl88x2bu/compile -j$(nproc) || make package/feeds/base/rtl88x2bu/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-use-kernel-byteorder.patch using plaintext: 
patching file include/drv_types.h

Applying ./patches/010-remove-repeat-flies.patch using plaintext: 
patching file include/drv_conf.h
patching file include/linux/old_unused_rtl_wireless.h (renamed from include/linux/wireless.h)
patching file include/rtl_autoconf.h (renamed from include/autoconf.h)

Applying ./patches/020-wireless-5.8.patch using plaintext: 
patching file os_dep/linux/ioctl_cfg80211.c
make[3]: *** No rule to make target '/openwrt/staging_dir/target-x86_64_musl/usr/include/mac80211-backport/backport/autoconf.h', needed by '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/rtl88x2bu-2021-01-21-48e7c19c/.configured_68b329da9893e34099c7d8ad5cb9c940'.  Stop.
```
