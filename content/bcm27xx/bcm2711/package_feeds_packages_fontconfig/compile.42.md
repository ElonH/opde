---
title: "compile.42"
date: 2021-06-29 09:38:24.600303
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
make package/feeds/packages/fontconfig/compile -j$(nproc) || make package/feeds/packages/fontconfig/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-Handle-absolute-sysconfdir-when-installing-symlinks.patch using plaintext: 
patching file conf.d/link_confs.py

Applying ./patches/020-distutils.patch using plaintext: 
patching file meson.build
Cloning into 'freetype2'...
Already on 'meson'
Your branch is up to date with 'origin/meson'.
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/fontconfig-2.13.93
Build dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/fontconfig-2.13.93/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: fontconfig
Project version: 2.13.93
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
Run-time dependency freetype2 found: NO (tried pkgconfig)
Found CMake: NO
Run-time dependency freetype found: NO (tried cmake)
Looking for a fallback subproject for the dependency freetype

|Executing subproject freetype2 method meson 
|
|Project name: freetype2
|Project version: 22.1.16
|C compiler for the host machine: ccache_cc (gcc 8.4.0 "aarch64-openwrt-linux-musl-gcc (OpenWrt GCC 8.4.0 r0-af265d3) 8.4.0")
|C linker for the host machine: ccache_cc ld.bfd 2.34
|C compiler for the build machine: ccache gcc (gcc 9.3.0 "gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0")
|C linker for the build machine: gcc ld.bfd 2.34
|Has header "unistd.h" : YES 
|Has header "fcntl.h" : YES 
|Has header "stdint.h" : YES 
|Library bz2 found: YES
|Header <bzlib.h> has symbol "BZ2_bzlibVersion" : YES 
|Dependency harfbuzz skipped: feature harfbuzz disabled
|Run-time dependency zlib found: YES 1.2.11
|Run-time dependency libpng found: YES 1.6.37
|Configuring ftconfig.h using configuration
|Program include/configure-ftoption_h.py found: YES (/openwrt/staging_dir/host/bin/python /openwrt/build_dir/target-aarch64_cortex-a72_musl/fontconfig-2.13.93/subprojects/freetype2/include/configure-ftoption_h.py)
|Configuring ftoption.h.in with command
|Configuring ftoption.h using configuration
|Build targets in project: 1
|Subproject freetype2 finished.

Dependency freetype from subproject subprojects/freetype2 found: YES 22.1.16
Run-time dependency expat found: YES 2.4.1
Has header "dirent.h" : YES 
Has header "fcntl.h" : YES (cached)
Has header "stdlib.h" : YES 
Has header "string.h" : YES 
Has header "unistd.h" : YES (cached)
Has header "sys/statvfs.h" : YES 
Has header "sys/vfs.h" : YES 
Has header "sys/statfs.h" : YES 
Has header "sys/param.h" : YES 
Has header "sys/mount.h" : YES 
Checking for function "link" : YES 
Checking for function "mkstemp" : YES 
Checking for function "mkostemp" : YES 
Checking for function "_mktemp_s" : NO 
Checking for function "mkdtemp" : YES 
Checking for function "getopt" : YES 
Checking for function "getopt_long" : YES 
Checking for function "getprogname" : NO 
Checking for function "getexecname" : NO 
Checking for function "rand" : YES 
Checking for function "random" : YES 
Checking for function "lrand48" : YES 
Checking for function "random_r" : NO 
Checking for function "rand_r" : YES 
Checking for function "readlink" : YES 
Checking for function "fstatvfs" : YES 
Checking for function "fstatfs" : YES 
Checking for function "lstat" : YES 
Checking for function "mmap" : YES 
Checking for function "vprintf" : YES 
Header <fcntl.h> has symbol "posix_fadvise" : YES 
Checking whether type "struct statvfs" has member "f_basetype" : NO 
Checking whether type "struct statvfs" has member "f_fstypename" : NO 
Checking whether type "struct statfs" has member "f_flags" : NO 
Checking whether type "struct statfs" has member "f_fstypename" : NO 
Checking whether type "struct dirent" has member "d_type" : YES 
Checking for size of "void *" : 8
Checking for alignment of "void *" : 8
Checking for alignment of "double" : 8
Checking if "Intel atomics" links: YES 
Checking if "Solaris atomic ops" links: NO 
Run-time dependency threads found: YES
Program gperf found: YES (/openwrt/staging_dir/hostpkg/bin/gperf)
Program sh found: YES (/usr/bin/sh)
Message: gperf len type is size_t
Checking for type "uint64_t" : YES 
Checking for type "int32_t" : YES 
Checking for type "uintptr_t" : YES 
Checking for type "intptr_t" : YES 
Program fc-case.py found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/fontconfig-2.13.93/fc-case/fc-case.py)
Program fc-lang.py found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/fontconfig-2.13.93/fc-lang/fc-lang.py)
Program link_confs.py found: YES (/openwrt/staging_dir/host/bin/python /openwrt/build_dir/target-aarch64_cortex-a72_musl/fontconfig-2.13.93/conf.d/link_confs.py)
Program write-35-lang-normalize-conf.py found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/fontconfig-2.13.93/conf.d/write-35-lang-normalize-conf.py)
Configuring README using configuration
Program xgettext skipped: feature nls disabled
Configuring config.h using configuration
Configuring fonts.conf using configuration
WARNING: Project targeting '>= 0.53' but tried to use feature introduced in '0.54.0': list_sep arg in summary.
Build targets in project: 18
WARNING: Project specifies a minimum meson_version '>= 0.50.0' but uses features which were added in newer versions:
 * 0.54.0: {'list_sep arg in summary'}

fontconfig 2.13.93

  General
    Documentation: NO
    NLS          : NO
    Tests        : NO
    Tools        : YES

  Subprojects
    freetype2    : YES

Option buildtype is: plain [default: debugoptimized]

ERROR: Could not detect Ninja v1.8.2 or newer

A full log can be found at /openwrt/build_dir/target-aarch64_cortex-a72_musl/fontconfig-2.13.93/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:72: /openwrt/build_dir/target-aarch64_cortex-a72_musl/fontconfig-2.13.93/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
