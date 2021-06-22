---
title: "compile.40"
date: 2021-06-22 10:46:12.807351
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
make package/feeds/base/hostapd/compile -j$(nproc) || make package/feeds/base/hostapd/compile V=s
```

#### Compile.txt

``` bash
Makefile:705: WARNING: skipping hostapd-utils -- package has no install section
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/hostapd-supplicant-full-openssl/hostapd-2021-05-22-b102f19b/wpa_supplicant'
  LD  wpa_cli
../src/crypto/tls_openssl.c:19:10: fatal error: openssl/ssl.h: No such file or directory
 #include <openssl/ssl.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
make[4]: *** [../src/build.rules:86: /openwrt/build_dir/target-mips_24kc_musl/hostapd-supplicant-full-openssl/hostapd-2021-05-22-b102f19b/build/wpa_supplicant/src/crypto/tls_openssl.o] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/hostapd-supplicant-full-openssl/hostapd-2021-05-22-b102f19b/wpa_supplicant'
make[3]: *** [Makefile:683: /openwrt/build_dir/target-mips_24kc_musl/hostapd-supplicant-full-openssl/hostapd-2021-05-22-b102f19b/.built] Error 2
```
