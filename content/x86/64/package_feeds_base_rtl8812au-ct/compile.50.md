---
title: "compile.50"
date: 2021-02-25 14:20:49.075352
hidden: false
draft: false
weight: -50
---

build number: `50`

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
make[3]: *** No rule to make target '/openwrt/staging_dir/target-x86_64_musl/usr/include/mac80211-backport/backport/autoconf.h', needed by '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/rtl8812au-ct-2020-01-13-e0d586aa/.configured_68b329da9893e34099c7d8ad5cb9c940'.  Stop.
```
