---
title: "compile.42"
date: 2021-06-29 09:38:24.625415
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
make package/feeds/packages/fastd/compile -j$(nproc) || make package/feeds/packages/fastd/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/0001-config-allow-disabling-L2TP-offload-when-fastd-doesn.patch using plaintext: 
patching file src/config.y
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/fastd-22
Build dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/fastd-22/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: fastd
Project version: v22
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
Compiler for C supports arguments -Wno-format-truncation: YES 
Compiler for C supports arguments -Wno-stringop-truncation: YES 
Program bison found: YES (/openwrt/staging_dir/host/bin/bison)
Configuring ciphers.c using configuration
Configuring macs.c using configuration
Configuring methods.c using configuration
Run-time dependency threads found: YES
Found pkg-config: /openwrt/staging_dir/host/bin/pkg-config (1.7.3)
Run-time dependency libuecc found: YES 7
Run-time dependency json-c found: YES 0.15
Library nacl found: YES
Header <netdb.h> has symbol "AI_ADDRCONFIG" : YES 
Checking for function "get_current_dir_name" : YES 
Has header "endian.h" : YES 
Header <endian.h> has symbol "be32toh" : YES 
Checking for function "setresuid" : YES 
Checking for function "setresgid" : YES 
Configuring build.h using configuration
Program clang-format found: NO
Build targets in project: 5


ERROR: Could not detect Ninja v1.8.2 or newer

A full log can be found at /openwrt/build_dir/target-aarch64_cortex-a72_musl/fastd-22/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:123: /openwrt/build_dir/target-aarch64_cortex-a72_musl/fastd-22/.configured_eb0eb41d4299986e1b4b59bbcfda8f52] Error 1
```
