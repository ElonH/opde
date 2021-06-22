---
title: "compile.40"
date: 2021-06-22 10:46:12.813327
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
make package/feeds/packages/chaosvpn/compile -j$(nproc) || make package/feeds/packages/chaosvpn/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/0001-OpenSSL-1.1.0-compile-fix.patch using plaintext: 
patching file crypto.c

Applying ./patches/010-openssl-deprecated.patch using plaintext: 
patching file crypto.c

Applying ./patches/020-cdefs.patch using plaintext: 
patching file ar.h
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/chaosvpn-2.19'
yacc -d cvconf.y
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/chaosvpn-2.19=chaosvpn-2.19 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -std=c99 -D_POSIX_C_SOURCE=2 -D_BSD_SOURCE -D_FILE_OFFSET_BITS=64 -O2 -Wall -g -I/usr/local/include -DPREFIX="\"/usr\"" -DTINCDIR="\"/etc/tinc\"" -o main.o -c main.c
In file included from main.c:18:
chaosvpn.h:16:10: fatal error: openssl/ssl.h: No such file or directory
 #include <openssl/ssl.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
make[4]: *** [Makefile:55: main.o] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/chaosvpn-2.19'
make[3]: *** [Makefile:54: /openwrt/build_dir/target-mips_24kc_musl/chaosvpn-2.19/.built] Error 2
```
