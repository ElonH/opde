---
title: "compile.42"
date: 2021-06-29 09:31:48.746950
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
make package/feeds/packages/mpd/compile -j$(nproc) || make package/feeds/packages/mpd/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-iconv.patch using plaintext: 
patching file src/lib/icu/meson.build

Applying ./patches/020-string-view.patch using plaintext: 
patching file src/tag/GenParseName.cxx

Applying ./patches/030-no-avfilter.patch using plaintext: 
patching file src/lib/ffmpeg/meson.build
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/mpd-full/mpd-0.22.8
Build dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/mpd-full/mpd-0.22.8/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: mpd
Project version: 0.22.8
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
Configuring Version.h using configuration
Compiler for C++ supports arguments -Wvla: YES 
Compiler for C++ supports arguments -Wdouble-promotion: YES 
Compiler for C++ supports arguments -fvisibility=hidden: YES 
Compiler for C++ supports arguments -ffast-math: YES 
Compiler for C++ supports arguments -ftree-vectorize: YES 
Compiler for C++ supports arguments -fno-threadsafe-statics: YES 
Compiler for C++ supports arguments -fmerge-all-constants: YES 
Compiler for C++ supports arguments -Wmissing-declarations: YES 
Compiler for C++ supports arguments -Wshadow: YES 
Compiler for C++ supports arguments -Wpointer-arith: YES 
Compiler for C++ supports arguments -Wcast-qual: YES 
Compiler for C++ supports arguments -Wwrite-strings: YES 
Compiler for C++ supports arguments -Wsign-compare: YES 
Compiler for C++ supports arguments -Wcomma: NO 
Compiler for C++ supports arguments -Wextra-semi: YES 
Compiler for C++ supports arguments -Wheader-hygiene: NO 
Compiler for C++ supports arguments -Winconsistent-missing-destructor-override: NO 
Compiler for C++ supports arguments -Wunreachable-code-break: NO 
Compiler for C++ supports arguments -Wunused: YES 
Compiler for C++ supports arguments -Wused-but-marked-unused: NO 
Compiler for C++ supports arguments -Wno-non-virtual-dtor: YES 
Compiler for C++ supports arguments -ffunction-sections: YES 
Compiler for C++ supports arguments -fdata-sections: YES 
Compiler for C supports arguments -Wvla: YES 
Compiler for C supports arguments -Wdouble-promotion: YES 
Compiler for C supports arguments -fvisibility=hidden: YES 
Compiler for C supports arguments -ffast-math: YES 
Compiler for C supports arguments -ftree-vectorize: YES 
Compiler for C supports arguments -Wmissing-prototypes: YES 
Compiler for C supports arguments -Wshadow: YES 
Compiler for C supports arguments -Wpointer-arith: YES 
Compiler for C supports arguments -Wstrict-prototypes: YES 
Compiler for C supports arguments -Wcast-qual: YES 
Compiler for C supports arguments -Wwrite-strings: YES 
Compiler for C supports arguments -pedantic: YES 
Compiler for C supports arguments -ffunction-sections: YES 
Compiler for C supports arguments -fdata-sections: YES 
Compiler for C++ supports link arguments -Wl,-z,relro: YES 
Compiler for C++ supports link arguments -Wl,-z,now: YES 
Compiler for C++ supports link arguments -Wl,--gc-sections: YES 
Checking for function "getpwnam_r" : YES 
Checking for function "getpwuid_r" : YES 
Checking for function "initgroups" : YES 
Checking for function "fnmatch" : YES 
Checking for function "strndup" : YES 
Checking for function "strcasestr" : YES 
Checking for function "syslog" : YES 
Found pkg-config: /openwrt/staging_dir/host/bin/pkg-config (1.7.3)
Run-time dependency Boost found: YES 1.76.0 (/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr)
Dependency liburing skipped: feature io_uring disabled
Configuring Features.h using configuration
Run-time dependency threads found: YES
Checking for function "pthread_setname_np" with dependency threads: YES 
Header <sys/socket.h> has symbol "AF_INET6" : YES 
Header <sys/socket.h> has symbol "struct ucred" : YES 
Header <sys/socket.h> has symbol "SO_PEERCRED" : YES 
Checking for function "getpeereid" : NO 
Dependency dbus-1 skipped: feature dbus disabled
Dependency icu-i18n skipped: feature icu disabled
Header <iconv.h> has symbol "iconv" : YES 
Library iconv found: YES
Dependency smbclient skipped: feature smbclient disabled
Run-time dependency zlib found: YES 1.2.11
Run-time dependency alsa found: YES 1.2.5
Dependency libchromaprint skipped: feature chromaprint disabled
Run-time dependency libcurl found: YES 7.77.0
Run-time dependency expat found: YES 2.4.1
Dependency libavformat skipped: feature ffmpeg disabled
Dependency libavcodec skipped: feature ffmpeg disabled
Dependency libavutil skipped: feature ffmpeg disabled
Library gcrypt skipped: feature qobuz disabled
Dependency libnfs skipped: feature nfs disabled
Dependency libpcre skipped: feature pcre disabled
Found CMake: NO
Run-time dependency libpulse found: NO (tried pkgconfig)

../../../../build_dir/target-aarch64_cortex-a72_musl/mpd-full/mpd-0.22.8/src/lib/pulse/meson.build:1:0: ERROR: Dependency "libpulse" not found, tried pkgconfig

A full log can be found at /openwrt/build_dir/target-aarch64_cortex-a72_musl/mpd-full/mpd-0.22.8/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:248: /openwrt/build_dir/target-aarch64_cortex-a72_musl/mpd-full/mpd-0.22.8/.configured_b9c5e0476841007a156251c144ddc1f5] Error 1
```
