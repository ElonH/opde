---
title: "compile.42"
date: 2021-06-29 09:40:48.062200
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
make package/feeds/packages/freetype/compile -j$(nproc) || make package/feeds/packages/freetype/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-meson.patch using plaintext: 
patching file meson.build

Applying ./patches/020-distutils.patch using plaintext: 
patching file meson.build

Applying ./patches/030-meson-pkgconfig.patch using plaintext: 
patching file meson.build
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/freetype-2.10.4
Build dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/freetype-2.10.4/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: freetype2
Project version: undefined
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
Has header "unistd.h" : YES 
Has header "fcntl.h" : YES 
Has header "sys/mman.h" : YES 
Found pkg-config: /openwrt/staging_dir/host/bin/pkg-config (1.7.3)
Run-time dependency zlib found: YES 1.2.11
Library bz2 skipped: feature bzip2 disabled
Run-time dependency libpng found: YES 1.6.37
Dependency harfbuzz skipped: feature harfbuzz disabled
Dependency libbrotlidec skipped: feature brotli disabled
Compiler for C supports function attribute visibility:hidden: YES 
Build targets in project: 5


ERROR: Could not detect Ninja v1.8.2 or newer

A full log can be found at /openwrt/build_dir/target-aarch64_cortex-a72_musl/freetype-2.10.4/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:71: /openwrt/build_dir/target-aarch64_cortex-a72_musl/freetype-2.10.4/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
