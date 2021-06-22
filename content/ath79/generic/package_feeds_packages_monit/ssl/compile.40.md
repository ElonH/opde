---
title: "compile.40"
date: 2021-06-22 10:47:21.987427
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
make package/feeds/packages/monit/compile -j$(nproc) || make package/feeds/packages/monit/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-fix-default-piddir.patch using plaintext: 
patching file configure
patching file configure.ac
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force -I m4
autoreconf: configure.ac: tracing
autoreconf: configure.ac: adding subdirectory libmonit to autoreconf
autoreconf: Entering directory `libmonit'
autoreconf: running: /openwrt/staging_dir/host/bin/libtoolize --install --force
OpenWrt-libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, `config'.
OpenWrt-libtoolize: linking file `config/config.guess'
OpenWrt-libtoolize: linking file `config/config.sub'
OpenWrt-libtoolize: linking file `config/install-sh'
OpenWrt-libtoolize: linking file `config/ltmain.sh'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `m4'.
OpenWrt-libtoolize: linking file `m4/libtool.m4'
OpenWrt-libtoolize: linking file `m4/ltoptions.m4'
OpenWrt-libtoolize: linking file `m4/ltsugar.m4'
OpenWrt-libtoolize: linking file `m4/ltversion.m4'
OpenWrt-libtoolize: linking file `m4/lt~obsolete.m4'
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
autoreconf: Leaving directory `libmonit'
OpenWrt-libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, `config'.
OpenWrt-libtoolize: linking file `config/config.guess'
OpenWrt-libtoolize: linking file `config/config.sub'
OpenWrt-libtoolize: linking file `config/install-sh'
OpenWrt-libtoolize: linking file `config/ltmain.sh'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `m4'.
OpenWrt-libtoolize: linking file `m4/libtool.m4'
OpenWrt-libtoolize: linking file `m4/ltoptions.m4'
OpenWrt-libtoolize: linking file `m4/ltsugar.m4'
OpenWrt-libtoolize: linking file `m4/ltversion.m4'
OpenWrt-libtoolize: linking file `m4/lt~obsolete.m4'
autoreconf: Leaving directory `.'
configure: loading site script /openwrt/include/site/mips
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking for mips-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... no
checking for ccache_cc option to accept ISO C89... none needed
checking whether ccache_cc understands -c and -o together... yes
checking for style of include used by make... GNU
checking dependency style of ccache_cc... none
checking whether make sets $(MAKE)... (cached) yes
checking for bison... bison -y
checking for flex... /openwrt/staging_dir/host/bin/flex
checking for pod2man... /usr/bin/pod2man
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking how to print strings... printf
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
checking for mips-openwrt-linux-strip... (cached) mips-openwrt-linux-musl-strip
checking for mips-openwrt-linux-ranlib... mips-openwrt-linux-musl-gcc-ranlib
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
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... no
checking for socket in -lsocket... no
checking for socket in -linet... no
checking for inet_addr in -lnsl... no
checking for inet_aton in -lresolv... yes
checking for crypt in -lc... yes
checking for pthread_create in -lpthread... yes
checking for ANSI C header files... (cached) yes
checking for sys/wait.h that is POSIX.1 compatible... yes
checking whether stat file-mode macros are broken... no
checking whether time.h and sys/time.h may both be included... yes
checking alloca.h usability... yes
checking alloca.h presence... yes
checking for alloca.h... yes
checking arpa/inet.h usability... yes
checking arpa/inet.h presence... yes
checking for arpa/inet.h... yes
checking asm/page.h usability... no
checking asm/page.h presence... no
checking for asm/page.h... no
checking asm/param.h usability... yes
checking asm/param.h presence... yes
checking for asm/param.h... yes
checking cf.h usability... no
checking cf.h presence... no
checking for cf.h... no
checking crt_externs.h usability... no
checking crt_externs.h presence... no
checking for crt_externs.h... no
checking ctype.h usability... yes
checking ctype.h presence... yes
checking for ctype.h... yes
checking crypt.h usability... yes
checking crypt.h presence... yes
checking for crypt.h... yes
checking CoreFoundation/CoreFoundation.h usability... no
checking CoreFoundation/CoreFoundation.h presence... no
checking for CoreFoundation/CoreFoundation.h... no
checking devstat.h usability... no
checking devstat.h presence... no
checking for devstat.h... no
checking dirent.h usability... yes
checking dirent.h presence... yes
checking for dirent.h... yes
checking DiskArbitration/DiskArbitration.h usability... no
checking DiskArbitration/DiskArbitration.h presence... no
checking for DiskArbitration/DiskArbitration.h... no
checking errno.h usability... yes
checking errno.h presence... yes
checking for errno.h... yes
checking execinfo.h usability... no
checking execinfo.h presence... no
checking for execinfo.h... no
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking getopt.h usability... yes
checking getopt.h presence... yes
checking for getopt.h... yes
checking glob.h usability... yes
checking glob.h presence... yes
checking for glob.h... yes
checking grp.h usability... yes
checking grp.h presence... yes
checking for grp.h... yes
checking ifaddrs.h usability... yes
checking ifaddrs.h presence... yes
checking for ifaddrs.h... yes
checking IOKit/storage/IOBlockStorageDriver.h usability... no
checking IOKit/storage/IOBlockStorageDriver.h presence... no
checking for IOKit/storage/IOBlockStorageDriver.h... no
checking kinfo.h usability... no
checking kinfo.h presence... no
checking for kinfo.h... no
checking kvm.h usability... no
checking kvm.h presence... no
checking for kvm.h... no
checking paths.h usability... yes
checking paths.h presence... yes
checking for paths.h... yes
checking kstat.h usability... no
checking kstat.h presence... no
checking for kstat.h... no
checking libzfs.h usability... no
checking libzfs.h presence... no
checking for libzfs.h... no
checking zone.h usability... no
checking zone.h presence... no
checking for zone.h... no
checking sys/protosw.h usability... no
checking sys/protosw.h presence... no
checking for sys/protosw.h... no
checking libproc.h usability... no
checking libproc.h presence... no
checking for libproc.h... no
checking limits.h usability... yes
checking limits.h presence... yes
checking for limits.h... yes
checking loadavg.h usability... no
checking loadavg.h presence... no
checking for loadavg.h... no
checking locale.h usability... yes
checking locale.h presence... yes
checking for locale.h... yes
checking lvm.h usability... no
checking lvm.h presence... no
checking for lvm.h... no
checking mach/boolean.h usability... no
checking mach/boolean.h presence... no
checking for mach/boolean.h... no
checking mach/host_info.h usability... no
checking mach/host_info.h presence... no
checking for mach/host_info.h... no
checking mach/mach.h usability... no
checking mach/mach.h presence... no
checking for mach/mach.h... no
checking mach/mach_host.h usability... no
checking mach/mach_host.h presence... no
checking for mach/mach_host.h... no
checking for memory.h... (cached) yes
checking mntent.h usability... yes
checking mntent.h presence... yes
checking for mntent.h... yes
checking netdb.h usability... yes
checking netdb.h presence... yes
checking for netdb.h... yes
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking netinet/in.h usability... yes
checking netinet/in.h presence... yes
checking for netinet/in.h... yes
checking netinet/tcp.h usability... yes
checking netinet/tcp.h presence... yes
checking for netinet/tcp.h... yes
checking netinet/in_systm.h usability... yes
checking netinet/in_systm.h presence... yes
checking for netinet/in_systm.h... yes
checking pam/pam_appl.h usability... no
checking pam/pam_appl.h presence... no
checking for pam/pam_appl.h... no
checking security/pam_appl.h usability... yes
checking security/pam_appl.h presence... yes
checking for security/pam_appl.h... yes
checking poll.h usability... yes
checking poll.h presence... yes
checking for poll.h... yes
checking procfs.h usability... no
checking procfs.h presence... no
checking for procfs.h... no
checking sys/procfs.h usability... yes
checking sys/procfs.h presence... yes
checking for sys/procfs.h... yes
checking procinfo.h usability... no
checking procinfo.h presence... no
checking for procinfo.h... no
checking pthread.h usability... yes
checking pthread.h presence... yes
checking for pthread.h... yes
checking pwd.h usability... yes
checking pwd.h presence... yes
checking for pwd.h... yes
checking regex.h usability... yes
checking regex.h presence... yes
checking for regex.h... yes
checking setjmp.h usability... yes
checking setjmp.h presence... yes
checking for setjmp.h... yes
checking signal.h usability... yes
checking signal.h presence... yes
checking for signal.h... yes
checking stdarg.h usability... yes
checking stdarg.h presence... yes
checking for stdarg.h... yes
checking stddef.h usability... yes
checking stddef.h presence... yes
checking for stddef.h... yes
checking stdio.h usability... yes
checking stdio.h presence... yes
checking for stdio.h... yes
checking for string.h... (cached) yes
checking for strings.h... (cached) yes
checking stropts.h usability... yes
checking stropts.h presence... yes
checking for stropts.h... yes
checking sys/cfgodm.h usability... no
checking sys/cfgodm.h presence... no
checking for sys/cfgodm.h... no
checking sys/cfgdb.h usability... no
checking sys/cfgdb.h presence... no
checking for sys/cfgdb.h... no
checking sys/dk.h usability... no
checking sys/dk.h presence... no
checking for sys/dk.h... no
checking sys/dkstat.h usability... no
checking sys/dkstat.h presence... no
checking for sys/dkstat.h... no
checking sys/disk.h usability... no
checking sys/disk.h presence... no
checking for sys/disk.h... no
checking sys/filio.h usability... no
checking sys/filio.h presence... no
checking for sys/filio.h... no
checking sys/fs/zfs.h usability... no
checking sys/fs/zfs.h presence... no
checking for sys/fs/zfs.h... no
checking sys/instance.h usability... no
checking sys/instance.h presence... no
checking for sys/instance.h... no
checking sys/ioctl.h usability... yes
checking sys/ioctl.h presence... yes
checking for sys/ioctl.h... yes
checking sys/iostat.h usability... no
checking sys/iostat.h presence... no
checking for sys/iostat.h... no
checking sys/loadavg.h usability... no
checking sys/loadavg.h presence... no
checking for sys/loadavg.h... no
checking sys/lock.h usability... no
checking sys/lock.h presence... no
checking for sys/lock.h... no
checking sys/mntent.h usability... no
checking sys/mntent.h presence... no
checking for sys/mntent.h... no
checking sys/mnttab.h usability... no
checking sys/mnttab.h presence... no
checking for sys/mnttab.h... no
checking sys/mutex.h usability... no
checking sys/mutex.h presence... no
checking for sys/mutex.h... no
checking sys/nlist.h usability... no
checking sys/nlist.h presence... no
checking for sys/nlist.h... no
checking sys/nvpair.h usability... no
checking sys/nvpair.h presence... no
checking for sys/nvpair.h... no
checking sys/param.h usability... yes
checking sys/param.h presence... yes
checking for sys/param.h... yes
checking sys/pstat.h usability... no
checking sys/pstat.h presence... no
checking for sys/pstat.h... no
checking sys/queue.h usability... yes
checking sys/queue.h presence... yes
checking for sys/queue.h... yes
checking sys/resource.h usability... yes
checking sys/resource.h presence... yes
checking for sys/resource.h... yes
checking sys/sched.h usability... no
checking sys/sched.h presence... no
checking for sys/sched.h... no
checking sys/statfs.h usability... yes
checking sys/statfs.h presence... yes
checking for sys/statfs.h... yes
checking sys/statvfs.h usability... yes
checking sys/statvfs.h presence... yes
checking for sys/statvfs.h... yes
checking sys/sysinfo.h usability... yes
checking sys/sysinfo.h presence... yes
checking for sys/sysinfo.h... yes
checking sys/systemcfg.h usability... no
checking sys/systemcfg.h presence... no
checking for sys/systemcfg.h... no
checking sys/time.h usability... yes
checking sys/time.h presence... yes
checking for sys/time.h... yes
checking sys/tree.h usability... no
checking sys/tree.h presence... no
checking for sys/tree.h... no
checking for sys/types.h... (cached) yes
checking sys/un.h usability... yes
checking sys/un.h presence... yes
checking for sys/un.h... yes
checking sys/utsname.h usability... yes
checking sys/utsname.h presence... yes
checking for sys/utsname.h... yes
checking sys/var.h usability... no
checking sys/var.h presence... no
checking for sys/var.h... no
checking sys/vmmeter.h usability... no
checking sys/vmmeter.h presence... no
checking for sys/vmmeter.h... no
checking sys/vm_usage.h usability... no
checking sys/vm_usage.h presence... no
checking for sys/vm_usage.h... no
checking sys/vfs.h usability... yes
checking sys/vfs.h presence... yes
checking for sys/vfs.h... yes
checking syslog.h usability... yes
checking syslog.h presence... yes
checking for syslog.h... yes
checking for unistd.h... (cached) yes
checking utmpx.h usability... yes
checking utmpx.h presence... yes
checking for utmpx.h... yes
checking uvm/uvm_extern.h usability... no
checking uvm/uvm_extern.h presence... no
checking for uvm/uvm_extern.h... no
checking uvm/uvm_param.h usability... no
checking uvm/uvm_param.h presence... no
checking for uvm/uvm_param.h... no
checking vm/vm.h usability... no
checking vm/vm.h presence... no
checking for vm/vm.h... no
checking for inttypes.h... (cached) yes
checking for libperfstat.h... no
checking for netinet/ip.h... yes
checking for net/if.h... yes
checking for netinet/ip_icmp.h... yes
checking for netinet/icmp6.h... yes
checking for sys/sysctl.h... no
checking for sys/mount.h... yes
checking for sys/proc.h... no
checking for sys/swap.h... yes
checking for sys/ucred.h... no
checking for sys/user.h... yes
checking for machine/vmparam.h... no
checking for vm/pmap.h... no
checking for machine/pmap.h... no
checking for vm/vm_map.h... no
checking for vm/vm_object.h... no
checking for sys/resourcevar.h... no
checking for uvm/uvm_map.h... no
checking for uvm/uvm_pmap.h... no
checking for uvm/uvm_object.h... no
checking for uvm/uvm.h... no
checking for boolean_t... no
checking for mode_t... yes
checking for pid_t... yes
checking for size_t... yes
checking for pid_t... (cached) yes
checking return type of signal handlers... void
checking whether struct tm is in sys/time.h or time.h... time.h
checking for struct tm.tm_gmtoff... no
checking for error_at_line... no
checking vfork.h usability... no
checking vfork.h presence... no
checking for vfork.h... no
checking for fork... yes
checking for vfork... yes
checking for working fork... cross
configure: WARNING: result yes guessed because of cross compilation
checking for working vfork... (cached) yes
checking whether lstat correctly handles trailing slash... (cached) yes
checking whether stat accepts an empty string... (cached) no
checking for strftime... (cached) yes
checking for statfs... yes
checking for statvfs... yes
checking for setlocale... (cached) yes
checking for getaddrinfo... (cached) yes
checking for syslog... yes
checking for vsyslog... yes
checking for backtrace... no
checking for getloadavg... yes
checking for getopt_long... yes
checking for va_copy... yes
checking for an ANSI C-conforming const... yes
checking whether byte ordering is bigendian... (cached) yes
checking for IPv6 support... (cached) yes
checking pid file location... /var/run
checking for large files support... enabled
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking for zlibVersion in -lz... yes
checking zlib.h usability... yes
checking zlib.h presence... yes
checking for zlib.h... yes
checking for PAM support... disabled
checking for static SSL support... disabled
checking for SSL support... enabled
checking for SSL include directory... /usr/include
checking for SSL library directory... Not found
checking for SSL_new in -lssl... no
configure: error: Could not find SSL library, please use --with-ssl-lib-dir option or disabled the SSL support using --without-ssl
make[3]: *** [Makefile:101: /openwrt/build_dir/target-mips_24kc_musl/monit-ssl/monit-5.26.0/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
