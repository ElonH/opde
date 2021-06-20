---
title: "compile.37"
date: 2021-06-20 22:33:34.430591
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
make package/feeds/packages/subversion/compile -j$(nproc) || make package/feeds/packages/subversion/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/301-cross-compilation-macos.patch using plaintext: 
patching file build/ac-macros/macosx.m4
patching file Makefile.in
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I build/ac-macros -I . --force 
build/ac-macros/zlib.m4:26: warning: underquoted definition of SVN_LIB_Z
build/ac-macros/zlib.m4:26:   run info Automake 'Extending aclocal'
build/ac-macros/zlib.m4:26:   or see http://www.gnu.org/software/automake/manual/automake.html#Extending-aclocal
autoreconf: configure.ac: tracing
autoreconf: running: /openwrt/staging_dir/host/bin/libtoolize --install --force
OpenWrt-libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, `build'.
OpenWrt-libtoolize: linking file `build/config.guess'
OpenWrt-libtoolize: linking file `build/config.sub'
OpenWrt-libtoolize: linking file `build/install-sh'
OpenWrt-libtoolize: linking file `build/ltmain.sh'
OpenWrt-libtoolize: Remember to add `LT_INIT' to configure.ac.
OpenWrt-libtoolize: Consider adding `AC_CONFIG_MACRO_DIR([m4])' to configure.ac and
OpenWrt-libtoolize: rerunning libtoolize, to keep the correct libtool macros in-tree.
OpenWrt-libtoolize: Consider adding `-I m4' to ACLOCAL_AMFLAGS in Makefile.am.
build/ac-macros/zlib.m4:26: warning: underquoted definition of SVN_LIB_Z
build/ac-macros/zlib.m4:26:   run info Automake 'Extending aclocal'
build/ac-macros/zlib.m4:26:   or see http://www.gnu.org/software/automake/manual/automake.html#Extending-aclocal
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=build/ac-macros --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=build/ac-macros --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: configure.ac: not using Automake
autoreconf: Leaving directory `.'
configure: loading site script /openwrt/include/site/mips
configure: Configuring Subversion 1.14.1
configure: creating config.nice
checking for mips-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
checking if ccache_cc accepts -std=c90... yes
checking if ccache_cc accepts -w... yes
checking if ccache_cc accepts -Werror=unknown-warning-option... no
checking whether we are using the GNU C++ compiler... yes
checking whether ccache_cxx accepts -g... yes
checking if ccache_cxx accepts -std=c++11... yes
checking if ccache_cxx accepts -w... yes
checking if ccache_cxx accepts -Werror=unknown-warning-option... no
checking how to run the C preprocessor... ccache_cc -E
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking target system type... mips-openwrt-linux-gnu
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking whether ln -s works... yes
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
configure: Apache Portable Runtime (APR) library configuration
checking for APR... yes
checking APR version... 1.7.0
configure: Apache Portable Runtime Utility (APRUTIL) library configuration
checking for APR-util... no
configure: WARNING: APRUTIL not found
The Apache Portable Runtime Utility (APRUTIL) library cannot be found.
Install APRUTIL on this system and configure Subversion with the
 appropriate --with-apr-util option.

configure: error: no suitable APRUTIL found
make[3]: *** [Makefile:126: /openwrt/build_dir/target-mips_24kc_musl/subversion-1.14.1/.configured_a17fb5ef857664f03cd0ce37cc5ea591] Error 1
```
