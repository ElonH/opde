---
title: "compile.40"
date: 2021-06-22 10:47:21.976327
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
make package/feeds/packages/tmate/compile -j$(nproc) || make package/feeds/packages/tmate/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-Avoid-initializing-stdout-twice.patch using plaintext: 
patching file log.c
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force 
autoreconf: configure.ac: tracing
autoreconf: configure.ac: creating directory etc
autoreconf: configure.ac: not using Libtool
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: configure.ac: not using Autoheader
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
configure.ac:17: installing 'etc/compile'
configure.ac:9: installing 'etc/config.guess'
configure.ac:9: installing 'etc/config.sub'
configure.ac:7: installing 'etc/install-sh'
configure.ac:7: installing 'etc/missing'
Makefile.am: installing 'etc/depcomp'
autoreconf: Leaving directory `.'
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/mips
checking whether make supports nested variables... yes
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
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
checking how to run the C preprocessor... ccache_cc -E
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking pkg-config is at least version 0.9.0... yes
checking for glibc... no
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
checking bitstring.h usability... no
checking bitstring.h presence... no
checking for bitstring.h... no
checking curses.h usability... yes
checking curses.h presence... yes
checking for curses.h... yes
checking dirent.h usability... yes
checking dirent.h presence... yes
checking for dirent.h... yes
checking execinfo.h usability... no
checking execinfo.h presence... no
checking for execinfo.h... no
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking for inttypes.h... (cached) yes
checking libutil.h usability... no
checking libutil.h presence... no
checking for libutil.h... no
checking ncurses.h usability... yes
checking ncurses.h presence... yes
checking for ncurses.h... yes
checking ndir.h usability... no
checking ndir.h presence... no
checking for ndir.h... no
checking paths.h usability... yes
checking paths.h presence... yes
checking for paths.h... yes
checking pty.h usability... yes
checking pty.h presence... yes
checking for pty.h... yes
checking for stdint.h... (cached) yes
checking sys/dir.h usability... yes
checking sys/dir.h presence... yes
checking for sys/dir.h... yes
checking sys/ndir.h usability... no
checking sys/ndir.h presence... no
checking for sys/ndir.h... no
checking sys/tree.h usability... no
checking sys/tree.h presence... no
checking for sys/tree.h... no
checking term.h usability... yes
checking term.h presence... yes
checking for term.h... yes
checking util.h usability... no
checking util.h presence... no
checking for util.h... no
checking for library containing flock... none required
checking for library containing backtrace... no
checking for backtrace... no
checking for dirfd... yes
checking for flock... yes
checking for setproctitle... no
checking for sysconf... yes
checking for cfmakeraw... yes
checking for library containing clock_gettime... none required
checking for LIBEVENT... no
checking for library containing event_init... no
configure: error: "libevent not found"
make[3]: *** [Makefile:55: /openwrt/build_dir/target-mips_24kc_musl/tmate-2.4.0/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
