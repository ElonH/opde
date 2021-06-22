---
title: "compile.40"
date: 2021-06-22 10:46:12.817090
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
make package/feeds/packages/tinc/compile -j$(nproc) || make package/feeds/packages/tinc/compile V=s
```

#### Compile.txt

``` bash
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force -I m4
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
autoreconf: configure.ac: tracing
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
autoreconf: configure.ac: not using Libtool
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
configure.ac:16: installing './compile'
configure.ac:31: installing './config.guess'
configure.ac:31: installing './config.sub'
configure.ac:8: installing './install-sh'
configure.ac:8: installing './missing'
Makefile.am: installing './INSTALL'
doc/Makefile.am:3: installing 'doc/texinfo.tex'
src/Makefile.am: installing './depcomp'
parallel-tests: installing './test-driver'
autoreconf: Leaving directory `.'
configure: WARNING: unrecognized options: --disable-nls, --with-kernel
configure: loading site script /openwrt/include/site/mips
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether make supports nested variables... (cached) yes
checking for style of include used by make... GNU
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
checking for ccache_cc option to accept ISO C99... none needed
checking how to run the C preprocessor... ccache_cc -E
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking whether to build with code coverage support... no
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking CFLAGS for maximum warnings... -Wall
checking whether C compiler accepts -DFORTIFY_SOURCE=2... yes
checking whether C compiler accepts -fwrapv... yes
checking whether C compiler accepts -fPIE... yes
checking whether the linker accepts -pie... yes
checking whether the linker accepts -Wl,-z,relro... yes
checking whether the linker accepts -Wl,-z,now... yes
checking syslog.h usability... yes
checking syslog.h presence... yes
checking for syslog.h... yes
checking sys/file.h usability... yes
checking sys/file.h presence... yes
checking for sys/file.h... yes
checking sys/ioctl.h usability... yes
checking sys/ioctl.h presence... yes
checking for sys/ioctl.h... yes
checking sys/mman.h usability... yes
checking sys/mman.h presence... yes
checking for sys/mman.h... yes
checking sys/param.h usability... yes
checking sys/param.h presence... yes
checking for sys/param.h... yes
checking sys/resource.h usability... yes
checking sys/resource.h presence... yes
checking for sys/resource.h... yes
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking sys/time.h usability... yes
checking sys/time.h presence... yes
checking for sys/time.h... yes
checking sys/un.h usability... yes
checking sys/un.h presence... yes
checking for sys/un.h... yes
checking sys/wait.h usability... yes
checking sys/wait.h presence... yes
checking for sys/wait.h... yes
checking netdb.h usability... yes
checking netdb.h presence... yes
checking for netdb.h... yes
checking arpa/inet.h usability... yes
checking arpa/inet.h presence... yes
checking for arpa/inet.h... yes
checking dirent.h usability... yes
checking dirent.h presence... yes
checking for dirent.h... yes
checking getopt.h usability... yes
checking getopt.h presence... yes
checking for getopt.h... yes
checking stddef.h usability... yes
checking stddef.h presence... yes
checking for stddef.h... yes
checking for net/if.h... yes
checking for net/if_types.h... no
checking for net/ethernet.h... yes
checking for net/if_arp.h... yes
checking for netinet/in_systm.h... yes
checking for netinet/in.h... yes
checking for netinet/in6.h... no
checking for netpacket/packet.h... yes
checking for netinet/if_ether.h... yes
checking for netinet/ip.h... yes
checking for netinet/ip6.h... yes
checking for resolv.h... yes
checking for netinet/tcp.h... yes
checking for netinet/ip_icmp.h... yes
checking for netinet/icmp6.h... yes
checking for working __malloc__ attribute... yes
checking for working __nonnull__ attribute... yes
checking for working __warn_unused_result__ attribute... yes
checking for struct ether_header... yes
checking for struct arphdr... yes
checking for struct ether_arp... yes
checking for struct ip... yes
checking for struct icmp... yes
checking for struct ip6_hdr... yes
checking for struct icmp6_hdr... yes
checking for struct nd_neighbor_solicit... yes
checking for struct nd_opt_hdr... yes
checking return type of signal handlers... void
checking for asprintf... yes
checking for daemon... yes
checking for fchmod... (cached) yes
checking for flock... yes
checking for fork... yes
checking for gettimeofday... (cached) yes
checking for mlockall... yes
checking for putenv... yes
checking for recvmmsg... yes
checking for strsignal... yes
checking for nanosleep... yes
checking for unsetenv... yes
checking for vsyslog... yes
checking for devname... no
checking for fdevname... no
checking for getopt_long... yes
checking whether res_init is declared... yes
checking for res_init in -lresolv... yes
checking for linux/if_tun.h... yes
checking zlib.h usability... yes
checking zlib.h presence... yes
checking for zlib.h... yes
checking for compress2 in -lz... yes
checking for lzo1x_1_compress in -llzo2... yes
checking lzo/lzo1x.h usability... yes
checking lzo/lzo1x.h presence... yes
checking for lzo/lzo1x.h... yes
checking for dlopen... yes
checking openssl/evp.h usability... no
checking openssl/evp.h presence... no
checking for openssl/evp.h... no
configure: error: LibreSSL/OpenSSL header files not found.
make[3]: *** [Makefile:79: /openwrt/build_dir/target-mips_24kc_musl/tinc-1.1-git/.configured_f0d39d1547a48a7936c082769259d686] Error 1
```
