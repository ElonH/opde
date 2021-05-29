---
title: "compile.24"
date: 2021-05-29 09:29:33.539184
hidden: false
draft: false
weight: -24
---

build number: `24`

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
Applying ./patches/164-ath10k-commit-rates-from-mac80211.patch using plaintext: 
patching file ath10k-5.10/mac.c

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

Applying ./patches/960-0010-ath10k-limit-htt-rx-ring-size.patch using plaintext: 
patching file ath10k-5.10/htt.h

Applying ./patches/960-0011-ath10k-limit-pci-buffer-size.patch using plaintext: 
patching file ath10k-5.10/pci.c
make[3]: *** No rule to make target '/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include/mac80211-backport/backport/autoconf.h', needed by '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-smallbuffers/ath10k-ct-2021-01-11-9fe1df7d/.configured_68b329da9893e34099c7d8ad5cb9c940'.  Stop.
```
