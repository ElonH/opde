---
title: "compile.42"
date: 2021-06-29 09:34:13.666804
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
make package/feeds/packages/gst1-libav/compile -j$(nproc) || make package/feeds/packages/gst1-libav/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-distutils.patch using plaintext: 
patching file meson.build
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/gst-libav-1.18.4
Build dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/gst-libav-1.18.4/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: gst-libav
Project version: 1.18.4
C compiler for the host machine: ccache_cc (gcc 8.4.0 "aarch64-openwrt-linux-musl-gcc (OpenWrt GCC 8.4.0 r0-af265d3) 8.4.0")
C linker for the host machine: ccache_cc ld.bfd 2.34
C++ compiler for the host machine: ccache_cxx (gcc 8.4.0 "aarch64-openwrt-linux-musl-g++ (OpenWrt GCC 8.4.0 r0-af265d3) 8.4.0")
C++ linker for the host machine: ccache_cxx ld.bfd 2.34
C compiler for the build machine: ccache gcc (gcc 9.3.0 "gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0")
C linker for the build machine: gcc ld.bfd 2.34
C++ compiler for the build machine: ccache g++ (gcc 9.3.0 "g++ (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0")
C++ linker for the build machine: g++ ld.bfd 2.34
Build machine cpu family: x86_64
Build machine cpu: x86_64
Host machine cpu family: aarch64
Host machine cpu: generic
Target machine cpu family: aarch64
Target machine cpu: generic
Found pkg-config: /openwrt/staging_dir/host/bin/pkg-config (1.7.3)
Run-time dependency libavfilter found: YES 7.85.100
Run-time dependency libavformat found: YES 58.45.100
Run-time dependency libavcodec found: YES 58.91.100
Run-time dependency libavutil found: YES 56.51.100
Checking if "libav is provided by FFmpeg" with dependencies libavfilter, libavformat, libavcodec, libavutil compiles: YES 
Has header "unistd.h" : YES 
Found CMake: NO
Run-time dependency gstreamer-1.0 found: NO (tried pkgconfig and cmake)
Looking for a fallback subproject for the dependency gstreamer-1.0

../../../../build_dir/target-aarch64_cortex-a72_musl/gst-libav-1.18.4/meson.build:83:0: ERROR: Neither a subproject directory nor a gstreamer.wrap file was found.

A full log can be found at /openwrt/build_dir/target-aarch64_cortex-a72_musl/gst-libav-1.18.4/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:219: /openwrt/build_dir/target-aarch64_cortex-a72_musl/gst-libav-1.18.4/.configured_c3004cb90b7a2c340455637c286fadbf] Error 1
```
