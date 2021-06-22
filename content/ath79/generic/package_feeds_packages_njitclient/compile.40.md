---
title: "compile.40"
date: 2021-06-22 10:50:44.057212
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
make package/feeds/packages/njitclient/compile -j$(nproc) || make package/feeds/packages/njitclient/compile V=s
```

#### Compile.txt

``` bash
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force 
autoreconf: configure.ac: tracing
autoreconf: configure.ac: adding subdirectory src to autoreconf
autoreconf: Entering directory `src'
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force -I m4
autoreconf: configure.ac: not using Libtool
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
configure.ac:12: installing './compile'
configure.ac:10: installing './install-sh'
configure.ac:10: installing './missing'
Makefile.am: installing './depcomp'
autoreconf: Leaving directory `src'
autoreconf: configure.ac: not using Autoheader
configure.ac:3: installing './install-sh'
configure.ac:3: installing './missing'
autoreconf: Leaving directory `.'
configure: loading site script /openwrt/include/site/mips
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating Makefile
=== configuring in src (/openwrt/build_dir/target-mips_24kc_musl/njit8021xclient-2.0-2018-11-24-dd28c17f/src)
configure: running /bin/bash ./configure --disable-option-checking '--prefix=/usr'  '--target=mips-openwrt-linux' '--host=mips-openwrt-linux' '--build=x86_64-pc-linux-gnu' '--program-prefix=' '--program-suffix=' '--exec-prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--libexecdir=/usr/lib' '--sysconfdir=/etc' '--datadir=/usr/share' '--localstatedir=/var' '--mandir=/usr/man' '--infodir=/usr/info' '--disable-nls' 'build_alias=x86_64-pc-linux-gnu' 'host_alias=mips-openwrt-linux' 'target_alias=mips-openwrt-linux' --cache-file=/dev/null --srcdir=.
configure: loading site script /openwrt/include/site/mips
checking program prefix for njit8021xclient... njit-
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
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
checking whether ccache_cc understands -c and -o together... yes
checking for style of include used by make... GNU
checking dependency style of ccache_cc... gcc3
checking gcc version... 8
checking for inline... inline
checking for library containing gethostbyname... none required
checking for library containing socket... none required
checking for library containing putmsg... no
checking for local pcap library... not found
checking for mips-openwrt-linux-pcap-config... no
checking for pcap-config... /openwrt/staging_dir/target-mips_24kc_musl/host/bin/pcap-config
configure: WARNING: using cross tools not prefixed with host triplet
checking for pcap_loop... yes
checking for pcap_list_datalinks... yes
checking for pcap_set_datalink... yes
checking for pcap_datalink_name_to_val... yes
checking for pcap_datalink_val_to_description... yes
checking for pcap_breakloop... yes
checking for pcap_dump_ftell... yes
checking pkg-config is at least version 0.9.0... yes
checking for libcrypto... no
configure: error: Package requirements (libcrypto) were not met:

Package 'libcrypto', required by 'virtual:world', not found

Consider adjusting the PKG_CONFIG_PATH environment variable if you
installed software in a non-standard prefix.

Alternatively, you may set the environment variables libcrypto_CFLAGS
and libcrypto_LIBS to avoid the need to call pkg-config.
See the pkg-config man page for more details.
configure: error: ./configure failed for src
make[3]: *** [Makefile:44: /openwrt/build_dir/target-mips_24kc_musl/njit8021xclient-2.0-2018-11-24-dd28c17f/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
