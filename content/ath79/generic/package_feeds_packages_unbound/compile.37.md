---
title: "compile.37"
date: 2021-06-20 22:39:07.397699
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
make package/feeds/packages/unbound/compile -j$(nproc) || make package/feeds/packages/unbound/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-configure_uname.patch using plaintext: 
patching file configure.ac

Applying ./patches/100-example-conf-in.patch using plaintext: 
patching file doc/example.conf.in
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
OpenWrt-libtoolize: Remember to add `LT_INIT' to configure.ac.
OpenWrt-libtoolize: Consider adding `AC_CONFIG_MACRO_DIR([m4])' to configure.ac and
OpenWrt-libtoolize: rerunning libtoolize, to keep the correct libtool macros in-tree.
OpenWrt-libtoolize: Consider adding `-I m4' to ACLOCAL_AMFLAGS in Makefile.am.
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: configure.ac: not using Automake
autoreconf: Leaving directory `.'
configure: WARNING: unrecognized options: --disable-nls, --with-user
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
checking for an ANSI C-conforming const... yes
checking for mips-openwrt-linux-gcc... (cached) ccache_cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether ccache_cc accepts -g... (cached) yes
checking for ccache_cc option to accept ISO C89... (cached) none needed
checking ccache_cc dependency flag... -MM
checking whether ccache_cc supports -Werror... yes
checking whether ccache_cc supports -Wall... yes
checking whether ccache_cc supports -std=c99... yes
checking whether ccache_cc supports -xc99... no
checking for getopt.h... yes
checking for time.h... yes
checking whether we need -std=c99 -D__EXTENSIONS__ -D_BSD_SOURCE -D_DEFAULT_SOURCE -D_POSIX_C_SOURCE=200112 -D_XOPEN_SOURCE=600 -D_XOPEN_SOURCE_EXTENDED=1 -D_ALL_SOURCE as a flag for ccache_cc... no
checking whether we need -std=c99 -D__EXTENSIONS__ -D_BSD_SOURCE -D_DEFAULT_SOURCE -D_POSIX_C_SOURCE=200112 -D_XOPEN_SOURCE=600 -D_ALL_SOURCE as a flag for ccache_cc... no
checking whether we need -std=c99 as a flag for ccache_cc... no
checking whether we need -D_BSD_SOURCE -D_DEFAULT_SOURCE as a flag for ccache_cc... no
checking whether we need -D_GNU_SOURCE as a flag for ccache_cc... no
checking whether we need -D_GNU_SOURCE -D_FRSRESGID as a flag for ccache_cc... yes
checking whether we need -D_POSIX_C_SOURCE=200112 as a flag for ccache_cc... no
checking whether we need -D__EXTENSIONS__ as a flag for ccache_cc... no
checking for inline... inline
checking whether the C compiler (ccache_cc) accepts the "format" attribute... yes
checking whether the C compiler (ccache_cc) accepts the "unused" attribute... yes
checking whether the C compiler (ccache_cc) accepts the "weak" attribute... yes
checking whether the C compiler (ccache_cc) accepts the "noreturn" attribute... yes
checking for flex... flex
checking lex output file root... lex.yy
checking lex library... none needed
checking whether yytext is a pointer... no
checking for yylex_destroy... yes
checking for lex %option... yes
checking for bison... bison -y
checking for doxygen... no
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking for mips-openwrt-linux-ar... /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-ar
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
checking for mips-openwrt-linux-ar... /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-ar
checking for archiver @FILE support... @
checking for mips-openwrt-linux-strip... (cached) mips-openwrt-linux-musl-strip
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
checking pkg-config is at least version 0.9.0... yes
checking for stdarg.h... yes
checking for stdbool.h... yes
checking for netinet/in.h... yes
checking for netinet/tcp.h... yes
checking for sys/param.h... yes
checking for sys/select.h... yes
checking for sys/socket.h... yes
checking for sys/un.h... yes
checking for sys/uio.h... yes
checking for sys/resource.h... yes
checking for arpa/inet.h... yes
checking for syslog.h... yes
checking for netdb.h... yes
checking for sys/wait.h... yes
checking for pwd.h... yes
checking for glob.h... yes
checking for grp.h... yes
checking for login_cap.h... no
checking for winsock2.h... no
checking for ws2tcpip.h... no
checking for endian.h... yes
checking for sys/endian.h... no
checking for libkern/OSByteOrder.h... no
checking for sys/ipc.h... yes
checking for sys/shm.h... yes
checking for ifaddrs.h... yes
checking for net/if.h... yes
checking TargetConditionals.h usability... no
checking TargetConditionals.h presence... no
checking for TargetConditionals.h... no
checking for int8_t... yes
checking for int16_t... yes
checking for int32_t... yes
checking for int64_t... yes
checking for uint8_t... yes
checking for uint16_t... yes
checking for uint32_t... yes
checking for uint64_t... yes
checking for size_t... yes
checking for ssize_t... yes
checking for uid_t in sys/types.h... yes
checking for pid_t... yes
checking for off_t... yes
checking for u_char... yes
checking for rlim_t... yes
checking for socklen_t... yes
checking for in_addr_t... yes
checking for in_port_t... yes
checking if memcmp compares unsigned... cross-compile no
checking size of time_t... 4
checking size of size_t... (cached) 4
checking for library containing inet_pton... none required
checking for library containing socket... none required
checking for unistd.h... (cached) yes
checking for working chown... no
checking vfork.h usability... no
checking vfork.h presence... no
checking for vfork.h... no
checking for fork... yes
checking for vfork... yes
checking for working fork... cross
configure: WARNING: result yes guessed because of cross compilation
checking for working vfork... (cached) yes
checking for _LARGEFILE_SOURCE value needed for large files... no
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking whether we need -D_LARGEFILE_SOURCE=1 as a flag for ccache_cc... no
checking if nonblocking sockets work... crosscompile(yes)
checking whether mkdir has one arg... no
checking for strptime... yes
checking whether strptime works... maybe
checking for GNU libc compatible malloc... no (crosscompile)
checking if compiler needs -Werror to reject unknown flags... no
checking for the pthreads library -lpthreads... no
checking whether pthreads work without any flags... yes
checking for joinable pthread attribute... PTHREAD_CREATE_JOINABLE
checking if more special flags are required for pthreads... no
checking for PTHREAD_PRIO_INHERIT... yes
checking for pthread_spinlock_t... yes
checking for pthread_rwlock_t... yes
checking for SSL... configure: error: Cannot find the SSL libraries in /openwrt/staging_dir/target-mips_24kc_musl/usr
make[3]: *** [Makefile:268: /openwrt/build_dir/target-mips_24kc_musl/unbound-1.13.1/.configured_5657cc7649455a42510018615ccd3d8b] Error 1
```
