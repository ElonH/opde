---
title: "compile.42"
date: 2021-06-29 09:30:58.580372
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
make package/feeds/packages/libgabe/compile -j$(nproc) || make package/feeds/packages/libgabe/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-shared-library.patch using plaintext: 
patching file Makefile.in
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-aarch64_cortex-a72_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/aclocal -I m4 -I . --force 
configure.ac:43: warning: macro 'AM_PATH_GLIB_2_0' not found in library
autoreconf: configure.ac: tracing
autoreconf: configure.ac: not using Libtool
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
configure.ac:43: error: possibly undefined macro: AM_PATH_GLIB_2_0
      If this token and others are legitimate, please use m4_pattern_allow.
      See the Autoconf documentation.
autoreconf: /openwrt/staging_dir/host/bin/autoconf failed with exit status: 1
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/aarch64
checking whether to enable debugging... no
checking for aarch64-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
checking for an ANSI C-conforming const... yes
checking how to run the C preprocessor... ccache_cc -E
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for ANSI C header files... yes
checking for sys/types.h... yes
checking for sys/stat.h... yes
checking for stdlib.h... yes
checking for string.h... yes
checking for memory.h... yes
checking for strings.h... yes
checking for inttypes.h... yes
checking for stdint.h... yes
checking for unistd.h... yes
checking for uint32_t... yes
checking for ANSI C header files... (cached) yes
checking for stdint.h... (cached) yes
checking for stdlib.h... (cached) yes
checking for string.h... (cached) yes
checking for stdlib.h... (cached) yes
checking for GNU libc compatible malloc... (cached) yes
checking for size_t... yes
checking for working alloca.h... yes
checking for alloca... yes
checking for vprintf... yes
checking for _doprnt... no
checking for gcry_md_hash_buffer in -lgcrypt... yes
checking for strdup... yes
./configure: line 4006: syntax error near unexpected token `2.0.0'
./configure: line 4006: `AM_PATH_GLIB_2_0(2.0.0)'
make[3]: *** [Makefile:51: /openwrt/build_dir/target-aarch64_cortex-a72_musl/libgabe-1.0/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 2
```
