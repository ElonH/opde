---
title: "compile.37"
date: 2021-06-20 22:26:36.882493
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
make package/feeds/packages/nsd/compile -j$(nproc) || make package/feeds/packages/nsd/compile V=s
```

#### Compile.txt

``` bash
configure: WARNING: unrecognized options: --disable-nls, --with-ipv6
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
checking for gawk... gawk
checking for mips-openwrt-linux-gcc... (cached) ccache_cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether ccache_cc accepts -g... (cached) yes
checking for ccache_cc option to accept ISO C89... (cached) none needed
checking whether ln -s works... yes
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking for flex... flex
checking lex output file root... lex.yy
checking lex library... none needed
checking whether yytext is a pointer... no
checking for bison... bison -y
checking if lex defines yy_current_buffer... no
checking for an ANSI C-conforming const... yes
checking for inline... inline
checking for uid_t in sys/types.h... yes
checking for pid_t... yes
checking for size_t... yes
checking for off_t... yes
checking whether the C compiler (ccache_cc) accepts the "format" attribute... yes
checking whether the C compiler (ccache_cc) accepts the "unused" attribute... yes
checking whether the C compiler (ccache_cc) accepts the "noreturn" attribute... yes
checking if memcmp compares unsigned... cross-compile no
checking whether ctime_r works with two arguments... yes
checking for ANSI C header files... (cached) yes
checking for sys/wait.h that is POSIX.1 compatible... yes
checking time.h usability... yes
checking time.h presence... yes
checking for time.h... yes
checking arpa/inet.h usability... yes
checking arpa/inet.h presence... yes
checking for arpa/inet.h... yes
checking signal.h usability... yes
checking signal.h presence... yes
checking for signal.h... yes
checking for string.h... (cached) yes
checking for strings.h... (cached) yes
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking limits.h usability... yes
checking limits.h presence... yes
checking for limits.h... yes
checking netinet/in.h usability... yes
checking netinet/in.h presence... yes
checking for netinet/in.h... yes
checking netinet/tcp.h usability... yes
checking netinet/tcp.h presence... yes
checking for netinet/tcp.h... yes
checking stddef.h usability... yes
checking stddef.h presence... yes
checking for stddef.h... yes
checking sys/param.h usability... yes
checking sys/param.h presence... yes
checking for sys/param.h... yes
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking sys/un.h usability... yes
checking sys/un.h presence... yes
checking for sys/un.h... yes
checking syslog.h usability... yes
checking syslog.h presence... yes
checking for syslog.h... yes
checking for unistd.h... (cached) yes
checking sys/select.h usability... yes
checking sys/select.h presence... yes
checking for sys/select.h... yes
checking stdarg.h usability... yes
checking stdarg.h presence... yes
checking for stdarg.h... yes
checking for stdint.h... (cached) yes
checking netdb.h usability... yes
checking netdb.h presence... yes
checking for netdb.h... yes
checking sys/bitypes.h usability... no
checking sys/bitypes.h presence... no
checking for sys/bitypes.h... no
checking tcpd.h usability... no
checking tcpd.h presence... no
checking for tcpd.h... no
checking glob.h usability... yes
checking glob.h presence... yes
checking for glob.h... yes
checking grp.h usability... yes
checking grp.h presence... yes
checking for grp.h... yes
checking endian.h usability... yes
checking endian.h presence... yes
checking for endian.h... yes
checking for double definition of struct va_list... (cached) no
checking whether strptime needs defines... (cached) no
checking for library containing inet_pton... none required
checking for library containing socket... none required
checking whether strptime works... maybe
checking if nonblocking sockets work... crosscompile(yes)
checking whether mkdir has one arg... no
checking for int8_t... yes
checking for int16_t... yes
checking for int32_t... yes
checking for int64_t... yes
checking for uint8_t... yes
checking for uint16_t... yes
checking for uint32_t... yes
checking for uint64_t... yes
checking for socklen_t... yes
checking for sig_atomic_t... yes
checking for ssize_t... yes
checking for suseconds_t... (cached) yes
checking for in_addr_t... yes
checking for struct sockaddr_storage.ss_family... yes
checking for struct stat.st_mtimensec... no
checking for struct stat.st_mtim.tv_nsec... yes
checking for struct sockaddr_un.sun_len... no
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
checking for stdlib.h... (cached) yes
checking for GNU libc compatible malloc... (cached) yes
checking return type of signal handlers... void
checking for _LARGEFILE_SOURCE value needed for large files... no
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking size of void*... 4
checking size of off_t... (cached) 8
checking for arc4random... no
checking for arc4random_uniform... no
checking for library containing setusercontext... no
checking for tzset... yes
checking for alarm... yes
checking for chroot... yes
checking for dup2... yes
checking for endpwent... yes
checking for gethostname... yes
checking for memset... yes
checking for memcpy... yes
checking for pwrite... yes
checking for socket... yes
checking for strcasecmp... yes
checking for strchr... yes
checking for strdup... yes
checking for strerror... (cached) yes
checking for strncasecmp... yes
checking for strtol... yes
checking for writev... yes
checking for getaddrinfo... (cached) yes
checking for getnameinfo... yes
checking for freeaddrinfo... yes
checking for gai_strerror... yes
checking for sigaction... yes
checking for sigprocmask... yes
checking for strptime... yes
checking for strftime... (cached) yes
checking for localtime_r... yes
checking for setusercontext... no
checking for glob... yes
checking for initgroups... yes
checking for setresuid... (cached) no
checking for setreuid... yes
checking for setresgid... yes
checking for setregid... yes
checking for getpwnam... yes
checking for mmap... yes
checking for ppoll... yes
checking for clock_gettime... yes
checking for accept4... yes
checking for struct mmsghdr... yes
checking for recvmmsg... yes
checking for sendmmsg... yes
checking for basename... yes
checking for inet_aton... yes
checking for inet_pton... yes
checking for inet_ntop... yes
checking for snprintf... yes
checking for strlcat... yes
checking for strlcpy... yes
checking for strptime... (cached) yes
checking for b64_pton... no
checking for b64_ntop... no
checking for pselect... yes
checking for memmove... yes
checking for reallocarray... no
checking for pselect prototype in sys/select.h... yes
checking for ctime_r prototype in time.h... yes
checking for struct timespec... yes
checking for SSL... configure: error: Cannot find the SSL libraries in /openwrt/staging_dir/target-mips_24kc_musl/usr
make[3]: *** [Makefile:134: /openwrt/build_dir/target-mips_24kc_musl/nsd-ssl/nsd-4.2.4/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
