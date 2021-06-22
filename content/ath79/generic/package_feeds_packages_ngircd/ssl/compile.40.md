---
title: "compile.40"
date: 2021-06-22 10:41:19.977927
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
make package/feeds/packages/ngircd/compile -j$(nproc) || make package/feeds/packages/ngircd/compile V=s
```

#### Compile.txt

``` bash
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/mips
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking for mips-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... no
checking for ccache_cc option to accept ISO C89... none needed
checking for style of include used by make... GNU
checking dependency style of ccache_cc... gcc3
checking for ccache_cc option to accept ISO C99... none needed
checking for ccache_cc option to accept ISO Standard C... (cached) none needed
checking for mips-openwrt-linux-ar... mips-openwrt-linux-musl-gcc-ar
checking the archiver (mips-openwrt-linux-musl-gcc-ar) interface... ar
checking for gawk... (cached) gawk
checking whether ln -s works... yes
checking whether make sets $(MAKE)... (cached) yes
checking for mips-openwrt-linux-ranlib... mips-openwrt-linux-musl-gcc-ranlib
checking for an ANSI C-conforming const... yes
checking for inline... inline
checking for function prototypes... yes
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
checking for string.h... (cached) yes
checking whether ccache_cc accepts -fstack-protector... yes
checking for ANSI C header files... (cached) yes
checking for sys/wait.h that is POSIX.1 compatible... yes
checking whether time.h and sys/time.h may both be included... yes
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking netdb.h usability... yes
checking netdb.h presence... yes
checking for netdb.h... yes
checking netinet/in.h usability... yes
checking netinet/in.h presence... yes
checking for netinet/in.h... yes
checking for stdlib.h... (cached) yes
checking for string.h... (cached) yes
checking for strings.h... (cached) yes
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking sys/time.h usability... yes
checking sys/time.h presence... yes
checking for sys/time.h... yes
checking for sys/types.h... (cached) yes
checking for unistd.h... (cached) yes
checking for arpa/inet.h... yes
checking for inttypes.h... (cached) yes
checking for malloc.h... yes
checking for netinet/in_systm.h... yes
checking for netinet/ip.h... yes
checking for stdbool.h... yes
checking for stddef.h... yes
checking for stdint.h... (cached) yes
checking for varargs.h... no
checking whether socklen_t exists... yes
checking for pid_t... yes
checking for size_t... yes
checking for ssize_t... yes
checking for uid_t in sys/types.h... yes
checking for uint16_t... yes
checking for uint32_t... yes
checking for uint8_t... yes
checking for struct sockaddr_in.sin_len... no
checking for library containing memmove... none required
checking for library containing gethostbyname... none required
checking for library containing bind... none required
checking vfork.h usability... no
checking vfork.h presence... no
checking for vfork.h... no
checking for fork... yes
checking for vfork... yes
checking for working fork... cross
configure: WARNING: result yes guessed because of cross compilation
checking for working vfork... (cached) yes
checking for strftime... (cached) yes
checking for alarm... yes
checking for dup2... yes
checking for endpwent... yes
checking for gethostbyaddr... yes
checking for gethostbyname... yes
checking for gethostname... yes
checking for gettimeofday... (cached) yes
checking for inet_ntoa... yes
checking for memmove... yes
checking for memset... yes
checking for setsid... yes
checking for socket... yes
checking for strcasecmp... yes
checking for strchr... yes
checking for strcspn... yes
checking for strerror... (cached) yes
checking for strncasecmp... yes
checking for strrchr... yes
checking for strspn... yes
checking for strstr... yes
checking for arc4random... no
checking for arc4random_stir... no
checking for gai_strerror... yes
checking for getnameinfo... yes
checking for inet_aton... yes
checking for setgroups... yes
checking for sigaction... yes
checking for sigprocmask... yes
checking for snprintf... yes
checking for strdup... yes
checking for strlcat... yes
checking for strlcpy... yes
checking for strndup... yes
checking for strsignal... yes
checking for strtok_r... yes
checking for unsetenv... yes
checking for vsnprintf... (cached) yes
checking for waitpid... yes
checking for getaddrinfo... (cached) yes
checking whether getaddrinfo() works... no
checking for library containing syslog... none required
checking syslog.h usability... yes
checking syslog.h presence... yes
checking for syslog.h... yes
checking for deflate in -lz... yes
checking for deflate... yes
checking zlib.h usability... yes
checking zlib.h presence... yes
checking for zlib.h... yes
checking for select... yes
checking for poll... yes
checking poll.h usability... yes
checking poll.h presence... yes
checking for poll.h... yes
checking sys/devpoll.h usability... no
checking sys/devpoll.h presence... no
checking for sys/devpoll.h... no
checking for epoll_create... yes
checking for kqueue... no
checking pkg-config is at least version 0.9.0... yes
checking for OPENSSL... no
checking for BIO_s_mem in -lcrypto... no
checking for SSL_new in -lssl... no
checking for SSL_new... no
configure: error: Can't enable openssl
make[3]: *** [Makefile:111: /openwrt/build_dir/target-mips_24kc_musl/ngircd-ssl/ngircd-26.1/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
