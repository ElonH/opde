---
title: "compile.42"
date: 2021-06-29 09:33:27.248598
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
make package/feeds/packages/bonnie++/compile -j$(nproc) || make package/feeds/packages/bonnie++/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/002-add-verbose-error-messages.patch using plaintext: 
patching file bon_file.cpp

Applying ./patches/010-meson.patch using plaintext: 
patching file conf.h.meson
patching file meson.build

Applying ./patches/100-remove-using-namespace-std.patch using plaintext: 
patching file bon_time.cpp
patching file bonnie++.cpp
patching file bonnie.h
patching file duration.cpp
patching file getc_putc.cpp
patching file rand.cpp
patching file rand.h

Applying ./patches/101-fix-wrong-printf-off_t-format.patch using plaintext: 
patching file port.h

Applying ./patches/102-add-missing-cast.patch using plaintext: 
patching file bon_time.cpp
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/bonnie++-2.00a
Build dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/bonnie++-2.00a/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: bonnie++
Project version: 2.00a
C++ compiler for the host machine: ccache_cxx (gcc 8.4.0 "aarch64-openwrt-linux-musl-g++ (OpenWrt GCC 8.4.0 r0-af265d3) 8.4.0")
C++ linker for the host machine: ccache_cxx ld.bfd 2.34
C++ compiler for the build machine: ccache g++ (gcc 9.3.0 "g++ (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0")
C++ linker for the build machine: g++ ld.bfd 2.34
Build machine cpu family: x86_64
Build machine cpu: x86_64
Host machine cpu family: aarch64
Host machine cpu: generic
Target machine cpu family: aarch64
Target machine cpu: generic
Has header "algorithm" : YES 
Configuring conf.h using configuration
Run-time dependency threads found: YES
Build targets in project: 6


ERROR: Could not detect Ninja v1.8.2 or newer

A full log can be found at /openwrt/build_dir/target-aarch64_cortex-a72_musl/bonnie++-2.00a/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:60: /openwrt/build_dir/target-aarch64_cortex-a72_musl/bonnie++-2.00a/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
