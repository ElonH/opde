---
title: "compile.40"
date: 2021-06-22 10:49:10.773260
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
make package/feeds/packages/shairport-sync/compile -j$(nproc) || make package/feeds/packages/shairport-sync/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-no-cxx.patch using plaintext: 
patching file Makefile.am
patching file configure.ac
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force 
autoreconf: configure.ac: tracing
autoreconf: configure.ac: not using Libtool
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
configure.ac:25: installing './compile'
configure.ac:6: installing './install-sh'
configure.ac:6: installing './missing'
Makefile.am: installing './INSTALL'
Makefile.am: installing './depcomp'
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
checking for mips-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... no
checking for ccache_cc option to accept ISO C89... none needed
checking whether ccache_cc understands -c and -o together... yes
checking for style of include used by make... GNU
checking dependency style of ccache_cc... gcc3
checking pkg-config is at least version 0.9.0... yes
checking for clock_gettime in -lrt... yes
checking for pthread_create in -lpthread... yes
checking for exp in -lm... yes
checking for popt... yes
checking for libconfig... yes
checking for alac... yes
checking for DAEMON... yes
checking for mbedtls_ssl_init in -lmbedtls... yes
checking for mbedtls_entropy_func in -lmbedcrypto... yes
checking for mbedtls_pk_init in -lmbedx509... yes
checking for soxr... yes
checking for avahi_client_new in -lavahi-client... yes
checking for avahi_strerror in -lavahi-common... yes
checking for alsa... yes
checking for xmltoman... no
configure: WARNING: xmltoman not found - not rebuilding man pages
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
checking getopt_long.h usability... no
checking getopt_long.h presence... no
checking for getopt_long.h... no
checking arpa/inet.h usability... yes
checking arpa/inet.h presence... yes
checking for arpa/inet.h... yes
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking limits.h usability... yes
checking limits.h presence... yes
checking for limits.h... yes
checking mach/mach.h usability... no
checking mach/mach.h presence... no
checking for mach/mach.h... no
checking for memory.h... (cached) yes
checking netdb.h usability... yes
checking netdb.h presence... yes
checking for netdb.h... yes
checking netinet/in.h usability... yes
checking netinet/in.h presence... yes
checking for netinet/in.h... yes
checking for stdint.h... (cached) yes
checking for stdlib.h... (cached) yes
checking for string.h... (cached) yes
checking sys/ioctl.h usability... yes
checking sys/ioctl.h presence... yes
checking for sys/ioctl.h... yes
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking sys/time.h usability... yes
checking sys/time.h presence... yes
checking for sys/time.h... yes
checking syslog.h usability... yes
checking syslog.h presence... yes
checking for syslog.h... yes
checking for unistd.h... (cached) yes
checking for inline... inline
checking for int16_t... yes
checking for int32_t... yes
checking for int64_t... yes
checking for pid_t... yes
checking for size_t... yes
checking for ssize_t... yes
checking for uint16_t... yes
checking for uint32_t... yes
checking for uint64_t... yes
checking for uint8_t... yes
checking for working alloca.h... yes
checking for alloca... yes
checking for error_at_line... no
checking vfork.h usability... no
checking vfork.h presence... no
checking for vfork.h... no
checking for fork... yes
checking for vfork... yes
checking for working fork... cross
configure: WARNING: result yes guessed because of cross compilation
checking for working vfork... (cached) yes
checking for atexit... yes
checking for clock_gettime... yes
checking for gethostname... yes
checking for inet_ntoa... yes
checking for memchr... yes
checking for memmove... yes
checking for memset... yes
checking for mkfifo... yes
checking for pow... yes
checking for select... yes
checking for socket... yes
checking for stpcpy... yes
checking for strcasecmp... yes
checking for strchr... yes
checking for strdup... yes
checking for strerror... (cached) yes
checking for strstr... yes
checking for strtol... yes
checking for strtoul... yes
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating Makefile
config.status: creating man/Makefile
config.status: creating scripts/shairport-sync.service
config.status: creating scripts/shairport-sync
config.status: creating config.h
config.status: executing depfiles commands
configure: WARNING: unrecognized options: --disable-nls
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/shairport-sync-mbedtls/shairport-sync-3.3.8'
make  all-recursive
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/shairport-sync-mbedtls/shairport-sync-3.3.8'
Making all in man
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/shairport-sync-mbedtls/shairport-sync-3.3.8/man'
make[6]: Nothing to be done for 'all'.
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/shairport-sync-mbedtls/shairport-sync-3.3.8/man'
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/shairport-sync-mbedtls/shairport-sync-3.3.8'
depbase=`echo shairport.o | sed 's|[^/]*$|.deps/&|;s|\.o$||'`;\
ccache_cc -DHAVE_CONFIG_H -I.   -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fno-common -Wno-multichar -Wall -Wextra -Wno-clobbered -Wno-psabi -pthread -DSYSCONFDIR=\"/etc\"  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/shairport-sync-mbedtls/shairport-sync-3.3.8=shairport-sync-3.3.8 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -MT shairport.o -MD -MP -MF $depbase.Tpo -c -o shairport.o shairport.c &&\
mv -f $depbase.Tpo $depbase.Po
depbase=`echo rtsp.o | sed 's|[^/]*$|.deps/&|;s|\.o$||'`;\
ccache_cc -DHAVE_CONFIG_H -I.   -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fno-common -Wno-multichar -Wall -Wextra -Wno-clobbered -Wno-psabi -pthread -DSYSCONFDIR=\"/etc\"  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/shairport-sync-mbedtls/shairport-sync-3.3.8=shairport-sync-3.3.8 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -MT rtsp.o -MD -MP -MF $depbase.Tpo -c -o rtsp.o rtsp.c &&\
mv -f $depbase.Tpo $depbase.Po
rtsp.c: In function 'metadata_init':
rtsp.c:1655:7: warning: unused variable 'ret' [-Wunused-variable]
   int ret;
       ^~~
rtsp.c: In function 'send_metadata':
rtsp.c:1816:10: warning: 'rc' may be used uninitialized in this function [-Wmaybe-uninitialized]
   return rc;
          ^~
depbase=`echo mdns.o | sed 's|[^/]*$|.deps/&|;s|\.o$||'`;\
ccache_cc -DHAVE_CONFIG_H -I.   -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fno-common -Wno-multichar -Wall -Wextra -Wno-clobbered -Wno-psabi -pthread -DSYSCONFDIR=\"/etc\"  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/shairport-sync-mbedtls/shairport-sync-3.3.8=shairport-sync-3.3.8 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -MT mdns.o -MD -MP -MF $depbase.Tpo -c -o mdns.o mdns.c &&\
mv -f $depbase.Tpo $depbase.Po
depbase=`echo common.o | sed 's|[^/]*$|.deps/&|;s|\.o$||'`;\
ccache_cc -DHAVE_CONFIG_H -I.   -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fno-common -Wno-multichar -Wall -Wextra -Wno-clobbered -Wno-psabi -pthread -DSYSCONFDIR=\"/etc\"  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/shairport-sync-mbedtls/shairport-sync-3.3.8=shairport-sync-3.3.8 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -MT common.o -MD -MP -MF $depbase.Tpo -c -o common.o common.c &&\
mv -f $depbase.Tpo $depbase.Po
depbase=`echo rtp.o | sed 's|[^/]*$|.deps/&|;s|\.o$||'`;\
ccache_cc -DHAVE_CONFIG_H -I.   -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fno-common -Wno-multichar -Wall -Wextra -Wno-clobbered -Wno-psabi -pthread -DSYSCONFDIR=\"/etc\"  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/shairport-sync-mbedtls/shairport-sync-3.3.8=shairport-sync-3.3.8 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -MT rtp.o -MD -MP -MF $depbase.Tpo -c -o rtp.o rtp.c &&\
mv -f $depbase.Tpo $depbase.Po
depbase=`echo player.o | sed 's|[^/]*$|.deps/&|;s|\.o$||'`;\
ccache_cc -DHAVE_CONFIG_H -I.   -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fno-common -Wno-multichar -Wall -Wextra -Wno-clobbered -Wno-psabi -pthread -DSYSCONFDIR=\"/etc\"  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/shairport-sync-mbedtls/shairport-sync-3.3.8=shairport-sync-3.3.8 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -MT player.o -MD -MP -MF $depbase.Tpo -c -o player.o player.c &&\
mv -f $depbase.Tpo $depbase.Po
depbase=`echo alac.o | sed 's|[^/]*$|.deps/&|;s|\.o$||'`;\
ccache_cc -DHAVE_CONFIG_H -I.   -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fno-common -Wno-multichar -Wall -Wextra -Wno-clobbered -Wno-psabi -pthread -DSYSCONFDIR=\"/etc\"  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/shairport-sync-mbedtls/shairport-sync-3.3.8=shairport-sync-3.3.8 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -MT alac.o -MD -MP -MF $depbase.Tpo -c -o alac.o alac.c &&\
mv -f $depbase.Tpo $depbase.Po
depbase=`echo audio.o | sed 's|[^/]*$|.deps/&|;s|\.o$||'`;\
ccache_cc -DHAVE_CONFIG_H -I.   -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fno-common -Wno-multichar -Wall -Wextra -Wno-clobbered -Wno-psabi -pthread -DSYSCONFDIR=\"/etc\"  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/shairport-sync-mbedtls/shairport-sync-3.3.8=shairport-sync-3.3.8 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -MT audio.o -MD -MP -MF $depbase.Tpo -c -o audio.o audio.c &&\
mv -f $depbase.Tpo $depbase.Po
depbase=`echo loudness.o | sed 's|[^/]*$|.deps/&|;s|\.o$||'`;\
ccache_cc -DHAVE_CONFIG_H -I.   -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fno-common -Wno-multichar -Wall -Wextra -Wno-clobbered -Wno-psabi -pthread -DSYSCONFDIR=\"/etc\"  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/shairport-sync-mbedtls/shairport-sync-3.3.8=shairport-sync-3.3.8 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -MT loudness.o -MD -MP -MF $depbase.Tpo -c -o loudness.o loudness.c &&\
mv -f $depbase.Tpo $depbase.Po
depbase=`echo activity_monitor.o | sed 's|[^/]*$|.deps/&|;s|\.o$||'`;\
ccache_cc -DHAVE_CONFIG_H -I.   -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fno-common -Wno-multichar -Wall -Wextra -Wno-clobbered -Wno-psabi -pthread -DSYSCONFDIR=\"/etc\"  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/shairport-sync-mbedtls/shairport-sync-3.3.8=shairport-sync-3.3.8 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -MT activity_monitor.o -MD -MP -MF $depbase.Tpo -c -o activity_monitor.o activity_monitor.c &&\
mv -f $depbase.Tpo $depbase.Po
depbase=`echo mdns_avahi.o | sed 's|[^/]*$|.deps/&|;s|\.o$||'`;\
ccache_cc -DHAVE_CONFIG_H -I.   -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fno-common -Wno-multichar -Wall -Wextra -Wno-clobbered -Wno-psabi -pthread -DSYSCONFDIR=\"/etc\"  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/shairport-sync-mbedtls/shairport-sync-3.3.8=shairport-sync-3.3.8 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -MT mdns_avahi.o -MD -MP -MF $depbase.Tpo -c -o mdns_avahi.o mdns_avahi.c &&\
mv -f $depbase.Tpo $depbase.Po
depbase=`echo audio_alsa.o | sed 's|[^/]*$|.deps/&|;s|\.o$||'`;\
ccache_cc -DHAVE_CONFIG_H -I.   -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fno-common -Wno-multichar -Wall -Wextra -Wno-clobbered -Wno-psabi -pthread -DSYSCONFDIR=\"/etc\"  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/shairport-sync-mbedtls/shairport-sync-3.3.8=shairport-sync-3.3.8 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -MT audio_alsa.o -MD -MP -MF $depbase.Tpo -c -o audio_alsa.o audio_alsa.c &&\
mv -f $depbase.Tpo $depbase.Po
ccache_cc -fno-common -Wno-multichar -Wall -Wextra -Wno-clobbered -Wno-psabi -pthread -DSYSCONFDIR=\"/etc\"  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/shairport-sync-mbedtls/shairport-sync-3.3.8=shairport-sync-3.3.8 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro   -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro  -o shairport-sync shairport.o rtsp.o mdns.o common.o rtp.o player.o alac.o audio.o loudness.o activity_monitor.o mdns_avahi.o   audio_alsa.o                 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lasound  -lavahi-common -lavahi-client -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lsoxr  -lmbedx509 -lmbedcrypto -lmbedtls -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -ldaemon  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lalac  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lconfig  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lpopt  -lm -lpthread -lrt 
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ld: player.o: in function `player_thread_cleanup_handler':
player.c:(.text+0x47e): undefined reference to `apple_alac_terminate'
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ld: player.o: in function `unencrypted_packet_decode':
player.c:(.text+0x794): undefined reference to `apple_alac_decode_frame'
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ld: player.o: in function `player_thread_func':
player.c:(.text+0x1ac8): undefined reference to `apple_alac_init'
collect2: error: ld returned 1 exit status
make[6]: *** [Makefile:651: shairport-sync] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/shairport-sync-mbedtls/shairport-sync-3.3.8'
make[5]: *** [Makefile:756: all-recursive] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/shairport-sync-mbedtls/shairport-sync-3.3.8'
make[4]: *** [Makefile:522: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/shairport-sync-mbedtls/shairport-sync-3.3.8'
make[3]: *** [Makefile:125: /openwrt/build_dir/target-mips_24kc_musl/shairport-sync-mbedtls/shairport-sync-3.3.8/.built] Error 2
```
