---
title: "compile.42"
date: 2021-06-29 09:38:24.610819
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
make package/feeds/packages/libdrm/compile -j$(nproc) || make package/feeds/packages/libdrm/compile V=s
```

#### Compile.txt

``` bash
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/libdrm-2.4.104
Build dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/libdrm-2.4.104/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: libdrm
Project version: 2.4.104
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
Run-time dependency threads found: YES
Program symbols-check.py found: YES (/openwrt/staging_dir/host/bin/python /openwrt/build_dir/target-aarch64_cortex-a72_musl/libdrm-2.4.104/symbols-check.py)
Program aarch64-openwrt-linux-musl-gcc-nm found: YES
Found pkg-config: /openwrt/staging_dir/host/bin/pkg-config (1.7.3)
Found CMake: NO
Run-time dependency atomic_ops found: NO (tried pkgconfig and cmake)
Checking if "Intel Atomics" links: YES 
Checking for function "dlsym" : YES 
Checking for function "clock_gettime" : YES 
Library m found: YES
Checking if "sys/select.h works" compiles: YES 
Checking if "alloca.h works" compiles: YES 
Header <sys/sysmacros.h> has symbol "major" : YES 
Header <sys/sysmacros.h> has symbol "minor" : YES 
Header <sys/sysmacros.h> has symbol "makedev" : YES 
Header <sys/mkdev.h> has symbol "major" : NO 
Checking for function "open_memstream" : YES 
Compiler for C supports arguments -Wall: YES 
Compiler for C supports arguments -Wextra: YES 
Compiler for C supports arguments -Wsign-compare: YES 
Compiler for C supports arguments -Werror=undef: YES 
Compiler for C supports arguments -Werror=implicit-function-declaration: YES 
Compiler for C supports arguments -Wpointer-arith: YES 
Compiler for C supports arguments -Wwrite-strings: YES 
Compiler for C supports arguments -Wstrict-prototypes: YES 
Compiler for C supports arguments -Wmissing-prototypes: YES 
Compiler for C supports arguments -Wmissing-declarations: YES 
Compiler for C supports arguments -Wnested-externs: YES 
Compiler for C supports arguments -Wpacked: YES 
Compiler for C supports arguments -Wswitch-enum: YES 
Compiler for C supports arguments -Wmissing-format-attribute: YES 
Compiler for C supports arguments -Wstrict-aliasing=2: YES 
Compiler for C supports arguments -Winit-self: YES 
Compiler for C supports arguments -Winline: YES 
Compiler for C supports arguments -Wshadow: YES 
Compiler for C supports arguments -Wdeclaration-after-statement: YES 
Compiler for C supports arguments -Wold-style-definition: YES 
Compiler for C supports arguments -Wunused-parameter: YES 
Compiler for C supports arguments -Wattributes: YES 
Compiler for C supports arguments -Wlong-long: YES 
Compiler for C supports arguments -Wmissing-field-initializers: YES 
Run-time dependency pciaccess found: YES 0.16
Run-time dependency cunit found: NO (tried pkgconfig and cmake)
Program rst2man found: NO
Checking if "compiler supports __attribute__(("hidden"))" compiles: YES 
Configuring config.h using configuration
Message: 
Message: libdrm will be compiled with:
Message: 
Message:   libkms         false
Message:   Intel API      false
Message:   vmwgfx API     false
Message:   Radeon API     false
Message:   AMDGPU API     false
Message:   Nouveau API    false
Message:   OMAP API       false
Message:   EXYNOS API     false
Message:   Freedreno API  false (kgsl: false)
Message:   Tegra API      false
Message:   VC4 API        false
Message:   Etnaviv API    false
Message: 
Build targets in project: 12

Option buildtype is: plain [default: debugoptimized]

ERROR: Could not detect Ninja v1.8.2 or newer

A full log can be found at /openwrt/build_dir/target-aarch64_cortex-a72_musl/libdrm-2.4.104/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:87: /openwrt/build_dir/target-aarch64_cortex-a72_musl/libdrm-2.4.104/.configured_cfedc8c97075577afea43599fe9a5c87] Error 1
```
