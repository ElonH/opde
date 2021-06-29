---
title: "compile.42"
date: 2021-06-29 09:26:41.855211
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
make package/feeds/packages/liblz4/compile -j$(nproc) || make package/feeds/packages/liblz4/compile V=s
```

#### Compile.txt

``` bash
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/lz4-1.9.3/contrib/meson
Build dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/lz4-1.9.3/contrib/meson/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: lz4
Project version: DUMMY
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
Program GetLz4LibraryVersion.py found: YES (/openwrt/staging_dir/host/bin/python /openwrt/build_dir/target-aarch64_cortex-a72_musl/lz4-1.9.3/contrib/meson/meson/GetLz4LibraryVersion.py)
Message: Project version is now: 1.9.3
Compiler for C supports arguments -pedantic: YES 
Program ../InstallSymlink.py found: YES (/openwrt/staging_dir/host/bin/python /openwrt/build_dir/target-aarch64_cortex-a72_musl/lz4-1.9.3/contrib/meson/meson/programs/../InstallSymlink.py)
Build targets in project: 2

Option buildtype is: plain [default: release]

ERROR: Could not detect Ninja v1.8.2 or newer

A full log can be found at /openwrt/build_dir/target-aarch64_cortex-a72_musl/lz4-1.9.3/contrib/meson/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:108: /openwrt/build_dir/target-aarch64_cortex-a72_musl/lz4-1.9.3/.configured_004b14e07ed5c6c456c4c20c75520ea4] Error 1
```
