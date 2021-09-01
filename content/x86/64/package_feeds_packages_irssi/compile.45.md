---
title: "compile.45"
date: 2021-09-01 09:25:00.625609
hidden: false
draft: false
weight: -45
---

build number: `45`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/irssi/compile -j$(nproc) || make package/feeds/packages/irssi/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-Fix-finding-OpenSSL-when-1.1-with-deprecated-APIs-di.patch using plaintext: 
patching file configure.ac
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-x86_64_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal -I m4 -I . --force -I m4 ${ACLOCAL_FLAGS}
autoreconf: configure.ac: tracing
autoreconf: running: /openwrt/staging_dir/host/bin/libtoolize --install --force
OpenWrt-libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, `build-aux'.
OpenWrt-libtoolize: linking file `build-aux/config.guess'
OpenWrt-libtoolize: linking file `build-aux/config.sub'
OpenWrt-libtoolize: linking file `build-aux/install-sh'
OpenWrt-libtoolize: linking file `build-aux/ltmain.sh'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `m4'.
OpenWrt-libtoolize: linking file `m4/libtool.m4'
OpenWrt-libtoolize: linking file `m4/ltoptions.m4'
OpenWrt-libtoolize: linking file `m4/ltsugar.m4'
OpenWrt-libtoolize: linking file `m4/ltversion.m4'
OpenWrt-libtoolize: linking file `m4/lt~obsolete.m4'
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-x86_64_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-x86_64_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
autoreconf: Leaving directory `.'
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/x86_64
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for x86_64-openwrt-linux-strip... x86_64-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether make supports nested variables... (cached) yes
checking whether to enable maintainer-specific portions of Makefiles... no
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
checking for style of include used by make... GNU
checking dependency style of ccache_cc... gcc3
checking how to run the C preprocessor... ccache_cc -E
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-openwrt-linux-gnu
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache_cc... x86_64-openwrt-linux-musl-ld
checking if the linker (x86_64-openwrt-linux-musl-ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... x86_64-openwrt-linux-musl-gcc-nm
checking the name lister (x86_64-openwrt-linux-musl-gcc-nm) interface... BSD nm
checking whether ln -s works... yes
checking the maximum length of command line arguments... 3145728
checking whether the shell understands some XSI constructs... yes
checking whether the shell understands "+="... yes
checking how to convert x86_64-pc-linux-gnu file names to x86_64-openwrt-linux-gnu format... func_convert_file_noop
checking how to convert x86_64-pc-linux-gnu file names to toolchain format... func_convert_file_noop
checking for x86_64-openwrt-linux-musl-ld option to reload object files... -r
checking for x86_64-openwrt-linux-objdump... x86_64-openwrt-linux-musl-objdump
checking how to recognize dependent libraries... pass_all
checking for x86_64-openwrt-linux-dlltool... no
checking for dlltool... no
checking how to associate runtime and link libraries... printf %s\n
checking for x86_64-openwrt-linux-ar... x86_64-openwrt-linux-musl-gcc-ar
checking for archiver @FILE support... @
checking for x86_64-openwrt-linux-strip... (cached) x86_64-openwrt-linux-musl-strip
checking for x86_64-openwrt-linux-ranlib... x86_64-openwrt-linux-musl-gcc-ranlib
checking command to parse x86_64-openwrt-linux-musl-gcc-nm output from ccache_cc object... ok
checking for sysroot... no
checking for x86_64-openwrt-linux-mt... no
checking for mt... no
checking if : is a manifest tool... no
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
checking for dlfcn.h... yes
checking for objdir... .libs
checking if ccache_cc supports -fno-rtti -fno-exceptions... no
checking for ccache_cc option to produce PIC... -fPIC -DPIC
checking if ccache_cc PIC flag -fPIC -DPIC works... yes
checking if ccache_cc static flag -static works... yes
checking if ccache_cc supports -c -o file.o... yes
checking if ccache_cc supports -c -o file.o... (cached) yes
checking whether the ccache_cc linker (x86_64-openwrt-linux-musl-ld -m elf_x86_64) supports shared libraries... yes
checking whether -lc should be explicitly linked in... no
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... yes
checking for sed... /openwrt/staging_dir/host/bin/sed
checking for perl... /openwrt/staging_dir/host/bin/perl
checking for unistd.h... (cached) yes
checking dirent.h usability... yes
checking dirent.h presence... yes
checking for dirent.h... yes
checking sys/ioctl.h usability... yes
checking sys/ioctl.h presence... yes
checking for sys/ioctl.h... yes
checking sys/resource.h usability... yes
checking sys/resource.h presence... yes
checking for sys/resource.h... yes
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking sys/time.h usability... yes
checking sys/time.h presence... yes
checking for sys/time.h... yes
checking sys/utsname.h usability... yes
checking sys/utsname.h presence... yes
checking for sys/utsname.h... yes
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking for library containing socket... none required
checking for library containing inet_addr... none required
checking for socklen_t... yes
checking size of int... (cached) 4
checking size of long... (cached) 8
checking size of long long... (cached) 8
checking size of off_t... (cached) 8
checking pkg-config is at least version 0.7... yes
checking for GLIB - version >= 2.28.0... no
*** Could not run GLIB test program, checking why...
*** The test program failed to compile or link. See the file config.log for the
*** exact error that occurred. This usually means GLIB is incorrectly installed.
*** trying without -lgmodule
checking pkg-config is at least version 0.7... yes
checking for GLIB - version >= 2.28.0... no
*** Could not run GLIB test program, checking why...
*** The test program failed to compile or link. See the file config.log for the
*** exact error that occurred. This usually means GLIB is incorrectly installed.

*** If you don't have GLIB, you can get it from ftp://ftp.gtk.org/pub/glib/
*** We recommend you get the latest stable GLIB 2 version.
*** Compile and install it, and make sure pkg-config finds it,
*** by adding the path where the .pc file is located to PKG_CONFIG_PATH
*** Or alternatively install your distribution's package:
*** sudo apt-get install libglib2.0-dev

configure: error: GLIB is required to build irssi.
make[3]: *** [Makefile:66: /openwrt/build_dir/target-x86_64_musl/irssi-1.2.3/.configured_a17fb5ef857664f03cd0ce37cc5ea591] Error 1
```
