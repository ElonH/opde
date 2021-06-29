---
title: "compile.42"
date: 2021-06-29 09:38:24.609854
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
make package/feeds/packages/pixman/compile -j$(nproc) || make package/feeds/packages/pixman/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/0004-pixman-fix-detection-of-mips-dspr2.patch using plaintext: 
patching file configure.ac
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-aarch64_cortex-a72_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/aclocal -I m4 -I . --force 
autoreconf: configure.ac: tracing
autoreconf: running: /openwrt/staging_dir/host/bin/libtoolize --install --force
OpenWrt-libtoolize: putting auxiliary files in `.'.
OpenWrt-libtoolize: linking file `./config.guess'
OpenWrt-libtoolize: linking file `./config.sub'
OpenWrt-libtoolize: linking file `./install-sh'
OpenWrt-libtoolize: linking file `./ltmain.sh'
OpenWrt-libtoolize: Consider adding `AC_CONFIG_MACRO_DIR([m4])' to configure.ac and
OpenWrt-libtoolize: rerunning libtoolize, to keep the correct libtool macros in-tree.
OpenWrt-libtoolize: Consider adding `-I m4' to ACLOCAL_AMFLAGS in Makefile.am.
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
demos/Makefile.am:17: warning: source file '../test/utils.c' is in a subdirectory,
demos/Makefile.am:17: but option 'subdir-objects' is disabled
automake: warning: possible forward-incompatibility.
automake: At least a source file is in a subdirectory, but the 'subdir-objects'
automake: automake option hasn't been enabled.  For now, the corresponding output
automake: object file(s) will be placed in the top-level directory.  However,
automake: this behaviour will change in future Automake versions: they will
automake: unconditionally cause object files to be placed in the same subdirectory
automake: of the corresponding sources.
automake: You are advised to start using 'subdir-objects' option throughout your
automake: project, to avoid future incompatibilities.
demos/Makefile.am:17: warning: source file '../test/utils-prng.c' is in a subdirectory,
demos/Makefile.am:17: but option 'subdir-objects' is disabled
autoreconf: Leaving directory `.'
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/pixman-0.40.0
Build dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/pixman-0.40.0/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: pixman
Project version: 0.40.0
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
Compiler for C supports arguments -Wdeclaration-after-statement: YES 
Compiler for C supports arguments -fno-strict-aliasing: YES 
Compiler for C supports arguments -fvisibility=hidden: YES 
Compiler for C supports arguments -Wundef: YES 
Compiler for C supports arguments -Wunused-local-typedefs: YES 
Checking if "GNU Inline ASM support." compiles: YES 
WARNING: OpenMP found but omp.h missing.
Run-time dependency OpenMP found: NO 
Found pkg-config: /openwrt/staging_dir/host/bin/pkg-config (1.7.3)
Found CMake: NO
Run-time dependency gtk+-2.0 found: NO (tried pkgconfig and cmake)
Run-time dependency glib-2.0 found: NO (tried pkgconfig and cmake)
Run-time dependency pixman-1 found: NO (tried pkgconfig and cmake)
Run-time dependency libpng found: NO (tried pkgconfig and cmake)
Has header "png.h" : NO 
Has header "png.h" : NO (cached)
Has header "png.h" : NO (cached)
Has header "png.h" : NO (cached)
Has header "png.h" : NO (cached)
Has header "png.h" : NO (cached)
Library m found: YES
Run-time dependency threads found: YES
Has header "pthread.h" : YES 
Checking for function "sigaction" : YES 
Checking for function "alarm" : YES 
Checking for function "mprotect" : YES 
Checking for function "getpagesize" : YES 
Checking for function "mmap" : YES 
Checking for function "getisax" : NO 
Checking for function "gettimeofday" : YES 
Checking for function "posix_memalign" : YES 
Checking for function "feenableexcept" with dependency -lm: NO 
Header <fenv.h> has symbol "FE_DIVBYZERO" : YES 
Check usable header "sys/mman.h" : YES 
Check usable header "fenv.h" : YES 
Check usable header "unistd.h" : YES 
Checking if "TLS via __thread" compiles: YES 
Checking if "__attribute__((constructor))" links: YES 
Checking if "Has float128 support" links: NO 
Checking for function "clz" : YES 
Checking if "Support for GCC vector extensions" links: YES 
Checking for size of "long" : 8
Configuring config.h using configuration
Configuring pixman-version.h using configuration
Compiler for C supports function attribute dllexport: NO 
Build targets in project: 40

Option buildtype is: plain [default: debugoptimized]

ERROR: Could not detect Ninja v1.8.2 or newer

A full log can be found at /openwrt/build_dir/target-aarch64_cortex-a72_musl/pixman-0.40.0/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:61: /openwrt/build_dir/target-aarch64_cortex-a72_musl/pixman-0.40.0/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
