---
title: "compile.40"
date: 2021-06-22 10:45:15.544364
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
make package/feeds/packages/ldns/compile -j$(nproc) || make package/feeds/packages/ldns/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-compile-for-darwin.patch using plaintext: 
patching file configure.ac

Applying ./patches/010-openssl-deprecated.patch using plaintext: 
patching file dnssec_verify.c
patching file drill/drill.c
patching file keys.c

Applying ./patches/020-openssl-dsa.patch using plaintext: 
patching file dnssec.c
patching file examples/ldns-dane.c
patching file examples/ldns-keygen.c
patching file examples/ldns-signzone.c
patching file examples/ldns-verify-zone.c
patching file host2str.c
patching file keys.c
patching file ldns/keys.h
patching file rr_functions.c

Applying ./patches/030-signzone.patch using plaintext: 
patching file examples/ldns-signzone.c
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force 
autoreconf: configure.ac: tracing
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
OpenWrt-libtoolize: Consider adding `-I m4' to ACLOCAL_AMFLAGS in Makefile.am.
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: configure.ac: not using Automake
autoreconf: Leaving directory `.'
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/mips
checking for mips-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
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
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for mips-openwrt-linux-ranlib... mips-openwrt-linux-musl-gcc-ranlib
checking for gawk... gawk
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
checking for mips-openwrt-linux-gcc... (cached) ccache_cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether ccache_cc accepts -g... (cached) yes
checking for ccache_cc option to accept ISO C89... (cached) none needed
checking ccache_cc dependency flag... -MM
checking whether make sets $(MAKE)... yes
checking whether ccache_cc supports -std=c99... yes
checking whether ccache_cc supports -xc99... no
checking for an ANSI C-conforming const... yes
checking whether ccache_cc supports -Wall... yes
checking whether ccache_cc supports -W... yes
checking whether ccache_cc supports -Wwrite-strings... yes
checking whether ccache_cc supports -Wstrict-prototypes... yes
checking whether ccache_cc supports -Wunused-function... yes
checking whether ccache_cc supports -Wmissing-prototypes... no
checking for getopt.h... yes
checking for time.h... yes
checking for winsock2.h... no
checking for ws2tcpip.h... no
checking whether ccache_cc supports -Werror... yes
checking whether ccache_cc supports -Wall... (cached) yes
checking whether ccache_cc supports -std=c99... (cached) yes
checking whether ccache_cc supports -xc99... (cached) no
checking for getopt.h... (cached) yes
checking for time.h... (cached) yes
checking whether we need -std=c99 -D__EXTENSIONS__ -D_BSD_SOURCE -D_DEFAULT_SOURCE -D_POSIX_C_SOURCE=200112 -D_XOPEN_SOURCE=600 -D_XOPEN_SOURCE_EXTENDED=1 -D_ALL_SOURCE as a flag for ccache_cc... failed
checking whether we need -std=c99 -D__EXTENSIONS__ -D_BSD_SOURCE -D_DEFAULT_SOURCE -D_POSIX_C_SOURCE=200112 -D_XOPEN_SOURCE=600 -D_ALL_SOURCE as a flag for ccache_cc... failed
checking whether we need -std=c99 as a flag for ccache_cc... failed
checking whether we need -D_BSD_SOURCE -D_DEFAULT_SOURCE as a flag for ccache_cc... failed
checking whether we need -D_GNU_SOURCE as a flag for ccache_cc... failed
checking whether we need -D_GNU_SOURCE -D_FRSRESGID as a flag for ccache_cc... failed
checking whether we need -D_POSIX_C_SOURCE=200112 as a flag for ccache_cc... failed
checking whether we need -D__EXTENSIONS__ as a flag for ccache_cc... failed
checking for inline... inline
checking for int8_t... yes
checking for int16_t... yes
checking for int32_t... yes
checking for int64_t... yes
checking for uint8_t... yes
checking for uint16_t... yes
checking for uint32_t... yes
checking for uint64_t... yes
checking for doxygen... no
checking for library containing socket... none required
checking for library containing inet_pton... none required
checking for poll(2)... yes
checking for mips-openwrt-linux-ar... /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-ar
checking for SSL... configure: error: Cannot find the SSL libraries in /openwrt/staging_dir/target-mips_24kc_musl/usr
make[3]: *** [Makefile:135: /openwrt/build_dir/target-mips_24kc_musl/ldns-1.7.1/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
