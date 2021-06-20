---
title: "compile.37"
date: 2021-06-20 22:36:26.326280
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
make package/feeds/packages/addrwatch/compile -j$(nproc) || make package/feeds/packages/addrwatch/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/002-fix-uclibc-sysconf.patch using plaintext: 
patching file src/addrwatch.c
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/mips
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
checking for pcap_open_live in -lpcap... yes
checking for shm_open in -lrt... yes
checking pkg-config is at least version 0.9.0... yes
checking for LIBEVENT... no
checking for event_dispatch in -levent... no
configure: error: Please install libevent-1.4 or libevent-2.0
make[3]: *** [Makefile:58: /openwrt/build_dir/target-mips_24kc_musl/addrwatch-1.0.2/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
