---
title: "compile.40"
date: 2021-06-22 10:37:31.190307
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
make package/feeds/packages/qBittorrent-Enhanced-Edition/compile -j$(nproc) || make package/feeds/packages/qBittorrent-Enhanced-Edition/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-remove-host-include-dir.patch using plaintext: 
patching file conf.pri.in
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/mips
checking for mips-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether the compiler supports GNU C... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to enable C11 features... none needed
checking whether ccache_cc understands -c and -o together... yes
checking whether the compiler supports GNU C++... yes
checking whether ccache_cxx accepts -g... yes
checking for ccache_cxx option to enable C++11 features... none needed
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a race-free mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports the include directive... yes (GNU style)
checking whether make supports nested variables... yes
checking dependency style of ccache_cc... none
checking dependency style of ccache_cxx... none
checking whether OS is FreeBSD... no
checking whether OS is macOS... no
checking pkg-config is at least version 0.23... yes
checking whether to enable the Debug build... no
checking whether to enable the stacktrace feature... no
checking whether to enable the GUI... no
checking whether to install the systemd service file... no
checking whether to enable the WebUI... yes
checking for Qt5 qmake >= 5.11... not found
configure: error: Could not find qmake
make[3]: *** [Makefile:64: /openwrt/build_dir/target-mips_24kc_musl/qBittorrent-Enhanced-Edition-release-4.3.4.10/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
