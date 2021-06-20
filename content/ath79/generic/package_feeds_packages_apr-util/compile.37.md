---
title: "compile.37"
date: 2021-06-20 22:33:34.428173
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
make package/feeds/packages/apr-util/compile -j$(nproc) || make package/feeds/packages/apr-util/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/002-fix-gdbm-error-handling.patch using plaintext: 
patching file dbm/apr_dbm_gdbm.c

Applying ./patches/003-support_mariadb.patch using plaintext: 
patching file build/dbd.m4
patching file dbd/apr_dbd_mysql.c

Applying ./patches/004-avoid_ldap_by_defaut.patch using plaintext: 
patching file apu-config.in

Applying ./patches/005-apu_config_dont_list_indep_libs.patch using plaintext: 
patching file apr-util.pc.in
patching file apu-config.in

Applying ./patches/006-avoid_db_by-default.patch using plaintext: 
patching file apu-config.in
autoreconf: Entering directory `.'
autoreconf: configure.in: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force 
aclocal.real: warning: autoconf input should be named 'configure.ac', not 'configure.in'
autoreconf: configure.in: tracing
autoreconf: configure.in: not using Libtool
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: configure.in: not using Automake
autoreconf: Leaving directory `.'
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/mips
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking target system type... mips-openwrt-linux-gnu
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking for working mkdir -p... yes
APR-util Version: 1.6.1
checking for chosen layout... apr-util
checking for mips-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
Applying apr-util hints file rules for mips-openwrt-linux-gnu
checking for APR... yes
  setting CPP to "ccache_cc -E"
  adding "-DLINUX" to CPPFLAGS
  adding "-D_REENTRANT" to CPPFLAGS
  adding "-D_GNU_SOURCE" to CPPFLAGS
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
  adding "-I/openwrt/staging_dir/target-mips_24kc_musl/usr/include" to CPPFLAGS
  adding "-L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib" to LDFLAGS
configure: checking for openssl in /openwrt/staging_dir/target-mips_24kc_musl/usr
checking openssl/x509.h usability... no
checking openssl/x509.h presence... no
checking for openssl/x509.h... no
checking for EVP_CIPHER_CTX_new in -lcrypto... no
checking whether EVP_PKEY_CTX_new is declared... no
configure: error: Crypto was requested but no crypto library could be enabled; specify the location of a crypto library using --with-openssl, --with-nss, and/or --with-commoncrypto.
make[3]: *** [Makefile:167: /openwrt/build_dir/target-mips_24kc_musl/apr-util-1.6.1/.configured_62e76c8bb3ec02aa58ec7ed71fe96025] Error 1
```
