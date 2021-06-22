---
title: "compile.40"
date: 2021-06-22 10:44:06.289332
hidden: false
draft: false
weight: -40
---

build number: `40`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/base/lldpd/compile -j$(nproc) || make package/feeds/base/lldpd/compile V=s
```

#### Compile.txt

``` bash
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force -I m4
autoreconf: configure.ac: tracing
autoreconf: configure.ac: adding subdirectory libevent to autoreconf
autoreconf: Entering directory `libevent'
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
configure.ac:118: error: Libtool version 2.4.2 or higher is required
m4/libtool.m4:48: LT_PREREQ is expanded from...
configure.ac:118: the top level
autom4te: /openwrt/staging_dir/host/bin/m4 failed with exit status: 63
aclocal.real: error: echo failed with exit status: 63
autoreconf: /openwrt/staging_dir/host/bin/aclocal failed with exit status: 63
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/mips
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether UID '1000' is supported by ustar format... yes
checking whether GID '1000' is supported by ustar format... yes
checking how to create a ustar tar archive... gnutar
checking whether to enable maintainer-specific portions of Makefiles... no
checking whether make supports nested variables... (cached) yes
checking whether make supports the include directive... yes (GNU style)
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
checking for mips-openwrt-linux-ar... mips-openwrt-linux-musl-gcc-ar
checking the archiver (mips-openwrt-linux-musl-gcc-ar) interface... ar
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache_cc... mips-openwrt-linux-musl-ld
checking if the linker (mips-openwrt-linux-musl-ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... mips-openwrt-linux-musl-gcc-nm
checking the name lister (mips-openwrt-linux-musl-gcc-nm) interface... BSD nm
checking whether ln -s works... yes
checking the maximum length of command line arguments... 3145728
checking how to convert x86_64-pc-linux-gnu file names to mips-openwrt-linux-gnu format... func_convert_file_noop
checking how to convert x86_64-pc-linux-gnu file names to toolchain format... func_convert_file_noop
checking for mips-openwrt-linux-musl-ld option to reload object files... -r
checking for mips-openwrt-linux-objdump... mips-openwrt-linux-musl-objdump
checking how to recognize dependent libraries... pass_all
checking for mips-openwrt-linux-dlltool... no
checking for dlltool... no
checking how to associate runtime and link libraries... printf %s\n
checking for mips-openwrt-linux-ar... (cached) mips-openwrt-linux-musl-gcc-ar
checking for archiver @FILE support... @
checking for mips-openwrt-linux-strip... (cached) mips-openwrt-linux-musl-strip
checking for mips-openwrt-linux-ranlib... mips-openwrt-linux-musl-gcc-ranlib
checking command to parse mips-openwrt-linux-musl-gcc-nm output from ccache_cc object... ok
checking for sysroot... no
checking for a working dd... /usr/bin/dd
checking how to truncate binary pipes... /usr/bin/dd bs=4096 count=1
checking for mips-openwrt-linux-mt... no
checking for mt... no
checking if : is a manifest tool... no
checking how to run the C preprocessor... ccache_cc -E
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
checking whether the ccache_cc linker (mips-openwrt-linux-musl-ld) supports shared libraries... yes
checking whether -lc should be explicitly linked in... no
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... yes
checking if LD -Wl,--version-script works... yes
checking for mips-openwrt-linux-gcc... (cached) ccache_cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether ccache_cc accepts -g... (cached) yes
checking for ccache_cc option to accept ISO C89... (cached) none needed
checking whether ccache_cc understands -c and -o together... (cached) yes
checking dependency style of ccache_cc... (cached) gcc3
checking for ccache_cc option to accept ISO C99... none needed
checking whether ln -s works... yes
checking for egrep... (cached) /openwrt/staging_dir/host/bin/grep -E
checking for gawk... (cached) gawk
checking CFLAGS for gcc -Wunknown-warning-option... no, unknown
checking CFLAGS for gcc -fdiagnostics-show-option... -fdiagnostics-show-option
checking CFLAGS for gcc -fdiagnostics-color=auto... -fdiagnostics-color=auto
checking CFLAGS for gcc -pipe... -pipe
checking CFLAGS for gcc -Wall... -Wall
checking CFLAGS for gcc -W... -W
checking CFLAGS for gcc -Wextra... -Wextra
checking CFLAGS for gcc -Wformat... -Wformat
checking CFLAGS for gcc -Wformat-security... -Wformat-security
checking CFLAGS for gcc -Wimplicit-fallthrough... -Wimplicit-fallthrough
checking CFLAGS for gcc -Wfatal-errors... -Wfatal-errors
checking CFLAGS for gcc -Wheader-guard... no, unknown
checking CFLAGS for gcc -Wdocumentation... no, unknown
checking CFLAGS for gcc -Winline... -Winline
checking CFLAGS for gcc -Wpointer-arith... -Wpointer-arith
checking CFLAGS for gcc -fno-omit-frame-pointer... -fno-omit-frame-pointer
checking CFLAGS for gcc -Wno-cast-align... -Wno-cast-align
checking CFLAGS for gcc -Wno-unused-parameter... -Wno-unused-parameter
checking CFLAGS for gcc -Wno-missing-field-initializers... -Wno-missing-field-initializers
checking CFLAGS for gcc -Wno-sign-compare... -Wno-sign-compare
checking whether the linker accepts the -Wl,-z,relro flag... yes
checking whether the linker accepts the -Wl,-z,now flag... yes
checking for typeof syntax and keyword spelling... typeof
checking if host OS is supported... yes (Linux)
checking CFLAGS for gcc -D_GNU_SOURCE... -D_GNU_SOURCE
checking for sys/types.h... (cached) yes
checking for netinet/in.h... yes
checking for arpa/nameser.h... yes
checking for netdb.h... yes
checking for resolv.h... yes
checking valgrind/valgrind.h usability... no
checking valgrind/valgrind.h presence... no
checking for valgrind/valgrind.h... no
checking for u_int32_t... yes
checking for uint32_t... yes
checking whether libc defines __progname... yes
checking whether compiler understands __alignof__... yes
checking for stdlib.h... (cached) yes
checking for GNU libc compatible malloc... (cached) yes
checking for stdlib.h... (cached) yes
checking for GNU libc compatible realloc... (cached) yes
checking for pid_t... yes
checking vfork.h usability... no
checking vfork.h presence... no
checking for vfork.h... no
checking for fork... yes
checking for vfork... yes
checking for working fork... cross
configure: WARNING: result yes guessed because of cross compilation
checking for working vfork... (cached) yes
checking for setproctitle... no
checking for setproctitle_init... no
checking for strlcpy... yes
checking for strnlen... yes
checking for strndup... yes
checking for strtonum... no
checking for getline... yes
checking for asprintf... yes
checking for vsyslog... yes
checking for daemon... yes
checking for setresuid... (cached) no
checking for setresgid... yes
checking for library containing res_init... none required
checking for check >= 0.9.4... no
checking for libevent >= 2.0.5... no
configure: error: *** libevent not found
make[3]: *** [Makefile:120: /openwrt/build_dir/target-mips_24kc_musl/lldpd-1.0.9/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
