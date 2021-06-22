---
title: "compile.40"
date: 2021-06-22 10:47:21.979859
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
make package/feeds/packages/apache/compile -j$(nproc) || make package/feeds/packages/apache/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-cross-compile.patch using plaintext: 
patching file server/Makefile.in
patching file configure.in
patching file acinclude.m4

Applying ./patches/004-fix-scoreboard-location.patch using plaintext: 
patching file include/scoreboard.h

Applying ./patches/005-httpd_conf.patch using plaintext: 
patching file docs/conf/httpd.conf.in

Applying ./patches/010-reproducible-builds.patch using plaintext: 
patching file server/buildmark.c
patching file server/Makefile.in

Applying ./patches/020-openssl-deprecated.patch using plaintext: 
patching file modules/md/md_crypt.c
patching file modules/ssl/ssl_engine_init.c
patching file modules/ssl/ssl_engine_io.c
patching file modules/ssl/ssl_engine_log.c
patching file modules/ssl/ssl_engine_vars.c
patching file modules/ssl/ssl_private.h
patching file support/ab.c
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
configure: loading site script /openwrt/include/site/mips
checking for chosen layout... OpenWrt
checking for working mkdir -p... yes
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking target system type... mips-openwrt-linux-gnu
configure: 
configure: Configuring Apache Portable Runtime library...
configure: 
checking for APR... yes
  setting CPP to "ccache_cc -E"
  adding "-DLINUX" to CPPFLAGS
  adding "-D_REENTRANT" to CPPFLAGS
  adding "-D_GNU_SOURCE" to CPPFLAGS
configure: 
configure: Configuring Apache Portable Runtime Utility library...
configure: 
checking for APR-util... configure: error: the --with-apr-util parameter is incorrect. It must specify an install prefix, a build directory, or an apu-config file.
make[3]: *** [Makefile:366: /openwrt/build_dir/target-mips_24kc_musl/httpd-2.4.46/.configured_48a111b792c849fbed7c628e57c118fa] Error 1
```
