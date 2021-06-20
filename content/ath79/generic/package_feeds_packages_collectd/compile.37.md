---
title: "compile.37"
date: 2021-06-20 22:32:33.849322
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
make package/feeds/packages/collectd/compile -j$(nproc) || make package/feeds/packages/collectd/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-undefined-AM_PATH_LIBGCRYPT.patch using plaintext: 
patching file fake-am_path_libgcrypt.m4

Applying ./patches/100-rrdtool-add-rrasingle-option.patch using plaintext: 
patching file src/rrdtool.c
patching file src/utils/rrdcreate/rrdcreate.c
patching file src/utils/rrdcreate/rrdcreate.h

Applying ./patches/140-fix-fqdnlookup.patch using plaintext: 
patching file src/daemon/configfile.c

Applying ./patches/300-delay-first-read-cycle.patch using plaintext: 
patching file src/daemon/plugin.c

Applying ./patches/320-reaction-to-ntp-time-change-at-boot.patch using plaintext: 
patching file src/daemon/collectd.c
patching file src/daemon/plugin.c

Applying ./patches/400-fix-olsrd-get-all.patch using plaintext: 
patching file src/olsrd.c

Applying ./patches/600-fix-libmodbus-detection.patch using plaintext: 
patching file configure.ac
patching file src/modbus.c

Applying ./patches/700-disable-sys-capability-check.patch using plaintext: 
patching file configure.ac

Applying ./patches/900-add-iwinfo-plugin.patch using plaintext: 
patching file configure.ac
patching file src/collectd.conf.in
patching file src/collectd.conf.pod
patching file src/iwinfo.c
patching file src/types.db
patching file Makefile.am

Applying ./patches/910-add-cake-qdisc-types.patch using plaintext: 
patching file src/types.db

Applying ./patches/920-backport-netlink-reg-noerror.patch using plaintext: 
patching file src/netlink.c

Applying ./patches/930-dhcpleases-add-dhcpleases-plugin.patch using plaintext: 
patching file Makefile.am
patching file README
patching file configure.ac
patching file src/collectd.conf.in
patching file src/dhcpleases.c

Applying ./patches/931-snmp6-add-ipv6-statistics.patch using plaintext: 
patching file Makefile.am
patching file README
patching file configure.ac
patching file src/collectd.conf.in
patching file src/snmp6.c
patching file src/types.db

Applying ./patches/932-add-ipstatistics.patch using plaintext: 
patching file src/ipstatistics.c
patching file src/types.db
patching file Makefile.am
patching file configure.ac
patching file src/collectd.conf.in

Applying ./patches/933-fix-smart-detection.patch using plaintext: 
patching file src/smart.c

Applying ./patches/934-ubi-prepare-read-for-percent.patch using plaintext: 
patching file src/ubi.c

Applying ./patches/935-ubi-add-percent.patch using plaintext: 
patching file src/ubi.c
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
configure: WARNING: unrecognized options: --disable-nls, --disable-ampq1, --disable-curl_jolokia, --disable-genericjmx, --disable-lvm, --disable-monitorus, --disable-openvz, --with-libnetlink
configure: loading site script /openwrt/include/site/mips
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking how to print strings... printf
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
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
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
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for mips-openwrt-linux-ranlib... mips-openwrt-linux-musl-gcc-ranlib
checking for gawk... gawk
checking command to parse mips-openwrt-linux-musl-gcc-nm output from ccache_cc object... ok
checking for sysroot... no
checking for mips-openwrt-linux-mt... no
checking for mt... no
checking if : is a manifest tool... no
checking how to run the C preprocessor... ccache_cc -E
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
checking for shl_load... no
checking for shl_load in -ldld... no
checking for dlopen... yes
checking whether a program can dlopen itself... cross
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... no
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... (cached) mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking whether make sets $(MAKE)... yes
checking for style of include used by make... GNU
checking whether make supports nested variables... yes
checking how to create a pax tar archive... gnutar
checking dependency style of ccache_cc... gcc3
checking whether make supports nested variables... (cached) yes
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking for ccache_cc option to accept ISO C99... none needed
checking for C compiler vendor... gnu
checking whether we are using the GNU C++ compiler... yes
checking whether ccache_cxx accepts -g... yes
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
checking dependency style of ccache_cxx... gcc3
checking how to run the C preprocessor... ccache_cc -E
checking for egrep... (cached) /openwrt/staging_dir/host/bin/grep -E
checking whether ln -s works... yes
checking whether make sets $(MAKE)... (cached) yes
checking for flex... flex
checking lex output file root... lex.yy
checking lex library... none needed
checking whether yytext is a pointer... no
checking for bison... bison -y
checking for valgrind... no
checking pkg-config is at least version 0.9.0... yes
checking if Bison is the parser generator... yes
checking for kernel type (linux-gnu)... Linux
checking for sys/wait.h that is POSIX.1 compatible... yes
checking for dirent.h that defines DIR... yes
checking for library containing opendir... none required
checking for arpa/inet.h... yes
checking for endian.h... yes
checking for fcntl.h... yes
checking for fnmatch.h... yes
checking for fs_info.h... no
checking for fshelp.h... no
checking for grp.h... yes
checking for kstat.h... no
checking for kvm.h... no
checking for libgen.h... yes
checking for locale.h... yes
checking for mntent.h... yes
checking for mnttab.h... no
checking for netdb.h... yes
checking for paths.h... yes
checking for poll.h... yes
checking for pthread_np.h... no
checking for pwd.h... yes
checking for regex.h... yes
checking for sys/endian.h... no
checking for sys/fs_types.h... no
checking for sys/fstyp.h... no
checking for sys/ioctl.h... yes
checking for sys/isa_defs.h... no
checking for sys/mntent.h... no
checking for sys/mnttab.h... no
checking for sys/param.h... yes
checking for sys/resource.h... yes
checking for sys/select.h... yes
checking for sys/socket.h... yes
checking for sys/statfs.h... yes
checking for sys/statvfs.h... yes
checking for sys/types.h... (cached) yes
checking for sys/un.h... yes
checking for sys/vfs.h... yes
checking for sys/vfstab.h... no
checking for sys/vmmeter.h... no
checking for syslog.h... yes
checking for wordexp.h... yes
checking for linux/ip_vs.h... yes
checking for netinet/in_systm.h... yes
checking for netinet/in.h... yes
checking for netinet/ip.h... yes
checking for netinet/ip_icmp.h... yes
checking for netinet/ip_var.h... no
checking for netinet/ip6.h... yes
checking for netinet/icmp6.h... yes
checking for netinet/tcp.h... yes
checking for netinet/udp.h... yes
checking sys/dkstat.h usability... no
checking sys/dkstat.h presence... no
checking for sys/dkstat.h... no
checking for sys/sysctl.h... no
checking ifaddrs.h usability... yes
checking ifaddrs.h presence... yes
checking for ifaddrs.h... yes
checking for net/if.h... yes
checking linux/major.h usability... yes
checking linux/major.h presence... yes
checking for linux/major.h... yes
checking for linux/raid/md_u.h... yes
checking sys/sysmacros.h usability... yes
checking sys/sysmacros.h presence... yes
checking for sys/sysmacros.h... yes
checking for linux/wireless.h... yes
checking for linux/if.h... yes
checking for linux/inet_diag.h... yes
checking for linux/netdevice.h... yes
checking for linux/sockios.h... yes
checking for linux/ethtool.h... yes
checking for linux/un.h... yes
checking cpuid.h usability... no
checking cpuid.h presence... no
checking for cpuid.h... no
checking linux/pci_regs.h usability... yes
checking linux/pci_regs.h presence... yes
checking for linux/pci_regs.h... yes
checking for sys/swap.h... yes
checking for vm/anon.h... no
checking sys/loadavg.h usability... no
checking sys/loadavg.h presence... no
checking for sys/loadavg.h... no
checking linux/config.h usability... no
checking linux/config.h presence... no
checking for linux/config.h... no
checking utmp.h usability... yes
checking utmp.h presence... yes
checking for utmp.h... yes
checking utmpx.h usability... yes
checking utmpx.h presence... yes
checking for utmpx.h... yes
checking for sys/ucred.h... no
checking for sys/mount.h... yes
checking for xfs/xqm.h... no
checking for net/if_arp.h... yes
checking net/ppp_defs.h usability... no
checking net/ppp_defs.h presence... no
checking for net/ppp_defs.h... no
checking for net/if_ppp.h... no
checking for netinet/if_ether.h... yes
checking for net/pfvar.h... no
checking termios.h usability... yes
checking termios.h presence... yes
checking for termios.h... yes
checking whether clock_boottime and clock_monotonic are supported... yes
checking for iwinfo_backend in -liwinfo... yes
checking for an ANSI C-conforming const... yes
checking for pid_t... yes
checking for size_t... yes
checking for uid_t in sys/types.h... yes
checking whether time.h and sys/time.h may both be included... yes
checking for asprintf... yes
checking for execvpe... yes
checking for getpwnam... yes
checking for getpwnam_r... yes
checking for if_indextoname... yes
checking for setgroups... yes
checking for setlocale... (cached) yes
checking whether strerror_r is declared... yes
checking for strerror_r... yes
checking whether strerror_r returns char *... no
checking for strtok_r... yes
checking for socket... yes
checking for inet_ntop... yes
checking for clock_gettime... yes
checking for nanosleep... yes
checking for getifaddrs... yes
checking for getloadavg... yes
checking for getutent... yes
checking for getutxent... yes
checking for host_statistics... no
checking for processor_info... no
checking for statfs... yes
checking for statvfs... yes
checking for sysctl... no
checking for sysctlbyname... no
checking for syslog... yes
checking for thread_info... no
checking for strptime... yes
checking whether strptime is exported by default... yes
checking for timegm... yes
checking for sysctl kern.cp_times... no
checking for sysctl kern.cp_time... no
checking for swapctl... no
checking whether clock_boottime and clock_monotonic are supported... (cached) yes
checking for getfsstat... no
checking for getvfsstat... no
checking for listmntent... no
checking for getmntent_r... yes
checking for getmntent... yes
checking whether getmntent takes one argument... yes
checking whether getmntent takes two arguments... no
checking whether htonll is defined... no
checking for struct if_data.ifi_ibytes... no
checking for struct if_data.ifi_opackets... no
checking for struct if_data.ifi_ierrors... no
checking for struct net_device_stats.rx_bytes... no
checking for struct net_device_stats.tx_packets... no
checking for struct net_device_stats.rx_errors... no
checking for struct inet_diag_req.id... yes
checking for struct inet_diag_req.idiag_states... yes
checking for struct ip_mreqn.imr_ifindex... yes
checking for struct kinfo_proc.ki_pid... no
checking for struct kinfo_proc.ki_rssize... no
checking for struct kinfo_proc.ki_rusage... no
checking for struct kinfo_proc.p_pid... no
checking for struct kinfo_proc.p_vm_rssize... no
checking for struct kinfo_proc2.p_pid... no
checking for struct kinfo_proc2.p_uru_maxrss... no
checking for struct udphdr.uh_dport... yes
checking for struct udphdr.uh_sport... yes
checking for struct udphdr.dest... no
checking for struct udphdr.source... no
checking for kstat_io_t.nwritten... no
checking for kstat_io_t.writes... no
checking for kstat_io_t.nwrites... no
checking for kstat_io_t.wtime... no
checking for pthread_setname_np... yes
checking for pthread_set_name_np... no
checking for struct ip6_ext... yes
checking i2c/smbus.h usability... no
checking i2c/smbus.h presence... no
checking for i2c/smbus.h... no
checking whether i2c_smbus_read_i2c_block_data is declared... no
checking for pthread_create in -lpthread... yes
checking pthread.h usability... yes
checking pthread.h presence... yes
checking for pthread.h... yes
checking for kvm_getprocs in -lkvm... no
checking for kvm_getswapinfo in -lkvm... no
checking for kvm_nlist in -lkvm... no
checking for kvm_openfiles in -lkvm... no
checking libaquaero5.h usability... no
checking libaquaero5.h presence... no
checking for libaquaero5.h... no
checking hiredis/hiredis.h usability... yes
checking hiredis/hiredis.h presence... yes
checking for hiredis/hiredis.h... yes
checking for redisCommand in -lhiredis... yes
checking redfish.h usability... no
checking redfish.h presence... no
checking for redfish.h... no
checking dbi/dbi.h usability... yes
checking dbi/dbi.h presence... yes
checking for dbi/dbi.h... yes
checking for dbi_initialize in -ldbi... yes
checking for DPDK... no
configure: no DPDK pkg-config, using defaults
checking rte_config.h usability... no
checking rte_config.h presence... no
checking for rte_config.h... no
checking libesmtp.h usability... no
checking libesmtp.h presence... no
checking for libesmtp.h... no
checking gm_protocol.h usability... no
checking gm_protocol.h presence... no
checking for gm_protocol.h... no
checking gps.h usability... no
checking gps.h presence... no
checking for gps.h... no
checking for GRPCPP... no
checking whether ccache_cxx accepts -std=c++11... yes
checking for grpc_cpp_plugin... no
checking libiptc/libiptc.h usability... yes
checking libiptc/libiptc.h presence... yes
checking for libiptc/libiptc.h... yes
checking libiptc/libip6tc.h usability... yes
checking libiptc/libip6tc.h presence... yes
checking for libiptc/libip6tc.h... yes
checking for iptc_handle_t... no
checking for ip6tc_handle_t... no
checking for library containing iptc_init... -lip4tc
checking for jni.h... not found
checking for jni_md.h... not found
checking for libjvm.so... found in /usr/lib/jvm/default-java/lib/server
checking for javac... not found
checking for jar... not found
checking for javac... no
checking for jar... no
checking ldap.h usability... yes
checking ldap.h presence... yes
checking for ldap.h... yes
checking for ldap_initialize in -lldap... yes
checking for LUA... yes
checking lua.h usability... yes
checking lua.h presence... yes
checking for lua.h... yes
checking lauxlib.h usability... yes
checking lauxlib.h presence... yes
checking for lauxlib.h... yes
checking lualib.h usability... yes
checking lualib.h presence... yes
checking for lualib.h... yes
checking for lua_settop... yes
checking libmemcached/memcached.h usability... no
checking libmemcached/memcached.h presence... no
checking for libmemcached/memcached.h... no
checking for MICROHTTPD... yes
checking microhttpd.h usability... yes
checking microhttpd.h presence... yes
checking for microhttpd.h... yes
checking for MHD_start_daemon in -lmicrohttpd... yes
configure: Not checking for libmodbus: Manually configured
checking modbus/modbus.h usability... yes
checking modbus/modbus.h presence... yes
checking for modbus/modbus.h... yes
checking for modbus_connect in -lmodbus... yes
checking for LIBMONGOC... no
checking mosquitto.h usability... no
checking mosquitto.h presence... no
checking for mosquitto.h... no
checking for libmnl.h... no
checking for libmnl/libmnl.h... yes
checking for linux/gen_stats.h... yes
checking for linux/pkt_sched.h... yes
checking for struct rtnl_link_stats64.tx_window_errors... yes
checking for struct rtnl_link_stats.rx_nohandler... yes
checking for struct rtnl_link_stats64.rx_nohandler... yes
checking whether IFLA_VF_STATS_RX_DROPPED is declared... yes
checking whether IFLA_VF_STATS_TX_DROPPED is declared... yes
checking whether IFLA_VF_STATS is declared... yes
checking for mnl_nlmsg_get_payload in -lmnl... yes
checking netapp_api.h usability... no
checking netapp_api.h presence... no
checking for netapp_api.h... no
checking net-snmp/net-snmp-config.h usability... yes
checking net-snmp/net-snmp-config.h presence... yes
checking for net-snmp/net-snmp-config.h... yes
checking for net-snmp/net-snmp-includes.h... yes
checking for init_snmp in -lnetsnmp... yes
checking for netsnmp_get_version in -lnetsnmp... yes
checking whether netsnmp library has old API... no
checking for net-snmp/agent/net-snmp-agent-includes.h... yes
checking for netsnmp_init_helpers in -lnetsnmphelpers... no
checking for init_agent in -lnetsnmpagent... yes
checking for get_tree in -lnetsnmp... yes
checking oping.h usability... yes
checking oping.h presence... yes
checking for oping.h... yes
checking for ping_construct in -loping... yes
checking owcapi.h usability... no
checking owcapi.h presence... no
checking for owcapi.h... no
checking pcap.h usability... yes
checking pcap.h presence... yes
checking for pcap.h... yes
checking for pcap_open_live in -lpcap... yes
checking whether libpcap has PCAP_ERROR_IFACE_NOT_UP... yes
checking for perl... /openwrt/staging_dir/host/bin/perl
checking for libperl... no
checking pmw_api.h usability... no
checking pmw_api.h presence... no
checking for pmw_api.h... no
checking libpq-fe.h usability... yes
checking libpq-fe.h presence... yes
checking for libpq-fe.h... yes
checking for PQserverVersion in -lpq... yes
checking pqos.h usability... no
checking pqos.h presence... no
checking for pqos.h... no
checking jansson.h usability... yes
checking jansson.h presence... yes
checking for jansson.h... yes
checking for json_loads in -ljansson... yes
checking jevents.h usability... no
checking jevents.h presence... no
checking for jevents.h... no
checking for PROTOBUF... yes
checking for main in -lprotobuf... yes
checking google/protobuf/util/time_util.h usability... yes
checking google/protobuf/util/time_util.h presence... yes
checking for google/protobuf/util/time_util.h... yes
checking for protoc... /openwrt/staging_dir/hostpkg/bin/protoc
checking for protoc 3.0.0+... yes (libprotoc 3.17.2)
checking for PROTOBUF_C... yes
checking for protobuf_c_message_pack in -lprotobuf-c... yes
checking protobuf-c/protobuf-c.h usability... yes
checking protobuf-c/protobuf-c.h presence... yes
checking for protobuf-c/protobuf-c.h... yes
checking for protoc-c... no
checking for python3-config... /openwrt/staging_dir/hostpkg/bin/python3-config
checking Python.h usability... no
checking Python.h presence... no
checking for Python.h... no
checking proton/proactor.h usability... no
checking proton/proactor.h presence... no
checking for proton/proactor.h... no
checking amqp.h usability... no
checking amqp.h presence... no
checking for amqp.h... no
checking librdkafka/rdkafka.h usability... no
checking librdkafka/rdkafka.h presence... no
checking for librdkafka/rdkafka.h... no
checking routeros_api.h usability... yes
checking routeros_api.h presence... yes
checking for routeros_api.h... yes
checking for ros_interface in -lrouteros... yes
checking for RRD... no
checking rrd.h usability... yes
checking rrd.h presence... yes
checking for rrd.h... yes
checking for rrd_update_r in -lrrd_th... no
checking for rrd_update in -lrrd... yes
checking for rrdc_update in -lrrd... no
checking sensors/sensors.h usability... yes
checking sensors/sensors.h presence... yes
checking for sensors/sensors.h... yes
checking for sensors_init in -lsensors... yes
checking for LIBSIGROK... no
checking openssl/sha.h usability... no
checking openssl/sha.h presence... no
checking for openssl/sha.h... no
checking openssl/blowfish.h usability... no
checking openssl/blowfish.h presence... no
checking for openssl/blowfish.h... no
checking openssl/rand.h usability... no
checking openssl/rand.h presence... no
checking for openssl/rand.h... no
checking pkg-config for libstatgrab... not found
checking tcrdb.h usability... no
checking tcrdb.h presence... no
checking for tcrdb.h... no
checking libudev.h usability... yes
checking libudev.h presence... yes
checking for libudev.h... yes
checking for udev_new in -ludev... yes
checking xenctrl.h usability... no
checking xenctrl.h presence... no
checking for xenctrl.h... no
checking MicAccessApi.h usability... no
checking MicAccessApi.h presence... no
checking for MicAccessApi.h... no
checking libxml/parser.h usability... yes
checking libxml/parser.h presence... yes
checking for libxml/parser.h... yes
checking for xmlXPathEval in -lxml2... yes
checking for libOpenIPMIpthread... no (pkg-config doesn't know OpenIPMIpthread)
checking atasmart.h usability... yes
checking atasmart.h presence... yes
checking for atasmart.h... yes
checking for sk_disk_open in -latasmart... yes
checking for LIBNOTIFY... no
checking for LIBRIEMANN_CLIENT... no
configure: Checking for libslurm using /openwrt/staging_dir/host/bin/pkg-config
checking which default log plugin to load... syslog
checking which default write plugin to load... rrdtool
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating src/libcollectdclient/collectd/lcc_features.h
config.status: creating Makefile
config.status: creating src/collectd.conf
config.status: creating src/libcollectdclient/libcollectdclient.pc
config.status: creating src/config.h
config.status: executing libtool commands
config.status: executing depfiles commands
configure: WARNING: unrecognized options: --disable-nls, --disable-ampq1, --disable-curl_jolokia, --disable-genericjmx, --disable-lvm, --disable-monitorus, --disable-openvz, --with-libnetlink

Configuration:
  Build:
    Platform  . . . . . . Linux
    Compiler vendor . . . gnu
    CC  . . . . . . . . . ccache_cc
    CFLAGS  . . . . . . . -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/collectd-5.12.0=collectd-5.12.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -DPIC -fpic
    CXXFLAGS  . . . . . . -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/collectd-5.12.0=collectd-5.12.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include 
    CPP . . . . . . . . . ccache_cc -E
    CPPFLAGS  . . . . . . -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/libxml2
    GRPC_CPP_PLUGIN . . . 
    LD  . . . . . . . . . mips-openwrt-linux-musl-ld
    LDFLAGS . . . . . . . -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -lm -lz -llua
    PROTOC  . . . . . . . /openwrt/staging_dir/hostpkg/bin/protoc
    YACC  . . . . . . . . bison -y
    YFLAGS  . . . . . . . 

  Libraries:
    intel mic . . . . . . no (MicAccessApi not found)
    libaquaero5 . . . . . no (libaquaero5.h not found)
    libatasmart . . . . . yes
    libcurl . . . . . . . no (curl-config failed)
    libdbi  . . . . . . . yes
    libdpdk . . . . . . . no (rte_config.h not found)
    libesmtp  . . . . . . no (libesmtp.h not found)
    libganglia  . . . . . no (gm_protocol.h not found)
    libgcrypt . . . . . . no
    libgps  . . . . . . . no (gps.h not found)
    libgrpc++ . . . . . . no (pkg-config could not find libgrpc++)
    libhiredis  . . . . . yes
    libi2c-dev  . . . . . no (symbol i2c_smbus_read_i2c_block_data not found - have you installed libi2c-dev ?)
    libiokit  . . . . . . no
    libiptc . . . . . . . yes
    libjansson  . . . . . yes
    libjevents  . . . . . no (jevents.h not found)
    libjvm  . . . . . . . no (jar not found)
    libkstat  . . . . . . no (Solaris only)
    libkvm  . . . . . . . no
    libldap . . . . . . . yes
    liblua  . . . . . . . yes
    libmemcached  . . . . no (libmemcached/memcached.h not found)
    libmicrohttpd . . . . yes
    libmnl  . . . . . . . yes
    libmodbus . . . . . . yes
    libmongoc . . . . . . no (pkg-config could not find libmongoc)
    libmosquitto  . . . . no (mosquitto.h not found)
    libmysql  . . . . . . no (mysql_config failed)
    libnetapp . . . . . . no (netapp_api.h not found)
    libnetsnmp  . . . . . yes
    libnetsnmpagent . . . yes
    libnotify . . . . . . no (pkg-config doesn't know libnotify)
    libnvidia-ml  . . . . no
    libopenipmi . . . . . no (pkg-config doesn't know OpenIPMIpthread)
    liboping  . . . . . . yes
    libowcapi . . . . . . no (owcapi.h not found)
    libpcap . . . . . . . yes
    libperfstat . . . . . no (AIX only)
    libperl . . . . . . . no
    libpmwapi . . . . . . no (pmw_api.h not found)
    libpq . . . . . . . . yes
    libpqos . . . . . . . no (pqos.h not found)
    libprotobuf . . . . . yes
    libprotobuf-c . . . . yes
    libpython . . . . . . no
    libqpid-proton .  . . no (proton/proactor.h not found)
    librabbitmq . . . . . no (amqp.h not found)
    libriemann-client . . no (pkg-config doesn't know libriemann-client)
    librdkafka  . . . . . no (librdkafka/rdkafka.h not found)
    librouteros . . . . . yes
    librrd  . . . . . . . yes (warning: librrd is not thread-safe)
    libsensors  . . . . . yes
    libsigrok   . . . . . no (pkg-config could not find libsigrok)
    libssl  . . . . . . . no (ssl header not found)
    libslurm .  . . . . . no (pkg-config doesn't know libslurm)
    libstatgrab . . . . . no (pkg-config doesn't know libstatgrab)
    libtokyotyrant  . . . no (tcrdb.h not found)
    libudev . . . . . . . yes
    libupsclient  . . . . no (pkg-config doesn't know libupsclient)
    libvarnish  . . . . . no (pkg-config doesn't know varnishapi)
    libvirt . . . . . . . no (pkg-config doesn't know libvirt)
    libxenctrl  . . . . . no (xenctrl.h not found)
    libxml2 . . . . . . . yes
    libxmms . . . . . . . no
    libyajl . . . . . . . no
    oracle  . . . . . . . no (ORACLE_HOME is not set)
    protobuf-c  . . . . . no (protoc-c compiler not found)
    protoc 3  . . . . . . yes
    iwinfo  . . . . . . . yes

  Features:
    daemon mode . . . . . yes
    debug . . . . . . . . no

  Bindings:
    perl  . . . . . . . . no

  Modules:
    aggregation . . . . . yes
    amqp    . . . . . . . no (disabled on command line)
    amqp1   . . . . . . . no (proton/proactor.h not found)
    apache  . . . . . . . no (curl-config failed) (dependency error)
    apcups  . . . . . . . yes
    apple_sensors . . . . no (disabled on command line)
    aquaero . . . . . . . no (disabled on command line)
    ascent  . . . . . . . no (dependency error)
    barometer . . . . . . no (disabled on command line)
    battery . . . . . . . no (disabled on command line)
    bind  . . . . . . . . no (dependency error)
    buddyinfo . . . . . . no (disabled on command line)
    capabilities  . . . . no (disabled on command line)
    ceph  . . . . . . . . no (disabled on command line)
    cgroups . . . . . . . no (disabled on command line)
    chrony. . . . . . . . yes
    check_uptime. . . . . yes
    connectivity. . . . . no
    conntrack . . . . . . yes
    contextswitch . . . . yes
    cpu . . . . . . . . . yes
    cpufreq . . . . . . . no (disabled on command line)
    cpusleep  . . . . . . no (disabled on command line)
    csv . . . . . . . . . yes
    curl  . . . . . . . . no (curl-config failed) (dependency error)
    curl_json . . . . . . no (disabled on command line)
    curl_xml  . . . . . . no (disabled on command line)
    dbi . . . . . . . . . no (disabled on command line)
    dcpmm  . . . . . .  . no (disabled on command line)
    df  . . . . . . . . . yes
    dhcpleases. . . . . . yes
    disk  . . . . . . . . yes
    dns . . . . . . . . . yes
    dpdkevents. . . . . . no (disabled on command line)
    dpdkstat  . . . . . . no (disabled on command line)
    dpdk_telemetry. . . . no (disabled on command line)
    drbd  . . . . . . . . no (disabled on command line)
    email . . . . . . . . yes
    entropy . . . . . . . yes
    ethstat . . . . . . . yes
    exec  . . . . . . . . yes
    fhcount . . . . . . . no (disabled on command line)
    filecount . . . . . . yes
    fscache . . . . . . . yes
    gmond . . . . . . . . no (disabled on command line)
    gps . . . . . . . . . no (disabled on command line)
    gpu_nvidia  . . . . . no (disabled on command line)
    grpc  . . . . . . . . no (disabled on command line)
    hddtemp . . . . . . . no (disabled on command line)
    hugepages . . . . . . no (disabled on command line)
    infiniband  . . . . . no (disabled on command line)
    intel_pmu . . . . . . no (disabled on command line)
    intel_rdt . . . . . . no (disabled on command line)
    interface . . . . . . yes
    ipc . . . . . . . . . no (disabled on command line)
    ipmi  . . . . . . . . no (disabled on command line)
    iptables  . . . . . . yes
    ipstats . . . . . . . no (disabled on command line)
    ipstatistics  . . . . yes
    ipvs  . . . . . . . . no (disabled on command line)
    irq . . . . . . . . . yes
    iwinfo  . . . . . . . yes
    java  . . . . . . . . no (disabled on command line)
    load  . . . . . . . . yes
    logfile . . . . . . . yes
    logparser . . . . . . no (disabled on command line)
    log_logstash  . . . . no (disabled on command line)
    lpar  . . . . . . . . no (disabled on command line)
    lua . . . . . . . . . yes
    madwifi . . . . . . . no (disabled on command line)
    match_empty_counter . yes
    match_hashed  . . . . yes
    match_regex . . . . . yes
    match_timediff  . . . yes
    match_value . . . . . yes
    mbmon . . . . . . . . no (disabled on command line)
    mcelog  . . . . . . . no (disabled on command line)
    md  . . . . . . . . . no (disabled on command line)
    mdevents  . . . . . . no (disabled on command line)
    memcachec . . . . . . no (disabled on command line)
    memcached . . . . . . no (disabled on command line)
    memory  . . . . . . . yes
    mic . . . . . . . . . no (disabled on command line)
    modbus  . . . . . . . yes
    mqtt  . . . . . . . . no (mosquitto.h not found) (dependency error)
    multimeter  . . . . . no (disabled on command line)
    mysql . . . . . . . . no (mysql_config failed) (dependency error)
    netapp  . . . . . . . no (disabled on command line)
    netlink . . . . . . . yes
    netstat_udp . . . . . no (disabled on command line)
    network . . . . . . . yes
    nfs . . . . . . . . . no (disabled on command line)
    nginx . . . . . . . . no (curl-config failed) (dependency error)
    notify_desktop  . . . no (disabled on command line)
    notify_email  . . . . no (disabled on command line)
    notify_nagios . . . . no (disabled on command line)
    ntpd  . . . . . . . . yes
    numa  . . . . . . . . no (disabled on command line)
    nut . . . . . . . . . no (disabled on command line)
    olsrd . . . . . . . . yes
    onewire . . . . . . . no (disabled on command line)
    openldap  . . . . . . no (disabled on command line)
    openvpn . . . . . . . yes
    oracle  . . . . . . . no (disabled on command line)
    ovs_events  . . . . . no (disabled on command line)
    ovs_stats . . . . . . no (disabled on command line)
    pcie_errors . . . . . no (disabled on command line)
    perl  . . . . . . . . no (needs libperl)
    pf  . . . . . . . . . no (disabled on command line)
    pinba . . . . . . . . no (disabled on command line)
    ping  . . . . . . . . yes
    postgresql  . . . . . yes
    powerdns  . . . . . . yes
    processes . . . . . . yes
    procevent . . . . . . no (disabled on command line)
    protocols . . . . . . yes
    python  . . . . . . . no (disabled on command line)
    redfish . . . . . . . no (disabled on command line)
    redis . . . . . . . . no (disabled on command line)
    routeros  . . . . . . yes
    rrdcached . . . . . . no (disabled on command line)
    rrdtool . . . . . . . yes
    sensors . . . . . . . yes
    serial  . . . . . . . no (disabled on command line)
    sigrok  . . . . . . . no (disabled on command line)
    slurm . . . . . . . . no (disabled on command line)
    smart . . . . . . . . yes
    snmp  . . . . . . . . yes
    snmp_agent  . . . . . no (disabled on command line)
    snmp6 . . . . . . . . yes
    statsd  . . . . . . . no (disabled on command line)
    swap  . . . . . . . . yes
    synproxy  . . . . . . no (disabled on command line)
    sysevent. . . . . . . no (disabled on command line)
    syslog  . . . . . . . yes
    table . . . . . . . . yes
    tail_csv  . . . . . . yes
    tail  . . . . . . . . yes
    tape  . . . . . . . . no (disabled on command line)
    target_notification . yes
    target_replace  . . . yes
    target_scale  . . . . yes
    target_set  . . . . . yes
    target_v5upgrade  . . yes
    tcpconns  . . . . . . yes
    teamspeak2  . . . . . yes
    ted . . . . . . . . . yes
    thermal . . . . . . . yes
    threshold . . . . . . yes
    tokyotyrant . . . . . no (disabled on command line)
    turbostat . . . . . . no (disabled on command line)
    ubi . . . . . . . . . no (disabled on command line)
    unixsock  . . . . . . yes
    uptime  . . . . . . . yes
    users . . . . . . . . yes
    uuid  . . . . . . . . no (disabled on command line)
    varnish . . . . . . . no (disabled on command line)
    virt  . . . . . . . . no (disabled on command line)
    vmem  . . . . . . . . yes
    vserver . . . . . . . no (disabled on command line)
    wireless  . . . . . . yes
    write_graphite  . . . yes
    write_http  . . . . . no (curl-config failed) (dependency error)
    write_influxdb_udp. . no (disabled on command line)
    write_kafka . . . . . no (disabled on command line)
    write_log . . . . . . no (disabled on command line)
    write_mongodb . . . . no (disabled on command line)
    write_prometheus. . . no (disabled on command line)
    write_redis . . . . . no (disabled on command line)
    write_riemann . . . . no (disabled on command line)
    write_sensu . . . . . no (disabled on command line)
    write_stackdriver . . no (disabled on command line)
    write_syslog . .  . . no (disabled on command line)
    write_tsdb  . . . . . no (disabled on command line)
    xencpu  . . . . . . . no (disabled on command line)
    xmms  . . . . . . . . no (disabled on command line)
    zfs_arc . . . . . . . no (disabled on command line)
    zone  . . . . . . . . no (disabled on command line)
    zookeeper . . . . . . no (disabled on command line)

configure: error: "Some plugins are missing dependencies - see the summary above for details"
make[3]: *** [Makefile:430: /openwrt/build_dir/target-mips_24kc_musl/collectd-5.12.0/.configured_c48004e55b315fa29c4f0a1d61c9a772] Error 1
```
