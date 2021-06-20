---
title: "compile.37"
date: 2021-06-20 22:26:36.877637
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
make package/feeds/packages/neon/compile -j$(nproc) || make package/feeds/packages/neon/compile V=s
```

#### Compile.txt

``` bash
configure: loading site script /openwrt/include/site/mips
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
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
checking for inline... inline
checking for an ANSI C-conforming const... yes
checking for size_t... yes
checking for off_t... yes
checking for uname... Linux
checking whether make sets $(MAKE)... yes
checking size of int... (cached) 4
checking size of long... (cached) 4
checking size of long long... (cached) 8
checking for gcc -Wformat -Werror sanity... yes
checking errno.h usability... yes
checking errno.h presence... yes
checking for errno.h... yes
checking stdarg.h usability... yes
checking stdarg.h presence... yes
checking for stdarg.h... yes
checking for string.h... (cached) yes
checking for stdlib.h... (cached) yes
checking sys/uio.h usability... yes
checking sys/uio.h presence... yes
checking for sys/uio.h... yes
checking size of size_t... (cached) 4
checking how to print size_t... u
checking size of off_t... (cached) 8
checking how to print off_t... lld
checking size of ssize_t... (cached) 4
checking how to print ssize_t... d
checking whether byte ordering is bigendian... (cached) yes
checking whether strerror_r is declared... yes
checking for strerror_r... yes
checking whether strerror_r returns char *... no
checking for snprintf... yes
checking for vsnprintf... (cached) yes
checking for sys/time.h... yes
checking for limits.h... yes
checking for sys/select.h... yes
checking for arpa/inet.h... yes
checking for libintl.h... yes
checking for signal.h... yes
checking for sys/socket.h... yes
checking for netinet/in.h... yes
checking for netinet/tcp.h... yes
checking for netdb.h... yes
checking for sys/poll.h... yes
checking for sys/limits.h... no
checking for fcntl.h... yes
checking for iconv.h... yes
checking for timezone global... yes
configure: LFS support unnecessary, off_t is not 32-bit
checking for strtoll... yes
checking for strcasecmp... yes
checking for signal... yes
checking for setvbuf... yes
checking for setsockopt... yes
checking for stpcpy... yes
checking for poll... yes
checking for fcntl... yes
checking for getsockopt... yes
checking whether stpcpy is declared... yes
checking for library containing socket... none needed
checking for library containing getaddrinfo... none needed
checking for gai_strerror... yes
checking for getnameinfo... yes
checking for inet_ntop... yes
checking for inet_pton... yes
configure: IPv6 support is enabled
checking for working AI_ADDRCONFIG... no
checking for socklen_t... yes
checking for struct tm.tm_gmtoff... yes
checking for struct tm.__tm_gmtoff... yes
checking zlib.h usability... yes
checking zlib.h presence... yes
checking for zlib.h... yes
checking for inflate in -lz... yes
configure: zlib support enabled, using -lz
checking whether to enable ACL support in neon... yes
checking for pkg-config... /openwrt/staging_dir/host/bin/pkg-config
checking for openssl pkg-config data... no
checking for library containing RSA_new... not found
configure: error: could not find library containing RSA_new
make[3]: *** [Makefile:82: /openwrt/build_dir/target-mips_24kc_musl/neon-0.31.2/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
