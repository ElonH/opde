---
title: "compile.27"
date: 2021-06-03 07:43:02.898543
hidden: false
draft: false
weight: -27
---

build number: `27`

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
make[4]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/linux-5.4.123'
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-regular/ath10k-ct-2021-01-11-9fe1df7d/ath10k-5.10/mac.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-regular/ath10k-ct-2021-01-11-9fe1df7d/ath10k-5.10/debug.o
/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-regular/ath10k-ct-2021-01-11-9fe1df7d/ath10k-5.10/debug.c: In function 'ath10k_read_debug_level':
/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-regular/ath10k-ct-2021-01-11-9fe1df7d/ath10k-5.10/debug.c:1388:1: warning: the frame size of 1456 bytes is larger than 1024 bytes [-Wframe-larger-than=]
 }
 ^
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-regular/ath10k-ct-2021-01-11-9fe1df7d/ath10k-5.10/core.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-regular/ath10k-ct-2021-01-11-9fe1df7d/ath10k-5.10/coredump.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-regular/ath10k-ct-2021-01-11-9fe1df7d/ath10k-5.10/htc.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-regular/ath10k-ct-2021-01-11-9fe1df7d/ath10k-5.10/htt.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-regular/ath10k-ct-2021-01-11-9fe1df7d/ath10k-5.10/htt_rx.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-regular/ath10k-ct-2021-01-11-9fe1df7d/ath10k-5.10/htt_tx.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-regular/ath10k-ct-2021-01-11-9fe1df7d/ath10k-5.10/txrx.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-regular/ath10k-ct-2021-01-11-9fe1df7d/ath10k-5.10/wmi.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-regular/ath10k-ct-2021-01-11-9fe1df7d/ath10k-5.10/wmi-tlv.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-regular/ath10k-ct-2021-01-11-9fe1df7d/ath10k-5.10/bmi.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-regular/ath10k-ct-2021-01-11-9fe1df7d/ath10k-5.10/hw.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-regular/ath10k-ct-2021-01-11-9fe1df7d/ath10k-5.10/p2p.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-regular/ath10k-ct-2021-01-11-9fe1df7d/ath10k-5.10/swap.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-regular/ath10k-ct-2021-01-11-9fe1df7d/ath10k-5.10/thermal.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-regular/ath10k-ct-2021-01-11-9fe1df7d/ath10k-5.10/leds.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-regular/ath10k-ct-2021-01-11-9fe1df7d/ath10k-5.10/debugfs_sta.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-regular/ath10k-ct-2021-01-11-9fe1df7d/ath10k-5.10/wow.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-regular/ath10k-ct-2021-01-11-9fe1df7d/ath10k-5.10/ce.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-regular/ath10k-ct-2021-01-11-9fe1df7d/ath10k-5.10/pci.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-regular/ath10k-ct-2021-01-11-9fe1df7d/ath10k-5.10/ahb.o
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-regular/ath10k-ct-2021-01-11-9fe1df7d/ath10k-5.10/ath10k_core.o
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-regular/ath10k-ct-2021-01-11-9fe1df7d/ath10k-5.10/ath10k_pci.o
  Building modules, stage 2.
  MODPOST 2 modules
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-regular/ath10k-ct-2021-01-11-9fe1df7d/ath10k-5.10/ath10k_core.mod.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-regular/ath10k-ct-2021-01-11-9fe1df7d/ath10k-5.10/ath10k_pci.mod.o
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-regular/ath10k-ct-2021-01-11-9fe1df7d/ath10k-5.10/ath10k_core.ko
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/ath10k-ct-regular/ath10k-ct-2021-01-11-9fe1df7d/ath10k-5.10/ath10k_pci.ko
make[4]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/linux-5.4.123'
Package kmod-ath10k-ct is missing dependencies for the following libraries:
hwmon.ko
make[3]: *** [Makefile:131: /openwrt/bin/targets/bcm27xx/bcm2711/packages/kmod-ath10k-ct_5.4.123+2021-01-11-9fe1df7d-2_aarch64_cortex-a72.ipk] Error 1
```
