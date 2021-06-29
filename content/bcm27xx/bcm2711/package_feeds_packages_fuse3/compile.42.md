---
title: "compile.42"
date: 2021-06-29 09:38:24.594026
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
make package/feeds/packages/fuse3/compile -j$(nproc) || make package/feeds/packages/fuse3/compile V=s
```

#### Compile.txt

``` bash
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/fuse-3.10.1
Build dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/fuse-3.10.1/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: libfuse3
Project version: 3.10.1
C compiler for the host machine: ccache_cc (gcc 8.4.0 "aarch64-openwrt-linux-musl-gcc (OpenWrt GCC 8.4.0 r0-af265d3) 8.4.0")
C linker for the host machine: ccache_cc ld.bfd 2.34
C compiler for the build machine: ccache gcc (gcc 9.3.0 "gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0")
C linker for the build machine: gcc ld.bfd 2.34
Build machine cpu family: x86_64
Build machine cpu: x86_64
Host machine cpu family: aarch64
Host machine cpu: cortex-a72
Target machine cpu family: aarch64
Target machine cpu: cortex-a72
Checking for function "fork" : YES 
Checking for function "fstatat" : YES 
Checking for function "openat" : YES 
Checking for function "readlinkat" : YES 
Checking for function "pipe2" : YES 
Checking for function "splice" : YES 
Checking for function "vmsplice" : YES 
Checking for function "posix_fallocate" : YES 
Checking for function "fdatasync" : YES 
Checking for function "utimensat" : YES 
Checking for function "copy_file_range" : YES 
Checking for function "fallocate" : YES 
Checking for function "setxattr" : YES 
Checking for function "iconv" : YES 
Checking whether type "struct stat" has member "st_atim" : YES 
Checking whether type "struct stat" has member "st_atimespec" : NO 
Configuring config.h using configuration
../../../../build_dir/target-aarch64_cortex-a72_musl/fuse-3.10.1/meson.build:68: WARNING: Consider using the built-in warning_level option instead of using "-Wall".
../../../../build_dir/target-aarch64_cortex-a72_musl/fuse-3.10.1/meson.build:68: WARNING: Consider using the built-in warning_level option instead of using "-Wextra".
../../../../build_dir/target-aarch64_cortex-a72_musl/fuse-3.10.1/meson.build:72: WARNING: Consider using the built-in warning_level option instead of using "-Wall".
../../../../build_dir/target-aarch64_cortex-a72_musl/fuse-3.10.1/meson.build:72: WARNING: Consider using the built-in warning_level option instead of using "-Wextra".
../../../../build_dir/target-aarch64_cortex-a72_musl/fuse-3.10.1/meson.build:72: WARNING: Consider using the built-in option for language standard version instead of using "-std=c++11".
Message: Compiler warns about unused result even when casting to void
Message: Compiler does not support symver attribute
Run-time dependency threads found: YES
Library iconv found: NO
Library dl found: YES
Library rt found: YES
Program install_helper.sh found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/fuse-3.10.1/util/install_helper.sh)
Build targets in project: 8

Option buildtype is: plain [default: debugoptimized]

ERROR: Could not detect Ninja v1.8.2 or newer

A full log can be found at /openwrt/build_dir/target-aarch64_cortex-a72_musl/fuse-3.10.1/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:109: /openwrt/build_dir/target-aarch64_cortex-a72_musl/fuse-3.10.1/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
