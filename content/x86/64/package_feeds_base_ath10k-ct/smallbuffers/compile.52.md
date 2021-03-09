---
title: "compile.52"
date: 2021-03-09 13:47:05.828429
hidden: false
draft: false
weight: -52
---

build number: `52`

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
Applying ./patches/161-ath10k-add-support-for-configuring-management-packet.patch using plaintext: 
patching file ath10k-4.19/mac.c

Applying ./patches/162-ath10k-fix-possible-out-of-bound-access-of-ath10k_ra.patch using plaintext: 
patching file ath10k-4.19/mac.c

Applying ./patches/163-ath10k-fix-incorrect-multicast-broadcast-rate-settin.patch using plaintext: 
patching file ath10k-4.19/mac.c

Applying ./patches/164-ath10k-commit-rates-from-mac80211.patch using plaintext: 
patching file ath10k-4.19/mac.c

Applying ./patches/201-ath10k-4.16_add-LED-and-GPIO-controlling-support-for-various-chipsets.patch using plaintext: 
patching file ath10k-4.19/Kconfig
patching file ath10k-4.19/Makefile
patching file ath10k-4.19/core.c
patching file ath10k-4.19/core.h
patching file ath10k-4.19/hw.h
patching file ath10k-4.19/leds.c
patching file ath10k-4.19/leds.h
patching file ath10k-4.19/mac.c
patching file ath10k-4.19/wmi-ops.h
patching file ath10k-4.19/wmi-tlv.c
patching file ath10k-4.19/wmi.c
patching file ath10k-4.19/wmi.h

Applying ./patches/202-ath10k-4.16-use-tpt-trigger-by-default.patch using plaintext: 
patching file ath10k-4.19/core.h
patching file ath10k-4.19/leds.c
patching file ath10k-4.19/mac.c

Applying ./patches/203-ath10k-Limit-available-channels-via-DT-ieee80211-fre.patch using plaintext: 
patching file ath10k-4.19/mac.c

Applying ./patches/960-0010-ath10k-limit-htt-rx-ring-size.patch using plaintext: 
patching file ath10k-4.19/htt.h
patching file ath10k-5.2/htt.h

Applying ./patches/960-0011-ath10k-limit-pci-buffer-size.patch using plaintext: 
patching file ath10k-4.19/pci.c
patching file ath10k-5.2/pci.c
make[3]: *** No rule to make target '/openwrt/staging_dir/target-x86_64_musl/usr/include/mac80211-backport/backport/autoconf.h', needed by '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/ath10k-ct-smallbuffers/ath10k-ct-2019-09-09-5e8cd86f/.configured_68b329da9893e34099c7d8ad5cb9c940'.  Stop.
```
