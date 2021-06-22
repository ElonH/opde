---
title: "compile.40"
date: 2021-06-22 10:50:06.153126
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
make package/feeds/packages/nmap/compile -j$(nproc) || make package/feeds/packages/nmap/compile V=s
```

#### Compile.txt

``` bash
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91'
Compiling libnetutil
cd libnetutil && make
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libnetutil'
make[5]: Nothing to be done for 'all'.
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libnetutil'
Compiling liblinear
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/liblinear'
make[5]: 'liblinear.a' is up to date.
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/liblinear'
Compiling libssh2
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libssh2/src'
make  all-am
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libssh2/src'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libssh2/src'
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libssh2/src'
cd libssh2/src && make libdir="/lib" prefix="" DESTDIR=/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libssh2 install-libLTLIBRARIES;
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libssh2/src'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libssh2/lib'
 /bin/bash ../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libssh2.la '/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libssh2/lib'
libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libssh2.so.1.0.1 /openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libssh2/lib/libssh2.so.1.0.1
libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libssh2/lib && { ln -s -f libssh2.so.1.0.1 libssh2.so.1 || { rm -f libssh2.so.1 && ln -s libssh2.so.1.0.1 libssh2.so.1; }; })
libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libssh2/lib && { ln -s -f libssh2.so.1.0.1 libssh2.so || { rm -f libssh2.so && ln -s libssh2.so.1.0.1 libssh2.so; }; })
libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libssh2.lai /openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libssh2/lib/libssh2.la
libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libssh2.a /openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libssh2/lib/libssh2.a
libtool: install: chmod 644 /openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libssh2/lib/libssh2.a
libtool: install: mips-openwrt-linux-musl-gcc-ranlib /openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libssh2/lib/libssh2.a
libtool: warning: remember to run 'libtool --finish /usr/lib'
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libssh2/src'
Compiling libnbase
cd nbase && make
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/nbase'
make[5]: Nothing to be done for 'all'.
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/nbase'
Compiling libdnet
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libdnet-stripped'
Making all in include
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libdnet-stripped/include'
make  all-recursive
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libdnet-stripped/include'
Making all in dnet
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libdnet-stripped/include/dnet'
make[8]: Nothing to be done for 'all'.
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libdnet-stripped/include/dnet'
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libdnet-stripped/include'
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libdnet-stripped/include'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libdnet-stripped/include'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libdnet-stripped/include'
Making all in src
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libdnet-stripped/src'
make[6]: Nothing to be done for 'all'.
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libdnet-stripped/src'
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libdnet-stripped'
make[6]: Nothing to be done for 'all-am'.
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libdnet-stripped'
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/libdnet-stripped'
ccache_cxx -c -I./liblinear -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I./libdnet-stripped/include -I./libssh2/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I./nbase -I./nsock/include -DHAVE_CONFIG_H -DNMAP_PLATFORM=\"mips-openwrt-linux-gnu\" -DNMAPDATADIR=\"/usr/share/nmap\" -D_FORTIFY_SOURCE=2 -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91=nmap-7.91 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -Wall -fno-strict-aliasing   nmap.cc -o nmap.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
nmap.cc:113:10: fatal error: openssl/opensslv.h: No such file or directory
 #include <openssl/opensslv.h>
          ^~~~~~~~~~~~~~~~~~~~
compilation terminated.
make[4]: *** [Makefile:120: nmap.o] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91'
make[3]: *** [Makefile:196: /openwrt/build_dir/target-mips_24kc_musl/nmap-full/nmap-7.91/.built] Error 2
```
