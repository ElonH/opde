---
title: "compile.37"
date: 2021-06-20 22:36:26.380557
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
make package/feeds/packages/xmlrpc-c/compile -j$(nproc) || make package/feeds/packages/xmlrpc-c/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-nanosleep.patch using plaintext: 
patching file lib/libutil/sleep.c
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/mips
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking whether make sets $(MAKE)... yes
checking for working aclocal... found
checking for working autoconf... found
checking for working automake... found
checking for working autoheader... found
checking for working makeinfo... found
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking whether to build Wininet client XML transport module... no
checking for curl-config... no
configure: You don't appear to have Curl installed (no working curl-config in your command search path), so we will not build the Curl client XML transport
checking whether to build Curl client XML transport module... no
checking whether to build Libwww client XML transport module... no
checking for mips-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... no
checking for ccache_cc option to accept ISO C89... none needed
checking for main in -lncurses... yes
checking for main in -lreadline... yes
checking whether to build tools... no
checking whether to build Abyss server module... no
checking whether to build CGI server module... no
checking whether to build C++ wrappers and tools... no
checking for mips-openwrt-linux-gcc... (cached) ccache_cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether ccache_cc accepts -g... (cached) no
checking for ccache_cc option to accept ISO C89... (cached) none needed
checking for socket... yes
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
checking wchar.h usability... yes
checking wchar.h presence... yes
checking for wchar.h... yes
checking sys/filio.h usability... no
checking sys/filio.h presence... no
checking for sys/filio.h... no
checking sys/ioctl.h usability... yes
checking sys/ioctl.h presence... yes
checking for sys/ioctl.h... yes
checking sys/select.h usability... yes
checking sys/select.h presence... yes
checking for sys/select.h... yes
checking stdarg.h usability... yes
checking stdarg.h presence... yes
checking for stdarg.h... yes
checking for size_t... yes
checking whether va_list is an array... no
checking whether compiler has __attribute__... yes
checking for vsnprintf... (cached) yes
checking for wcsncmp... yes
checking for setgroups... yes
checking for asprintf... yes
checking for setenv... yes
checking for strtoll... yes
checking for strtoull... yes
checking for strtoq... no
checking for strtouq... no
checking for __strtoll... no
checking for __strtoull... no
checking for _strtoui64... no
checking for pselect... yes
checking for gettimeofday... (cached) yes
checking for localtime_r... yes
checking for gmtime_r... yes
checking for strcasecmp... yes
checking for stricmp... no
checking for _stricmp... no
checking whether to use Abyss pthread function... no
checking for OpenSSL library... no
configure: You don't appear to Openssl installed (no pkg-config file for it in your pkg-config search path), so we will not build the Abyss Openssl channel module
checking whether to build Abyss Openssl channel module... no
checking whether to build the libxml2 backend... no
checking for mips-openwrt-linux-ar... mips-openwrt-linux-musl-gcc-ar
checking for mips-openwrt-linux-ranlib... mips-openwrt-linux-musl-gcc-ranlib
configure: creating ./config.status
config.status: creating srcdir.mk
config.status: creating config.mk
config.status: creating xmlrpc_config.h
configure: WARNING: unrecognized options: --disable-nls
configure: ==>
configure: ==>We are not building any client XML transport (see earlier messages explaining why), therefore WE WILL NOT BUILD THE CLIENT LIBRARY.
configure: ==>
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07'
rm -f shell_config
Lots of echoes to 'shell_config' suppressed here ...
make -C include/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07//include/Makefile \
    all 
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include'
>xmlrpc-c/config.h
Lots of echoes to 'xmlrpc-c/config.h' suppressed here ...
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include'
rm -f xmlrpc-c-config
Echoes to 'xmlrpc-c-config' suppressed here ...
cat shell_config >>xmlrpc-c-config
cat xmlrpc-c-config.main >>xmlrpc-c-config
chmod a+rx xmlrpc-c-config
rm -f xmlrpc-c-config.test
Echoes to 'xmlrpc-c-config.test' suppressed here ...
cat shell_config >>xmlrpc-c-config.test
cat xmlrpc-c-config.test.main >>xmlrpc-c-config.test
chmod a+rx xmlrpc-c-config.test
make -C lib/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07//lib/Makefile \
    all 
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib'
make -C util/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/util/Makefile \
    all 
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/util'
cat /dev/null >depend.mk
ln -s /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 srcdir
ln -s /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 blddir
ccache_cc -c -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -Isrcdir/lib/util/include -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  casprintf.c
ccache_cc -c -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -Isrcdir/lib/util/include -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  cmdline_parser.c
ccache_cc -c -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -Isrcdir/lib/util/include -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  getoptx.c
ccache_cc -c -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -Isrcdir/lib/util/include -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  string_parser.c
ccache_cc -c -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -Isrcdir/lib/util/include -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  stripcaseeq.c
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/util'
make -C libutil/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil/Makefile \
    all 
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil'
cat /dev/null >depend.mk
ln -s /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 srcdir
ln -s /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 blddir
ccache_cc -c -o asprintf.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  asprintf.c
ccache_cc -c -o base64.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  base64.c
ccache_cc -c -o error.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  error.c
ccache_cc -c -o lock_platform.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  lock_platform.c
ccache_cc -c -o lock_pthread.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  lock_pthread.c
ccache_cc -c -o lock_none.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  lock_none.c
ccache_cc -c -o make_printable.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  make_printable.c
ccache_cc -c -o memblock.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  memblock.c
ccache_cc -c -o mempool.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  mempool.c
ccache_cc -c -o select.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  select.c
ccache_cc -c -o sleep.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  sleep.c
ccache_cc -c -o string_number.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  string_number.c
ccache_cc -c -o time.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  time.c
ccache_cc -c -o utf8.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  utf8.c
ccache_cc -c -o asprintf.osh -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC asprintf.c
ccache_cc -c -o base64.osh -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC base64.c
ccache_cc -c -o error.osh -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC error.c
ccache_cc -c -o lock_platform.osh -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC lock_platform.c
ccache_cc -c -o lock_pthread.osh -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC lock_pthread.c
ccache_cc -c -o lock_none.osh -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC lock_none.c
ccache_cc -c -o make_printable.osh -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC make_printable.c
ccache_cc -c -o memblock.osh -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC memblock.c
ccache_cc -c -o mempool.osh -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC mempool.c
ccache_cc -c -o select.osh -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC select.c
ccache_cc -c -o sleep.osh -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC sleep.c
ccache_cc -c -o string_number.osh -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC string_number.c
ccache_cc -c -o time.osh -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC time.c
ccache_cc -c -o utf8.osh -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include -Isrcdir/include -Isrcdir/lib/util/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC utf8.c
rm -f xmlrpc_util.pc
Echoes to 'xmlrpc_util.pc' suppressed here ...
rm -f libxmlrpc_util.a
mips-openwrt-linux-musl-gcc-ar cru libxmlrpc_util.a asprintf.o base64.o error.o lock_platform.o lock_pthread.o lock_none.o make_printable.o memblock.o mempool.o select.o sleep.o string_number.o time.o utf8.o
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
mips-openwrt-linux-musl-gcc-ranlib libxmlrpc_util.a
ccache_cc -pthread  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro  -shared -Wl,-soname,libxmlrpc_util.so.4  asprintf.osh base64.osh error.osh lock_platform.osh lock_pthread.osh lock_none.osh make_printable.osh memblock.osh mempool.osh select.osh sleep.osh string_number.osh time.osh utf8.osh   -o libxmlrpc_util.so.4.51  
rm -f libxmlrpc_util.so.4
ln -s libxmlrpc_util.so.4.51 libxmlrpc_util.so.4
rm -f libxmlrpc_util.so
ln -s libxmlrpc_util.so.4 libxmlrpc_util.so
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil'
make -C expat/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/Makefile \
    all 
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat'
make -C gennmtab/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/gennmtab/Makefile \
    all 
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/gennmtab'
cat /dev/null >depend.mk
make[7]: Nothing to be done for 'all'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/gennmtab'
rm -f xmlrpc_expat.pc
Echoes to 'xmlrpc_expat.pc' suppressed here ...
make -C xmltok/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok/Makefile \
    all 
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok'
cat /dev/null >depend.mk
ln -s /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 srcdir
ln -s /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 blddir
rm -f nametab.h
../gennmtab/gennmtab >nametab.h
ccache_cc -c -o xmlrole.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -DXML_BYTE_ORDER=0  -I. -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir/lib/util/include -Isrcdir/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  xmlrole.c
xmlrole.c: In function 'prolog0':
xmlrole.c:94:20: warning: this statement may fall through [-Wimplicit-fallthrough=]
     state->handler = prolog1;
     ~~~~~~~~~~~~~~~^~~~~~~~~
xmlrole.c:95:3: note: here
   case XML_TOK_BOM:
   ^~~~
ccache_cc -c -o xmltok.osh -I. -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir/lib/util/include -Isrcdir/include -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC -DXML_BYTE_ORDER=0  -I. -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir/lib/util/include -Isrcdir/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC xmltok.c
In file included from xmltok.c:246:
xmltok_impl.c: In function 'normal_isPublicId':
xmltok_impl.c:1470:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (!(BYTE_TO_ASCII(enc, ptr) & ~0x7f))
          ^
xmltok_impl.c:1472:5: note: here
     default:
     ^~~~~~~
xmltok_impl.c: In function 'normal_sameName':
xmltok_impl.c:1686:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (*ptr1++ != *ptr2++) \
          ^
xmltok_impl.c:1688:5: note: in expansion of macro 'LEAD_CASE'
     LEAD_CASE(4) LEAD_CASE(3) LEAD_CASE(2)
     ^~~~~~~~~
xmltok_impl.c:1685:5: note: here
     case BT_LEAD ## n: \
     ^~~~
xmltok_impl.c:1688:18: note: in expansion of macro 'LEAD_CASE'
     LEAD_CASE(4) LEAD_CASE(3) LEAD_CASE(2)
                  ^~~~~~~~~
xmltok_impl.c:1686:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (*ptr1++ != *ptr2++) \
          ^
xmltok_impl.c:1688:18: note: in expansion of macro 'LEAD_CASE'
     LEAD_CASE(4) LEAD_CASE(3) LEAD_CASE(2)
                  ^~~~~~~~~
xmltok_impl.c:1685:5: note: here
     case BT_LEAD ## n: \
     ^~~~
xmltok_impl.c:1688:31: note: in expansion of macro 'LEAD_CASE'
     LEAD_CASE(4) LEAD_CASE(3) LEAD_CASE(2)
                               ^~~~~~~~~
xmltok_impl.c: In function 'normal_scanRef':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:512:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:512:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:521:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:521:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'normal_scanPercent':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:964:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:964:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:974:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:974:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'normal_scanLt':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:697:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:697:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:732:7: note: in expansion of macro 'CHECK_NMSTRT_CASES'
       CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
       ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:732:7: note: in expansion of macro 'CHECK_NMSTRT_CASES'
       CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
       ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:743:4: note: in expansion of macro 'CHECK_NMSTRT_CASES'
    CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
    ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:743:4: note: in expansion of macro 'CHECK_NMSTRT_CASES'
    CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
    ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:721:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:721:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'normal_scanPi':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:242:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:242:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:249:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:249:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'normal_scanEndTag':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:402:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:402:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:409:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:409:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'normal_scanAtts':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:553:7: note: in expansion of macro 'CHECK_NMSTRT_CASES'
       CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
       ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:553:7: note: in expansion of macro 'CHECK_NMSTRT_CASES'
       CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
       ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:653:4: note: in expansion of macro 'CHECK_NMSTRT_CASES'
    CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
    ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:653:4: note: in expansion of macro 'CHECK_NMSTRT_CASES'
    CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
    ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:542:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:542:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'normal_prologTok':
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:1229:2: note: in expansion of macro 'CHECK_NAME_CASES'
  CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
  ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:1229:2: note: in expansion of macro 'CHECK_NAME_CASES'
  CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
  ^~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:1215:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:1215:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'normal_scanPoundName':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:993:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:993:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:1000:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:1000:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
In file included from xmltok.c:775:
xmltok_impl.c: In function 'big2_isPublicId':
xmltok_impl.c:1470:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (!(BYTE_TO_ASCII(enc, ptr) & ~0x7f))
          ^
xmltok_impl.c:1472:5: note: here
     default:
     ^~~~~~~
xmltok_impl.c: In function 'big2_sameName':
xmltok_impl.c:1686:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (*ptr1++ != *ptr2++) \
          ^
xmltok_impl.c:1688:5: note: in expansion of macro 'LEAD_CASE'
     LEAD_CASE(4) LEAD_CASE(3) LEAD_CASE(2)
     ^~~~~~~~~
xmltok_impl.c:1685:5: note: here
     case BT_LEAD ## n: \
     ^~~~
xmltok_impl.c:1688:18: note: in expansion of macro 'LEAD_CASE'
     LEAD_CASE(4) LEAD_CASE(3) LEAD_CASE(2)
                  ^~~~~~~~~
xmltok_impl.c:1686:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (*ptr1++ != *ptr2++) \
          ^
xmltok_impl.c:1688:18: note: in expansion of macro 'LEAD_CASE'
     LEAD_CASE(4) LEAD_CASE(3) LEAD_CASE(2)
                  ^~~~~~~~~
xmltok_impl.c:1685:5: note: here
     case BT_LEAD ## n: \
     ^~~~
xmltok_impl.c:1688:31: note: in expansion of macro 'LEAD_CASE'
     LEAD_CASE(4) LEAD_CASE(3) LEAD_CASE(2)
                               ^~~~~~~~~
xmltok_impl.c: In function 'big2_scanRef':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:512:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:512:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:521:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:521:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'big2_scanPercent':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:964:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:964:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:974:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:974:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'big2_scanLt':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:697:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:697:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:732:7: note: in expansion of macro 'CHECK_NMSTRT_CASES'
       CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
       ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:732:7: note: in expansion of macro 'CHECK_NMSTRT_CASES'
       CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
       ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:743:4: note: in expansion of macro 'CHECK_NMSTRT_CASES'
    CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
    ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:743:4: note: in expansion of macro 'CHECK_NMSTRT_CASES'
    CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
    ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:721:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:721:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'big2_scanPi':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:242:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:242:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:249:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:249:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'big2_scanEndTag':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:402:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:402:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:409:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:409:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'big2_scanAtts':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:553:7: note: in expansion of macro 'CHECK_NMSTRT_CASES'
       CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
       ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:553:7: note: in expansion of macro 'CHECK_NMSTRT_CASES'
       CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
       ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:653:4: note: in expansion of macro 'CHECK_NMSTRT_CASES'
    CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
    ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:653:4: note: in expansion of macro 'CHECK_NMSTRT_CASES'
    CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
    ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:542:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:542:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'big2_prologTok':
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:1229:2: note: in expansion of macro 'CHECK_NAME_CASES'
  CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
  ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:1229:2: note: in expansion of macro 'CHECK_NAME_CASES'
  CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
  ^~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:1215:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:1215:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'big2_scanPoundName':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:993:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:993:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:1000:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:1000:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
In file included from xmltok.c:644:
xmltok_impl.c: In function 'little2_isPublicId':
xmltok_impl.c:1470:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (!(BYTE_TO_ASCII(enc, ptr) & ~0x7f))
          ^
xmltok_impl.c:1472:5: note: here
     default:
     ^~~~~~~
xmltok_impl.c: In function 'little2_sameName':
xmltok_impl.c:1686:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (*ptr1++ != *ptr2++) \
          ^
xmltok_impl.c:1688:5: note: in expansion of macro 'LEAD_CASE'
     LEAD_CASE(4) LEAD_CASE(3) LEAD_CASE(2)
     ^~~~~~~~~
xmltok_impl.c:1685:5: note: here
     case BT_LEAD ## n: \
     ^~~~
xmltok_impl.c:1688:18: note: in expansion of macro 'LEAD_CASE'
     LEAD_CASE(4) LEAD_CASE(3) LEAD_CASE(2)
                  ^~~~~~~~~
xmltok_impl.c:1686:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (*ptr1++ != *ptr2++) \
          ^
xmltok_impl.c:1688:18: note: in expansion of macro 'LEAD_CASE'
     LEAD_CASE(4) LEAD_CASE(3) LEAD_CASE(2)
                  ^~~~~~~~~
xmltok_impl.c:1685:5: note: here
     case BT_LEAD ## n: \
     ^~~~
xmltok_impl.c:1688:31: note: in expansion of macro 'LEAD_CASE'
     LEAD_CASE(4) LEAD_CASE(3) LEAD_CASE(2)
                               ^~~~~~~~~
xmltok_impl.c: In function 'little2_scanRef':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:512:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:512:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:521:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:521:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'little2_scanPercent':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:964:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:964:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:974:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:974:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'little2_scanLt':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:697:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:697:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:732:7: note: in expansion of macro 'CHECK_NMSTRT_CASES'
       CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
       ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:732:7: note: in expansion of macro 'CHECK_NMSTRT_CASES'
       CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
       ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:743:4: note: in expansion of macro 'CHECK_NMSTRT_CASES'
    CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
    ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:743:4: note: in expansion of macro 'CHECK_NMSTRT_CASES'
    CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
    ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:721:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:721:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'little2_scanPi':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:242:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:242:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:249:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:249:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'little2_scanEndTag':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:402:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:402:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:409:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:409:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'little2_scanAtts':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:553:7: note: in expansion of macro 'CHECK_NMSTRT_CASES'
       CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
       ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:553:7: note: in expansion of macro 'CHECK_NMSTRT_CASES'
       CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
       ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:653:4: note: in expansion of macro 'CHECK_NMSTRT_CASES'
    CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
    ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:653:4: note: in expansion of macro 'CHECK_NMSTRT_CASES'
    CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
    ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:542:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:542:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'little2_prologTok':
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:1229:2: note: in expansion of macro 'CHECK_NAME_CASES'
  CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
  ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:1229:2: note: in expansion of macro 'CHECK_NAME_CASES'
  CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
  ^~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:1215:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:1215:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'little2_scanPoundName':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:993:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:993:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:1000:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:1000:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
ccache_cc -c -o xmlrole.osh -I. -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir/lib/util/include -Isrcdir/include -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC -DXML_BYTE_ORDER=0  -I. -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir/lib/util/include -Isrcdir/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC xmlrole.c
xmlrole.c: In function 'prolog0':
xmlrole.c:94:20: warning: this statement may fall through [-Wimplicit-fallthrough=]
     state->handler = prolog1;
     ~~~~~~~~~~~~~~~^~~~~~~~~
xmlrole.c:95:3: note: here
   case XML_TOK_BOM:
   ^~~~
ccache_cc -c -o xmltok.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -DXML_BYTE_ORDER=0  -I. -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir/lib/util/include -Isrcdir/include  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  xmltok.c
In file included from xmltok.c:246:
xmltok_impl.c: In function 'normal_isPublicId':
xmltok_impl.c:1470:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (!(BYTE_TO_ASCII(enc, ptr) & ~0x7f))
          ^
xmltok_impl.c:1472:5: note: here
     default:
     ^~~~~~~
xmltok_impl.c: In function 'normal_sameName':
xmltok_impl.c:1686:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (*ptr1++ != *ptr2++) \
          ^
xmltok_impl.c:1688:5: note: in expansion of macro 'LEAD_CASE'
     LEAD_CASE(4) LEAD_CASE(3) LEAD_CASE(2)
     ^~~~~~~~~
xmltok_impl.c:1685:5: note: here
     case BT_LEAD ## n: \
     ^~~~
xmltok_impl.c:1688:18: note: in expansion of macro 'LEAD_CASE'
     LEAD_CASE(4) LEAD_CASE(3) LEAD_CASE(2)
                  ^~~~~~~~~
xmltok_impl.c:1686:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (*ptr1++ != *ptr2++) \
          ^
xmltok_impl.c:1688:18: note: in expansion of macro 'LEAD_CASE'
     LEAD_CASE(4) LEAD_CASE(3) LEAD_CASE(2)
                  ^~~~~~~~~
xmltok_impl.c:1685:5: note: here
     case BT_LEAD ## n: \
     ^~~~
xmltok_impl.c:1688:31: note: in expansion of macro 'LEAD_CASE'
     LEAD_CASE(4) LEAD_CASE(3) LEAD_CASE(2)
                               ^~~~~~~~~
xmltok_impl.c: In function 'normal_scanRef':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:512:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:512:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:521:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:521:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'normal_scanPercent':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:964:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:964:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:974:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:974:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'normal_scanLt':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:697:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:697:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:732:7: note: in expansion of macro 'CHECK_NMSTRT_CASES'
       CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
       ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:732:7: note: in expansion of macro 'CHECK_NMSTRT_CASES'
       CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
       ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:743:4: note: in expansion of macro 'CHECK_NMSTRT_CASES'
    CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
    ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:743:4: note: in expansion of macro 'CHECK_NMSTRT_CASES'
    CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
    ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:721:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:721:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'normal_scanPi':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:242:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:242:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:249:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:249:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'normal_scanEndTag':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:402:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:402:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:409:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:409:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'normal_scanAtts':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:553:7: note: in expansion of macro 'CHECK_NMSTRT_CASES'
       CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
       ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:553:7: note: in expansion of macro 'CHECK_NMSTRT_CASES'
       CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
       ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:653:4: note: in expansion of macro 'CHECK_NMSTRT_CASES'
    CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
    ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:653:4: note: in expansion of macro 'CHECK_NMSTRT_CASES'
    CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
    ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:542:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:542:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'normal_prologTok':
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:1229:2: note: in expansion of macro 'CHECK_NAME_CASES'
  CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
  ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:1229:2: note: in expansion of macro 'CHECK_NAME_CASES'
  CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
  ^~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:1215:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:1215:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'normal_scanPoundName':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:993:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:993:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:1000:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:1000:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
In file included from xmltok.c:775:
xmltok_impl.c: In function 'big2_isPublicId':
xmltok_impl.c:1470:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (!(BYTE_TO_ASCII(enc, ptr) & ~0x7f))
          ^
xmltok_impl.c:1472:5: note: here
     default:
     ^~~~~~~
xmltok_impl.c: In function 'big2_sameName':
xmltok_impl.c:1686:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (*ptr1++ != *ptr2++) \
          ^
xmltok_impl.c:1688:5: note: in expansion of macro 'LEAD_CASE'
     LEAD_CASE(4) LEAD_CASE(3) LEAD_CASE(2)
     ^~~~~~~~~
xmltok_impl.c:1685:5: note: here
     case BT_LEAD ## n: \
     ^~~~
xmltok_impl.c:1688:18: note: in expansion of macro 'LEAD_CASE'
     LEAD_CASE(4) LEAD_CASE(3) LEAD_CASE(2)
                  ^~~~~~~~~
xmltok_impl.c:1686:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (*ptr1++ != *ptr2++) \
          ^
xmltok_impl.c:1688:18: note: in expansion of macro 'LEAD_CASE'
     LEAD_CASE(4) LEAD_CASE(3) LEAD_CASE(2)
                  ^~~~~~~~~
xmltok_impl.c:1685:5: note: here
     case BT_LEAD ## n: \
     ^~~~
xmltok_impl.c:1688:31: note: in expansion of macro 'LEAD_CASE'
     LEAD_CASE(4) LEAD_CASE(3) LEAD_CASE(2)
                               ^~~~~~~~~
xmltok_impl.c: In function 'big2_scanRef':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:512:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:512:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:521:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:521:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'big2_scanPercent':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:964:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:964:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:974:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:974:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'big2_scanLt':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:697:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:697:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:732:7: note: in expansion of macro 'CHECK_NMSTRT_CASES'
       CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
       ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:732:7: note: in expansion of macro 'CHECK_NMSTRT_CASES'
       CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
       ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:743:4: note: in expansion of macro 'CHECK_NMSTRT_CASES'
    CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
    ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:743:4: note: in expansion of macro 'CHECK_NMSTRT_CASES'
    CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
    ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:721:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:721:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'big2_scanPi':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:242:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:242:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:249:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:249:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'big2_scanEndTag':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:402:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:402:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:409:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:409:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'big2_scanAtts':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:553:7: note: in expansion of macro 'CHECK_NMSTRT_CASES'
       CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
       ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:553:7: note: in expansion of macro 'CHECK_NMSTRT_CASES'
       CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
       ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:653:4: note: in expansion of macro 'CHECK_NMSTRT_CASES'
    CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
    ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:653:4: note: in expansion of macro 'CHECK_NMSTRT_CASES'
    CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
    ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:542:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:542:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'big2_prologTok':
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:1229:2: note: in expansion of macro 'CHECK_NAME_CASES'
  CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
  ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:1229:2: note: in expansion of macro 'CHECK_NAME_CASES'
  CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
  ^~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:1215:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:1215:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'big2_scanPoundName':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:993:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:993:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:1000:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:1000:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
In file included from xmltok.c:644:
xmltok_impl.c: In function 'little2_isPublicId':
xmltok_impl.c:1470:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (!(BYTE_TO_ASCII(enc, ptr) & ~0x7f))
          ^
xmltok_impl.c:1472:5: note: here
     default:
     ^~~~~~~
xmltok_impl.c: In function 'little2_sameName':
xmltok_impl.c:1686:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (*ptr1++ != *ptr2++) \
          ^
xmltok_impl.c:1688:5: note: in expansion of macro 'LEAD_CASE'
     LEAD_CASE(4) LEAD_CASE(3) LEAD_CASE(2)
     ^~~~~~~~~
xmltok_impl.c:1685:5: note: here
     case BT_LEAD ## n: \
     ^~~~
xmltok_impl.c:1688:18: note: in expansion of macro 'LEAD_CASE'
     LEAD_CASE(4) LEAD_CASE(3) LEAD_CASE(2)
                  ^~~~~~~~~
xmltok_impl.c:1686:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (*ptr1++ != *ptr2++) \
          ^
xmltok_impl.c:1688:18: note: in expansion of macro 'LEAD_CASE'
     LEAD_CASE(4) LEAD_CASE(3) LEAD_CASE(2)
                  ^~~~~~~~~
xmltok_impl.c:1685:5: note: here
     case BT_LEAD ## n: \
     ^~~~
xmltok_impl.c:1688:31: note: in expansion of macro 'LEAD_CASE'
     LEAD_CASE(4) LEAD_CASE(3) LEAD_CASE(2)
                               ^~~~~~~~~
xmltok_impl.c: In function 'little2_scanRef':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:512:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:512:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:521:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:521:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'little2_scanPercent':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:964:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:964:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:974:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:974:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'little2_scanLt':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:697:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:697:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:732:7: note: in expansion of macro 'CHECK_NMSTRT_CASES'
       CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
       ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:732:7: note: in expansion of macro 'CHECK_NMSTRT_CASES'
       CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
       ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:743:4: note: in expansion of macro 'CHECK_NMSTRT_CASES'
    CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
    ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:743:4: note: in expansion of macro 'CHECK_NMSTRT_CASES'
    CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
    ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:721:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:721:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'little2_scanPi':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:242:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:242:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:249:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:249:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'little2_scanEndTag':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:402:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:402:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:409:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:409:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'little2_scanAtts':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:553:7: note: in expansion of macro 'CHECK_NMSTRT_CASES'
       CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
       ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:553:7: note: in expansion of macro 'CHECK_NMSTRT_CASES'
       CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
       ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:653:4: note: in expansion of macro 'CHECK_NMSTRT_CASES'
    CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
    ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:653:4: note: in expansion of macro 'CHECK_NMSTRT_CASES'
    CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
    ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:542:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:542:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'little2_prologTok':
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:1229:2: note: in expansion of macro 'CHECK_NAME_CASES'
  CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
  ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:1229:2: note: in expansion of macro 'CHECK_NAME_CASES'
  CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
  ^~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:1215:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:1215:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c: In function 'little2_scanPoundName':
xmltok_impl.c:83:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NMSTRT_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:993:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:87:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:993:3: note: in expansion of macro 'CHECK_NMSTRT_CASES'
   CHECK_NMSTRT_CASES(enc, ptr, end, nextTokPtr)
   ^~~~~~~~~~~~~~~~~~
xmltok_impl.c:55:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!IS_NAME_CHAR_MINBPC(enc, ptr)) { \
        ^
xmltok_impl.c:1000:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
xmltok_impl.c:59:3: note: here
   case BT_NMSTRT: \
   ^~~~
xmltok_impl.c:1000:5: note: in expansion of macro 'CHECK_NAME_CASES'
     CHECK_NAME_CASES(enc, ptr, end, nextTokPtr)
     ^~~~~~~~~~~~~~~~
ccache_cc -pthread  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro  -shared -Wl,-soname,libxmlrpc_xmltok.so.3  xmltok.osh xmlrole.osh  -o libxmlrpc_xmltok.so.3.51  
rm -f libxmlrpc_xmltok.a
mips-openwrt-linux-musl-gcc-ar cru libxmlrpc_xmltok.a xmltok.o xmlrole.o
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
mips-openwrt-linux-musl-gcc-ranlib libxmlrpc_xmltok.a
rm -f libxmlrpc_xmltok.so.3
ln -s libxmlrpc_xmltok.so.3.51 libxmlrpc_xmltok.so.3
rm -f libxmlrpc_xmltok.so
ln -s libxmlrpc_xmltok.so.3 libxmlrpc_xmltok.so
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok'
make -C xmlparse/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmlparse/Makefile \
    all 
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmlparse'
cat /dev/null >depend.mk
ln -s /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 srcdir
ccache_cc -c -o xmlparse.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir/lib/expat/xmltok -Isrcdir/lib/util/include -Isrcdir/include   -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  xmlparse.c
xmlparse.c: In function 'doProlog':
xmlparse.c:3931:21: warning: this statement may fall through [-Wimplicit-fallthrough=]
         *errorCodeP = XML_ERROR_PARAM_ENTITY_REF;
         ~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~
xmlparse.c:3932:7: note: here
       case XML_TOK_XML_DECL:
       ^~~~
xmlparse.c:3933:21: warning: this statement may fall through [-Wimplicit-fallthrough=]
         *errorCodeP = XML_ERROR_MISPLACED_XML_PI;
         ~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~
xmlparse.c:3934:7: note: here
       default:
       ^~~~~~~
ccache_cc -c -o xmlparse.osh -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir/lib/expat/xmltok -Isrcdir/lib/util/include -Isrcdir/include  -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -I/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 -Isrcdir/lib/expat/xmltok -Isrcdir/lib/util/include -Isrcdir/include   -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC xmlparse.c
xmlparse.c: In function 'doProlog':
xmlparse.c:3931:21: warning: this statement may fall through [-Wimplicit-fallthrough=]
         *errorCodeP = XML_ERROR_PARAM_ENTITY_REF;
         ~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~
xmlparse.c:3932:7: note: here
       case XML_TOK_XML_DECL:
       ^~~~
xmlparse.c:3933:21: warning: this statement may fall through [-Wimplicit-fallthrough=]
         *errorCodeP = XML_ERROR_MISPLACED_XML_PI;
         ~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~
xmlparse.c:3934:7: note: here
       default:
       ^~~~~~~
make -C /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok/Makefile \
    libxmlrpc_xmltok.so
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok'
make[8]: 'libxmlrpc_xmltok.so' is up to date.
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok'
make -C /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil/Makefile \
    libxmlrpc_util.so
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil'
make[8]: 'libxmlrpc_util.so' is up to date.
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil'
rm -f libxmlrpc_xmlparse.a
mips-openwrt-linux-musl-gcc-ar cru libxmlrpc_xmlparse.a xmlparse.o
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
mips-openwrt-linux-musl-gcc-ranlib libxmlrpc_xmlparse.a
ccache_cc -pthread  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro  -shared -Wl,-soname,libxmlrpc_xmlparse.so.3  xmlparse.osh /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok/libxmlrpc_xmltok.so /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil/libxmlrpc_util.so /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok/libxmlrpc_xmltok.so /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil/libxmlrpc_util.so -o libxmlrpc_xmlparse.so.3.51  
rm -f libxmlrpc_xmlparse.so.3
ln -s libxmlrpc_xmlparse.so.3.51 libxmlrpc_xmlparse.so.3
rm -f libxmlrpc_xmlparse.so
ln -s libxmlrpc_xmlparse.so.3 libxmlrpc_xmlparse.so
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmlparse'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat'
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib'
make -C src/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07//src/Makefile \
    all 
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/src'
cat /dev/null >depend.mk
ln -s /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 srcdir
ln -s /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07 blddir
ccache_cc -c -o base_global.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  base_global.c
ccache_cc -c -o double.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  double.c
ccache_cc -c -o json.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  json.c
ccache_cc -c -o parse_datetime.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  parse_datetime.c
ccache_cc -c -o parse_value.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  parse_value.c
ccache_cc -c -o resource.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  resource.c
ccache_cc -c -o trace.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  trace.c
make -C /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/GNUmakefile version.h
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07'
rm -f version.h
echo "/* Generated by make file rule */" >>version.h
echo "#define XMLRPC_C_VERSION" \"1.51.7"\"" >>version.h
echo "#define XMLRPC_VERSION_MAJOR 1" >>version.h
echo "#define XMLRPC_VERSION_MINOR 51" >>version.h
echo "#define XMLRPC_VERSION_POINT 7" >>version.h
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07'
ccache_cc -c -o xmlrpc_data.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  xmlrpc_data.c
ccache_cc -c -o xmlrpc_datetime.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  xmlrpc_datetime.c
ccache_cc -c -o xmlrpc_string.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  xmlrpc_string.c
ccache_cc -c -o xmlrpc_array.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  xmlrpc_array.c
ccache_cc -c -o xmlrpc_struct.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  xmlrpc_struct.c
ccache_cc -c -o xmlrpc_build.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  xmlrpc_build.c
ccache_cc -c -o xmlrpc_decompose.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  xmlrpc_decompose.c
ccache_cc -c -o xmlrpc_expat.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  xmlrpc_expat.c
xmlrpc_expat.c: In function 'xml_init':
xmlrpc_expat.c:47:29: warning: unused parameter 'envP' [-Wunused-parameter]
 xml_init(xmlrpc_env * const envP) {
          ~~~~~~~~~~~~~~~~~~~^~~~
ccache_cc -c -o xmlrpc_parse.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  xmlrpc_parse.c
ccache_cc -c -o xmlrpc_serialize.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  xmlrpc_serialize.c
ccache_cc -c -o xmlrpc_authcookie.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  xmlrpc_authcookie.c
ccache_cc -c -o registry.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include   -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  registry.c
ccache_cc -c -o method.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include   -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  method.c
ccache_cc -c -o system_method.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include   -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  system_method.c
ccache_cc -c -o base_global.osh -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC base_global.c
ccache_cc -c -o double.osh -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC double.c
ccache_cc -c -o json.osh -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC json.c
ccache_cc -c -o parse_datetime.osh -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC parse_datetime.c
ccache_cc -c -o parse_value.osh -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC parse_value.c
ccache_cc -c -o resource.osh -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC resource.c
ccache_cc -c -o trace.osh -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC trace.c
ccache_cc -c -o version.osh -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC version.c
ccache_cc -c -o xmlrpc_data.osh -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC xmlrpc_data.c
ccache_cc -c -o xmlrpc_datetime.osh -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC xmlrpc_datetime.c
ccache_cc -c -o xmlrpc_string.osh -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC xmlrpc_string.c
ccache_cc -c -o xmlrpc_array.osh -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC xmlrpc_array.c
ccache_cc -c -o xmlrpc_struct.osh -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC xmlrpc_struct.c
ccache_cc -c -o xmlrpc_build.osh -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC xmlrpc_build.c
ccache_cc -c -o xmlrpc_decompose.osh -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC xmlrpc_decompose.c
ccache_cc -c -o xmlrpc_expat.osh -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC xmlrpc_expat.c
xmlrpc_expat.c: In function 'xml_init':
xmlrpc_expat.c:47:29: warning: unused parameter 'envP' [-Wunused-parameter]
 xml_init(xmlrpc_env * const envP) {
          ~~~~~~~~~~~~~~~~~~~^~~~
ccache_cc -c -o xmlrpc_parse.osh -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC xmlrpc_parse.c
ccache_cc -c -o xmlrpc_serialize.osh -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC xmlrpc_serialize.c
ccache_cc -c -o xmlrpc_authcookie.osh -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC xmlrpc_authcookie.c
make -C /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil/Makefile \
    libxmlrpc_util.so
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil'
make[6]: 'libxmlrpc_util.so' is up to date.
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil'
make -C /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmlparse/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmlparse/Makefile \
    libxmlrpc_xmlparse.so
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmlparse'
make -C /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok/Makefile \
    libxmlrpc_xmltok.so
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok'
make[7]: 'libxmlrpc_xmltok.so' is up to date.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok'
make -C /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil/Makefile \
    libxmlrpc_util.so
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil'
make[7]: 'libxmlrpc_util.so' is up to date.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmlparse'
make -C /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok/Makefile \
    libxmlrpc_xmltok.so
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok'
make[6]: 'libxmlrpc_xmltok.so' is up to date.
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok'
ccache_cc -c -o registry.osh -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include   -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC registry.c
ccache_cc -c -o method.osh -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include   -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC method.c
ccache_cc -c -o system_method.osh -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3 -fPIC   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include   -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC system_method.c
rm -f xmlrpc.pc
Echoes to 'xmlrpc.pc' suppressed here ...
rm -f xmlrpc_client.pc
Echoes to 'xmlrpc_client.pc' suppressed here ...
rm -f xmlrpc_server.pc
Echoes to 'xmlrpc_server.pc' suppressed here ...
rm -f xmlrpc_server_abyss.pc
Echoes to 'xmlrpc_server_abyss.pc' suppressed here ...
rm -f xmlrpc_server_cgi.pc
Echoes to 'xmlrpc_server_cgi.pc' suppressed here ...
ccache_cc -c -o version.o -DNDEBUG -pthread -Wall -W -Wno-uninitialized -Wundef -Wno-unknown-pragmas -Wmissing-declarations -Wstrict-prototypes -Wmissing-prototypes -Wimplicit -fno-common -g -O3   -Iblddir -Iblddir/include -Isrcdir/include -Isrcdir/lib/util/include  -Isrcdir/lib/expat/xmlparse  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07=xmlrpc-c-1.51.07 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  version.c
rm -f libxmlrpc_server.a
mips-openwrt-linux-musl-gcc-ar cru libxmlrpc_server.a registry.o method.o system_method.o
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
mips-openwrt-linux-musl-gcc-ranlib libxmlrpc_server.a
ccache_cc -pthread  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro  -shared -Wl,-soname,libxmlrpc.so.3  base_global.osh double.osh json.osh parse_datetime.osh parse_value.osh resource.osh trace.osh version.osh xmlrpc_data.osh xmlrpc_datetime.osh xmlrpc_string.osh xmlrpc_array.osh xmlrpc_struct.osh xmlrpc_build.osh xmlrpc_decompose.osh xmlrpc_expat.osh xmlrpc_parse.osh xmlrpc_serialize.osh xmlrpc_authcookie.osh -L/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil -lxmlrpc_util  -Lblddir/lib/expat/xmlparse -lxmlrpc_xmlparse -Lblddir/lib/expat/xmltok -lxmlrpc_xmltok -o libxmlrpc.so.3.51  
rm -f libxmlrpc.a
mips-openwrt-linux-musl-gcc-ar cru libxmlrpc.a base_global.o double.o json.o parse_datetime.o parse_value.o resource.o trace.o version.o xmlrpc_data.o xmlrpc_datetime.o xmlrpc_string.o xmlrpc_array.o xmlrpc_struct.o xmlrpc_build.o xmlrpc_decompose.o xmlrpc_expat.o xmlrpc_parse.o xmlrpc_serialize.o xmlrpc_authcookie.o
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
mips-openwrt-linux-musl-gcc-ranlib libxmlrpc.a
rm -f libxmlrpc.so.3
ln -s libxmlrpc.so.3.51 libxmlrpc.so.3
rm -f libxmlrpc.so
ln -s libxmlrpc.so.3 libxmlrpc.so
ccache_cc -pthread  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro  -shared -Wl,-soname,libxmlrpc_server.so.3  registry.osh method.osh system_method.osh -L. -lxmlrpc -Lblddir/lib/expat/xmlparse -lxmlrpc_xmlparse -Lblddir/lib/expat/xmltok -lxmlrpc_xmltok -L/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil -lxmlrpc_util  -o libxmlrpc_server.so.3.51  
rm -f libxmlrpc_server.so.3
ln -s libxmlrpc_server.so.3.51 libxmlrpc_server.so.3
rm -f libxmlrpc_server.so
ln -s libxmlrpc_server.so.3 libxmlrpc_server.so
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/src'
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07'
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07'
make -C include/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07//include/Makefile \
    install 
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include'
/bin/bash /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/mkinstalldirs /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib
mkdir /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install
mkdir /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr
mkdir /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib
/bin/bash /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/mkinstalldirs /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/include
mkdir /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/include
/bin/bash /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/mkinstalldirs /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/include/xmlrpc-c
mkdir /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/include/xmlrpc-c
 /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 644 xmlrpc-c/config.h /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/include/xmlrpc-c/config.h 
 /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 644 xmlrpc-c/inttypes.h /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/include/xmlrpc-c/inttypes.h 
 /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 644 xmlrpc-c/c_util.h /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/include/xmlrpc-c/c_util.h 
 /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 644 xmlrpc-c/util.h /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/include/xmlrpc-c/util.h 
 /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 644 xmlrpc-c/base.h /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/include/xmlrpc-c/base.h 
 /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 644 xmlrpc-c/json.h /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/include/xmlrpc-c/json.h 
 /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 644 xmlrpc-c/abyss.h /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/include/xmlrpc-c/abyss.h 
 /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 644 xmlrpc-c/abyss_unixsock.h /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/include/xmlrpc-c/abyss_unixsock.h 
 /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 644 xmlrpc-c/abyss_winsock.h /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/include/xmlrpc-c/abyss_winsock.h 
 /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 644 xmlrpc-c/server.h /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/include/xmlrpc-c/server.h 
 /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 644 xmlrpc-c/server_abyss.h /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/include/xmlrpc-c/server_abyss.h 
 /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 644 xmlrpc-c/server_w32httpsys.h /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/include/xmlrpc-c/server_w32httpsys.h 
 /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 644 xmlrpc-c/oldxmlrpc.h /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/include/xmlrpc-c/oldxmlrpc.h 
/bin/bash /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/mkinstalldirs /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/bin
mkdir /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/bin
/bin/bash /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/mkinstalldirs /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/pkgconfig
mkdir /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/pkgconfig
cd /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/include; \
  rm -f xmlrpc.h xmlrpc_client.h xmlrpc_server.h xmlrpc_cgi.h \
                xmlrpc_server_abyss.h xmlrpc_abyss.h \
	xmlrpc_server_w32httpsys.h \
        XmlRpcCpp.h; \
  ln -s xmlrpc-c/oldxmlrpc.h         xmlrpc.h; ln -s xmlrpc-c/server.h            xmlrpc_server.h; ln -s xmlrpc-c/server_abyss.h      xmlrpc_abyss.h; ln -s xmlrpc-c/server_w32httpsys.h xmlrpc_server_w32httpsys.h; 
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/include'
make -C lib/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07//lib/Makefile \
    install 
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib'
make -C util/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/util/Makefile \
    install 
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/util'
make[6]: Nothing to be done for 'install'.
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/util'
make -C libutil/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil/Makefile \
    install 
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil'
/bin/bash /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/mkinstalldirs /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib
 /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 644 libxmlrpc_util.a /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/libxmlrpc_util.a
 mips-openwrt-linux-musl-gcc-ranlib /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/libxmlrpc_util.a
/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 755 libxmlrpc_util.so.4.51 /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/libxmlrpc_util.so.4.51
cd /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib; \
  rm -f libxmlrpc_util.so.4; \
          ln -s libxmlrpc_util.so.4.51 libxmlrpc_util.so.4
cd /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib; \
  rm -f libxmlrpc_util.so; \
          ln -s libxmlrpc_util.so.4 libxmlrpc_util.so
/bin/bash /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/mkinstalldirs /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/include
/bin/bash /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/mkinstalldirs /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/include/xmlrpc-c
/bin/bash /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/mkinstalldirs /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/pkgconfig
/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 644 xmlrpc_util.pc /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/pkgconfig/xmlrpc_util.pc
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil'
make -C expat/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/Makefile \
    install 
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat'
/bin/bash /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/mkinstalldirs /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib
/bin/bash /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/mkinstalldirs /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/include
/bin/bash /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/mkinstalldirs /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/include/xmlrpc-c
/bin/bash /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/mkinstalldirs /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/pkgconfig
/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 644 xmlrpc_expat.pc /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/pkgconfig/xmlrpc_expat.pc
make -C gennmtab/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/gennmtab/Makefile \
    install 
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/gennmtab'
make[7]: Nothing to be done for 'install'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/gennmtab'
make -C xmlparse/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmlparse/Makefile \
    install 
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmlparse'
/bin/bash /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/mkinstalldirs /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib
 /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 644 libxmlrpc_xmlparse.a /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/libxmlrpc_xmlparse.a
 mips-openwrt-linux-musl-gcc-ranlib /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/libxmlrpc_xmlparse.a
make -C /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok/Makefile \
    libxmlrpc_xmltok.so
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok'
make[8]: 'libxmlrpc_xmltok.so' is up to date.
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok'
make -C /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil/Makefile \
    libxmlrpc_util.so
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil'
make[8]: 'libxmlrpc_util.so' is up to date.
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil'
/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 755 libxmlrpc_xmlparse.so.3.51 /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/libxmlrpc_xmlparse.so.3.51
cd /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib; \
  rm -f libxmlrpc_xmlparse.so.3; \
          ln -s libxmlrpc_xmlparse.so.3.51 libxmlrpc_xmlparse.so.3
cd /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib; \
  rm -f libxmlrpc_xmlparse.so; \
          ln -s libxmlrpc_xmlparse.so.3 libxmlrpc_xmlparse.so
/bin/bash /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/mkinstalldirs /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/include
/bin/bash /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/mkinstalldirs /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/include/xmlrpc-c
/bin/bash /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/mkinstalldirs /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/pkgconfig
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmlparse'
make -C xmltok/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok/Makefile \
    install 
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok'
/bin/bash /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/mkinstalldirs /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib
 /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 644 libxmlrpc_xmltok.a /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/libxmlrpc_xmltok.a
 mips-openwrt-linux-musl-gcc-ranlib /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/libxmlrpc_xmltok.a
/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 755 libxmlrpc_xmltok.so.3.51 /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/libxmlrpc_xmltok.so.3.51
cd /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib; \
  rm -f libxmlrpc_xmltok.so.3; \
          ln -s libxmlrpc_xmltok.so.3.51 libxmlrpc_xmltok.so.3
cd /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib; \
  rm -f libxmlrpc_xmltok.so; \
          ln -s libxmlrpc_xmltok.so.3 libxmlrpc_xmltok.so
/bin/bash /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/mkinstalldirs /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/include
/bin/bash /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/mkinstalldirs /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/include/xmlrpc-c
/bin/bash /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/mkinstalldirs /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/pkgconfig
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat'
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib'
make -C src/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07//src/Makefile \
    install 
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/src'
/bin/bash /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/mkinstalldirs /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib
 /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 644 libxmlrpc.a /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/libxmlrpc.a
 /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 644 libxmlrpc_server.a /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/libxmlrpc_server.a
 mips-openwrt-linux-musl-gcc-ranlib /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/libxmlrpc.a
 mips-openwrt-linux-musl-gcc-ranlib /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/libxmlrpc_server.a
make -C /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil/Makefile \
    libxmlrpc_util.so
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil'
make[6]: 'libxmlrpc_util.so' is up to date.
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil'
make -C /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmlparse/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmlparse/Makefile \
    libxmlrpc_xmlparse.so
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmlparse'
make -C /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok/Makefile \
    libxmlrpc_xmltok.so
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok'
make[7]: 'libxmlrpc_xmltok.so' is up to date.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok'
make -C /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil/Makefile \
    libxmlrpc_util.so
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil'
make[7]: 'libxmlrpc_util.so' is up to date.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/libutil'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmlparse'
make -C /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok/ -f /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok/Makefile \
    libxmlrpc_xmltok.so
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok'
make[6]: 'libxmlrpc_xmltok.so' is up to date.
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/lib/expat/xmltok'
/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 755 libxmlrpc.so.3.51 /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/libxmlrpc.so.3.51
cd /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib; \
  rm -f libxmlrpc.so.3; \
          ln -s libxmlrpc.so.3.51 libxmlrpc.so.3
cd /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib; \
  rm -f libxmlrpc.so; \
          ln -s libxmlrpc.so.3 libxmlrpc.so
/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 755 libxmlrpc_server.so.3.51 /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/libxmlrpc_server.so.3.51
cd /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib; \
  rm -f libxmlrpc_server.so.3; \
          ln -s libxmlrpc_server.so.3.51 libxmlrpc_server.so.3
cd /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib; \
  rm -f libxmlrpc_server.so; \
          ln -s libxmlrpc_server.so.3 libxmlrpc_server.so
/bin/bash /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/mkinstalldirs /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/include
/bin/bash /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/mkinstalldirs /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/include/xmlrpc-c
/bin/bash /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/mkinstalldirs /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/pkgconfig
/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 644 xmlrpc.pc /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/pkgconfig/xmlrpc.pc
/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 644 xmlrpc_client.pc /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/pkgconfig/xmlrpc_client.pc
/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 644 xmlrpc_server.pc /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/pkgconfig/xmlrpc_server.pc
/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 644 xmlrpc_server_abyss.pc /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/pkgconfig/xmlrpc_server_abyss.pc
/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 644 xmlrpc_server_cgi.pc /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/pkgconfig/xmlrpc_server_cgi.pc
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/src'
/bin/bash /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/mkinstalldirs /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib
/bin/bash /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/mkinstalldirs /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/include
/bin/bash /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/mkinstalldirs /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/include/xmlrpc-c
/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/install-sh -c -m 755 xmlrpc-c-config /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/bin/xmlrpc-c-config
/bin/bash /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/mkinstalldirs /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/pkgconfig
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07'
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-mips_24kc/xmlrpc-c-common/usr/lib/libxmlrpc_util.so.4.51: shared object
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-mips_24kc/xmlrpc-c-common into /openwrt/bin/packages/mips_24kc/packages/xmlrpc-c-common_1.51.07-1_mips_24kc.ipk
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-mips_24kc/xmlrpc-c-internal/usr/lib/libxmlrpc_xmlparse.so.3.51: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-mips_24kc/xmlrpc-c-internal/usr/lib/libxmlrpc.so.3.51: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-mips_24kc/xmlrpc-c-internal/usr/lib/libxmlrpc_xmltok.so.3.51: shared object
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-mips_24kc/xmlrpc-c-internal into /openwrt/bin/packages/mips_24kc/packages/xmlrpc-c-internal_1.51.07-1_mips_24kc.ipk
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-mips_24kc/xmlrpc-c into /openwrt/bin/packages/mips_24kc/packages/xmlrpc-c_1.51.07-1_mips_24kc.ipk
cp: cannot stat '/openwrt/build_dir/target-mips_24kc_musl/xmlrpc-c-internal/xmlrpc-c-1.51.07/ipkg-install/usr/lib/libxmlrpc_client*': No such file or directory
make[3]: *** [Makefile:225: /openwrt/bin/packages/mips_24kc/packages/xmlrpc-c-client_1.51.07-1_mips_24kc.ipk] Error 1
```
