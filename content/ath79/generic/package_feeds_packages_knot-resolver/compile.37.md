---
title: "compile.37"
date: 2021-06-20 22:32:33.831272
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
make package/feeds/packages/knot-resolver/compile -j$(nproc) || make package/feeds/packages/knot-resolver/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-fix-lmdb.patch using plaintext: 
patching file meson.build

Applying ./patches/030-fix-policy-hack.patch using plaintext: 
patching file modules/policy/policy.lua
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-mips_24kc_musl/knot-resolver-5.3.2
Build dir: /openwrt/build_dir/target-mips_24kc_musl/knot-resolver-5.3.2/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: knot-resolver
Project version: 5.3.2
C compiler for the host machine: ccache_cc (gcc 8.4.0 "mips-openwrt-linux-musl-gcc (OpenWrt GCC 8.4.0 r0-91deb05) 8.4.0")
C linker for the host machine: ccache_cc ld.bfd 2.34
C++ compiler for the host machine: ccache_cxx (gcc 8.4.0 "mips-openwrt-linux-musl-g++ (OpenWrt GCC 8.4.0 r0-91deb05) 8.4.0")
C++ linker for the host machine: ccache_cxx ld.bfd 2.34
C compiler for the build machine: ccache gcc (gcc 9.3.0 "gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0")
C linker for the build machine: gcc ld.bfd 2.34
C++ compiler for the build machine: ccache g++ (gcc 9.3.0 "g++ (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0")
C++ linker for the build machine: g++ ld.bfd 2.34
Build machine cpu family: x86_64
Build machine cpu: x86_64
Host machine cpu family: mips
Host machine cpu: generic
Target machine cpu family: mips
Target machine cpu: generic
Message: --- required dependencies ---
Found pkg-config: /openwrt/staging_dir/host/bin/pkg-config (1.7.3)
Found CMake: NO
Run-time dependency libknot found: NO (tried pkgconfig)

../../../../build_dir/target-mips_24kc_musl/knot-resolver-5.3.2/meson.build:22:0: ERROR: Dependency "libknot" not found, tried pkgconfig

A full log can be found at /openwrt/build_dir/target-mips_24kc_musl/knot-resolver-5.3.2/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:97: /openwrt/build_dir/target-mips_24kc_musl/knot-resolver-5.3.2/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
