---
title: "compile.37"
date: 2021-06-20 22:32:33.828451
hidden: false
draft: false
weight: -37
---

build number: `37`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/netifyd/compile -j$(nproc) || make package/feeds/packages/netifyd/compile V=s
```

#### Compile.txt

``` bash
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force ${ACLOCAL_FLAGS} -I m4
autoreconf: configure.ac: tracing
autoreconf: configure.ac: adding subdirectory libs/inih to autoreconf
autoreconf: Entering directory `libs/inih'
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force -I m4
autoreconf: running: /openwrt/staging_dir/host/bin/libtoolize --install --force
OpenWrt-libtoolize: putting auxiliary files in `.'.
OpenWrt-libtoolize: linking file `./config.guess'
OpenWrt-libtoolize: linking file `./config.sub'
OpenWrt-libtoolize: linking file `./install-sh'
OpenWrt-libtoolize: linking file `./ltmain.sh'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `m4'.
OpenWrt-libtoolize: linking file `m4/libtool.m4'
OpenWrt-libtoolize: linking file `m4/ltoptions.m4'
OpenWrt-libtoolize: linking file `m4/ltsugar.m4'
OpenWrt-libtoolize: linking file `m4/ltversion.m4'
OpenWrt-libtoolize: linking file `m4/lt~obsolete.m4'
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
configure.ac:12: installing './compile'
configure.ac:6: installing './missing'
Makefile.am: installing './depcomp'
autoreconf: Leaving directory `libs/inih'
autoreconf: configure.ac: adding subdirectory libs/ndpi to autoreconf
autoreconf: Entering directory `libs/ndpi'
autoreconf: configure.ac: not using Autoconf
autoreconf: Leaving directory `libs/ndpi'
autoreconf: configure.ac: adding subdirectory libs/gperftools to autoreconf
autoreconf: Entering directory `libs/gperftools'
OpenWrt-libtoolize: putting auxiliary files in `.'.
OpenWrt-libtoolize: linking file `./config.guess'
OpenWrt-libtoolize: linking file `./config.sub'
OpenWrt-libtoolize: linking file `./install-sh'
OpenWrt-libtoolize: linking file `./ltmain.sh'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `m4'.
OpenWrt-libtoolize: linking file `m4/libtool.m4'
OpenWrt-libtoolize: linking file `m4/ltoptions.m4'
OpenWrt-libtoolize: linking file `m4/ltsugar.m4'
OpenWrt-libtoolize: linking file `m4/ltversion.m4'
OpenWrt-libtoolize: linking file `m4/lt~obsolete.m4'
configure.ac:57: installing './compile'
configure.ac:21: installing './missing'
Makefile.am: installing './depcomp'
parallel-tests: installing './test-driver'
autoreconf: Leaving directory `libs/gperftools'
OpenWrt-libtoolize: putting auxiliary files in `.'.
OpenWrt-libtoolize: linking file `./config.guess'
OpenWrt-libtoolize: linking file `./config.sub'
OpenWrt-libtoolize: linking file `./install-sh'
OpenWrt-libtoolize: linking file `./ltmain.sh'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `m4'.
OpenWrt-libtoolize: linking file `m4/libtool.m4'
OpenWrt-libtoolize: linking file `m4/ltoptions.m4'
OpenWrt-libtoolize: linking file `m4/ltsugar.m4'
OpenWrt-libtoolize: linking file `m4/ltversion.m4'
OpenWrt-libtoolize: linking file `m4/lt~obsolete.m4'
configure.ac:17: installing './compile'
configure.ac:12: installing './missing'
deploy/Makefile.am:21: warning: '%'-style pattern rules are a GNU make extension
deploy/debian/Makefile.am:13: warning: '%'-style pattern rules are a GNU make extension
deploy/edgeos/Makefile.am:13: warning: '%'-style pattern rules are a GNU make extension
deploy/systemd/Makefile.am:21: warning: '%'-style pattern rules are a GNU make extension
deploy/ubios/Makefile.am:13: warning: '%'-style pattern rules are a GNU make extension
src/Makefile.am: installing './depcomp'
autoreconf: Leaving directory `.'
+ SUBDIRS=libs/gperftools libs/ndpi
+ cd libs/gperftools
+ ./autogen.sh
+ cd libs/ndpi
+ ./autogen.sh
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: aclocal --force -I m4
autoreconf: configure.ac: tracing
autoreconf: running: libtoolize --copy --force
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `m4'.
OpenWrt-libtoolize: copying file `m4/libtool.m4'
OpenWrt-libtoolize: copying file `m4/ltoptions.m4'
OpenWrt-libtoolize: copying file `m4/ltsugar.m4'
OpenWrt-libtoolize: copying file `m4/ltversion.m4'
OpenWrt-libtoolize: copying file `m4/lt~obsolete.m4'
autoreconf: running: /openwrt/staging_dir/target-mips_24kc_musl/../host/bin/autoconf --force
autoreconf: running: /openwrt/staging_dir/target-mips_24kc_musl/../host/bin/autoheader --force
autoreconf: running: automake --add-missing --copy --force-missing
autoreconf: Leaving directory `.'
+ xargs touch
+ pwd
+ find /openwrt/build_dir/target-mips_24kc_musl/netifyd-2021-05-19-v3.07 -name configure.ac
+ mkdir -vp m4 libs/inih/m4
+ libtoolize --force
OpenWrt-libtoolize: putting auxiliary files in `.'.
OpenWrt-libtoolize: linking file `./ltmain.sh'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `m4'.
OpenWrt-libtoolize: linking file `m4/libtool.m4'
OpenWrt-libtoolize: linking file `m4/ltoptions.m4'
OpenWrt-libtoolize: linking file `m4/ltsugar.m4'
OpenWrt-libtoolize: linking file `m4/ltversion.m4'
OpenWrt-libtoolize: linking file `m4/lt~obsolete.m4'
+ aclocal
+ autoheader
+ automake --force-missing --add-missing
deploy/Makefile.am:21: warning: '%'-style pattern rules are a GNU make extension
deploy/debian/Makefile.am:13: warning: '%'-style pattern rules are a GNU make extension
deploy/edgeos/Makefile.am:13: warning: '%'-style pattern rules are a GNU make extension
deploy/systemd/Makefile.am:21: warning: '%'-style pattern rules are a GNU make extension
deploy/ubios/Makefile.am:13: warning: '%'-style pattern rules are a GNU make extension
+ autoreconf -i --force -I m4
OpenWrt-libtoolize: putting auxiliary files in `.'.
OpenWrt-libtoolize: copying file `./ltmain.sh'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `m4'.
OpenWrt-libtoolize: copying file `m4/libtool.m4'
OpenWrt-libtoolize: copying file `m4/ltoptions.m4'
OpenWrt-libtoolize: copying file `m4/ltsugar.m4'
OpenWrt-libtoolize: copying file `m4/ltversion.m4'
OpenWrt-libtoolize: copying file `m4/lt~obsolete.m4'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `m4'.
OpenWrt-libtoolize: copying file `m4/libtool.m4'
OpenWrt-libtoolize: copying file `m4/ltoptions.m4'
OpenWrt-libtoolize: copying file `m4/ltsugar.m4'
OpenWrt-libtoolize: copying file `m4/ltversion.m4'
OpenWrt-libtoolize: copying file `m4/lt~obsolete.m4'
OpenWrt-libtoolize: putting auxiliary files in `.'.
OpenWrt-libtoolize: copying file `./ltmain.sh'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `m4'.
OpenWrt-libtoolize: copying file `m4/libtool.m4'
OpenWrt-libtoolize: copying file `m4/ltoptions.m4'
OpenWrt-libtoolize: copying file `m4/ltsugar.m4'
OpenWrt-libtoolize: copying file `m4/ltversion.m4'
OpenWrt-libtoolize: copying file `m4/lt~obsolete.m4'
OpenWrt-libtoolize: putting auxiliary files in `.'.
OpenWrt-libtoolize: copying file `./ltmain.sh'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `m4'.
OpenWrt-libtoolize: copying file `m4/libtool.m4'
OpenWrt-libtoolize: copying file `m4/ltoptions.m4'
OpenWrt-libtoolize: copying file `m4/ltsugar.m4'
OpenWrt-libtoolize: copying file `m4/ltversion.m4'
OpenWrt-libtoolize: copying file `m4/lt~obsolete.m4'
deploy/Makefile.am:21: warning: '%'-style pattern rules are a GNU make extension
deploy/debian/Makefile.am:13: warning: '%'-style pattern rules are a GNU make extension
deploy/edgeos/Makefile.am:13: warning: '%'-style pattern rules are a GNU make extension
deploy/systemd/Makefile.am:21: warning: '%'-style pattern rules are a GNU make extension
deploy/ubios/Makefile.am:13: warning: '%'-style pattern rules are a GNU make extension
configure: loading site script /openwrt/include/site/mips
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking how to create a pax tar archive... gnutar
checking for style of include used by make... GNU
checking for mips-openwrt-linux-gcc... ccache_cc
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
checking minix/config.h usability... no
checking minix/config.h presence... no
checking for minix/config.h... no
checking whether it is safe to define __EXTENSIONS__... yes
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking for mips-openwrt-linux-gcc... (cached) ccache_cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether ccache_cc accepts -g... (cached) yes
checking for ccache_cc option to accept ISO C89... (cached) none needed
checking whether ccache_cc understands -c and -o together... (cached) yes
checking dependency style of ccache_cc... (cached) gcc3
checking whether we are using the GNU C++ compiler... yes
checking whether ccache_cxx accepts -g... yes
checking dependency style of ccache_cxx... gcc3
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache_cc... mips-openwrt-linux-musl-ld
checking if the linker (mips-openwrt-linux-musl-ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... mips-openwrt-linux-musl-gcc-nm
checking the name lister (mips-openwrt-linux-musl-gcc-nm) interface... BSD nm
checking whether ln -s works... yes
checking the maximum length of command line arguments... 3145728
checking whether the shell understands some XSI constructs... yes
checking whether the shell understands "+="... yes
checking how to convert x86_64-pc-linux-gnu file names to mips-openwrt-linux-gnu format... func_convert_file_noop
checking how to convert x86_64-pc-linux-gnu file names to toolchain format... func_convert_file_noop
checking for mips-openwrt-linux-musl-ld option to reload object files... -r
checking for mips-openwrt-linux-objdump... mips-openwrt-linux-musl-objdump
checking how to recognize dependent libraries... pass_all
checking for mips-openwrt-linux-dlltool... no
checking for dlltool... no
checking how to associate runtime and link libraries... printf %s\n
checking for mips-openwrt-linux-ar... mips-openwrt-linux-musl-gcc-ar
checking for archiver @FILE support... @
checking for mips-openwrt-linux-strip... (cached) mips-openwrt-linux-musl-strip
checking for mips-openwrt-linux-ranlib... mips-openwrt-linux-musl-gcc-ranlib
checking command to parse mips-openwrt-linux-musl-gcc-nm output from ccache_cc object... ok
checking for sysroot... no
checking for mips-openwrt-linux-mt... no
checking for mt... no
checking if : is a manifest tool... no
checking for dlfcn.h... yes
checking for objdir... .libs
checking if ccache_cc supports -fno-rtti -fno-exceptions... no
checking for ccache_cc option to produce PIC... -fPIC -DPIC
checking if ccache_cc PIC flag -fPIC -DPIC works... yes
checking if ccache_cc static flag -static works... yes
checking if ccache_cc supports -c -o file.o... yes
checking if ccache_cc supports -c -o file.o... (cached) yes
checking whether the ccache_cc linker (mips-openwrt-linux-musl-ld) supports shared libraries... yes
checking whether -lc should be explicitly linked in... no
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... yes
checking how to run the C++ preprocessor... ccache_cxx -E
checking for ld used by ccache_cxx... mips-openwrt-linux-musl-ld
checking if the linker (mips-openwrt-linux-musl-ld) is GNU ld... yes
checking whether the ccache_cxx linker (mips-openwrt-linux-musl-ld) supports shared libraries... yes
checking for ccache_cxx option to produce PIC... -fPIC -DPIC
checking if ccache_cxx PIC flag -fPIC -DPIC works... yes
checking if ccache_cxx static flag -static works... yes
checking if ccache_cxx supports -c -o file.o... yes
checking if ccache_cxx supports -c -o file.o... (cached) yes
checking whether the ccache_cxx linker (mips-openwrt-linux-musl-ld) supports shared libraries... yes
checking dynamic linker characteristics... (cached) GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking pkg-config is at least version 0.23... yes
checking for bash... /openwrt/staging_dir/host/bin/bash
checking for osc... no
checking whether ccache_cxx supports C++11 features by default... yes
checking for pcap_open_live in -lpcap... yes
checking for pthread_create in -lpthread... yes
checking for timer_create in -lrt... yes
checking for ns_initparse in -lresolv... yes
checking for LIBCURL... no
configure: error: Package requirements (libcurl) were not met:

Package 'libcurl', required by 'virtual:world', not found

Consider adjusting the PKG_CONFIG_PATH environment variable if you
installed software in a non-standard prefix.

Alternatively, you may set the environment variables LIBCURL_CFLAGS
and LIBCURL_LIBS to avoid the need to call pkg-config.
See the pkg-config man page for more details.
make[3]: *** [Makefile:118: /openwrt/build_dir/target-mips_24kc_musl/netifyd-2021-05-19-v3.07/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
