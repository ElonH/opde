---
title: "compile.41"
date: 2021-06-23 23:22:00.782622
hidden: false
draft: false
weight: -41
---

build number: `41`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/freeradius3/compile -j$(nproc) || make package/feeds/packages/freeradius3/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-fix-cert-expiry.patch using plaintext: 
patching file raddb/certs/ca.cnf
patching file raddb/certs/client.cnf
patching file raddb/certs/server.cnf

Applying ./patches/002-disable-session-cache-CVE-2017-9148.patch using plaintext: 
patching file src/main/tls.c

Applying ./patches/003-freeradius-fix-error-for-expansion-of-macro.patch using plaintext: 
patching file src/include/threads.h

Applying ./patches/004-get-hostname-from-proc-in-radtest.patch using plaintext: 
patching file src/main/radtest.in

Applying ./patches/010-openssl-deprecated.patch using plaintext: 
patching file src/main/threads.c
patching file src/main/tls.c
patching file src/main/version.c
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-x86_64_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal -I m4 -I . --force 
configure.ac:26: warning: AC_INIT: not a literal: $Id$
configure.ac:2351: warning: AC_CONFIG_SUBDIRS: you should use literals
../../lib/autoconf/status.m4:1097: AC_CONFIG_SUBDIRS is expanded from...
configure.ac:2351: the top level
configure.ac:26: warning: AC_INIT: not a literal: $Id$
configure.ac:2351: warning: AC_CONFIG_SUBDIRS: you should use literals
../../lib/autoconf/status.m4:1097: AC_CONFIG_SUBDIRS is expanded from...
configure.ac:2351: the top level
autoreconf: configure.ac: tracing
configure.ac:26: warning: AC_INIT: not a literal: $Id$
configure.ac:2351: warning: AC_CONFIG_SUBDIRS: you should use literals
../../lib/autoconf/status.m4:1097: AC_CONFIG_SUBDIRS is expanded from...
configure.ac:2351: the top level
autoreconf: configure.ac: subdirectory $mysubdirs not present
autoreconf: configure.ac: not using Libtool
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-x86_64_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
configure.ac:26: warning: AC_INIT: not a literal: $Id$
configure.ac:2351: warning: AC_CONFIG_SUBDIRS: you should use literals
../../lib/autoconf/status.m4:1097: AC_CONFIG_SUBDIRS is expanded from...
configure.ac:2351: the top level
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-x86_64_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
configure.ac:26: warning: AC_INIT: not a literal: $Id$
configure.ac:2351: warning: AC_CONFIG_SUBDIRS: you should use literals
../../lib/autoconf/status.m4:1097: AC_CONFIG_SUBDIRS is expanded from...
configure.ac:2351: the top level
autoreconf: configure.ac: not using Automake
autoreconf: Leaving directory `.'
configure: loading site script /openwrt/include/site/x86_64
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-openwrt-linux-gnu
checking target system type... x86_64-openwrt-linux-gnu
checking for x86_64-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
checking whether we are using the GNU C++ compiler... yes
checking whether ccache_cxx accepts -g... yes
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
checking whether ccache_cc needs -traditional... no
checking whether we are using SUNPro C... no
checking for x86_64-openwrt-linux-ranlib... x86_64-openwrt-linux-musl-gcc-ranlib
checking if compiler is clang... no
checking for the compiler flag "-Wno-unknown-warning-option"... no
checking for the compiler flag "-Qunused-arguments"... no
checking for the compiler flag "-Wno-date-time"... yes
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking whether byte ordering is bigendian... (cached) no
checking for gmake... no
checking for make... /usr/bin/make
checking number of system cores... 
checking for git... yes
checking docdir... ${datadir}/doc/freeradius
checking logdir... /var/log
checking radacctdir... /var/db/radacct
checking raddbdir... /etc/freeradius3
checking dictdir... /usr/share/freeradius3
checking for perl... /openwrt/staging_dir/host/bin/perl
checking for snmpget... no
configure: WARNING: snmpget not found - Simultaneous-Use and checkrad may not work
checking for snmpwalk... no
configure: WARNING: snmpwalk not found - Simultaneous-Use and checkrad may not work
checking for rusers... /usr/bin/rusers
checking for locate... /openwrt/staging_dir/host/bin/locate
checking for dirname... /usr/bin/dirname
checking for grep... (cached) /openwrt/staging_dir/host/bin/grep
checking for _talloc in -ltalloc in /openwrt/staging_dir/target-x86_64_musl/usr/lib... yes
checking pthread.h usability... yes
checking pthread.h presence... yes
checking for pthread.h... yes
checking for pthread_create in -lpthread... yes
checking for the compiler flag "-pthread"... yes
checking for library containing sem_init... none required
checking for dlopen in -ldl... yes
checking for getsockname in -lsocket... no
checking for inet_aton in -lresolv... yes
checking for inet_ntoa in -lnsl... no
checking for htonl in -lws2_32... no
checking for pcap_open_live in -lpcap... yes
checking for pcap_fopen_offline... yes
checking for pcap_dump_fopen... yes
checking for pcap_create... yes
checking for pcap_activate... yes
checking for lcc_connect in -lcollectdclient... no
checking for lcc_connect in -lcollectdclient in /usr/local/lib... no
checking for lcc_connect in -lcollectdclient in /opt/lib... no
configure: WARNING: collectdclient library not found. Use --with-collectdclient-lib-dir=<path>.
checking for cap_get_proc in -lcap... yes
checking for a readline compatible library... -lreadline
checking readline.h usability... no
checking readline.h presence... no
checking for readline.h... no
checking readline/readline.h usability... yes
checking readline/readline.h presence... yes
checking for readline/readline.h... yes
checking whether readline supports history... yes
checking history.h usability... no
checking history.h presence... no
checking for history.h... no
checking readline/history.h usability... yes
checking readline/history.h presence... yes
checking for readline/history.h... yes
configure: skipping test for systemd watchdog
configure: skipping test for systemd/sd-daemon.h.
checking for talloc.h in /openwrt/staging_dir/target-x86_64_musl/usr/include/... yes
checking for dirent.h that defines DIR... yes
checking for library containing opendir... none required
checking for ANSI C header files... (cached) yes
checking whether time.h and sys/time.h may both be included... yes
checking for sys/wait.h that is POSIX.1 compatible... yes
checking arpa/inet.h usability... yes
checking arpa/inet.h presence... yes
checking for arpa/inet.h... yes
checking crypt.h usability... yes
checking crypt.h presence... yes
checking for crypt.h... yes
checking dlfcn.h usability... yes
checking dlfcn.h presence... yes
checking for dlfcn.h... yes
checking errno.h usability... yes
checking errno.h presence... yes
checking for errno.h... yes
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking features.h usability... yes
checking features.h presence... yes
checking for features.h... yes
checking fnmatch.h usability... yes
checking fnmatch.h presence... yes
checking for fnmatch.h... yes
checking getopt.h usability... yes
checking getopt.h presence... yes
checking for getopt.h... yes
checking glob.h usability... yes
checking glob.h presence... yes
checking for glob.h... yes
checking grp.h usability... yes
checking grp.h presence... yes
checking for grp.h... yes
checking for inttypes.h... (cached) yes
checking limits.h usability... yes
checking limits.h presence... yes
checking for limits.h... yes
checking linux/if_packet.h usability... yes
checking linux/if_packet.h presence... yes
checking for linux/if_packet.h... yes
checking malloc.h usability... yes
checking malloc.h presence... yes
checking for malloc.h... yes
checking netdb.h usability... yes
checking netdb.h presence... yes
checking for netdb.h... yes
checking netinet/in.h usability... yes
checking netinet/in.h presence... yes
checking for netinet/in.h... yes
checking prot.h usability... no
checking prot.h presence... no
checking for prot.h... no
checking pwd.h usability... yes
checking pwd.h presence... yes
checking for pwd.h... yes
checking resource.h usability... no
checking resource.h presence... no
checking for resource.h... no
checking semaphore.h usability... yes
checking semaphore.h presence... yes
checking for semaphore.h... yes
checking sia.h usability... no
checking sia.h presence... no
checking for sia.h... no
checking siad.h usability... no
checking siad.h presence... no
checking for siad.h... no
checking signal.h usability... yes
checking signal.h presence... yes
checking for signal.h... yes
checking stdatomic.h usability... yes
checking stdatomic.h presence... yes
checking for stdatomic.h... yes
checking stdalign.h usability... yes
checking stdalign.h presence... yes
checking for stdalign.h... yes
checking stdbool.h usability... yes
checking stdbool.h presence... yes
checking for stdbool.h... yes
checking stddef.h usability... yes
checking stddef.h presence... yes
checking for stddef.h... yes
checking for stdint.h... (cached) yes
checking stdio.h usability... yes
checking stdio.h presence... yes
checking for stdio.h... yes
checking sys/event.h usability... no
checking sys/event.h presence... no
checking for sys/event.h... no
checking sys/fcntl.h usability... yes
checking sys/fcntl.h presence... yes
checking for sys/fcntl.h... yes
checking sys/prctl.h usability... yes
checking sys/prctl.h presence... yes
checking for sys/prctl.h... yes
checking sys/procctl.h usability... no
checking sys/procctl.h presence... no
checking for sys/procctl.h... no
checking sys/ptrace.h usability... yes
checking sys/ptrace.h presence... yes
checking for sys/ptrace.h... yes
checking sys/resource.h usability... yes
checking sys/resource.h presence... yes
checking for sys/resource.h... yes
checking sys/security.h usability... no
checking sys/security.h presence... no
checking for sys/security.h... no
checking sys/select.h usability... yes
checking sys/select.h presence... yes
checking for sys/select.h... yes
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking sys/time.h usability... yes
checking sys/time.h presence... yes
checking for sys/time.h... yes
checking for sys/types.h... (cached) yes
checking sys/un.h usability... yes
checking sys/un.h presence... yes
checking for sys/un.h... yes
checking for sys/wait.h... (cached) yes
checking syslog.h usability... yes
checking syslog.h presence... yes
checking for syslog.h... yes
checking for unistd.h... (cached) yes
checking utime.h usability... yes
checking utime.h presence... yes
checking for utime.h... yes
checking utmp.h usability... yes
checking utmp.h presence... yes
checking for utmp.h... yes
checking utmpx.h usability... yes
checking utmpx.h presence... yes
checking for utmpx.h... yes
checking winsock.h usability... no
checking winsock.h presence... no
checking for winsock.h... no
checking for net/if.h... yes
checking for DH_new in -lcrypto... yes
checking for SSL_new in -lssl... yes
checking for openssl/ssl.h... yes
checking openssl/asn1.h usability... yes
checking openssl/asn1.h presence... yes
checking for openssl/asn1.h... yes
checking openssl/conf.h usability... yes
checking openssl/conf.h presence... yes
checking for openssl/conf.h... yes
checking openssl/crypto.h usability... yes
checking openssl/crypto.h presence... yes
checking for openssl/crypto.h... yes
checking openssl/err.h usability... yes
checking openssl/err.h presence... yes
checking for openssl/err.h... yes
checking openssl/evp.h usability... yes
checking openssl/evp.h presence... yes
checking for openssl/evp.h... yes
checking openssl/hmac.h usability... yes
checking openssl/hmac.h presence... yes
checking for openssl/hmac.h... yes
checking openssl/md5.h usability... yes
checking openssl/md5.h presence... yes
checking for openssl/md5.h... yes
checking openssl/md4.h usability... yes
checking openssl/md4.h presence... yes
checking for openssl/md4.h... yes
checking openssl/rand.h usability... yes
checking openssl/rand.h presence... yes
checking for openssl/rand.h... yes
checking openssl/sha.h usability... yes
checking openssl/sha.h presence... yes
checking for openssl/sha.h... yes
checking for openssl/ssl.h... (cached) yes
checking openssl/ocsp.h usability... yes
checking openssl/ocsp.h presence... yes
checking for openssl/ocsp.h... yes
checking openssl/engine.h usability... yes
checking openssl/engine.h presence... yes
checking for openssl/engine.h... yes
checking for OpenSSL version >= 0.9.7... yes
checking OpenSSL library and header version consistency... cross-compiling (assuming yes)
checking for SSL_get_client_random... yes
checking for SSL_get_server_random... yes
checking for SSL_SESSION_get_master_key... yes
checking for HMAC_CTX_new... yes
checking for HMAC_CTX_free... yes
checking for ASN1_STRING_get0_data... yes
checking for CONF_modules_load_file... yes
checking for CRYPTO_set_id_callback... no
checking for CRYPTO_set_locking_callback... no
checking for pcap.h... yes
configure: skipping test for collectd/client.h.
checking for sys/capability.h... yes
checking for off_t... yes
checking for pid_t... yes
checking for size_t... yes
checking for uid_t in sys/types.h... yes
checking for socklen_t... yes
checking for uint8_t... yes
checking for uint16_t... yes
checking for uint32_t... yes
checking for uint64_t... yes
checking for __uint128_t... yes
checking for uint128_t... no
checking for struct in6_addr... yes
checking for struct sockaddr_storage... yes
checking for struct sockaddr_in6... yes
checking for struct addrinfo... yes
checking if sig_t is defined... yes
checking for bindat... no
checking for clock_gettime... yes
checking for closefrom... no
checking for ctime_r... yes
checking for dladdr... yes
checking for fcntl... yes
checking for fopencookie... yes
checking for funopen... no
checking for getaddrinfo... (cached) yes
checking for getnameinfo... yes
checking for getopt_long... yes
checking for getpeereid... no
checking for getresuid... yes
checking for gettimeofday... (cached) yes
checking for getusershell... yes
checking for gmtime_r... yes
checking for if_indextoname... yes
checking for inet_aton... yes
checking for inet_ntop... yes
checking for inet_pton... yes
checking for initgroups... yes
checking for kqueue... no
checking for localtime_r... yes
checking for mallopt... no
checking for mkdirat... yes
checking for openat... yes
checking for pthread_sigmask... yes
checking for setlinebuf... yes
checking for setresuid... (cached) no
checking for setsid... yes
checking for setuid... yes
checking for setvbuf... yes
checking for sigaction... yes
checking for sigprocmask... yes
checking for snprintf... yes
checking for strcasecmp... yes
checking for strlcat... yes
checking for strlcpy... yes
checking for strncasecmp... yes
checking for strsep... yes
checking for strsignal... yes
checking for unlinkat... yes
checking for vdprintf... yes
checking for vsnprintf... (cached) yes
checking return type of signal handlers... void
checking for ut_xtime in struct utmpx... no
checking for ipi_addr in struct in_pktinfo... yes
checking for ipi6_addr in struct in6_pktinfo... yes
checking if htonll is defined... no
checking if htonlll is defined... no
checking for an ANSI C-conforming const... yes
checking type of OS... Linux
checking if building with -DNDEBUG... yes
checking for __thread support in compiler... no
checking for __declspec(thread) support in compiler... no
checking for _Thread_local support in compiler... no
checking for __builtin_choose_expr support in compiler... (cached) yes
checking for __builtin_types_compatible_p support in compiler... (cached) yes
checking for __builtin_bswap64 support in compiler... (cached) yes
checking for __attribute__((__bounded__)) support in compiler... (cached) no
checking for talloc_set_memlimit in -ltalloc... yes
checking for crypt in -lcrypt... yes
checking for crypt_r in -lcrypt... yes
checking for setkey in -lcipher... no
checking for execinfo.h... no
checking for execinfo.h in /usr/local/include/... no
checking for execinfo.h in /opt/include/... no
checking for pcre.h... yes
checking for pcre_compile in -lpcre... yes
checking for library containing __atomic_load_4... none required
checking gethostbyaddr_r() syntax... GNU-style
checking gethostbyname_r() syntax... GNU-style
checking getpwnam_r... yes
checking getgrnam_r... yes
checking ctime_r() syntax... POSIX-style
top_builddir=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21
configure: creating ./config.status
config.status: creating ./Make.inc
config.status: creating ./src/include/build-radpaths-h
config.status: creating ./src/main/radsniff.mk
config.status: creating ./src/main/checkrad
config.status: creating ./src/main/radlast
config.status: creating ./src/main/radtest
config.status: creating ./scripts/rc.radiusd
config.status: creating ./scripts/cron/radiusd.cron.daily
config.status: creating ./scripts/cron/radiusd.cron.monthly
config.status: creating ./scripts/cryptpasswd
config.status: creating ./raddb/radrelay.conf
config.status: creating ./raddb/radiusd.conf
config.status: creating src/include/autoconf.h
config.status: executing stamp-h commands
config.status: executing build-radpaths-h commands
config.status: executing main-chmod commands
config.status: executing scripts-chmod commands
=== configuring in src/modules/rlm_python3 (/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21/src/modules/rlm_python3)
configure: running /bin/bash ./configure --disable-option-checking '--prefix=/usr'  '--target=x86_64-openwrt-linux' '--host=x86_64-openwrt-linux' '--build=x86_64-pc-linux-gnu' '--program-prefix=' '--program-suffix=' '--exec-prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--libexecdir=/usr/lib' '--sysconfdir=/etc' '--datadir=/usr/share' '--localstatedir=/var' '--mandir=/usr/man' '--infodir=/usr/info' '--disable-nls' '_python_sysroot=/openwrt/staging_dir/target-x86_64_musl' '_python_prefix=/usr' '_python_exec_prefix=/usr' '--libdir=/usr/lib/freeradius3' '--libexecdir=/usr/lib/freeradius3' '--disable-developer' '--with-threads' '--with-openssl' '--with-openssl-includes=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-openssl-libraries=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--disable-openssl-version-check' '--with-talloc-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-talloc-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--enable-strict-dependencies' '--with-dictdir=/usr/share/freeradius3' '--with-raddbdir=/etc/freeradius3' '--with-radacctdir=/var/db/radacct' '--with-logdir=/var/log' '--without-edir' '--without-snmp' '--without-rlm_cache' '--without-rlm_cache_memcached' '--without-rlm_couchbase' '--without-rlm_counter' '--without-rlm_eap_ikev2' '--without-rlm_eap_sim' '--without-rlm_eap_tnc' '--without-rlm_example' '--without-rlm_idn' '--without-rlm_ippool' '--without-rlm_krb5' '--without-rlm_opendirectory' '--without-rlm_pam' '--without-rlm_perl' '--without-rlm_python' '--without-rlm_redis' '--without-rlm_rediswho' '--without-rlm_ruby' '--without-rlm_securid' '--without-rlm_smsotp' '--without-rlm_sql_db2' '--without-rlm_sql_firebird' '--without-rlm_sql_freetds' '--without-rlm_sql_iodbc' '--without-rlm_sql_oracle' '--without-rlm_sql_unixodbc' '--without-rlm_unbound' '--without-rlm_yubikey' '--with-rlm_eap_peap' '--with-rlm_eap_peap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_peap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_pwd' '--with-rlm_eap_pwd-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_pwd-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_tls' '--with-rlm_eap_tls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_tls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_ttls' '--with-rlm_eap_ttls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_ttls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_ldap' '--with-rlm_ldap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_ldap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-modules=rlm_python3' '--with-rlm-python3-config-bin=/openwrt/staging_dir/target-x86_64_musl/host/bin/python3.9-config' '--with-rlm_radutmp' '--with-rlm_rest' '--with-rlm_sql' '--with-rlm_sql_mysql' '--with-mysql-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include/mysql' '--with-rlm_sql_postgresql' '--with-rlm_sql_sqlite' '--with-rlm_sqlcounter' '--with-rlm_sqlippool' '--with-rlm_unix' 'build_alias=x86_64-pc-linux-gnu' 'host_alias=x86_64-openwrt-linux' 'target_alias=x86_64-openwrt-linux' 'CC=ccache_cc' 'CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' 'LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro ' 'LIBS=-latomic -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl' 'CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include ' 'CXX=ccache_cxx' 'CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' --cache-file=/dev/null --srcdir=.
configure: loading site script /openwrt/include/site/x86_64
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
configure: /openwrt/staging_dir/target-x86_64_musl/host/bin/python3.9-config's cflags were "-I/openwrt/staging_dir/target-x86_64_musl/usr/include/python3.9 -I/openwrt/staging_dir/target-x86_64_musl/usr/include/python3.9  -Wno-unused-result -Wsign-compare -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/Python-3.9.5=Python-3.9.5 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DNDEBUG -fno-inline -DNDEBUG -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/Python-3.9.5=Python-3.9.5 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro"
configure: Sanitized cflags were "-isystem/openwrt/staging_dir/target-x86_64_musl/usr/include/python3.9 -isystem/openwrt/staging_dir/target-x86_64_musl/usr/include/python3.9    -pipe -fno-caller-saves -fno-plt -fhonour-copts   -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/Python-3.9.5=Python-3.9.5   -fstack-protector -D_FORTIFY_SOURCE=1   -fno-inline -pipe -fno-caller-saves -fno-plt -fhonour-copts   -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/Python-3.9.5=Python-3.9.5   -fstack-protector -D_FORTIFY_SOURCE=1  "
configure: /openwrt/staging_dir/target-x86_64_musl/host/bin/python3.9-config's ldflags were " -L/openwrt/staging_dir/target-x86_64_musl/usr/lib  -ldl  -lpthread -lm -lm }"
configure: Sanitized ldflags were "-L/openwrt/staging_dir/target-x86_64_musl/usr/lib -ldl -lpthread -lm -lm"
configure: creating ./config.status
config.status: creating all.mk
config.status: creating config.h
=== configuring in src/modules/rlm_cache (/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21/src/modules/rlm_cache)
configure: running /bin/bash ./configure --disable-option-checking '--prefix=/usr'  '--target=x86_64-openwrt-linux' '--host=x86_64-openwrt-linux' '--build=x86_64-pc-linux-gnu' '--program-prefix=' '--program-suffix=' '--exec-prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--libexecdir=/usr/lib' '--sysconfdir=/etc' '--datadir=/usr/share' '--localstatedir=/var' '--mandir=/usr/man' '--infodir=/usr/info' '--disable-nls' '_python_sysroot=/openwrt/staging_dir/target-x86_64_musl' '_python_prefix=/usr' '_python_exec_prefix=/usr' '--libdir=/usr/lib/freeradius3' '--libexecdir=/usr/lib/freeradius3' '--disable-developer' '--with-threads' '--with-openssl' '--with-openssl-includes=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-openssl-libraries=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--disable-openssl-version-check' '--with-talloc-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-talloc-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--enable-strict-dependencies' '--with-dictdir=/usr/share/freeradius3' '--with-raddbdir=/etc/freeradius3' '--with-radacctdir=/var/db/radacct' '--with-logdir=/var/log' '--without-edir' '--without-snmp' '--without-rlm_cache' '--without-rlm_cache_memcached' '--without-rlm_couchbase' '--without-rlm_counter' '--without-rlm_eap_ikev2' '--without-rlm_eap_sim' '--without-rlm_eap_tnc' '--without-rlm_example' '--without-rlm_idn' '--without-rlm_ippool' '--without-rlm_krb5' '--without-rlm_opendirectory' '--without-rlm_pam' '--without-rlm_perl' '--without-rlm_python' '--without-rlm_redis' '--without-rlm_rediswho' '--without-rlm_ruby' '--without-rlm_securid' '--without-rlm_smsotp' '--without-rlm_sql_db2' '--without-rlm_sql_firebird' '--without-rlm_sql_freetds' '--without-rlm_sql_iodbc' '--without-rlm_sql_oracle' '--without-rlm_sql_unixodbc' '--without-rlm_unbound' '--without-rlm_yubikey' '--with-rlm_eap_peap' '--with-rlm_eap_peap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_peap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_pwd' '--with-rlm_eap_pwd-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_pwd-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_tls' '--with-rlm_eap_tls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_tls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_ttls' '--with-rlm_eap_ttls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_ttls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_ldap' '--with-rlm_ldap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_ldap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-modules=rlm_python3' '--with-rlm-python3-config-bin=/openwrt/staging_dir/target-x86_64_musl/host/bin/python3.9-config' '--with-rlm_radutmp' '--with-rlm_rest' '--with-rlm_sql' '--with-rlm_sql_mysql' '--with-mysql-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include/mysql' '--with-rlm_sql_postgresql' '--with-rlm_sql_sqlite' '--with-rlm_sqlcounter' '--with-rlm_sqlippool' '--with-rlm_unix' 'build_alias=x86_64-pc-linux-gnu' 'host_alias=x86_64-openwrt-linux' 'target_alias=x86_64-openwrt-linux' 'CC=ccache_cc' 'CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' 'LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro ' 'LIBS=-latomic -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl' 'CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include ' 'CXX=ccache_cxx' 'CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' --cache-file=/dev/null --srcdir=.
configure: loading site script /openwrt/include/site/x86_64
*** module rlm_cache is disabled.
configure: creating ./config.status
config.status: creating all.mk
=== configuring in src/modules/rlm_counter (/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21/src/modules/rlm_counter)
configure: running /bin/bash ./configure --disable-option-checking '--prefix=/usr'  '--target=x86_64-openwrt-linux' '--host=x86_64-openwrt-linux' '--build=x86_64-pc-linux-gnu' '--program-prefix=' '--program-suffix=' '--exec-prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--libexecdir=/usr/lib' '--sysconfdir=/etc' '--datadir=/usr/share' '--localstatedir=/var' '--mandir=/usr/man' '--infodir=/usr/info' '--disable-nls' '_python_sysroot=/openwrt/staging_dir/target-x86_64_musl' '_python_prefix=/usr' '_python_exec_prefix=/usr' '--libdir=/usr/lib/freeradius3' '--libexecdir=/usr/lib/freeradius3' '--disable-developer' '--with-threads' '--with-openssl' '--with-openssl-includes=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-openssl-libraries=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--disable-openssl-version-check' '--with-talloc-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-talloc-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--enable-strict-dependencies' '--with-dictdir=/usr/share/freeradius3' '--with-raddbdir=/etc/freeradius3' '--with-radacctdir=/var/db/radacct' '--with-logdir=/var/log' '--without-edir' '--without-snmp' '--without-rlm_cache' '--without-rlm_cache_memcached' '--without-rlm_couchbase' '--without-rlm_counter' '--without-rlm_eap_ikev2' '--without-rlm_eap_sim' '--without-rlm_eap_tnc' '--without-rlm_example' '--without-rlm_idn' '--without-rlm_ippool' '--without-rlm_krb5' '--without-rlm_opendirectory' '--without-rlm_pam' '--without-rlm_perl' '--without-rlm_python' '--without-rlm_redis' '--without-rlm_rediswho' '--without-rlm_ruby' '--without-rlm_securid' '--without-rlm_smsotp' '--without-rlm_sql_db2' '--without-rlm_sql_firebird' '--without-rlm_sql_freetds' '--without-rlm_sql_iodbc' '--without-rlm_sql_oracle' '--without-rlm_sql_unixodbc' '--without-rlm_unbound' '--without-rlm_yubikey' '--with-rlm_eap_peap' '--with-rlm_eap_peap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_peap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_pwd' '--with-rlm_eap_pwd-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_pwd-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_tls' '--with-rlm_eap_tls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_tls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_ttls' '--with-rlm_eap_ttls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_ttls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_ldap' '--with-rlm_ldap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_ldap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-modules=rlm_python3' '--with-rlm-python3-config-bin=/openwrt/staging_dir/target-x86_64_musl/host/bin/python3.9-config' '--with-rlm_radutmp' '--with-rlm_rest' '--with-rlm_sql' '--with-rlm_sql_mysql' '--with-mysql-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include/mysql' '--with-rlm_sql_postgresql' '--with-rlm_sql_sqlite' '--with-rlm_sqlcounter' '--with-rlm_sqlippool' '--with-rlm_unix' 'build_alias=x86_64-pc-linux-gnu' 'host_alias=x86_64-openwrt-linux' 'target_alias=x86_64-openwrt-linux' 'CC=ccache_cc' 'CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' 'LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro ' 'LIBS=-latomic -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl' 'CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include ' 'CXX=ccache_cxx' 'CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' --cache-file=/dev/null --srcdir=.
configure: loading site script /openwrt/include/site/x86_64
*** module rlm_counter is disabled.
configure: creating ./config.status
config.status: creating all.mk
config.status: creating config.h
=== configuring in src/modules/rlm_eap (/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21/src/modules/rlm_eap)
configure: running /bin/bash ./configure --disable-option-checking '--prefix=/usr'  '--target=x86_64-openwrt-linux' '--host=x86_64-openwrt-linux' '--build=x86_64-pc-linux-gnu' '--program-prefix=' '--program-suffix=' '--exec-prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--libexecdir=/usr/lib' '--sysconfdir=/etc' '--datadir=/usr/share' '--localstatedir=/var' '--mandir=/usr/man' '--infodir=/usr/info' '--disable-nls' '_python_sysroot=/openwrt/staging_dir/target-x86_64_musl' '_python_prefix=/usr' '_python_exec_prefix=/usr' '--libdir=/usr/lib/freeradius3' '--libexecdir=/usr/lib/freeradius3' '--disable-developer' '--with-threads' '--with-openssl' '--with-openssl-includes=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-openssl-libraries=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--disable-openssl-version-check' '--with-talloc-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-talloc-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--enable-strict-dependencies' '--with-dictdir=/usr/share/freeradius3' '--with-raddbdir=/etc/freeradius3' '--with-radacctdir=/var/db/radacct' '--with-logdir=/var/log' '--without-edir' '--without-snmp' '--without-rlm_cache' '--without-rlm_cache_memcached' '--without-rlm_couchbase' '--without-rlm_counter' '--without-rlm_eap_ikev2' '--without-rlm_eap_sim' '--without-rlm_eap_tnc' '--without-rlm_example' '--without-rlm_idn' '--without-rlm_ippool' '--without-rlm_krb5' '--without-rlm_opendirectory' '--without-rlm_pam' '--without-rlm_perl' '--without-rlm_python' '--without-rlm_redis' '--without-rlm_rediswho' '--without-rlm_ruby' '--without-rlm_securid' '--without-rlm_smsotp' '--without-rlm_sql_db2' '--without-rlm_sql_firebird' '--without-rlm_sql_freetds' '--without-rlm_sql_iodbc' '--without-rlm_sql_oracle' '--without-rlm_sql_unixodbc' '--without-rlm_unbound' '--without-rlm_yubikey' '--with-rlm_eap_peap' '--with-rlm_eap_peap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_peap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_pwd' '--with-rlm_eap_pwd-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_pwd-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_tls' '--with-rlm_eap_tls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_tls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_ttls' '--with-rlm_eap_ttls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_ttls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_ldap' '--with-rlm_ldap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_ldap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-modules=rlm_python3' '--with-rlm-python3-config-bin=/openwrt/staging_dir/target-x86_64_musl/host/bin/python3.9-config' '--with-rlm_radutmp' '--with-rlm_rest' '--with-rlm_sql' '--with-rlm_sql_mysql' '--with-mysql-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include/mysql' '--with-rlm_sql_postgresql' '--with-rlm_sql_sqlite' '--with-rlm_sqlcounter' '--with-rlm_sqlippool' '--with-rlm_unix' 'build_alias=x86_64-pc-linux-gnu' 'host_alias=x86_64-openwrt-linux' 'target_alias=x86_64-openwrt-linux' 'CC=ccache_cc' 'CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' 'LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro ' 'LIBS=-latomic -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl' 'CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include ' 'CXX=ccache_cxx' 'CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' --cache-file=/dev/null --srcdir=.
configure: loading site script /openwrt/include/site/x86_64
checking for x86_64-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
configure: creating ./config.status
=== configuring in ./types/rlm_eap_ikev2 (/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21/src/modules/rlm_eap/./types/rlm_eap_ikev2)
configure: running /bin/bash ./configure --disable-option-checking '--prefix=/usr'  '--target=x86_64-openwrt-linux' '--host=x86_64-openwrt-linux' '--build=x86_64-pc-linux-gnu' '--program-prefix=' '--program-suffix=' '--exec-prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--libexecdir=/usr/lib' '--sysconfdir=/etc' '--datadir=/usr/share' '--localstatedir=/var' '--mandir=/usr/man' '--infodir=/usr/info' '--disable-nls' '_python_sysroot=/openwrt/staging_dir/target-x86_64_musl' '_python_prefix=/usr' '_python_exec_prefix=/usr' '--libdir=/usr/lib/freeradius3' '--libexecdir=/usr/lib/freeradius3' '--disable-developer' '--with-threads' '--with-openssl' '--with-openssl-includes=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-openssl-libraries=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--disable-openssl-version-check' '--with-talloc-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-talloc-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--enable-strict-dependencies' '--with-dictdir=/usr/share/freeradius3' '--with-raddbdir=/etc/freeradius3' '--with-radacctdir=/var/db/radacct' '--with-logdir=/var/log' '--without-edir' '--without-snmp' '--without-rlm_cache' '--without-rlm_cache_memcached' '--without-rlm_couchbase' '--without-rlm_counter' '--without-rlm_eap_ikev2' '--without-rlm_eap_sim' '--without-rlm_eap_tnc' '--without-rlm_example' '--without-rlm_idn' '--without-rlm_ippool' '--without-rlm_krb5' '--without-rlm_opendirectory' '--without-rlm_pam' '--without-rlm_perl' '--without-rlm_python' '--without-rlm_redis' '--without-rlm_rediswho' '--without-rlm_ruby' '--without-rlm_securid' '--without-rlm_smsotp' '--without-rlm_sql_db2' '--without-rlm_sql_firebird' '--without-rlm_sql_freetds' '--without-rlm_sql_iodbc' '--without-rlm_sql_oracle' '--without-rlm_sql_unixodbc' '--without-rlm_unbound' '--without-rlm_yubikey' '--with-rlm_eap_peap' '--with-rlm_eap_peap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_peap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_pwd' '--with-rlm_eap_pwd-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_pwd-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_tls' '--with-rlm_eap_tls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_tls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_ttls' '--with-rlm_eap_ttls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_ttls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_ldap' '--with-rlm_ldap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_ldap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-modules=rlm_python3' '--with-rlm-python3-config-bin=/openwrt/staging_dir/target-x86_64_musl/host/bin/python3.9-config' '--with-rlm_radutmp' '--with-rlm_rest' '--with-rlm_sql' '--with-rlm_sql_mysql' '--with-mysql-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include/mysql' '--with-rlm_sql_postgresql' '--with-rlm_sql_sqlite' '--with-rlm_sqlcounter' '--with-rlm_sqlippool' '--with-rlm_unix' 'build_alias=x86_64-pc-linux-gnu' 'host_alias=x86_64-openwrt-linux' 'target_alias=x86_64-openwrt-linux' 'CC=ccache_cc' 'CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' 'LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro ' 'LIBS=-latomic -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl' 'CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include ' 'CXX=ccache_cxx' 'CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' --cache-file=/dev/null --srcdir=.
configure: loading site script /openwrt/include/site/x86_64
*** module rlm_eap_ikev2 is disabled.
configure: creating ./config.status
config.status: creating all.mk
=== configuring in ./types/rlm_eap_fast (/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21/src/modules/rlm_eap/./types/rlm_eap_fast)
configure: running /bin/bash ./configure --disable-option-checking '--prefix=/usr'  '--target=x86_64-openwrt-linux' '--host=x86_64-openwrt-linux' '--build=x86_64-pc-linux-gnu' '--program-prefix=' '--program-suffix=' '--exec-prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--libexecdir=/usr/lib' '--sysconfdir=/etc' '--datadir=/usr/share' '--localstatedir=/var' '--mandir=/usr/man' '--infodir=/usr/info' '--disable-nls' '_python_sysroot=/openwrt/staging_dir/target-x86_64_musl' '_python_prefix=/usr' '_python_exec_prefix=/usr' '--libdir=/usr/lib/freeradius3' '--libexecdir=/usr/lib/freeradius3' '--disable-developer' '--with-threads' '--with-openssl' '--with-openssl-includes=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-openssl-libraries=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--disable-openssl-version-check' '--with-talloc-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-talloc-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--enable-strict-dependencies' '--with-dictdir=/usr/share/freeradius3' '--with-raddbdir=/etc/freeradius3' '--with-radacctdir=/var/db/radacct' '--with-logdir=/var/log' '--without-edir' '--without-snmp' '--without-rlm_cache' '--without-rlm_cache_memcached' '--without-rlm_couchbase' '--without-rlm_counter' '--without-rlm_eap_ikev2' '--without-rlm_eap_sim' '--without-rlm_eap_tnc' '--without-rlm_example' '--without-rlm_idn' '--without-rlm_ippool' '--without-rlm_krb5' '--without-rlm_opendirectory' '--without-rlm_pam' '--without-rlm_perl' '--without-rlm_python' '--without-rlm_redis' '--without-rlm_rediswho' '--without-rlm_ruby' '--without-rlm_securid' '--without-rlm_smsotp' '--without-rlm_sql_db2' '--without-rlm_sql_firebird' '--without-rlm_sql_freetds' '--without-rlm_sql_iodbc' '--without-rlm_sql_oracle' '--without-rlm_sql_unixodbc' '--without-rlm_unbound' '--without-rlm_yubikey' '--with-rlm_eap_peap' '--with-rlm_eap_peap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_peap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_pwd' '--with-rlm_eap_pwd-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_pwd-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_tls' '--with-rlm_eap_tls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_tls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_ttls' '--with-rlm_eap_ttls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_ttls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_ldap' '--with-rlm_ldap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_ldap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-modules=rlm_python3' '--with-rlm-python3-config-bin=/openwrt/staging_dir/target-x86_64_musl/host/bin/python3.9-config' '--with-rlm_radutmp' '--with-rlm_rest' '--with-rlm_sql' '--with-rlm_sql_mysql' '--with-mysql-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include/mysql' '--with-rlm_sql_postgresql' '--with-rlm_sql_sqlite' '--with-rlm_sqlcounter' '--with-rlm_sqlippool' '--with-rlm_unix' 'build_alias=x86_64-pc-linux-gnu' 'host_alias=x86_64-openwrt-linux' 'target_alias=x86_64-openwrt-linux' 'CC=ccache_cc' 'CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' 'LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro ' 'LIBS=-latomic -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl' 'CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include ' 'CXX=ccache_cxx' 'CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' --cache-file=/dev/null --srcdir=.
configure: loading site script /openwrt/include/site/x86_64
checking for x86_64-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
checking for openssl/ec.h... yes
checking for EVP_CIPHER_CTX_new in -lcrypto... yes
checking how to run the C preprocessor... ccache_cc -E
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for OpenSSL version >= 1.0.1a... yes
configure: creating ./config.status
config.status: creating all.mk
=== configuring in ./types/rlm_eap_pwd (/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21/src/modules/rlm_eap/./types/rlm_eap_pwd)
configure: running /bin/bash ./configure --disable-option-checking '--prefix=/usr'  '--target=x86_64-openwrt-linux' '--host=x86_64-openwrt-linux' '--build=x86_64-pc-linux-gnu' '--program-prefix=' '--program-suffix=' '--exec-prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--libexecdir=/usr/lib' '--sysconfdir=/etc' '--datadir=/usr/share' '--localstatedir=/var' '--mandir=/usr/man' '--infodir=/usr/info' '--disable-nls' '_python_sysroot=/openwrt/staging_dir/target-x86_64_musl' '_python_prefix=/usr' '_python_exec_prefix=/usr' '--libdir=/usr/lib/freeradius3' '--libexecdir=/usr/lib/freeradius3' '--disable-developer' '--with-threads' '--with-openssl' '--with-openssl-includes=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-openssl-libraries=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--disable-openssl-version-check' '--with-talloc-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-talloc-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--enable-strict-dependencies' '--with-dictdir=/usr/share/freeradius3' '--with-raddbdir=/etc/freeradius3' '--with-radacctdir=/var/db/radacct' '--with-logdir=/var/log' '--without-edir' '--without-snmp' '--without-rlm_cache' '--without-rlm_cache_memcached' '--without-rlm_couchbase' '--without-rlm_counter' '--without-rlm_eap_ikev2' '--without-rlm_eap_sim' '--without-rlm_eap_tnc' '--without-rlm_example' '--without-rlm_idn' '--without-rlm_ippool' '--without-rlm_krb5' '--without-rlm_opendirectory' '--without-rlm_pam' '--without-rlm_perl' '--without-rlm_python' '--without-rlm_redis' '--without-rlm_rediswho' '--without-rlm_ruby' '--without-rlm_securid' '--without-rlm_smsotp' '--without-rlm_sql_db2' '--without-rlm_sql_firebird' '--without-rlm_sql_freetds' '--without-rlm_sql_iodbc' '--without-rlm_sql_oracle' '--without-rlm_sql_unixodbc' '--without-rlm_unbound' '--without-rlm_yubikey' '--with-rlm_eap_peap' '--with-rlm_eap_peap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_peap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_pwd' '--with-rlm_eap_pwd-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_pwd-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_tls' '--with-rlm_eap_tls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_tls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_ttls' '--with-rlm_eap_ttls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_ttls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_ldap' '--with-rlm_ldap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_ldap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-modules=rlm_python3' '--with-rlm-python3-config-bin=/openwrt/staging_dir/target-x86_64_musl/host/bin/python3.9-config' '--with-rlm_radutmp' '--with-rlm_rest' '--with-rlm_sql' '--with-rlm_sql_mysql' '--with-mysql-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include/mysql' '--with-rlm_sql_postgresql' '--with-rlm_sql_sqlite' '--with-rlm_sqlcounter' '--with-rlm_sqlippool' '--with-rlm_unix' 'build_alias=x86_64-pc-linux-gnu' 'host_alias=x86_64-openwrt-linux' 'target_alias=x86_64-openwrt-linux' 'CC=ccache_cc' 'CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' 'LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro ' 'LIBS=-latomic -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl' 'CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include ' 'CXX=ccache_cxx' 'CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' --cache-file=/dev/null --srcdir=.
configure: loading site script /openwrt/include/site/x86_64
checking for x86_64-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
checking for openssl/ec.h... yes
checking for EVP_CIPHER_CTX_new in -lcrypto... yes
checking for EVP_sha256... yes
checking for EC_GROUP_free... yes
configure: creating ./config.status
config.status: creating all.mk
=== configuring in ./types/rlm_eap_tnc (/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21/src/modules/rlm_eap/./types/rlm_eap_tnc)
configure: running /bin/bash ./configure --disable-option-checking '--prefix=/usr'  '--target=x86_64-openwrt-linux' '--host=x86_64-openwrt-linux' '--build=x86_64-pc-linux-gnu' '--program-prefix=' '--program-suffix=' '--exec-prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--libexecdir=/usr/lib' '--sysconfdir=/etc' '--datadir=/usr/share' '--localstatedir=/var' '--mandir=/usr/man' '--infodir=/usr/info' '--disable-nls' '_python_sysroot=/openwrt/staging_dir/target-x86_64_musl' '_python_prefix=/usr' '_python_exec_prefix=/usr' '--libdir=/usr/lib/freeradius3' '--libexecdir=/usr/lib/freeradius3' '--disable-developer' '--with-threads' '--with-openssl' '--with-openssl-includes=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-openssl-libraries=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--disable-openssl-version-check' '--with-talloc-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-talloc-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--enable-strict-dependencies' '--with-dictdir=/usr/share/freeradius3' '--with-raddbdir=/etc/freeradius3' '--with-radacctdir=/var/db/radacct' '--with-logdir=/var/log' '--without-edir' '--without-snmp' '--without-rlm_cache' '--without-rlm_cache_memcached' '--without-rlm_couchbase' '--without-rlm_counter' '--without-rlm_eap_ikev2' '--without-rlm_eap_sim' '--without-rlm_eap_tnc' '--without-rlm_example' '--without-rlm_idn' '--without-rlm_ippool' '--without-rlm_krb5' '--without-rlm_opendirectory' '--without-rlm_pam' '--without-rlm_perl' '--without-rlm_python' '--without-rlm_redis' '--without-rlm_rediswho' '--without-rlm_ruby' '--without-rlm_securid' '--without-rlm_smsotp' '--without-rlm_sql_db2' '--without-rlm_sql_firebird' '--without-rlm_sql_freetds' '--without-rlm_sql_iodbc' '--without-rlm_sql_oracle' '--without-rlm_sql_unixodbc' '--without-rlm_unbound' '--without-rlm_yubikey' '--with-rlm_eap_peap' '--with-rlm_eap_peap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_peap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_pwd' '--with-rlm_eap_pwd-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_pwd-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_tls' '--with-rlm_eap_tls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_tls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_ttls' '--with-rlm_eap_ttls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_ttls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_ldap' '--with-rlm_ldap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_ldap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-modules=rlm_python3' '--with-rlm-python3-config-bin=/openwrt/staging_dir/target-x86_64_musl/host/bin/python3.9-config' '--with-rlm_radutmp' '--with-rlm_rest' '--with-rlm_sql' '--with-rlm_sql_mysql' '--with-mysql-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include/mysql' '--with-rlm_sql_postgresql' '--with-rlm_sql_sqlite' '--with-rlm_sqlcounter' '--with-rlm_sqlippool' '--with-rlm_unix' 'build_alias=x86_64-pc-linux-gnu' 'host_alias=x86_64-openwrt-linux' 'target_alias=x86_64-openwrt-linux' 'CC=ccache_cc' 'CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' 'LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro ' 'LIBS=-latomic -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl' 'CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include ' 'CXX=ccache_cxx' 'CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' --cache-file=/dev/null --srcdir=.
configure: loading site script /openwrt/include/site/x86_64
*** module rlm_eap_tnc is disabled.
configure: creating ./config.status
config.status: creating all.mk
=== configuring in ./types/rlm_eap_sim (/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21/src/modules/rlm_eap/./types/rlm_eap_sim)
configure: running /bin/bash ./configure --disable-option-checking '--prefix=/usr'  '--target=x86_64-openwrt-linux' '--host=x86_64-openwrt-linux' '--build=x86_64-pc-linux-gnu' '--program-prefix=' '--program-suffix=' '--exec-prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--libexecdir=/usr/lib' '--sysconfdir=/etc' '--datadir=/usr/share' '--localstatedir=/var' '--mandir=/usr/man' '--infodir=/usr/info' '--disable-nls' '_python_sysroot=/openwrt/staging_dir/target-x86_64_musl' '_python_prefix=/usr' '_python_exec_prefix=/usr' '--libdir=/usr/lib/freeradius3' '--libexecdir=/usr/lib/freeradius3' '--disable-developer' '--with-threads' '--with-openssl' '--with-openssl-includes=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-openssl-libraries=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--disable-openssl-version-check' '--with-talloc-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-talloc-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--enable-strict-dependencies' '--with-dictdir=/usr/share/freeradius3' '--with-raddbdir=/etc/freeradius3' '--with-radacctdir=/var/db/radacct' '--with-logdir=/var/log' '--without-edir' '--without-snmp' '--without-rlm_cache' '--without-rlm_cache_memcached' '--without-rlm_couchbase' '--without-rlm_counter' '--without-rlm_eap_ikev2' '--without-rlm_eap_sim' '--without-rlm_eap_tnc' '--without-rlm_example' '--without-rlm_idn' '--without-rlm_ippool' '--without-rlm_krb5' '--without-rlm_opendirectory' '--without-rlm_pam' '--without-rlm_perl' '--without-rlm_python' '--without-rlm_redis' '--without-rlm_rediswho' '--without-rlm_ruby' '--without-rlm_securid' '--without-rlm_smsotp' '--without-rlm_sql_db2' '--without-rlm_sql_firebird' '--without-rlm_sql_freetds' '--without-rlm_sql_iodbc' '--without-rlm_sql_oracle' '--without-rlm_sql_unixodbc' '--without-rlm_unbound' '--without-rlm_yubikey' '--with-rlm_eap_peap' '--with-rlm_eap_peap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_peap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_pwd' '--with-rlm_eap_pwd-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_pwd-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_tls' '--with-rlm_eap_tls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_tls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_ttls' '--with-rlm_eap_ttls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_ttls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_ldap' '--with-rlm_ldap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_ldap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-modules=rlm_python3' '--with-rlm-python3-config-bin=/openwrt/staging_dir/target-x86_64_musl/host/bin/python3.9-config' '--with-rlm_radutmp' '--with-rlm_rest' '--with-rlm_sql' '--with-rlm_sql_mysql' '--with-mysql-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include/mysql' '--with-rlm_sql_postgresql' '--with-rlm_sql_sqlite' '--with-rlm_sqlcounter' '--with-rlm_sqlippool' '--with-rlm_unix' 'build_alias=x86_64-pc-linux-gnu' 'host_alias=x86_64-openwrt-linux' 'target_alias=x86_64-openwrt-linux' 'CC=ccache_cc' 'CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' 'LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro ' 'LIBS=-latomic -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl' 'CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include ' 'CXX=ccache_cxx' 'CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' --cache-file=/dev/null --srcdir=.
configure: loading site script /openwrt/include/site/x86_64
*** module rlm_eap_sim is disabled.
configure: creating ./config.status
config.status: creating all.mk
=== configuring in src/modules/rlm_ippool (/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21/src/modules/rlm_ippool)
configure: running /bin/bash ./configure --disable-option-checking '--prefix=/usr'  '--target=x86_64-openwrt-linux' '--host=x86_64-openwrt-linux' '--build=x86_64-pc-linux-gnu' '--program-prefix=' '--program-suffix=' '--exec-prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--libexecdir=/usr/lib' '--sysconfdir=/etc' '--datadir=/usr/share' '--localstatedir=/var' '--mandir=/usr/man' '--infodir=/usr/info' '--disable-nls' '_python_sysroot=/openwrt/staging_dir/target-x86_64_musl' '_python_prefix=/usr' '_python_exec_prefix=/usr' '--libdir=/usr/lib/freeradius3' '--libexecdir=/usr/lib/freeradius3' '--disable-developer' '--with-threads' '--with-openssl' '--with-openssl-includes=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-openssl-libraries=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--disable-openssl-version-check' '--with-talloc-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-talloc-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--enable-strict-dependencies' '--with-dictdir=/usr/share/freeradius3' '--with-raddbdir=/etc/freeradius3' '--with-radacctdir=/var/db/radacct' '--with-logdir=/var/log' '--without-edir' '--without-snmp' '--without-rlm_cache' '--without-rlm_cache_memcached' '--without-rlm_couchbase' '--without-rlm_counter' '--without-rlm_eap_ikev2' '--without-rlm_eap_sim' '--without-rlm_eap_tnc' '--without-rlm_example' '--without-rlm_idn' '--without-rlm_ippool' '--without-rlm_krb5' '--without-rlm_opendirectory' '--without-rlm_pam' '--without-rlm_perl' '--without-rlm_python' '--without-rlm_redis' '--without-rlm_rediswho' '--without-rlm_ruby' '--without-rlm_securid' '--without-rlm_smsotp' '--without-rlm_sql_db2' '--without-rlm_sql_firebird' '--without-rlm_sql_freetds' '--without-rlm_sql_iodbc' '--without-rlm_sql_oracle' '--without-rlm_sql_unixodbc' '--without-rlm_unbound' '--without-rlm_yubikey' '--with-rlm_eap_peap' '--with-rlm_eap_peap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_peap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_pwd' '--with-rlm_eap_pwd-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_pwd-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_tls' '--with-rlm_eap_tls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_tls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_ttls' '--with-rlm_eap_ttls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_ttls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_ldap' '--with-rlm_ldap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_ldap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-modules=rlm_python3' '--with-rlm-python3-config-bin=/openwrt/staging_dir/target-x86_64_musl/host/bin/python3.9-config' '--with-rlm_radutmp' '--with-rlm_rest' '--with-rlm_sql' '--with-rlm_sql_mysql' '--with-mysql-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include/mysql' '--with-rlm_sql_postgresql' '--with-rlm_sql_sqlite' '--with-rlm_sqlcounter' '--with-rlm_sqlippool' '--with-rlm_unix' 'build_alias=x86_64-pc-linux-gnu' 'host_alias=x86_64-openwrt-linux' 'target_alias=x86_64-openwrt-linux' 'CC=ccache_cc' 'CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' 'LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro ' 'LIBS=-latomic -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl' 'CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include ' 'CXX=ccache_cxx' 'CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' --cache-file=/dev/null --srcdir=.
configure: loading site script /openwrt/include/site/x86_64
*** module rlm_ippool is disabled.
configure: creating ./config.status
config.status: creating all.mk
config.status: creating config.h
=== configuring in src/modules/rlm_krb5 (/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21/src/modules/rlm_krb5)
configure: running /bin/bash ./configure --disable-option-checking '--prefix=/usr'  '--target=x86_64-openwrt-linux' '--host=x86_64-openwrt-linux' '--build=x86_64-pc-linux-gnu' '--program-prefix=' '--program-suffix=' '--exec-prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--libexecdir=/usr/lib' '--sysconfdir=/etc' '--datadir=/usr/share' '--localstatedir=/var' '--mandir=/usr/man' '--infodir=/usr/info' '--disable-nls' '_python_sysroot=/openwrt/staging_dir/target-x86_64_musl' '_python_prefix=/usr' '_python_exec_prefix=/usr' '--libdir=/usr/lib/freeradius3' '--libexecdir=/usr/lib/freeradius3' '--disable-developer' '--with-threads' '--with-openssl' '--with-openssl-includes=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-openssl-libraries=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--disable-openssl-version-check' '--with-talloc-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-talloc-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--enable-strict-dependencies' '--with-dictdir=/usr/share/freeradius3' '--with-raddbdir=/etc/freeradius3' '--with-radacctdir=/var/db/radacct' '--with-logdir=/var/log' '--without-edir' '--without-snmp' '--without-rlm_cache' '--without-rlm_cache_memcached' '--without-rlm_couchbase' '--without-rlm_counter' '--without-rlm_eap_ikev2' '--without-rlm_eap_sim' '--without-rlm_eap_tnc' '--without-rlm_example' '--without-rlm_idn' '--without-rlm_ippool' '--without-rlm_krb5' '--without-rlm_opendirectory' '--without-rlm_pam' '--without-rlm_perl' '--without-rlm_python' '--without-rlm_redis' '--without-rlm_rediswho' '--without-rlm_ruby' '--without-rlm_securid' '--without-rlm_smsotp' '--without-rlm_sql_db2' '--without-rlm_sql_firebird' '--without-rlm_sql_freetds' '--without-rlm_sql_iodbc' '--without-rlm_sql_oracle' '--without-rlm_sql_unixodbc' '--without-rlm_unbound' '--without-rlm_yubikey' '--with-rlm_eap_peap' '--with-rlm_eap_peap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_peap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_pwd' '--with-rlm_eap_pwd-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_pwd-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_tls' '--with-rlm_eap_tls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_tls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_ttls' '--with-rlm_eap_ttls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_ttls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_ldap' '--with-rlm_ldap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_ldap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-modules=rlm_python3' '--with-rlm-python3-config-bin=/openwrt/staging_dir/target-x86_64_musl/host/bin/python3.9-config' '--with-rlm_radutmp' '--with-rlm_rest' '--with-rlm_sql' '--with-rlm_sql_mysql' '--with-mysql-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include/mysql' '--with-rlm_sql_postgresql' '--with-rlm_sql_sqlite' '--with-rlm_sqlcounter' '--with-rlm_sqlippool' '--with-rlm_unix' 'build_alias=x86_64-pc-linux-gnu' 'host_alias=x86_64-openwrt-linux' 'target_alias=x86_64-openwrt-linux' 'CC=ccache_cc' 'CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' 'LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro ' 'LIBS=-latomic -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl' 'CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include ' 'CXX=ccache_cxx' 'CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' --cache-file=/dev/null --srcdir=.
configure: loading site script /openwrt/include/site/x86_64
*** module rlm_krb5 is disabled.
configure: creating ./config.status
config.status: creating all.mk
=== configuring in src/modules/rlm_ldap (/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21/src/modules/rlm_ldap)
configure: running /bin/bash ./configure --disable-option-checking '--prefix=/usr'  '--target=x86_64-openwrt-linux' '--host=x86_64-openwrt-linux' '--build=x86_64-pc-linux-gnu' '--program-prefix=' '--program-suffix=' '--exec-prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--libexecdir=/usr/lib' '--sysconfdir=/etc' '--datadir=/usr/share' '--localstatedir=/var' '--mandir=/usr/man' '--infodir=/usr/info' '--disable-nls' '_python_sysroot=/openwrt/staging_dir/target-x86_64_musl' '_python_prefix=/usr' '_python_exec_prefix=/usr' '--libdir=/usr/lib/freeradius3' '--libexecdir=/usr/lib/freeradius3' '--disable-developer' '--with-threads' '--with-openssl' '--with-openssl-includes=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-openssl-libraries=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--disable-openssl-version-check' '--with-talloc-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-talloc-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--enable-strict-dependencies' '--with-dictdir=/usr/share/freeradius3' '--with-raddbdir=/etc/freeradius3' '--with-radacctdir=/var/db/radacct' '--with-logdir=/var/log' '--without-edir' '--without-snmp' '--without-rlm_cache' '--without-rlm_cache_memcached' '--without-rlm_couchbase' '--without-rlm_counter' '--without-rlm_eap_ikev2' '--without-rlm_eap_sim' '--without-rlm_eap_tnc' '--without-rlm_example' '--without-rlm_idn' '--without-rlm_ippool' '--without-rlm_krb5' '--without-rlm_opendirectory' '--without-rlm_pam' '--without-rlm_perl' '--without-rlm_python' '--without-rlm_redis' '--without-rlm_rediswho' '--without-rlm_ruby' '--without-rlm_securid' '--without-rlm_smsotp' '--without-rlm_sql_db2' '--without-rlm_sql_firebird' '--without-rlm_sql_freetds' '--without-rlm_sql_iodbc' '--without-rlm_sql_oracle' '--without-rlm_sql_unixodbc' '--without-rlm_unbound' '--without-rlm_yubikey' '--with-rlm_eap_peap' '--with-rlm_eap_peap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_peap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_pwd' '--with-rlm_eap_pwd-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_pwd-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_tls' '--with-rlm_eap_tls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_tls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_ttls' '--with-rlm_eap_ttls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_ttls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_ldap' '--with-rlm_ldap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_ldap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-modules=rlm_python3' '--with-rlm-python3-config-bin=/openwrt/staging_dir/target-x86_64_musl/host/bin/python3.9-config' '--with-rlm_radutmp' '--with-rlm_rest' '--with-rlm_sql' '--with-rlm_sql_mysql' '--with-mysql-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include/mysql' '--with-rlm_sql_postgresql' '--with-rlm_sql_sqlite' '--with-rlm_sqlcounter' '--with-rlm_sqlippool' '--with-rlm_unix' 'build_alias=x86_64-pc-linux-gnu' 'host_alias=x86_64-openwrt-linux' 'target_alias=x86_64-openwrt-linux' 'CC=ccache_cc' 'CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' 'LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro ' 'LIBS=-latomic -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl' 'CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include ' 'CXX=ccache_cxx' 'CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' --cache-file=/dev/null --srcdir=.
configure: loading site script /openwrt/include/site/x86_64
checking for x86_64-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
checking for ldap_init in -lldap in /openwrt/staging_dir/target-x86_64_musl/usr/lib... yes
checking for ldap.h in /openwrt/staging_dir/target-x86_64_musl/usr/include/... yes
checking for ldap_sasl_interactive_bind... yes
checking for ldap_unbind_ext_s... yes
checking for ldap_start_tls_s... yes
checking for ldap_initialize... yes
checking for ldap_set_rebind_proc... yes
checking for ldap_create_sort_control... yes
checking for ldap_create_sort_keylist... yes
checking for ldap_free_sort_keylist... yes
checking for ldap_url_parse... yes
checking for ldap_is_ldap_url... yes
checking for ldap_url_desc2str... yes
checking whether ldap_set_rebind_proc takes 3 arguments... 3
checking for sasl/sasl.h in /openwrt/staging_dir/target-x86_64_musl/usr/include/... yes
configure: creating ./config.status
config.status: creating all.mk
config.status: creating config.h
=== configuring in src/modules/rlm_mschap (/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21/src/modules/rlm_mschap)
configure: running /bin/bash ./configure --disable-option-checking '--prefix=/usr'  '--target=x86_64-openwrt-linux' '--host=x86_64-openwrt-linux' '--build=x86_64-pc-linux-gnu' '--program-prefix=' '--program-suffix=' '--exec-prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--libexecdir=/usr/lib' '--sysconfdir=/etc' '--datadir=/usr/share' '--localstatedir=/var' '--mandir=/usr/man' '--infodir=/usr/info' '--disable-nls' '_python_sysroot=/openwrt/staging_dir/target-x86_64_musl' '_python_prefix=/usr' '_python_exec_prefix=/usr' '--libdir=/usr/lib/freeradius3' '--libexecdir=/usr/lib/freeradius3' '--disable-developer' '--with-threads' '--with-openssl' '--with-openssl-includes=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-openssl-libraries=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--disable-openssl-version-check' '--with-talloc-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-talloc-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--enable-strict-dependencies' '--with-dictdir=/usr/share/freeradius3' '--with-raddbdir=/etc/freeradius3' '--with-radacctdir=/var/db/radacct' '--with-logdir=/var/log' '--without-edir' '--without-snmp' '--without-rlm_cache' '--without-rlm_cache_memcached' '--without-rlm_couchbase' '--without-rlm_counter' '--without-rlm_eap_ikev2' '--without-rlm_eap_sim' '--without-rlm_eap_tnc' '--without-rlm_example' '--without-rlm_idn' '--without-rlm_ippool' '--without-rlm_krb5' '--without-rlm_opendirectory' '--without-rlm_pam' '--without-rlm_perl' '--without-rlm_python' '--without-rlm_redis' '--without-rlm_rediswho' '--without-rlm_ruby' '--without-rlm_securid' '--without-rlm_smsotp' '--without-rlm_sql_db2' '--without-rlm_sql_firebird' '--without-rlm_sql_freetds' '--without-rlm_sql_iodbc' '--without-rlm_sql_oracle' '--without-rlm_sql_unixodbc' '--without-rlm_unbound' '--without-rlm_yubikey' '--with-rlm_eap_peap' '--with-rlm_eap_peap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_peap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_pwd' '--with-rlm_eap_pwd-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_pwd-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_tls' '--with-rlm_eap_tls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_tls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_ttls' '--with-rlm_eap_ttls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_ttls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_ldap' '--with-rlm_ldap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_ldap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-modules=rlm_python3' '--with-rlm-python3-config-bin=/openwrt/staging_dir/target-x86_64_musl/host/bin/python3.9-config' '--with-rlm_radutmp' '--with-rlm_rest' '--with-rlm_sql' '--with-rlm_sql_mysql' '--with-mysql-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include/mysql' '--with-rlm_sql_postgresql' '--with-rlm_sql_sqlite' '--with-rlm_sqlcounter' '--with-rlm_sqlippool' '--with-rlm_unix' 'build_alias=x86_64-pc-linux-gnu' 'host_alias=x86_64-openwrt-linux' 'target_alias=x86_64-openwrt-linux' 'CC=ccache_cc' 'CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' 'LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro ' 'LIBS=-latomic -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl' 'CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include ' 'CXX=ccache_cxx' 'CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' --cache-file=/dev/null --srcdir=.
configure: loading site script /openwrt/include/site/x86_64
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
checking for membership.h... no
checking for membership.h in /usr/local/include/... no
checking for membership.h in /opt/include/... no
checking for wbclient.h in /usr/include/samba-4.0/... no
checking for wbclient.h... no
checking for wbclient.h in /usr/local/include/... no
checking for wbclient.h in /opt/include/... no
configure: WARNING: wbclient.h not found. Use --with-winbind-include-dir=<path>.
configure: WARNING: silently building without support for direct authentication via winbind. requires: libwbclient
checking for core/ntstatus.h in /usr/include/samba-4.0/... no
checking for core/ntstatus.h... no
checking for core/ntstatus.h in /usr/local/include/... no
checking for core/ntstatus.h in /opt/include/... no
configure: WARNING: core/ntstatus.h not found. Use --with-winbind-include-dir=<path>.
configure: WARNING: silently building without support for direct authentication via winbind. requires: libwbclient
configure: creating ./config.status
config.status: creating rlm_mschap.mk
config.status: creating config.h
=== configuring in src/modules/rlm_pam (/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21/src/modules/rlm_pam)
configure: running /bin/bash ./configure --disable-option-checking '--prefix=/usr'  '--target=x86_64-openwrt-linux' '--host=x86_64-openwrt-linux' '--build=x86_64-pc-linux-gnu' '--program-prefix=' '--program-suffix=' '--exec-prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--libexecdir=/usr/lib' '--sysconfdir=/etc' '--datadir=/usr/share' '--localstatedir=/var' '--mandir=/usr/man' '--infodir=/usr/info' '--disable-nls' '_python_sysroot=/openwrt/staging_dir/target-x86_64_musl' '_python_prefix=/usr' '_python_exec_prefix=/usr' '--libdir=/usr/lib/freeradius3' '--libexecdir=/usr/lib/freeradius3' '--disable-developer' '--with-threads' '--with-openssl' '--with-openssl-includes=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-openssl-libraries=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--disable-openssl-version-check' '--with-talloc-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-talloc-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--enable-strict-dependencies' '--with-dictdir=/usr/share/freeradius3' '--with-raddbdir=/etc/freeradius3' '--with-radacctdir=/var/db/radacct' '--with-logdir=/var/log' '--without-edir' '--without-snmp' '--without-rlm_cache' '--without-rlm_cache_memcached' '--without-rlm_couchbase' '--without-rlm_counter' '--without-rlm_eap_ikev2' '--without-rlm_eap_sim' '--without-rlm_eap_tnc' '--without-rlm_example' '--without-rlm_idn' '--without-rlm_ippool' '--without-rlm_krb5' '--without-rlm_opendirectory' '--without-rlm_pam' '--without-rlm_perl' '--without-rlm_python' '--without-rlm_redis' '--without-rlm_rediswho' '--without-rlm_ruby' '--without-rlm_securid' '--without-rlm_smsotp' '--without-rlm_sql_db2' '--without-rlm_sql_firebird' '--without-rlm_sql_freetds' '--without-rlm_sql_iodbc' '--without-rlm_sql_oracle' '--without-rlm_sql_unixodbc' '--without-rlm_unbound' '--without-rlm_yubikey' '--with-rlm_eap_peap' '--with-rlm_eap_peap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_peap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_pwd' '--with-rlm_eap_pwd-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_pwd-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_tls' '--with-rlm_eap_tls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_tls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_ttls' '--with-rlm_eap_ttls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_ttls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_ldap' '--with-rlm_ldap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_ldap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-modules=rlm_python3' '--with-rlm-python3-config-bin=/openwrt/staging_dir/target-x86_64_musl/host/bin/python3.9-config' '--with-rlm_radutmp' '--with-rlm_rest' '--with-rlm_sql' '--with-rlm_sql_mysql' '--with-mysql-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include/mysql' '--with-rlm_sql_postgresql' '--with-rlm_sql_sqlite' '--with-rlm_sqlcounter' '--with-rlm_sqlippool' '--with-rlm_unix' 'build_alias=x86_64-pc-linux-gnu' 'host_alias=x86_64-openwrt-linux' 'target_alias=x86_64-openwrt-linux' 'CC=ccache_cc' 'CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' 'LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro ' 'LIBS=-latomic -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl' 'CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include ' 'CXX=ccache_cxx' 'CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' --cache-file=/dev/null --srcdir=.
configure: loading site script /openwrt/include/site/x86_64
*** module rlm_pam is disabled.
configure: creating ./config.status
config.status: creating all.mk
config.status: creating config.h
=== configuring in src/modules/rlm_perl (/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21/src/modules/rlm_perl)
configure: running /bin/bash ./configure --disable-option-checking '--prefix=/usr'  '--target=x86_64-openwrt-linux' '--host=x86_64-openwrt-linux' '--build=x86_64-pc-linux-gnu' '--program-prefix=' '--program-suffix=' '--exec-prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--libexecdir=/usr/lib' '--sysconfdir=/etc' '--datadir=/usr/share' '--localstatedir=/var' '--mandir=/usr/man' '--infodir=/usr/info' '--disable-nls' '_python_sysroot=/openwrt/staging_dir/target-x86_64_musl' '_python_prefix=/usr' '_python_exec_prefix=/usr' '--libdir=/usr/lib/freeradius3' '--libexecdir=/usr/lib/freeradius3' '--disable-developer' '--with-threads' '--with-openssl' '--with-openssl-includes=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-openssl-libraries=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--disable-openssl-version-check' '--with-talloc-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-talloc-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--enable-strict-dependencies' '--with-dictdir=/usr/share/freeradius3' '--with-raddbdir=/etc/freeradius3' '--with-radacctdir=/var/db/radacct' '--with-logdir=/var/log' '--without-edir' '--without-snmp' '--without-rlm_cache' '--without-rlm_cache_memcached' '--without-rlm_couchbase' '--without-rlm_counter' '--without-rlm_eap_ikev2' '--without-rlm_eap_sim' '--without-rlm_eap_tnc' '--without-rlm_example' '--without-rlm_idn' '--without-rlm_ippool' '--without-rlm_krb5' '--without-rlm_opendirectory' '--without-rlm_pam' '--without-rlm_perl' '--without-rlm_python' '--without-rlm_redis' '--without-rlm_rediswho' '--without-rlm_ruby' '--without-rlm_securid' '--without-rlm_smsotp' '--without-rlm_sql_db2' '--without-rlm_sql_firebird' '--without-rlm_sql_freetds' '--without-rlm_sql_iodbc' '--without-rlm_sql_oracle' '--without-rlm_sql_unixodbc' '--without-rlm_unbound' '--without-rlm_yubikey' '--with-rlm_eap_peap' '--with-rlm_eap_peap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_peap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_pwd' '--with-rlm_eap_pwd-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_pwd-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_tls' '--with-rlm_eap_tls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_tls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_ttls' '--with-rlm_eap_ttls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_ttls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_ldap' '--with-rlm_ldap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_ldap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-modules=rlm_python3' '--with-rlm-python3-config-bin=/openwrt/staging_dir/target-x86_64_musl/host/bin/python3.9-config' '--with-rlm_radutmp' '--with-rlm_rest' '--with-rlm_sql' '--with-rlm_sql_mysql' '--with-mysql-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include/mysql' '--with-rlm_sql_postgresql' '--with-rlm_sql_sqlite' '--with-rlm_sqlcounter' '--with-rlm_sqlippool' '--with-rlm_unix' 'build_alias=x86_64-pc-linux-gnu' 'host_alias=x86_64-openwrt-linux' 'target_alias=x86_64-openwrt-linux' 'CC=ccache_cc' 'CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' 'LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro ' 'LIBS=-latomic -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl' 'CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include ' 'CXX=ccache_cxx' 'CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' --cache-file=/dev/null --srcdir=.
configure: loading site script /openwrt/include/site/x86_64
*** module rlm_perl is disabled.
configure: creating ./config.status
config.status: creating all.mk
config.status: creating config.h
=== configuring in src/modules/rlm_python (/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21/src/modules/rlm_python)
configure: running /bin/bash ./configure --disable-option-checking '--prefix=/usr'  '--target=x86_64-openwrt-linux' '--host=x86_64-openwrt-linux' '--build=x86_64-pc-linux-gnu' '--program-prefix=' '--program-suffix=' '--exec-prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--libexecdir=/usr/lib' '--sysconfdir=/etc' '--datadir=/usr/share' '--localstatedir=/var' '--mandir=/usr/man' '--infodir=/usr/info' '--disable-nls' '_python_sysroot=/openwrt/staging_dir/target-x86_64_musl' '_python_prefix=/usr' '_python_exec_prefix=/usr' '--libdir=/usr/lib/freeradius3' '--libexecdir=/usr/lib/freeradius3' '--disable-developer' '--with-threads' '--with-openssl' '--with-openssl-includes=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-openssl-libraries=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--disable-openssl-version-check' '--with-talloc-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-talloc-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--enable-strict-dependencies' '--with-dictdir=/usr/share/freeradius3' '--with-raddbdir=/etc/freeradius3' '--with-radacctdir=/var/db/radacct' '--with-logdir=/var/log' '--without-edir' '--without-snmp' '--without-rlm_cache' '--without-rlm_cache_memcached' '--without-rlm_couchbase' '--without-rlm_counter' '--without-rlm_eap_ikev2' '--without-rlm_eap_sim' '--without-rlm_eap_tnc' '--without-rlm_example' '--without-rlm_idn' '--without-rlm_ippool' '--without-rlm_krb5' '--without-rlm_opendirectory' '--without-rlm_pam' '--without-rlm_perl' '--without-rlm_python' '--without-rlm_redis' '--without-rlm_rediswho' '--without-rlm_ruby' '--without-rlm_securid' '--without-rlm_smsotp' '--without-rlm_sql_db2' '--without-rlm_sql_firebird' '--without-rlm_sql_freetds' '--without-rlm_sql_iodbc' '--without-rlm_sql_oracle' '--without-rlm_sql_unixodbc' '--without-rlm_unbound' '--without-rlm_yubikey' '--with-rlm_eap_peap' '--with-rlm_eap_peap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_peap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_pwd' '--with-rlm_eap_pwd-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_pwd-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_tls' '--with-rlm_eap_tls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_tls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_ttls' '--with-rlm_eap_ttls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_ttls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_ldap' '--with-rlm_ldap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_ldap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-modules=rlm_python3' '--with-rlm-python3-config-bin=/openwrt/staging_dir/target-x86_64_musl/host/bin/python3.9-config' '--with-rlm_radutmp' '--with-rlm_rest' '--with-rlm_sql' '--with-rlm_sql_mysql' '--with-mysql-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include/mysql' '--with-rlm_sql_postgresql' '--with-rlm_sql_sqlite' '--with-rlm_sqlcounter' '--with-rlm_sqlippool' '--with-rlm_unix' 'build_alias=x86_64-pc-linux-gnu' 'host_alias=x86_64-openwrt-linux' 'target_alias=x86_64-openwrt-linux' 'CC=ccache_cc' 'CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' 'LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro ' 'LIBS=-latomic -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl' 'CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include ' 'CXX=ccache_cxx' 'CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' --cache-file=/dev/null --srcdir=.
configure: loading site script /openwrt/include/site/x86_64
*** module rlm_python is disabled.
configure: creating ./config.status
config.status: creating all.mk
config.status: creating config.h
=== configuring in src/modules/rlm_radutmp (/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21/src/modules/rlm_radutmp)
configure: running /bin/bash ./configure --disable-option-checking '--prefix=/usr'  '--target=x86_64-openwrt-linux' '--host=x86_64-openwrt-linux' '--build=x86_64-pc-linux-gnu' '--program-prefix=' '--program-suffix=' '--exec-prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--libexecdir=/usr/lib' '--sysconfdir=/etc' '--datadir=/usr/share' '--localstatedir=/var' '--mandir=/usr/man' '--infodir=/usr/info' '--disable-nls' '_python_sysroot=/openwrt/staging_dir/target-x86_64_musl' '_python_prefix=/usr' '_python_exec_prefix=/usr' '--libdir=/usr/lib/freeradius3' '--libexecdir=/usr/lib/freeradius3' '--disable-developer' '--with-threads' '--with-openssl' '--with-openssl-includes=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-openssl-libraries=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--disable-openssl-version-check' '--with-talloc-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-talloc-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--enable-strict-dependencies' '--with-dictdir=/usr/share/freeradius3' '--with-raddbdir=/etc/freeradius3' '--with-radacctdir=/var/db/radacct' '--with-logdir=/var/log' '--without-edir' '--without-snmp' '--without-rlm_cache' '--without-rlm_cache_memcached' '--without-rlm_couchbase' '--without-rlm_counter' '--without-rlm_eap_ikev2' '--without-rlm_eap_sim' '--without-rlm_eap_tnc' '--without-rlm_example' '--without-rlm_idn' '--without-rlm_ippool' '--without-rlm_krb5' '--without-rlm_opendirectory' '--without-rlm_pam' '--without-rlm_perl' '--without-rlm_python' '--without-rlm_redis' '--without-rlm_rediswho' '--without-rlm_ruby' '--without-rlm_securid' '--without-rlm_smsotp' '--without-rlm_sql_db2' '--without-rlm_sql_firebird' '--without-rlm_sql_freetds' '--without-rlm_sql_iodbc' '--without-rlm_sql_oracle' '--without-rlm_sql_unixodbc' '--without-rlm_unbound' '--without-rlm_yubikey' '--with-rlm_eap_peap' '--with-rlm_eap_peap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_peap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_pwd' '--with-rlm_eap_pwd-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_pwd-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_tls' '--with-rlm_eap_tls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_tls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_ttls' '--with-rlm_eap_ttls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_ttls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_ldap' '--with-rlm_ldap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_ldap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-modules=rlm_python3' '--with-rlm-python3-config-bin=/openwrt/staging_dir/target-x86_64_musl/host/bin/python3.9-config' '--with-rlm_radutmp' '--with-rlm_rest' '--with-rlm_sql' '--with-rlm_sql_mysql' '--with-mysql-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include/mysql' '--with-rlm_sql_postgresql' '--with-rlm_sql_sqlite' '--with-rlm_sqlcounter' '--with-rlm_sqlippool' '--with-rlm_unix' 'build_alias=x86_64-pc-linux-gnu' 'host_alias=x86_64-openwrt-linux' 'target_alias=x86_64-openwrt-linux' 'CC=ccache_cc' 'CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' 'LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro ' 'LIBS=-latomic -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl' 'CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include ' 'CXX=ccache_cxx' 'CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' --cache-file=/dev/null --srcdir=.
configure: loading site script /openwrt/include/site/x86_64
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
checking sys/mman.h usability... yes
checking sys/mman.h presence... yes
checking for sys/mman.h... yes
configure: creating ./config.status
config.status: creating all.mk
config.status: creating config.h
=== configuring in src/modules/rlm_realm (/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21/src/modules/rlm_realm)
configure: running /bin/bash ./configure --disable-option-checking '--prefix=/usr'  '--target=x86_64-openwrt-linux' '--host=x86_64-openwrt-linux' '--build=x86_64-pc-linux-gnu' '--program-prefix=' '--program-suffix=' '--exec-prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--libexecdir=/usr/lib' '--sysconfdir=/etc' '--datadir=/usr/share' '--localstatedir=/var' '--mandir=/usr/man' '--infodir=/usr/info' '--disable-nls' '_python_sysroot=/openwrt/staging_dir/target-x86_64_musl' '_python_prefix=/usr' '_python_exec_prefix=/usr' '--libdir=/usr/lib/freeradius3' '--libexecdir=/usr/lib/freeradius3' '--disable-developer' '--with-threads' '--with-openssl' '--with-openssl-includes=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-openssl-libraries=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--disable-openssl-version-check' '--with-talloc-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-talloc-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--enable-strict-dependencies' '--with-dictdir=/usr/share/freeradius3' '--with-raddbdir=/etc/freeradius3' '--with-radacctdir=/var/db/radacct' '--with-logdir=/var/log' '--without-edir' '--without-snmp' '--without-rlm_cache' '--without-rlm_cache_memcached' '--without-rlm_couchbase' '--without-rlm_counter' '--without-rlm_eap_ikev2' '--without-rlm_eap_sim' '--without-rlm_eap_tnc' '--without-rlm_example' '--without-rlm_idn' '--without-rlm_ippool' '--without-rlm_krb5' '--without-rlm_opendirectory' '--without-rlm_pam' '--without-rlm_perl' '--without-rlm_python' '--without-rlm_redis' '--without-rlm_rediswho' '--without-rlm_ruby' '--without-rlm_securid' '--without-rlm_smsotp' '--without-rlm_sql_db2' '--without-rlm_sql_firebird' '--without-rlm_sql_freetds' '--without-rlm_sql_iodbc' '--without-rlm_sql_oracle' '--without-rlm_sql_unixodbc' '--without-rlm_unbound' '--without-rlm_yubikey' '--with-rlm_eap_peap' '--with-rlm_eap_peap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_peap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_pwd' '--with-rlm_eap_pwd-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_pwd-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_tls' '--with-rlm_eap_tls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_tls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_ttls' '--with-rlm_eap_ttls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_ttls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_ldap' '--with-rlm_ldap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_ldap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-modules=rlm_python3' '--with-rlm-python3-config-bin=/openwrt/staging_dir/target-x86_64_musl/host/bin/python3.9-config' '--with-rlm_radutmp' '--with-rlm_rest' '--with-rlm_sql' '--with-rlm_sql_mysql' '--with-mysql-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include/mysql' '--with-rlm_sql_postgresql' '--with-rlm_sql_sqlite' '--with-rlm_sqlcounter' '--with-rlm_sqlippool' '--with-rlm_unix' 'build_alias=x86_64-pc-linux-gnu' 'host_alias=x86_64-openwrt-linux' 'target_alias=x86_64-openwrt-linux' 'CC=ccache_cc' 'CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' 'LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro ' 'LIBS=-latomic -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl' 'CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include ' 'CXX=ccache_cxx' 'CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' --cache-file=/dev/null --srcdir=.
configure: loading site script /openwrt/include/site/x86_64
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
checking for tidc_create in -ltr_tid... no
checking for tidc_create in -ltr_tid in /usr/local/lib... no
checking for tidc_create in -ltr_tid in /opt/lib... no
checking for tid_srvr_get_key_expiration in -ltr_tid... no
checking for tid_srvr_get_key_expiration in -ltr_tid in /usr/local/lib... no
checking for tid_srvr_get_key_expiration in -ltr_tid in /opt/lib... no
checking for trust_router/tr_dh.h... no
checking for trust_router/tr_dh.h in /usr/local/include/... no
checking for trust_router/tr_dh.h in /opt/include/... no
configure: creating ./config.status
config.status: creating all.mk
=== configuring in src/modules/rlm_rest (/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21/src/modules/rlm_rest)
configure: running /bin/bash ./configure --disable-option-checking '--prefix=/usr'  '--target=x86_64-openwrt-linux' '--host=x86_64-openwrt-linux' '--build=x86_64-pc-linux-gnu' '--program-prefix=' '--program-suffix=' '--exec-prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--libexecdir=/usr/lib' '--sysconfdir=/etc' '--datadir=/usr/share' '--localstatedir=/var' '--mandir=/usr/man' '--infodir=/usr/info' '--disable-nls' '_python_sysroot=/openwrt/staging_dir/target-x86_64_musl' '_python_prefix=/usr' '_python_exec_prefix=/usr' '--libdir=/usr/lib/freeradius3' '--libexecdir=/usr/lib/freeradius3' '--disable-developer' '--with-threads' '--with-openssl' '--with-openssl-includes=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-openssl-libraries=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--disable-openssl-version-check' '--with-talloc-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-talloc-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--enable-strict-dependencies' '--with-dictdir=/usr/share/freeradius3' '--with-raddbdir=/etc/freeradius3' '--with-radacctdir=/var/db/radacct' '--with-logdir=/var/log' '--without-edir' '--without-snmp' '--without-rlm_cache' '--without-rlm_cache_memcached' '--without-rlm_couchbase' '--without-rlm_counter' '--without-rlm_eap_ikev2' '--without-rlm_eap_sim' '--without-rlm_eap_tnc' '--without-rlm_example' '--without-rlm_idn' '--without-rlm_ippool' '--without-rlm_krb5' '--without-rlm_opendirectory' '--without-rlm_pam' '--without-rlm_perl' '--without-rlm_python' '--without-rlm_redis' '--without-rlm_rediswho' '--without-rlm_ruby' '--without-rlm_securid' '--without-rlm_smsotp' '--without-rlm_sql_db2' '--without-rlm_sql_firebird' '--without-rlm_sql_freetds' '--without-rlm_sql_iodbc' '--without-rlm_sql_oracle' '--without-rlm_sql_unixodbc' '--without-rlm_unbound' '--without-rlm_yubikey' '--with-rlm_eap_peap' '--with-rlm_eap_peap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_peap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_pwd' '--with-rlm_eap_pwd-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_pwd-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_tls' '--with-rlm_eap_tls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_tls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_ttls' '--with-rlm_eap_ttls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_ttls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_ldap' '--with-rlm_ldap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_ldap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-modules=rlm_python3' '--with-rlm-python3-config-bin=/openwrt/staging_dir/target-x86_64_musl/host/bin/python3.9-config' '--with-rlm_radutmp' '--with-rlm_rest' '--with-rlm_sql' '--with-rlm_sql_mysql' '--with-mysql-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include/mysql' '--with-rlm_sql_postgresql' '--with-rlm_sql_sqlite' '--with-rlm_sqlcounter' '--with-rlm_sqlippool' '--with-rlm_unix' 'build_alias=x86_64-pc-linux-gnu' 'host_alias=x86_64-openwrt-linux' 'target_alias=x86_64-openwrt-linux' 'CC=ccache_cc' 'CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' 'LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro ' 'LIBS=-latomic -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl' 'CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include ' 'CXX=ccache_cxx' 'CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' --cache-file=/dev/null --srcdir=.
configure: loading site script /openwrt/include/site/x86_64
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
checking for gawk... gawk
checking for curl-config... /openwrt/staging_dir/target-x86_64_musl/host/bin/curl-config
checking for the version of libcurl... 7.77.0
checking for libcurl >= version 7.19.1... yes
checking whether libcurl is usable... yes
checking for curl_free... yes
configure: curl-config's cflags were "-I/openwrt/staging_dir/target-x86_64_musl/usr/include"
configure: Sanitized cflags are "-isystem /openwrt/staging_dir/target-x86_64_musl/usr/include"
checking for json/json.h... no
checking for json/json.h in /usr/local/include/... no
checking for json/json.h in /opt/include/... no
checking for json-c/json.h... yes
checking for json_c_version in -ljson-c... yes
checking for json_c_version... yes
checking for json_type_to_name... yes
configure: creating ./config.status
config.status: creating all.mk
config.status: creating config.h
=== configuring in src/modules/rlm_sql (/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21/src/modules/rlm_sql)
configure: running /bin/bash ./configure --disable-option-checking '--prefix=/usr'  '--target=x86_64-openwrt-linux' '--host=x86_64-openwrt-linux' '--build=x86_64-pc-linux-gnu' '--program-prefix=' '--program-suffix=' '--exec-prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--libexecdir=/usr/lib' '--sysconfdir=/etc' '--datadir=/usr/share' '--localstatedir=/var' '--mandir=/usr/man' '--infodir=/usr/info' '--disable-nls' '_python_sysroot=/openwrt/staging_dir/target-x86_64_musl' '_python_prefix=/usr' '_python_exec_prefix=/usr' '--libdir=/usr/lib/freeradius3' '--libexecdir=/usr/lib/freeradius3' '--disable-developer' '--with-threads' '--with-openssl' '--with-openssl-includes=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-openssl-libraries=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--disable-openssl-version-check' '--with-talloc-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-talloc-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--enable-strict-dependencies' '--with-dictdir=/usr/share/freeradius3' '--with-raddbdir=/etc/freeradius3' '--with-radacctdir=/var/db/radacct' '--with-logdir=/var/log' '--without-edir' '--without-snmp' '--without-rlm_cache' '--without-rlm_cache_memcached' '--without-rlm_couchbase' '--without-rlm_counter' '--without-rlm_eap_ikev2' '--without-rlm_eap_sim' '--without-rlm_eap_tnc' '--without-rlm_example' '--without-rlm_idn' '--without-rlm_ippool' '--without-rlm_krb5' '--without-rlm_opendirectory' '--without-rlm_pam' '--without-rlm_perl' '--without-rlm_python' '--without-rlm_redis' '--without-rlm_rediswho' '--without-rlm_ruby' '--without-rlm_securid' '--without-rlm_smsotp' '--without-rlm_sql_db2' '--without-rlm_sql_firebird' '--without-rlm_sql_freetds' '--without-rlm_sql_iodbc' '--without-rlm_sql_oracle' '--without-rlm_sql_unixodbc' '--without-rlm_unbound' '--without-rlm_yubikey' '--with-rlm_eap_peap' '--with-rlm_eap_peap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_peap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_pwd' '--with-rlm_eap_pwd-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_pwd-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_tls' '--with-rlm_eap_tls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_tls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_ttls' '--with-rlm_eap_ttls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_ttls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_ldap' '--with-rlm_ldap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_ldap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-modules=rlm_python3' '--with-rlm-python3-config-bin=/openwrt/staging_dir/target-x86_64_musl/host/bin/python3.9-config' '--with-rlm_radutmp' '--with-rlm_rest' '--with-rlm_sql' '--with-rlm_sql_mysql' '--with-mysql-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include/mysql' '--with-rlm_sql_postgresql' '--with-rlm_sql_sqlite' '--with-rlm_sqlcounter' '--with-rlm_sqlippool' '--with-rlm_unix' 'build_alias=x86_64-pc-linux-gnu' 'host_alias=x86_64-openwrt-linux' 'target_alias=x86_64-openwrt-linux' 'CC=ccache_cc' 'CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' 'LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro ' 'LIBS=-latomic -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl' 'CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include ' 'CXX=ccache_cxx' 'CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' --cache-file=/dev/null --srcdir=.
configure: loading site script /openwrt/include/site/x86_64
checking for x86_64-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
configure: creating ./config.status
config.status: creating all.mk
=== configuring in ./drivers/rlm_sql_iodbc (/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21/src/modules/rlm_sql/./drivers/rlm_sql_iodbc)
configure: running /bin/bash ./configure --disable-option-checking '--prefix=/usr'  '--target=x86_64-openwrt-linux' '--host=x86_64-openwrt-linux' '--build=x86_64-pc-linux-gnu' '--program-prefix=' '--program-suffix=' '--exec-prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--libexecdir=/usr/lib' '--sysconfdir=/etc' '--datadir=/usr/share' '--localstatedir=/var' '--mandir=/usr/man' '--infodir=/usr/info' '--disable-nls' '_python_sysroot=/openwrt/staging_dir/target-x86_64_musl' '_python_prefix=/usr' '_python_exec_prefix=/usr' '--libdir=/usr/lib/freeradius3' '--libexecdir=/usr/lib/freeradius3' '--disable-developer' '--with-threads' '--with-openssl' '--with-openssl-includes=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-openssl-libraries=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--disable-openssl-version-check' '--with-talloc-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-talloc-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--enable-strict-dependencies' '--with-dictdir=/usr/share/freeradius3' '--with-raddbdir=/etc/freeradius3' '--with-radacctdir=/var/db/radacct' '--with-logdir=/var/log' '--without-edir' '--without-snmp' '--without-rlm_cache' '--without-rlm_cache_memcached' '--without-rlm_couchbase' '--without-rlm_counter' '--without-rlm_eap_ikev2' '--without-rlm_eap_sim' '--without-rlm_eap_tnc' '--without-rlm_example' '--without-rlm_idn' '--without-rlm_ippool' '--without-rlm_krb5' '--without-rlm_opendirectory' '--without-rlm_pam' '--without-rlm_perl' '--without-rlm_python' '--without-rlm_redis' '--without-rlm_rediswho' '--without-rlm_ruby' '--without-rlm_securid' '--without-rlm_smsotp' '--without-rlm_sql_db2' '--without-rlm_sql_firebird' '--without-rlm_sql_freetds' '--without-rlm_sql_iodbc' '--without-rlm_sql_oracle' '--without-rlm_sql_unixodbc' '--without-rlm_unbound' '--without-rlm_yubikey' '--with-rlm_eap_peap' '--with-rlm_eap_peap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_peap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_pwd' '--with-rlm_eap_pwd-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_pwd-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_tls' '--with-rlm_eap_tls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_tls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_ttls' '--with-rlm_eap_ttls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_ttls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_ldap' '--with-rlm_ldap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_ldap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-modules=rlm_python3' '--with-rlm-python3-config-bin=/openwrt/staging_dir/target-x86_64_musl/host/bin/python3.9-config' '--with-rlm_radutmp' '--with-rlm_rest' '--with-rlm_sql' '--with-rlm_sql_mysql' '--with-mysql-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include/mysql' '--with-rlm_sql_postgresql' '--with-rlm_sql_sqlite' '--with-rlm_sqlcounter' '--with-rlm_sqlippool' '--with-rlm_unix' 'build_alias=x86_64-pc-linux-gnu' 'host_alias=x86_64-openwrt-linux' 'target_alias=x86_64-openwrt-linux' 'CC=ccache_cc' 'CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' 'LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro ' 'LIBS=-latomic -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl' 'CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include ' 'CXX=ccache_cxx' 'CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' --cache-file=/dev/null --srcdir=.
configure: loading site script /openwrt/include/site/x86_64
*** module rlm_sql_iodbc is disabled.
configure: creating ./config.status
config.status: creating all.mk
=== configuring in ./drivers/rlm_sql_mysql (/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21/src/modules/rlm_sql/./drivers/rlm_sql_mysql)
configure: running /bin/bash ./configure --disable-option-checking '--prefix=/usr'  '--target=x86_64-openwrt-linux' '--host=x86_64-openwrt-linux' '--build=x86_64-pc-linux-gnu' '--program-prefix=' '--program-suffix=' '--exec-prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--libexecdir=/usr/lib' '--sysconfdir=/etc' '--datadir=/usr/share' '--localstatedir=/var' '--mandir=/usr/man' '--infodir=/usr/info' '--disable-nls' '_python_sysroot=/openwrt/staging_dir/target-x86_64_musl' '_python_prefix=/usr' '_python_exec_prefix=/usr' '--libdir=/usr/lib/freeradius3' '--libexecdir=/usr/lib/freeradius3' '--disable-developer' '--with-threads' '--with-openssl' '--with-openssl-includes=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-openssl-libraries=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--disable-openssl-version-check' '--with-talloc-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-talloc-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--enable-strict-dependencies' '--with-dictdir=/usr/share/freeradius3' '--with-raddbdir=/etc/freeradius3' '--with-radacctdir=/var/db/radacct' '--with-logdir=/var/log' '--without-edir' '--without-snmp' '--without-rlm_cache' '--without-rlm_cache_memcached' '--without-rlm_couchbase' '--without-rlm_counter' '--without-rlm_eap_ikev2' '--without-rlm_eap_sim' '--without-rlm_eap_tnc' '--without-rlm_example' '--without-rlm_idn' '--without-rlm_ippool' '--without-rlm_krb5' '--without-rlm_opendirectory' '--without-rlm_pam' '--without-rlm_perl' '--without-rlm_python' '--without-rlm_redis' '--without-rlm_rediswho' '--without-rlm_ruby' '--without-rlm_securid' '--without-rlm_smsotp' '--without-rlm_sql_db2' '--without-rlm_sql_firebird' '--without-rlm_sql_freetds' '--without-rlm_sql_iodbc' '--without-rlm_sql_oracle' '--without-rlm_sql_unixodbc' '--without-rlm_unbound' '--without-rlm_yubikey' '--with-rlm_eap_peap' '--with-rlm_eap_peap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_peap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_pwd' '--with-rlm_eap_pwd-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_pwd-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_tls' '--with-rlm_eap_tls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_tls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_eap_ttls' '--with-rlm_eap_ttls-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_eap_ttls-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-rlm_ldap' '--with-rlm_ldap-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include' '--with-rlm_ldap-lib-dir=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-modules=rlm_python3' '--with-rlm-python3-config-bin=/openwrt/staging_dir/target-x86_64_musl/host/bin/python3.9-config' '--with-rlm_radutmp' '--with-rlm_rest' '--with-rlm_sql' '--with-rlm_sql_mysql' '--with-mysql-include-dir=/openwrt/staging_dir/target-x86_64_musl/usr/include/mysql' '--with-rlm_sql_postgresql' '--with-rlm_sql_sqlite' '--with-rlm_sqlcounter' '--with-rlm_sqlippool' '--with-rlm_unix' 'build_alias=x86_64-pc-linux-gnu' 'host_alias=x86_64-openwrt-linux' 'target_alias=x86_64-openwrt-linux' 'CC=ccache_cc' 'CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' 'LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro ' 'LIBS=-latomic -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl -lcrypto -lssl' 'CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include ' 'CXX=ccache_cxx' 'CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21=freeradius-server-release_3_0_21 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_OPENSSL_RAND_H' --cache-file=/dev/null --srcdir=.
configure: loading site script /openwrt/include/site/x86_64
checking for x86_64-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
checking for mysql_config... no
checking for mysql_init in -lmysqlclient_r in /usr/lib... no
checking for mysql_init in -lmysqlclient_r in /usr/lib/mysql... no
checking for mysql_init in -lmysqlclient_r in /usr/local/lib/mysql... no
checking for mysql_init in -lmysqlclient_r in /usr/local/mysql/lib/mysql... no
checking for mysql_init in -lmysqlclient_r... no
checking for mysql_init in -lmysqlclient_r in /usr/local/lib... no
checking for mysql_init in -lmysqlclient_r in /opt/lib... no
checking for mysql_init in -lmysqlclient in /usr/lib... no
checking for mysql_init in -lmysqlclient in /usr/lib/mysql... no
checking for mysql_init in -lmysqlclient in /usr/local/lib/mysql... no
checking for mysql_init in -lmysqlclient in /usr/local/mysql/lib/mysql... no
checking for mysql_init in -lmysqlclient... no
checking for mysql_init in -lmysqlclient in /usr/local/lib... no
checking for mysql_init in -lmysqlclient in /opt/lib... no
./configure: line 3144: mariadb_config: command not found
checking for mysql_init in -lmariadb (using mariadb_config)... no
configure: WARNING: MySQL libraries not found. Use --with-mysql-lib-dir=<path>.
./configure: line 3261: mariadb_config: command not found
checking for mysql.h (using mariadb_config --cflags)... no
./configure: line 3292: mariadb_config: command not found
checking for mysql.h (using mariadb_config --include)... no
checking for mysql/mysql.h in /openwrt/staging_dir/target-x86_64_musl/usr/include/mysql/... no
checking for mysql/mysql.h in /usr/local/include/... no
checking for mysql/mysql.h in /usr/local/mysql/include/... no
checking for mysql/mysql.h... no
checking for mysql/mysql.h in /usr/local/include/... no
checking for mysql/mysql.h in /opt/include/... no
configure: WARNING: MySQL headers not found. Use --with-mysql-include-dir=<path>.
configure: error: set --without-rlm_sql_mysql to disable it explicitly.
configure: error: ./configure failed for ./drivers/rlm_sql_mysql
configure: error: ./configure failed for src/modules/rlm_sql
make[3]: *** [Makefile:770: /openwrt/build_dir/target-x86_64_musl/freeradius-server-release_3_0_21/.configured_059ce960b95c68443337f43a915dbd53] Error 1
```
