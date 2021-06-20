---
title: "compile.37"
date: 2021-06-20 22:27:32.440997
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
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force 
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
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
configure.ac:26: warning: AC_INIT: not a literal: $Id$
configure.ac:2351: warning: AC_CONFIG_SUBDIRS: you should use literals
../../lib/autoconf/status.m4:1097: AC_CONFIG_SUBDIRS is expanded from...
configure.ac:2351: the top level
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
configure.ac:26: warning: AC_INIT: not a literal: $Id$
configure.ac:2351: warning: AC_CONFIG_SUBDIRS: you should use literals
../../lib/autoconf/status.m4:1097: AC_CONFIG_SUBDIRS is expanded from...
configure.ac:2351: the top level
autoreconf: configure.ac: not using Automake
autoreconf: Leaving directory `.'
configure: loading site script /openwrt/include/site/mips
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking target system type... mips-openwrt-linux-gnu
checking for mips-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... no
configure: error: in `/openwrt/build_dir/target-mips_24kc_musl/freeradius-server-release_3_0_21':
configure: error: C compiler cannot create executables
See `config.log' for more details
make[3]: *** [Makefile:770: /openwrt/build_dir/target-mips_24kc_musl/freeradius-server-release_3_0_21/.configured_059ce960b95c68443337f43a915dbd53] Error 77
```
