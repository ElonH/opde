---
title: "compile.42"
date: 2021-06-29 09:38:24.595368
hidden: false
draft: false
weight: -42
---

build number: `42`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/libmpdclient/compile -j$(nproc) || make package/feeds/packages/libmpdclient/compile V=s
```

#### Compile.txt

``` bash
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/libmpdclient-2.19
Build dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/libmpdclient-2.19/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: libmpdclient
Project version: 2.19
C compiler for the host machine: ccache_cc (gcc 8.4.0 "aarch64-openwrt-linux-musl-gcc (OpenWrt GCC 8.4.0 r0-af265d3) 8.4.0")
C linker for the host machine: ccache_cc ld.bfd 2.34
C compiler for the build machine: ccache gcc (gcc 9.3.0 "gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0")
C linker for the build machine: gcc ld.bfd 2.34
Build machine cpu family: x86_64
Build machine cpu: x86_64
Host machine cpu family: aarch64
Host machine cpu: generic
Target machine cpu family: aarch64
Target machine cpu: generic
Checking for function "strndup" : YES 
Checking for function "getaddrinfo" : YES 
Configuring config.h using configuration
Configuring version.h using configuration
Compiler for C supports arguments -Wall: YES 
Compiler for C supports arguments -Wextra: YES 
Compiler for C supports arguments -Wno-deprecated-declarations: YES 
Compiler for C supports arguments -Wmissing-prototypes: YES 
Compiler for C supports arguments -Wshadow: YES 
Compiler for C supports arguments -Wpointer-arith: YES 
Compiler for C supports arguments -Wstrict-prototypes: YES 
Compiler for C supports arguments -Wcast-qual: YES 
Compiler for C supports arguments -Wwrite-strings: YES 
../../../../build_dir/target-aarch64_cortex-a72_musl/libmpdclient-2.19/meson.build:70: WARNING: Consider using the built-in warning_level option instead of using "-Wall".
../../../../build_dir/target-aarch64_cortex-a72_musl/libmpdclient-2.19/meson.build:70: WARNING: Consider using the built-in warning_level option instead of using "-Wextra".
Compiler for C supports link arguments -Wl,--version-script=/openwrt/build_dir/target-aarch64_cortex-a72_musl/libmpdclient-2.19/libmpdclient.ld: YES 
Build targets in project: 2


ERROR: Could not detect Ninja v1.8.2 or newer

A full log can be found at /openwrt/build_dir/target-aarch64_cortex-a72_musl/libmpdclient-2.19/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:69: /openwrt/build_dir/target-aarch64_cortex-a72_musl/libmpdclient-2.19/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
