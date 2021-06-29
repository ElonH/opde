---
title: "compile.42"
date: 2021-06-29 09:30:58.581381
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
make package/feeds/packages/gnunet-fuse/compile -j$(nproc) || make package/feeds/packages/gnunet-fuse/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-musl-compat.patch using plaintext: 
patching file src/fuse/mutex.c
Copying file ABOUT-NLS
Copying file config.rpath
Copying file m4/gettext.m4
Copying file m4/host-cpu-c-abi.m4
Copying file m4/iconv.m4
Copying file m4/intlmacosx.m4
Copying file m4/lib-ld.m4
Copying file m4/lib-link.m4
Copying file m4/lib-prefix.m4
Copying file m4/nls.m4
Copying file m4/po.m4
Copying file m4/progtest.m4
Copying file po/Makefile.in.in
Copying file po/Makevars.template
Copying file po/Rules-quot
Copying file po/en@boldquot.header
Copying file po/en@quot.header
Copying file po/insert-header.sin
Copying file po/remove-potcdate.sin
autoreconf: Entering directory `.'
autoreconf: running: true --force
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-aarch64_cortex-a72_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/aclocal -I m4 -I . --force -I m4
autoreconf: configure.ac: tracing
autoreconf: configure.ac: not using Libtool
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
autoreconf: Leaving directory `.'
configure: loading site script /openwrt/include/site/aarch64
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for aarch64-openwrt-linux-strip... aarch64-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking for style of include used by make... GNU
checking for aarch64-openwrt-linux-gcc... ccache_cc
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
checking for aarch64-openwrt-linux-gcc... (cached) ccache_cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether ccache_cc accepts -g... (cached) yes
checking for ccache_cc option to accept ISO C89... (cached) none needed
checking whether ccache_cc understands -c and -o together... (cached) yes
checking dependency style of ccache_cc... (cached) gcc3
checking whether ln -s works... yes
checking whether make sets $(MAKE)... (cached) yes
checking for aarch64-openwrt-linux-gcc... (cached) ccache_cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether ccache_cc accepts -g... (cached) yes
checking for ccache_cc option to accept ISO C89... (cached) none needed
checking whether ccache_cc understands -c and -o together... (cached) yes
checking dependency style of ccache_cc... (cached) gcc3
checking for aarch64-openwrt-linux-gcc... (cached) ccache_cc
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
checking host system type... aarch64-openwrt-linux-gnu
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking for _LARGEFILE_SOURCE value needed for large files... no
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking whether NLS is requested... no
checking for msgfmt... /openwrt/staging_dir/hostpkg/bin/msgfmt
checking for gmsgfmt... /openwrt/staging_dir/hostpkg/bin/msgfmt
checking for xgettext... /openwrt/staging_dir/hostpkg/bin/xgettext
checking for msgmerge... /openwrt/staging_dir/hostpkg/bin/msgmerge
checking for ld... aarch64-openwrt-linux-musl-ld
checking if the linker (aarch64-openwrt-linux-musl-ld) is GNU ld... yes
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
checking for GNUnet core... /openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr
checking for GNUnet util library in /openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr... checking for gnunet/gnunet_util_lib.h... yes
checking for GNUNET_xfree_ in -lgnunetutil... yes
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating Makefile
config.status: creating po/Makefile.in
config.status: creating doc/Makefile
config.status: creating src/Makefile
config.status: creating src/fuse/Makefile
config.status: creating gnunet_fuse_config.h
config.status: executing depfiles commands
config.status: executing po-directories commands
config.status: creating po/POTFILES
config.status: creating po/Makefile
make[4]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0'
make  all-recursive
make[5]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0'
Making all in src
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/src'
Making all in fuse
make[7]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/src/fuse'
Making all in .
make[8]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/src/fuse'
ccache_cc -DHAVE_CONFIG_H -I. -I../..  -I../../src/include -I../.. -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include -D_FILE_OFFSET_BITS=64 -DFUSE_USE_VERSION=26 -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include   -fno-strict-aliasing -Wall -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0=gnunet-fuse-0.14.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include 	 -MT gnunet_fuse-gnunet-fuse.o -MD -MP -MF .deps/gnunet_fuse-gnunet-fuse.Tpo -c -o gnunet_fuse-gnunet-fuse.o `test -f 'gnunet-fuse.c' || echo './'`gnunet-fuse.c
ccache_cc -DHAVE_CONFIG_H -I. -I../..  -I../../src/include -I../.. -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include -D_FILE_OFFSET_BITS=64 -DFUSE_USE_VERSION=26 -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include   -fno-strict-aliasing -Wall -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0=gnunet-fuse-0.14.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include 	 -MT gnunet_fuse-gfs_download.o -MD -MP -MF .deps/gnunet_fuse-gfs_download.Tpo -c -o gnunet_fuse-gfs_download.o `test -f 'gfs_download.c' || echo './'`gfs_download.c
mv -f .deps/gnunet_fuse-gfs_download.Tpo .deps/gnunet_fuse-gfs_download.Po
ccache_cc -DHAVE_CONFIG_H -I. -I../..  -I../../src/include -I../.. -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include -D_FILE_OFFSET_BITS=64 -DFUSE_USE_VERSION=26 -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include   -fno-strict-aliasing -Wall -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0=gnunet-fuse-0.14.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include 	 -MT gnunet_fuse-mutex.o -MD -MP -MF .deps/gnunet_fuse-mutex.Tpo -c -o gnunet_fuse-mutex.o `test -f 'mutex.c' || echo './'`mutex.c
mv -f .deps/gnunet_fuse-gnunet-fuse.Tpo .deps/gnunet_fuse-gnunet-fuse.Po
ccache_cc -DHAVE_CONFIG_H -I. -I../..  -I../../src/include -I../.. -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include -D_FILE_OFFSET_BITS=64 -DFUSE_USE_VERSION=26 -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include   -fno-strict-aliasing -Wall -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0=gnunet-fuse-0.14.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include 	 -MT gnunet_fuse-readdir.o -MD -MP -MF .deps/gnunet_fuse-readdir.Tpo -c -o gnunet_fuse-readdir.o `test -f 'readdir.c' || echo './'`readdir.c
mv -f .deps/gnunet_fuse-mutex.Tpo .deps/gnunet_fuse-mutex.Po
ccache_cc -DHAVE_CONFIG_H -I. -I../..  -I../../src/include -I../.. -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include -D_FILE_OFFSET_BITS=64 -DFUSE_USE_VERSION=26 -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include   -fno-strict-aliasing -Wall -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0=gnunet-fuse-0.14.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include 	 -MT gnunet_fuse-read.o -MD -MP -MF .deps/gnunet_fuse-read.Tpo -c -o gnunet_fuse-read.o `test -f 'read.c' || echo './'`read.c
mv -f .deps/gnunet_fuse-readdir.Tpo .deps/gnunet_fuse-readdir.Po
ccache_cc -DHAVE_CONFIG_H -I. -I../..  -I../../src/include -I../.. -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include -D_FILE_OFFSET_BITS=64 -DFUSE_USE_VERSION=26 -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include   -fno-strict-aliasing -Wall -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0=gnunet-fuse-0.14.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include 	 -MT gnunet_fuse-open.o -MD -MP -MF .deps/gnunet_fuse-open.Tpo -c -o gnunet_fuse-open.o `test -f 'open.c' || echo './'`open.c
mv -f .deps/gnunet_fuse-read.Tpo .deps/gnunet_fuse-read.Po
ccache_cc -DHAVE_CONFIG_H -I. -I../..  -I../../src/include -I../.. -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include -D_FILE_OFFSET_BITS=64 -DFUSE_USE_VERSION=26 -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include   -fno-strict-aliasing -Wall -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0=gnunet-fuse-0.14.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include 	 -MT gnunet_fuse-getattr.o -MD -MP -MF .deps/gnunet_fuse-getattr.Tpo -c -o gnunet_fuse-getattr.o `test -f 'getattr.c' || echo './'`getattr.c
mv -f .deps/gnunet_fuse-open.Tpo .deps/gnunet_fuse-open.Po
mv -f .deps/gnunet_fuse-getattr.Tpo .deps/gnunet_fuse-getattr.Po
ccache_cc  -fno-strict-aliasing -Wall -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0=gnunet-fuse-0.14.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include 	  -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib  -o gnunet-fuse gnunet_fuse-gnunet-fuse.o gnunet_fuse-gfs_download.o gnunet_fuse-mutex.o gnunet_fuse-readdir.o gnunet_fuse-read.o gnunet_fuse-open.o gnunet_fuse-getattr.o -lgnunetutil -lfuse -lgnunetfs  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lpthread 
make[8]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/src/fuse'
make[7]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/src/fuse'
Making all in .
make[7]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/src'
make[7]: Nothing to be done for 'all-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/src'
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/src'
Making all in doc
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/doc'
make[6]: Nothing to be done for 'all'.
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/doc'
Making all in po
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/po'
make[6]: Nothing to be done for 'all'.
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/po'
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0'
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0'
make[5]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0'
make[4]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0'
make[4]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0'
Making install in src
make[5]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/src'
Making install in fuse
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/src/fuse'
Making install in .
make[7]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/src/fuse'
make[8]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/src/fuse'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/ipkg-install/usr/bin'
  /openwrt/staging_dir/host/bin/install -c gnunet-fuse '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/ipkg-install/usr/bin'
make[8]: Nothing to be done for 'install-data-am'.
make[8]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/src/fuse'
make[7]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/src/fuse'
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/src/fuse'
Making install in .
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/src'
make[7]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/src'
make[7]: Nothing to be done for 'install-exec-am'.
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/src'
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/src'
make[5]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/src'
Making install in doc
make[5]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/doc'
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/doc'
make[6]: Nothing to be done for 'install-exec-am'.
 /usr/bin/mkdir -p '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/ipkg-install/usr/man/man1'
 /openwrt/staging_dir/host/bin/install -c -m 644 gnunet-fuse.1 '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/ipkg-install/usr/man/man1'
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/doc'
make[5]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/doc'
Making install in po
make[5]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/po'
if test "gnunet-fuse" = "gettext-tools"; then \
  /usr/bin/mkdir -p /openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/ipkg-install/usr/share/gettext/po; \
  for file in Makefile.in.in remove-potcdate.sin quot.sed boldquot.sed en@quot.header en@boldquot.header insert-header.sin Rules-quot   Makevars.template; do \
    /openwrt/staging_dir/host/bin/install -c -m 644 ./$file \
		    /openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/ipkg-install/usr/share/gettext/po/$file; \
  done; \
  for file in Makevars; do \
    rm -f /openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/ipkg-install/usr/share/gettext/po/$file; \
  done; \
else \
  : ; \
fi
make[5]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0/po'
make[5]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0'
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0'
make[6]: Nothing to be done for 'install-exec-am'.
make[6]: Nothing to be done for 'install-data-am'.
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0'
make[5]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0'
make[4]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gnunet-fuse-0.14.0'
Package gnunet-fuse is missing dependencies for the following libraries:
libgnunetfs.so.2
make[3]: *** [Makefile:49: /openwrt/bin/packages/aarch64_cortex-a72/packages/gnunet-fuse_0.14.0-1_aarch64_cortex-a72.ipk] Error 1
```
