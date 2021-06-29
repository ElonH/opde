---
title: "compile.42"
date: 2021-06-29 09:32:34.515822
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
make package/feeds/packages/conmon/compile -j$(nproc) || make package/feeds/packages/conmon/compile V=s
```

#### Compile.txt

``` bash
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/conmon-2.0.29
Build dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/conmon-2.0.29/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: conmon
Project version: 2.0.29
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
Program git found: YES (/openwrt/staging_dir/host/bin/git)
../../../../build_dir/target-aarch64_cortex-a72_musl/conmon-2.0.29/meson.build:34: WARNING: Consider using the built-in optimization level instead of using "-Os".
../../../../build_dir/target-aarch64_cortex-a72_musl/conmon-2.0.29/meson.build:34: WARNING: Consider using the built-in warning_level option instead of using "-Wall".
../../../../build_dir/target-aarch64_cortex-a72_musl/conmon-2.0.29/meson.build:34: WARNING: Consider using the built-in werror option instead of using "-Werror".
Found pkg-config: /openwrt/staging_dir/host/bin/pkg-config (1.7.3)
Found CMake: NO
Run-time dependency glib-2.0 found: NO (tried pkgconfig)

../../../../build_dir/target-aarch64_cortex-a72_musl/conmon-2.0.29/meson.build:36:0: ERROR: Dependency "glib-2.0" not found, tried pkgconfig

A full log can be found at /openwrt/build_dir/target-aarch64_cortex-a72_musl/conmon-2.0.29/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:48: /openwrt/build_dir/target-aarch64_cortex-a72_musl/conmon-2.0.29/.configured_a17fb5ef857664f03cd0ce37cc5ea591] Error 1
```
