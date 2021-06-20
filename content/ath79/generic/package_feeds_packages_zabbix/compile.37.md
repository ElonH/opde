---
title: "compile.37"
date: 2021-06-20 22:27:32.415220
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
make package/feeds/packages/zabbix/compile -j$(nproc) || make package/feeds/packages/zabbix/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-change-agentd-config.patch using plaintext: 
patching file conf/zabbix_agentd.conf

Applying ./patches/110-reproducible-builds.patch using plaintext: 
patching file src/libs/zbxcommon/str.c
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/mips
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
configure: Configuring Zabbix 5.0.7
checking whether make sets $(MAKE)... (cached) yes
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
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
checking whether make supports the include directive... yes (GNU style)
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
checking stdio.h usability... yes
checking stdio.h presence... yes
checking for stdio.h... yes
checking for stdlib.h... (cached) yes
checking for string.h... (cached) yes
checking for unistd.h... (cached) yes
checking netdb.h usability... yes
checking netdb.h presence... yes
checking for netdb.h... yes
checking signal.h usability... yes
checking signal.h presence... yes
checking for signal.h... yes
checking syslog.h usability... yes
checking syslog.h presence... yes
checking for syslog.h... yes
checking time.h usability... yes
checking time.h presence... yes
checking for time.h... yes
checking errno.h usability... yes
checking errno.h presence... yes
checking for errno.h... yes
checking for sys/types.h... (cached) yes
checking for sys/stat.h... (cached) yes
checking netinet/in.h usability... yes
checking netinet/in.h presence... yes
checking for netinet/in.h... yes
checking math.h usability... yes
checking math.h presence... yes
checking for math.h... yes
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking dirent.h usability... yes
checking dirent.h presence... yes
checking for dirent.h... yes
checking ctype.h usability... yes
checking ctype.h presence... yes
checking for ctype.h... yes
checking mtent.h usability... no
checking mtent.h presence... no
checking for mtent.h... no
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking sys/param.h usability... yes
checking sys/param.h presence... yes
checking for sys/param.h... yes
checking arpa/inet.h usability... yes
checking arpa/inet.h presence... yes
checking for arpa/inet.h... yes
checking sys/vfs.h usability... yes
checking sys/vfs.h presence... yes
checking for sys/vfs.h... yes
checking sys/pstat.h usability... no
checking sys/pstat.h presence... no
checking for sys/pstat.h... no
checking for sys/sysinfo.h... (cached) no
checking sys/statvfs.h usability... yes
checking sys/statvfs.h presence... yes
checking for sys/statvfs.h... yes
checking sys/statfs.h usability... yes
checking sys/statfs.h presence... yes
checking for sys/statfs.h... yes
checking for sys/socket.h... (cached) yes
checking sys/loadavg.h usability... no
checking sys/loadavg.h presence... no
checking for sys/loadavg.h... no
checking for arpa/inet.h... (cached) yes
checking sys/vmmeter.h usability... no
checking sys/vmmeter.h presence... no
checking for sys/vmmeter.h... no
checking for strings.h... (cached) yes
checking vm/vm_param.h usability... no
checking vm/vm_param.h presence... no
checking for vm/vm_param.h... no
checking sys/time.h usability... yes
checking sys/time.h presence... yes
checking for sys/time.h... yes
checking kstat.h usability... no
checking kstat.h presence... no
checking for kstat.h... no
checking sys/syscall.h usability... yes
checking sys/syscall.h presence... yes
checking for sys/syscall.h... yes
checking sys/sysmacros.h usability... yes
checking sys/sysmacros.h presence... yes
checking for sys/sysmacros.h... yes
checking for stdint.h... (cached) yes
checking mach/host_info.h usability... no
checking mach/host_info.h presence... no
checking for mach/host_info.h... no
checking mach/mach_host.h usability... no
checking mach/mach_host.h presence... no
checking for mach/mach_host.h... no
checking knlist.h usability... no
checking knlist.h presence... no
checking for knlist.h... no
checking pwd.h usability... yes
checking pwd.h presence... yes
checking for pwd.h... yes
checking sys/var.h usability... no
checking sys/var.h presence... no
checking for sys/var.h... no
checking arpa/nameser.h usability... yes
checking arpa/nameser.h presence... yes
checking for arpa/nameser.h... yes
checking assert.h usability... yes
checking assert.h presence... yes
checking for assert.h... yes
checking sys/dkstat.h usability... no
checking sys/dkstat.h presence... no
checking for sys/dkstat.h... no
checking sys/disk.h usability... no
checking sys/disk.h presence... no
checking for sys/disk.h... no
checking sys/sched.h usability... no
checking sys/sched.h presence... no
checking for sys/sched.h... no
checking zone.h usability... no
checking zone.h presence... no
checking for zone.h... no
checking nlist.h usability... yes
checking nlist.h presence... yes
checking for nlist.h... yes
checking kvm.h usability... no
checking kvm.h presence... no
checking for kvm.h... no
checking linux/kernel.h usability... yes
checking linux/kernel.h presence... yes
checking for linux/kernel.h... yes
checking procinfo.h usability... no
checking procinfo.h presence... no
checking for procinfo.h... no
checking sys/dk.h usability... no
checking sys/dk.h presence... no
checking for sys/dk.h... no
checking sys/resource.h usability... yes
checking sys/resource.h presence... yes
checking for sys/resource.h... yes
checking pthread.h usability... yes
checking pthread.h presence... yes
checking for pthread.h... yes
checking windows.h usability... no
checking windows.h presence... no
checking for windows.h... no
checking process.h usability... no
checking process.h presence... no
checking for process.h... no
checking conio.h usability... no
checking conio.h presence... no
checking for conio.h... no
checking sys/wait.h usability... yes
checking sys/wait.h presence... yes
checking for sys/wait.h... yes
checking stdarg.h usability... yes
checking stdarg.h presence... yes
checking for stdarg.h... yes
checking winsock2.h usability... no
checking winsock2.h presence... no
checking for winsock2.h... no
checking pdh.h usability... no
checking pdh.h presence... no
checking for pdh.h... no
checking psapi.h usability... no
checking psapi.h presence... no
checking for psapi.h... no
checking sys/sem.h usability... yes
checking sys/sem.h presence... yes
checking for sys/sem.h... yes
checking sys/ipc.h usability... yes
checking sys/ipc.h presence... yes
checking for sys/ipc.h... yes
checking sys/shm.h usability... yes
checking sys/shm.h presence... yes
checking for sys/shm.h... yes
checking Winldap.h usability... no
checking Winldap.h presence... no
checking for Winldap.h... no
checking Winber.h usability... no
checking Winber.h presence... no
checking for Winber.h... no
checking lber.h usability... yes
checking lber.h presence... yes
checking for lber.h... yes
checking ws2tcpip.h usability... no
checking ws2tcpip.h presence... no
checking for ws2tcpip.h... no
checking for inttypes.h... (cached) yes
checking sys/file.h usability... yes
checking sys/file.h presence... yes
checking for sys/file.h... yes
checking grp.h usability... yes
checking grp.h presence... yes
checking for grp.h... yes
checking execinfo.h usability... no
checking execinfo.h presence... no
checking for execinfo.h... no
checking sys/systemcfg.h usability... no
checking sys/systemcfg.h presence... no
checking for sys/systemcfg.h... no
checking sys/mnttab.h usability... no
checking sys/mnttab.h presence... no
checking for sys/mnttab.h... no
checking mntent.h usability... yes
checking mntent.h presence... yes
checking for mntent.h... yes
checking sys/times.h usability... yes
checking sys/times.h presence... yes
checking for sys/times.h... yes
checking dlfcn.h usability... yes
checking dlfcn.h presence... yes
checking for dlfcn.h... yes
checking sys/utsname.h usability... yes
checking sys/utsname.h presence... yes
checking for sys/utsname.h... yes
checking sys/un.h usability... yes
checking sys/un.h presence... yes
checking for sys/un.h... yes
checking sys/protosw.h usability... no
checking sys/protosw.h presence... no
checking for sys/protosw.h... no
checking stddef.h usability... yes
checking stddef.h presence... yes
checking for stddef.h... yes
checking limits.h usability... yes
checking limits.h presence... yes
checking for limits.h... yes
checking float.h usability... yes
checking float.h presence... yes
checking for float.h... yes
checking for resolv.h... yes
checking for net/if.h... yes
checking for net/if_mib.h... no
checking whether compiler supports -Werror=cpp... yes
checking for sys/mount.h... yes
checking for sys/proc.h... no
checking for sys/sysctl.h... no
checking for sys/user.h... yes
checking for sys/swap.h... yes
checking for sys/ucontext.h... yes
checking for devstat.h... no
checking for linux/netlink.h... yes
checking linux/inet_diag.h usability... yes
checking linux/inet_diag.h presence... yes
checking for linux/inet_diag.h... yes
checking for libperfstat.h... no
checking for library containing socket... none required
checking for library containing kstat_open... no
checking for library containing gethostbyname... none required
checking for library containing clock_gettime... none required
checking for library containing dlopen... none required
checking for library containing perfstat_memory_total... no
checking for library containing devstat_getdevs... no
checking for library containing getdevs... no
checking for library containing backtrace_symbols... no
checking for main in -lm... yes
checking for main in -lkvm... no
checking for DNS lookup functions... yes
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking for an ANSI C-conforming const... yes
checking for pid_t... yes
checking for socklen_t... yes
checking for actual socklen_t parameter type in socket functions... socklen_t
checking for integer field name in union sigval of struct siginfo_t... sival_int
checking for res_ninit... no
checking for res_ndestroy... no
checking for _res._u._ext.nsaddrs... yes
checking for _res._u._ext.ext... no
checking for _res._ext.ext.nsaddrs... no
checking for struct sockaddr_in6.sin6_len... no
checking for union semun... no
checking for struct swaptable in sys/swap.h... no
checking for struct sensordev in sys/sensors.h... no
checking for struct statvfs64 in sys/statvfs.h... no
checking for struct statfs64 in sys/statfs.h... no
checking for field ss_family in struct sockaddr_storage... yes
checking for field mem_unit in struct sysinfo... yes
checking for field freeswap in struct sysinfo... yes
checking for field totalswap in struct sysinfo... yes
checking for field totalram in struct sysinfo... yes
checking for field sharedram in struct sysinfo... yes
checking for field bufferram in struct sysinfo... yes
checking for field freeram in struct sysinfo... yes
checking for field uptime in struct sysinfo... yes
checking for field procs in struct sysinfo... yes
checking for field tm_gmtoff in struct tm... yes
checking for linker options --start-group/--end-group... yes
checking for '__thread' compiler support... yes
checking for field updates in struct vminfo_t... no
checking for function sysconf() in unistd.h... yes
checking for function initgroups()... yes
checking for functions seteuid() and setegid()... yes
checking for function setproctitle()... no
checking for function sysctlbyname()... no
checking for function sysctl (KERN_BOOTTIME)... no
checking for function sysctl (HW_NCPU)... no
checking for function sysctl (KERN_MAXFILES)... no
checking for function sysctl (KERN_MAXPROC)... no
checking for function sysctl (KERN_CPTIME,KERN_CPTIME2)... no
checking for function clock_gettime in time.h... yes
checking for macro __va_copy() in stdarg.h... yes
checking for macro __VA_ARGS__... yes
checking return type of signal handlers... void
checking for getloadavg... yes
checking for hstrerror... yes
checking for getenv... yes
checking for putenv... yes
checking for sigqueue... yes
checking for round... yes
checking for /proc filesystem... yes
checking for file /proc/stat... yes
checking for file /proc/cpuinfo... yes
checking for file /proc/0/psinfo... no
checking for file /proc/loadavg... yes
checking for file /proc/net/dev... yes
checking for long long format... no
checking for -rdynamic linking option... no
checking for libperfstat 5.2.0.40 fileset... no
checking for libperfstat 5.3.0.60 fileset... no
checking for architecture... linux (linux-gnu)
checking for the linux kernel version... unknown family (5.8.0-1033-azure)
checking size of void *... (cached) 4
checking for Oracle support... no
checking for pg_config... /openwrt/staging_dir/target-mips_24kc_musl/host/bin/pg_config
checking for PostgreSQL libraries... yes
checking if PostgreSQL version is >= 9.2... yes
checking for Zabbix server/proxy database selection... ok
checking for multirow insert statements... yes
checking pkg-config is at least version 0.9.0... yes
checking for zlib support... yes
checking for pthread.h... (cached) yes
checking for process shared libpthread support... no
checking for libevent support... configure: error: Unable to use libevent (libevent check failed)
make[3]: *** [Makefile:313: /openwrt/build_dir/target-mips_24kc_musl/zabbix-5.0.7/.configured_0b3870f13e1c90a19d5806087bbb6577] Error 1
```
