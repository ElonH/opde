---
title: "compile.42"
date: 2021-06-29 09:38:24.605636
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
make package/feeds/packages/libinput/compile -j$(nproc) || make package/feeds/packages/libinput/compile V=s
```

#### Compile.txt

``` bash
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/libinput-1.17.1
Build dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/libinput-1.17.1/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: libinput
Project version: 1.17.1
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
Compiler for C supports arguments -Wno-unused-parameter: YES 
Compiler for C supports arguments -Wmissing-prototypes: YES 
Compiler for C supports arguments -Wstrict-prototypes: YES 
Compiler for C supports arguments -Wundef: YES 
Compiler for C supports arguments -Wlogical-op: YES 
Compiler for C supports arguments -Wpointer-arith: YES 
Compiler for C supports arguments -Wuninitialized: YES 
Compiler for C supports arguments -Winit-self: YES 
Compiler for C supports arguments -Wstrict-prototypes: YES (cached)
Compiler for C supports arguments -Wimplicit-fallthrough: YES 
Compiler for C supports arguments -Wredundant-decls: YES 
Compiler for C supports arguments -Wincompatible-pointer-types: YES 
Compiler for C supports arguments -Wformat=2: YES 
Compiler for C supports arguments -Wmissing-declarations: YES 
Compiler for C supports arguments -fvisibility=hidden: YES 
Fetching value of define "static_assert" :  
Header <dirent.h> has symbol "versionsort" : YES 
Header <errno.h> has symbol "program_invocation_short_name" : YES 
Has header "xlocale.h" : NO 
Checking if "locale.h" links: YES 
Header <sys/ptrace.h> has symbol "PTRACE_ATTACH" : YES 
Found pkg-config: /openwrt/staging_dir/host/bin/pkg-config (1.7.3)
Run-time dependency libudev found: YES 243
Run-time dependency mtdev found: YES 1.1.6
Found CMake: NO
Run-time dependency libevdev found: NO (tried pkgconfig)

../../../../build_dir/target-aarch64_cortex-a72_musl/libinput-1.17.1/meson.build:144:0: ERROR: Dependency "libevdev" not found, tried pkgconfig

A full log can be found at /openwrt/build_dir/target-aarch64_cortex-a72_musl/libinput-1.17.1/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:73: /openwrt/build_dir/target-aarch64_cortex-a72_musl/libinput-1.17.1/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
