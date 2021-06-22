---
title: "compile.40"
date: 2021-06-22 10:51:50.600726
hidden: false
draft: false
weight: -40
---

build number: `40`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/base/cryptodev-linux/compile -j$(nproc) || make package/feeds/base/cryptodev-linux/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-fix-build-for-kernel-v5.9-rc1.patch using plaintext: 
patching file zc.c
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/cryptodev-linux-cryptodev-linux-1.11'
make -C /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124 M=/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/cryptodev-linux-cryptodev-linux-1.11 ARCH=mips CROSS_COMPILE=mips-openwrt-linux-musl- modules
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124'
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/cryptodev-linux-cryptodev-linux-1.11/ioctl.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/cryptodev-linux-cryptodev-linux-1.11/main.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/cryptodev-linux-cryptodev-linux-1.11/cryptlib.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/cryptodev-linux-cryptodev-linux-1.11/authenc.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/cryptodev-linux-cryptodev-linux-1.11/zc.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/cryptodev-linux-cryptodev-linux-1.11/util.o
  LD [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/cryptodev-linux-cryptodev-linux-1.11/cryptodev.o
  Building modules, stage 2.
  MODPOST 1 modules
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/cryptodev-linux-cryptodev-linux-1.11/cryptodev.mod.o
  LD [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/cryptodev-linux-cryptodev-linux-1.11/cryptodev.ko
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124'
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/cryptodev-linux-cryptodev-linux-1.11'
Package kmod-cryptodev is missing dependencies for the following libraries:
aead.ko
crypto_hash.ko
make[3]: *** [Makefile:68: /openwrt/bin/targets/ath79/generic/packages/kmod-cryptodev_5.4.124+1.11-ath79-1_mips_24kc.ipk] Error 1
```
