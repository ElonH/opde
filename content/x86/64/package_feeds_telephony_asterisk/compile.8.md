---
title: "compile.8"
date: 2021-05-06 05:08:54.017294
hidden: false
draft: false
weight: -8
---

build number: `8`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/telephony/asterisk/compile -j$(nproc) || make package/feeds/telephony/asterisk/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/030-GNU-GLOB-exts-only-on-glibc.patch using plaintext: 
patching file res/ael/ael.flex
patching file res/ael/ael_lex.c

Applying ./patches/053-musl-mutex-init.patch using plaintext: 
patching file include/asterisk/lock.h

Applying ./patches/100-build-reproducibly.patch using plaintext: 
patching file build_tools/make_build_h
patching file Makefile

Applying ./patches/110-fix-astmm.patch using plaintext: 
patching file include/asterisk/compat.h

Applying ./patches/130-eventfd.patch using plaintext: 
patching file configure.ac

Applying ./patches/140-use-default-lua.patch using plaintext: 
patching file configure.ac

Applying ./patches/150-musl-12x.patch using plaintext: 
patching file include/asterisk/compat.h
patching file utils/db1-ast/include/db.h
Generating the configure script for Asterisk ...
Generating the configure script for menuselect ...
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/x86_64
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-openwrt-linux-gnu
checking for x86_64-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
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
checking whether char is unsigned... no
checking for x86_64-openwrt-linux-uname... no
checking for uname... /usr/bin/uname
configure: WARNING: using cross tools not prefixed with host triplet
checking for x86_64-openwrt-linux-gcc... (cached) ccache_cc
checking for x86_64-openwrt-linux-g++... ccache_cxx
checking for x86_64-openwrt-linux-ld... x86_64-openwrt-linux-musl-ld
checking for x86_64-openwrt-linux-ranlib... x86_64-openwrt-linux-musl-gcc-ranlib
checking whether we are using the GNU C++ compiler... yes
checking whether ccache_cxx accepts -g... yes
checking how to run the C preprocessor... ccache_cc -E
checking how to run the C++ preprocessor... ccache_cxx -E
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for egrep... grep -E
checking for ld used by ccache_cc... x86_64-openwrt-linux-musl-ld
checking if the linker (x86_64-openwrt-linux-musl-ld) is GNU ld... yes
checking for gawk... gawk
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether ln -s works... yes
checking for x86_64-openwrt-linux-ranlib... (cached) x86_64-openwrt-linux-musl-gcc-ranlib
checking for GNU make... make
checking for egrep... (cached) /openwrt/staging_dir/host/bin/grep -E
checking for x86_64-openwrt-linux-strip... x86_64-openwrt-linux-musl-strip
checking for x86_64-openwrt-linux-ar... x86_64-openwrt-linux-musl-gcc-ar
checking for bison... /openwrt/staging_dir/host/bin/bison
checking for cmp... /usr/bin/cmp
checking for cat... /usr/bin/cat
checking for cut... /usr/bin/cut
checking for flex... /openwrt/staging_dir/host/bin/flex
checking for grep... (cached) /openwrt/staging_dir/host/bin/grep
checking for python2.7... /usr/bin/python2.7
checking for find... /openwrt/staging_dir/host/bin/find
checking for basename... /usr/bin/basename
checking for dirname... /usr/bin/dirname
checking for sh... /bin/bash
checking for ln... /usr/bin/ln
checking for doxygen... :
checking for dot... :
checking for wget... /openwrt/staging_dir/host/bin/wget
checking for curl... /usr/bin/curl
checking for xmllint... /openwrt/staging_dir/hostpkg/bin/xmllint
checking for xmlstarlet... no
checking for xml... no
checking for bash... /bin/bash
checking for git... /openwrt/staging_dir/host/bin/git
checking for alembic... :
checking for bzip2... /openwrt/staging_dir/hostpkg/bin/bzip2
checking for tar... /openwrt/staging_dir/host/bin/tar
checking for patch... /openwrt/staging_dir/host/bin/patch
checking for sed... (cached) /openwrt/staging_dir/host/bin/sed
checking for nm... /usr/bin/nm
checking for ldconfig... (cached) no
checking for sha1sum... /usr/bin/sha1sum
checking for openssl... /openwrt/staging_dir/host/bin/openssl
checking for bison that supports parse-param... /openwrt/staging_dir/host/bin/bison
checking for x86_64-openwrt-linux-soxmix... no
checking for soxmix... no
checking for md5... no
checking for md5sum... md5sum
checking for a sed that does not truncate output... (cached) /openwrt/staging_dir/host/bin/sed
checking whether ccache_cc is Clang... no
checking whether pthreads work with -pthread... yes
checking for joinable pthread attribute... PTHREAD_CREATE_JOINABLE
checking whether more special flags are required for pthreads... no
checking for PTHREAD_PRIO_INHERIT... yes
checking for RAII support... checking for gcc -fnested-functions... no
checking for clang strsep/strcmp optimization... no
checking for gawk... (cached) gawk
checking for curl-config... /openwrt/staging_dir/target-x86_64_musl/usr/bin/curl-config
checking for the version of libcurl... 7.76.0
checking for libcurl >= version 7.10.1... yes
checking whether libcurl is usable... yes
checking for curl_free... yes
checking for size_t... yes
checking for working alloca.h... yes
checking for alloca... yes
checking for dirent.h that defines DIR... yes
checking for library containing opendir... none required
checking for ANSI C header files... (cached) yes
checking for sys/wait.h that is POSIX.1 compatible... yes
checking for sys/types.h... (cached) yes
checking for netinet/in.h... yes
checking for arpa/nameser.h... yes
checking for netdb.h... yes
checking for resolv.h... yes
checking for arpa/nameser.h... (cached) yes
checking assert.h usability... yes
checking assert.h presence... yes
checking for assert.h... yes
checking ctype.h usability... yes
checking ctype.h presence... yes
checking for ctype.h... yes
checking dlfcn.h usability... yes
checking dlfcn.h presence... yes
checking for dlfcn.h... yes
checking errno.h usability... yes
checking errno.h presence... yes
checking for errno.h... yes
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking float.h usability... yes
checking float.h presence... yes
checking for float.h... yes
checking grp.h usability... yes
checking grp.h presence... yes
checking for grp.h... yes
checking for inttypes.h... (cached) yes
checking limits.h usability... yes
checking limits.h presence... yes
checking for limits.h... yes
checking locale.h usability... yes
checking locale.h presence... yes
checking for locale.h... yes
checking math.h usability... yes
checking math.h presence... yes
checking for math.h... yes
checking pwd.h usability... yes
checking pwd.h presence... yes
checking for pwd.h... yes
checking for netinet/in.h... (cached) yes
checking regex.h usability... yes
checking regex.h presence... yes
checking for regex.h... yes
checking sched.h usability... yes
checking sched.h presence... yes
checking for sched.h... yes
checking stdarg.h usability... yes
checking stdarg.h presence... yes
checking for stdarg.h... yes
checking for stdint.h... (cached) yes
checking stdio.h usability... yes
checking stdio.h presence... yes
checking for stdio.h... yes
checking for stdlib.h... (cached) yes
checking for string.h... (cached) yes
checking syslog.h usability... yes
checking syslog.h presence... yes
checking for syslog.h... yes
checking sys/file.h usability... yes
checking sys/file.h presence... yes
checking for sys/file.h... yes
checking sys/ioctl.h usability... yes
checking sys/ioctl.h presence... yes
checking for sys/ioctl.h... yes
checking sys/param.h usability... yes
checking sys/param.h presence... yes
checking for sys/param.h... yes
checking sys/resource.h usability... yes
checking sys/resource.h presence... yes
checking for sys/resource.h... yes
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking for sys/stat.h... (cached) yes
checking sys/time.h usability... yes
checking sys/time.h presence... yes
checking for sys/time.h... yes
checking for sys/types.h... (cached) yes
checking sys/un.h usability... yes
checking sys/un.h presence... yes
checking for sys/un.h... yes
checking termios.h usability... yes
checking termios.h presence... yes
checking for termios.h... yes
checking time.h usability... yes
checking time.h presence... yes
checking for time.h... yes
checking for unistd.h... (cached) yes
checking arpa/inet.h usability... yes
checking arpa/inet.h presence... yes
checking for arpa/inet.h... yes
checking libintl.h usability... yes
checking libintl.h presence... yes
checking for libintl.h... yes
checking malloc.h usability... yes
checking malloc.h presence... yes
checking for malloc.h... yes
checking for netdb.h... (cached) yes
checking stddef.h usability... yes
checking stddef.h presence... yes
checking for stddef.h... yes
checking for strings.h... (cached) yes
checking sys/event.h usability... no
checking sys/event.h presence... no
checking for sys/event.h... no
checking utime.h usability... yes
checking utime.h presence... yes
checking for utime.h... yes
checking pkg-config is at least version 0.9.0... yes
checking for LIBEDIT... yes
checking for Testing for libedit unicode support... yes
checking for uuid_generate_random in -luuid... yes
checking uuid/uuid.h usability... yes
checking uuid/uuid.h presence... yes
checking for uuid/uuid.h... yes
checking for JANSSON... yes
checking for clock_gettime in -lrt... yes
checking for x86_64-openwrt-linux-xml2-config... /openwrt/staging_dir/target-x86_64_musl/host/bin/x86_64-openwrt-linux-xml2-config
checking xlocale.h usability... no
checking xlocale.h presence... no
checking for xlocale.h... no
checking winsock.h usability... no
checking winsock.h presence... no
checking for winsock.h... no
checking winsock2.h usability... no
checking winsock2.h presence... no
checking for winsock2.h... no
checking sys/poll.h usability... yes
checking sys/poll.h presence... yes
checking for sys/poll.h... yes
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking for stdbool.h that conforms to C99... yes
checking for _Bool... yes
checking for an ANSI C-conforming const... yes
checking for uid_t in sys/types.h... yes
checking for inline... inline
checking for long double with more range or precision than double... yes
checking for mode_t... yes
checking for off_t... yes
checking for pid_t... yes
checking for size_t... (cached) yes
checking for struct stat.st_blksize... yes
checking for struct ucred.uid... yes
checking for struct ucred.cr_uid... no
checking for struct sockpeercred.uid... no
checking for struct ifreq.ifr_ifru.ifru_hwaddr... yes
checking whether time.h and sys/time.h may both be included... yes
checking whether struct tm is in sys/time.h or time.h... time.h
checking for working volatile... yes
checking for ptrdiff_t... yes
checking for struct stat.st_mtim... yes
checking for struct stat.st_mtimensec... no
checking for struct stat.st_mtimespec... no
checking for unistd.h... (cached) yes
checking for working chown... no
checking whether closedir returns void... yes
checking for error_at_line... no
checking vfork.h usability... no
checking vfork.h presence... no
checking for vfork.h... no
checking for fork... yes
checking for vfork... yes
checking for working fork... cross
configure: WARNING: result yes guessed because of cross compilation
checking for working vfork... (cached) yes
checking for _LARGEFILE_SOURCE value needed for large files... no
checking whether ccache_cc needs -traditional... no
checking for working memcmp... (cached) yes
checking for stdlib.h... (cached) yes
checking for unistd.h... (cached) yes
checking for sys/param.h... (cached) yes
checking for utime.h... (cached) yes
checking for getpagesize... yes
checking for working mmap... no
checking sys/select.h usability... yes
checking sys/select.h presence... yes
checking for sys/select.h... yes
checking for sys/socket.h... (cached) yes
checking types of arguments for select... int,fd_set *,struct timeval *
checking whether lstat correctly handles trailing slash... (cached) yes
checking whether stat accepts an empty string... (cached) no
checking for working strcoll... no
checking for strftime... (cached) yes
checking for working strnlen... yes
checking for working strtod... no
checking for pow... yes
checking whether utime accepts a null argument... guessing yes
checking for vprintf... yes
checking for _doprnt... no
checking for asprintf... yes
checking for atexit... yes
checking for closefrom... no
checking for dup2... yes
checking for eaccess... yes
checking for endpwent... yes
checking for euidaccess... yes
checking for ffsll... yes
checking for ftruncate... yes
checking for getcwd... (cached) yes
checking for gethostbyname... yes
checking for gethostname... yes
checking for getloadavg... yes
checking for gettimeofday... (cached) yes
checking for glob... yes
checking for ioperm... yes
checking for inet_ntoa... yes
checking for isascii... yes
checking for memchr... yes
checking for memmove... yes
checking for memset... yes
checking for mkdir... yes
checking for mkdtemp... yes
checking for munmap... yes
checking for newlocale... yes
checking for pipe2... yes
checking for ppoll... yes
checking for putenv... yes
checking for re_comp... no
checking for regcomp... yes
checking for select... yes
checking for setenv... yes
checking for socket... yes
checking for strcasecmp... yes
checking for strcasestr... yes
checking for strchr... yes
checking for strcspn... yes
checking for strdup... yes
checking for strerror... (cached) yes
checking for strlcat... yes
checking for strlcpy... yes
checking for strncasecmp... yes
checking for strndup... yes
checking for strnlen... yes
checking for strrchr... yes
checking for strsep... yes
checking for strspn... yes
checking for strstr... yes
checking for strtod... (cached) no
checking for strtol... yes
checking for strtold... yes
checking for strtoq... no
checking for unsetenv... yes
checking for uselocale... yes
checking for utime... yes
checking for vasprintf... yes
checking for getpeereid... no
checking for sysctl... no
checking for swapctl... no
checking for malloc_trim... no
checking for htonll... no
checking for ntohll... no
checking for sqrt in -lm... yes
checking for exp2... yes
checking for log2... yes
checking for exp10... yes
checking for log10... yes
checking for sin... yes
checking for cos... yes
checking for tan... yes
checking for asin... yes
checking for acos... yes
checking for atan... yes
checking for atan2... yes
checking for pow... (cached) yes
checking for rint... yes
checking for exp... yes
checking for log... yes
checking for remainder... yes
checking for fmod... yes
checking for round... yes
checking for roundf... yes
checking for trunc... yes
checking for floor... yes
checking for ceil... yes
checking for exp2l... yes
checking for log2l... yes
checking for exp10l... yes
checking for log10l... yes
checking for sinl... yes
checking for cosl... yes
checking for tanl... yes
checking for asinl... yes
checking for acosl... yes
checking for atanl... yes
checking for atan2l... yes
checking for powl... yes
checking for sqrtl... yes
checking for rintl... yes
checking for expl... yes
checking for logl... yes
checking for remainderl... yes
checking for fmodl... yes
checking for roundl... yes
checking for truncl... yes
checking for floorl... yes
checking for ceill... yes
checking for LLONG_MAX in limits.h... yes
checking for timersub in time.h... yes
checking for a version of GNU ld that supports the --dynamic-list flag... yes
checking for sys/poll.h... (cached) yes
checking for inet_aton... yes
checking for IP_PKTINFO... yes
checking for library containing gethostbyname_r... none required
checking for gethostbyname_r with 6 arguments... yes
checking for gethostbyname_r with 5 arguments... no
checking byteswap.h usability... yes
checking byteswap.h presence... yes
checking for byteswap.h... yes
checking for __swap16 variant of <sys/endian.h> byteswapping macros... no
checking for bswap16 variant of <sys/endian.h> byteswapping macros... no
checking for locale_t in locale.h... yes
checking for O_EVTONLY in fcntl.h... no
checking for O_SYMLINK in fcntl.h... no
checking for PTHREAD_RWLOCK_INITIALIZER in pthread.h... yes
checking for PTHREAD_RWLOCK_PREFER_WRITER_NP in pthread.h... no
checking for PTHREAD_MUTEX_RECURSIVE_NP in pthread.h... no
checking for PTHREAD_MUTEX_ADAPTIVE_NP in pthread.h... no
checking for pthread_spinlock_t in pthread.h... yes
checking for pthread_rwlock_timedwrlock() in pthread.h... yes
checking for working unnamed semaphores... cross-compile
configure: WARNING: result yes guessed because of cross compilation
checking if PTHREAD_ONCE_INIT needs braces... no
checking for PTHREAD_RECURSIVE_MUTEX_INITIALIZER_NP in pthread.h... no
checking whether we can compare a mutex to its initial value... no
checking sys/thr.h usability... no
checking sys/thr.h presence... no
checking for sys/thr.h... no
checking for compiler sync operations... yes
checking for compiler atomic operations... yes
checking if your system printf is NULL-safe.... unknown
checking if socket() accepts SOCK_NONBLOCK... cross-compile
checking if we can increase the maximum select-able file descriptor... cross-compile
checking if we have usable eventfd support... yes
checking for compiler 'attribute pure' support... yes
checking for compiler 'attribute malloc' support... yes
checking for compiler 'attribute const' support... yes
checking for compiler 'attribute unused' support... yes
checking for compiler 'attribute always_inline' support... no
checking for compiler 'attribute deprecated' support... yes
checking for compiler 'attribute sentinel' support... yes
checking for compiler 'attribute warn_unused_result' support... yes
checking for compiler 'attribute may_alias' support... yes
checking for compiler 'attribute constructor' support... yes
checking for compiler 'attribute destructor' support... yes
checking for compiler 'attribute noreturn' support... yes
checking for -fsanitize=address support... yes
checking for -fsanitize=thread support... yes
checking for -fsanitize=leak support... yes
checking for -fsanitize=undefined support... yes
checking for -Wdeclaration-after-statement support... yes
checking for -Wtrampolines support... yes
checking for _FORTIFY_SOURCE support... yes
checking for -fno-strict-overflow... yes
checking for -Wno-format-truncation... yes
checking for -Wno-stringop-truncation... yes
checking for -Wshadow... yes
checking for -march=native support... yes
checking whether to use rpath... not needed
checking for sysinfo... yes
checking for library containing res_9_ninit... no
checking for res_ninit... no
checking for BIND_8_COMPAT required... no
checking for GLOB_NOMAGIC in glob.h... no
checking for GLOB_BRACE in glob.h... no
checking for RTLD_NOLOAD in dlfcn.h... yes
checking for IP_MTU_DISCOVER in netinet/in.h... yes
checking size of int... (cached) 4
checking size of long... (cached) 8
checking size of long long... (cached) 8
checking size of char *... 8
checking size of long... (cached) 8
checking size of long long... (cached) 8
checking size of fd_set.fds_bits... (cached) 8
checking for dladdr in dlfcn.h... yes
checking for snd_pcm_open in -lasound... yes
checking alsa/asoundlib.h usability... yes
checking alsa/asoundlib.h presence... yes
checking for alsa/asoundlib.h... yes
checking for bfd_openr in -lbfd... yes
checking bfd.h usability... yes
checking bfd.h presence... yes
checking for bfd.h... yes
checking for cap_from_text in -lcap... yes
checking sys/capability.h usability... yes
checking sys/capability.h presence... yes
checking for sys/capability.h... yes
checking for DAHDI_RESET_COUNTERS in dahdi/user.h... no
checking for DAHDI_DEFAULT_MTU_MRU in dahdi/user.h... no
checking for DAHDI_CODE in dahdi/user.h... no
checking for DAHDI_POLICY_HALF_FULL in dahdi/user.h... no
checking for enhanced dahdi vmwi support... no
checking if "int foo = DAHDI_ECHOCANCEL_FAX_MODE" compiles using dahdi/user.h... no
checking for getifaddrs() support... yes
checking for timerfd support... yes
checking for iconv_open in -liconv... yes
checking iconv.h usability... yes
checking iconv.h presence... yes
checking for iconv.h... yes
checking for icaltimezone_get_utc_timezone in -lical... yes
checking libical/ical.h usability... yes
checking libical/ical.h presence... yes
checking for libical/ical.h... yes
checking for iks_start_sasl in -liksemel... yes
checking iksemel.h usability... yes
checking iksemel.h presence... yes
checking for iksemel.h... yes
checking for system c-client library...... yes
checking for SQLConnect in -liodbc... no
checking for inotify_init in -lc... yes
checking sys/inotify.h usability... yes
checking sys/inotify.h presence... yes
checking for sys/inotify.h... yes
checking for jack_activate in -ljack... no
checking for kqueue in -lc... no
checking for kevent64... no
checking for ldap_initialize in -lldap... yes
checking ldap.h usability... yes
checking ldap.h presence... yes
checking for ldap.h... yes
checking for x86_64-openwrt-linux-mysql_config... no
checking for mysql_config... /openwrt/staging_dir/target-x86_64_musl/host/bin/mysql_config
checking for MySQL client bool support... no
checking for MySQL client my_bool support... yes
checking for x86_64-openwrt-linux-neon-config... (cached) /openwrt/staging_dir/target-x86_64_musl/usr/bin/neon-config
checking for x86_64-openwrt-linux-neon-config... (cached) /openwrt/staging_dir/target-x86_64_musl/usr/bin/neon-config
checking for x86_64-openwrt-linux-net-snmp-config... no
checking for net-snmp-config... /openwrt/staging_dir/target-x86_64_musl/usr/bin/net-snmp-config
checking for ub_ctx_delete in -lunbound... yes
checking unbound.h usability... yes
checking unbound.h presence... yes
checking for unbound.h... yes
checking for unbound version >= 1.5... yes (guessed for cross-compile)
checking for SQLConnect in -lodbc... yes
checking sql.h usability... yes
checking sql.h presence... yes
checking for sql.h... yes
checking for ogg_stream_init in -logg... yes
checking ogg/ogg.h usability... yes
checking ogg/ogg.h presence... yes
checking for ogg/ogg.h... yes
checking for ba2str in -lbluetooth... yes
checking bluetooth/bluetooth.h usability... yes
checking bluetooth/bluetooth.h presence... yes
checking for bluetooth/bluetooth.h... yes
checking for bs_version in -lbeanstalk... no
checking linux/soundcard.h usability... yes
checking linux/soundcard.h presence... yes
checking for linux/soundcard.h... yes
checking for x86_64-openwrt-linux-pg_config... no
checking for pg_config... /openwrt/staging_dir/target-x86_64_musl/usr/bin/pg_config
checking for PQescapeStringConn in -lpq... yes
checking for pg_encoding_to_char within Postgres headers... yes
checking for PJPROJECT... yes
checking for pjsip_dlg_create_uas_and_inc_lock in -lpjsip... yes
checking pjsip.h usability... yes
checking pjsip.h presence... yes
checking for pjsip.h... yes
checking for pjsip_tsx_create_uac2 in -lpjsip... yes
checking for pjsip.h... (cached) yes
checking if "pjmedia_mod_offer_flag flag = PJMEDIA_SDP_NEG_ALLOW_MEDIA_CHANGE" compiles using pjmedia.h... yes
checking for pjsip_get_dest_info in -lpjsip... yes
checking for pjsip.h... (cached) yes
checking for pj_ssl_cert_load_from_files2 in -lpj... yes
checking pjlib.h usability... yes
checking pjlib.h presence... yes
checking for pjlib.h... yes
checking for pjsip_endpt_set_ext_resolver in -lpjsip... yes
checking for pjsip.h... (cached) yes
checking if "struct pjsip_tls_setting setting; int proto; proto = setting.proto;" compiles using pjsip.h... yes
checking if "pjsip_cfg()->endpt.accept_multiple_sdp_answers = 0;" compiles using pjsip.h... yes
checking if "pjsip_cfg()->endpt.use_compact_form = PJ_TRUE;" compiles using pjsip.h... yes
checking if "struct pjsip_tpselector sel; sel.disable_connection_reuse = PJ_TRUE;" compiles using pjsip.h... yes
checking if "struct pjsip_oauth_credential credential;" compiles using pjsip.h... yes
checking for pjproject on_valid_pair callback... yes
checking for pjsip_evsub_add_ref in -lpjsip... yes
checking for pjsip.h... (cached) yes
checking for pjsip_inv_add_ref in -lpjsip... yes
checking for pjsip.h... (cached) yes
checking for pjsip_auth_clt_deinit in -lpjsip... yes
checking for pjsip.h... (cached) yes
checking for pjsip_tsx_layer_find_tsx2 in -lpjsip... yes
checking for pjsip.h... (cached) yes
checking for poptStrerror in -lpopt... yes
checking popt.h usability... yes
checking popt.h presence... yes
checking for popt.h... yes
checking for PORTAUDIO... yes
checking for pri_connected_line_update in -lpri... no
checking for resample_open in -lresample... no
checking for fftw_malloc in -lfftw3... no
checking for sf_open in -lsndfile... yes
checking sndfile.h usability... yes
checking sndfile.h presence... yes
checking for sndfile.h... yes
checking for minimum version of SpanDSP... yes
checking for span_set_message_handler in -lspandsp... yes
checking spandsp.h usability... yes
checking spandsp.h presence... yes
checking for spandsp.h... yes
checking for t38_terminal_init in -lspandsp... yes
checking for spandsp.h... (cached) yes
checking for ss7_set_isup_timer in -lss7... no
checking for openr2_chan_new in -lopenr2... no
checking for opus_encoder_create in -lopus... yes
checking opus/opus.h usability... yes
checking opus/opus.h presence... yes
checking for opus/opus.h... yes
checking for op_open_callbacks in -lopusfile... no
checking for luaL_newstate in -llua... yes
checking lua.h usability... yes
checking lua.h presence... yes
checking for lua.h... yes
checking for codec2_create in -lcodec2... no
checking for cpg_join in -lcpg... no
checking for corosync_cfg_state_track in -lcfg... no
checking for speex_encode in -lspeex... yes
checking speex/speex.h usability... yes
checking speex/speex.h presence... yes
checking for speex/speex.h... yes
checking for speex_preprocess_ctl in -lspeex... no
checking for speex_preprocess_ctl in -lspeexdsp... yes
checking for speex/speex.h... (cached) yes
checking for sqlite3_open in -lsqlite3... yes
checking sqlite3.h usability... yes
checking sqlite3.h presence... yes
checking for sqlite3.h... yes
checking for crypt in -lcrypt... yes
checking crypt.h usability... yes
checking crypt.h presence... yes
checking for crypt.h... yes
checking for crypt... yes
checking for crypt_r in -lcrypt... yes
checking for AES_encrypt in -lcrypto... yes
checking openssl/aes.h usability... yes
checking openssl/aes.h presence... yes
checking for openssl/aes.h... yes
checking for SSL_connect in -lssl... yes
checking openssl/ssl.h usability... yes
checking openssl/ssl.h presence... yes
checking for openssl/ssl.h... yes
checking for BIO_meth_new in -lssl... yes
checking for openssl/ssl.h... (cached) yes
checking for srtp_init in -lsrtp2... yes
checking srtp2/srtp.h usability... yes
checking srtp2/srtp.h presence... yes
checking for srtp2/srtp.h... yes
checking for the ability of -lsrtp2 to be linked in a shared object... yes
checking for srtp_crypto_policy_set_aes_cm_256_hmac_sha1_80 in -lsrtp2... yes
checking for srtp_crypto_policy_set_aes_cm_192_hmac_sha1_80 in -lsrtp2... yes
checking for srtp_crypto_policy_set_aes_gcm_128_8_auth in -lsrtp2... yes
checking for srtp_shutdown in -lsrtp2... yes
checking for srtp2/srtp.h... (cached) yes
checking for srtp_get_version_string in -lsrtp2... yes
checking for srtp2/srtp.h... (cached) yes
checking for GMIME... no
checking for GMIME... no
checking for GMIME... no
checking for GMIME... no
checking for GMIME... no
checking for malloc in -lhoard... no
checking for tone_zone_find_by_num in -ltonezone... no
checking for tone_zone_find in -ltonezone... no
checking for vorbis_info_init in -lvorbis... yes
checking vorbis/codec.h usability... yes
checking vorbis/codec.h presence... yes
checking for vorbis/codec.h... yes
checking for OV_CALLBACKS_NOCLOSE declared in vorbis/vorbisfile.h... yes
checking for compress in -lz... yes
checking zlib.h usability... yes
checking zlib.h presence... yes
checking for zlib.h... yes
checking whether ODBC has support for Unicode types... yes
checking linux/compiler.h usability... no
checking linux/compiler.h presence... no
checking for linux/compiler.h... no
checking for linux/ixjuser.h... no
checking for MSG_NOSIGNAL in sys/socket.h... yes
checking for SO_NOSIGPIPE in sys/socket.h... no
checking for IMG_Load in -lSDL_image... no
checking for sws_getContext in -lavcodec... no
checking linux/videodev.h usability... no
checking linux/videodev.h presence... no
checking for linux/videodev.h... no
checking for XOpenDisplay in -lX11... no
checking for XOpenDisplay in -lX11... (cached) no
checking for SYSTEMD... no
checking for LOG_AUTH in syslog.h... yes
checking for LOG_AUTHPRIV in syslog.h... yes
checking for LOG_CRON in syslog.h... yes
checking for LOG_DAEMON in syslog.h... yes
checking for LOG_FTP in syslog.h... yes
checking for LOG_KERN in syslog.h... yes
checking for LOG_LPR in syslog.h... yes
checking for LOG_MAIL in syslog.h... yes
checking for LOG_NEWS in syslog.h... yes
checking for LOG_SYSLOG in syslog.h... yes
checking for LOG_UUCP in syslog.h... yes
checking for mandatory modules:  ALSA BLUETOOTH CAP DAHDI GSM ILBC ICAL IKSEMEL IMAP_TK LIBEDIT LIBXML2 LUA NETSNMP OGG PGSQL PJPROJECT POPT PORTAUDIO PRI SPANDSP SPEEX SPEEX_PREPROCESS SPEEXDSP SQLITE3 SRTP TONEZONE UNBOUND VORBIS ZLIB... fail

configure: ***
configure: *** The DAHDI installation appears to be missing or broken.
configure: *** Either correct the installation, or run configure
configure: *** including --without-dahdi.

configure: ***
configure: *** The PRI installation appears to be missing or broken.
configure: *** Either correct the installation, or run configure
configure: *** including --without-pri.

configure: ***
configure: *** The TONEZONE installation appears to be missing or broken.
configure: *** Either correct the installation, or run configure
configure: *** including --without-tonezone.
make[3]: *** [Makefile:749: /openwrt/build_dir/target-x86_64_musl/asterisk-18.2.2/.configured_91d67d9c4b0bbd9e75147cae155a012c] Error 1
```
