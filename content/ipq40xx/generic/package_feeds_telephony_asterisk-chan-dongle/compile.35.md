---
title: "compile.35"
date: 2021-06-20 00:34:38.498334
hidden: false
draft: false
weight: -35
---

build number: `35`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/telephony/asterisk-chan-dongle/compile -j$(nproc) || make package/feeds/telephony/asterisk-chan-dongle/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/200-fix-iconv-detection.patch using plaintext: 
patching file configure.ac

Applying ./patches/300-use-openwrt-flags.patch using plaintext: 
patching file configure.ac
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/usr/share/aclocal -I m4 -I . --force 
autoreconf: configure.ac: tracing
autoreconf: configure.ac: not using Libtool
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
configure.ac:71: installing './compile'
configure.ac:6: installing './config.guess'
configure.ac:6: installing './config.sub'
configure.ac:7: installing './install-sh'
configure.ac:7: installing './missing'
automake: error: no 'Makefile.am' found for any configure output
autoreconf: /openwrt/staging_dir/host/bin/automake failed with exit status: 1
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/arm
checking build system type... x86_64-pc-linux-gnu
checking host system type... arm-openwrt-linux-gnu
checking target system type... arm-openwrt-linux-gnu
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for arm-openwrt-linux-strip... arm-openwrt-linux-muslgnueabi-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking for arm-openwrt-linux-gcc... ccache_cc
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
checking dependency style of ccache_cc... none
checking how to run the C preprocessor... ccache_cc -E
checking for strip... (cached) arm-openwrt-linux-muslgnueabi-strip
checking for rm... rm
checking for library containing libiconv... -liconv
checking for sqlite3_open in -lsqlite3... yes
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
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking for stdlib.h... (cached) yes
checking for string.h... (cached) yes
checking sys/time.h usability... yes
checking sys/time.h presence... yes
checking for sys/time.h... yes
checking termios.h usability... yes
checking termios.h presence... yes
checking for termios.h... yes
checking whether asterisk.h in /openwrt/staging_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/usr/include... no
configure: error: Can't find "asterisk.h"
make[3]: *** [Makefile:71: /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/asterisk-chan-dongle-2020-05-28-328b2b7d/.configured_a17fb5ef857664f03cd0ce37cc5ea591] Error 1
```
