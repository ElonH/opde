---
title: "compile.37"
date: 2021-06-20 22:36:26.364462
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
make package/feeds/packages/uw-imap/compile -j$(nproc) || make package/feeds/packages/uw-imap/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-fix_Makefiles_and_shlib.patch using plaintext: 
patching file Makefile
patching file src/osdep/unix/Makefile

Applying ./patches/002-imap-2004a-doc.patch using plaintext: 
patching file src/imapd/imapd.8
patching file src/ipopd/ipopd.8

Applying ./patches/003-imap-2007e-overflow.patch using plaintext: 
patching file src/c-client/rfc822.c

Applying ./patches/005-imap-2007e-authmd5.patch using plaintext: 
patching file src/c-client/auth_md5.c

Applying ./patches/006-imap-2007f-format-security.patch using plaintext: 
patching file src/osdep/unix/flocklnx.c

Applying ./patches/007-imap-2007e-poll.patch using plaintext: 
patching file src/osdep/unix/os_lnx.c
patching file src/osdep/unix/os_slx.c
patching file src/osdep/unix/tcp_unix.c

Applying ./patches/010-imap-2007f-openssl-1.1.patch using plaintext: 
patching file src/osdep/unix/ssl_unix.c

Applying ./patches/020-deprecated-openssl.patch using plaintext: 
patching file src/osdep/unix/ssl_unix.c
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/imap-2007f'
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/imap-2007f'
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+ Building in full compliance with RFC 3501 security
+ requirements:
++ TLS/SSL encryption is supported
++ Unencrypted plaintext passwords are prohibited
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/imap-2007f'
Applying an process to sources...
tools/an "ln -s" src/c-client c-client
tools/an "ln -s" src/ansilib c-client
tools/an "ln -s" src/charset c-client
tools/an "ln -s" src/osdep/unix c-client
tools/an "ln -s" src/mtest mtest
tools/an "ln -s" src/ipopd ipopd
tools/an "ln -s" src/imapd imapd
tools/an "ln -s" src/mailutil mailutil
tools/an "ln -s" src/mlock mlock
tools/an "ln -s" src/dmail dmail
tools/an "ln -s" src/tmail tmail
ln -s tools/an .
make build EXTRACFLAGS='-Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/imap-2007f=imap-2007f -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -fPIC -DPIC -D_REENTRANT -DDISABLE_POP_PROXY -fno-strict-aliasing -Wno-pointer-sign -Wno-implicit-function-declaration -Wno-incompatible-pointer-types' EXTRALDFLAGS='' EXTRADRIVERS='mbox' EXTRAAUTHENTICATORS='' PASSWDTYPE=std SSLTYPE=nopwd IP=6 EXTRASPECIALS='' BUILDTYPE=slx
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/imap-2007f'
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/imap-2007f'
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+ Building with IPv6 support
+
+ NOTE: Some versions of glibc have a bug in the getaddrinfo
+ call which does DNS name resolution. This bug causes host
+ names to be canonicalized incorrectly, as well as doing an
+ unnecessary and performance-sapping reverse DNS call. This
+ problem does not affect the IPv4 gethostbyname call.
+
+ getaddrinfo works properly on Mac OS X and Windows. However,
+ the problem has been observed on some Linux systems.
+
+ If you answer n to the following question the build will be
+ cancelled and you must rebuild. If you did not specify IPv6
+ yourself, try adding IP6=4 to the make command line.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/imap-2007f'
Building c-client for slx...
cd c-client;make slx EXTRACFLAGS='-Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/imap-2007f=imap-2007f -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -fPIC -DPIC -D_REENTRANT -DDISABLE_POP_PROXY -fno-strict-aliasing -Wno-pointer-sign -Wno-implicit-function-declaration -Wno-incompatible-pointer-types'\
 EXTRALDFLAGS=''\
 EXTRADRIVERS='mbox'\
 EXTRAAUTHENTICATORS=''\
 PASSWDTYPE=std SSLTYPE=nopwd IP=6\
   OSTYPE=slx
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/imap-2007f/c-client'
You are building for libc6/glibc versions of Secure Linux
If you want libc5 versions you must use sl5 instead!
If you want libc4 versions you must use sl4 instead!
make build EXTRACFLAGS='-Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/imap-2007f=imap-2007f -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -fPIC -DPIC -D_REENTRANT -DDISABLE_POP_PROXY -fno-strict-aliasing -Wno-pointer-sign -Wno-implicit-function-declaration -Wno-incompatible-pointer-types' EXTRALDFLAGS='' EXTRADRIVERS='mbox' EXTRAAUTHENTICATORS='' PASSWDTYPE=std SSLTYPE=nopwd IP=6  OS=slx \
 SIGTYPE=psx CHECKPW=psx CRXTYPE=nfs \
 SPOOLDIR=/var/spool \
 ACTIVEFILE=/var/lib/news/active \
 RSHPATH=/usr/bin/rsh \
 BASECFLAGS="-g -Os -pipe -fno-omit-frame-pointer" \
 BASELDFLAGS="-lcrypt"
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/imap-2007f/c-client'
sh -c 'rm -rf auths.c crexcl.c ip_unix.c linkage.[ch] siglocal.c osdep*.[ch] *.o ARCHIVE *FLAGS *TYPE c-client.a || true'
Building with SSL
ln -s ssl_unix.c osdepssl.c
echo "  ssl_onceonlyinit ();" >> linkage.c
Normal UNIX SSL load flags
Building with SSL and plaintext passwords disabled unless SSL/TLS
echo "  mail_parameters (NIL,SET_DISABLEPLAINTEXT,(void *) 2);" >> linkage.c
Once-only environment setup...
echo "ar rc c-client.a osdep.o mail.o misc.o newsrc.o smanager.o utf8.o utf8aux.o siglocal.o dummy.o pseudo.o netmsg.o flstring.o fdstring.o rfc822.o nntp.o smtp.o imap4r1.o pop3.o unix.o mbx.o mmdf.o tenex.o mtx.o news.o phile.o mh.o mx.o mix.o;mips-openwrt-linux-musl-gcc-ranlib c-client.a" > ARCHIVE
echo "-I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/openssl -DSSL_CERT_DIRECTORY=\"/etc/ssl/certs\" -DSSL_KEY_DIRECTORY=\"/etc/ssl/certs\" -DCREATEPROTO=unixproto -DEMPTYPROTO=unixproto -DMD5ENABLE=\"/etc/cram-md5.pwd\" -DMAILSPOOL=\"/var/spool/mail\" -DANONYMOUSHOME=\"/var/spool/mail/anonymous\" -DACTIVEFILE=\"/var/lib/news/active\" -DNEWSSPOOL=\"/var/spool/news\" -DRSHPATH=\"/usr/bin/rsh\" -DLOCKPGM=\"\" -DLOCKPGM1=\"/usr/libexec/mlock\" -DLOCKPGM2=\"/usr/sbin/mlock\" -DLOCKPGM3=\"/etc/mlock\"" > OSCFLAGS
echo "ccache_cc -g -Os -pipe -fno-omit-frame-pointer -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/imap-2007f=imap-2007f -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -fPIC -DPIC -D_REENTRANT -DDISABLE_POP_PROXY -fno-strict-aliasing -Wno-pointer-sign -Wno-implicit-function-declaration -Wno-incompatible-pointer-types -DCHUNKSIZE=65536 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/openssl -DSSL_CERT_DIRECTORY=\"/etc/ssl/certs\" -DSSL_KEY_DIRECTORY=\"/etc/ssl/certs\" -DCREATEPROTO=unixproto -DEMPTYPROTO=unixproto -DMD5ENABLE=\"/etc/cram-md5.pwd\" -DMAILSPOOL=\"/var/spool/mail\" -DANONYMOUSHOME=\"/var/spool/mail/anonymous\" -DACTIVEFILE=\"/var/lib/news/active\" -DNEWSSPOOL=\"/var/spool/news\" -DRSHPATH=\"/usr/bin/rsh\" -DLOCKPGM=\"\" -DLOCKPGM1=\"/usr/libexec/mlock\" -DLOCKPGM2=\"/usr/sbin/mlock\" -DLOCKPGM3=\"/etc/mlock\" -shared  -Wl,-soname,libc-client.so \
-o libc-client.so.2007f osdep.o mail.o misc.o newsrc.o smanager.o utf8.o utf8aux.o siglocal.o dummy.o pseudo.o netmsg.o flstring.o fdstring.o rfc822.o nntp.o smtp.o imap4r1.o pop3.o unix.o mbx.o mmdf.o tenex.o mtx.o news.o phile.o mh.o mx.o mix.o -lcrypt  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lssl -lcrypto " >> ARCHIVE
echo slx > OSTYPE
./drivers mbox imap nntp pop3 mix mx mbx tenex mtx mh mmdf unix news phile dummy
./mkauths  ext md5 pla log
echo "  mail_versioncheck (CCLIENTVERSION);" >> linkage.c
ln -s os_slx.h osdep.h
ln -s os_slx.c osdepbas.c
ln -s log_std.c osdeplog.c
ln -s sig_psx.c siglocal.c
ln -s crx_nfs.c crexcl.c
ln -s ip6_unix.c ip_unix.c
sh -c '(test slx = sc5 -o slx = sco -o ! -f /usr/include/sys/statvfs.h) && echo -DNOFSTATVFS >> OSCFLAGS || fgrep statvfs64 /usr/include/sys/statvfs.h > /dev/null || echo -DNOFSTATVFS64 >> OSCFLAGS'
Standard password authentication
ln -s ckp_psx.c osdepckp.c
cat osdepbas.c osdepckp.c osdeplog.c osdepssl.c > osdep.c
Building OS-dependent module
If you get No such file error messages for files x509.h, ssl.h,
pem.h, buffer.h, bio.h, and crypto.h, that means that OpenSSL
is not installed on your system. Either install OpenSSL first
or build with command: make slx SSLTYPE=none
ccache_cc -c -g -Os -pipe -fno-omit-frame-pointer -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/imap-2007f=imap-2007f -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -fPIC -DPIC -D_REENTRANT -DDISABLE_POP_PROXY -fno-strict-aliasing -Wno-pointer-sign -Wno-implicit-function-declaration -Wno-incompatible-pointer-types -DCHUNKSIZE=65536 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/openssl -DSSL_CERT_DIRECTORY=\"/etc/ssl/certs\" -DSSL_KEY_DIRECTORY=\"/etc/ssl/certs\" -DCREATEPROTO=unixproto -DEMPTYPROTO=unixproto -DMD5ENABLE=\"/etc/cram-md5.pwd\" -DMAILSPOOL=\"/var/spool/mail\" -DANONYMOUSHOME=\"/var/spool/mail/anonymous\" -DACTIVEFILE=\"/var/lib/news/active\" -DNEWSSPOOL=\"/var/spool/news\" -DRSHPATH=\"/usr/bin/rsh\" -DLOCKPGM=\"\" -DLOCKPGM1=\"/usr/libexec/mlock\" -DLOCKPGM2=\"/usr/sbin/mlock\" -DLOCKPGM3=\"/etc/mlock\" -c osdep.c
osdep.c:232:10: fatal error: x509v3.h: No such file or directory
 #include <x509v3.h>
          ^~~~~~~~~~
compilation terminated.
make[7]: *** [Makefile:936: osdep.o] Error 1
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/imap-2007f/c-client'
make[6]: *** [Makefile:687: slx] Error 2
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/imap-2007f/c-client'
make[5]: *** [Makefile:683: OSTYPE] Error 2
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/imap-2007f'
make[4]: *** [Makefile:311: slx] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/imap-2007f'
make[3]: *** [Makefile:76: /openwrt/build_dir/target-mips_24kc_musl/imap-2007f/.built] Error 2
```
