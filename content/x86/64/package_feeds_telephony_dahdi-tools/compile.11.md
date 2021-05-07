---
title: "compile.11"
date: 2021-05-07 23:28:45.863659
hidden: false
draft: false
weight: -11
---

build number: `11`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/telephony/dahdi-tools/compile -j$(nproc) || make package/feeds/telephony/dahdi-tools/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/020-fix-undefined-reference-to-get_ver.patch using plaintext: 
patching file xpp/echo_loader.c
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-x86_64_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal -I m4 -I . --force -I m4
autoreconf: configure.ac: tracing
autoreconf: configure.ac: creating directory auxdir
autoreconf: running: /openwrt/staging_dir/host/bin/libtoolize --install --force
OpenWrt-libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, `auxdir'.
OpenWrt-libtoolize: linking file `auxdir/config.guess'
OpenWrt-libtoolize: linking file `auxdir/config.sub'
OpenWrt-libtoolize: linking file `auxdir/install-sh'
OpenWrt-libtoolize: linking file `auxdir/ltmain.sh'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `m4'.
OpenWrt-libtoolize: linking file `m4/libtool.m4'
OpenWrt-libtoolize: linking file `m4/ltoptions.m4'
OpenWrt-libtoolize: linking file `m4/ltsugar.m4'
OpenWrt-libtoolize: linking file `m4/ltversion.m4'
OpenWrt-libtoolize: linking file `m4/lt~obsolete.m4'
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-x86_64_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-x86_64_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
configure.ac:69: installing 'auxdir/compile'
configure.ac:15: installing 'auxdir/missing'
Makefile.am: installing 'auxdir/depcomp'
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
checking for x86_64-openwrt-linux-ld... x86_64-openwrt-linux-musl-ld
checking whether we are using the GNU C++ compiler... yes
checking whether ccache_cxx accepts -g... yes
checking dependency style of ccache_cxx... gcc3
checking for x86_64-openwrt-linux-gcc... (cached) ccache_cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether ccache_cc accepts -g... (cached) yes
checking for ccache_cc option to accept ISO C89... (cached) none needed
checking whether ccache_cc understands -c and -o together... (cached) yes
checking dependency style of ccache_cc... (cached) gcc3
checking how to run the C preprocessor... ccache_cc -E
checking whether ln -s works... yes
checking whether make sets $(MAKE)... (cached) yes
checking for gawk... (cached) gawk
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-openwrt-linux-gnu
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache_cc... x86_64-openwrt-linux-musl-ld
checking if the linker (x86_64-openwrt-linux-musl-ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... x86_64-openwrt-linux-musl-gcc-nm
checking the name lister (x86_64-openwrt-linux-musl-gcc-nm) interface... BSD nm
checking the maximum length of command line arguments... 1572864
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
checking how to run the C++ preprocessor... ccache_cxx -E
checking for ld used by ccache_cxx... x86_64-openwrt-linux-musl-ld -m elf_x86_64
checking if the linker (x86_64-openwrt-linux-musl-ld -m elf_x86_64) is GNU ld... yes
checking whether the ccache_cxx linker (x86_64-openwrt-linux-musl-ld -m elf_x86_64) supports shared libraries... yes
checking for ccache_cxx option to produce PIC... -fPIC -DPIC
checking if ccache_cxx PIC flag -fPIC -DPIC works... yes
checking if ccache_cxx static flag -static works... yes
checking if ccache_cxx supports -c -o file.o... yes
checking if ccache_cxx supports -c -o file.o... (cached) yes
checking whether the ccache_cxx linker (x86_64-openwrt-linux-musl-ld -m elf_x86_64) supports shared libraries... yes
checking dynamic linker characteristics... (cached) GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking for GNU make... make
/openwrt/staging_dir/host/bin/sed: can't read conftest.c: No such file or directory
checking for grep... (cached) /openwrt/staging_dir/host/bin/grep
checking for sh... /bin/bash
checking for ln... /usr/bin/ln
checking for wget... /openwrt/staging_dir/host/bin/wget
checking for perl... /openwrt/staging_dir/host/bin/perl
checking for perl libdir... 
checking for -Wdeclaration-after-statement support... yes
checking sys/soundcard.h usability... yes
checking sys/soundcard.h presence... yes
checking for sys/soundcard.h... yes
checking linux/soundcard.h usability... yes
checking linux/soundcard.h presence... yes
checking for linux/soundcard.h... yes
checking arpa/inet.h usability... yes
checking arpa/inet.h presence... yes
checking for arpa/inet.h... yes
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking limits.h usability... yes
checking limits.h presence... yes
checking for limits.h... yes
checking netinet/in.h usability... yes
checking netinet/in.h presence... yes
checking for netinet/in.h... yes
checking for stdint.h... (cached) yes
checking for stdlib.h... (cached) yes
checking for string.h... (cached) yes
checking sys/ioctl.h usability... yes
checking sys/ioctl.h presence... yes
checking for sys/ioctl.h... yes
checking sys/param.h usability... yes
checking sys/param.h presence... yes
checking for sys/param.h... yes
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking sys/time.h usability... yes
checking sys/time.h presence... yes
checking for sys/time.h... yes
checking syslog.h usability... yes
checking syslog.h presence... yes
checking for syslog.h... yes
checking for unistd.h... (cached) yes
checking for inline... inline
checking for size_t... yes
checking for ssize_t... yes
checking for uint16_t... yes
checking for uint32_t... yes
checking for uint8_t... yes
checking for cos in -lm... yes
checking for pthread_create in -lpthread... yes
checking for DAHDI_CODE in dahdi/user.h... no
checking for DAHDI_CONFIG_NTTE in dahdi/user.h... no
checking whether DAHDI_TXMIRROR is declared... no
checking for semtimedop... yes
checking for alarm... yes
checking for bzero... (cached) yes
checking for gettimeofday... (cached) yes
checking for memset... yes
checking for pow... yes
checking for regcomp... yes
checking for select... yes
checking for socket... yes
checking for strcasecmp... yes
checking for strchr... yes
checking for strdup... yes
checking for strerror... (cached) yes
checking for strrchr... yes
checking for strstr... yes
checking for strtol... yes
checking for strtoul... yes
checking for error_at_line... no
checking for stdlib.h... (cached) yes
checking for GNU libc compatible malloc... (cached) yes
checking pkg-config is at least version 0.9.0... yes
checking for GENERIC_HDLC_VERSION version 4 in linux/hdlc.h... no
checking for GENERIC_HDLC_VERSION version 4 in linux/hdlc/ioctl.h... yes
configure: ***
configure: *** Building this package requires DAHDI support. *** 
configure: *** Please install the dahdi-linux package. ***
configure: ***
make[3]: *** [Makefile:99: /openwrt/build_dir/target-x86_64_musl/dahdi-tools-3.1.0/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
