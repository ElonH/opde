---
title: "compile.42"
date: 2021-06-29 09:26:41.853000
hidden: false
draft: false
weight: -42
---

build number: `42`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/gmediarender/compile -j$(nproc) || make package/feeds/packages/gmediarender/compile V=s
```

#### Compile.txt

``` bash
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-aarch64_cortex-a72_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/aclocal -I m4 -I . --force 
autoreconf: configure.ac: tracing
autoreconf: configure.ac: creating directory config
autoreconf: configure.ac: not using Libtool
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
configure.ac:8: installing 'config/compile'
configure.ac:6: installing 'config/install-sh'
configure.ac:6: installing 'config/missing'
Makefile.am: installing './INSTALL'
src/Makefile.am: installing 'config/depcomp'
autoreconf: Leaving directory `.'
configure: WARNING: unrecognized options: --disable-nls, --with-build-cc
configure: loading site script /openwrt/include/site/aarch64
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for aarch64-openwrt-linux-strip... aarch64-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking for style of include used by make... GNU
checking for aarch64-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
checking whether ccache_cc understands -c and -o together... yes
checking dependency style of ccache_cc... gcc3
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking for aarch64-openwrt-linux-gcc... (cached) ccache_cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether ccache_cc accepts -g... (cached) yes
checking for ccache_cc option to accept ISO C89... (cached) none needed
checking whether ccache_cc understands -c and -o together... (cached) yes
checking dependency style of ccache_cc... (cached) gcc3
checking for ccache_cc option to accept ISO C99... none needed
checking for ccache_cc option to accept ISO Standard C... (cached) none needed
checking whether make sets $(MAKE)... (cached) yes
checking for asprintf... yes
checking for exp in -lm... yes
checking pkg-config is at least version 0.9.0... yes
checking for GLIB... no
checking for GST... no
checking for GST... no
checking for LIBUPNP... yes
checking how to run the C preprocessor... ccache_cc -E
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for ANSI C header files... yes
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating Makefile
config.status: creating src/Makefile
config.status: creating data/Makefile
config.status: creating config.h
config.status: executing depfiles commands
configure: WARNING: unrecognized options: --disable-nls, --with-build-cc
make[4]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gmediarender-0.0.8'
make  all-recursive
make[5]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gmediarender-0.0.8'
Making all in src
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gmediarender-0.0.8/src'
(echo "#define GM_COMPILE_VERSION \"0.0.8\"" > git-version.h-new; \
cmp -s git-version.h git-version.h-new || cp git-version.h-new git-version.h; \
rm git-version.h-new)
ccache_cc -DHAVE_CONFIG_H -I. -I..    -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include/upnp  -DPKG_DATADIR=\"/usr/share/gmediarender\" -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include   -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/gmediarender-0.0.8=gmediarender-0.0.8 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include -std=gnu99 -Wall -Wpointer-arith -Wmissing-prototypes -Wmissing-declarations -Wwrite-strings -MT upnp_service.o -MD -MP -MF .deps/upnp_service.Tpo -c -o upnp_service.o upnp_service.c
mv -f .deps/upnp_service.Tpo .deps/upnp_service.Po
ccache_cc -DHAVE_CONFIG_H -I. -I..    -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include/upnp  -DPKG_DATADIR=\"/usr/share/gmediarender\" -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include   -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/gmediarender-0.0.8=gmediarender-0.0.8 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include -std=gnu99 -Wall -Wpointer-arith -Wmissing-prototypes -Wmissing-declarations -Wwrite-strings -MT upnp_control.o -MD -MP -MF .deps/upnp_control.Tpo -c -o upnp_control.o upnp_control.c
In file included from upnp_control.c:44:
webserver.h:27:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
make[6]: *** [Makefile:392: upnp_control.o] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gmediarender-0.0.8/src'
make[5]: *** [Makefile:365: all-recursive] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gmediarender-0.0.8'
make[4]: *** [Makefile:306: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gmediarender-0.0.8'
make[3]: *** [Makefile:57: /openwrt/build_dir/target-aarch64_cortex-a72_musl/gmediarender-0.0.8/.built] Error 2
```
