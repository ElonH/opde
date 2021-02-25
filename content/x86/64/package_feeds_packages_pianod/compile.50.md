---
title: "compile.50"
date: 2021-02-25 14:20:49.081016
hidden: false
draft: false
weight: -50
---

build number: `50`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/pianod/compile -j$(nproc) || make package/feeds/packages/pianod/compile V=s
```

#### Compile.txt

``` bash
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-x86_64_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal -I m4 -I . --force 
autoreconf: configure.ac: tracing
autoreconf: configure.ac: not using Libtool
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-x86_64_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-x86_64_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
configure.ac:19: installing './ar-lib'
configure.ac:13: installing './compile'
configure.ac:9: installing './install-sh'
configure.ac:9: installing './missing'
parallel-tests: installing './test-driver'
src/Makefile.am: installing './depcomp'
autoreconf: Leaving directory `.'
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/x86_64
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for x86_64-openwrt-linux-strip... x86_64-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking for x86_64-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
checking whether ccache_cc understands -c and -o together... yes
checking for style of include used by make... GNU
checking dependency style of ccache_cc... gcc3
checking whether compiler accepts "-std=c99"... yes
checking whether ln -s works... yes
checking for x86_64-openwrt-linux-ranlib... x86_64-openwrt-linux-musl-gcc-ranlib
checking for x86_64-openwrt-linux-ar... x86_64-openwrt-linux-musl-gcc-ar
checking the archiver (x86_64-openwrt-linux-musl-gcc-ar) interface... ar
checking for library containing pow... none required
checking for pthread_create in -lpthread... yes
checking pkg-config is at least version 0.9.0... yes
checking for ao... yes
checking for mpg123... yes
checking for json... yes
checking for gcry_cipher_open in -lgcrypt... yes
>>Using mbedTLS
checking for mbedtls_ssl_set_session in -lmbedtls... no
configure: error: Cannot find required library: libmbedtls
make[3]: *** [Makefile:113: /openwrt/build_dir/target-x86_64_musl/pianod-174.09/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
