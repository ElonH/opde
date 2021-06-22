---
title: "compile.40"
date: 2021-06-22 10:50:06.151093
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
make package/feeds/packages/jose/compile -j$(nproc) || make package/feeds/packages/jose/compile V=s
```

#### Compile.txt

``` bash
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-mips_24kc_musl/jose-11
Build dir: /openwrt/build_dir/target-mips_24kc_musl/jose-11/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: jose
Project version: 11
C compiler for the host machine: ccache_cc (gcc 8.4.0 "mips-openwrt-linux-musl-gcc (OpenWrt GCC 8.4.0 r0-d97b735) 8.4.0")
C linker for the host machine: ccache_cc ld.bfd 2.34
C compiler for the build machine: ccache gcc (gcc 9.3.0 "gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0")
C linker for the build machine: gcc ld.bfd 2.34
Build machine cpu family: x86_64
Build machine cpu: x86_64
Host machine cpu family: mips
Host machine cpu: generic
Target machine cpu family: mips
Target machine cpu: generic
Found pkg-config: /openwrt/staging_dir/host/bin/pkg-config (1.7.3)
Run-time dependency zlib found: YES 1.2.11
Run-time dependency threads found: YES
Run-time dependency jansson found: YES 2.13.1
Found CMake: NO
Run-time dependency libcrypto found: NO (tried pkgconfig)

../../../../build_dir/target-mips_24kc_musl/jose-11/meson.build:41:0: ERROR: Dependency "libcrypto" not found, tried pkgconfig

A full log can be found at /openwrt/build_dir/target-mips_24kc_musl/jose-11/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:79: /openwrt/build_dir/target-mips_24kc_musl/jose-11/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
