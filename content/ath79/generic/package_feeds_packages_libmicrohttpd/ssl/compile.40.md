---
title: "compile.40"
date: 2021-06-22 10:51:50.619041
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
make package/feeds/packages/libmicrohttpd/compile -j$(nproc) || make package/feeds/packages/libmicrohttpd/compile V=s
```

#### Compile.txt

``` bash
configure: loading site script /openwrt/include/site/mips
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a race-free mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether z/OS special settings are required... no
checking for gawk... (cached) gawk
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking whether ln -s works... yes
checking whether make sets $(MAKE)... (cached) yes
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking for mips-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether the compiler supports GNU C... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to enable C11 features... none needed
checking whether ccache_cc understands -c and -o together... yes
checking whether make supports the include directive... yes (GNU style)
checking dependency style of ccache_cc... gcc3
checking how to run the C preprocessor... ccache_cc -E
checking for presence of stdio.h... yes
checking for presence of wchar.h... yes
checking for presence of stdlib.h... yes
checking for presence of string.h... yes
checking for presence of strings.h... yes
checking for presence of stdint.h... yes
checking for presence of fcntl.h... yes
checking for presence of sys/types.h... yes
checking for presence of time.h... yes
checking for presence of unistd.h... yes
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking whether _GNU_SOURCE is already defined... no
checking whether headers accept _GNU_SOURCE... yes
checking whether to try __BSD_VISIBLE macro... no
checking whether to try _DARWIN_C_SOURCE macro... no
checking whether to try __EXTENSIONS__ macro... no
checking whether to try _NETBSD_SOURCE macro... no
checking whether to try _BSD_SOURCE macro... no
checking whether to try _TANDEM_SOURCE macro... no
checking whether to try _ALL_SOURCE macro... no
checking whether _XOPEN_SOURCE is already defined... no
checking headers for POSIX.1-2008/SUSv4 features... available, works always
checking for useful system-specific features... no
checking for final set of defined symbols... _GNU_SOURCE _XOPEN_SOURCE=700
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for ld used by ccache_cc... mips-openwrt-linux-musl-ld
checking if the linker (mips-openwrt-linux-musl-ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... mips-openwrt-linux-musl-gcc-nm
checking the name lister (mips-openwrt-linux-musl-gcc-nm) interface... BSD nm
checking the maximum length of command line arguments... 3145728
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
checking for a working dd... /usr/bin/dd
checking how to truncate binary pipes... /usr/bin/dd bs=4096 count=1
checking for mips-openwrt-linux-mt... no
checking for mt... no
checking if : is a manifest tool... no
checking for stdio.h... yes
checking for stdlib.h... yes
checking for string.h... yes
checking for inttypes.h... yes
checking for stdint.h... yes
checking for strings.h... yes
checking for sys/stat.h... yes
checking for sys/types.h... yes
checking for unistd.h... yes
checking for fcntl.h... yes
checking for math.h... yes
checking for errno.h... yes
checking for limits.h... yes
checking for locale.h... yes
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
checking for mips-openwrt-linux-windres... no
checking for windres... no
checking whether NLS is requested... no
checking for msgfmt... /openwrt/staging_dir/hostpkg/bin/msgfmt
checking for gmsgfmt... /openwrt/staging_dir/hostpkg/bin/msgfmt
checking for xgettext... /openwrt/staging_dir/hostpkg/bin/xgettext
checking for msgmerge... /openwrt/staging_dir/hostpkg/bin/msgmerge
checking for ld... mips-openwrt-linux-musl-ld
checking if the linker (mips-openwrt-linux-musl-ld) is GNU ld... yes
checking for shared library run path origin... done
checking 32-bit host C ABI... yes
checking for ELF binary format... yes
checking for the common suffixes of directories in the library search path... lib,lib32,lib
checking for CFPreferencesCopyAppValue... no
checking for CFLocaleCopyPreferredLanguages... no
checking whether to use NLS... no
checking for stdbool.h... yes
checking for bool... yes
checking whether "true" is defined or builtin... yes
checking whether "false" is defined or builtin... yes
checking whether "true" and "false" could be used... yes
checking whether C compiler accepts -Werror=attributes... yes
checking whether -Werror=attributes actually works... yes
checking for function inline keywords supported by ccache_cc... inline __attribute__((always_inline))
checking for target host OS... Linux
checking whether ccache_cc is Clang... no
checking whether pthreads work with "-pthread" and "-lpthread"... yes
checking for joinable pthread attribute... PTHREAD_CREATE_JOINABLE
checking whether more special flags are required for pthreads... no
checking for PTHREAD_PRIO_INHERIT... yes
checking whether pthread_sigmask(3) is available... yes
checking for threading lib to use with libmicrohttpd (auto)... posix
checking for ccache_cc options needed to detect all undeclared functions... none needed
checking for pthread_np.h... no
checking whether pthread_attr_setname_np is declared... no
checking whether pthread_setname_np is declared... yes
checking for pthread_setname_np(3) in NetBSD or OSF1 form... no
checking for pthread_setname_np(3) in GNU/Linux form... yes
checking whether to enable thread names... yes
checking for sys/time.h... yes
checking for gettimeofday... (cached) yes
checking for time.h... yes
checking for nanosleep... yes
checking for unistd.h... (cached) yes
checking for usleep... yes
checking for string.h... (cached) yes
checking for sys/types.h... (cached) yes
checking for sys/socket.h... yes
checking for netinet/in.h... yes
checking for time.h... (cached) yes
checking for sys/select.h... yes
checking for netinet/tcp.h... yes
checking whether shutdown of listen socket trigger select()... yes
checking for library containing sendmsg... none required
checking for writev... yes
checking whether the linker accepts -fno-strict-aliasing... yes
checking whether C compiler accepts -fno-strict-aliasing... yes
checking whether byte ordering is bigendian... (cached) yes
checking for variable-length arrays... yes
checking whether __func__ magic-macro is available... yes
checking whether __builtin_bswap32() is available... yes
checking whether __builtin_bswap64() is available... yes
checking for curl... yes
checking for makeinfo... yes
checking for linux/version.h... yes
checking for Linux epoll(7) interface... yes
checking for epoll_create1()... yes
checking for sys/types.h... (cached) yes
checking for sys/time.h... (cached) yes
checking for sys/msg.h... yes
checking for time.h... (cached) yes
checking for sys/mman.h... yes
checking for sys/ioctl.h... yes
checking for sys/socket.h... (cached) yes
checking for sys/select.h... (cached) yes
checking for netdb.h... yes
checking for netinet/in.h... (cached) yes
checking for netinet/ip.h... yes
checking for netinet/tcp.h... (cached) yes
checking for arpa/inet.h... yes
checking for endian.h... yes
checking for machine/endian.h... no
checking for sys/endian.h... no
checking for sys/param.h... yes
checking for sys/machine.h... no
checking for sys/byteorder.h... no
checking for machine/param.h... no
checking for sys/isa_defs.h... no
checking for signal.h... yes
checking for inttypes.h... (cached) yes
checking for stddef.h... yes
checking for unistd.h... (cached) yes
checking for sockLib.h... no
checking for inetLib.h... no
checking for net/if.h... yes
checking for search.h... yes
checking for tsearch... yes
checking for twalk... yes
checking whether tdelete works... guessing yes
checking for dlfcn.h... (cached) yes
checking for zlib.h... yes
checking for function random... yes
checking for struct sockaddr_in.sin_len... no
checking for struct sockaddr_in6.sin6_len... no
checking for struct sockaddr_storage.ss_len... no
checking for function getsockname... yes
checking whether getsockname() is usable... assuming yes
checking for sys/eventfd.h... yes
checking whether eventfd(2) is usable... yes
checking for accept4... yes
checking for gmtime_r... yes
checking for memmem... yes
checking for snprintf... yes
checking whether gmtime_s is declared... no
checking whether SOCK_NONBLOCK is declared... yes
checking whether clock_gettime is declared... yes
checking for library containing clock_gettime... none required
checking for clock_get_time... no
checking for gethrtime... no
checking for IPv6... yes
checking for function sysconf... yes
checking whether the linker accepts -fvisibility=hidden... yes
checking whether C compiler accepts -fvisibility=hidden... yes
checking for suitable libmagic... no
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking for _LARGEFILE_SOURCE value needed for large files... no
checking for lseek64... yes
checking for pread64... yes
checking for pread... yes
checking for Linux-style sendfile(2)... yes
checking for sendfile64... yes
checking whether to generate error messages... yes
checking whether to enable postprocessor... yes
checking for zzuf... no
checking for socat... no
checking pkg-config is at least version 0.9.0... yes
checking how to find GnuTLS library... automatically, forced
checking whether to add pkg-config special search directories... no
checking for gnutls... no
checking for gnutls/gnutls.h... no
checking for libgcrypt-config... /openwrt/staging_dir/target-mips_24kc_musl/host/bin/libgcrypt-config
checking for LIBGCRYPT - version >= 1.2.2... yes (1.9.3)
checking for gcrypt.h... yes
checking for gnutls/gnutls.h... no
configure: error: can't find usable libgnutls
make[3]: *** [Makefile:96: /openwrt/build_dir/target-mips_24kc_musl/libmicrohttpd-ssl/libmicrohttpd-0.9.73/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
