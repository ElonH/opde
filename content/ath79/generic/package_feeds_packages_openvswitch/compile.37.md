---
title: "compile.37"
date: 2021-06-20 22:36:26.376348
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
make package/feeds/packages/openvswitch/compile -j$(nproc) || make package/feeds/packages/openvswitch/compile V=s
```

#### Compile.txt

``` bash
WARNING: kmod-openvswitch is not available in the kernel config - generating empty package

Applying ./patches/0001-netdev-linux-Let-interface-flag-survive-internal-por.patch using plaintext: 
patching file lib/netdev-linux.c

Applying ./patches/0002-python-separate-host-target-python-for-cross-compile.patch using plaintext: 
patching file Makefile.am
patching file m4/openvswitch.m4
Hunk #1 succeeded at 372 (offset -11 lines).

Applying ./patches/0003-ovs-lib-fix-install_dir.patch using plaintext: 
patching file utilities/ovs-lib.in

Applying ./patches/0004-build-trim-build.patch using plaintext: 
patching file Makefile.am
Hunk #1 succeeded at 477 (offset 2 lines).

Applying ./patches/0006-datapath-allow-passing-additional-OVS_KERNEL_MAKE_FL.patch using plaintext: 
patching file datapath/linux/Makefile.main.in

Applying ./patches/0007-build-only-link-libopenvswitch-with-libunwind-libunb.patch using plaintext: 
patching file lib/automake.mk
patching file lib/libopenvswitch.pc.in
patching file m4/openvswitch.m4
Hunk #1 succeeded at 646 (offset -11 lines).
Hunk #2 succeeded at 659 (offset -11 lines).
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force -I m4
autoreconf: configure.ac: tracing
autoreconf: running: /openwrt/staging_dir/host/bin/libtoolize --install --force
OpenWrt-libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, `build-aux'.
OpenWrt-libtoolize: linking file `build-aux/config.guess'
OpenWrt-libtoolize: linking file `build-aux/config.sub'
OpenWrt-libtoolize: linking file `build-aux/install-sh'
OpenWrt-libtoolize: linking file `build-aux/ltmain.sh'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `m4'.
OpenWrt-libtoolize: linking file `m4/libtool.m4'
OpenWrt-libtoolize: linking file `m4/ltoptions.m4'
OpenWrt-libtoolize: linking file `m4/ltsugar.m4'
OpenWrt-libtoolize: linking file `m4/ltversion.m4'
OpenWrt-libtoolize: linking file `m4/lt~obsolete.m4'
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
autoreconf: Leaving directory `.'
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/mips
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking how to create a pax tar archive... gnutar
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
checking for ccache_cc option to accept ISO C99... none needed
checking whether we are using the GNU C++ compiler... yes
checking whether ccache_cxx accepts -g... yes
checking dependency style of ccache_cxx... gcc3
checking how to run the C preprocessor... ccache_cc -E
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking pkg-config is at least version 0.9.0... yes
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
checking whether byte ordering is bigendian... (cached) yes
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for ld used by ccache_cc... mips-openwrt-linux-musl-ld
checking if the linker (mips-openwrt-linux-musl-ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... mips-openwrt-linux-musl-gcc-nm
checking the name lister (mips-openwrt-linux-musl-gcc-nm) interface... BSD nm
checking whether ln -s works... yes
checking the maximum length of command line arguments... 3145728
checking whether the shell understands some XSI constructs... yes
checking whether the shell understands "+="... yes
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
checking for mips-openwrt-linux-mt... no
checking for mt... no
checking if : is a manifest tool... no
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
checking how to run the C++ preprocessor... ccache_cxx -E
checking for ld used by ccache_cxx... mips-openwrt-linux-musl-ld
checking if the linker (mips-openwrt-linux-musl-ld) is GNU ld... yes
checking whether the ccache_cxx linker (mips-openwrt-linux-musl-ld) supports shared libraries... yes
checking for ccache_cxx option to produce PIC... -fPIC -DPIC
checking if ccache_cxx PIC flag -fPIC -DPIC works... yes
checking if ccache_cxx static flag -static works... yes
checking if ccache_cxx supports -c -o file.o... yes
checking if ccache_cxx supports -c -o file.o... (cached) yes
checking whether the ccache_cxx linker (mips-openwrt-linux-musl-ld) supports shared libraries... yes
checking dynamic linker characteristics... (cached) GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking for library containing pow... none required
checking for library containing clock_gettime... none required
checking for library containing timer_create... none required
checking for library containing pthread_rwlock_tryrdlock... none required
checking for library containing pthread_rwlockattr_destroy... none required
checking for library containing pthread_spin_lock... none required
checking for pthread_spin_lock... yes
checking whether strerror_r is declared... yes
checking for strerror_r... yes
checking whether strerror_r returns char *... no
checking for MSVC x64 compiler... no
checking windows.h usability... no
checking windows.h presence... no
checking for windows.h... no
checking for linux/netlink.h... yes
checking for pkg-config... /openwrt/staging_dir/host/bin/pkg-config
checking for openssl/ssl.h in /usr/local/ssl... no
checking for openssl/ssl.h in /usr/lib/ssl... no
checking for openssl/ssl.h in /usr/ssl... no
checking for openssl/ssl.h in /usr/pkg... no
checking for openssl/ssl.h in /usr/local... no
checking for openssl/ssl.h in /usr... yes
checking whether compiling and linking against OpenSSL works... no
configure: WARNING: Cannot find openssl:



OpenFlow connections over SSL will not be supported.
(You may use --disable-ssl to suppress this warning.)
checking for Python 3 (version 3.4 or later)... (cached) python3.9
checking for flake8... (cached) no
checking for sphinx-build-3... none
checking for dot... no
checking net/if_dl.h usability... no
checking net/if_dl.h presence... no
checking for net/if_dl.h... no
checking whether strtok_r macro segfaults on some inputs... yes
checking whether AF_XDP is enabled... no
checking whether sys_siglist is declared... (cached) no
checking whether malloc_trim is declared... no
checking for struct stat.st_mtim.tv_nsec... yes
checking for struct stat.st_mtimensec... no
checking for struct ifreq.ifr_flagshigh... no
checking for struct mmsghdr.msg_len... yes
checking for struct sockaddr_in6.sin6_scope_id... yes
checking for mlockall... yes
checking for strnlen... yes
checking for getloadavg... yes
checking for statvfs... yes
checking for getmntent_r... yes
checking for sendmmsg... yes
checking for clock_gettime... yes
checking mntent.h usability... yes
checking mntent.h presence... yes
checking for mntent.h... yes
checking sys/statvfs.h usability... yes
checking sys/statvfs.h presence... yes
checking for sys/statvfs.h... yes
checking linux/types.h usability... yes
checking linux/types.h presence... yes
checking for linux/types.h... yes
checking linux/if_ether.h usability... yes
checking linux/if_ether.h presence... yes
checking for linux/if_ether.h... yes
checking linux/net_namespace.h usability... yes
checking linux/net_namespace.h presence... yes
checking for linux/net_namespace.h... yes
checking stdatomic.h usability... yes
checking stdatomic.h presence... yes
checking for stdatomic.h... yes
checking bits/floatn-common.h usability... no
checking bits/floatn-common.h presence... no
checking for bits/floatn-common.h... no
checking for net/if_mib.h... no
checking for library containing backtrace... no
checking linux/perf_event.h usability... yes
checking linux/perf_event.h presence... yes
checking for linux/perf_event.h... yes
checking valgrind/valgrind.h usability... no
checking valgrind/valgrind.h presence... no
checking for valgrind/valgrind.h... no
checking for connect in -lsocket... no
checking for library containing gethostbyname... none required
checking XenServer release... none
checking for groff... no
checking whether ccache_cc has <threads.h> that supports thread_local... yes
checking for library containing __atomic_load_8... -latomic
checking whether ccache_cc supports GCC 4.0+ atomic built-ins... no
checking value of __atomic_always_lock_free(1)... unsupported
checking value of __atomic_always_lock_free(2)... unsupported
checking value of __atomic_always_lock_free(4)... unsupported
checking value of __atomic_always_lock_free(8)... unsupported
checking for library containing aio_write... none required
checking for pthread_set_name_np... no
checking for pthread_setname_np() variant... glibc
checking whether __linux__ is defined... true
checking linker output version information... libX-2.15.so.0.0.0)
checking whether ccache_cxx supports C++11 features by default... yes
checking for working posix_memalign... no
checking for ub_ctx_create in -lunbound... no
checking for unw_backtrace in -lunwind... yes
checking libunwind.h usability... yes
checking libunwind.h presence... yes
checking for libunwind.h... yes
checking whether the preprocessor supports include_next... yes
checking whether system header files limit the line length... no
checking for stdio.h... yes
checking for string.h... (cached) yes
checking whether ccache_cc accepts -Werror... yes
checking whether ccache_cc accepts -Wall... yes
checking whether ccache_cc accepts -Wextra... yes
checking whether ccache_cc accepts -Wno-sign-compare... yes
checking whether ccache_cc accepts -Wpointer-arith... yes
checking whether ccache_cc accepts -Wformat -Wformat-security... yes
checking whether ccache_cc accepts -Wswitch-enum... yes
checking whether ccache_cc accepts -Wunused-parameter... yes
checking whether ccache_cc accepts -Wbad-function-cast... yes
checking whether ccache_cc accepts -Wcast-align... yes
checking whether ccache_cc accepts -Wstrict-prototypes... yes
checking whether ccache_cc accepts -Wold-style-definition... yes
checking whether ccache_cc accepts -Wmissing-prototypes... yes
checking whether ccache_cc accepts -Wmissing-field-initializers... yes
checking whether ccache_cc accepts -Wthread-safety... no
checking whether ccache_cc accepts -fno-strict-aliasing... yes
checking whether ccache_cc accepts -Wswitch-bool... yes
checking whether ccache_cc accepts -Wlogical-not-parentheses... yes
checking whether ccache_cc accepts -Wsizeof-array-argument... yes
checking whether ccache_cc accepts -Wbool-compare... yes
checking whether ccache_cc accepts -Wshift-negative-value... yes
checking whether ccache_cc accepts -Wduplicated-cond... yes
checking whether ccache_cc accepts -Qunused-arguments... no
checking whether ccache_cc accepts -Wshadow... yes
checking whether ccache_cc accepts -Wmultistatement-macros... yes
checking whether ccache_cc accepts -Wcast-align=strict... yes
checking whether ccache_cc accepts -Wno-null-pointer-arithmetic... no
checking whether ccache_cc accepts -Warray-bounds-pointer-arithmetic... no
checking whether ccache_cc accepts -Wno-unused... yes
checking whether ccache_cc accepts -Wno-unused-parameter... yes
checking whether ccache_cc accepts -mavx512f... no
checking whether ccache_cc accepts -mavx512f... (cached) no
checking target hint for cgcc... other
checking vector options for cgcc... 
checking whether DPCLS Autovalidator is default implementation... no
checking binutils avx512 assembler checks passing... no
configure: WARNING: --with-linux is deprecated and kernel support is limited to 5.8 and below
checking for Linux build directory... /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124
checking for Linux source directory... /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124
checking for kernel version... 5.4.124
checking whether src_err, matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/arch/x86/include/asm/checksum_32.h... file not found
checking whether rt6_get_cookie matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/ip6_fib.h... yes
checking whether ipv6_stub has member dst_entry in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/addrconf.h... no
checking whether ipv6_dst_lookup.*net matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/addrconf.h... no
checking whether ipv6_dst_lookup_flow.*net matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/addrconf.h... no
checking whether ipv6_stub matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/addrconf.h... no
checking whether ipv6_dst_lookup_flow matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/addrconf.h... no
checking whether ERR_CAST matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/err.h... yes
checking whether IS_ERR_OR_NULL matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/err.h... yes
checking whether PTR_ERR_OR_ZERO matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/err.h... yes
checking whether static_branch_unlikely( matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/jump_label.h... yes
checking whether DEFINE_STATIC_KEY_FALSE matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/jump_label.h... yes
checking whether DECLARE_STATIC_KEY_FALSE matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/jump_label.h... yes
checking whether eth_hw_addr_random matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/etherdevice.h... yes
checking whether ether_addr_copy matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/etherdevice.h... yes
checking whether IFLA_GENEVE_TOS matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/uapi/linux/if_link.h... yes
checking whether rtnl_link_stats64 matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/uapi/linux/if_link.h... yes
checking whether rtnl_link_stats64 matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/if_link.h... no
checking whether vlan_set_encap_proto matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/if_vlan.h... yes
checking whether vlan_hwaccel_push_inside matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/if_vlan.h... yes
checking whether __vlan_hwaccel_clear_tag matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/if_vlan.h... yes
checking whether ipv4_is_multicast matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/in.h... yes
checking whether proto_ports_offset matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/in.h... yes
checking whether __ip_select_ident.*dst_entry matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/ip.h... no
checking whether __ip_select_ident.*net matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/ip.h... yes
checking whether inet_get_local_port_range.*net matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/ip.h... yes
checking whether ip_defrag.*net matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/ip.h... yes
checking whether ip_do_fragment has parameter net in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/ip.h... yes
checking whether ip_local_out has parameter net in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/ip.h... yes
checking whether ip_skb_dst_mtu matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/ip.h... yes
checking whether IPSKB_FRAG_PMTU matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/ip.h... yes
checking whether __ip_tunnel_change_mtu matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/ip_tunnels.h... yes
checking whether hashfn.*const matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/inet_frag.h... no
checking whether last_in matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/inet_frag.h... no
checking whether inet_frag_evicting matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/inet_frag.h... no
checking whether inet_frag_evictor matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/inet_frag.h... no
checking whether inet_frags has member frags_work in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/inet_frag.h... no
checking whether inet_frags has member rwlock in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/inet_frag.h... no
checking whether inet_frag_queue has member list_evictor in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/inet_frag.h... no
checking whether inet_frag_lru_move matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/inet_frag.h... no
checking whether sub_frag_mem_limit has parameter struct.netns_frags in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/inet_frag.h... no
checking whether void.*inet_frags_init matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/inet_frag.h... no
checking whether vif matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/inetpeer.h... yes
checking whether ip_tunnel_key has member label in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/ip_tunnels.h... yes
checking whether iptunnel_pull_offloads matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/ip_tunnels.h... yes
checking whether dst_cache matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/dst_cache.h... yes
checking whether erspan_md2 matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/erspan.h... yes
checking whether dst_cache matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/dst_cache.h... yes
checking whether mpls_hdr matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/mpls.h... yes
checking whether sock_create_kern.*net matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/net.h... yes
checking whether ndo_fill_metadata_dst matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... yes
checking whether dev_disable_lro matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... yes
checking whether dev_get_stats matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... yes
checking whether dev_get_by_index_rcu matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... yes
checking whether dev_recursion_level matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... yes
checking whether __skb_gso_segment matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... yes
checking whether skb_gso_error_unwind matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... yes
checking whether can_checksum_protocol matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... yes
checking whether ndo_get_iflink matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... yes
checking whether ndo_features_check matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... yes
checking whether ndo_add_vxlan_port matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... no
checking whether ndo_add_geneve_port matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... no
checking whether ndo_udp_tunnel_add matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... yes
checking whether netdev_features_t matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... yes
checking whether pcpu_sw_netstats.*tstats matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... yes
checking whether netif_needs_gso.*net_device matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... no
checking whether skb_csum_hwoffload_help matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... yes
checking whether udp_offload matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... no
checking whether udp_offload.*uoff matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... no
checking whether gro_remcsum matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... yes
checking whether IFF_PHONY_HEADROOM matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... yes
checking whether net_device_ops has member extended in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... no
checking whether netdev_master_upper_dev_link has parameter upper_priv in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... yes
checking whether netdev_master_upper_dev_link_rh matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... no
checking whether net_device has member max_mtu in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... yes
checking whether net_device_ops_extended has member ndo_change_mtu in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... no
checking whether dev_change_flags has parameter extack in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... yes
checking whether nf_hook_state matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netfilter.h... yes
checking whether nf_hook_state has member struct net  in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netfilter.h... yes
checking whether nf_register_net_hook matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netfilter.h... yes
checking whether nf_hookfn.*nf_hook_ops matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netfilter.h... no
checking whether nf_hookfn has parameter priv in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netfilter.h... yes
checking whether nf_hook_ops has member owner in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netfilter.h... no
checking whether NFPROTO_INET matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netfilter.h... no
checking whether CONFIG_NF_NAT_NEEDED matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netfilter.h... no
checking whether nf_ipv6_ops has member fragment.*sock in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netfilter_ipv6.h... yes
checking whether nf_conn has member struct timer_list[ \t]*timeout in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netfilter/nf_conntrack.h... no
checking whether nf_ct_delete( matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netfilter/nf_conntrack.h... yes
checking whether nf_ct_tmpl_alloc has parameter nf_conntrack_zone in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netfilter/nf_conntrack.h... yes
checking whether nf_ct_get_tuplepr has parameter struct.net in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netfilter/nf_conntrack.h... yes
checking whether nf_ct_set matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netfilter/nf_conntrack.h... yes
checking whether nf_ct_is_untracked matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netfilter/nf_conntrack.h... no
checking whether nf_ct_invert_tuplepr matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netfilter/nf_conntrack.h... no
checking whether nf_ct_zone_init matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netfilter/nf_conntrack_zones.h... yes
checking whether net_ns_get matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netfilter/nf_conntrack_l3proto.h... file not found
checking whether nf_connlabels_get matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netfilter/nf_conntrack_labels.h... yes
checking whether nf_connlabels_get has parameter int bit in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netfilter/nf_conntrack_labels.h... yes
checking whether nf_conn_labels has member words in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netfilter/nf_conntrack_labels.h... no
checking whether nf_ct_nat_ext_add matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netfilter/nf_nat.h... yes
checking whether nf_nat_alloc_null_binding matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netfilter/nf_nat.h... yes
checking whether nf_nat_range2 matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netfilter/nf_nat.h... yes
checking whether nf_nat_packet matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netfilter/nf_nat.h... yes
checking whether nf_ct_seq_adjust matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netfilter/nf_conntrack_seqadj.h... yes
checking whether nf_conncount_gc_list matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netfilter/nf_conntrack_count.h... yes
checking whether int nf_conncount_add matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netfilter/nf_conntrack_count.h... yes
checking whether nf_ct_set_timeout matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netfilter/nf_conntrack_timeout.h... yes
checking whether struct nf_ct_timeout matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netfilter/nf_conntrack_timeout.h... yes
checking whether \(*nf_ct_timeout_find_get_hook\) has parameter net in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netfilter/nf_conntrack_timeout.h... yes
checking whether prandom_u32[\(] matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/random.h... no
checking whether prandom_u32_max matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/random.h... no
checking whether prandom_u32[\(] matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/prandom.h... yes
checking whether prandom_u32_max matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/prandom.h... yes
checking whether get_link_net matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/rtnetlink.h... yes
checking whether name_assign_type matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/rtnetlink.h... yes
checking whether rtnl_create_link.*src_net matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/rtnetlink.h... no
checking whether possible_net_t matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/net_namespace.h... yes
checking whether rcu_read_lock_held matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/rcupdate.h... yes
checking whether lockdep_rtnl_is_held matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/rtnetlink.h... yes
checking whether net_rwsem matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/rtnetlink.h... yes
checking whether rtnl_create_link has parameter extack in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/rtnetlink.h... yes
checking whether nf_reset_ct matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether [^@]proto_data_valid matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... no
checking whether skb_checksum_start_offset matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether inner_protocol matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether inner_protocol_type matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether skb_inner_transport_offset matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether kfree_skb_list matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether rxhash matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... no
checking whether u16.*rxhash matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... no
checking whether skb_dst( matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether skb_copy_from_linear_data_offset matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether skb_reset_tail_pointer matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether skb_cow_head matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether skb_warn_if_lro matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether consume_skb matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether skb_frag_page matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether skb_has_frag_list matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether __skb_fill_page_desc matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether skb_reset_mac_len matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether skb_unclone matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether skb_orphan_frags matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether skb_get_hash( matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether skb_clear_hash matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether int.skb_zerocopy( matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether skb_ensure_writable matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether skb_vlan_pop matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether __skb_vlan_pop matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether skb_vlan_push matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether skb_clear_hash_if_not_l4 matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether skb_postpush_rcsum matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether lco_csum matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether skb_nfct matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether skb_put_zero matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether __wsum matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/types.h... no
checking whether __wsum matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/uapi/linux/types.h... yes
checking whether csum_replace4 matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/checksum.h... yes
checking whether csum_unfold matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/checksum.h... yes
checking whether dst_discard_sk matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/dst.h... no
checking whether __skb_dst_copy matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/dst.h... yes
checking whether genl_has_listeners matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/genetlink.h... yes
checking whether mcgrp_offset matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/genetlink.h... yes
checking whether parallel_ops matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/genetlink.h... yes
checking whether netlink_has_listeners(net->genl_sock matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/genetlink.h... yes
checking whether genlmsg_parse matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/genetlink.h... yes
checking whether genl_notify.*family matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/genetlink.h... yes
checking whether genl_validate_flags matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/genetlink.h... yes
checking whether genl_notify has parameter net in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/genetlink.h... no
checking whether genl_multicast_group has member id in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/genetlink.h... no
checking whether geneve_hdr matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/geneve.h... no
checking whether gre_cisco_register matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/gre.h... no
checking whether gre_handle_offloads matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/gre.h... no
checking whether IP6_FH_F_SKIP_RH matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/ipv6.h... yes
checking whether ip6_local_out_sk matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/ipv6.h... no
checking whether __ipv6_addr_jhash matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/ipv6.h... yes
checking whether rt6i.*u.dst matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/ip6_fib.h... no
checking whether ip6_frag.*sock matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/ip6_route.h... yes
checking whether nla_put_64bit matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netlink.h... yes
checking whether nla_get_be16 matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netlink.h... yes
checking whether nla_put_be16 matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netlink.h... yes
checking whether nla_put_be32 matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netlink.h... yes
checking whether nla_put_be64 matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netlink.h... yes
checking whether nla_put_in_addr matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netlink.h... yes
checking whether nla_find_nested matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netlink.h... yes
checking whether nla_is_last matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netlink.h... yes
checking whether nla_nest_start_noflag matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netlink.h... yes
checking whether void.*netlink_set_err matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netlink.h... no
checking whether nla_parse has parameter netlink_ext_ack in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netlink.h... yes
checking whether sctp_compute_cksum matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/sctp/checksum.h... yes
checking whether vlan_insert_tag_set_proto matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/if_vlan.h... yes
checking whether __vlan_insert_tag matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/if_vlan.h... yes
checking whether vlan_get_protocol matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/if_vlan.h... yes
checking whether skb_vlan_tagged matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/if_vlan.h... yes
checking whether eth_type_vlan matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/if_vlan.h... yes
checking whether metadata_dst_alloc has parameter metadata_type in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/dst_metadata.h... yes
checking whether u64_stats_fetch_begin_irq matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/u64_stats_sync.h... yes
checking whether struct vxlan_metadata matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/vxlan.h... yes
checking whether udp_flow_src_port matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/udp.h... yes
checking whether inet_get_local_port_range(net matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/udp.h... yes
checking whether udp_v4_check matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/udp.h... yes
checking whether udp_tunnel_gro_complete matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/udp_tunnel.h... yes
checking whether sk_buff.*udp_tunnel_handle_offloads matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/udp_tunnel.h... no
checking whether udp_tunnel_sock_cfg has member gro_receive in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/udp_tunnel.h... yes
checking whether ignore_df matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether NET_NAME_UNKNOWN matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/uapi/linux/netdevice.h... yes
checking whether sk_no_check_tx matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/sock.h... yes
checking whether no_check6_tx matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/udp.h... yes
checking whether udp_add_offload has parameter net in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/protocol.h... no
checking whether nf_defrag_ipv6_enable has parameter net in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netfilter/ipv6/nf_defrag_ipv6.h... yes
checking whether family_list matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/genetlink.h... no
checking whether net_device has member needs_free_netdev in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... yes
checking whether vxlan_dev has member cfg in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/vxlan.h... yes
checking whether nf_conntrack_helper_put matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netfilter/nf_conntrack_helper.h... yes
checking whether nf_nat_helper_try_module_get matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netfilter/nf_conntrack_helper.h... yes
checking whether nf_nat_helper_put matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netfilter/nf_conntrack_helper.h... yes
checking whether [[:space:]]SKB_GSO_UDP[[:space:]] matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether DST_NOCACHE matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/dst.h... no
checking whether rtnl_link_ops has member extack in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/rtnetlink.h... yes
checking whether nf_hook_ops has member list in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netfilter.h... no
checking whether IP_CT_UNTRACKED matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/uapi/linux/netfilter/nf_conntrack_common.h... yes
checking whether netdev_master_upper_dev_link has parameter extack in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... yes
checking whether __LINUX_COMPILER_TYPES_H matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/compiler_types.h... yes
checking whether ktime_get_ts64 matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/timekeeping.h... yes
checking whether EXPORT_SYMBOL_GPL(peernet2id_alloc) matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/net_namespace.h... no
checking whether ktime_get_ns matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/timekeeping.h... yes
checking whether frag_percpu_counter_batch matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/inet_frag.h... no
checking whether null_compute_pseudo matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether __skb_checksum_convert matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether net_device has member max_mtu in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... yes
checking whether __ip6_tnl_parm has member erspan_ver in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/ip6_tunnel.h... yes
checking whether SKB_GSO_IPXIP6 matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether ip6_make_flowlabel has parameter fl6 in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/ipv6.h... yes
checking whether netns_sysctl_ipv6 has member auto_flowlabels in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/ipv6.h... no
checking whether netif_keep_dst matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... yes
checking whether net_device_ops has member ndo_get_iflink in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... yes
checking whether skb_set_inner_ipproto matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether tunnel_encap_types matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/uapi/linux/if_tunnel.h... yes
checking whether IFLA_IPTUN_ENCAP_TYPE matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/uapi/linux/if_tunnel.h... yes
checking whether IFLA_IPTUN_COLLECT_METADATA matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/uapi/linux/if_tunnel.h... yes
checking whether IFLA_GRE_ENCAP_DPORT matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/uapi/linux/if_tunnel.h... yes
checking whether IFLA_GRE_COLLECT_METADATA matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/uapi/linux/if_tunnel.h... yes
checking whether IFLA_GRE_IGNORE_DF matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/uapi/linux/if_tunnel.h... yes
checking whether IFLA_GRE_FWMARK matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/uapi/linux/if_tunnel.h... yes
checking whether IFLA_GRE_ERSPAN_INDEX matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/uapi/linux/if_tunnel.h... yes
checking whether IFLA_GRE_ERSPAN_HWID matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/uapi/linux/if_tunnel.h... yes
checking whether IFLA_IPTUN_FWMARK matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/uapi/linux/if_tunnel.h... yes
checking whether sk_buff has member csum_valid in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether sk_buff has member vlan_present in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether skb_checksum_simple_validate matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether void.*ndo_get_stats64 matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/netdevice.h... yes
checking whether init_timer_deferrable matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/timer.h... no
checking whether ip_tunnel_info_opts_set has parameter flags in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/ip_tunnels.h... yes
checking whether inet_frags has member rnd in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/inet_frag.h... no
checking whether __LINUX_OVERFLOW_H matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/overflow.h... yes
checking whether struct_size matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/overflow.h... yes
checking whether kvmalloc_array matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/mm.h... yes
checking whether kvmalloc_node matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/mm.h... yes
checking whether nf_conntrack_l3proto matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netfilter/nf_conntrack_l3proto.h... file not found
checking whether nf_conntrack_in has parameter nf_hook_state in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netfilter/nf_conntrack_core.h... yes
checking whether IP6_DEFRAG_CONNTRACK_IN matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/ipv6_frag.h... yes
checking whether nf_ct_helper_ext_add has parameter nf_conntrack_helper in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netfilter/nf_conntrack_helper.h... no
checking whether gre_calc_hlen matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/gre.h... yes
checking whether ip_gre_calc_hlen matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/gre.h... no
checking whether rb_link_node_rcu matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/rbtree.h... yes
checking whether bool confirm_neigh matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/dst_ops.h... yes
checking whether fqdir matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/inet_frag.h... yes
checking whether genl_ops has member policy in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/genetlink.h... no
checking whether nla_parse_deprecated_strict matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/netlink.h... yes
checking whether validate has member extack in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/net/rtnetlink.h... yes
checking whether __skb_set_hash matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether sw_hash matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking whether skb_get_hash_raw matches in /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/linux/skbuff.h... yes
checking for struct tcf_t.firstuse... yes
checking whether dpdk is enabled... no
checking whether make supports nested variables... (cached) yes
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating lib/stdio.h
config.status: creating lib/string.h
config.status: creating ovsdb/libovsdb.sym
config.status: creating ofproto/libofproto.sym
config.status: creating lib/libsflow.sym
config.status: creating lib/libopenvswitch.sym
config.status: creating vtep/libvtep.sym
config.status: creating Makefile
config.status: creating datapath/Makefile
config.status: creating datapath/linux/Kbuild
config.status: creating datapath/linux/Makefile
config.status: creating datapath/linux/Makefile.main
config.status: creating tests/atlocal
config.status: creating lib/libopenvswitch.pc
config.status: creating lib/libsflow.pc
config.status: creating ofproto/libofproto.pc
config.status: creating ovsdb/libovsdb.pc
config.status: creating include/openvswitch/version.h
config.status: creating config.h
config.status: executing tests/atconfig commands
config.status: executing depfiles commands
config.status: executing libtool commands
config.status: executing include/openflow/openflow.h.stamp commands
config.status: executing utilities/bugtool/dummy commands
config.status: executing ipsec/dummy commands
configure: WARNING: unrecognized options: --disable-nls
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0'
sed -f ./build-aux/extract-odp-netlink-h < datapath/linux/compat/include/linux/openvswitch.h > include/odp-netlink.h
PYTHONPATH=./python":"$PYTHONPATH PYTHONDONTWRITEBYTECODE=yes /openwrt/staging_dir/hostpkg/bin/python3.9 ./ovsdb/ovsdb-idlc.in annotate ./vswitchd/vswitch.ovsschema ./lib/vswitch-idl.ann > lib/vswitch-idl.ovsidl.tmp && mv lib/vswitch-idl.ovsidl.tmp lib/vswitch-idl.ovsidl
PYTHONPATH=./python":"$PYTHONPATH PYTHONDONTWRITEBYTECODE=yes /openwrt/staging_dir/hostpkg/bin/python3.9 ./ovsdb/ovsdb-idlc.in annotate ./ovsdb/_server.ovsschema ./lib/ovsdb-server-idl.ann > lib/ovsdb-server-idl.ovsidl.tmp && mv lib/ovsdb-server-idl.ovsidl.tmp lib/ovsdb-server-idl.ovsidl
PYTHONPATH=./python":"$PYTHONPATH PYTHONDONTWRITEBYTECODE=yes /openwrt/staging_dir/hostpkg/bin/python3.9 ./ovsdb/ovsdb-idlc.in annotate ./vtep/vtep.ovsschema ./vtep/vtep-idl.ann > vtep/vtep-idl.ovsidl.tmp && \
mv vtep/vtep-idl.ovsidl.tmp vtep/vtep-idl.ovsidl
sh -f ./build-aux/extract-odp-netlink-macros-h include/odp-netlink.h > include/odp-netlink-macros.h
PYTHONPATH=./python":"$PYTHONPATH PYTHONDONTWRITEBYTECODE=yes /openwrt/staging_dir/hostpkg/bin/python3.9 ./ovsdb/ovsdb-idlc.in c-idl-source lib/vswitch-idl.ovsidl > lib/vswitch-idl.c.tmp && mv lib/vswitch-idl.c.tmp lib/vswitch-idl.c
PYTHONPATH=./python":"$PYTHONPATH PYTHONDONTWRITEBYTECODE=yes /openwrt/staging_dir/hostpkg/bin/python3.9 ./ovsdb/ovsdb-idlc.in c-idl-header lib/vswitch-idl.ovsidl > lib/vswitch-idl.h.tmp && mv lib/vswitch-idl.h.tmp lib/vswitch-idl.h
PYTHONPATH=./python":"$PYTHONPATH PYTHONDONTWRITEBYTECODE=yes /openwrt/staging_dir/hostpkg/bin/python3.9 ./ovsdb/ovsdb-idlc.in c-idl-source lib/ovsdb-server-idl.ovsidl > lib/ovsdb-server-idl.c.tmp && mv lib/ovsdb-server-idl.c.tmp lib/ovsdb-server-idl.c
PYTHONPATH=./python":"$PYTHONPATH PYTHONDONTWRITEBYTECODE=yes /openwrt/staging_dir/hostpkg/bin/python3.9 ./ovsdb/ovsdb-idlc.in c-idl-header lib/ovsdb-server-idl.ovsidl > lib/ovsdb-server-idl.h.tmp && mv lib/ovsdb-server-idl.h.tmp lib/ovsdb-server-idl.h
PYTHONPATH=./python":"$PYTHONPATH PYTHONDONTWRITEBYTECODE=yes /openwrt/staging_dir/hostpkg/bin/python3.9 ./ovsdb/ovsdb-idlc.in c-idl-source vtep/vtep-idl.ovsidl > vtep/vtep-idl.c.tmp && mv vtep/vtep-idl.c.tmp vtep/vtep-idl.c
PYTHONPATH=./python":"$PYTHONPATH PYTHONDONTWRITEBYTECODE=yes /openwrt/staging_dir/hostpkg/bin/python3.9 ./ovsdb/ovsdb-idlc.in c-idl-header vtep/vtep-idl.ovsidl > vtep/vtep-idl.h.tmp && mv vtep/vtep-idl.h.tmp vtep/vtep-idl.h
make  all-recursive
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0'
Making all in datapath
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath'
Making all in linux
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux'
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../actions.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../conntrack.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../datapath.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../dp_notify.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../flow.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../flow_netlink.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../flow_table.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../vport.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../vport-internal_dev.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../vport-netdev.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../nsh.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../meter.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/dev-openvswitch.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/dst_cache.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/exthdrs_core.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/geneve.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/gre.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/gso.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/genetlink-openvswitch.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/inet_fragment.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/ip_gre.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/ip_fragment.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/ip_output.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/ip_tunnel.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/ip_tunnels_core.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/ip6_output.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/ip6_gre.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/ip6_tunnel.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/lisp.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/netdevice.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/nf_conncount.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/nf_conntrack_core.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/nf_conntrack_proto.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/nf_conntrack_reasm.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/nf_conntrack_timeout.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/reciprocal_div.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/skbuff-openvswitch.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/socket.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/stt.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/udp.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/udp_tunnel.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/vxlan.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../linux/compat/utils.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../vport-geneve.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../vport-gre.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../vport-lisp.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../vport-stt.c 
ln -s /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/../vport-vxlan.c 
make -C /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124 KCFLAGS="-fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl=target-mips_24kc_musl" HOSTCFLAGS="-O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -Wall -Wmissing-prototypes -Wstrict-prototypes" CROSS_COMPILE="mips-openwrt-linux-musl-" ARCH="mips" KBUILD_HAVE_NLS=no KBUILD_BUILD_USER="" KBUILD_BUILD_HOST="" KBUILD_BUILD_TIMESTAMP="Sun Jun 20 08:51:56 2021" KBUILD_BUILD_VERSION="0" HOST_LOADLIBES="-L/openwrt/staging_dir/host/lib" KBUILD_HOSTLDLIBS="-L/openwrt/staging_dir/host/lib" CONFIG_SHELL="bash" V=''  cmd_syscalls= KBUILD_EXTRA_SYMBOLS="/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/symvers/netatop.symvers /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/symvers/cryptodev-linux.symvers /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/symvers/r8125.symvers /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/symvers/trelay.symvers /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/symvers/siit.symvers /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/symvers/r8152.symvers /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/symvers/exfat.symvers /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/symvers/gpio-button-hotplug.symvers /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/symvers/mtd-rw.symvers /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/symvers/button-hotplug.symvers /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/symvers/r8168.symvers /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/symvers/open-app-filter.symvers /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/symvers/nat46.symvers /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/symvers/antfs.symvers /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/symvers/gl-mifi-mcu.symvers" KERNELRELEASE=5.4.124 ARCH=mips M=/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux modules
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124'
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/actions.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/conntrack.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/datapath.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/dp_notify.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/flow.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/flow_netlink.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/flow_table.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/vport.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/vport-internal_dev.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/vport-netdev.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/nsh.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/meter.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/dev-openvswitch.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/dst_cache.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/exthdrs_core.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/geneve.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/gre.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/gso.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/genetlink-openvswitch.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/inet_fragment.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/ip_gre.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/ip_fragment.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/ip_output.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/ip_tunnel.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/ip_tunnels_core.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/ip6_output.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/ip6_gre.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/ip6_tunnel.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/lisp.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/netdevice.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/nf_conncount.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/nf_conntrack_core.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/nf_conntrack_proto.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/nf_conntrack_reasm.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/nf_conntrack_timeout.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/reciprocal_div.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/skbuff-openvswitch.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/socket.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/stt.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/udp.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/udp_tunnel.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/vxlan.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/utils.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/vport-geneve.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/vport-gre.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/vport-lisp.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/vport-stt.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/vport-vxlan.o
  LD [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/openvswitch.o
  Building modules, stage 2.
  MODPOST 6 modules
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/openvswitch.mod.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/vport-geneve.mod.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/vport-gre.mod.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/vport-lisp.mod.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/vport-stt.mod.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/vport-vxlan.mod.o
  LD [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/openvswitch.ko
  LD [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/vport-geneve.ko
  LD [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/vport-gre.ko
  LD [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/vport-lisp.ko
  LD [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/vport-stt.ko
  LD [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux/vport-vxlan.ko
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath/linux'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/datapath'
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0'
PYTHONPATH=./python":"$PYTHONPATH PYTHONDONTWRITEBYTECODE=yes /openwrt/staging_dir/hostpkg/bin/python3.9 build-aux/extract-ofp-fields meta-flow ./include/openvswitch/meta-flow.h > lib/meta-flow.inc.tmp
mv lib/meta-flow.inc.tmp lib/meta-flow.inc
depbase=`echo lib/multipath.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/bash ./libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I.    -I ./include -I ./include -I ./lib -I ./lib -I/usr/include -DNDEBUG -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -Wstrict-prototypes -Wall -Wextra -Wno-sign-compare -Wpointer-arith -Wformat -Wformat-security -Wswitch-enum -Wunused-parameter -Wbad-function-cast -Wcast-align -Wstrict-prototypes -Wold-style-definition -Wmissing-prototypes -Wmissing-field-initializers -fno-strict-aliasing -Wswitch-bool -Wlogical-not-parentheses -Wsizeof-array-argument -Wbool-compare -Wshift-negative-value -Wduplicated-cond -Wshadow -Wmultistatement-macros -Wcast-align=strict   -fomit-frame-pointer -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0=openvswitch-2.15.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto -std=gnu99  -MT lib/multipath.lo -MD -MP -MF $depbase.Tpo -c -o lib/multipath.lo lib/multipath.c &&\
mv -f $depbase.Tpo $depbase.Plo
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I ./include -I ./include -I ./lib -I ./lib -I/usr/include -DNDEBUG -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -Wstrict-prototypes -Wall -Wextra -Wno-sign-compare -Wpointer-arith -Wformat -Wformat-security -Wswitch-enum -Wunused-parameter -Wbad-function-cast -Wcast-align -Wstrict-prototypes -Wold-style-definition -Wmissing-prototypes -Wmissing-field-initializers -fno-strict-aliasing -Wswitch-bool -Wlogical-not-parentheses -Wsizeof-array-argument -Wbool-compare -Wshift-negative-value -Wduplicated-cond -Wshadow -Wmultistatement-macros -Wcast-align=strict -fomit-frame-pointer -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0=openvswitch-2.15.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto -std=gnu99 -MT lib/multipath.lo -MD -MP -MF lib/.deps/multipath.Tpo -c lib/multipath.c  -fPIC -DPIC -o lib/.libs/multipath.o
In file included from /usr/include/bits/local_lim.h:38,
                 from /usr/include/bits/posix1_lim.h:161,
                 from /usr/include/limits.h:183,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/usr/include/linux/limits.h:7: warning: "NGROUPS_MAX" redefined
 #define NGROUPS_MAX    65536 /* supplemental group IDs are available */
 
In file included from /usr/include/limits.h:124,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:46: note: this is the location of the previous definition
 #define NGROUPS_MAX 32
 
In file included from /usr/include/bits/posix1_lim.h:161,
                 from /usr/include/limits.h:183,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/usr/include/bits/local_lim.h:64: warning: "PTHREAD_KEYS_MAX" redefined
 #define PTHREAD_KEYS_MAX 1024
 
In file included from /usr/include/limits.h:124,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:58: note: this is the location of the previous definition
 #define PTHREAD_KEYS_MAX 128
 
In file included from /usr/include/bits/posix1_lim.h:161,
                 from /usr/include/limits.h:183,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/usr/include/bits/local_lim.h:69: warning: "PTHREAD_DESTRUCTOR_ITERATIONS" redefined
 #define PTHREAD_DESTRUCTOR_ITERATIONS _POSIX_THREAD_DESTRUCTOR_ITERATIONS
 
In file included from /usr/include/limits.h:124,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:60: note: this is the location of the previous definition
 #define PTHREAD_DESTRUCTOR_ITERATIONS 4
 
In file included from /usr/include/bits/posix1_lim.h:161,
                 from /usr/include/limits.h:183,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/usr/include/bits/local_lim.h:81: warning: "PTHREAD_STACK_MIN" redefined
 #define PTHREAD_STACK_MIN 16384
 
In file included from /usr/include/limits.h:124,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:59: note: this is the location of the previous definition
 #define PTHREAD_STACK_MIN 2048
 
In file included from /usr/include/bits/posix1_lim.h:161,
                 from /usr/include/limits.h:183,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/usr/include/bits/local_lim.h:84: warning: "DELAYTIMER_MAX" redefined
 #define DELAYTIMER_MAX 2147483647
 
In file included from /usr/include/limits.h:124,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:63: note: this is the location of the previous definition
 #define DELAYTIMER_MAX 0x7fffffff
 
In file included from /usr/include/bits/posix1_lim.h:161,
                 from /usr/include/limits.h:183,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/usr/include/bits/local_lim.h:93: warning: "HOST_NAME_MAX" redefined
 #define HOST_NAME_MAX  64
 
In file included from /usr/include/limits.h:124,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:54: note: this is the location of the previous definition
 #define HOST_NAME_MAX 255
 
In file included from /usr/include/bits/posix1_lim.h:161,
                 from /usr/include/limits.h:183,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/usr/include/bits/local_lim.h:99: warning: "SEM_VALUE_MAX" redefined
 #define SEM_VALUE_MAX   (2147483647)
 
In file included from /usr/include/limits.h:124,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:61: note: this is the location of the previous definition
 #define SEM_VALUE_MAX 0x7fffffff
 
In file included from /usr/include/limits.h:187,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/usr/include/bits/posix2_lim.h:88: warning: "RE_DUP_MAX" redefined
 #define RE_DUP_MAX (0x7fff)
 
In file included from /usr/include/limits.h:124,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:77: note: this is the location of the previous definition
 #define RE_DUP_MAX 255
 
In file included from /usr/include/limits.h:191,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/usr/include/bits/xopen_lim.h:62: warning: "_XOPEN_IOV_MAX" redefined
 #define _XOPEN_IOV_MAX _POSIX_UIO_MAXIOV
 
In file included from /usr/include/limits.h:124,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:154: note: this is the location of the previous definition
 #define _XOPEN_IOV_MAX          16
 
In file included from /usr/include/limits.h:191,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/usr/include/bits/xopen_lim.h:66: warning: "IOV_MAX" redefined
 # define IOV_MAX __IOV_MAX
 
In file included from /usr/include/limits.h:124,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:48: note: this is the location of the previous definition
 #define IOV_MAX 1024
 
In file included from /usr/include/limits.h:191,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/usr/include/bits/xopen_lim.h:73: warning: "NL_ARGMAX" redefined
 #define NL_ARGMAX _POSIX_ARG_MAX
 
In file included from /usr/include/limits.h:124,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:79: note: this is the location of the previous definition
 #define NL_ARGMAX 9
 
In file included from /usr/include/limits.h:191,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/usr/include/bits/xopen_lim.h:76: warning: "NL_LANGMAX" redefined
 #define NL_LANGMAX _POSIX2_LINE_MAX
 
In file included from /usr/include/limits.h:124,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:92: note: this is the location of the previous definition
 #define NL_LANGMAX 32
 
In file included from /usr/include/limits.h:191,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/usr/include/bits/xopen_lim.h:79: warning: "NL_MSGMAX" redefined
 #define NL_MSGMAX INT_MAX
 
In file included from /usr/include/limits.h:124,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:80: note: this is the location of the previous definition
 #define NL_MSGMAX 32767
 
In file included from /usr/include/limits.h:191,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/usr/include/bits/xopen_lim.h:84: warning: "NL_NMAX" redefined
 # define NL_NMAX INT_MAX
 
In file included from /usr/include/limits.h:124,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:99: note: this is the location of the previous definition
 #define NL_NMAX 16
 
In file included from /usr/include/limits.h:191,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/usr/include/bits/xopen_lim.h:88: warning: "NL_SETMAX" redefined
 #define NL_SETMAX INT_MAX
 
In file included from /usr/include/limits.h:124,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:81: note: this is the location of the previous definition
 #define NL_SETMAX 255
 
In file included from /usr/include/limits.h:191,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/usr/include/bits/xopen_lim.h:91: warning: "NL_TEXTMAX" redefined
 #define NL_TEXTMAX INT_MAX
 
In file included from /usr/include/limits.h:124,
                 from lib/bitmap.h:20,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:82: note: this is the location of the previous definition
 #define NL_TEXTMAX 2048
 
In file included from lib/bitmap.h:21,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/usr/include/stdlib.h:152:8: error: '_Float128' is not supported on this target
 extern _Float128 strtof128 (const char *__restrict __nptr,
        ^~~~~~~~~
/usr/include/stdlib.h:164:8: error: '_Float64x' is not supported on this target
 extern _Float64x strtof64x (const char *__restrict __nptr,
        ^~~~~~~~~
/usr/include/stdlib.h:245:4: error: '_Float128' is not supported on this target
    _Float128 __f)
    ^~~~~~~~~
/usr/include/stdlib.h:257:4: error: '_Float64x' is not supported on this target
    _Float64x __f)
    ^~~~~~~~~
/usr/include/stdlib.h:330:8: error: '_Float128' is not supported on this target
 extern _Float128 strtof128_l (const char *__restrict __nptr,
        ^~~~~~~~~
/usr/include/stdlib.h:344:8: error: '_Float64x' is not supported on this target
 extern _Float64x strtof64x_l (const char *__restrict __nptr,
        ^~~~~~~~~
In file included from /usr/include/stdlib.h:1017,
                 from lib/bitmap.h:21,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/usr/include/bits/stdlib.h: In function 'wctomb':
/usr/include/bits/stdlib.h:90:3: error: #error "Assumed value of MB_LEN_MAX wrong"
 # error "Assumed value of MB_LEN_MAX wrong"
   ^~~~~
In file included from ./lib/stdio.h:17,
                 from lib/util.h:26,
                 from lib/bitmap.h:22,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/usr/include/stdio.h: At top level:
/usr/include/stdio.h:52:9: error: unknown type name '__gnuc_va_list'
 typedef __gnuc_va_list va_list;
         ^~~~~~~~~~~~~~
/usr/include/stdio.h:52:24: error: conflicting types for 'va_list'
 typedef __gnuc_va_list va_list;
                        ^~~~~~~
In file included from /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/stdarg.h:10,
                 from lib/util.h:25,
                 from lib/bitmap.h:22,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/bits/alltypes.h:6:27: note: previous declaration of 'va_list' was here
 typedef __builtin_va_list va_list;
                           ^~~~~~~
In file included from ./lib/stdio.h:17,
                 from lib/util.h:26,
                 from lib/bitmap.h:22,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/usr/include/stdio.h:342:8: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
        __gnuc_va_list __arg);
        ^~~~~~~~~~~~~~
        va_list
/usr/include/stdio.h:347:54: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
 extern int vprintf (const char *__restrict __format, __gnuc_va_list __arg);
                                                      ^~~~~~~~~~~~~~
                                                      va_list
/usr/include/stdio.h:350:8: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
        __gnuc_va_list __arg) __THROWNL;
        ^~~~~~~~~~~~~~
        va_list
/usr/include/stdio.h:359:42: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
         const char *__restrict __format, __gnuc_va_list __arg)
                                          ^~~~~~~~~~~~~~
                                          va_list
/usr/include/stdio.h:367:9: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
         __gnuc_va_list __arg)
         ^~~~~~~~~~~~~~
         va_list
/usr/include/stdio.h:380:8: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
        __gnuc_va_list __arg)
        ^~~~~~~~~~~~~~
        va_list
/usr/include/stdio.h:433:7: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
       __gnuc_va_list __arg)
       ^~~~~~~~~~~~~~
       va_list
/usr/include/stdio.h:440:53: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
 extern int vscanf (const char *__restrict __format, __gnuc_va_list __arg)
                                                     ^~~~~~~~~~~~~~
                                                     va_list
/usr/include/stdio.h:445:40: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
       const char *__restrict __format, __gnuc_va_list __arg)
                                        ^~~~~~~~~~~~~~
                                        va_list
In file included from /usr/include/features.h:461,
                 from /usr/include/bits/libc-header-start.h:33,
                 from /usr/include/stdint.h:26,
                 from lib/multipath.h:20,
                 from lib/multipath.c:19:
/usr/include/stdio.h:453:37: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
    const char *__restrict __format, __gnuc_va_list __arg),
                                     ^~~~~~~~~~~~~~
/usr/include/sys/cdefs.h:174:46: note: in definition of macro '__REDIRECT'
 # define __REDIRECT(name, proto, alias) name proto __asm__ (__ASMNAME (#alias))
                                              ^~~~~
/usr/include/stdio.h:457:5: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
     __gnuc_va_list __arg), __isoc99_vscanf)
     ^~~~~~~~~~~~~~
/usr/include/sys/cdefs.h:174:46: note: in definition of macro '__REDIRECT'
 # define __REDIRECT(name, proto, alias) name proto __asm__ (__ASMNAME (#alias))
                                              ^~~~~
/usr/include/stdio.h:462:8: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
        __gnuc_va_list __arg), __isoc99_vsscanf)
        ^~~~~~~~~~~~~~
/usr/include/sys/cdefs.h:182:11: note: in definition of macro '__REDIRECT_NTH'
      name proto __asm__ (__ASMNAME (#alias)) __THROW
           ^~~~~
In file included from ./lib/stdio.h:17,
                 from lib/util.h:26,
                 from lib/bitmap.h:22,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/usr/include/stdio.h:831:8: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
        __gnuc_va_list __args)
        ^~~~~~~~~~~~~~
        va_list
In file included from /usr/include/stdio.h:867,
                 from ./lib/stdio.h:17,
                 from lib/util.h:26,
                 from lib/bitmap.h:22,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/usr/include/bits/stdio2.h:30:7: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
       __gnuc_va_list __ap) __THROW;
       ^~~~~~~~~~~~~~
       va_list
In file included from /usr/include/features.h:461,
                 from /usr/include/bits/libc-header-start.h:33,
                 from /usr/include/stdint.h:26,
                 from lib/multipath.h:20,
                 from lib/multipath.c:19:
/usr/include/bits/stdio2.h:47:4: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
    __gnuc_va_list __ap))
    ^~~~~~~~~~~~~~
/usr/include/sys/cdefs.h:57:59: note: in definition of macro '__NTH'
 #  define __NTH(fct) __attribute__ ((__nothrow__ __LEAF)) fct
                                                           ^~~
In file included from /usr/include/stdio.h:867,
                 from ./lib/stdio.h:17,
                 from lib/util.h:26,
                 from lib/bitmap.h:22,
                 from lib/flow.h:25,
                 from lib/nx-match.h:24,
                 from lib/multipath.c:25:
/usr/include/bits/stdio2.h:60:8: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
        __gnuc_va_list __ap) __THROW;
        ^~~~~~~~~~~~~~
        va_list
In file included from /usr/include/features.h:461,
                 from /usr/include/bits/libc-header-start.h:33,
                 from /usr/include/stdint.h:26,
                 from lib/multipath.h:20,
                 from lib/multipath.c:19:
/usr/include/bits/stdio2.h:78:35: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
     const char *__restrict __fmt, __gnuc_va_list __ap))
                                   ^~~~~~~~~~~~~~
/usr/include/sys/cdefs.h:57:59: note: in definition of macro '__NTH'
 #  define __NTH(fct) __attribute__ ((__nothrow__ __LEAF)) fct
                                                           ^~~
make[6]: *** [Makefile:3395: lib/multipath.lo] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0'
make[5]: *** [Makefile:4129: all-recursive] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0'
make[4]: *** [Makefile:2108: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0'
make[3]: *** [Makefile:273: /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/.built] Error 2
```
