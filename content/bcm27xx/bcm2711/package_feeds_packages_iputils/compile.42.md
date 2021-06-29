---
title: "compile.42"
date: 2021-06-29 09:38:24.615123
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
make package/feeds/packages/iputils/compile -j$(nproc) || make package/feeds/packages/iputils/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001_version_fix.patch using plaintext: 
patching file meson.build
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/iputils-20210202
Build dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/iputils-20210202/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: iputils
Project version: 20210202
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
Found pkg-config: /openwrt/staging_dir/host/bin/pkg-config (1.7.3)
Found CMake: NO
Run-time dependency systemd found: NO (tried pkgconfig and cmake)
Checking for function "__fpending" : YES 
Checking for function "getrandom" : YES 
Checking for function "nanosleep" : YES 
Checking if "struct icmp6_nodeinfo" compiles: NO 
Checking if "struct tm time;" compiles: YES 
Library m found: YES
Library resolv found: YES
Checking for function "clock_gettime" : YES 
Library disabler-appears-to-disable-executable-build found: NO
Run-time dependency disabler-appears-to-disable-executable-build found: NO (tried pkgconfig and cmake)
Run-time dependency disabler-appears-to-disable-executable-build found: NO (tried pkgconfig and cmake)
Has header "inttypes.h" : YES 
Has header "limits.h" : YES 
Has header "linux/rtnetlink.h" : YES 
Has header "memory.h" : YES 
Has header "netdb.h" : YES 
Has header "netinet/icmp6.h" : YES 
Has header "netinet/in.h" : YES 
Has header "netinet/ip6.h" : YES 
Has header "pwd.h" : YES 
Has header "stdint.h" : YES 
Has header "stdlib.h" : YES 
Has header "string.h" : YES 
Has header "strings.h" : YES 
Has header "sys/capability.h" : YES 
Has header "syslog.h" : YES 
Has header "sys/time.h" : YES 
Has header "sys/types.h" : YES 
Has header "sys/uio.h" : YES 
Has header "sys/utsname.h" : YES 
Has header "unistd.h" : YES 
Has header "stdio.h" : YES 
Has header "stdlib.h" : YES (cached)
Has header "stddef.h" : YES 
Has header "stdarg.h" : YES 
Run-time dependency threads found: YES
Has header "error.h" : NO 
Configuring git-version.h using configuration
Configuring config.h using configuration
Program setcap /usr/sbin/setcap /sbin/setcap found: NO
Configuring tftp using configuration
Configuring ninfod.sh using configuration
Message: 

APPLICATIONS (build)
man: false
HTML man: false
arping: true (capability or suid: false)
clockdiff: true (capability or suid: false)
ninfod: true (syslog: true)
ping: true (capability or suid: false)
rarpd: false
rdisc: true (server: true)
tftpd: true
tracepath: true
traceroute6: false (capability or suid: false)

CONFIGURATION
Capatiblity (with libcap): false
IDN (with libidn2): false
I18N (with gettext): false
systemd: false

SYSTEM PATHS
prefix: /usr
bindir: /usr/bin
localedir: /usr/share/locale
sbindir: /usr/sbin
systemdunitdir: 

Build targets in project: 8


ERROR: Could not detect Ninja v1.8.2 or newer

A full log can be found at /openwrt/build_dir/target-aarch64_cortex-a72_musl/iputils-20210202/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:154: /openwrt/build_dir/target-aarch64_cortex-a72_musl/iputils-20210202/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
