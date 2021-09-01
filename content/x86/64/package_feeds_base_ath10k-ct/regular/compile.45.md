---
title: "compile.45"
date: 2021-09-01 09:23:40.566977
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
make package/feeds/base/ath10k-ct/compile -j$(nproc) || make package/feeds/base/ath10k-ct/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/201-ath10k-add-LED-and-GPIO-controlling-support-for-various-chipsets.patch using plaintext: 
patching file ath10k-5.10/Kconfig
patching file ath10k-5.10/Makefile
patching file ath10k-5.10/core.c
patching file ath10k-5.10/core.h
patching file ath10k-5.10/hw.h
patching file ath10k-5.10/leds.c
patching file ath10k-5.10/leds.h
patching file ath10k-5.10/mac.c
patching file ath10k-5.10/wmi-ops.h
patching file ath10k-5.10/wmi-tlv.c
patching file ath10k-5.10/wmi.c
patching file ath10k-5.10/wmi.h

Applying ./patches/202-ath10k-use-tpt-trigger-by-default.patch using plaintext: 
patching file ath10k-5.10/core.h
patching file ath10k-5.10/leds.c
patching file ath10k-5.10/mac.c

Applying ./patches/203-ath10k-Try-to-get-mac-address-from-dts.patch using plaintext: 
patching file ath10k-5.10/core.c
Hunk #2 succeeded at 3882 (offset 819 lines).

Applying ./patches/960-0010-ath10k-limit-htt-rx-ring-size.patch using plaintext: 
patching file ath10k-5.10/htt.h

Applying ./patches/960-0011-ath10k-limit-pci-buffer-size.patch using plaintext: 
patching file ath10k-5.10/pci.c
make[3]: *** No rule to make target '/openwrt/staging_dir/target-x86_64_musl/usr/include/mac80211-backport/backport/autoconf.h', needed by '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/ath10k-ct-regular/ath10k-ct-2021-06-03-b44cd7b2/.configured_68b329da9893e34099c7d8ad5cb9c940'.  Stop.
```
