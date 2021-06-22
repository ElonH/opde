---
title: "compile.40"
date: 2021-06-22 10:45:15.518305
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
make package/feeds/packages/exim/compile -j$(nproc) || make package/feeds/packages/exim/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-allow-json-dynamic-lookup.patch using plaintext: 
patching file src/drtables.c

Applying ./patches/030-openssl-deprecated.patch using plaintext: 
patching file src/dane-openssl.c
patching file src/pdkim/signing.c
patching file src/tls-openssl.c
patching file src/tlscert-openssl.c

Applying ./patches/100-localscan_dlopen.patch using plaintext: 
patching file src/config.h.defaults
patching file src/EDITME
patching file src/globals.c
patching file src/globals.h
patching file src/local_scan.c
patching file src/readconf.c
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/exim-gnutls/exim-4.94.2'

>>> Creating links to source files...
>>> Creating lookups/Makefile for building dynamic modules
>>> New Makefile & lookups/Makefile installed
>>> Use "make makefile" if you need to force rebuilding of the makefile
 
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/exim-gnutls/exim-4.94.2'
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/exim-gnutls/exim-4.94.2/build-Linux-mips'
cc buildconfig.c
/bin/sh ../scripts/Configure-config.h "make"
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/exim-gnutls/exim-4.94.2/build-Linux-mips'
make[5]: 'buildconfig' is up to date.
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/exim-gnutls/exim-4.94.2/build-Linux-mips'
Building configuration file config.h
>>> config.h built

cc -DMACRO_PREDEF macro_predef.c
In file included from hash.h:14,
                 from exim.h:530,
                 from macro_predef.c:12:
sha_ver.h:24:12: fatal error: gnutls/gnutls.h: No such file or directory
   24 | #  include <gnutls/gnutls.h>
      |            ^~~~~~~~~~~~~~~~~
compilation terminated.
make[4]: *** [Makefile:267: macro_predef.o] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/exim-gnutls/exim-4.94.2/build-Linux-mips'
make[3]: *** [Makefile:338: /openwrt/build_dir/target-mips_24kc_musl/exim-gnutls/exim-4.94.2/.configured_d92a942a8d749d03d3e878ee19749a25] Error 2
```
