---
title: "compile.40"
date: 2021-06-22 10:49:10.762908
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
make package/feeds/packages/keepalived/compile -j$(nproc) || make package/feeds/packages/keepalived/compile V=s
```

#### Compile.txt

``` bash
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
checking pkg-config is at least version 0.9.0... yes
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
checking whether make supports the include directive... yes (GNU style)
checking dependency style of ccache_cc... gcc3
checking whether make sets $(MAKE)... (cached) yes
checking for mips-openwrt-linux-ranlib... mips-openwrt-linux-musl-gcc-ranlib
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking whether ln -s works... yes
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for mips-openwrt-linux-strip... (cached) mips-openwrt-linux-musl-strip
checking for mips-openwrt-linux-ldd... no
checking for ldd... ldd
configure: WARNING: using cross tools not prefixed with host triplet
checking for mips-openwrt-linux-ar... mips-openwrt-linux-musl-gcc-ar
checking the archiver (mips-openwrt-linux-musl-gcc-ar) interface... ar
checking msghdr.msg_controllen is size_t... yes
checking diagnostic pragmas in functions... yes
checking diagnostic push/pop pragmas... yes
checking for -Wall... yes
checking for -Wextra... yes
checking for -Wunused... yes
checking for -Wstrict-prototypes... yes
checking for -Wabsolute-value... no
checking for -Waddress-of-packed-member... no
checking for -Walloca... yes
checking for -Walloc-zero... yes
checking for -Warray-bounds=2... yes
checking for -Wattribute-alias... yes
checking for -Wbad-function-cast... yes
checking for -Wcast-align... yes
checking for -Wcast-qual... yes
checking for -Wchkp... yes
checking for -Wdate-time... yes
checking for -Wdisabled-optimization... yes
checking for -Wdouble-promotion... yes
checking for -Wduplicated-branches... yes
checking for -Wduplicated-cond... yes
checking for -Wfloat-conversion... yes
checking for -Wfloat-equal... yes
checking for -Wformat-overflow... yes
checking for -Wformat-security... yes
checking for -Wformat-signedness... yes
checking for -Wformat-truncation... yes
checking for -Wframe-larger-than=5120... yes
checking for -Wimplicit-fallthrough=3... yes
checking for -Winit-self... yes
checking for -Winline... yes
checking for -Wjump-misses-init... yes
checking for -Wlogical-op... yes
checking for -Wmissing-declarations... yes
checking for -Wmissing-field-initializers... yes
checking for -Wmissing-prototypes... yes
checking for -Wnested-externs... yes
checking for -Wnormalized... yes
checking for -Wnull-dereference... yes
checking for -Wold-style-definition... yes
checking for -Woverlength-strings... yes
checking for -Wpointer-arith... yes
checking for -Wredundant-decls... yes
checking for -Wshadow... yes
checking for -Wshift-overflow=2... yes
checking for -Wstack-protector... yes
checking for -Wstrict-overflow=4... yes
checking for -Wstrict-prototypes... yes
checking for -Wstringop-overflow=2... yes
checking for -Wsuggest-attribute=cold... yes
checking for -Wsuggest-attribute=const... yes
checking for -Wsuggest-attribute=format... yes
checking for -Wsuggest-attribute=malloc... yes
checking for -Wsuggest-attribute=noreturn... yes
checking for -Wsuggest-attribute=pure... yes
checking for -Wsync-nand... yes
checking for -Wtrampolines... yes
checking for -Wundef... yes
checking for -Wuninitialized... yes
checking for -Wunknown-pragmas... yes
checking for -Wunsuffixed-float-constants... yes
checking for -Wunused-const-variable=2... yes
checking for -Wunused-macros... yes
checking for -Wvariadic-macros... yes
checking for -Wwrite-strings... yes
checking for PIE support... yes
checking for -Wformat -Werror=format-security support... yes
checking for -Wp,-D_FORTIFY_SOURCE=2 support... yes
checking for -fexceptions support... yes
checking for -fstack-protector-strong support... yes
checking for --param=ssp-buffer-size=4 support... yes
checking for -grecord-gcc-switches support... yes
checking for -Wl,-z,relro support... yes
checking for -Wl,-z,now support... yes
checking for -O2 support... yes
checking for unaligned memory access... unknown
configure: WARNING: Cannot determine if unaligned access supported. Assuming yes.
checking for unaligned memory access causes warnings... yes
checking for clock_gettime() requires -lrt... no
checking how to run the C preprocessor... ccache_cc -E
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
checking arpa/inet.h usability... yes
checking arpa/inet.h presence... yes
checking for arpa/inet.h... yes
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking limits.h usability... yes
checking limits.h presence... yes
checking for limits.h... yes
checking netdb.h usability... yes
checking netdb.h presence... yes
checking for netdb.h... yes
checking netinet/in.h usability... yes
checking netinet/in.h presence... yes
checking for netinet/in.h... yes
checking for stdint.h... (cached) yes
checking for stdlib.h... (cached) yes
checking for string.h... (cached) yes
checking sys/ioctl.h usability... yes
checking sys/ioctl.h presence... yes
checking for sys/ioctl.h... yes
checking sys/param.h usability... yes
checking sys/param.h presence... yes
checking for sys/param.h... yes
checking sys/prctl.h usability... yes
checking sys/prctl.h presence... yes
checking for sys/prctl.h... yes
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking sys/time.h usability... yes
checking sys/time.h presence... yes
checking for sys/time.h... yes
checking syslog.h usability... yes
checking syslog.h presence... yes
checking for syslog.h... yes
checking for unistd.h... (cached) yes
checking linux/errqueue.h needs sys/time.h... yes
checking asm/types.h usability... yes
checking asm/types.h presence... yes
checking for asm/types.h... yes
checking linux/ethtool.h usability... yes
checking linux/ethtool.h presence... yes
checking for linux/ethtool.h... yes
checking linux/icmpv6.h usability... yes
checking linux/icmpv6.h presence... yes
checking for linux/icmpv6.h... yes
checking linux/if_ether.h usability... yes
checking linux/if_ether.h presence... yes
checking for linux/if_ether.h... yes
checking linux/if_packet.h usability... yes
checking linux/if_packet.h presence... yes
checking for linux/if_packet.h... yes
checking linux/ip.h usability... yes
checking linux/ip.h presence... yes
checking for linux/ip.h... yes
checking linux/sockios.h usability... yes
checking linux/sockios.h presence... yes
checking for linux/sockios.h... yes
checking linux/types.h usability... yes
checking linux/types.h presence... yes
checking for linux/types.h... yes
checking for linux/fib_rules.h... yes
checking for linux/if_addr.h... yes
checking for linux/if_link.h... yes
checking for linux/if_arp.h... yes
checking for stdbool.h that conforms to C99... yes
checking for _Bool... yes
checking for inline... inline
checking for int64_t... yes
checking for pid_t... yes
checking for size_t... yes
checking for uint16_t... yes
checking for uint32_t... yes
checking for uint64_t... yes
checking for uint8_t... yes
checking for an ANSI C-conforming const... yes
checking vfork.h usability... no
checking vfork.h presence... no
checking for vfork.h... no
checking for fork... yes
checking for vfork... yes
checking for working fork... cross
configure: WARNING: result yes guessed because of cross compilation
checking for working vfork... (cached) yes
checking for dup2... yes
checking for dup3... yes
checking for getcwd... (cached) yes
checking for gettimeofday... (cached) yes
checking for malloc... yes
checking for memmove... yes
checking for memset... yes
checking for realloc... yes
checking for select... yes
checking for setenv... yes
checking for socket... yes
checking for strcasecmp... yes
checking for strchr... yes
checking for strdup... yes
checking for strerror... (cached) yes
checking for strpbrk... yes
checking for strstr... yes
checking for strtol... yes
checking for strtoul... yes
checking for uname... yes
checking for vsyslog... yes
checking for memfd_create... yes
checking whether O_TMPFILE is declared... yes
checking whether ETHERTYPE_IPV6 is declared... yes
checking openssl/ssl.h usability... no
checking openssl/ssl.h presence... no
checking for openssl/ssl.h... no
configure: error: 
  !!! OpenSSL is not properly installed on your system. !!!
  !!! Can not include OpenSSL headers files.            !!!
make[3]: *** [Makefile:276: /openwrt/build_dir/target-mips_24kc_musl/keepalived-2.2.2/.configured_50a5276b2d6d680992b6dedc30512953] Error 1
```
