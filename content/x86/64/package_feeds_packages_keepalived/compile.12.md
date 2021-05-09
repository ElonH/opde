---
title: "compile.12"
date: 2021-05-09 11:30:13.983739
hidden: false
draft: false
weight: -12
---

build number: `12`

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
configure: loading site script /openwrt/include/site/x86_64
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for x86_64-openwrt-linux-strip... x86_64-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether make supports nested variables... (cached) yes
checking pkg-config is at least version 0.9.0... yes
checking for x86_64-openwrt-linux-gcc... ccache_cc
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
checking for x86_64-openwrt-linux-ranlib... x86_64-openwrt-linux-musl-gcc-ranlib
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking whether ln -s works... yes
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for x86_64-openwrt-linux-strip... (cached) x86_64-openwrt-linux-musl-strip
checking for x86_64-openwrt-linux-ldd... no
checking for ldd... ldd
configure: WARNING: using cross tools not prefixed with host triplet
checking for x86_64-openwrt-linux-ar... x86_64-openwrt-linux-musl-gcc-ar
checking the archiver (x86_64-openwrt-linux-musl-gcc-ar) interface... ar
checking msghdr.msg_controllen is size_t... no
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
checking for unaligned memory access causes warnings... no
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
checking openssl/ssl.h usability... yes
checking openssl/ssl.h presence... yes
checking for openssl/ssl.h... yes
checking openssl/err.h usability... yes
checking openssl/err.h presence... yes
checking for openssl/err.h... yes
checking openssl/md5.h usability... yes
checking openssl/md5.h presence... yes
checking for openssl/md5.h... yes
checking for MD5_Init in -lcrypto... yes
checking for SSL_CTX_new in -lssl... yes
checking SSL_set_tlsext_host_name() - may be a definition... yes
checking for SSL_CTX_set_verify_depth... yes
checking for SSL_set0_rbio... yes
checking for OPENSSL_init_crypto... yes
checking for TLS_method... yes
configure: WARNING: Cannot determine if need to OPENSSL_init_crypto() problem. Assuming yes for safety.
checking whether IPV4_DEVCONF_ARP_IGNORE is declared... yes
checking whether IPV4_DEVCONF_ACCEPT_LOCAL is declared... yes
checking whether IPV4_DEVCONF_RP_FILTER is declared... yes
checking whether IPV4_DEVCONF_ARPFILTER is declared... yes
checking for linux/rtnetlink.h... yes
checking for nl_socket_alloc in -lnl-3... yes
checking for genl_connect in -lnl-genl-3... yes
checking netlink/netlink.h usability... yes
checking netlink/netlink.h presence... yes
checking for netlink/netlink.h... yes
checking netlink/genl/ctrl.h usability... yes
checking netlink/genl/ctrl.h presence... yes
checking for netlink/genl/ctrl.h... yes
checking netlink/genl/genl.h usability... yes
checking netlink/genl/genl.h presence... yes
checking for netlink/genl/genl.h... yes
checking for magic_open in -lmagic... yes
checking whether RTA_ENCAP is declared... yes
checking whether RTA_EXPIRES is declared... yes
checking whether RTA_NEWDST is declared... yes
checking whether RTA_PREF is declared... yes
checking whether FRA_SUPPRESS_PREFIXLEN is declared... yes
checking whether FRA_SUPPRESS_IFGROUP is declared... yes
checking whether FRA_TUN_ID is declared... yes
checking whether RTAX_CC_ALGO is declared... yes
checking whether RTAX_QUICKACK is declared... yes
checking whether RTEXT_FILTER_SKIP_STATS is declared... yes
checking whether FRA_L3MDEV is declared... yes
checking whether FRA_UID_RANGE is declared... yes
checking whether RTAX_FASTOPEN_NO_COOKIE is declared... yes
checking whether RTA_VIA is declared... yes
checking whether FRA_PROTOCOL is declared... yes
checking whether FRA_IP_PROTO is declared... yes
checking whether FRA_SPORT_RANGE is declared... yes
checking whether FRA_DPORT_RANGE is declared... yes
checking whether RTA_TTL_PROPAGATE is declared... yes
checking whether IFA_FLAGS is declared... yes
checking whether LWTUNNEL_ENCAP_MPLS is declared... yes
checking whether LWTUNNEL_ENCAP_ILA is declared... yes
checking libiptc/libip6tc.h usability... yes
checking libiptc/libip6tc.h presence... yes
checking for libiptc/libip6tc.h... yes
checking libiptc/libiptc.h usability... yes
checking libiptc/libiptc.h presence... yes
checking for libiptc/libiptc.h... yes
checking libiptc/libxtc.h usability... yes
checking libiptc/libxtc.h presence... yes
checking for libiptc/libxtc.h... yes
checking for library containing iptc_init... -lip4tc
checking for library containing ipset_session_init... -lipset
checking libipset/data.h usability... yes
checking libipset/data.h presence... yes
checking for libipset/data.h... yes
checking libipset/linux_ip_set.h usability... yes
checking libipset/linux_ip_set.h presence... yes
checking for libipset/linux_ip_set.h... yes
checking libipset/session.h usability... yes
checking libipset/session.h presence... yes
checking for libipset/session.h... yes
checking libipset/types.h usability... yes
checking libipset/types.h presence... yes
checking for libipset/types.h... yes
checking for struct xt_set_info_match_v4.match_set.index... yes
checking for libipset version 7 or later... yes
checking for linux/if.h and net/if.h namespace collision... yes
checking for linux/if_ether.h then netinet/in.h then linux/if.h namespace collision... no
checking for linux/if_ether.h then netinet/if_ether.h namespace collision... yes
checking for libiptc/libiptc.h linux/if.h and net/if.h namespace collision... no
checking whether IPVS_DEST_ATTR_ADDR_FAMILY is declared... yes
checking whether IPVS_DAEMON_ATTR_SYNC_MAXLEN is declared... yes
checking whether IPVS_DAEMON_ATTR_MCAST_GROUP is declared... yes
checking whether IPVS_DAEMON_ATTR_MCAST_GROUP6 is declared... yes
checking whether IPVS_DAEMON_ATTR_MCAST_PORT is declared... yes
checking whether IPVS_DAEMON_ATTR_MCAST_TTL is declared... yes
checking whether IPVS_SVC_ATTR_STATS64 is declared... yes
checking whether IPVS_DEST_ATTR_STATS64 is declared... yes
checking whether IPVS_DEST_ATTR_TUN_TYPE is declared... yes
checking whether IP_VS_TUNNEL_ENCAP_FLAG_NOCSUM is declared... yes
checking whether IP_VS_CONN_F_TUNNEL_TYPE_GRE is declared... yes
checking whether IFLA_IPVLAN_MODE is declared... yes
./configure: line 11303: test: =: unary operator expected
checking whether GLOB_BRACE is declared... no
checking whether GLOB_ALTDIRFUNC is declared... no
checking for timegm()... yes
checking whether IFLA_INET6_ADDR_GEN_MODE is declared... yes
checking whether IFLA_VRF_MAX is declared... yes
checking openssl/sha.h usability... yes
checking openssl/sha.h presence... yes
checking for openssl/sha.h... yes
checking for SHA1_Init in -lcrypto... yes
checking whether SO_MARK is declared... yes
checking for sphinx-build... No
checking for rpm... No

checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating Makefile
config.status: creating keepalived/Makefile
config.status: creating lib/Makefile
config.status: creating keepalived/core/Makefile
config.status: creating keepalived.spec
config.status: creating genhash/Makefile
config.status: creating keepalived/check/Makefile
config.status: creating keepalived/vrrp/Makefile
config.status: creating keepalived/bfd/Makefile
config.status: creating doc/Makefile
config.status: creating bin_install/Makefile
config.status: creating keepalived/dbus/Makefile
config.status: creating keepalived/etc/Makefile
config.status: creating keepalived/etc/init/Makefile
config.status: creating keepalived/etc/init.d/Makefile
config.status: creating keepalived/etc/sysconfig/Makefile
config.status: creating keepalived/etc/keepalived/Makefile
config.status: creating keepalived/trackers/Makefile
config.status: creating doc/man/man8/Makefile
config.status: creating doc/man/man5/Makefile
config.status: creating doc/man/man1/Makefile
config.status: creating lib/config.h
config.status: creating lib/config_warnings.h
config.status: executing depfiles commands
configure: WARNING: unrecognized options: --disable-nls

Keepalived configuration
------------------------
Keepalived version       : 2.2.2
Compiler                 : ccache_cc x86_64-openwrt-linux-musl-gcc (OpenWrt GCC 8.4.0 r0-da0bb5a) 8.4.0
Preprocessor flags       : -D_GNU_SOURCE -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/libnl3 -I/openwrt/staging_dir/target-x86_64_musl/usr/include
Compiler flags           : -g -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2=keepalived-2.2.2 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/build_dir/target-x86_64_musl/linux-x86_64/linux-5.4.115 -Wall -Wextra -Wunused -Wstrict-prototypes -Walloca -Walloc-zero -Warray-bounds=2 -Wattribute-alias -Wbad-function-cast -Wcast-align -Wcast-qual -Wchkp -Wdate-time -Wdisabled-optimization -Wdouble-promotion -Wduplicated-branches -Wduplicated-cond -Wfloat-conversion -Wfloat-equal -Wformat-overflow -Wformat-security -Wformat-signedness -Wformat-truncation -Wframe-larger-than=5120 -Wimplicit-fallthrough=3 -Winit-self -Winline -Wjump-misses-init -Wlogical-op -Wmissing-declarations -Wmissing-field-initializers -Wmissing-prototypes -Wnested-externs -Wnormalized -Wnull-dereference -Wold-style-definition -Woverlength-strings -Wpointer-arith -Wredundant-decls -Wshadow -Wshift-overflow=2 -Wstack-protector -Wstrict-overflow=4 -Wstrict-prototypes -Wstringop-overflow=2 -Wsuggest-attribute=cold -Wsuggest-attribute=const -Wsuggest-attribute=format -Wsuggest-attribute=malloc -Wsuggest-attribute=noreturn -Wsuggest-attribute=pure -Wsync-nand -Wtrampolines -Wundef -Wuninitialized -Wunknown-pragmas -Wunsuffixed-float-constants -Wunused-const-variable=2 -Wunused-macros -Wvariadic-macros -Wwrite-strings -fPIE -Wformat -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -O2
Linker flags             : -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro -pie -Wl,-z,relro -Wl,-z,now
Extra Lib                : -lm -lcrypto -lssl -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lnl-3 -lnl-genl-3 -lmagic -lip4tc -lip6tc -lipset
Use IPVS Framework       : Yes
IPVS use libnl           : Yes
IPVS syncd attributes    : Yes
IPVS 64 bit stats        : Yes
HTTP_GET regex support   : No
fwmark socket support    : Yes
Use VRRP Framework       : Yes
Use VRRP VMAC            : Yes
Use VRRP authentication  : Yes
With track_process       : 
With linkbeat            : Yes
Use BFD Framework        : No
SNMP vrrp support        : No
SNMP checker support     : No
SNMP RFCv2 support       : No
SNMP RFCv3 support       : No
DBUS support             : No
SHA1 support             : Yes
Use JSON output          : No
libnl version            : 3
Use IPv4 devconf         : Yes
Use iptables             : Yes
Use libipset             : Yes
Use nftables             : No
init type                : SYSV
systemd notify           : No
Strict config checks     : No
Build genhash            : Yes
Build documentation      : No
Default runtime options  : -D
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2'
Making all in lib
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/lib'
make  all-am
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/lib'
  CC       memory.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       utils.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       notify.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       timer.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       scheduler.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from scheduler.h:39,
                 from scheduler.c:45:
scheduler.c: In function 'thread_new':
list_head.h:134:20: warning: inlining failed in call to 'list_del_init': call is unlikely and code size would grow [-Winline]
 static inline void list_del_init(struct list_head *entry)
                    ^~~~~~~~~~~~~
scheduler.c:1024:2: note: called from here
  list_del_init(&thread->e_list);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from scheduler.h:38,
                 from scheduler.c:45:
scheduler.c: In function 'thread_add_read_sands':
scheduler.c:868:14: warning: inlining failed in call to 'thread_timer_cmp': call is unlikely and code size would grow [-Winline]
 RB_TIMER_CMP(thread);
              ^~~~~~
timer.h:58:1: note: in definition of macro 'RB_TIMER_CMP'
 obj##_timer_cmp(const obj##_t *r1, const obj##_t *r2)  \
 ^~~
In file included from scheduler.h:40,
                 from scheduler.c:45:
scheduler.c:1103:45: note: called from here
  rb_insert_sort_cached(&m->read, thread, n, thread_timer_cmp);
rbtree.h:297:15: note: in definition of macro 'rb_insert_sort_cached'
   int __cmp = compar(new, __data);   \
               ^~~~~~
In file included from scheduler.h:38,
                 from scheduler.c:45:
scheduler.c: In function 'thread_requeue_read':
scheduler.c:868:14: warning: inlining failed in call to 'thread_timer_cmp': call is unlikely and code size would grow [-Winline]
 RB_TIMER_CMP(thread);
              ^~~~~~
timer.h:58:1: note: in definition of macro 'RB_TIMER_CMP'
 obj##_timer_cmp(const obj##_t *r1, const obj##_t *r2)  \
 ^~~
In file included from scheduler.h:40,
                 from scheduler.c:45:
scheduler.c:1167:51: note: called from here
  rb_move_cached(&thread->master->read, thread, n, thread_timer_cmp);
rbtree.h:391:16: note: in definition of macro 'rb_move_cached'
   if ((prev && compar(prev, node) > 0) ||    \
                ^~~~~~
In file included from scheduler.h:38,
                 from scheduler.c:45:
scheduler.c:868:14: warning: inlining failed in call to 'thread_timer_cmp': call is unlikely and code size would grow [-Winline]
 RB_TIMER_CMP(thread);
              ^~~~~~
timer.h:58:1: note: in definition of macro 'RB_TIMER_CMP'
 obj##_timer_cmp(const obj##_t *r1, const obj##_t *r2)  \
 ^~~
In file included from scheduler.h:40,
                 from scheduler.c:45:
scheduler.c:1167:51: note: called from here
  rb_move_cached(&thread->master->read, thread, n, thread_timer_cmp);
rbtree.h:392:16: note: in definition of macro 'rb_move_cached'
       (next && compar(next, node) < 0)) {    \
                ^~~~~~
In file included from scheduler.h:38,
                 from scheduler.c:45:
scheduler.c:868:14: warning: inlining failed in call to 'thread_timer_cmp': call is unlikely and code size would grow [-Winline]
 RB_TIMER_CMP(thread);
              ^~~~~~
timer.h:58:1: note: in definition of macro 'RB_TIMER_CMP'
 obj##_timer_cmp(const obj##_t *r1, const obj##_t *r2)  \
 ^~~
In file included from scheduler.h:40,
                 from scheduler.c:45:
scheduler.c:1167:51: note: called from here
  rb_move_cached(&thread->master->read, thread, n, thread_timer_cmp);
rbtree.h:297:15: note: in definition of macro 'rb_insert_sort_cached'
   int __cmp = compar(new, __data);   \
               ^~~~~~
scheduler.c:1167:2: note: in expansion of macro 'rb_move_cached'
  rb_move_cached(&thread->master->read, thread, n, thread_timer_cmp);
  ^~~~~~~~~~~~~~
In file included from scheduler.h:38,
                 from scheduler.c:45:
scheduler.c: In function 'thread_add_write':
scheduler.c:868:14: warning: inlining failed in call to 'thread_timer_cmp': call is unlikely and code size would grow [-Winline]
 RB_TIMER_CMP(thread);
              ^~~~~~
timer.h:58:1: note: in definition of macro 'RB_TIMER_CMP'
 obj##_timer_cmp(const obj##_t *r1, const obj##_t *r2)  \
 ^~~
In file included from scheduler.h:40,
                 from scheduler.c:45:
scheduler.c:1232:46: note: called from here
  rb_insert_sort_cached(&m->write, thread, n, thread_timer_cmp);
rbtree.h:297:15: note: in definition of macro 'rb_insert_sort_cached'
   int __cmp = compar(new, __data);   \
               ^~~~~~
In file included from scheduler.h:39,
                 from scheduler.c:45:
scheduler.c: In function 'thread_destroy_list':
list_head.h:134:20: warning: inlining failed in call to 'list_del_init': call is unlikely and code size would grow [-Winline]
 static inline void list_del_init(struct list_head *entry)
                    ^~~~~~~~~~~~~
scheduler.c:925:3: note: called from here
   list_del_init(&thread->e_list);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from scheduler.h:39,
                 from scheduler.c:45:
scheduler.c: In function 'thread_cleanup_master':
list_head.h:134:20: warning: inlining failed in call to 'list_del_init': call is unlikely and code size would grow [-Winline]
 static inline void list_del_init(struct list_head *entry)
                    ^~~~~~~~~~~~~
scheduler.c:878:3: note: called from here
   list_del_init(&thread->e_list);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from scheduler.h:38,
                 from scheduler.c:45:
scheduler.c: In function 'thread_add_timer':
scheduler.c:868:14: warning: inlining failed in call to 'thread_timer_cmp': call is unlikely and code size would grow [-Winline]
 RB_TIMER_CMP(thread);
              ^~~~~~
timer.h:58:1: note: in definition of macro 'RB_TIMER_CMP'
 obj##_timer_cmp(const obj##_t *r1, const obj##_t *r2)  \
 ^~~
In file included from scheduler.h:40,
                 from scheduler.c:45:
scheduler.c:1285:46: note: called from here
  rb_insert_sort_cached(&m->timer, thread, n, thread_timer_cmp);
rbtree.h:297:15: note: in definition of macro 'rb_insert_sort_cached'
   int __cmp = compar(new, __data);   \
               ^~~~~~
In file included from scheduler.h:38,
                 from scheduler.c:45:
scheduler.c: In function 'timer_thread_update_timeout':
scheduler.c:868:14: warning: inlining failed in call to 'thread_timer_cmp': call is unlikely and code size would grow [-Winline]
 RB_TIMER_CMP(thread);
              ^~~~~~
timer.h:58:1: note: in definition of macro 'RB_TIMER_CMP'
 obj##_timer_cmp(const obj##_t *r1, const obj##_t *r2)  \
 ^~~
In file included from scheduler.h:40,
                 from scheduler.c:45:
scheduler.c:1309:52: note: called from here
  rb_move_cached(&thread->master->timer, thread, n, thread_timer_cmp);
rbtree.h:391:16: note: in definition of macro 'rb_move_cached'
   if ((prev && compar(prev, node) > 0) ||    \
                ^~~~~~
In file included from scheduler.h:38,
                 from scheduler.c:45:
scheduler.c:868:14: warning: inlining failed in call to 'thread_timer_cmp': call is unlikely and code size would grow [-Winline]
 RB_TIMER_CMP(thread);
              ^~~~~~
timer.h:58:1: note: in definition of macro 'RB_TIMER_CMP'
 obj##_timer_cmp(const obj##_t *r1, const obj##_t *r2)  \
 ^~~
In file included from scheduler.h:40,
                 from scheduler.c:45:
scheduler.c:1309:52: note: called from here
  rb_move_cached(&thread->master->timer, thread, n, thread_timer_cmp);
rbtree.h:392:16: note: in definition of macro 'rb_move_cached'
       (next && compar(next, node) < 0)) {    \
                ^~~~~~
In file included from scheduler.h:38,
                 from scheduler.c:45:
scheduler.c:868:14: warning: inlining failed in call to 'thread_timer_cmp': call is unlikely and code size would grow [-Winline]
 RB_TIMER_CMP(thread);
              ^~~~~~
timer.h:58:1: note: in definition of macro 'RB_TIMER_CMP'
 obj##_timer_cmp(const obj##_t *r1, const obj##_t *r2)  \
 ^~~
In file included from scheduler.h:40,
                 from scheduler.c:45:
scheduler.c:1309:52: note: called from here
  rb_move_cached(&thread->master->timer, thread, n, thread_timer_cmp);
rbtree.h:297:15: note: in definition of macro 'rb_insert_sort_cached'
   int __cmp = compar(new, __data);   \
               ^~~~~~
scheduler.c:1309:2: note: in expansion of macro 'rb_move_cached'
  rb_move_cached(&thread->master->timer, thread, n, thread_timer_cmp);
  ^~~~~~~~~~~~~~
In file included from scheduler.h:38,
                 from scheduler.c:45:
scheduler.c: In function 'thread_add_child':
scheduler.c:868:14: warning: inlining failed in call to 'thread_timer_cmp': call is unlikely and code size would grow [-Winline]
 RB_TIMER_CMP(thread);
              ^~~~~~
timer.h:58:1: note: in definition of macro 'RB_TIMER_CMP'
 obj##_timer_cmp(const obj##_t *r1, const obj##_t *r2)  \
 ^~~
In file included from scheduler.h:40,
                 from scheduler.c:45:
scheduler.c:1352:46: note: called from here
  rb_insert_sort_cached(&m->child, thread, n, thread_timer_cmp);
rbtree.h:297:15: note: in definition of macro 'rb_insert_sort_cached'
   int __cmp = compar(new, __data);   \
               ^~~~~~
In file included from scheduler.h:39,
                 from scheduler.c:45:
scheduler.c: In function 'thread_cancel':
list_head.h:134:20: warning: inlining failed in call to 'list_del_init': call is unlikely and code size would grow [-Winline]
 static inline void list_del_init(struct list_head *entry)
                    ^~~~~~~~~~~~~
scheduler.c:1489:3: note: called from here
   list_del_init(&thread->e_list);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from scheduler.h:39,
                 from scheduler.c:45:
list_head.h:134:20: warning: inlining failed in call to 'list_del_init': call is unlikely and code size would grow [-Winline]
 static inline void list_del_init(struct list_head *entry)
                    ^~~~~~~~~~~~~
scheduler.c:1495:3: note: called from here
   list_del_init(&thread->e_list);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from scheduler.h:39,
                 from scheduler.c:45:
list_head.h:134:20: warning: inlining failed in call to 'list_del_init': call is unlikely and code size would grow [-Winline]
 static inline void list_del_init(struct list_head *entry)
                    ^~~~~~~~~~~~~
scheduler.c:1504:3: note: called from here
   list_del_init(&thread->e_list);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from scheduler.h:39,
                 from scheduler.c:45:
scheduler.c: In function 'process_threads':
list_head.h:134:20: warning: inlining failed in call to 'list_del_init': call is unlikely and code size would grow [-Winline]
 static inline void list_del_init(struct list_head *entry)
                    ^~~~~~~~~~~~~
scheduler.c:1024:2: note: called from here
  list_del_init(&thread->e_list);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  CC       vector.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       html.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       parser.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from parser.c:57:
parser.c: In function 'free_seq':
list_head.h:134:20: warning: inlining failed in call to 'list_del_init': call is unlikely and code size would grow [-Winline]
 static inline void list_del_init(struct list_head *entry)
                    ^~~~~~~~~~~~~
parser.c:1252:2: note: called from here
  list_del_init(&seq->e_list);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from parser.c:57:
parser.c: In function 'free_seq_lst':
list_head.h:134:20: warning: inlining failed in call to 'list_del_init': call is unlikely and code size would grow [-Winline]
 static inline void list_del_init(struct list_head *entry)
                    ^~~~~~~~~~~~~
parser.c:1266:2: note: called from here
  list_del_init(&seq->e_list);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from parser.c:57:
list_head.h:134:20: warning: inlining failed in call to 'list_del_init': call is unlikely and code size would grow [-Winline]
 static inline void list_del_init(struct list_head *entry)
                    ^~~~~~~~~~~~~
parser.c:1270:3: note: called from here
   list_del_init(&param->e_list);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from parser.c:57:
list_head.h:134:20: warning: inlining failed in call to 'list_del_init': call is unlikely and code size would grow [-Winline]
 static inline void list_del_init(struct list_head *entry)
                    ^~~~~~~~~~~~~
parser.c:1279:4: note: called from here
    list_del_init(&value->e_list);
    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from parser.c:57:
list_head.h:134:20: warning: inlining failed in call to 'list_del_init': call is unlikely and code size would grow [-Winline]
 static inline void list_del_init(struct list_head *entry)
                    ^~~~~~~~~~~~~
parser.c:1283:3: note: called from here
   list_del_init(&value_set->e_list);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from parser.c:57:
parser.c: In function 'read_line.constprop':
list_head.h:134:20: warning: inlining failed in call to 'list_del_init': call is unlikely and code size would grow [-Winline]
 static inline void list_del_init(struct list_head *entry)
                    ^~~~~~~~~~~~~
parser.c:1878:2: note: called from here
  list_del_init(&stack_ent->e_list);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from parser.c:57:
list_head.h:134:20: warning: inlining failed in call to 'list_del_init': call is unlikely and code size would grow [-Winline]
 static inline void list_del_init(struct list_head *entry)
                    ^~~~~~~~~~~~~
parser.c:2402:2: note: called from here
  list_del_init(&file->e_list);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from parser.c:57:
list_head.h:134:20: warning: inlining failed in call to 'list_del_init': call is unlikely and code size would grow [-Winline]
 static inline void list_del_init(struct list_head *entry)
                    ^~~~~~~~~~~~~
parser.c:2646:7: note: called from here
       list_del_init(&file->e_list);
       ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from parser.c:57:
parser.c: In function 'init_data':
list_head.h:134:20: warning: inlining failed in call to 'list_del_init': call is unlikely and code size would grow [-Winline]
 static inline void list_del_init(struct list_head *entry)
                    ^~~~~~~~~~~~~
parser.c:1989:2: note: called from here
  list_del_init(&def->e_list);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from parser.c:57:
list_head.h:134:20: warning: inlining failed in call to 'list_del_init': call is unlikely and code size would grow [-Winline]
 static inline void list_del_init(struct list_head *entry)
                    ^~~~~~~~~~~~~
parser.c:1847:3: note: called from here
   list_del_init(&stack->e_list);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  CC       signals.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       logger.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       list_head.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       rbtree.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
rbtree.c: In function '__rb_erase_color':
rbtree.c:94:1: warning: inlining failed in call to '__rb_rotate_set_parents': call is unlikely and code size would grow [-Winline]
 __rb_rotate_set_parents(struct rb_node *old, struct rb_node *new,
 ^~~~~~~~~~~~~~~~~~~~~~~
rbtree.c:279:5: note: called from here
     __rb_rotate_set_parents(parent, sibling, root,
     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        RB_RED);
        ~~~~~~~
rbtree.c:94:1: warning: inlining failed in call to '__rb_rotate_set_parents': call is unlikely and code size would grow [-Winline]
 __rb_rotate_set_parents(struct rb_node *old, struct rb_node *new,
 ^~~~~~~~~~~~~~~~~~~~~~~
rbtree.c:371:4: note: called from here
    __rb_rotate_set_parents(parent, sibling, root,
    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       RB_BLACK);
       ~~~~~~~~~
rbtree.c:94:1: warning: inlining failed in call to '__rb_rotate_set_parents': call is unlikely and code size would grow [-Winline]
 __rb_rotate_set_parents(struct rb_node *old, struct rb_node *new,
 ^~~~~~~~~~~~~~~~~~~~~~~
rbtree.c:383:5: note: called from here
     __rb_rotate_set_parents(parent, sibling, root,
     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        RB_RED);
        ~~~~~~~
rbtree.c:94:1: warning: inlining failed in call to '__rb_rotate_set_parents': call is unlikely and code size would grow [-Winline]
 __rb_rotate_set_parents(struct rb_node *old, struct rb_node *new,
 ^~~~~~~~~~~~~~~~~~~~~~~
rbtree.c:424:4: note: called from here
    __rb_rotate_set_parents(parent, sibling, root,
    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       RB_BLACK);
       ~~~~~~~~~
rbtree.c: In function 'rb_insert_color':
rbtree.c:94:1: warning: inlining failed in call to '__rb_rotate_set_parents': call is unlikely and code size would grow [-Winline]
 __rb_rotate_set_parents(struct rb_node *old, struct rb_node *new,
 ^~~~~~~~~~~~~~~~~~~~~~~
rbtree.c:203:4: note: called from here
    __rb_rotate_set_parents(gparent, parent, root, RB_RED);
    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
rbtree.c:94:1: warning: inlining failed in call to '__rb_rotate_set_parents': call is unlikely and code size would grow [-Winline]
 __rb_rotate_set_parents(struct rb_node *old, struct rb_node *new,
 ^~~~~~~~~~~~~~~~~~~~~~~
rbtree.c:238:4: note: called from here
    __rb_rotate_set_parents(gparent, parent, root, RB_RED);
    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
rbtree.c: In function 'rb_erase':
rbtree.c:94:1: warning: inlining failed in call to '__rb_rotate_set_parents': call is unlikely and code size would grow [-Winline]
 __rb_rotate_set_parents(struct rb_node *old, struct rb_node *new,
 ^~~~~~~~~~~~~~~~~~~~~~~
rbtree.c:279:5: note: called from here
     __rb_rotate_set_parents(parent, sibling, root,
     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        RB_RED);
        ~~~~~~~
rbtree.c:94:1: warning: inlining failed in call to '__rb_rotate_set_parents': call is unlikely and code size would grow [-Winline]
 __rb_rotate_set_parents(struct rb_node *old, struct rb_node *new,
 ^~~~~~~~~~~~~~~~~~~~~~~
rbtree.c:371:4: note: called from here
    __rb_rotate_set_parents(parent, sibling, root,
    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       RB_BLACK);
       ~~~~~~~~~
rbtree.c:94:1: warning: inlining failed in call to '__rb_rotate_set_parents': call is unlikely and code size would grow [-Winline]
 __rb_rotate_set_parents(struct rb_node *old, struct rb_node *new,
 ^~~~~~~~~~~~~~~~~~~~~~~
rbtree.c:383:5: note: called from here
     __rb_rotate_set_parents(parent, sibling, root,
     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        RB_RED);
        ~~~~~~~
rbtree.c:94:1: warning: inlining failed in call to '__rb_rotate_set_parents': call is unlikely and code size would grow [-Winline]
 __rb_rotate_set_parents(struct rb_node *old, struct rb_node *new,
 ^~~~~~~~~~~~~~~~~~~~~~~
rbtree.c:424:4: note: called from here
    __rb_rotate_set_parents(parent, sibling, root,
    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       RB_BLACK);
       ~~~~~~~~~
rbtree.c: In function 'rb_insert_color_cached':
rbtree.c:94:1: warning: inlining failed in call to '__rb_rotate_set_parents': call is unlikely and code size would grow [-Winline]
 __rb_rotate_set_parents(struct rb_node *old, struct rb_node *new,
 ^~~~~~~~~~~~~~~~~~~~~~~
rbtree.c:203:4: note: called from here
    __rb_rotate_set_parents(gparent, parent, root, RB_RED);
    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
rbtree.c:94:1: warning: inlining failed in call to '__rb_rotate_set_parents': call is unlikely and code size would grow [-Winline]
 __rb_rotate_set_parents(struct rb_node *old, struct rb_node *new,
 ^~~~~~~~~~~~~~~~~~~~~~~
rbtree.c:238:4: note: called from here
    __rb_rotate_set_parents(gparent, parent, root, RB_RED);
    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
rbtree.c: In function '__rb_insert_augmented':
rbtree.c:94:1: warning: inlining failed in call to '__rb_rotate_set_parents': call is unlikely and code size would grow [-Winline]
 __rb_rotate_set_parents(struct rb_node *old, struct rb_node *new,
 ^~~~~~~~~~~~~~~~~~~~~~~
rbtree.c:203:4: note: called from here
    __rb_rotate_set_parents(gparent, parent, root, RB_RED);
    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
rbtree.c:94:1: warning: inlining failed in call to '__rb_rotate_set_parents': call is unlikely and code size would grow [-Winline]
 __rb_rotate_set_parents(struct rb_node *old, struct rb_node *new,
 ^~~~~~~~~~~~~~~~~~~~~~~
rbtree.c:238:4: note: called from here
    __rb_rotate_set_parents(gparent, parent, root, RB_RED);
    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
rbtree.c: In function 'rb_erase_cached':
rbtree.c:94:1: warning: inlining failed in call to '__rb_rotate_set_parents': call is unlikely and code size would grow [-Winline]
 __rb_rotate_set_parents(struct rb_node *old, struct rb_node *new,
 ^~~~~~~~~~~~~~~~~~~~~~~
rbtree.c:279:5: note: called from here
     __rb_rotate_set_parents(parent, sibling, root,
     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        RB_RED);
        ~~~~~~~
rbtree.c:94:1: warning: inlining failed in call to '__rb_rotate_set_parents': call is unlikely and code size would grow [-Winline]
 __rb_rotate_set_parents(struct rb_node *old, struct rb_node *new,
 ^~~~~~~~~~~~~~~~~~~~~~~
rbtree.c:371:4: note: called from here
    __rb_rotate_set_parents(parent, sibling, root,
    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       RB_BLACK);
       ~~~~~~~~~
rbtree.c:94:1: warning: inlining failed in call to '__rb_rotate_set_parents': call is unlikely and code size would grow [-Winline]
 __rb_rotate_set_parents(struct rb_node *old, struct rb_node *new,
 ^~~~~~~~~~~~~~~~~~~~~~~
rbtree.c:383:5: note: called from here
     __rb_rotate_set_parents(parent, sibling, root,
     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        RB_RED);
        ~~~~~~~
rbtree.c:94:1: warning: inlining failed in call to '__rb_rotate_set_parents': call is unlikely and code size would grow [-Winline]
 __rb_rotate_set_parents(struct rb_node *old, struct rb_node *new,
 ^~~~~~~~~~~~~~~~~~~~~~~
rbtree.c:424:4: note: called from here
    __rb_rotate_set_parents(parent, sibling, root,
    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       RB_BLACK);
       ~~~~~~~~~
  CC       process.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       json_writer.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       rttables.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  AR       liblib.a
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/lib'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/lib'
Making all in keepalived
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived'
Making all in core
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/core'
  CC       main.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
main.c: In function 'do_reload':
main.c:473:1: warning: inlining failed in call to 'remove_reload_file': call is unlikely and code size would grow [-Winline]
 remove_reload_file(void)
 ^~~~~~~~~~~~~~~~~~
main.c:494:3: note: called from here
   remove_reload_file();
   ^~~~~~~~~~~~~~~~~~~~
main.c: In function 'reload_check_child_thread':
main.c:473:1: warning: inlining failed in call to 'remove_reload_file': call is unlikely and code size would grow [-Winline]
 remove_reload_file(void)
 ^~~~~~~~~~~~~~~~~~
main.c:921:2: note: called from here
  remove_reload_file();
  ^~~~~~~~~~~~~~~~~~~~
In file included from ../../lib/keepalived_magic.h:29,
                 from ../../lib/notify.h:34,
                 from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/global_data.h:50,
                 from main.c:43:
main.c: In function 'keepalived_main':
../../lib/logger.h:60:1: warning: inlining failed in call to 'open_syslog': call is unlikely and code size would grow [-Winline]
 open_syslog(const char *ident)
 ^~~~~~~~~~~
main.c:2337:2: note: called from here
  open_syslog(PACKAGE_NAME);
  ^~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../lib/keepalived_magic.h:29,
                 from ../../lib/notify.h:34,
                 from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/global_data.h:50,
                 from main.c:43:
../../lib/logger.h:60:1: warning: inlining failed in call to 'open_syslog': call is unlikely and code size would grow [-Winline]
 open_syslog(const char *ident)
 ^~~~~~~~~~~
main.c:2337:2: note: called from here
  open_syslog(PACKAGE_NAME);
  ^~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../lib/keepalived_magic.h:29,
                 from ../../lib/notify.h:34,
                 from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/global_data.h:50,
                 from main.c:43:
../../lib/logger.h:60:1: warning: inlining failed in call to 'open_syslog': call is unlikely and code size would grow [-Winline]
 open_syslog(const char *ident)
 ^~~~~~~~~~~
main.c:2378:4: note: called from here
    open_syslog(PACKAGE_NAME);
    ^~~~~~~~~~~~~~~~~~~~~~~~~
main.c:473:1: warning: inlining failed in call to 'remove_reload_file': call is unlikely and code size would grow [-Winline]
 remove_reload_file(void)
 ^~~~~~~~~~~~~~~~~~
main.c:494:3: note: called from here
   remove_reload_file();
   ^~~~~~~~~~~~~~~~~~~~
In file included from ../../lib/keepalived_magic.h:29,
                 from ../../lib/notify.h:34,
                 from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/global_data.h:50,
                 from main.c:43:
../../lib/logger.h:60:1: warning: inlining failed in call to 'open_syslog': call is unlikely and code size would grow [-Winline]
 open_syslog(const char *ident)
 ^~~~~~~~~~~
main.c:2464:4: note: called from here
    open_syslog(syslog_ident);
    ^~~~~~~~~~~~~~~~~~~~~~~~~
main.c:473:1: warning: inlining failed in call to 'remove_reload_file': call is unlikely and code size would grow [-Winline]
 remove_reload_file(void)
 ^~~~~~~~~~~~~~~~~~
main.c:2556:3: note: called from here
   remove_reload_file();
   ^~~~~~~~~~~~~~~~~~~~
  CC       daemon.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       pidfile.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       layer4.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       smtp.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       global_data.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/global_data.h:50,
                 from global_data.c:29:
global_data.c: In function 'init_global_data':
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
global_data.c:309:3: note: called from here
   free_notify_script(&data->vrrp_notify_fifo.script);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/global_data.h:50,
                 from global_data.c:29:
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
global_data.c:324:4: note: called from here
    free_notify_script(&data->lvs_notify_fifo.script);
    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/global_data.h:50,
                 from global_data.c:29:
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
global_data.c:335:4: note: called from here
    free_notify_script(&data->lvs_notify_fifo.script);
    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/global_data.h:50,
                 from global_data.c:29:
global_data.c: In function 'free_global_data':
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
global_data.c:370:2: note: called from here
  free_notify_script(&data->shutdown_script);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/global_data.h:50,
                 from global_data.c:29:
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
global_data.c:369:2: note: called from here
  free_notify_script(&data->startup_script);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/global_data.h:50,
                 from global_data.c:29:
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
global_data.c:376:2: note: called from here
  free_notify_script(&data->notify_fifo.script);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/global_data.h:50,
                 from global_data.c:29:
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
global_data.c:380:2: note: called from here
  free_notify_script(&data->vrrp_notify_fifo.script);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/global_data.h:50,
                 from global_data.c:29:
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
global_data.c:402:2: note: called from here
  free_notify_script(&data->lvs_notify_fifo.script);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  CC       global_parser.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from global_parser.c:46:
global_parser.c: In function 'instance_handler':
../../lib/parser.h:97:1: warning: inlining failed in call to 'set_value_r': call is unlikely and code size would grow [-Winline]
 set_value_r(const vector_t *strvec)
 ^~~~~~~~~~~
../../lib/parser.h:110:26: note: called from here
 #define set_value(str)  (set_value_r(str))
                         ~^~~~~~~~~~~~~~~~~
global_parser.c:1585:33: note: in expansion of macro 'set_value'
    global_data->instance_name = set_value(strvec);
                                 ^~~~~~~~~
global_parser.c: In function 'net_namespace_handler':
../../lib/parser.h:97:1: warning: inlining failed in call to 'set_value_r': call is unlikely and code size would grow [-Winline]
 set_value_r(const vector_t *strvec)
 ^~~~~~~~~~~
../../lib/parser.h:110:26: note: called from here
 #define set_value(str)  (set_value_r(str))
                         ~^~~~~~~~~~~~~~~~~
global_parser.c:1518:36: note: in expansion of macro 'set_value'
   global_data->network_namespace = set_value(strvec);
                                    ^~~~~~~~~
global_parser.c: In function 'net_namespace_ipvs_handler':
../../lib/parser.h:97:1: warning: inlining failed in call to 'set_value_r': call is unlikely and code size would grow [-Winline]
 set_value_r(const vector_t *strvec)
 ^~~~~~~~~~~
../../lib/parser.h:110:26: note: called from here
 #define set_value(str)  (set_value_r(str))
                         ~^~~~~~~~~~~~~~~~~
global_parser.c:1540:41: note: in expansion of macro 'set_value'
   global_data->network_namespace_ipvs = set_value(strvec);
                                         ^~~~~~~~~
global_parser.c: In function 'reload_check_config_handler':
../../lib/parser.h:97:1: warning: inlining failed in call to 'set_value_r': call is unlikely and code size would grow [-Winline]
 set_value_r(const vector_t *strvec)
 ^~~~~~~~~~~
../../lib/parser.h:110:26: note: called from here
 #define set_value(str)  (set_value_r(str))
                         ~^~~~~~~~~~~~~~~~~
global_parser.c:2072:38: note: in expansion of macro 'set_value'
   global_data->reload_check_config = set_value(strvec);
                                      ^~~~~~~~~
global_parser.c: In function 'default_interface_handler':
../../lib/parser.h:97:1: warning: inlining failed in call to 'set_value_r': call is unlikely and code size would grow [-Winline]
 set_value_r(const vector_t *strvec)
 ^~~~~~~~~~~
../../lib/parser.h:110:26: note: called from here
 #define set_value(str)  (set_value_r(str))
                         ~^~~~~~~~~~~~~~~~~
global_parser.c:449:32: note: in expansion of macro 'set_value'
  global_data->default_ifname = set_value(strvec);
                                ^~~~~~~~~
global_parser.c: In function 'emailfrom_handler':
../../lib/parser.h:97:1: warning: inlining failed in call to 'set_value_r': call is unlikely and code size would grow [-Winline]
 set_value_r(const vector_t *strvec)
 ^~~~~~~~~~~
../../lib/parser.h:110:26: note: called from here
 #define set_value(str)  (set_value_r(str))
                         ~^~~~~~~~~~~~~~~~~
global_parser.c:175:28: note: in expansion of macro 'set_value'
  global_data->email_from = set_value(strvec);
                            ^~~~~~~~~
global_parser.c: In function 'routerid_handler':
../../lib/parser.h:97:1: warning: inlining failed in call to 'set_value_r': call is unlikely and code size would grow [-Winline]
 set_value_r(const vector_t *strvec)
 ^~~~~~~~~~~
../../lib/parser.h:110:26: note: called from here
 #define set_value(str)  (set_value_r(str))
                         ~^~~~~~~~~~~~~~~~~
global_parser.c:164:27: note: in expansion of macro 'set_value'
  global_data->router_id = set_value(strvec);
                           ^~~~~~~~~
global_parser.c: In function 'lvs_syncd_handler':
../../lib/parser.h:97:1: warning: inlining failed in call to 'set_value_r': call is unlikely and code size would grow [-Winline]
 set_value_r(const vector_t *strvec)
 ^~~~~~~~~~~
../../lib/parser.h:110:26: note: called from here
 #define set_value(str)  (set_value_r(str))
                         ~^~~~~~~~~~~~~~~~~
global_parser.c:536:34: note: in expansion of macro 'set_value'
  global_data->lvs_syncd.ifname = set_value(strvec);
                                  ^~~~~~~~~
  CC       keepalived_netlink.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
keepalived_netlink.c: In function 'netlink_if_address_filter':
keepalived_netlink.c:145:1: warning: inlining failed in call to 'addr_is_equal2.isra.2': call is unlikely and code size would grow [-Winline]
 addr_is_equal2(struct ifaddrmsg* ifa, void* addr, ip_address_t* vip_addr, interface_t *ifp, vrrp_t *vrrp)
 ^~~~~~~~~~~~~~
keepalived_netlink.c:222:9: note: called from here
     if (addr_is_equal2(ifa, addr, ip_addr, ifp, vrrp))
         ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
keepalived_netlink.c:145:1: warning: inlining failed in call to 'addr_is_equal2.isra.2': call is unlikely and code size would grow [-Winline]
 addr_is_equal2(struct ifaddrmsg* ifa, void* addr, ip_address_t* vip_addr, interface_t *ifp, vrrp_t *vrrp)
 ^~~~~~~~~~~~~~
keepalived_netlink.c:228:8: note: called from here
    if (addr_is_equal2(ifa, addr, ip_addr, ifp, vrrp))
        ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../lib/logger.h:34,
                 from ../../lib/keepalived_magic.h:29,
                 from ../../lib/notify.h:34,
                 from ../../keepalived/include/check_data.h:41,
                 from ../../keepalived/include/check_api.h:35,
                 from keepalived_netlink.c:54:
../../lib/utils.h:164:20: warning: inlining failed in call to 'inaddr_equal': call is unlikely and code size would grow [-Winline]
 static inline bool inaddr_equal(sa_family_t family, const void *addr1, const void *addr2)
                    ^~~~~~~~~~~~
keepalived_netlink.c:971:28: note: called from here
        is_tracking_saddr = inaddr_equal(ifa->ifa_family, &vrrp->saddr, addr.addr);
                            ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../lib/logger.h:34,
                 from ../../lib/keepalived_magic.h:29,
                 from ../../lib/notify.h:34,
                 from ../../keepalived/include/check_data.h:41,
                 from ../../keepalived/include/check_api.h:35,
                 from keepalived_netlink.c:54:
../../lib/utils.h:164:20: warning: inlining failed in call to 'inaddr_equal': call is unlikely and code size would grow [-Winline]
 static inline bool inaddr_equal(sa_family_t family, const void *addr1, const void *addr2)
                    ^~~~~~~~~~~~
keepalived_netlink.c:1015:9: note: called from here
     if (inaddr_equal(AF_INET, &ifp->sin_addr, addr.in)) {
         ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../lib/logger.h:34,
                 from ../../lib/keepalived_magic.h:29,
                 from ../../lib/notify.h:34,
                 from ../../keepalived/include/check_data.h:41,
                 from ../../keepalived/include/check_api.h:35,
                 from keepalived_netlink.c:54:
../../lib/utils.h:164:20: warning: inlining failed in call to 'inaddr_equal': call is unlikely and code size would grow [-Winline]
 static inline bool inaddr_equal(sa_family_t family, const void *addr1, const void *addr2)
                    ^~~~~~~~~~~~
keepalived_netlink.c:1034:11: note: called from here
       if (inaddr_equal(AF_INET, &saddr->u.sin_addr, addr.in)) {
           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../lib/logger.h:34,
                 from ../../lib/keepalived_magic.h:29,
                 from ../../lib/notify.h:34,
                 from ../../keepalived/include/check_data.h:41,
                 from ../../keepalived/include/check_api.h:35,
                 from keepalived_netlink.c:54:
../../lib/utils.h:164:20: warning: inlining failed in call to 'inaddr_equal': call is unlikely and code size would grow [-Winline]
 static inline bool inaddr_equal(sa_family_t family, const void *addr1, const void *addr2)
                    ^~~~~~~~~~~~
keepalived_netlink.c:1042:9: note: called from here
     if (inaddr_equal(AF_INET6, &ifp->sin6_addr, addr.in6)) {
         ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../lib/logger.h:34,
                 from ../../lib/keepalived_magic.h:29,
                 from ../../lib/notify.h:34,
                 from ../../keepalived/include/check_data.h:41,
                 from ../../keepalived/include/check_api.h:35,
                 from keepalived_netlink.c:54:
../../lib/utils.h:164:20: warning: inlining failed in call to 'inaddr_equal': call is unlikely and code size would grow [-Winline]
 static inline bool inaddr_equal(sa_family_t family, const void *addr1, const void *addr2)
                    ^~~~~~~~~~~~
keepalived_netlink.c:1061:11: note: called from here
       if (inaddr_equal(AF_INET6, &saddr->u.sin6_addr, addr.in6)) {
           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../lib/logger.h:34,
                 from ../../lib/keepalived_magic.h:29,
                 from ../../lib/notify.h:34,
                 from ../../keepalived/include/check_data.h:41,
                 from ../../keepalived/include/check_api.h:35,
                 from keepalived_netlink.c:54:
../../lib/utils.h:164:20: warning: inlining failed in call to 'inaddr_equal': call is unlikely and code size would grow [-Winline]
 static inline bool inaddr_equal(sa_family_t family, const void *addr1, const void *addr2)
                    ^~~~~~~~~~~~
keepalived_netlink.c:1095:11: note: called from here
      if (!inaddr_equal(ifa->ifa_family, vrrp->family == AF_INET ? &(PTR_CAST(struct sockaddr_in, &vrrp->saddr))->sin_addr : (void *)&(PTR_CAST(struct sockaddr_in6, &vrrp->saddr))->sin6_addr, addr.addr))
           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../lib/logger.h:34,
                 from ../../lib/keepalived_magic.h:29,
                 from ../../lib/notify.h:34,
                 from ../../keepalived/include/check_data.h:41,
                 from ../../keepalived/include/check_api.h:35,
                 from keepalived_netlink.c:54:
../../lib/utils.h:164:20: warning: inlining failed in call to 'inaddr_equal': call is unlikely and code size would grow [-Winline]
 static inline bool inaddr_equal(sa_family_t family, const void *addr1, const void *addr2)
                    ^~~~~~~~~~~~
keepalived_netlink.c:1100:12: note: called from here
            inaddr_equal(ifa->ifa_family, &vrrp->saddr, addr.addr);
            ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
keepalived_netlink.c:145:1: warning: inlining failed in call to 'addr_is_equal2.isra.2': call is unlikely and code size would grow [-Winline]
 addr_is_equal2(struct ifaddrmsg* ifa, void* addr, ip_address_t* vip_addr, interface_t *ifp, vrrp_t *vrrp)
 ^~~~~~~~~~~~~~
keepalived_netlink.c:173:9: note: called from here
  return addr_is_equal2(ifa, addr, vip_addr, ifp, NULL);
         ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
keepalived_netlink.c:145:1: warning: inlining failed in call to 'addr_is_equal2.isra.2': call is unlikely and code size would grow [-Winline]
 addr_is_equal2(struct ifaddrmsg* ifa, void* addr, ip_address_t* vip_addr, interface_t *ifp, vrrp_t *vrrp)
 ^~~~~~~~~~~~~~
keepalived_netlink.c:173:9: note: called from here
  return addr_is_equal2(ifa, addr, vip_addr, ifp, NULL);
         ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  CC       namespaces.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       reload_monitor.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
reload_monitor.c: In function 'read_file':
reload_monitor.c:115:1: warning: inlining failed in call to 'cancel_reload': call is unlikely and code size would grow [-Winline]
 cancel_reload(bool log)
 ^~~~~~~~~~~~~
reload_monitor.c:234:4: note: called from here
    cancel_reload(true);
    ^~~~~~~~~~~~~~~~~~~
reload_monitor.c:115:1: warning: inlining failed in call to 'cancel_reload': call is unlikely and code size would grow [-Winline]
 cancel_reload(bool log)
 ^~~~~~~~~~~~~
reload_monitor.c:240:3: note: called from here
   cancel_reload(true);
   ^~~~~~~~~~~~~~~~~~~
reload_monitor.c:115:1: warning: inlining failed in call to 'cancel_reload': call is unlikely and code size would grow [-Winline]
 cancel_reload(bool log)
 ^~~~~~~~~~~~~
reload_monitor.c:252:3: note: called from here
   cancel_reload(true);
   ^~~~~~~~~~~~~~~~~~~
reload_monitor.c:115:1: warning: inlining failed in call to 'cancel_reload': call is unlikely and code size would grow [-Winline]
 cancel_reload(bool log)
 ^~~~~~~~~~~~~
reload_monitor.c:271:5: note: called from here
     cancel_reload(true);
     ^~~~~~~~~~~~~~~~~~~
reload_monitor.c: In function 'inotify_event_thread':
reload_monitor.c:115:1: warning: inlining failed in call to 'cancel_reload': call is unlikely and code size would grow [-Winline]
 cancel_reload(bool log)
 ^~~~~~~~~~~~~
reload_monitor.c:370:6: note: called from here
      cancel_reload(true);
      ^~~~~~~~~~~~~~~~~~~
reload_monitor.c:115:1: warning: inlining failed in call to 'cancel_reload': call is unlikely and code size would grow [-Winline]
 cancel_reload(bool log)
 ^~~~~~~~~~~~~
reload_monitor.c:394:7: note: called from here
       cancel_reload(true);
       ^~~~~~~~~~~~~~~~~~~
reload_monitor.c: In function 'stop_reload_monitor':
reload_monitor.c:115:1: warning: inlining failed in call to 'cancel_reload': call is unlikely and code size would grow [-Winline]
 cancel_reload(bool log)
 ^~~~~~~~~~~~~
reload_monitor.c:460:2: note: called from here
  cancel_reload(false);
  ^~~~~~~~~~~~~~~~~~~~
  CC       config_notify.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  AR       libcore.a
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/core'
Making all in vrrp
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/vrrp'
  CC       vrrp_daemon.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       vrrp_print.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       vrrp_data.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../keepalived/include/global_data.h:46,
                 from vrrp_data.c:33:
vrrp_data.c: In function 'free_sync_group':
../../lib/list_head.h:134:20: warning: inlining failed in call to 'list_del_init': call is unlikely and code size would grow [-Winline]
 static inline void list_del_init(struct list_head *entry)
                    ^~~~~~~~~~~~~
vrrp_data.c:148:2: note: called from here
  list_del_init(&sgroup->e_list);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/global_data.h:50,
                 from vrrp_data.c:33:
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
vrrp_data.c:173:2: note: called from here
  free_notify_script(&sgroup->script);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/global_data.h:50,
                 from vrrp_data.c:33:
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
vrrp_data.c:172:2: note: called from here
  free_notify_script(&sgroup->script_stop);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/global_data.h:50,
                 from vrrp_data.c:33:
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
vrrp_data.c:171:2: note: called from here
  free_notify_script(&sgroup->script_fault);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/global_data.h:50,
                 from vrrp_data.c:33:
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
vrrp_data.c:170:2: note: called from here
  free_notify_script(&sgroup->script_master);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/global_data.h:50,
                 from vrrp_data.c:33:
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
vrrp_data.c:169:2: note: called from here
  free_notify_script(&sgroup->script_backup);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/global_data.h:46,
                 from vrrp_data.c:33:
../../lib/list_head.h:134:20: warning: inlining failed in call to 'list_del_init': call is unlikely and code size would grow [-Winline]
 static inline void list_del_init(struct list_head *entry)
                    ^~~~~~~~~~~~~
vrrp_data.c:131:3: note: called from here
   list_del_init(&vrrp->s_list);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/global_data.h:50,
                 from vrrp_data.c:33:
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
vrrp_data.c:173:2: note: called from here
  free_notify_script(&sgroup->script);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/global_data.h:50,
                 from vrrp_data.c:33:
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
vrrp_data.c:172:2: note: called from here
  free_notify_script(&sgroup->script_stop);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/global_data.h:50,
                 from vrrp_data.c:33:
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
vrrp_data.c:171:2: note: called from here
  free_notify_script(&sgroup->script_fault);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/global_data.h:50,
                 from vrrp_data.c:33:
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
vrrp_data.c:170:2: note: called from here
  free_notify_script(&sgroup->script_master);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/global_data.h:50,
                 from vrrp_data.c:33:
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
vrrp_data.c:169:2: note: called from here
  free_notify_script(&sgroup->script_backup);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/global_data.h:46,
                 from vrrp_data.c:33:
vrrp_data.c: In function 'free_vscript':
../../lib/list_head.h:134:20: warning: inlining failed in call to 'list_del_init': call is unlikely and code size would grow [-Winline]
 static inline void list_del_init(struct list_head *entry)
                    ^~~~~~~~~~~~~
vrrp_data.c:271:2: note: called from here
  list_del_init(&vscript->e_list);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/global_data.h:50,
                 from vrrp_data.c:33:
vrrp_data.c: In function 'free_vrrp_data':
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
vrrp_data.c:546:2: note: called from here
  free_notify_script(&vrrp->script_master_rx_lower_pri);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/global_data.h:50,
                 from vrrp_data.c:33:
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
vrrp_data.c:545:2: note: called from here
  free_notify_script(&vrrp->script);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/global_data.h:50,
                 from vrrp_data.c:33:
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
vrrp_data.c:544:2: note: called from here
  free_notify_script(&vrrp->script_deleted);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/global_data.h:50,
                 from vrrp_data.c:33:
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
vrrp_data.c:543:2: note: called from here
  free_notify_script(&vrrp->script_stop);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/global_data.h:50,
                 from vrrp_data.c:33:
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
vrrp_data.c:542:2: note: called from here
  free_notify_script(&vrrp->script_fault);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/global_data.h:50,
                 from vrrp_data.c:33:
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
vrrp_data.c:541:2: note: called from here
  free_notify_script(&vrrp->script_master);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/global_data.h:50,
                 from vrrp_data.c:33:
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
vrrp_data.c:540:2: note: called from here
  free_notify_script(&vrrp->script_backup);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/global_data.h:46,
                 from vrrp_data.c:33:
../../lib/list_head.h:134:20: warning: inlining failed in call to 'list_del_init': call is unlikely and code size would grow [-Winline]
 static inline void list_del_init(struct list_head *entry)
                    ^~~~~~~~~~~~~
vrrp_data.c:563:2: note: called from here
  list_del_init(&vrrp->e_list);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/global_data.h:46,
                 from vrrp_data.c:33:
../../lib/list_head.h:134:20: warning: inlining failed in call to 'list_del_init': call is unlikely and code size would grow [-Winline]
 static inline void list_del_init(struct list_head *entry)
                    ^~~~~~~~~~~~~
vrrp_data.c:500:2: note: called from here
  list_del_init(&peer->e_list);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/global_data.h:46,
                 from vrrp_data.c:33:
../../lib/list_head.h:134:20: warning: inlining failed in call to 'list_del_init': call is unlikely and code size would grow [-Winline]
 static inline void list_del_init(struct list_head *entry)
                    ^~~~~~~~~~~~~
vrrp_data.c:563:2: note: called from here
  list_del_init(&vrrp->e_list);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
  CC       vrrp_parser.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
vrrp_parser.c: In function 'vrrp_notify_master_rx_lower_pri':
vrrp_parser.c:290:1: warning: inlining failed in call to 'set_vrrp_notify_script.isra.4': call is unlikely and code size would grow [-Winline]
 set_vrrp_notify_script(__attribute__((unused)) const vector_t *strvec, int extra_params)
 ^~~~~~~~~~~~~~~~~~~~~~
vrrp_parser.c:1012:37: note: called from here
  vrrp->script_master_rx_lower_pri = set_vrrp_notify_script(strvec, 0);
                                     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
vrrp_parser.c: In function 'vrrp_notify_handler':
vrrp_parser.c:290:1: warning: inlining failed in call to 'set_vrrp_notify_script.isra.4': call is unlikely and code size would grow [-Winline]
 set_vrrp_notify_script(__attribute__((unused)) const vector_t *strvec, int extra_params)
 ^~~~~~~~~~~~~~~~~~~~~~
vrrp_parser.c:1001:17: note: called from here
  vrrp->script = set_vrrp_notify_script(strvec, 4);
                 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
vrrp_parser.c: In function 'vrrp_notify_deleted_handler':
vrrp_parser.c:290:1: warning: inlining failed in call to 'set_vrrp_notify_script.isra.4': call is unlikely and code size would grow [-Winline]
 set_vrrp_notify_script(__attribute__((unused)) const vector_t *strvec, int extra_params)
 ^~~~~~~~~~~~~~~~~~~~~~
vrrp_parser.c:988:26: note: called from here
   vrrp->script_deleted = set_vrrp_notify_script(strvec, 0);
                          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
vrrp_parser.c: In function 'vrrp_notify_stop_handler':
vrrp_parser.c:290:1: warning: inlining failed in call to 'set_vrrp_notify_script.isra.4': call is unlikely and code size would grow [-Winline]
 set_vrrp_notify_script(__attribute__((unused)) const vector_t *strvec, int extra_params)
 ^~~~~~~~~~~~~~~~~~~~~~
vrrp_parser.c:975:22: note: called from here
  vrrp->script_stop = set_vrrp_notify_script(strvec, 0);
                      ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
vrrp_parser.c: In function 'vrrp_notify_fault_handler':
vrrp_parser.c:290:1: warning: inlining failed in call to 'set_vrrp_notify_script.isra.4': call is unlikely and code size would grow [-Winline]
 set_vrrp_notify_script(__attribute__((unused)) const vector_t *strvec, int extra_params)
 ^~~~~~~~~~~~~~~~~~~~~~
vrrp_parser.c:964:23: note: called from here
  vrrp->script_fault = set_vrrp_notify_script(strvec, 0);
                       ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
vrrp_parser.c: In function 'vrrp_notify_master_handler':
vrrp_parser.c:290:1: warning: inlining failed in call to 'set_vrrp_notify_script.isra.4': call is unlikely and code size would grow [-Winline]
 set_vrrp_notify_script(__attribute__((unused)) const vector_t *strvec, int extra_params)
 ^~~~~~~~~~~~~~~~~~~~~~
vrrp_parser.c:953:24: note: called from here
  vrrp->script_master = set_vrrp_notify_script(strvec, 0);
                        ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
vrrp_parser.c: In function 'vrrp_notify_backup_handler':
vrrp_parser.c:290:1: warning: inlining failed in call to 'set_vrrp_notify_script.isra.4': call is unlikely and code size would grow [-Winline]
 set_vrrp_notify_script(__attribute__((unused)) const vector_t *strvec, int extra_params)
 ^~~~~~~~~~~~~~~~~~~~~~
vrrp_parser.c:942:24: note: called from here
  vrrp->script_backup = set_vrrp_notify_script(strvec, 0);
                        ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
vrrp_parser.c: In function 'vrrp_gnotify_handler':
vrrp_parser.c:290:1: warning: inlining failed in call to 'set_vrrp_notify_script.isra.4': call is unlikely and code size would grow [-Winline]
 set_vrrp_notify_script(__attribute__((unused)) const vector_t *strvec, int extra_params)
 ^~~~~~~~~~~~~~~~~~~~~~
vrrp_parser.c:347:19: note: called from here
  vgroup->script = set_vrrp_notify_script(strvec, 4);
                   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
vrrp_parser.c: In function 'vrrp_gnotify_stop_handler':
vrrp_parser.c:290:1: warning: inlining failed in call to 'set_vrrp_notify_script.isra.4': call is unlikely and code size would grow [-Winline]
 set_vrrp_notify_script(__attribute__((unused)) const vector_t *strvec, int extra_params)
 ^~~~~~~~~~~~~~~~~~~~~~
vrrp_parser.c:336:24: note: called from here
  vgroup->script_stop = set_vrrp_notify_script(strvec, 0);
                        ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
vrrp_parser.c: In function 'vrrp_gnotify_fault_handler':
vrrp_parser.c:290:1: warning: inlining failed in call to 'set_vrrp_notify_script.isra.4': call is unlikely and code size would grow [-Winline]
 set_vrrp_notify_script(__attribute__((unused)) const vector_t *strvec, int extra_params)
 ^~~~~~~~~~~~~~~~~~~~~~
vrrp_parser.c:325:25: note: called from here
  vgroup->script_fault = set_vrrp_notify_script(strvec, 0);
                         ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
vrrp_parser.c: In function 'vrrp_gnotify_master_handler':
vrrp_parser.c:290:1: warning: inlining failed in call to 'set_vrrp_notify_script.isra.4': call is unlikely and code size would grow [-Winline]
 set_vrrp_notify_script(__attribute__((unused)) const vector_t *strvec, int extra_params)
 ^~~~~~~~~~~~~~~~~~~~~~
vrrp_parser.c:314:26: note: called from here
  vgroup->script_master = set_vrrp_notify_script(strvec, 0);
                          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
vrrp_parser.c: In function 'vrrp_gnotify_backup_handler':
vrrp_parser.c:290:1: warning: inlining failed in call to 'set_vrrp_notify_script.isra.4': call is unlikely and code size would grow [-Winline]
 set_vrrp_notify_script(__attribute__((unused)) const vector_t *strvec, int extra_params)
 ^~~~~~~~~~~~~~~~~~~~~~
vrrp_parser.c:303:26: note: called from here
  vgroup->script_backup = set_vrrp_notify_script(strvec, 0);
                          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  CC       vrrp.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../lib/logger.h:34,
                 from ../../lib/keepalived_magic.h:29,
                 from ../../lib/notify.h:34,
                 from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/vrrp_arp.h:31,
                 from vrrp.c:49:
vrrp.c: In function 'vrrp_update_pkt':
../../lib/utils.h:183:24: warning: inlining failed in call to 'csum_incremental_update32': call is unlikely and code size would grow [-Winline]
 static inline uint16_t csum_incremental_update32(const uint16_t old_csum, const uint32_t old_val, const uint32_t new_val)
                        ^~~~~~~~~~~~~~~~~~~~~~~~~
vrrp.c:432:20: note: called from here
       hd->chksum = csum_incremental_update32(hd->chksum, ip->daddr, new_daddr);
                    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../lib/logger.h:34,
                 from ../../lib/keepalived_magic.h:29,
                 from ../../lib/notify.h:34,
                 from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/vrrp_arp.h:31,
                 from vrrp.c:49:
../../lib/utils.h:183:24: warning: inlining failed in call to 'csum_incremental_update32': call is unlikely and code size would grow [-Winline]
 static inline uint16_t csum_incremental_update32(const uint16_t old_csum, const uint32_t old_val, const uint32_t new_val)
                        ^~~~~~~~~~~~~~~~~~~~~~~~~
vrrp.c:445:18: note: called from here
     hd->chksum = csum_incremental_update32(hd->chksum, ip->saddr, new_saddr);
                  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../lib/logger.h:34,
                 from ../../lib/keepalived_magic.h:29,
                 from ../../lib/notify.h:34,
                 from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/vrrp_arp.h:31,
                 from vrrp.c:49:
vrrp.c: In function 'vrrp_check_packet':
../../lib/utils.h:183:24: warning: inlining failed in call to 'csum_incremental_update32': call is unlikely and code size would grow [-Winline]
 static inline uint16_t csum_incremental_update32(const uint16_t old_csum, const uint32_t old_val, const uint32_t new_val)
                        ^~~~~~~~~~~~~~~~~~~~~~~~~
vrrp.c:523:16: note: called from here
   hd->chksum = csum_incremental_update32(hd->chksum, ip->daddr, global_data->vrrp_mcast_group4.sin_addr.s_addr);
                ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp.h:40,
                 from ../../keepalived/include/vrrp_arp.h:31,
                 from vrrp.c:49:
vrrp.c: In function 'vrrp_state_master_tx':
../../lib/timer.h:86:1: warning: inlining failed in call to 'timer_add_now': call is unlikely and code size would grow [-Winline]
 timer_add_now(timeval_t a)
 ^~~~~~~~~~~~~
vrrp.c:1688:30: note: called from here
   vrrp->garp_refresh_timer = timer_add_now(vrrp->garp_refresh);
                              ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp.h:40,
                 from ../../keepalived/include/vrrp_arp.h:31,
                 from vrrp.c:49:
../../lib/timer.h:86:1: warning: inlining failed in call to 'timer_add_now': call is unlikely and code size would grow [-Winline]
 timer_add_now(timeval_t a)
 ^~~~~~~~~~~~~
vrrp.c:1692:27: note: called from here
   vrrp->vmac_garp_timer = timer_add_now(vrrp->vmac_garp_intvl);
                           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp.h:40,
                 from ../../keepalived/include/vrrp_arp.h:31,
                 from vrrp.c:49:
../../lib/timer.h:86:1: warning: inlining failed in call to 'timer_add_now': call is unlikely and code size would grow [-Winline]
 timer_add_now(timeval_t a)
 ^~~~~~~~~~~~~
vrrp.c:1973:31: note: called from here
    vrrp->garp_refresh_timer = timer_add_now(vrrp->garp_refresh);
                               ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp.h:40,
                 from ../../keepalived/include/vrrp_arp.h:31,
                 from vrrp.c:49:
../../lib/timer.h:86:1: warning: inlining failed in call to 'timer_add_now': call is unlikely and code size would grow [-Winline]
 timer_add_now(timeval_t a)
 ^~~~~~~~~~~~~
vrrp.c:1980:28: note: called from here
    vrrp->vmac_garp_timer = timer_add_now(vrrp->vmac_garp_intvl);
                            ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp.h:40,
                 from ../../keepalived/include/vrrp_arp.h:31,
                 from vrrp.c:49:
../../lib/timer.h:86:1: warning: inlining failed in call to 'timer_add_now': call is unlikely and code size would grow [-Winline]
 timer_add_now(timeval_t a)
 ^~~~~~~~~~~~~
vrrp.c:1980:28: note: called from here
    vrrp->vmac_garp_timer = timer_add_now(vrrp->vmac_garp_intvl);
                            ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../lib/logger.h:34,
                 from ../../lib/keepalived_magic.h:29,
                 from ../../lib/notify.h:34,
                 from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/vrrp_arp.h:31,
                 from vrrp.c:49:
../../lib/utils.h: In function 'vrrp_complete_init':
../../lib/utils.h:128:19: warning: inlining failed in call to '__ip6_addr_equal': call is unlikely and code size would grow [-Winline]
 static inline int __ip6_addr_equal(const struct in6_addr *a1,
                   ^~~~~~~~~~~~~~~~
../../lib/utils.h:170:10: note: called from here
   return __ip6_addr_equal(a1, a2);
          ^~~~~~~~~~~~~~~~~~~~~~~~
../../lib/utils.h:128:19: warning: inlining failed in call to '__ip6_addr_equal': call is unlikely and code size would grow [-Winline]
 static inline int __ip6_addr_equal(const struct in6_addr *a1,
                   ^~~~~~~~~~~~~~~~
../../lib/utils.h:170:10: note: called from here
   return __ip6_addr_equal(a1, a2);
          ^~~~~~~~~~~~~~~~~~~~~~~~
../../lib/utils.h:128:19: warning: inlining failed in call to '__ip6_addr_equal': call is unlikely and code size would grow [-Winline]
 static inline int __ip6_addr_equal(const struct in6_addr *a1,
                   ^~~~~~~~~~~~~~~~
../../lib/utils.h:170:10: note: called from here
   return __ip6_addr_equal(a1, a2);
          ^~~~~~~~~~~~~~~~~~~~~~~~
../../lib/utils.h:128:19: warning: inlining failed in call to '__ip6_addr_equal': call is unlikely and code size would grow [-Winline]
 static inline int __ip6_addr_equal(const struct in6_addr *a1,
                   ^~~~~~~~~~~~~~~~
../../lib/utils.h:170:10: note: called from here
   return __ip6_addr_equal(a1, a2);
          ^~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp.h:40,
                 from ../../keepalived/include/vrrp_arp.h:31,
                 from vrrp.c:49:
vrrp.c: In function 'clear_diff_vrrp':
../../lib/timer.h:86:1: warning: inlining failed in call to 'timer_add_now': call is unlikely and code size would grow [-Winline]
 timer_add_now(timeval_t a)
 ^~~~~~~~~~~~~
vrrp.c:4730:37: note: called from here
      new_vrrp->garp_refresh_timer = timer_add_now(new_vrrp->garp_refresh);
                                     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  CC       vrrp_notify.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       vrrp_scheduler.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../lib/scheduler.h:38,
                 from ../../keepalived/include/vrrp_scheduler.h:32,
                 from vrrp_scheduler.c:35:
vrrp_scheduler.c: In function 'vrrp_init_instance_sands':
vrrp_scheduler.c:292:14: warning: inlining failed in call to 'vrrp_timer_cmp': call is unlikely and code size would grow [-Winline]
 RB_TIMER_CMP(vrrp);
              ^~~~
../../lib/timer.h:58:1: note: in definition of macro 'RB_TIMER_CMP'
 obj##_timer_cmp(const obj##_t *r1, const obj##_t *r2)  \
 ^~~
In file included from ../../lib/scheduler.h:40,
                 from ../../keepalived/include/vrrp_scheduler.h:32,
                 from vrrp_scheduler.c:35:
vrrp_scheduler.c:328:59: note: called from here
  rb_move_cached(&vrrp->sockets->rb_sands, vrrp, rb_sands, vrrp_timer_cmp);
../../lib/rbtree.h:391:16: note: in definition of macro 'rb_move_cached'
   if ((prev && compar(prev, node) > 0) ||    \
                ^~~~~~
In file included from ../../lib/scheduler.h:38,
                 from ../../keepalived/include/vrrp_scheduler.h:32,
                 from vrrp_scheduler.c:35:
vrrp_scheduler.c:292:14: warning: inlining failed in call to 'vrrp_timer_cmp': call is unlikely and code size would grow [-Winline]
 RB_TIMER_CMP(vrrp);
              ^~~~
../../lib/timer.h:58:1: note: in definition of macro 'RB_TIMER_CMP'
 obj##_timer_cmp(const obj##_t *r1, const obj##_t *r2)  \
 ^~~
In file included from ../../lib/scheduler.h:40,
                 from ../../keepalived/include/vrrp_scheduler.h:32,
                 from vrrp_scheduler.c:35:
vrrp_scheduler.c:328:59: note: called from here
  rb_move_cached(&vrrp->sockets->rb_sands, vrrp, rb_sands, vrrp_timer_cmp);
../../lib/rbtree.h:392:16: note: in definition of macro 'rb_move_cached'
       (next && compar(next, node) < 0)) {    \
                ^~~~~~
In file included from ../../lib/scheduler.h:38,
                 from ../../keepalived/include/vrrp_scheduler.h:32,
                 from vrrp_scheduler.c:35:
vrrp_scheduler.c:292:14: warning: inlining failed in call to 'vrrp_timer_cmp': call is unlikely and code size would grow [-Winline]
 RB_TIMER_CMP(vrrp);
              ^~~~
../../lib/timer.h:58:1: note: in definition of macro 'RB_TIMER_CMP'
 obj##_timer_cmp(const obj##_t *r1, const obj##_t *r2)  \
 ^~~
In file included from ../../lib/scheduler.h:40,
                 from ../../keepalived/include/vrrp_scheduler.h:32,
                 from vrrp_scheduler.c:35:
vrrp_scheduler.c:328:59: note: called from here
  rb_move_cached(&vrrp->sockets->rb_sands, vrrp, rb_sands, vrrp_timer_cmp);
../../lib/rbtree.h:297:15: note: in definition of macro 'rb_insert_sort_cached'
   int __cmp = compar(new, __data);   \
               ^~~~~~
vrrp_scheduler.c:328:2: note: in expansion of macro 'rb_move_cached'
  rb_move_cached(&vrrp->sockets->rb_sands, vrrp, rb_sands, vrrp_timer_cmp);
  ^~~~~~~~~~~~~~
In file included from ../../lib/scheduler.h:38,
                 from ../../keepalived/include/vrrp_scheduler.h:32,
                 from vrrp_scheduler.c:35:
vrrp_scheduler.c: In function 'vrrp_dispatcher_init':
vrrp_scheduler.c:292:14: warning: inlining failed in call to 'vrrp_timer_cmp': call is unlikely and code size would grow [-Winline]
 RB_TIMER_CMP(vrrp);
              ^~~~
../../lib/timer.h:58:1: note: in definition of macro 'RB_TIMER_CMP'
 obj##_timer_cmp(const obj##_t *r1, const obj##_t *r2)  \
 ^~~
In file included from ../../lib/scheduler.h:40,
                 from ../../keepalived/include/vrrp_scheduler.h:32,
                 from vrrp_scheduler.c:35:
vrrp_scheduler.c:338:67: note: called from here
   rb_insert_sort_cached(&vrrp->sockets->rb_sands, vrrp, rb_sands, vrrp_timer_cmp);
../../lib/rbtree.h:297:15: note: in definition of macro 'rb_insert_sort_cached'
   int __cmp = compar(new, __data);   \
               ^~~~~~
  CC       vrrp_sync.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       vrrp_arp.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       vrrp_if.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       vrrp_track.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       vrrp_ipaddress.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../lib/scheduler.h:39,
                 from ../../lib/notify.h:31,
                 from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/vrrp_ipaddress.h:35,
                 from vrrp_ipaddress.c:31:
vrrp_ipaddress.c: In function 'clear_diff_static_addresses':
../../lib/list_head.h:199:20: warning: inlining failed in call to 'list_copy': call is unlikely and code size would grow [-Winline]
 static inline void list_copy(struct list_head *dst, struct list_head *src)
                    ^~~~~~~~~
vrrp_ipaddress.c:770:2: note: called from here
  list_copy(&vrrp_data->static_addresses, &new.vip);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../lib/scheduler.h:39,
                 from ../../lib/notify.h:31,
                 from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/vrrp_ipaddress.h:35,
                 from vrrp_ipaddress.c:31:
../../lib/list_head.h:199:20: warning: inlining failed in call to 'list_copy': call is unlikely and code size would grow [-Winline]
 static inline void list_copy(struct list_head *dst, struct list_head *src)
                    ^~~~~~~~~
vrrp_ipaddress.c:769:2: note: called from here
  list_copy(&old_vrrp_data->static_addresses, &old.vip);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../lib/scheduler.h:39,
                 from ../../lib/notify.h:31,
                 from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/vrrp_ipaddress.h:35,
                 from vrrp_ipaddress.c:31:
../../lib/list_head.h:199:20: warning: inlining failed in call to 'list_copy': call is unlikely and code size would grow [-Winline]
 static inline void list_copy(struct list_head *dst, struct list_head *src)
                    ^~~~~~~~~
vrrp_ipaddress.c:763:2: note: called from here
  list_copy(&new.vip, &vrrp_data->static_addresses);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../lib/scheduler.h:39,
                 from ../../lib/notify.h:31,
                 from ../../keepalived/include/vrrp.h:41,
                 from ../../keepalived/include/vrrp_ipaddress.h:35,
                 from vrrp_ipaddress.c:31:
../../lib/list_head.h:199:20: warning: inlining failed in call to 'list_copy': call is unlikely and code size would grow [-Winline]
 static inline void list_copy(struct list_head *dst, struct list_head *src)
                    ^~~~~~~~~
vrrp_ipaddress.c:762:2: note: called from here
  list_copy(&old.vip, &old_vrrp_data->static_addresses);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  CC       vrrp_ndisc.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       vrrp_if_config.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
vrrp_if_config.c: In function 'set_sysctl':
vrrp_if_config.c:101:1: warning: stack protector not protecting function: all local arrays are less than 4 bytes long [-Wstack-protector]
 set_sysctl(const char* prefix, const char* iface, const char* parameter, unsigned value)
 ^~~~~~~~~~
vrrp_if_config.c: In function 'get_sysctl':
vrrp_if_config.c:131:1: warning: stack protector not protecting function: all local arrays are less than 4 bytes long [-Wstack-protector]
 get_sysctl(const char* prefix, const char* iface, const char* parameter)
 ^~~~~~~~~~
vrrp_if_config.c: In function 'set_promote_secondaries':
vrrp_if_config.c:179:1: warning: inlining failed in call to 'netlink_set_interface_flags': call is unlikely and code size would grow [-Winline]
 netlink_set_interface_flags(int ifindex, const sysctl_opts_t *sys_opts)
 ^~~~~~~~~~~~~~~~~~~~~~~~~~~
vrrp_if_config.c:298:2: note: called from here
  netlink_set_interface_flags(ifp->ifindex, promote_secondaries_sysctl);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
vrrp_if_config.c: In function 'reset_promote_secondaries':
vrrp_if_config.c:179:1: warning: inlining failed in call to 'netlink_set_interface_flags': call is unlikely and code size would grow [-Winline]
 netlink_set_interface_flags(int ifindex, const sysctl_opts_t *sys_opts)
 ^~~~~~~~~~~~~~~~~~~~~~~~~~~
vrrp_if_config.c:306:2: note: called from here
  netlink_set_interface_flags(ifp->ifindex, promote_secondaries_sysctl);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
vrrp_if_config.c: In function 'restore_rp_filter':
vrrp_if_config.c:179:1: warning: inlining failed in call to 'netlink_set_interface_flags': call is unlikely and code size would grow [-Winline]
 netlink_set_interface_flags(int ifindex, const sysctl_opts_t *sys_opts)
 ^~~~~~~~~~~~~~~~~~~~~~~~~~~
vrrp_if_config.c:515:5: note: called from here
     netlink_set_interface_flags(ifp->ifindex, rpfilter_sysctl);
     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
vrrp_if_config.c: In function 'set_interface_parameters':
vrrp_if_config.c:179:1: warning: inlining failed in call to 'netlink_set_interface_flags': call is unlikely and code size would grow [-Winline]
 netlink_set_interface_flags(int ifindex, const sysctl_opts_t *sys_opts)
 ^~~~~~~~~~~~~~~~~~~~~~~~~~~
vrrp_if_config.c:462:4: note: called from here
    netlink_set_interface_flags(ifp->ifindex, rpfilter_sysctl);
    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
vrrp_if_config.c:179:1: warning: inlining failed in call to 'netlink_set_interface_flags': call is unlikely and code size would grow [-Winline]
 netlink_set_interface_flags(int ifindex, const sysctl_opts_t *sys_opts)
 ^~~~~~~~~~~~~~~~~~~~~~~~~~~
vrrp_if_config.c:221:6: note: called from here
  if (netlink_set_interface_flags(ifp->ifindex, vmac_sysctl))
      ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
vrrp_if_config.c:179:1: warning: inlining failed in call to 'netlink_set_interface_flags': call is unlikely and code size would grow [-Winline]
 netlink_set_interface_flags(int ifindex, const sysctl_opts_t *sys_opts)
 ^~~~~~~~~~~~~~~~~~~~~~~~~~~
vrrp_if_config.c:239:8: note: called from here
    if (netlink_set_interface_flags(base_ifp->ifindex, parent_sysctl)) {
        ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
vrrp_if_config.c: In function 'reset_interface_parameters':
vrrp_if_config.c:179:1: warning: inlining failed in call to 'netlink_set_interface_flags': call is unlikely and code size would grow [-Winline]
 netlink_set_interface_flags(int ifindex, const sysctl_opts_t *sys_opts)
 ^~~~~~~~~~~~~~~~~~~~~~~~~~~
vrrp_if_config.c:267:13: note: called from here
  if ((res = netlink_set_interface_flags(ifp->ifindex, reset_parent_sysctl)))
             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  CC       vrrp_static_track.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       vrrp_iproute.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from vrrp_iproute.c:42:
vrrp_iproute.c: In function 'netlink_route':
../../keepalived/include/keepalived_netlink.h:117:1: warning: inlining failed in call to 'rta_addattr32': call is unlikely and code size would grow [-Winline]
 rta_addattr32(struct rtattr *rta, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~~~~~
vrrp_iproute.c:412:3: note: called from here
   rta_addattr32(rta, sizeof(buf), RTAX_RTT, iproute->rtt);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from vrrp_iproute.c:42:
../../keepalived/include/keepalived_netlink.h:117:1: warning: inlining failed in call to 'rta_addattr32': call is unlikely and code size would grow [-Winline]
 rta_addattr32(struct rtattr *rta, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~~~~~
vrrp_iproute.c:415:3: note: called from here
   rta_addattr32(rta, sizeof(buf), RTAX_RTTVAR, iproute->rttvar);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from vrrp_iproute.c:42:
../../keepalived/include/keepalived_netlink.h:117:1: warning: inlining failed in call to 'rta_addattr32': call is unlikely and code size would grow [-Winline]
 rta_addattr32(struct rtattr *rta, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~~~~~
vrrp_iproute.c:418:3: note: called from here
   rta_addattr32(rta, sizeof(buf), RTAX_RTO_MIN, iproute->rto_min);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from vrrp_iproute.c:42:
../../keepalived/include/keepalived_netlink.h:117:1: warning: inlining failed in call to 'rta_addattr32': call is unlikely and code size would grow [-Winline]
 rta_addattr32(struct rtattr *rta, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~~~~~
vrrp_iproute.c:421:3: note: called from here
   rta_addattr32(rta, sizeof(buf), RTAX_FEATURES, iproute->features);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from vrrp_iproute.c:42:
../../keepalived/include/keepalived_netlink.h:117:1: warning: inlining failed in call to 'rta_addattr32': call is unlikely and code size would grow [-Winline]
 rta_addattr32(struct rtattr *rta, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~~~~~
vrrp_iproute.c:424:3: note: called from here
   rta_addattr32(rta, sizeof(buf), RTAX_MTU, iproute->mtu);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from vrrp_iproute.c:42:
../../keepalived/include/keepalived_netlink.h:117:1: warning: inlining failed in call to 'rta_addattr32': call is unlikely and code size would grow [-Winline]
 rta_addattr32(struct rtattr *rta, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~~~~~
vrrp_iproute.c:427:3: note: called from here
   rta_addattr32(rta, sizeof(buf), RTAX_WINDOW, iproute->window);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from vrrp_iproute.c:42:
../../keepalived/include/keepalived_netlink.h:117:1: warning: inlining failed in call to 'rta_addattr32': call is unlikely and code size would grow [-Winline]
 rta_addattr32(struct rtattr *rta, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~~~~~
vrrp_iproute.c:430:3: note: called from here
   rta_addattr32(rta, sizeof(buf), RTAX_SSTHRESH, iproute->ssthresh);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from vrrp_iproute.c:42:
../../keepalived/include/keepalived_netlink.h:117:1: warning: inlining failed in call to 'rta_addattr32': call is unlikely and code size would grow [-Winline]
 rta_addattr32(struct rtattr *rta, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~~~~~
vrrp_iproute.c:433:3: note: called from here
   rta_addattr32(rta, sizeof(buf), RTAX_CWND, iproute->cwnd);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from vrrp_iproute.c:42:
../../keepalived/include/keepalived_netlink.h:117:1: warning: inlining failed in call to 'rta_addattr32': call is unlikely and code size would grow [-Winline]
 rta_addattr32(struct rtattr *rta, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~~~~~
vrrp_iproute.c:436:3: note: called from here
   rta_addattr32(rta, sizeof(buf), RTAX_ADVMSS, iproute->advmss);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from vrrp_iproute.c:42:
../../keepalived/include/keepalived_netlink.h:117:1: warning: inlining failed in call to 'rta_addattr32': call is unlikely and code size would grow [-Winline]
 rta_addattr32(struct rtattr *rta, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~~~~~
vrrp_iproute.c:439:3: note: called from here
   rta_addattr32(rta, sizeof(buf), RTAX_REORDERING, iproute->reordering);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from vrrp_iproute.c:42:
../../keepalived/include/keepalived_netlink.h:117:1: warning: inlining failed in call to 'rta_addattr32': call is unlikely and code size would grow [-Winline]
 rta_addattr32(struct rtattr *rta, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~~~~~
vrrp_iproute.c:442:3: note: called from here
   rta_addattr32(rta, sizeof(buf), RTAX_HOPLIMIT, iproute->hoplimit);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from vrrp_iproute.c:42:
../../keepalived/include/keepalived_netlink.h:117:1: warning: inlining failed in call to 'rta_addattr32': call is unlikely and code size would grow [-Winline]
 rta_addattr32(struct rtattr *rta, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~~~~~
vrrp_iproute.c:445:3: note: called from here
   rta_addattr32(rta, sizeof(buf), RTAX_INITCWND, iproute->initcwnd);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from vrrp_iproute.c:42:
../../keepalived/include/keepalived_netlink.h:117:1: warning: inlining failed in call to 'rta_addattr32': call is unlikely and code size would grow [-Winline]
 rta_addattr32(struct rtattr *rta, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~~~~~
vrrp_iproute.c:448:3: note: called from here
   rta_addattr32(rta, sizeof(buf), RTAX_INITRWND, iproute->initrwnd);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from vrrp_iproute.c:42:
../../keepalived/include/keepalived_netlink.h:117:1: warning: inlining failed in call to 'rta_addattr32': call is unlikely and code size would grow [-Winline]
 rta_addattr32(struct rtattr *rta, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~~~~~
vrrp_iproute.c:452:3: note: called from here
   rta_addattr32(rta, sizeof(buf), RTAX_QUICKACK, iproute->quickack);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from vrrp_iproute.c:42:
../../keepalived/include/keepalived_netlink.h:117:1: warning: inlining failed in call to 'rta_addattr32': call is unlikely and code size would grow [-Winline]
 rta_addattr32(struct rtattr *rta, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~~~~~
vrrp_iproute.c:462:3: note: called from here
   rta_addattr32(rta, sizeof(buf), RTAX_FASTOPEN_NO_COOKIE, iproute->fastopen_no_cookie);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from vrrp_iproute.c:42:
../../keepalived/include/keepalived_netlink.h:117:1: warning: inlining failed in call to 'rta_addattr32': call is unlikely and code size would grow [-Winline]
 rta_addattr32(struct rtattr *rta, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~~~~~
vrrp_iproute.c:472:4: note: called from here
    rta_addattr32(rta, sizeof(buf), RTAX_LOCK, iproute->lock);
    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from vrrp_iproute.c:42:
../../keepalived/include/keepalived_netlink.h:117:1: warning: inlining failed in call to 'rta_addattr32': call is unlikely and code size would grow [-Winline]
 rta_addattr32(struct rtattr *rta, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~~~~~
vrrp_iproute.c:256:54: note: called from here
   rtnh->rtnh_len = (unsigned short)(rtnh->rtnh_len + rta_addattr32(rta, len, RTA_FLOW, nh->realms));
                                                      ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  CC       vrrp_iprule.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from vrrp_iprule.c:42:
vrrp_iprule.c: In function 'netlink_rule':
../../keepalived/include/keepalived_netlink.h:89:1: warning: inlining failed in call to 'addattr32.constprop': call is unlikely and code size would grow [-Winline]
 addattr32(struct nlmsghdr *n, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~
vrrp_iprule.c:183:4: note: called from here
    addattr32(&req.n, sizeof(req), FRA_TABLE, iprule->table);
    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from vrrp_iprule.c:42:
../../keepalived/include/keepalived_netlink.h:89:1: warning: inlining failed in call to 'addattr32.constprop': call is unlikely and code size would grow [-Winline]
 addattr32(struct nlmsghdr *n, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~
vrrp_iprule.c:201:3: note: called from here
   addattr32(&req.n, sizeof(req), FRA_PRIORITY, iprule->priority);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from vrrp_iprule.c:42:
../../keepalived/include/keepalived_netlink.h:89:1: warning: inlining failed in call to 'addattr32.constprop': call is unlikely and code size would grow [-Winline]
 addattr32(struct nlmsghdr *n, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~
vrrp_iprule.c:204:3: note: called from here
   addattr32(&req.n, sizeof(req), FRA_FWMARK, iprule->fwmark);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from vrrp_iprule.c:42:
../../keepalived/include/keepalived_netlink.h:89:1: warning: inlining failed in call to 'addattr32.constprop': call is unlikely and code size would grow [-Winline]
 addattr32(struct nlmsghdr *n, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~
vrrp_iprule.c:207:3: note: called from here
   addattr32(&req.n, sizeof(req), FRA_FWMASK, iprule->fwmask);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from vrrp_iprule.c:42:
../../keepalived/include/keepalived_netlink.h:89:1: warning: inlining failed in call to 'addattr32.constprop': call is unlikely and code size would grow [-Winline]
 addattr32(struct nlmsghdr *n, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~
vrrp_iprule.c:210:3: note: called from here
   addattr32(&req.n, sizeof(req), FRA_FLOW, iprule->realms);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from vrrp_iprule.c:42:
../../keepalived/include/keepalived_netlink.h:89:1: warning: inlining failed in call to 'addattr32.constprop': call is unlikely and code size would grow [-Winline]
 addattr32(struct nlmsghdr *n, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~
vrrp_iprule.c:214:3: note: called from here
   addattr32(&req.n, sizeof(req), FRA_SUPPRESS_PREFIXLEN, iprule->suppress_prefix_len);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from vrrp_iprule.c:42:
../../keepalived/include/keepalived_netlink.h:89:1: warning: inlining failed in call to 'addattr32.constprop': call is unlikely and code size would grow [-Winline]
 addattr32(struct nlmsghdr *n, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~
vrrp_iprule.c:219:3: note: called from here
   addattr32(&req.n, sizeof(req), FRA_SUPPRESS_IFGROUP, iprule->suppress_group);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from vrrp_iprule.c:42:
../../keepalived/include/keepalived_netlink.h:89:1: warning: inlining failed in call to 'addattr32.constprop': call is unlikely and code size would grow [-Winline]
 addattr32(struct nlmsghdr *n, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~
vrrp_iprule.c:264:3: note: called from here
   addattr32(&req.n, sizeof(req), FRA_GOTO, iprule->goto_target);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp_iproute.h:39,
                 from vrrp_iprule.c:40:
vrrp_iprule.c: In function 'clear_diff_rules':
../../keepalived/include/vrrp_ipaddress.h:96:1: warning: inlining failed in call to 'IP_ISEQ': call is unlikely and code size would grow [-Winline]
 IP_ISEQ(ip_address_t *X, const ip_address_t *Y)
 ^~~~~~~
vrrp_iprule.c:67:7: note: called from here
      !IP_ISEQ(x->from_addr, y->from_addr) ||
       ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/vrrp_iproute.h:39,
                 from vrrp_iprule.c:40:
../../keepalived/include/vrrp_ipaddress.h:96:1: warning: inlining failed in call to 'IP_ISEQ': call is unlikely and code size would grow [-Winline]
 IP_ISEQ(ip_address_t *X, const ip_address_t *Y)
 ^~~~~~~
vrrp_iprule.c:68:7: note: called from here
      !IP_ISEQ(x->to_addr, y->to_addr) ||
       ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  CC       vrrp_ip_rule_route_parser.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       vrrp_vmac.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from vrrp_vmac.c:34:
vrrp_vmac.c: In function 'netlink_update_vrf':
../../keepalived/include/keepalived_netlink.h:89:1: warning: inlining failed in call to 'addattr32.constprop': call is unlikely and code size would grow [-Winline]
 addattr32(struct nlmsghdr *n, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~
vrrp_vmac.c:727:2: note: called from here
  addattr32(&req.n, sizeof(req), IFLA_MASTER, ifindex);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from vrrp_vmac.c:34:
vrrp_vmac.c: In function 'netlink_link_add_vmac':
../../keepalived/include/keepalived_netlink.h:89:1: warning: inlining failed in call to 'addattr32.constprop': call is unlikely and code size would grow [-Winline]
 addattr32(struct nlmsghdr *n, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~
vrrp_vmac.c:331:3: note: called from here
   addattr32(&req.n, sizeof(req), IFLA_LINK, vrrp->configured_ifp->ifindex);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from vrrp_vmac.c:34:
../../keepalived/include/keepalived_netlink.h:89:1: warning: inlining failed in call to 'addattr32.constprop': call is unlikely and code size would grow [-Winline]
 addattr32(struct nlmsghdr *n, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~
vrrp_vmac.c:323:3: note: called from here
   addattr32(&req.n, sizeof(req), IFLA_MACVLAN_MODE,
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      MACVLAN_MODE_PRIVATE);
      ~~~~~~~~~~~~~~~~~~~~~
In file included from vrrp_vmac.c:34:
../../keepalived/include/keepalived_netlink.h:89:1: warning: inlining failed in call to 'addattr32.constprop': call is unlikely and code size would grow [-Winline]
 addattr32(struct nlmsghdr *n, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~
vrrp_vmac.c:339:4: note: called from here
    addattr32(&req.n, sizeof(req), IFLA_MASTER, vrrp->configured_ifp->vrf_master_ifp->ifindex);
    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from vrrp_vmac.c:34:
vrrp_vmac.c: In function 'netlink_link_add_ipvlan':
../../keepalived/include/keepalived_netlink.h:89:1: warning: inlining failed in call to 'addattr32.constprop': call is unlikely and code size would grow [-Winline]
 addattr32(struct nlmsghdr *n, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~
vrrp_vmac.c:535:3: note: called from here
   addattr32(&req.n, sizeof(req), IFLA_LINK, vrrp->configured_ifp->ifindex);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from vrrp_vmac.c:34:
../../keepalived/include/keepalived_netlink.h:89:1: warning: inlining failed in call to 'addattr32.constprop': call is unlikely and code size would grow [-Winline]
 addattr32(struct nlmsghdr *n, size_t maxlen, unsigned short type, uint32_t data)
 ^~~~~~~~~
vrrp_vmac.c:558:4: note: called from here
    addattr32(&req.n, sizeof(req), IFLA_MASTER, vrrp->configured_ifp->vrf_master_ifp->ifindex);
    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  CC       vrrp_ipsecah.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       vrrp_firewall.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       vrrp_iptables.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       vrrp_iptables_calls.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
vrrp_iptables_calls.c: In function 'ip4tables_close':
vrrp_iptables_calls.c:159:10: warning: 'sav_errno' may be used uninitialized in this function [-Wmaybe-uninitialized]
   return ( sav_errno ) ;
          ^
vrrp_iptables_calls.c: In function 'ip6tables_close':
vrrp_iptables_calls.c:312:10: warning: 'sav_errno' may be used uninitialized in this function [-Wmaybe-uninitialized]
   return ( sav_errno ) ;
          ^
  CC       vrrp_ipset.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  AR       libvrrp.a
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/vrrp'
Making all in check
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/check'
  CC       check_daemon.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       check_data.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../keepalived/include/check_data.h:41,
                 from check_data.c:30:
check_data.c: In function 'free_rs':
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
check_data.c:441:2: note: called from here
  free_notify_script(&rs->notify_down);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/check_data.h:41,
                 from check_data.c:30:
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
check_data.c:440:2: note: called from here
  free_notify_script(&rs->notify_up);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/check_data.h:41,
                 from check_data.c:30:
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
check_data.c:441:2: note: called from here
  free_notify_script(&rs->notify_down);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/check_data.h:41,
                 from check_data.c:30:
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
check_data.c:440:2: note: called from here
  free_notify_script(&rs->notify_up);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/check_data.h:41,
                 from check_data.c:30:
check_data.c: In function 'free_vs':
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
check_data.c:610:2: note: called from here
  free_notify_script(&vs->notify_quorum_down);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/check_data.h:41,
                 from check_data.c:30:
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
check_data.c:609:2: note: called from here
  free_notify_script(&vs->notify_quorum_up);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/check_data.h:41,
                 from check_data.c:30:
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
check_data.c:610:2: note: called from here
  free_notify_script(&vs->notify_quorum_down);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../keepalived/include/check_data.h:41,
                 from check_data.c:30:
../../lib/notify.h:78:1: warning: inlining failed in call to 'free_notify_script': call is unlikely and code size would grow [-Winline]
 free_notify_script(notify_script_t **script)
 ^~~~~~~~~~~~~~~~~~
check_data.c:609:2: note: called from here
  free_notify_script(&vs->notify_quorum_up);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../lib/logger.h:34,
                 from ../../lib/keepalived_magic.h:29,
                 from ../../lib/notify.h:34,
                 from ../../keepalived/include/check_data.h:41,
                 from check_data.c:30:
../../keepalived/include/ipwrapper.h: In function 'validate_check_config':
../../lib/utils.h:137:20: warning: inlining failed in call to 'sockstorage_equal': call is unlikely and code size would grow [-Winline]
 static inline bool sockstorage_equal(const struct sockaddr_storage *s1,
                    ^~~~~~~~~~~~~~~~~
In file included from check_data.c:38:
../../keepalived/include/ipwrapper.h:49:9: note: called from here
  return sockstorage_equal(&rs_a->addr, &rs_b->addr);
         ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../lib/logger.h:34,
                 from ../../lib/keepalived_magic.h:29,
                 from ../../lib/notify.h:34,
                 from ../../keepalived/include/check_data.h:41,
                 from check_data.c:30:
../../lib/utils.h:137:20: warning: inlining failed in call to 'sockstorage_equal': call is unlikely and code size would grow [-Winline]
 static inline bool sockstorage_equal(const struct sockaddr_storage *s1,
                    ^~~~~~~~~~~~~~~~~
In file included from check_data.c:38:
../../keepalived/include/ipwrapper.h:49:9: note: called from here
  return sockstorage_equal(&rs_a->addr, &rs_b->addr);
         ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  CC       check_parser.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from check_parser.c:38:
check_parser.c: In function 'rs_virtualhost_handler':
../../lib/parser.h:97:1: warning: inlining failed in call to 'set_value_r': call is unlikely and code size would grow [-Winline]
 set_value_r(const vector_t *strvec)
 ^~~~~~~~~~~
../../lib/parser.h:110:26: note: called from here
 #define set_value(str)  (set_value_r(str))
                         ~^~~~~~~~~~~~~~~~~
check_parser.c:870:20: note: in expansion of macro 'set_value'
  rs->virtualhost = set_value(strvec);
                    ^~~~~~~~~
check_parser.c: In function 'vs_virtualhost_handler':
../../lib/parser.h:97:1: warning: inlining failed in call to 'set_value_r': call is unlikely and code size would grow [-Winline]
 set_value_r(const vector_t *strvec)
 ^~~~~~~~~~~
../../lib/parser.h:110:26: note: called from here
 #define set_value(str)  (set_value_r(str))
                         ~^~~~~~~~~~~~~~~~~
check_parser.c:601:20: note: in expansion of macro 'set_value'
  vs->virtualhost = set_value(strvec);
                    ^~~~~~~~~
check_parser.c: In function 'handle_ssl_file':
../../lib/parser.h:97:1: warning: inlining failed in call to 'set_value_r': call is unlikely and code size would grow [-Winline]
 set_value_r(const vector_t *strvec)
 ^~~~~~~~~~~
../../lib/parser.h:110:26: note: called from here
 #define set_value(str)  (set_value_r(str))
                         ~^~~~~~~~~~~~~~~~~
check_parser.c:80:15: note: in expansion of macro 'set_value'
  *file_name = set_value(strvec);
               ^~~~~~~~~
  CC       check_api.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../lib/logger.h:34,
                 from ../../lib/keepalived_magic.h:29,
                 from ../../lib/notify.h:34,
                 from ../../keepalived/include/check_data.h:41,
                 from ../../keepalived/include/check_api.h:35,
                 from check_api.c:30:
check_api.c: In function 'compare_conn_opts':
../../lib/utils.h:137:20: warning: inlining failed in call to 'sockstorage_equal': call is unlikely and code size would grow [-Winline]
 static inline bool sockstorage_equal(const struct sockaddr_storage *s1,
                    ^~~~~~~~~~~~~~~~~
check_api.c:213:7: note: called from here
  if (!sockstorage_equal(&a->dst, &b->dst))
       ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../lib/logger.h:34,
                 from ../../lib/keepalived_magic.h:29,
                 from ../../lib/notify.h:34,
                 from ../../keepalived/include/check_data.h:41,
                 from ../../keepalived/include/check_api.h:35,
                 from check_api.c:30:
../../lib/utils.h:137:20: warning: inlining failed in call to 'sockstorage_equal': call is unlikely and code size would grow [-Winline]
 static inline bool sockstorage_equal(const struct sockaddr_storage *s1,
                    ^~~~~~~~~~~~~~~~~
check_api.c:215:7: note: called from here
  if (!sockstorage_equal(&a->bindto, &b->bindto))
       ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  CC       check_tcp.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       check_http.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from check_http.c:43:
check_http.c: In function 'path_handler':
../../lib/parser.h:97:1: warning: inlining failed in call to 'set_value_r': call is unlikely and code size would grow [-Winline]
 set_value_r(const vector_t *strvec)
 ^~~~~~~~~~~
../../lib/parser.h:110:26: note: called from here
 #define set_value(str)  (set_value_r(str))
                         ~^~~~~~~~~~~~~~~~~
check_http.c:500:14: note: in expansion of macro 'set_value'
  url->path = set_value(strvec);
              ^~~~~~~~~
check_http.c: In function 'url_virtualhost_handler':
../../lib/parser.h:97:1: warning: inlining failed in call to 'set_value_r': call is unlikely and code size would grow [-Winline]
 set_value_r(const vector_t *strvec)
 ^~~~~~~~~~~
../../lib/parser.h:110:26: note: called from here
 #define set_value(str)  (set_value_r(str))
                         ~^~~~~~~~~~~~~~~~~
check_http.c:587:21: note: in expansion of macro 'set_value'
  url->virtualhost = set_value(strvec);
                     ^~~~~~~~~
check_http.c: In function 'virtualhost_handler':
../../lib/parser.h:97:1: warning: inlining failed in call to 'set_value_r': call is unlikely and code size would grow [-Winline]
 set_value_r(const vector_t *strvec)
 ^~~~~~~~~~~
../../lib/parser.h:110:26: note: called from here
 #define set_value(str)  (set_value_r(str))
                         ~^~~~~~~~~~~~~~~~~
check_http.c:458:30: note: in expansion of macro 'set_value'
  http_get_chk->virtualhost = set_value(strvec);
                              ^~~~~~~~~
  CC       check_ssl.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       check_smtp.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       check_misc.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       check_dns.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       check_print.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       ipwrapper.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../lib/logger.h:34,
                 from ../../lib/keepalived_magic.h:29,
                 from ../../lib/notify.h:34,
                 from ../../keepalived/include/check_data.h:41,
                 from ../../keepalived/include/ipwrapper.h:31,
                 from ipwrapper.c:28:
ipwrapper.c: In function 'vsge_exist':
../../lib/utils.h:137:20: warning: inlining failed in call to 'sockstorage_equal': call is unlikely and code size would grow [-Winline]
 static inline bool sockstorage_equal(const struct sockaddr_storage *s1,
                    ^~~~~~~~~~~~~~~~~
ipwrapper.c:79:7: note: called from here
  if (!sockstorage_equal(&vsge_a->addr, &vsge_b->addr) ||
       ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../lib/logger.h:34,
                 from ../../lib/keepalived_magic.h:29,
                 from ../../lib/notify.h:34,
                 from ../../keepalived/include/check_data.h:41,
                 from ../../keepalived/include/ipwrapper.h:31,
                 from ipwrapper.c:28:
../../lib/utils.h:137:20: warning: inlining failed in call to 'sockstorage_equal': call is unlikely and code size would grow [-Winline]
 static inline bool sockstorage_equal(const struct sockaddr_storage *s1,
                    ^~~~~~~~~~~~~~~~~
ipwrapper.c:80:7: note: called from here
      !sockstorage_equal(&vsge_a->addr_end, &vsge_b->addr_end))
       ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../lib/logger.h:34,
                 from ../../lib/keepalived_magic.h:29,
                 from ../../lib/notify.h:34,
                 from ../../keepalived/include/check_data.h:41,
                 from ../../keepalived/include/ipwrapper.h:31,
                 from ipwrapper.c:28:
ipwrapper.c: In function 'clear_diff_services':
../../lib/utils.h:137:20: warning: inlining failed in call to 'sockstorage_equal': call is unlikely and code size would grow [-Winline]
 static inline bool sockstorage_equal(const struct sockaddr_storage *s1,
                    ^~~~~~~~~~~~~~~~~
ipwrapper.c:63:8: note: called from here
       !sockstorage_equal(&vs_a->addr, &vs_b->addr))
        ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../lib/logger.h:34,
                 from ../../lib/keepalived_magic.h:29,
                 from ../../lib/notify.h:34,
                 from ../../keepalived/include/check_data.h:41,
                 from ../../keepalived/include/ipwrapper.h:31,
                 from ipwrapper.c:28:
../../lib/utils.h:137:20: warning: inlining failed in call to 'sockstorage_equal': call is unlikely and code size would grow [-Winline]
 static inline bool sockstorage_equal(const struct sockaddr_storage *s1,
                    ^~~~~~~~~~~~~~~~~
In file included from ipwrapper.c:28:
../../keepalived/include/ipwrapper.h:49:9: note: called from here
  return sockstorage_equal(&rs_a->addr, &rs_b->addr);
         ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../lib/logger.h:34,
                 from ../../lib/keepalived_magic.h:29,
                 from ../../lib/notify.h:34,
                 from ../../keepalived/include/check_data.h:41,
                 from ../../keepalived/include/ipwrapper.h:31,
                 from ipwrapper.c:28:
../../lib/utils.h:137:20: warning: inlining failed in call to 'sockstorage_equal': call is unlikely and code size would grow [-Winline]
 static inline bool sockstorage_equal(const struct sockaddr_storage *s1,
                    ^~~~~~~~~~~~~~~~~
In file included from ipwrapper.c:28:
../../keepalived/include/ipwrapper.h:49:9: note: called from here
  return sockstorage_equal(&rs_a->addr, &rs_b->addr);
         ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  CC       ipvswrapper.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       libipvs.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       check_udp.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       check_ping.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       check_file.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  AR       libcheck.a
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/check'
Making all in trackers
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/trackers'
  CC       track_file.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  AR       libtracker.a
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/trackers'
Making all in etc
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc'
Making all in init
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc/init'
make[7]: Nothing to be done for 'all'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc/init'
Making all in init.d
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc/init.d'
make[7]: Nothing to be done for 'all'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc/init.d'
Making all in keepalived
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc/keepalived'
  CP       keepalived.conf
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc/keepalived'
Making all in sysconfig
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc/sysconfig'
  EDIT     keepalived
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc/sysconfig'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc'
make[7]: Nothing to be done for 'all-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived'
  CC       main.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CCLD     keepalived
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived'
Making all in doc
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/doc'
Making all in man/man8
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/doc/man/man8'
make[6]: Nothing to be done for 'all'.
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/doc/man/man8'
Making all in man/man5
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/doc/man/man5'
make[6]: Nothing to be done for 'all'.
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/doc/man/man5'
Making all in man/man1
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/doc/man/man1'
make[6]: Nothing to be done for 'all'.
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/doc/man/man1'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/doc'
make[6]: Nothing to be done for 'all-am'.
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/doc'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/doc'
Making all in genhash
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/genhash'
  CC       main.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       sock.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       layer4.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       http.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CC       ssl.o
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
  CCLD     genhash
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/genhash'
Making all in bin_install
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/bin_install'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/bin_install'
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2'
  EDIT     README
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2'
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2'
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2'
Making install in lib
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/lib'
make  install-am
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/lib'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/lib'
make[7]: Nothing to be done for 'install-exec-am'.
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/lib'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/lib'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/lib'
Making install in keepalived
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived'
Making install in core
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/core'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/core'
make[7]: Nothing to be done for 'install-exec-am'.
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/core'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/core'
Making install in vrrp
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/vrrp'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/vrrp'
make[7]: Nothing to be done for 'install-exec-am'.
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/vrrp'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/vrrp'
Making install in check
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/check'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/check'
make[7]: Nothing to be done for 'install-exec-am'.
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/check'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/check'
Making install in trackers
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/trackers'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/trackers'
make[7]: Nothing to be done for 'install-exec-am'.
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/trackers'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/trackers'
Making install in etc
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc'
Making install in init
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc/init'
make[8]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc/init'
make[8]: Nothing to be done for 'install-exec-am'.
make[8]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc/init'
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc/init'
Making install in init.d
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc/init.d'
make[8]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc/init.d'
make[8]: Nothing to be done for 'install-exec-am'.
 /usr/bin/mkdir -p '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/ipkg-install/etc/rc.d/init.d'
 /openwrt/staging_dir/host/bin/install -c -m 644 keepalived '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/ipkg-install/etc/rc.d/init.d'
make[8]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc/init.d'
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc/init.d'
Making install in keepalived
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc/keepalived'
make[8]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc/keepalived'
make[8]: Nothing to be done for 'install-exec-am'.
 /usr/bin/mkdir -p '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/ipkg-install/etc/keepalived'
 /openwrt/staging_dir/host/bin/install -c -m 644 keepalived.conf '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/ipkg-install/etc/keepalived'
make[8]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc/keepalived'
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc/keepalived'
Making install in sysconfig
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc/sysconfig'
make[8]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc/sysconfig'
make[8]: Nothing to be done for 'install-exec-am'.
 /usr/bin/mkdir -p '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/ipkg-install/etc/sysconfig'
 /openwrt/staging_dir/host/bin/install -c -m 644 keepalived '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/ipkg-install/etc/sysconfig'
make[8]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc/sysconfig'
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc/sysconfig'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc'
make[8]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc'
make[8]: Nothing to be done for 'install-exec-am'.
make[8]: Nothing to be done for 'install-data-am'.
make[8]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc'
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived/etc'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/ipkg-install/usr/sbin'
  /openwrt/staging_dir/host/bin/install -c keepalived '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/ipkg-install/usr/sbin'
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/keepalived'
Making install in doc
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/doc'
Making install in man/man8
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/doc/man/man8'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/doc/man/man8'
make[7]: Nothing to be done for 'install-exec-am'.
 /usr/bin/mkdir -p '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/ipkg-install/usr/man/man8'
 /openwrt/staging_dir/host/bin/install -c -m 644 keepalived.8 '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/ipkg-install/usr/man/man8'
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/doc/man/man8'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/doc/man/man8'
Making install in man/man5
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/doc/man/man5'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/doc/man/man5'
make[7]: Nothing to be done for 'install-exec-am'.
 /usr/bin/mkdir -p '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/ipkg-install/usr/man/man5'
 /openwrt/staging_dir/host/bin/install -c -m 644 keepalived.conf.5 '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/ipkg-install/usr/man/man5'
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/doc/man/man5'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/doc/man/man5'
Making install in man/man1
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/doc/man/man1'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/doc/man/man1'
make[7]: Nothing to be done for 'install-exec-am'.
 /usr/bin/mkdir -p '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/ipkg-install/usr/man/man1'
 /openwrt/staging_dir/host/bin/install -c -m 644 genhash.1 '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/ipkg-install/usr/man/man1'
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/doc/man/man1'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/doc/man/man1'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/doc'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/doc'
make[7]: Nothing to be done for 'install-exec-am'.
 /usr/bin/mkdir -p '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/ipkg-install/usr/share/snmp/mibs'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/ipkg-install/etc/keepalived/samples'
 /openwrt/staging_dir/host/bin/install -c -m 644 ./samples/client.pem ./samples/dh1024.pem ./samples/keepalived.conf.HTTP_GET.port ./samples/keepalived.conf.IPv6 ./samples/keepalived.conf.PING_CHECK ./samples/keepalived.conf.SMTP_CHECK ./samples/keepalived.conf.SSL_GET ./samples/keepalived.conf.UDP_CHECK ./samples/keepalived.conf.conditional_conf ./samples/keepalived.conf.fwmark ./samples/keepalived.conf.inhibit ./samples/keepalived.conf.misc_check ./samples/keepalived.conf.misc_check_arg ./samples/keepalived.conf.quorum ./samples/keepalived.conf.sample ./samples/keepalived.conf.status_code ./samples/keepalived.conf.track_interface ./samples/keepalived.conf.virtual_server_group ./samples/keepalived.conf.virtualhost ./samples/keepalived.conf.vrrp ./samples/keepalived.conf.vrrp.localcheck ./samples/keepalived.conf.vrrp.lvs_syncd ./samples/keepalived.conf.vrrp.routes ./samples/keepalived.conf.vrrp.rules ./samples/keepalived.conf.vrrp.scripts ./samples/keepalived.conf.vrrp.static_ipaddress ./samples/keepalived.conf.vrrp.sync ./samples/root.pem ./samples/sample.misccheck.smbcheck.sh ./samples/sample_notify_fifo.sh '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/ipkg-install/etc/keepalived/samples'
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/doc'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/doc'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/doc'
Making install in genhash
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/genhash'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/genhash'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/ipkg-install/usr/bin'
  /openwrt/staging_dir/host/bin/install -c genhash '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/ipkg-install/usr/bin'
make[6]: Nothing to be done for 'install-data-am'.
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/genhash'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/genhash'
Making install in bin_install
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/bin_install'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/bin_install'
make[6]: Nothing to be done for 'install-exec-am'.
make[6]: Nothing to be done for 'install-data-am'.
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/bin_install'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/bin_install'
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2'
make[6]: Nothing to be done for 'install-exec-am'.
 /usr/bin/mkdir -p '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/ipkg-install/usr/share/doc/keepalived'
 /openwrt/staging_dir/host/bin/install -c -m 644 README '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2/ipkg-install/usr/share/doc/keepalived'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2'
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/keepalived-2.2.2'
Package keepalived is missing dependencies for the following libraries:
libip6tc.so.2
make[3]: *** [Makefile:295: /openwrt/bin/packages/x86_64/packages/keepalived_2.2.2-1_x86_64.ipk] Error 1
```
