---
title: "compile.42"
date: 2021-06-29 09:40:48.072131
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
make package/feeds/packages/zstd/compile -j$(nproc) || make package/feeds/packages/zstd/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-fix-meson.patch using plaintext: 
patching file build/meson/lib/meson.build
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/zstd-1.4.9/build/meson
Build dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/zstd-1.4.9/build/meson/openwrt-build
Build type: cross build
WARNING: Unknown options: "bin_control, build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: zstd
Project version: DUMMY
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
Program GetZstdLibraryVersion.py found: YES (/openwrt/staging_dir/host/bin/python /openwrt/build_dir/target-aarch64_cortex-a72_musl/zstd-1.4.9/build/meson/GetZstdLibraryVersion.py)
Message: Project version is now: 1.4.9
Library m found: YES
Run-time dependency threads found: YES
Dependency zlib skipped: feature zlib disabled
Dependency liblzma skipped: feature lzma disabled
Dependency liblz4 skipped: feature lz4 disabled
Compiler for C supports arguments -Wextra: YES 
Compiler for C supports arguments -Wundef: YES 
Compiler for C supports arguments -Wshadow: YES 
Compiler for C supports arguments -Wcast-align: YES 
Compiler for C supports arguments -Wcast-qual: YES 
Compiler for C supports arguments -Wstrict-prototypes: YES 
Compiler for C++ supports arguments -Wextra: YES 
Compiler for C++ supports arguments -Wundef: YES 
Compiler for C++ supports arguments -Wshadow: YES 
Compiler for C++ supports arguments -Wcast-align: YES 
Compiler for C++ supports arguments -Wcast-qual: YES 
../../../../build_dir/target-aarch64_cortex-a72_musl/zstd-1.4.9/build/meson/meson.build:117: WARNING: Consider using the built-in warning_level option instead of using "-Wextra".
../../../../build_dir/target-aarch64_cortex-a72_musl/zstd-1.4.9/build/meson/meson.build:118: WARNING: Consider using the built-in warning_level option instead of using "-Wextra".
Message: Enable legacy support back to version 0.1
Message: Enable multi-threading support
Program ../InstallSymlink.py found: YES (/openwrt/staging_dir/host/bin/python /openwrt/build_dir/target-aarch64_cortex-a72_musl/zstd-1.4.9/build/meson/programs/../InstallSymlink.py)
Build targets in project: 3

Option buildtype is: plain [default: release]

ERROR: Could not detect Ninja v1.8.2 or newer

A full log can be found at /openwrt/build_dir/target-aarch64_cortex-a72_musl/zstd-1.4.9/build/meson/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:107: /openwrt/build_dir/target-aarch64_cortex-a72_musl/zstd-1.4.9/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
