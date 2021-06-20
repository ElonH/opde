---
title: "compile.37"
date: 2021-06-20 22:37:23.040413
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
make package/feeds/packages/nmap/compile -j$(nproc) || make package/feeds/packages/nmap/compile V=s
```

#### Compile.txt

``` bash
configure: loading site script /openwrt/include/site/mips
checking whether NLS is requested... no
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking for mips-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
checking for inline... inline
checking for mips-openwrt-linux-gcc... (cached) ccache_cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether ccache_cc accepts -g... (cached) yes
checking for ccache_cc option to accept ISO C89... (cached) none needed
checking whether we are using the GNU C++ compiler... yes
checking whether ccache_cxx accepts -g... yes
checking for mips-openwrt-linux-ranlib... mips-openwrt-linux-musl-gcc-ranlib
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking for gawk... gawk
checking for __func__... yes
checking for mips-openwrt-linux-strip... /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-strip
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
checking pwd.h usability... yes
checking pwd.h presence... yes
checking for pwd.h... yes
checking termios.h usability... yes
checking termios.h presence... yes
checking for termios.h... yes
checking sys/sockio.h usability... no
checking sys/sockio.h presence... no
checking for sys/sockio.h... no
checking for stdint.h... (cached) yes
checking for sys/stat.h... (cached) yes
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking for linux/rtnetlink.h... yes
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking for net/if.h... yes
checking for library containing setsockopt... none required
checking for library containing gethostbyname... none required
checking if AF_INET6 IPPROTO_RAW sockets include the packet header... yes
checking for a Python interpreter with version >= 2.4... python2
checking for python2... /usr/bin/python2
checking for python2 version... 2.7
checking for python2 platform... linux2
checking for python2 script directory... ${prefix}/lib/python2.7/dist-packages
checking for python2 extension module directory... ${exec_prefix}/lib/python2.7/dist-packages
checking pcap.h usability... yes
checking pcap.h presence... yes
checking for pcap.h... yes
checking for pcap_create in -lpcap... yes
checking sys/ioccom.h usability... no
checking sys/ioccom.h presence... no
checking for sys/ioccom.h... no
checking sys/time.h usability... yes
checking sys/time.h presence... yes
checking for sys/time.h... yes
checking net/bpf.h usability... no
checking net/bpf.h presence... no
checking for net/bpf.h... no
checking if libpcap is suitable... cross-compiling -- assuming yes
checking for pcap_set_immediate_mode... yes
checking pcre/pcre.h usability... no
checking pcre/pcre.h presence... no
checking for pcre/pcre.h... no
checking zlib.h usability... yes
checking zlib.h presence... yes
checking for zlib.h... yes
checking for gzread in -lz... yes
checking for library containing dlopen... none required
yes
checking whether byte ordering is bigendian... (cached) yes
checking if struct in_addr is a wacky huge structure (some Sun boxes)... no
checking if struct icmp exists... yes
checking if struct ip exists... yes
checking if struct ip has ip_sum member... yes
checking for strerror... (cached) yes
checking for type of 6th argument to recvfrom()... socklen_t
configure: creating ./config.status
config.status: creating Makefile
config.status: creating libnetutil/Makefile
config.status: creating nmap_config.h
config.status: nmap_config.h is unchanged
=== configuring in nping (/openwrt/build_dir/target-mips_24kc_musl/nmap-ssl/nmap-7.91/nping)
configure: running /bin/bash ./configure --disable-option-checking '--prefix=/usr'  '--target=mips-openwrt-linux' '--host=mips-openwrt-linux' '--build=x86_64-pc-linux-gnu' '--program-prefix=' '--program-suffix=' '--exec-prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--libexecdir=/usr/lib' '--sysconfdir=/etc' '--datadir=/usr/share' '--localstatedir=/var' '--mandir=/usr/man' '--infodir=/usr/info' '--disable-nls' '_python_sysroot=/openwrt/staging_dir/target-mips_24kc_musl' '_python_prefix=/usr' '_python_exec_prefix=/usr' '--with-libdnet=included' '--with-liblinear=included' '--with-libpcap=/openwrt/staging_dir/target-mips_24kc_musl/usr' '--with-libpcre=/openwrt/staging_dir/target-mips_24kc_musl/usr' '--with-libz=/openwrt/staging_dir/target-mips_24kc_musl/usr' '--with-ncat' '--without-localdirs' '--without-ndiff' '--without-zenmap' '--with-nping' '--with-openssl=/openwrt/staging_dir/target-mips_24kc_musl/usr' '--without-liblua' '--without-libssh2' 'build_alias=x86_64-pc-linux-gnu' 'host_alias=mips-openwrt-linux' 'target_alias=mips-openwrt-linux' 'CC=ccache_cc' 'CFLAGS=-Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/nmap-ssl/nmap-7.91=nmap-7.91 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro ' 'LDFLAGS=-L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro ' 'CPPFLAGS=-I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include ' 'CXX=ccache_cxx' 'CXXFLAGS=-Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/nmap-ssl/nmap-7.91=nmap-7.91 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro ' '--with-libssl-prefix=/openwrt/staging_dir/target-mips_24kc_musl/usr' '--with-libz-prefix=/openwrt/staging_dir/target-mips_24kc_musl/usr' --cache-file=/dev/null --srcdir=.
configure: loading site script /openwrt/include/site/mips
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking for mips-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
checking for inline... inline
checking for mips-openwrt-linux-gcc... (cached) ccache_cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether ccache_cc accepts -g... (cached) yes
checking for ccache_cc option to accept ISO C89... (cached) none needed
checking whether we are using the GNU C++ compiler... yes
checking whether ccache_cxx accepts -g... yes
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether the compiler is gcc 4 or greater... yes
checking for __func__... yes
checking for mips-openwrt-linux-strip... /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-strip
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
checking pwd.h usability... yes
checking pwd.h presence... yes
checking for pwd.h... yes
checking termios.h usability... yes
checking termios.h presence... yes
checking for termios.h... yes
checking sys/sockio.h usability... no
checking sys/sockio.h presence... no
checking for sys/sockio.h... no
checking for library containing setsockopt... none required
checking for library containing gethostbyname... none required
checking for library containing dlopen... none required
checking for library containing nl_handle_alloc... no
checking for EVP_sha256... no
configure: error: Your version of OpenSSL does not support SHA-256. Please install OpenSSL 0.9.8 or later.
configure: error: ./configure failed for nping
make[3]: *** [Makefile:197: /openwrt/build_dir/target-mips_24kc_musl/nmap-ssl/nmap-7.91/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
