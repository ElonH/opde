---
title: "compile.37"
date: 2021-06-20 22:36:26.358823
hidden: false
draft: false
weight: -37
---

build number: `37`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/ratched/compile -j$(nproc) || make package/feeds/packages/ratched/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/0001-Disable-non-IANA-TLS-extensions.patch using plaintext: 
patching file openssl_clienthello.c

Applying ./patches/0002-openssl-fix-compilation-without-deprecated-APIs.patch using plaintext: 
patching file openssl.c
patching file openssl_certs.c
patching file openssl_tls.c
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/ratched-1.0.0'
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/ratched-1.0.0=ratched-1.0.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DBUILD_TIMESTAMP_UTC="\"unknown\"" -DBUILD_REVISION="\"1.0.0-1\""   -c -o atomic.o atomic.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/ratched-1.0.0=ratched-1.0.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DBUILD_TIMESTAMP_UTC="\"unknown\"" -DBUILD_REVISION="\"1.0.0-1\""   -c -o certforgery.o certforgery.c
certforgery.c:30:10: fatal error: openssl/evp.h: No such file or directory
 #include <openssl/evp.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
make[4]: *** [<builtin>: certforgery.o] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/ratched-1.0.0'
make[3]: *** [Makefile:40: /openwrt/build_dir/target-mips_24kc_musl/ratched-1.0.0/.built] Error 2
```
