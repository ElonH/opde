---
title: "compile.42"
date: 2021-06-29 09:32:34.522095
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
make package/feeds/packages/libpsl/compile -j$(nproc) || make package/feeds/packages/libpsl/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-python.patch using plaintext: 
patching file meson.build
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/libpsl-0.21.1
Build dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/libpsl-0.21.1/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: libpsl
Project version: 0.21.1
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
Found pkg-config: /openwrt/staging_dir/host/bin/pkg-config (1.7.3)
Run-time dependency libidn2 found: YES 2.3.0
Library unistring found: YES
Check usable header "unistd.h" : YES 
Check usable header "stdint.h" : YES 
Check usable header "alloca.h" : YES 
Check usable header "dirent.h" : YES 
Checking for function "alloca" : YES 
Checking for function "strndup" : YES 
Checking for function "clock_gettime" : YES 
Checking for function "fmemopen" : YES 
Checking for function "nl_langinfo" : YES 
Configuring config.h using configuration
Configuring libpsl.h using configuration
Build targets in project: 13


ERROR: Could not detect Ninja v1.8.2 or newer

A full log can be found at /openwrt/build_dir/target-aarch64_cortex-a72_musl/libpsl-0.21.1/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:64: /openwrt/build_dir/target-aarch64_cortex-a72_musl/libpsl-0.21.1/.configured_a17fb5ef857664f03cd0ce37cc5ea591] Error 1
```
