---
title: "compile.37"
date: 2021-06-20 22:32:33.812319
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
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/exim-ldap/exim-4.94.2'

>>> Creating links to source files...
>>> Creating lookups/Makefile for building dynamic modules
>>> New Makefile & lookups/Makefile installed
>>> Use "make makefile" if you need to force rebuilding of the makefile
 
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/exim-ldap/exim-4.94.2'
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/exim-ldap/exim-4.94.2/build-Linux-mips'
cc buildconfig.c
/bin/sh ../scripts/Configure-config.h "make"
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/exim-ldap/exim-4.94.2/build-Linux-mips'
make[5]: 'buildconfig' is up to date.
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/exim-ldap/exim-4.94.2/build-Linux-mips'
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
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/exim-ldap/exim-4.94.2/build-Linux-mips'
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/exim-ldap/exim-4.94.2'
/bin/sh scripts/source_checks
`Makefile' is up to date.
 
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/exim-ldap/exim-4.94.2/build-Linux-mips'
/bin/sh ../scripts/Configure-os.c
./macro_predef > macro.c
ccache_cc exim_dbmbuild.c
In file included from hash.h:14,
                 from exim.h:530,
                 from exim_dbmbuild.c:32:
sha_ver.h:38:12: fatal error: openssl/ssl.h: No such file or directory
 #  include <openssl/ssl.h>
            ^~~~~~~~~~~~~~~
compilation terminated.
make[5]: *** [Makefile:861: exim_dbmbuild.o] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/exim-ldap/exim-4.94.2/build-Linux-mips'
make[4]: *** [Makefile:35: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/exim-ldap/exim-4.94.2'
make[3]: *** [Makefile:288: /openwrt/build_dir/target-mips_24kc_musl/exim-ldap/exim-4.94.2/.built] Error 2
```
