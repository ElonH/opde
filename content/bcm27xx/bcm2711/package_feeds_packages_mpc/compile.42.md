---
title: "compile.42"
date: 2021-06-29 09:38:24.627535
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
make package/feeds/packages/mpc/compile -j$(nproc) || make package/feeds/packages/mpc/compile V=s
```

#### Compile.txt

``` bash
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/mpc-0.33
Build dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/mpc-0.33/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: mpc
Project version: 0.33
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
Configuring config.h using configuration
Compiler for C supports link arguments -Wl,--gc-sections: YES 
Compiler for C supports link arguments -Wl,--icf=all: NO 
Compiler for C supports arguments -Wall: YES 
Compiler for C supports arguments -Wextra: YES 
Compiler for C supports arguments -Wno-deprecated-declarations: YES 
Compiler for C supports arguments -Wmissing-prototypes: YES 
Compiler for C supports arguments -Wshadow: YES 
Compiler for C supports arguments -Wpointer-arith: YES 
Compiler for C supports arguments -Wstrict-prototypes: YES 
Compiler for C supports arguments -Wcast-qual: YES 
Compiler for C supports arguments -Wwrite-strings: YES 
Compiler for C supports arguments -fvisibility=hidden: YES 
Compiler for C supports arguments -ffunction-sections: YES 
Compiler for C supports arguments -fdata-sections: YES 
../../../../build_dir/target-aarch64_cortex-a72_musl/mpc-0.33/meson.build:67: WARNING: Consider using the built-in warning_level option instead of using "-Wall".
../../../../build_dir/target-aarch64_cortex-a72_musl/mpc-0.33/meson.build:67: WARNING: Consider using the built-in warning_level option instead of using "-Wextra".
Found pkg-config: /openwrt/staging_dir/host/bin/pkg-config (1.7.3)
Found CMake: NO
Run-time dependency libmpdclient found: NO (tried pkgconfig)

../../../../build_dir/target-aarch64_cortex-a72_musl/mpc-0.33/meson.build:69:0: ERROR: Dependency "libmpdclient" not found, tried pkgconfig

A full log can be found at /openwrt/build_dir/target-aarch64_cortex-a72_musl/mpc-0.33/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:55: /openwrt/build_dir/target-aarch64_cortex-a72_musl/mpc-0.33/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
