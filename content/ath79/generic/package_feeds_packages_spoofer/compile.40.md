---
title: "compile.40"
date: 2021-06-22 10:45:15.515243
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
make package/feeds/packages/spoofer/compile -j$(nproc) || make package/feeds/packages/spoofer/compile V=s
```

#### Compile.txt

``` bash
configure: WARNING: unrecognized options: --disable-nls, --enable-prober
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
checking whether the C++ compiler works... yes
checking for C++ compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C++ compiler... yes
checking whether ccache_cxx accepts -g... yes
checking for style of include used by make... GNU
checking dependency style of ccache_cxx... gcc3
checking whether ccache_cxx supports C++14 features by default... yes
checking for mips-openwrt-linux-gcc... ccache_cxx
checking whether we are using the GNU C compiler... yes
checking whether ccache_cxx accepts -g... yes
checking for ccache_cxx option to accept ISO C89... unsupported
checking whether ccache_cxx understands -c and -o together... yes
checking dependency style of ccache_cxx... gcc3
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking how to run the C preprocessor... ccache_cxx -E
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking whether ccache_cxx is Clang... no
checking whether pthreads work with -pthread... yes
checking for joinable pthread attribute... PTHREAD_CREATE_JOINABLE
checking whether more special flags are required for pthreads... no
checking for PTHREAD_PRIO_INHERIT... yes
checking how to run the C preprocessor... ccache_cxx -E
checking for mips-openwrt-linux-ranlib... mips-openwrt-linux-musl-gcc-ranlib
checking for mips-openwrt-linux-ar... mips-openwrt-linux-musl-gcc-ar
checking the archiver (mips-openwrt-linux-musl-gcc-ar) interface... ar
checking for mips-openwrt-linux-strip... (cached) mips-openwrt-linux-musl-strip
checking for mips-openwrt-linux-protoc... /openwrt/staging_dir/hostpkg/bin/protoc
checking for library containing socket... none required
checking for library containing gethostbyname... none required
checking for library containing pcap_close... -lpcap
checking for protobuf library... -lprotobuf-lite
checking whether /openwrt/staging_dir/hostpkg/bin/protoc supports "oneof"... yes
checking for ByteSizeLong() in ::google::protobuf::MessageLite... yes
checking how to run the C++ preprocessor... ccache_cxx -E
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
checking arpa/inet.h usability... yes
checking arpa/inet.h presence... yes
checking for arpa/inet.h... yes
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking for inttypes.h... (cached) yes
checking netdb.h usability... yes
checking netdb.h presence... yes
checking for netdb.h... yes
checking netinet/in.h usability... yes
checking netinet/in.h presence... yes
checking for netinet/in.h... yes
checking for stdint.h... (cached) yes
checking for stdlib.h... (cached) yes
checking for string.h... (cached) yes
checking for strings.h... (cached) yes
checking sys/param.h usability... yes
checking sys/param.h presence... yes
checking for sys/param.h... yes
checking for sys/types.h... (cached) yes
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking for unistd.h... (cached) yes
checking netinet/in_systm.h usability... yes
checking netinet/in_systm.h presence... yes
checking for netinet/in_systm.h... yes
checking for netinet/ip.h... yes
checking for netinet/ip6.h... yes
checking ws2tcpip.h usability... no
checking ws2tcpip.h presence... no
checking for ws2tcpip.h... no
checking pcap/pcap.h usability... yes
checking pcap/pcap.h presence... yes
checking for pcap/pcap.h... yes
checking cxxabi.h usability... yes
checking cxxabi.h presence... yes
checking for cxxabi.h... yes
checking for <unordered_map>... yes
checking for pid_t... yes
checking for size_t... yes
checking for ssize_t... yes
checking for stdbool.h that conforms to C99... no
checking for _Bool... no
checking for uint16_t... yes
checking for uint32_t... yes
checking for uint64_t... yes
checking for uint8_t... yes
checking whether byte ordering is bigendian... (cached) yes
checking vfork.h usability... no
checking vfork.h presence... no
checking for vfork.h... no
checking for fork... yes
checking for vfork... yes
checking for working fork... cross
configure: WARNING: result yes guessed because of cross compilation
checking for working vfork... (cached) yes
checking for alarm... yes
checking for bzero... (cached) yes
checking for gethostbyname... yes
checking for gethostname... yes
checking for inet_ntoa... yes
checking for inet_ntop... yes
checking for inet_pton... yes
checking for memmove... yes
checking for memset... yes
checking for socket... yes
checking for strtol... yes
checking for strtoul... yes
checking for getopt_long... yes
checking for arc4random... no
checking for arc4random_stir... no
checking for srandomdev... no
checking for srandom... yes
checking for gettimeofday... (cached) yes
checking for pcap_close... yes
checking for pcap_create... yes
checking for pcap_open_live... yes
checking for pcap_sendpacket... yes
checking for pcap_datalink_val_to_name... yes
checking for struct sockaddr_in6... yes
checking for sa_family_t... yes
checking for mips-openwrt-linux-pkg-config... /openwrt/staging_dir/host/bin/pkg-config
checking for openssl/ssl.h in /usr/local/ssl... no
checking for openssl/ssl.h in /usr/lib/ssl... no
checking for openssl/ssl.h in /usr/ssl... no
checking for openssl/ssl.h in /usr/pkg... no
checking for openssl/ssl.h in /usr/local... no
checking for openssl/ssl.h in /usr... yes
checking whether compiling and linking against OpenSSL works... no
configure: error: An openssl library is required.
make[3]: *** [Makefile:72: /openwrt/build_dir/target-mips_24kc_musl/spoofer-1.4.6/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
