---
title: "compile.37"
date: 2021-06-20 22:33:34.437672
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
make package/feeds/packages/rtorrent/compile -j$(nproc) || make package/feeds/packages/rtorrent/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/120-fix-ncurses.patch using plaintext: 
patching file src/display/canvas.h

Applying ./patches/130-usleep.patch using plaintext: 
patching file src/thread_base.cc
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force -I scripts
autoreconf: configure.ac: tracing
autoreconf: running: /openwrt/staging_dir/host/bin/libtoolize --install --force
OpenWrt-libtoolize: putting auxiliary files in `.'.
OpenWrt-libtoolize: linking file `./config.guess'
OpenWrt-libtoolize: linking file `./config.sub'
OpenWrt-libtoolize: linking file `./install-sh'
OpenWrt-libtoolize: linking file `./ltmain.sh'
OpenWrt-libtoolize: putting macros in `scripts'.
OpenWrt-libtoolize: linking file `scripts/libtool.m4'
OpenWrt-libtoolize: linking file `scripts/ltoptions.m4'
OpenWrt-libtoolize: linking file `scripts/ltsugar.m4'
OpenWrt-libtoolize: linking file `scripts/ltversion.m4'
OpenWrt-libtoolize: linking file `scripts/lt~obsolete.m4'
OpenWrt-libtoolize: Consider adding `AC_CONFIG_MACRO_DIR([m4])' to configure.ac and
OpenWrt-libtoolize: rerunning libtoolize, to keep the correct libtool macros in-tree.
OpenWrt-libtoolize: `AC_PROG_RANLIB' is rendered obsolete by `LT_INIT'
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
configure.ac:10: installing './compile'
configure.ac:5: installing './missing'
src/Makefile.am: installing './depcomp'
parallel-tests: installing './test-driver'
autoreconf: Leaving directory `.'
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/mips
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking for mips-openwrt-linux-ranlib... mips-openwrt-linux-musl-gcc-ranlib
checking whether the C++ compiler works... no
configure: error: in `/openwrt/build_dir/target-mips_24kc_musl/rtorrent-norpc/rtorrent-0.9.8':
configure: error: C++ compiler cannot create executables
See `config.log' for more details
make[3]: *** [Makefile:93: /openwrt/build_dir/target-mips_24kc_musl/rtorrent-norpc/rtorrent-0.9.8/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 77
```
