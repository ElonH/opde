---
title: "compile.42"
date: 2021-06-29 09:35:34.996245
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
make package/feeds/packages/spice/compile -j$(nproc) || make package/feeds/packages/spice/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-doxy.patch using plaintext: 
patching file meson.build

Applying ./patches/030-include-generated-code.patch using plaintext: 
patching file subprojects/spice-common/common/meson.build

Applying ./patches/040-only-server.patch using plaintext: 
patching file meson.build

Applying ./patches/050-no-mkenums.patch using plaintext: 
patching file server/meson.build
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/spice-0.15.0
Build dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/spice-0.15.0/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: spice
Project version: 0.15.0
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
Message: Updating submodules
Message: libspice.so version: 1.14.1
Run-time dependency threads found: YES

|Executing subproject spice-common method meson 
|
|Project name: spice-common
|Project version: undefined
|C compiler for the host machine: ccache_cc (gcc 8.4.0 "aarch64-openwrt-linux-musl-gcc (OpenWrt GCC 8.4.0 r0-af265d3) 8.4.0")
|C linker for the host machine: ccache_cc ld.bfd 2.34
|C compiler for the build machine: ccache gcc (gcc 9.3.0 "gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0")
|C linker for the build machine: gcc ld.bfd 2.34
|Has header "alloca.h" : YES 
|Has header "arpa/inet.h" : YES 
|Has header "dlfcn.h" : YES 
|Has header "inttypes.h" : YES 
|Has header "netinet/in.h" : YES 
|Has header "stdlib.h" : YES 
|Has header "sys/socket.h" : YES 
|Has header "sys/stat.h" : YES 
|Has header "sys/types.h" : YES 
|Has header "unistd.h" : YES 
|Has header "regex.h" : YES 
|Has header "sys/mman.h" : YES 
|Checking for function "alloca" : YES 
|Checking for function "sigaction" : YES 
|Checking for function "drand48" : YES 
|Checking for function "setlinebuf" : YES 
|Library m found: YES
|Found pkg-config: /openwrt/staging_dir/host/bin/pkg-config (1.7.3)
|Found CMake: NO
|Run-time dependency glib-2.0 found: NO (tried pkgconfig)

../../../../build_dir/target-aarch64_cortex-a72_musl/spice-0.15.0/subprojects/spice-common/meson.build:110:2: ERROR: Dependency "glib-2.0" not found, tried pkgconfig

A full log can be found at /openwrt/build_dir/target-aarch64_cortex-a72_musl/spice-0.15.0/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:84: /openwrt/build_dir/target-aarch64_cortex-a72_musl/spice-0.15.0/.configured_a17fb5ef857664f03cd0ce37cc5ea591] Error 1
```
