---
title: "compile.37"
date: 2021-06-20 22:26:36.886968
hidden: false
draft: false
weight: -37
---

build number: `37`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/tang/compile -j$(nproc) || make package/feeds/packages/tang/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-http.patch using plaintext: 
patching file meson.build
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-mips_24kc_musl/tang-10
Build dir: /openwrt/build_dir/target-mips_24kc_musl/tang-10/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: tang
Project version: 10
C compiler for the host machine: ccache_cc (gcc 8.4.0 "mips-openwrt-linux-musl-gcc (OpenWrt GCC 8.4.0 r0-91deb05) 8.4.0")
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
Found CMake: NO
Run-time dependency jose found: NO (tried pkgconfig)

../../../../build_dir/target-mips_24kc_musl/tang-10/meson.build:51:0: ERROR: Dependency "jose" not found, tried pkgconfig

A full log can be found at /openwrt/build_dir/target-mips_24kc_musl/tang-10/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:70: /openwrt/build_dir/target-mips_24kc_musl/tang-10/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
