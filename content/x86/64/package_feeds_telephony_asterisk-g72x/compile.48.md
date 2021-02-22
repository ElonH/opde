---
title: "compile.48"
date: 2021-02-22 14:41:15.178478
hidden: false
draft: false
weight: -48
---

build number: `48`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/telephony/asterisk-g72x/compile -j$(nproc) || make package/feeds/telephony/asterisk-g72x/compile V=s
```

#### Compile.txt

``` bash
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-x86_64_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal -I m4 -I . --force -I m4
autoreconf: configure.ac: tracing
autoreconf: running: /openwrt/staging_dir/host/bin/libtoolize --install --force
OpenWrt-libtoolize: putting auxiliary files in `.'.
OpenWrt-libtoolize: linking file `./config.guess'
OpenWrt-libtoolize: linking file `./config.sub'
OpenWrt-libtoolize: linking file `./install-sh'
OpenWrt-libtoolize: linking file `./ltmain.sh'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `m4'.
OpenWrt-libtoolize: linking file `m4/libtool.m4'
OpenWrt-libtoolize: linking file `m4/ltoptions.m4'
OpenWrt-libtoolize: linking file `m4/ltsugar.m4'
OpenWrt-libtoolize: linking file `m4/ltversion.m4'
OpenWrt-libtoolize: linking file `m4/lt~obsolete.m4'
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-x86_64_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-x86_64_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
configure.ac:8: installing './compile'
configure.ac:7: installing './missing'
Makefile.am: installing './depcomp'
autoreconf: Leaving directory `.'
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/x86_64
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-openwrt-linux-gnu
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for x86_64-openwrt-linux-strip... x86_64-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking for x86_64-openwrt-linux-gcc... ccache_cc
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
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache_cc... x86_64-openwrt-linux-musl-ld
checking if the linker (x86_64-openwrt-linux-musl-ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... x86_64-openwrt-linux-musl-gcc-nm
checking the name lister (x86_64-openwrt-linux-musl-gcc-nm) interface... BSD nm
checking whether ln -s works... yes
checking the maximum length of command line arguments... 1572864
checking whether the shell understands some XSI constructs... yes
checking whether the shell understands "+="... yes
checking how to convert x86_64-pc-linux-gnu file names to x86_64-openwrt-linux-gnu format... func_convert_file_noop
checking how to convert x86_64-pc-linux-gnu file names to toolchain format... func_convert_file_noop
checking for x86_64-openwrt-linux-musl-ld option to reload object files... -r
checking for x86_64-openwrt-linux-objdump... x86_64-openwrt-linux-musl-objdump
checking how to recognize dependent libraries... pass_all
checking for x86_64-openwrt-linux-dlltool... no
checking for dlltool... no
checking how to associate runtime and link libraries... printf %s\n
checking for x86_64-openwrt-linux-ar... x86_64-openwrt-linux-musl-gcc-ar
checking for archiver @FILE support... @
checking for x86_64-openwrt-linux-strip... (cached) x86_64-openwrt-linux-musl-strip
checking for x86_64-openwrt-linux-ranlib... x86_64-openwrt-linux-musl-gcc-ranlib
checking command to parse x86_64-openwrt-linux-musl-gcc-nm output from ccache_cc object... ok
checking for sysroot... no
checking for x86_64-openwrt-linux-mt... no
checking for mt... no
checking if : is a manifest tool... no
checking how to run the C preprocessor... ccache_cc -E
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
checking for dlfcn.h... yes
checking for objdir... .libs
checking if ccache_cc supports -fno-rtti -fno-exceptions... no
checking for ccache_cc option to produce PIC... -fPIC -DPIC
checking if ccache_cc PIC flag -fPIC -DPIC works... yes
checking if ccache_cc static flag -static works... yes
checking if ccache_cc supports -c -o file.o... yes
checking if ccache_cc supports -c -o file.o... (cached) yes
checking whether the ccache_cc linker (x86_64-openwrt-linux-musl-ld -m elf_x86_64) supports shared libraries... yes
checking whether -lc should be explicitly linked in... no
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... no
checking asterisk/asterisk.h usability... no
checking asterisk/asterisk.h presence... no
checking for asterisk/asterisk.h... no
checking whether C compiler accepts -march=native... yes
checking whether C compiler accepts -mavx... yes
checking whether C compiler accepts -march=core2... yes
checking whether C compiler accepts -march=atom... yes
checking whether C compiler accepts -march=k8-sse3... yes
checking whether C compiler accepts -march=barcelona... yes
checking whether C compiler accepts -march=geode... no
checking whether C compiler accepts -flto... yes
checking for initBcg729EncoderChannel in -lbcg729... yes
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating Makefile
config.status: creating config.h
config.status: executing depfiles commands
config.status: executing libtool commands
configure: WARNING: unrecognized options: --disable-nls

Architecture: x86_64
  CPU -march: native
      CFLAGS: -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/asterisk-g72x-1.4.3=asterisk-g72x-1.4.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro   -I"/openwrt/staging_dir/target-x86_64_musl/usr/include"
     LDFLAGS: 
 Codecs impl: Bcg729
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/asterisk-g72x-1.4.3'
make  all-am
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/asterisk-g72x-1.4.3'
/bin/bash ./libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I.   -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include  -I/usr/local/include -DG72X_ASTERISK=160 -I"/openwrt/staging_dir/target-x86_64_musl/usr/include" -DG72X_BCG729 -Wall -D_GNU_SOURCE -DG72X_9 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/asterisk-g72x-1.4.3=asterisk-g72x-1.4.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -MT codec_g729_la-codec_g72x.lo -MD -MP -MF .deps/codec_g729_la-codec_g72x.Tpo -c -o codec_g729_la-codec_g72x.lo `test -f 'codec_g72x.c' || echo './'`codec_g72x.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/usr/local/include -DG72X_ASTERISK=160 -I/openwrt/staging_dir/target-x86_64_musl/usr/include -DG72X_BCG729 -Wall -D_GNU_SOURCE -DG72X_9 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/asterisk-g72x-1.4.3=asterisk-g72x-1.4.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -MT codec_g729_la-codec_g72x.lo -MD -MP -MF .deps/codec_g729_la-codec_g72x.Tpo -c codec_g72x.c  -fPIC -DPIC -o .libs/codec_g729_la-codec_g72x.o
codec_g72x.c:24:18: fatal error: asterisk.h: No such file or directory
         #include <asterisk.h>
                  ^~~~~~~~~~~~
compilation terminated.
make[5]: *** [Makefile:648: codec_g729_la-codec_g72x.lo] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/asterisk-g72x-1.4.3'
make[4]: *** [Makefile:424: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/asterisk-g72x-1.4.3'
make[3]: *** [Makefile:56: /openwrt/build_dir/target-x86_64_musl/asterisk-g72x-1.4.3/.built] Error 2
```
