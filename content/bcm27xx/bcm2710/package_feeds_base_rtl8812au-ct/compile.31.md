---
title: "compile.31"
date: 2021-06-10 17:14:47.825091
hidden: false
draft: false
weight: -31
---

build number: `31`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/base/rtl8812au-ct/compile -j$(nproc) || make package/feeds/base/rtl8812au-ct/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-use-kernel-byteorder.patch using plaintext: 
patching file include/drv_types.h

Applying ./patches/002-vendor_command_policy.patch using plaintext: 
patching file os_dep/linux/rtw_cfgvendor.c

Applying ./patches/003-wireless-5.8.patch using plaintext: 
patching file os_dep/linux/ioctl_cfg80211.c
make[3]: *** No rule to make target '/openwrt/staging_dir/target-aarch64_cortex-a53_musl/usr/include/mac80211-backport/backport/autoconf.h', needed by '/openwrt/build_dir/target-aarch64_cortex-a53_musl/linux-bcm27xx_bcm2710/rtl8812au-ct-2020-12-07-1e9689c8/.configured_68b329da9893e34099c7d8ad5cb9c940'.  Stop.
```
