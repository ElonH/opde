---
title: "compile.42"
date: 2021-06-29 09:40:48.064785
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
make package/feeds/packages/gst1-plugins-base/compile -j$(nproc) || make package/feeds/packages/gst1-plugins-base/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-distutils.patch using plaintext: 
patching file meson.build
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/gst-plugins-base-1.18.4
Build dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/gst-plugins-base-1.18.4/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: gst-plugins-base
Project version: 1.18.4
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
WARNING: Project targeting '>= 0.48' but tried to use feature introduced in '0.54.0': native arg in add_languages.
C++ compiler for the host machine: ccache_cxx (gcc 8.4.0 "aarch64-openwrt-linux-musl-g++ (OpenWrt GCC 8.4.0 r0-af265d3) 8.4.0")
C++ linker for the host machine: ccache_cxx ld.bfd 2.34
Compiler for C supports link arguments -Wl,-Bsymbolic-functions: YES 
Compiler for C supports arguments -fvisibility=hidden: YES 
Compiler for C supports arguments -fno-strict-aliasing: YES 
Message: Disabling GLib cast checks
Message: Disabling GLib asserts
Message: Disabling GLib checks
Has header "dlfcn.h" : YES 
Has header "emmintrin.h" : NO 
Has header "inttypes.h" : YES 
Has header "memory.h" : YES 
Has header "netinet/in.h" : YES 
Has header "netinet/tcp.h" : YES 
Has header "process.h" : NO 
Has header "smmintrin.h" : NO 
Has header "stdint.h" : YES 
Has header "strings.h" : YES 
Has header "string.h" : YES 
Has header "sys/socket.h" : YES 
Has header "sys/stat.h" : YES 
Has header "sys/types.h" : YES 
Has header "sys/wait.h" : YES 
Has header "unistd.h" : YES 
Has header "winsock2.h" : NO 
Has header "xmmintrin.h" : NO 
Has header "linux/dma-buf.h" : YES 
Library m found: YES
Checking for function "dcgettext" with dependency -lm: YES 
Checking for function "gmtime_r" with dependency -lm: YES 
Checking for function "localtime_r" with dependency -lm: YES 
Checking for function "lrintf" with dependency -lm: YES 
Checking for function "mmap" with dependency -lm: YES 
Checking for function "log2" with dependency -lm: YES 
Checking for size of "char" : 1
Checking for size of "int" : 4
Checking for size of "long" : 8
Checking for size of "short" : 2
Checking for size of "void*" : 8
Compiler for C++ supports arguments -Waggregate-return: YES 
Compiler for C supports arguments -Wmissing-declarations: YES 
Compiler for C++ supports arguments -Wmissing-declarations: YES 
Compiler for C supports arguments -Wredundant-decls: YES 
Compiler for C++ supports arguments -Wredundant-decls: YES 
Compiler for C supports arguments -Wundef: YES 
Compiler for C++ supports arguments -Wundef: YES 
Compiler for C supports arguments -Wwrite-strings: YES 
Compiler for C++ supports arguments -Wwrite-strings: YES 
Compiler for C supports arguments -Wformat: YES 
Compiler for C++ supports arguments -Wformat: YES 
Compiler for C supports arguments -Wformat-nonliteral: YES 
Compiler for C++ supports arguments -Wformat-nonliteral: YES 
Compiler for C supports arguments -Wformat-security: YES 
Compiler for C++ supports arguments -Wformat-security: YES 
Compiler for C supports arguments -Winit-self: YES 
Compiler for C++ supports arguments -Winit-self: YES 
Compiler for C supports arguments -Wmissing-include-dirs: YES 
Compiler for C++ supports arguments -Wmissing-include-dirs: YES 
Compiler for C supports arguments -Waddress: YES 
Compiler for C++ supports arguments -Waddress: YES 
Compiler for C supports arguments -Wno-multichar: YES 
Compiler for C++ supports arguments -Wno-multichar: YES 
Compiler for C supports arguments -Wvla: YES 
Compiler for C++ supports arguments -Wvla: YES 
Compiler for C supports arguments -Wpointer-arith: YES 
Compiler for C++ supports arguments -Wpointer-arith: YES 
Compiler for C supports arguments -Wmissing-prototypes: YES 
Compiler for C supports arguments -Wdeclaration-after-statement: YES 
Dependency x11 skipped: feature x11 disabled
Found pkg-config: /openwrt/staging_dir/host/bin/pkg-config (1.7.3)
Found CMake: NO
Run-time dependency glib-2.0 found: NO (tried pkgconfig and cmake)
Looking for a fallback subproject for the dependency glib-2.0

../../../../build_dir/target-aarch64_cortex-a72_musl/gst-plugins-base-1.18.4/meson.build:285:0: ERROR: Neither a subproject directory nor a glib.wrap file was found.

A full log can be found at /openwrt/build_dir/target-aarch64_cortex-a72_musl/gst-plugins-base-1.18.4/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:249: /openwrt/build_dir/target-aarch64_cortex-a72_musl/gst-plugins-base-1.18.4/.configured_819da7b9d1a602c2976d7611e77112f3] Error 1
```
