---
title: "compile.41"
date: 2021-06-23 23:11:37.903304
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
make package/feeds/packages/exim/compile -j$(nproc) || make package/feeds/packages/exim/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-allow-json-dynamic-lookup.patch using plaintext: 
patching file src/drtables.c

Applying ./patches/030-openssl-deprecated.patch using plaintext: 
patching file src/dane-openssl.c
patching file src/pdkim/signing.c
patching file src/tls-openssl.c
patching file src/tlscert-openssl.c

Applying ./patches/100-localscan_dlopen.patch using plaintext: 
patching file src/config.h.defaults
patching file src/EDITME
patching file src/globals.c
patching file src/globals.h
patching file src/local_scan.c
patching file src/readconf.c
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/exim-ldap/exim-4.94.2'

>>> Creating links to source files...
>>> Creating lookups/Makefile for building dynamic modules
>>> New Makefile & lookups/Makefile installed
>>> Use "make makefile" if you need to force rebuilding of the makefile
 
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/exim-ldap/exim-4.94.2'
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/exim-ldap/exim-4.94.2/build-Linux-x86_64'
cc buildconfig.c
/bin/sh ../scripts/Configure-config.h "make"
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/exim-ldap/exim-4.94.2/build-Linux-x86_64'
make[5]: 'buildconfig' is up to date.
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/exim-ldap/exim-4.94.2/build-Linux-x86_64'
Building configuration file config.h
>>> config.h built

cc -DMACRO_PREDEF macro_predef.c
cc -DMACRO_PREDEF globals.c
cc -DMACRO_PREDEF readconf.c
cc -DMACRO_PREDEF route.c
cc -DMACRO_PREDEF transport.c
cc -DMACRO_PREDEF drtables.c
cc -DMACRO_PREDEF tls.c
cc -DMACRO_PREDEF transports/appendfile.c
cc -DMACRO_PREDEF transports/autoreply.c
cc -DMACRO_PREDEF transports/lmtp.c
cc -DMACRO_PREDEF transports/pipe.c
cc -DMACRO_PREDEF transports/queuefile.c
cc -DMACRO_PREDEF transports/smtp.c
cc -DMACRO_PREDEF routers/accept.c
cc -DMACRO_PREDEF routers/dnslookup.c
cc -DMACRO_PREDEF routers/ipliteral.c
cc -DMACRO_PREDEF routers/iplookup.c
cc -DMACRO_PREDEF routers/manualroute.c
cc -DMACRO_PREDEF routers/queryprogram.c
cc -DMACRO_PREDEF routers/redirect.c
cc -DMACRO_PREDEF auths/auth-spa.c
cc -DMACRO_PREDEF auths/cram_md5.c
cc -DMACRO_PREDEF auths/cyrus_sasl.c
cc -DMACRO_PREDEF auths/dovecot.c
cc -DMACRO_PREDEF auths/gsasl_exim.c
cc -DMACRO_PREDEF auths/heimdal_gssapi.c
cc -DMACRO_PREDEF auths/plaintext.c
cc -DMACRO_PREDEF auths/spa.c
cc -DMACRO_PREDEF auths/tls.c
cc -DMACRO_PREDEF auths/external.c
cc -DMACRO_PREDEF dkim.c
cc -DMACRO_PREDEF malware.c
cc -DMACRO_PREDEF pdkim/signing.c
cc -o macro_predef
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/exim-ldap/exim-4.94.2/build-Linux-x86_64'
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/exim-ldap/exim-4.94.2'
/bin/sh scripts/source_checks
`Makefile' is up to date.
 
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/exim-ldap/exim-4.94.2/build-Linux-x86_64'
/bin/sh ../scripts/Configure-os.c
./macro_predef > macro.c
ccache_cc exim_dbmbuild.c
ccache_cc -DEXIM_DUMPDB exim_dbutil.c
ccache_cc -DCOMPILE_UTILITY os.c
ccache_cc -DCOMPILE_UTILITY store.c
ccache_cc -DEXIM_FIXDB exim_dbutil.c
ccache_cc -DCOMPILE_UTILITY queue.c
ccache_cc -DEXIM_TIDYDB exim_dbutil.c
ccache_cc exim_lock.c
ccache_cc -o exim_lock
>>> exim_lock utility built
 
ccache_cc acl.c
acl.c: In function 'acl_check_condition':
acl.c:3202:24: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
        submission_name = parse_fix_phrase(p+6, pp-p-6);
                        ^
ccache_cc base64.c
ccache_cc child.c
ccache_cc crypt16.c
ccache_cc daemon.c
ccache_cc dbfn.c
ccache_cc debug.c
debug.c: In function 'debug_print_socket':
debug.c:354:22: warning: passing argument 2 of 'getpeername' from incompatible pointer type [-Wincompatible-pointer-types]
  if (getpeername(fd, sinp, &alen) == 0)
                      ^~~~
In file included from ../../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify/sys/socket.h:22,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/netinet/tcp.h:98,
                 from os.h:80,
                 from exim.h:36,
                 from debug.c:9:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/sys/socket.h:339:23: note: expected 'struct sockaddr * restrict' but argument is of type 'struct sockaddr_in *'
 int getpeername (int, struct sockaddr *__restrict, socklen_t *__restrict);
                       ^
debug.c:366:22: warning: passing argument 2 of 'getpeername' from incompatible pointer type [-Wincompatible-pointer-types]
  if (getpeername(fd, sin6p, &alen) == 0)
                      ^~~~~
In file included from ../../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify/sys/socket.h:22,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/netinet/tcp.h:98,
                 from os.h:80,
                 from exim.h:36,
                 from debug.c:9:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/sys/socket.h:339:23: note: expected 'struct sockaddr * restrict' but argument is of type 'struct sockaddr_in6 *'
 int getpeername (int, struct sockaddr *__restrict, socklen_t *__restrict);
                       ^
debug.c:379:29: warning: passing argument 2 of 'getpeername' from incompatible pointer type [-Wincompatible-pointer-types]
         if (getpeername(fd, sunp, &alen) == 0)
                             ^~~~
In file included from ../../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify/sys/socket.h:22,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/netinet/tcp.h:98,
                 from os.h:80,
                 from exim.h:36,
                 from debug.c:9:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/sys/socket.h:339:23: note: expected 'struct sockaddr * restrict' but argument is of type 'struct sockaddr_un *'
 int getpeername (int, struct sockaddr *__restrict, socklen_t *__restrict);
                       ^
ccache_cc deliver.c
ccache_cc directory.c
ccache_cc dns.c
ccache_cc drtables.c
ccache_cc enq.c
ccache_cc exim.c
In file included from exim.h:531,
                 from exim.c:14:
exim.c: In function 'exim_nullstd':
exim.c:558:33: warning: too many arguments for format [-Wformat-extra-args]
       string_open_failed(errno, "/dev/null", NULL));
                                 ^~~~~~~~~~~
functions.h:556:57: note: in definition of macro 'string_open_failed'
  string_open_failed_trc(eno, US __FUNCTION__, __LINE__, fmt, __VA_ARGS__)
                                                         ^~~
exim.c: In function 'main':
exim.c:4823:17: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
 originator_name = parse_fix_phrase(originator_name, Ustrlen(originator_name));
                 ^
ccache_cc expand.c
ccache_cc filter.c
filter.c: In function 'interpret_commands':
filter.c:2021:23: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  else headers_charset = s; /*XXX loses track of const */
                       ^
filter.c:2045:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
       fmsg = expargs[0];  /*XXX loses track of const */
            ^
filter.c:2132:40: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
    if (i != mailarg_index_text) for (p = s; *p != 0; p++)
                                        ^
filter.c:2182:24: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
    commands->args[i].u = s; /*XXX loses track of const */
                        ^
ccache_cc filtertest.c
ccache_cc globals.c
ccache_cc dkim.c
ccache_cc dkim_transport.c
ccache_cc hash.c
ccache_cc header.c
ccache_cc host.c
ccache_cc ip.c
ccache_cc log.c
ccache_cc lss.c
ccache_cc match.c
ccache_cc md5.c
ccache_cc moan.c
ccache_cc os.c
ccache_cc parse.c
ccache_cc priv.c
ccache_cc queue.c
ccache_cc rda.c
ccache_cc readconf.c
ccache_cc receive.c
ccache_cc retry.c
ccache_cc rewrite.c
ccache_cc rfc2047.c
ccache_cc route.c
ccache_cc search.c
ccache_cc sieve.c
ccache_cc smtp_in.c
ccache_cc smtp_out.c
ccache_cc spool_in.c
ccache_cc spool_out.c
ccache_cc std-crypto.c
ccache_cc store.c
ccache_cc string.c
ccache_cc tls.c
ccache_cc tod.c
ccache_cc transport.c
ccache_cc tree.c
ccache_cc verify.c
ccache_cc environment.c
ccache_cc macro.c
ccache_cc malware.c
ccache_cc mime.c
ccache_cc regex.c
ccache_cc spam.c
ccache_cc spool_mbox.c
ccache_cc arc.c
ccache_cc bmi_spam.c
ccache_cc dane.c
ccache_cc dcc.c
ccache_cc dmarc.c
ccache_cc imap_utf7.c
ccache_cc spf.c
ccache_cc srs.c
ccache_cc utf8.c
>>> exicyclog script built
>>> exinext script built
>>> exiwhat script built
>>> exigrep script built
>>> eximstats script built
>>> exipick script built
>>> exiqgrep script built
>>> exiqsumm script built
>>> transport-filter.pl script built
>>> convert4r3 script built
>>> convert4r4 script built
>>> exim_checkaccess script built

ccache_cc -o exim_dbmbuild
>>> exim_dbmbuild utility built
 
ccache_cc -o exim_dumpdb
>>> exim_dumpdb utility built
 
ccache_cc -o exim_fixdb
>>> exim_fixdb utility built
 
ccache_cc -o exim_tidydb
>>> exim_tidydb utility built
 
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/exim-ldap/exim-4.94.2/build-Linux-x86_64/lookups'
ccache_cc dsearch.c
ccache_cc lsearch.c
ccache_cc ldap.c
ccache_cc spf.c
ccache_cc readsock.c
ccache_cc lf_quote.c
ccache_cc lf_check_file.c
ccache_cc lf_sqlperform.c
ccache_cc -shared cdb.c
ccache_cc -shared dbmdb.c
ccache_cc -shared dnsdb.c
ccache_cc -shared json.c
ccache_cc -shared mysql.c
mysql.c:16:10: fatal error: mysql.h: No such file or directory
 #include <mysql.h>       /* The system header */
          ^~~~~~~~~
compilation terminated.
make[6]: *** [Makefile:54: mysql.so] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/exim-ldap/exim-4.94.2/build-Linux-x86_64/lookups'
make[5]: *** [Makefile:1033: buildlookups] Error 2
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/exim-ldap/exim-4.94.2/build-Linux-x86_64'
make[4]: *** [Makefile:35: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/exim-ldap/exim-4.94.2'
make[3]: *** [Makefile:288: /openwrt/build_dir/target-x86_64_musl/exim-ldap/exim-4.94.2/.built] Error 2
```
