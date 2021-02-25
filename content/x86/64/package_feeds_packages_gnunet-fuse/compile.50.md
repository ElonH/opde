---
title: "compile.50"
date: 2021-02-25 14:20:49.079920
hidden: false
draft: false
weight: -50
---

build number: `50`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/gnunet-fuse/compile -j$(nproc) || make package/feeds/packages/gnunet-fuse/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-musl-compat.patch using plaintext: 
patching file src/fuse/mutex.c
autopoint: *** Missing version: please specify in configure.ac through a line 'AM_GNU_GETTEXT_VERSION(x.yy.zz)' the gettext version the package is using
autopoint: *** Stop.
autoreconf: Entering directory `.'
autoreconf: running: true --force
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-x86_64_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal -I m4 -I . --force -I m4
autoreconf: configure.ac: tracing
autoreconf: configure.ac: not using Libtool
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-x86_64_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-x86_64_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
autoreconf: Leaving directory `.'
configure: loading site script /openwrt/include/site/x86_64
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for x86_64-openwrt-linux-strip... x86_64-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking for style of include used by make... GNU
checking for x86_64-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
checking whether ccache_cc understands -c and -o together... yes
checking dependency style of ccache_cc... gcc3
checking for library containing strerror... none required
checking for gawk... (cached) gawk
checking for x86_64-openwrt-linux-gcc... (cached) ccache_cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether ccache_cc accepts -g... (cached) yes
checking for ccache_cc option to accept ISO C89... (cached) none needed
checking whether ccache_cc understands -c and -o together... (cached) yes
checking dependency style of ccache_cc... (cached) gcc3
checking whether ln -s works... yes
checking whether make sets $(MAKE)... (cached) yes
checking for x86_64-openwrt-linux-gcc... (cached) ccache_cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether ccache_cc accepts -g... (cached) yes
checking for ccache_cc option to accept ISO C89... (cached) none needed
checking whether ccache_cc understands -c and -o together... (cached) yes
checking dependency style of ccache_cc... (cached) gcc3
checking for x86_64-openwrt-linux-gcc... (cached) ccache_cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether ccache_cc accepts -g... (cached) yes
checking for ccache_cc option to accept ISO C89... (cached) none needed
checking whether ccache_cc understands -c and -o together... (cached) yes
checking dependency style of ccache_cc... (cached) gcc3
checking how to run the C preprocessor... ccache_cc -E
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for ANSI C header files... yes
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-openwrt-linux-gnu
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking for _LARGEFILE_SOURCE value needed for large files... no
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking whether NLS is requested... no
checking for msgfmt... /openwrt/staging_dir/hostpkg/bin/msgfmt
checking for gmsgfmt... /openwrt/staging_dir/hostpkg/bin/msgfmt
checking for xgettext... /openwrt/staging_dir/hostpkg/bin/xgettext
checking for msgmerge... /openwrt/staging_dir/hostpkg/bin/msgmerge
checking for ld... x86_64-openwrt-linux-musl-ld
checking if the linker (x86_64-openwrt-linux-musl-ld) is GNU ld... yes
checking for shared library run path origin... done
checking 32-bit host C ABI... no
checking for ELF binary format... yes
checking for the common suffixes of directories in the library search path... lib,lib,lib64
checking for CFPreferencesCopyAppValue... no
checking for CFLocaleCopyPreferredLanguages... no
checking whether to use NLS... no
checking for sys/types.h... yes
checking for sys/stat.h... yes
checking for stdlib.h... yes
checking for string.h... yes
checking for memory.h... yes
checking for strings.h... yes
checking for inttypes.h... yes
checking for stdint.h... yes
checking for unistd.h... yes
checking errno.h usability... yes
checking errno.h presence... yes
checking for errno.h... yes
checking stdio.h usability... yes
checking stdio.h presence... yes
checking for stdio.h... yes
checking for unistd.h... (cached) yes
checking locale.h usability... yes
checking locale.h presence... yes
checking for locale.h... yes
checking for sys/stat.h... (cached) yes
checking for sys/types.h... (cached) yes
checking langinfo.h usability... yes
checking langinfo.h presence... yes
checking for langinfo.h... yes
checking libintl.h usability... yes
checking libintl.h presence... yes
checking for libintl.h... yes
checking for unistd.h... (cached) yes
checking stddef.h usability... yes
checking stddef.h presence... yes
checking for stddef.h... yes
checking argz.h usability... no
checking argz.h presence... no
checking for argz.h... no
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking netinet/in.h usability... yes
checking netinet/in.h presence... yes
checking for netinet/in.h... yes
checking stdarg.h usability... yes
checking stdarg.h presence... yes
checking for stdarg.h... yes
checking sys/param.h usability... yes
checking sys/param.h presence... yes
checking for sys/param.h... yes
checking for library containing fuse_exit... -lfuse
checking for uncrustify... no
checking for GNUnet core... /openwrt/staging_dir/target-x86_64_musl/usr
checking for GNUnet util library in /openwrt/staging_dir/target-x86_64_musl/usr... checking for gnunet/gnunet_util_lib.h... no
configure: error: gnunet-fuse requires GNUnet
make[3]: *** [Makefile:44: /openwrt/build_dir/target-x86_64_musl/gnunet-fuse-0.13.0/.configured_a17fb5ef857664f03cd0ce37cc5ea591] Error 1
```
