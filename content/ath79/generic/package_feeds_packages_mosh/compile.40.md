---
title: "compile.40"
date: 2021-06-22 10:45:15.525360
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
make package/feeds/packages/mosh/compile -j$(nproc) || make package/feeds/packages/mosh/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/020-std.patch using plaintext: 
patching file src/network/network.cc
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/mips
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether make supports nested variables... (cached) yes
checking for mips-openwrt-linux-cc... ccache_cc
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
checking whether we are using the GNU C++ compiler... yes
checking whether ccache_cxx accepts -g... yes
checking dependency style of ccache_cxx... gcc3
checking for mips-openwrt-linux-ranlib... mips-openwrt-linux-musl-gcc-ranlib
checking for protoc... /openwrt/staging_dir/hostpkg/bin/protoc
checking for mips-openwrt-linux-ar... mips-openwrt-linux-musl-gcc-ar
checking the archiver (mips-openwrt-linux-musl-gcc-ar) interface... ar
checking whether C++ compiler accepts -fno-default-inline... yes
checking whether C++ compiler accepts -pipe... yes
checking for library containing compress... -lz
checking for library containing socket... none required
checking for library containing inet_addr... none required
checking for library containing clock_gettime... none required
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
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking langinfo.h usability... yes
checking langinfo.h presence... yes
checking for langinfo.h... yes
checking limits.h usability... yes
checking limits.h presence... yes
checking for limits.h... yes
checking locale.h usability... yes
checking locale.h presence... yes
checking for locale.h... yes
checking netdb.h usability... yes
checking netdb.h presence... yes
checking for netdb.h... yes
checking netinet/in.h usability... yes
checking netinet/in.h presence... yes
checking for netinet/in.h... yes
checking stddef.h usability... yes
checking stddef.h presence... yes
checking for stddef.h... yes
checking for stdint.h... (cached) yes
checking for inttypes.h... (cached) yes
checking for stdlib.h... (cached) yes
checking for string.h... (cached) yes
checking sys/ioctl.h usability... yes
checking sys/ioctl.h presence... yes
checking for sys/ioctl.h... yes
checking sys/resource.h usability... yes
checking sys/resource.h presence... yes
checking for sys/resource.h... yes
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking for sys/stat.h... (cached) yes
checking sys/time.h usability... yes
checking sys/time.h presence... yes
checking for sys/time.h... yes
checking termios.h usability... yes
checking termios.h presence... yes
checking for termios.h... yes
checking for unistd.h... (cached) yes
checking wchar.h usability... yes
checking wchar.h presence... yes
checking for wchar.h... yes
checking wctype.h usability... yes
checking wctype.h presence... yes
checking for wctype.h... yes
checking pty.h usability... yes
checking pty.h presence... yes
checking for pty.h... yes
checking util.h usability... no
checking util.h presence... no
checking for util.h... no
checking libutil.h usability... no
checking libutil.h presence... no
checking for libutil.h... no
checking paths.h usability... yes
checking paths.h presence... yes
checking for paths.h... yes
checking endian.h usability... yes
checking endian.h presence... yes
checking for endian.h... yes
checking sys/endian.h usability... no
checking sys/endian.h presence... no
checking for sys/endian.h... no
checking utmpx.h usability... yes
checking utmpx.h presence... yes
checking for utmpx.h... yes
checking termio.h usability... no
checking termio.h presence... no
checking for termio.h... no
checking sys/uio.h usability... yes
checking sys/uio.h presence... yes
checking for sys/uio.h... yes
checking how to run the C++ preprocessor... ccache_cxx -E
checking memory usability... yes
checking memory presence... yes
checking for memory... yes
checking tr1/memory usability... yes
checking tr1/memory presence... yes
checking for tr1/memory... yes
checking for stdbool.h that conforms to C99... yes
checking for _Bool... yes
checking for inline... inline
checking for int64_t... yes
checking for pid_t... yes
checking for C/C++ restrict keyword... __restrict
checking for size_t... yes
checking for ssize_t... yes
checking for uint16_t... yes
checking for uint32_t... yes
checking for uint64_t... yes
checking for uint8_t... yes
checking for uintptr_t... yes
checking vfork.h usability... no
checking vfork.h presence... no
checking for vfork.h... no
checking for fork... yes
checking for vfork... yes
checking for working fork... cross
configure: WARNING: result yes guessed because of cross compilation
checking for working vfork... (cached) yes
checking whether mbrtowc and mbstate_t are properly declared... yes
checking for gettimeofday... (cached) yes
checking for setrlimit... yes
checking for iswprint... yes
checking for memchr... yes
checking for memset... yes
checking for nl_langinfo... yes
checking for posix_memalign... yes
checking for setenv... yes
checking for setlocale... (cached) yes
checking for sigaction... yes
checking for socket... yes
checking for strchr... yes
checking for strdup... yes
checking for strncasecmp... yes
checking for strtok... yes
checking for strerror... (cached) yes
checking for strtol... yes
checking for wcwidth... yes
checking for cfmakeraw... yes
checking for pselect... yes
checking for getaddrinfo... (cached) yes
checking for getnameinfo... yes
checking for pledge... no
checking pkg-config is at least version 0.9.0... yes
checking for TINFO... no
checking for TINFO... no
checking curses.h usability... yes
checking curses.h presence... yes
checking for curses.h... yes
checking for main in -ltinfo... yes
checking CommonCrypto/CommonCrypto.h usability... no
checking CommonCrypto/CommonCrypto.h presence... no
checking for CommonCrypto/CommonCrypto.h... no
checking for CRYPTO... no
checking openssl/aes.h usability... no
checking openssl/aes.h presence... no
checking for openssl/aes.h... no
configure: error: OpenSSL crypto library not found
make[3]: *** [Makefile:119: /openwrt/build_dir/target-mips_24kc_musl/mosh-1.3.2/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
