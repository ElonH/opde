---
title: "compile.42"
date: 2021-06-29 09:35:35.009825
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
make package/feeds/packages/libesmtp/compile -j$(nproc) || make package/feeds/packages/libesmtp/compile V=s
```

#### Compile.txt

``` bash
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/libESMTP-1.1.0
Build dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/libESMTP-1.1.0/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: libESMTP
Project version: 1.1.0
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
Compiler for C supports arguments -D_POSIX_C_SOURCE=200809L: YES 
Library dl found: YES
Found pkg-config: /openwrt/staging_dir/host/bin/pkg-config (1.7.3)
Run-time dependency openssl found: YES 1.1.1k
Run-time dependency threads found: YES
Library lwres skipped: feature lwres disabled
Checking for function "strlcpy" : YES 
Checking for function "strdup" : YES 
Checking for function "strncasecmp" : YES 
Checking for function "strcasecmp" : YES 
Header <string.h> has symbol "memrchr" : NO 
Checking for size of "unsigned int" : 4
Checking for size of "unsigned long" : 8
Checking for size of "unsigned short" : 2
Configuring config.h using configuration
Configuring libesmtp.spec using configuration
Build targets in project: 6

libESMTP 1.1.0

    current:revision:age: 8:0:2
    so version          : 6.2.0
    prefix              : /usr
    libdir              : lib
    threads             : True
    lwres               : False
    AUTH modules        : /usr/lib/esmtp-plugins-6.2.0
    Legacy file layout  : False
    STARTTLS            : True
    CHUNKING            : True
    ETRN                : True
    XUSR                : True


ERROR: Could not detect Ninja v1.8.2 or newer

A full log can be found at /openwrt/build_dir/target-aarch64_cortex-a72_musl/libESMTP-1.1.0/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:66: /openwrt/build_dir/target-aarch64_cortex-a72_musl/libESMTP-1.1.0/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
