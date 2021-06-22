---
title: "compile.40"
date: 2021-06-22 10:50:44.055248
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
make package/feeds/packages/apk/compile -j$(nproc) || make package/feeds/packages/apk/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/0001-remove-doc-generation.patch using plaintext: 
patching file Makefile

Applying ./patches/010-openssl-deprecated.patch using plaintext: 
patching file libfetch/common.c
patching file src/apk.c
patching file src/apk_openssl.h
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/apk-tools-v2.12.4'
  GENERR  libfetch/ftperr.h
  GENERR  libfetch/httperr.h
  CC      libfetch/common.o
In file included from libfetch/common.h:41,
                 from libfetch/common.c:54:
libfetch/openssl-compat.h:1:10: fatal error: openssl/crypto.h: No such file or directory
 #include <openssl/crypto.h>
          ^~~~~~~~~~~~~~~~~~
compilation terminated.
make[5]: *** [Make.rules:221: libfetch/common.o] Error 1
make[4]: *** [Make.rules:337: libfetch/] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/apk-tools-v2.12.4'
make[3]: *** [Makefile:76: /openwrt/build_dir/target-mips_24kc_musl/apk-tools-v2.12.4/.built] Error 2
```
