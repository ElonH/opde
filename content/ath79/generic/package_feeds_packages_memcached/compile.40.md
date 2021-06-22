---
title: "compile.40"
date: 2021-06-22 10:37:31.208835
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
make package/feeds/packages/memcached/compile -j$(nproc) || make package/feeds/packages/memcached/compile V=s
```

#### Compile.txt

``` bash
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/mips
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking for mips-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
checking whether ccache_cc understands -c and -o together... yes
checking whether make supports the include directive... yes (GNU style)
checking dependency style of ccache_cc... gcc3
checking how to run the C preprocessor... ccache_cc -E
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for icc in use... no
checking for clang in use... no
checking for ANSI C header files... yes
checking for sys/types.h... yes
checking for sys/stat.h... yes
checking for stdlib.h... yes
checking for string.h... yes
checking for memory.h... yes
checking for strings.h... yes
checking for inttypes.h... yes
checking for stdint.h... yes
checking for unistd.h... yes
checking whether __SUNPRO_C is declared... no
checking for ccache_cc option to accept ISO C99... none needed
checking sasl/sasl.h usability... yes
checking sasl/sasl.h presence... yes
checking for sasl/sasl.h... yes
checking size of void *... (cached) 4
checking for library containing clock_gettime... none required
checking for library containing socket... none required
checking for library containing gethostbyname... none required
checking for libevent directory... configure: error: libevent is required.  You can get it from https://www.monkey.org/~provos/libevent/

      If it's already installed, specify its path using --with-libevent=/dir/

make[3]: *** [Makefile:67: /openwrt/build_dir/target-mips_24kc_musl/memcached-1.6.9/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
