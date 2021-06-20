---
title: "compile.37"
date: 2021-06-20 22:33:34.401072
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
make package/feeds/packages/atlas-probe/compile -j$(nproc) || make package/feeds/packages/atlas-probe/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-fix-stime-glibc-remove.patch using plaintext: 
patching file coreutils/date.c
patching file util-linux/rdate.c
patching file networking/httpget.c
patching file networking/httppost.c
autoreconf: Entering directory `libevent-2.1.11-stable'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I libevent-2.1.11-stable --force -I m4
autoreconf: configure.ac: tracing
autoreconf: running: /openwrt/staging_dir/host/bin/libtoolize --install --force
OpenWrt-libtoolize: putting auxiliary files in `.'.
OpenWrt-libtoolize: linking file `./config.guess'
OpenWrt-libtoolize: linking file `./config.sub'
OpenWrt-libtoolize: linking file `./install-sh'
OpenWrt-libtoolize: linking file `./ltmain.sh'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `m4'.
OpenWrt-libtoolize: linking file `m4/libtool.m4'
OpenWrt-libtoolize: linking file `m4/ltoptions.m4'
OpenWrt-libtoolize: linking file `m4/ltsugar.m4'
OpenWrt-libtoolize: linking file `m4/ltversion.m4'
OpenWrt-libtoolize: linking file `m4/lt~obsolete.m4'
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=libevent-2.1.11-stable --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=libevent-2.1.11-stable --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
configure.ac:25: installing './compile'
configure.ac:13: installing './missing'
Makefile.am: installing './depcomp'
parallel-tests: installing './test-driver'
autoreconf: Leaving directory `libevent-2.1.11-stable'
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
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking whether ln -s works... yes
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking whether ccache_cc needs -traditional... no
checking how to print strings... printf
checking for a sed that does not truncate output... (cached) /openwrt/staging_dir/host/bin/sed
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache_cc... mips-openwrt-linux-musl-ld
checking if the linker (mips-openwrt-linux-musl-ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... mips-openwrt-linux-musl-gcc-nm
checking the name lister (mips-openwrt-linux-musl-gcc-nm) interface... BSD nm
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
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... no
checking whether to build static libraries... yes
checking for library containing inet_ntoa... none required
checking for library containing socket... none required
checking for library containing inet_aton... none required
checking for library containing clock_gettime... none required
checking for clock_gettime... yes
checking for library containing sendfile... none required
checking for WIN32... no
checking for MIDIPIX... no
checking for CYGWIN... no
checking zlib.h usability... yes
checking zlib.h presence... yes
checking for zlib.h... yes
checking for library containing inflateEnd... -lz
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking for mips-openwrt-linux-pkg-config... /openwrt/staging_dir/host/bin/pkg-config
checking if pkg-config is at least version 0.15.0... yes
checking for library containing SSL_new... no
checking for library containing SSL_new... no
checking openssl/ssl.h usability... no
checking openssl/ssl.h presence... no
checking for openssl/ssl.h... no
checking arpa/inet.h usability... yes
checking arpa/inet.h presence... yes
checking for arpa/inet.h... yes
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking ifaddrs.h usability... yes
checking ifaddrs.h presence... yes
checking for ifaddrs.h... yes
checking mach/mach_time.h usability... no
checking mach/mach_time.h presence... no
checking for mach/mach_time.h... no
checking netdb.h usability... yes
checking netdb.h presence... yes
checking for netdb.h... yes
checking netinet/in.h usability... yes
checking netinet/in.h presence... yes
checking for netinet/in.h... yes
checking netinet/in6.h usability... no
checking netinet/in6.h presence... no
checking for netinet/in6.h... no
checking netinet/tcp.h usability... yes
checking netinet/tcp.h presence... yes
checking for netinet/tcp.h... yes
checking sys/un.h usability... yes
checking sys/un.h presence... yes
checking for sys/un.h... yes
checking poll.h usability... yes
checking poll.h presence... yes
checking for poll.h... yes
checking port.h usability... no
checking port.h presence... no
checking for port.h... no
checking stdarg.h usability... yes
checking stdarg.h presence... yes
checking for stdarg.h... yes
checking stddef.h usability... yes
checking stddef.h presence... yes
checking for stddef.h... yes
checking sys/devpoll.h usability... no
checking sys/devpoll.h presence... no
checking for sys/devpoll.h... no
checking sys/epoll.h usability... yes
checking sys/epoll.h presence... yes
checking for sys/epoll.h... yes
checking sys/event.h usability... no
checking sys/event.h presence... no
checking for sys/event.h... no
checking sys/eventfd.h usability... yes
checking sys/eventfd.h presence... yes
checking for sys/eventfd.h... yes
checking sys/ioctl.h usability... yes
checking sys/ioctl.h presence... yes
checking for sys/ioctl.h... yes
checking sys/mman.h usability... yes
checking sys/mman.h presence... yes
checking for sys/mman.h... yes
checking sys/param.h usability... yes
checking sys/param.h presence... yes
checking for sys/param.h... yes
checking sys/queue.h usability... yes
checking sys/queue.h presence... yes
checking for sys/queue.h... yes
checking sys/resource.h usability... yes
checking sys/resource.h presence... yes
checking for sys/resource.h... yes
checking sys/select.h usability... yes
checking sys/select.h presence... yes
checking for sys/select.h... yes
checking sys/sendfile.h usability... yes
checking sys/sendfile.h presence... yes
checking for sys/sendfile.h... yes
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking for sys/stat.h... (cached) yes
checking sys/time.h usability... yes
checking sys/time.h presence... yes
checking for sys/time.h... yes
checking sys/timerfd.h usability... yes
checking sys/timerfd.h presence... yes
checking for sys/timerfd.h... yes
checking sys/uio.h usability... yes
checking sys/uio.h presence... yes
checking for sys/uio.h... yes
checking sys/wait.h usability... yes
checking sys/wait.h presence... yes
checking for sys/wait.h... yes
checking errno.h usability... yes
checking errno.h presence... yes
checking for errno.h... yes
checking for sys/sysctl.h... no
checking for TAILQ_FOREACH in sys/queue.h... yes
checking for timeradd in sys/time.h... yes
checking for timercmp in sys/time.h... yes
checking for timerclear in sys/time.h... yes
checking for timerisset in sys/time.h... yes
checking for an ANSI C-conforming const... yes
checking for inline... inline
checking whether time.h and sys/time.h may both be included... yes
checking for accept4... yes
checking for arc4random... no
checking for arc4random_buf... no
checking for arc4random_addrandom... no
checking for eventfd... yes
checking for epoll_create1... yes
checking for fcntl... yes
checking for getegid... yes
checking for geteuid... yes
checking for getifaddrs... yes
checking for getnameinfo... yes
checking for getprotobynumber... yes
checking for gettimeofday... (cached) yes
checking for inet_ntop... yes
checking for inet_pton... yes
checking for issetugid... yes
checking for mach_absolute_time... no
checking for mmap... yes
checking for nanosleep... yes
checking for pipe... yes
checking for pipe2... yes
checking for putenv... yes
checking for sendfile... yes
checking for setenv... yes
checking for setrlimit... yes
checking for sigaction... yes
checking for signal... yes
checking for splice... yes
checking for strlcpy... yes
checking for strsep... yes
checking for strtok_r... yes
checking for strtoll... yes
checking for sysctl... no
checking for timerfd_create... yes
checking for umask... yes
checking for unsetenv... yes
checking for usleep... yes
checking for vasprintf... yes
checking for getservbyname... yes
checking for getaddrinfo... yes
checking for F_SETFD in fcntl.h... yes
checking for select... yes
checking for poll... yes
checking for epoll_ctl... yes
checking for port_create... no
checking for pid_t... yes
checking for size_t... yes
checking for ssize_t... yes
checking for uint64_t... yes
checking for uint32_t... yes
checking for uint16_t... yes
checking for uint8_t... yes
checking for uintptr_t... yes
checking for fd_mask... yes
checking size of long long... (cached) 8
checking size of long... (cached) 4
checking size of int... (cached) 4
checking size of short... (cached) 2
checking size of size_t... (cached) 4
checking size of void *... (cached) 4
checking size of off_t... (cached) 8
checking size of time_t... 4
checking for struct in6_addr... yes
checking for struct sockaddr_in6... yes
checking for struct sockaddr_un... yes
checking for sa_family_t... yes
checking for struct addrinfo... yes
checking for struct sockaddr_storage... yes
checking for struct in6_addr.s6_addr32... yes
checking for struct in6_addr.s6_addr16... yes
checking for struct sockaddr_in.sin_len... no
checking for struct sockaddr_in6.sin6_len... no
checking for struct sockaddr_storage.ss_family... yes
checking for struct sockaddr_storage.__ss_family... no
checking for struct linger... yes
checking for socklen_t... yes
checking whether our compiler supports __func__... yes
checking whether our compiler supports __FUNCTION__... yes
checking for the pthreads library -lpthreads... no
checking whether pthreads work without any flags... yes
checking for joinable pthread attribute... PTHREAD_CREATE_JOINABLE
checking if more special flags are required for pthreads... no
checking size of pthread_t... 4
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating libevent.pc
config.status: creating libevent_openssl.pc
config.status: creating libevent_pthreads.pc
config.status: creating libevent_core.pc
config.status: creating libevent_extra.pc
config.status: creating Makefile
config.status: creating config.h
config.status: creating evconfig-private.h
config.status: executing depfiles commands
config.status: executing libtool commands
configure: WARNING: unrecognized options: --disable-nls
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/ripe-atlas-probe-busybox-2.2.1/libevent-2.1.11-stable'
  GEN      test/rpcgen-attempted
  GEN      include/event2/event-config.h
make  all-am
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/ripe-atlas-probe-busybox-2.2.1/libevent-2.1.11-stable'
  CC       buffer.lo
  CC       bufferevent.lo
  CC       bufferevent_filter.lo
  CC       bufferevent_pair.lo
  CC       bufferevent_ratelim.lo
  CC       bufferevent_sock.lo
  CC       event.lo
  CC       evmap.lo
  CC       evthread.lo
  CC       evutil.lo
  CC       evutil_rand.lo
  CC       evutil_time.lo
  CC       listener.lo
  CC       log.lo
  CC       select.lo
  CC       poll.lo
  CC       epoll.lo
  CC       signal.lo
  CC       evdns.lo
  CC       event_tagging.lo
  CC       evrpc.lo
  CC       http.lo
  CCLD     libevent.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CCLD     libevent_core.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CCLD     libevent_extra.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CC       evthread_pthread.lo
  CCLD     libevent_pthreads.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CC       sample/dns-example.o
  CCLD     sample/dns-example
  CC       sample/event-read-fifo.o
  CCLD     sample/event-read-fifo
  CC       sample/hello-world.o
  CCLD     sample/hello-world
  CC       sample/http-server.o
  CCLD     sample/http-server
  CC       sample/http-connect.o
  CCLD     sample/http-connect
  CC       sample/signal-test.o
  CCLD     sample/signal-test
  CC       sample/time-test.o
  CCLD     sample/time-test
  CC       test/bench.o
  CCLD     test/bench
  CC       test/bench_cascade.o
  CCLD     test/bench_cascade
  CC       test/bench_http.o
  CCLD     test/bench_http
  CC       test/bench_httpclient.o
  CCLD     test/bench_httpclient
  CC       test/test-changelist.o
  CCLD     test/test-changelist
  CC       test/test-dumpevents.o
  CCLD     test/test-dumpevents
  CC       test/test-eof.o
  CCLD     test/test-eof
  CC       test/test-closed.o
  CCLD     test/test-closed
  CC       test/test-fdleak.o
  CCLD     test/test-fdleak
  CC       test/test-init.o
  CCLD     test/test-init
  CC       test/test-ratelim.o
  CCLD     test/test-ratelim
  CC       test/test-time.o
  CCLD     test/test-time
  CC       test/test-weof.o
  CCLD     test/test-weof
  CC       test/test_regress-regress.o
  CC       test/test_regress-regress.gen.o
  CC       test/test_regress-regress_buffer.o
  CC       test/test_regress-regress_bufferevent.o
  CC       test/test_regress-regress_dns.o
  CC       test/test_regress-regress_et.o
  CC       test/test_regress-regress_finalize.o
  CC       test/test_regress-regress_http.o
  CC       test/test_regress-regress_listener.o
  CC       test/test_regress-regress_main.o
  CC       test/test_regress-regress_minheap.o
  CC       test/test_regress-regress_rpc.o
  CC       test/test_regress-regress_testutils.o
  CC       test/test_regress-regress_util.o
  CC       test/test_regress-tinytest.o
  CC       test/test_regress-regress_thread.o
  CC       test/test_regress-regress_zlib.o
  CCLD     test/regress
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/ripe-atlas-probe-busybox-2.2.1/libevent-2.1.11-stable'
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/ripe-atlas-probe-busybox-2.2.1/libevent-2.1.11-stable'
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/ripe-atlas-probe-busybox-2.2.1'
  GEN     include/applets.h
  GEN     include/usage.h
  GEN     scripts/Kbuild
  GEN     editors/Kbuild
  GEN     editors/Config.in
  GEN     procps/Kbuild
  GEN     procps/Config.in
  GEN     modutils/Kbuild
  GEN     modutils/Config.in
  GEN     applets/Kbuild
  GEN     libpwdgrp/Kbuild
  GEN     selinux/Kbuild
  GEN     selinux/Config.in
  GEN     console-tools/Kbuild
  GEN     console-tools/Config.in
  GEN     e2fsprogs/Kbuild
  GEN     e2fsprogs/Config.in
  GEN     coreutils/Kbuild
  GEN     coreutils/Config.in
  GEN     coreutils/libcoreutils/Kbuild
  GEN     eperd/Kbuild
  GEN     eperd/Config.in
  GEN     loginutils/Kbuild
  GEN     loginutils/Config.in
  GEN     sysklogd/Kbuild
  GEN     sysklogd/Config.in
  GEN     util-linux/Kbuild
  GEN     util-linux/Config.in
  GEN     util-linux/volume_id/Kbuild
  GEN     util-linux/volume_id/Config.in
  GEN     shell/Kbuild
  GEN     shell/Config.in
  GEN     runit/Kbuild
  GEN     runit/Config.in
  GEN     findutils/Kbuild
  GEN     findutils/Config.in
  GEN     networking/Kbuild
  GEN     networking/Config.in
  GEN     networking/udhcp/Kbuild
  GEN     networking/udhcp/Config.in
  GEN     networking/libiproute/Kbuild
  GEN     miscutils/Kbuild
  GEN     miscutils/Config.in
  GEN     mailutils/Kbuild
  GEN     mailutils/Config.in
  GEN     archival/Kbuild
  GEN     archival/Config.in
  GEN     archival/libarchive/Kbuild
  GEN     libbb/Kbuild
  GEN     libbb/Config.in
  GEN     init/Kbuild
  GEN     init/Config.in
  GEN     debianutils/Kbuild
  GEN     debianutils/Config.in
  GEN     printutils/Kbuild
  GEN     printutils/Config.in
  HOSTCC  scripts/basic/fixdep
  HOSTCC  scripts/basic/split-include
scripts/basic/split-include.c: In function 'main':
scripts/basic/split-include.c:134:6: warning: ignoring return value of 'fgets', declared with attribute warn_unused_result [-Wunused-result]
  134 |      fgets(old_line, buffer_size, fp_target);
      |      ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  HOSTCC  scripts/basic/docproc
  HOSTCC  scripts/kconfig/conf.o
scripts/kconfig/conf.c: In function 'conf_askvalue':
scripts/kconfig/conf.c:106:3: warning: ignoring return value of 'fgets', declared with attribute warn_unused_result [-Wunused-result]
  106 |   fgets(line, 128, stdin);
      |   ^~~~~~~~~~~~~~~~~~~~~~~
scripts/kconfig/conf.c: In function 'conf_choice':
scripts/kconfig/conf.c:354:4: warning: ignoring return value of 'fgets', declared with attribute warn_unused_result [-Wunused-result]
  354 |    fgets(line, 128, stdin);
      |    ^~~~~~~~~~~~~~~~~~~~~~~
  HOSTCC  scripts/kconfig/kxgettext.o
  HOSTCC  scripts/kconfig/mconf.o
scripts/kconfig/mconf.c: In function 'show_textbox':
scripts/kconfig/mconf.c:847:2: warning: ignoring return value of 'write', declared with attribute warn_unused_result [-Wunused-result]
  847 |  write(fd, text, strlen(text));
      |  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
scripts/kconfig/mconf.c: In function 'exec_conf':
scripts/kconfig/mconf.c:481:2: warning: ignoring return value of 'pipe', declared with attribute warn_unused_result [-Wunused-result]
  481 |  pipe(pipefd);
      |  ^~~~~~~~~~~~
  SHIPPED scripts/kconfig/zconf.tab.c
  SHIPPED scripts/kconfig/lex.zconf.c
  SHIPPED scripts/kconfig/zconf.hash.c
  HOSTCC  scripts/kconfig/zconf.tab.o
In file included from scripts/kconfig/zconf.tab.c:2168:
scripts/kconfig/confdata.c: In function 'conf_write':
scripts/kconfig/confdata.c:366:19: warning: '.tmpconfig.' directive writing 11 bytes into a region of size between 1 and 128 [-Wformat-overflow=]
  366 |  sprintf(newname, "%s.tmpconfig.%d", dirname, (int)getpid());
      |                   ^~~~~~~~~~~~~~~~~
In file included from /usr/include/stdio.h:867,
                 from scripts/kconfig/zconf.tab.c:144:
/usr/include/x86_64-linux-gnu/bits/stdio2.h:36:10: note: '__builtin___sprintf_chk' output between 13 and 150 bytes into a destination of size 128
   36 |   return __builtin___sprintf_chk (__s, __USE_FORTIFY_LEVEL - 1,
      |          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   37 |       __bos (__s), __fmt, __va_arg_pack ());
      |       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from scripts/kconfig/zconf.tab.c:2168:
scripts/kconfig/confdata.c:366:19: warning: '.tmpconfig.' directive writing 11 bytes into a region of size between 1 and 128 [-Wformat-overflow=]
  366 |  sprintf(newname, "%s.tmpconfig.%d", dirname, (int)getpid());
      |                   ^~~~~~~~~~~~~~~~~
In file included from /usr/include/stdio.h:867,
                 from scripts/kconfig/zconf.tab.c:144:
/usr/include/x86_64-linux-gnu/bits/stdio2.h:36:10: note: '__builtin___sprintf_chk' output between 13 and 150 bytes into a destination of size 128
   36 |   return __builtin___sprintf_chk (__s, __USE_FORTIFY_LEVEL - 1,
      |          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   37 |       __bos (__s), __fmt, __va_arg_pack ());
      |       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from scripts/kconfig/zconf.tab.c:2168:
scripts/kconfig/confdata.c:582:19: warning: '%s' directive writing likely 7 or more bytes into a region of size between 1 and 128 [-Wformat-overflow=]
  582 |  sprintf(tmpname, "%s%s", dirname, basename);
      |                   ^~~~~~
scripts/kconfig/confdata.c:582:19: note: assuming directive output of 7 bytes
In file included from /usr/include/stdio.h:867,
                 from scripts/kconfig/zconf.tab.c:144:
/usr/include/x86_64-linux-gnu/bits/stdio2.h:36:10: note: '__builtin___sprintf_chk' output 1 or more bytes (assuming 135) into a destination of size 128
   36 |   return __builtin___sprintf_chk (__s, __USE_FORTIFY_LEVEL - 1,
      |          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   37 |       __bos (__s), __fmt, __va_arg_pack ());
      |       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  HOSTLD  scripts/kconfig/conf
scripts/kconfig/conf -s Config.in
eperd/Config.in:67 error: Overlong line
#
# using defaults found in .config
#
  SPLIT   include/autoconf.h -> include/config/*
  GEN     include/bbconfigopts.h
  GEN     include/common_bufsiz.h
  HOSTCC  applets/usage
applets/usage.c: In function 'main':
applets/usage.c:52:3: warning: ignoring return value of 'write', declared with attribute warn_unused_result [-Wunused-result]
   52 |   write(STDOUT_FILENO, usage_array[i].usage, strlen(usage_array[i].usage) + 1);
      |   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  GEN     include/usage_compressed.h
  HOSTCC  applets/applet_tables
  GEN     include/applet_tables.h include/NUM_APPLETS.h
  GEN     include/applet_tables.h include/NUM_APPLETS.h
  CC      applets/applets.o
  LD      applets/built-in.o
  HOSTCC  applets/usage_pod
applets/usage_pod.c: In function 'main':
applets/usage_pod.c:74:3: warning: format not a string literal and no format arguments [-Wformat-security]
   74 |   printf(usage_array[i].aname);
      |   ^~~~~~
  LD      archival/built-in.o
  CC      archival/bbunzip.o
  CC      archival/bzip2.o
  CC      archival/cpio.o
  CC      archival/dpkg.o
  CC      archival/dpkg_deb.o
  CC      archival/gzip.o
  CC      archival/lzop.o
  CC      archival/rpm.o
  CC      archival/rpm2cpio.o
  CC      archival/tar.o
  CC      archival/unzip.o
  AR      archival/lib.a
  LD      archival/libarchive/built-in.o
  CC      archival/libarchive/common.o
  CC      archival/libarchive/data_align.o
  CC      archival/libarchive/data_extract_all.o
  CC      archival/libarchive/data_extract_to_command.o
  CC      archival/libarchive/data_extract_to_stdout.o
  CC      archival/libarchive/data_skip.o
  CC      archival/libarchive/decompress_bunzip2.o
  CC      archival/libarchive/decompress_gunzip.o
  CC      archival/libarchive/decompress_unlzma.o
  CC      archival/libarchive/decompress_unxz.o
  CC      archival/libarchive/filter_accept_all.o
  CC      archival/libarchive/filter_accept_list.o
  CC      archival/libarchive/filter_accept_list_reassign.o
  CC      archival/libarchive/filter_accept_reject_list.o
  CC      archival/libarchive/find_list_entry.o
  CC      archival/libarchive/get_header_ar.o
  CC      archival/libarchive/get_header_cpio.o
  CC      archival/libarchive/get_header_tar.o
  CC      archival/libarchive/get_header_tar_bz2.o
  CC      archival/libarchive/get_header_tar_gz.o
  CC      archival/libarchive/get_header_tar_lzma.o
  CC      archival/libarchive/get_header_tar_xz.o
  CC      archival/libarchive/header_list.o
  CC      archival/libarchive/header_skip.o
  CC      archival/libarchive/header_verbose_list.o
  CC      archival/libarchive/init_handle.o
  CC      archival/libarchive/lzo1x_1.o
  CC      archival/libarchive/lzo1x_1o.o
  CC      archival/libarchive/lzo1x_d.o
  CC      archival/libarchive/open_transformer.o
  CC      archival/libarchive/seek_by_jump.o
  CC      archival/libarchive/seek_by_read.o
  CC      archival/libarchive/unpack_ar_archive.o
  CC      archival/libarchive/unsafe_prefix.o
  AR      archival/libarchive/lib.a
  LD      console-tools/built-in.o
  CC      console-tools/chvt.o
  CC      console-tools/clear.o
  CC      console-tools/deallocvt.o
  CC      console-tools/dumpkmap.o
  CC      console-tools/fgconsole.o
  CC      console-tools/kbd_mode.o
  CC      console-tools/loadfont.o
  CC      console-tools/loadkmap.o
  CC      console-tools/openvt.o
  CC      console-tools/reset.o
  CC      console-tools/resize.o
  CC      console-tools/setconsole.o
  CC      console-tools/setkeycodes.o
  CC      console-tools/setlogcons.o
  CC      console-tools/showkey.o
  AR      console-tools/lib.a
  LD      coreutils/built-in.o
  CC      coreutils/basename.o
  CC      coreutils/buddyinfo.o
  CC      coreutils/cal.o
  CC      coreutils/cat.o
  CC      coreutils/catv.o
  CC      coreutils/chgrp.o
  CC      coreutils/chmod.o
  CC      coreutils/chown.o
  CC      coreutils/chroot.o
  CC      coreutils/cksum.o
  CC      coreutils/comm.o
  CC      coreutils/condmv.o
  CC      coreutils/cp.o
  CC      coreutils/cut.o
  CC      coreutils/date.o
  CC      coreutils/dd.o
  CC      coreutils/df.o
  CC      coreutils/dfrm.o
coreutils/dfrm.c: In function 'dfrm_main':
coreutils/dfrm.c:39:11: warning: variable 'opt' set but not used [-Wunused-but-set-variable]
  uint32_t opt;
           ^~~
  CC      coreutils/dirname.o
  CC      coreutils/dos2unix.o
  CC      coreutils/du.o
  CC      coreutils/echo.o
  CC      coreutils/env.o
  CC      coreutils/expand.o
  CC      coreutils/expr.o
  CC      coreutils/false.o
  CC      coreutils/findpid.o
coreutils/findpid.c: In function 'findpid_main':
coreutils/findpid.c:40:64: warning: passing argument 2 of 'strcmp' from incompatible pointer type [-Wincompatible-pointer-types]
                  || (p->argv0 && strcmp(bb_basename(p->argv0), argv) == 0)
                                                                ^~~~
In file included from ../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/string.h:22,
                 from include/libbb.h:35,
                 from coreutils/findpid.c:23:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/string.h:37:27: note: expected 'const char *' but argument is of type 'char **'
 int strcmp (const char *, const char *);
                           ^~~~~~~~~~~~
coreutils/findpid.c:30:9: warning: unused variable 'pidList' [-Wunused-variable]
  pid_t* pidList;
         ^~~~~~~
  CC      coreutils/fold.o
  CC      coreutils/fsync.o
  CC      coreutils/head.o
  CC      coreutils/hostid.o
  CC      coreutils/id.o
  CC      coreutils/install.o
  CC      coreutils/ln.o
  CC      coreutils/logname.o
  CC      coreutils/ls.o
  CC      coreutils/md5_sha1_sum.o
  CC      coreutils/mkdir.o
  CC      coreutils/mkfifo.o
  CC      coreutils/mknod.o
  CC      coreutils/mv.o
  CC      coreutils/nice.o
  CC      coreutils/nohup.o
  CC      coreutils/od.o
  CC      coreutils/printenv.o
  CC      coreutils/printf.o
  CC      coreutils/pwd.o
  CC      coreutils/readlink.o
  CC      coreutils/realpath.o
  CC      coreutils/rm.o
  CC      coreutils/rmdir.o
  CC      coreutils/seq.o
  CC      coreutils/shuf.o
  CC      coreutils/sleep.o
  CC      coreutils/sort.o
  CC      coreutils/split.o
  CC      coreutils/stat.o
  CC      coreutils/stty.o
  CC      coreutils/sum.o
  CC      coreutils/sync.o
  CC      coreutils/tac.o
  CC      coreutils/tail.o
  CC      coreutils/tee.o
  CC      coreutils/test.o
  CC      coreutils/test_ptr_hack.o
  CC      coreutils/touch.o
  CC      coreutils/tr.o
  CC      coreutils/true.o
  CC      coreutils/truncate.o
  CC      coreutils/tty.o
  CC      coreutils/uname.o
  CC      coreutils/uniq.o
  CC      coreutils/unlink.o
  CC      coreutils/usleep.o
  CC      coreutils/uudecode.o
  CC      coreutils/uuencode.o
  CC      coreutils/wc.o
  CC      coreutils/whoami.o
  CC      coreutils/yes.o
  AR      coreutils/lib.a
  LD      coreutils/libcoreutils/built-in.o
  CC      coreutils/libcoreutils/cp_mv_stat.o
  CC      coreutils/libcoreutils/getopt_mk_fifo_nod.o
  AR      coreutils/libcoreutils/lib.a
  LD      debianutils/built-in.o
  CC      debianutils/mktemp.o
  CC      debianutils/pipe_progress.o
  CC      debianutils/run_parts.o
  CC      debianutils/start_stop_daemon.o
  CC      debianutils/which.o
  AR      debianutils/lib.a
  LD      e2fsprogs/built-in.o
  CC      e2fsprogs/chattr.o
  CC      e2fsprogs/e2fs_lib.o
  CC      e2fsprogs/fsck.o
  CC      e2fsprogs/lsattr.o
  AR      e2fsprogs/lib.a
  LD      editors/built-in.o
  CC      editors/awk.o
  CC      editors/cmp.o
  CC      editors/diff.o
  CC      editors/ed.o
  CC      editors/patch.o
  CC      editors/sed.o
  CC      editors/vi.o
  AR      editors/lib.a
  LD      eperd/built-in.o
  CC      eperd/condmv.o
  CC      eperd/eooqd.o
eperd/eooqd.c: In function 'post_results':
eperd/eooqd.c:812:8: warning: passing argument 1 of 'free' discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
   free(fn_header); fn_header= NULL;
        ^~~~~~~~~
In file included from ../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdlib.h:22,
                 from include/libbb.h:32,
                 from eperd/eooqd.c:28:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/stdlib.h:41:12: note: expected 'void *' but argument is of type 'const char *'
 void free (void *);
            ^~~~~~
eperd/eooqd.c:813:8: warning: passing argument 1 of 'free' discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
   free(fn_session_id); fn_session_id= NULL;
        ^~~~~~~~~~~~~
In file included from ../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdlib.h:22,
                 from include/libbb.h:32,
                 from eperd/eooqd.c:28:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/stdlib.h:41:12: note: expected 'void *' but argument is of type 'const char *'
 void free (void *);
            ^~~~~~
eperd/eooqd.c:814:8: warning: passing argument 1 of 'free' discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
   free(fn_ooq_sent); fn_ooq_sent= NULL;
        ^~~~~~~~~~~
In file included from ../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdlib.h:22,
                 from include/libbb.h:32,
                 from eperd/eooqd.c:28:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/stdlib.h:41:12: note: expected 'void *' but argument is of type 'const char *'
 void free (void *);
            ^~~~~~
eperd/eooqd.c: In function 'checkQueue':
eperd/eooqd.c:524:18: warning: 'slot' may be used uninitialized in this function [-Wmaybe-uninitialized]
  if (state->slots[slot].cmdstate != NULL)
                  ^
eperd/eooqd.c:338:25: note: 'slot' was declared here
  int i, argc, fd, skip, slot;
                         ^~~~
  CC      eperd/eperd.o
eperd/eperd.c:477:13: warning: 'safe_setenv4' defined but not used [-Wunused-function]
 static void safe_setenv4(char **pvar_val, const char *var, const char *val /*, int len*/)
             ^~~~~~~~~~~~
eperd/eperd.c: In function 'SynchronizeFile':
eperd/eperd.c:835:16: warning: 'last' may be used uninitialized in this function [-Wmaybe-uninitialized]
   last->cl_Next= line;
   ~~~~~~~~~~~~~^~~~~~
eperd/eperd.c:787:12: note: 'last' was declared here
  CronLine *last;
            ^~~~
  CC      eperd/evhttpget.o
  CC      eperd/evntp.o
  CC      eperd/evping.o
  CC      eperd/evsslgetcert.o
  CC      eperd/evtdig.o
In file included from eperd/evtdig.c:58:
eperd/tcputil.h:8:10: fatal error: openssl/ssl.h: No such file or directory
 #include <openssl/ssl.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
make[5]: *** [scripts/Makefile.build:198: eperd/evtdig.o] Error 1
make[4]: *** [Makefile:743: eperd] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/ripe-atlas-probe-busybox-2.2.1'
make[3]: *** [Makefile:74: /openwrt/build_dir/target-mips_24kc_musl/ripe-atlas-probe-busybox-2.2.1/.built] Error 2
```
