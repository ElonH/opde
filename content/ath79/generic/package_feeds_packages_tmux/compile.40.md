---
title: "compile.40"
date: 2021-06-22 10:37:31.207754
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
make package/feeds/packages/tmux/compile -j$(nproc) || make package/feeds/packages/tmux/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/100-add-crosscompiling-fallbacks.patch using plaintext: 
patching file configure.ac
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force 
autoreconf: configure.ac: tracing
autoreconf: configure.ac: creating directory etc
autoreconf: configure.ac: not using Libtool
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: configure.ac: not using Autoheader
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
configure.ac:45: installing 'etc/compile'
configure.ac:10: installing 'etc/config.guess'
configure.ac:10: installing 'etc/config.sub'
configure.ac:8: installing 'etc/install-sh'
configure.ac:8: installing 'etc/missing'
Makefile.am: installing 'etc/depcomp'
configure.ac: installing 'etc/ylwrap'
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
checking for ccache_cc option to accept ISO C99... none needed
checking how to run the C preprocessor... ccache_cc -E
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for bison... bison -y
checking pkg-config is at least version 0.9.0... yes
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
checking minix/config.h usability... no
checking minix/config.h presence... no
checking for minix/config.h... no
checking whether it is safe to define __EXTENSIONS__... yes
checking bitstring.h usability... no
checking bitstring.h presence... no
checking for bitstring.h... no
checking dirent.h usability... yes
checking dirent.h presence... yes
checking for dirent.h... yes
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking for inttypes.h... (cached) yes
checking libproc.h usability... no
checking libproc.h presence... no
checking for libproc.h... no
checking libutil.h usability... no
checking libutil.h presence... no
checking for libutil.h... no
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
checking util.h usability... no
checking util.h presence... no
checking for util.h... no
checking for library containing sys_signame... no
checking for fmod in -lm... yes
checking for library containing flock... none required
checking for dirfd... yes
checking for flock... yes
checking for prctl... yes
checking for proc_pidinfo... no
checking for sysconf... yes
checking for asprintf... yes
checking for cfmakeraw... yes
checking for clock_gettime... yes
checking for closefrom... no
checking for explicit_bzero... yes
checking for fgetln... yes
checking for freezero... no
checking for getdtablecount... no
checking for getdtablesize... yes
checking for getline... yes
checking for getprogname... no
checking for memmem... yes
checking for setenv... yes
checking for setproctitle... no
checking for strcasestr... yes
checking for strlcat... yes
checking for strlcpy... yes
checking for strndup... yes
checking for strsep... yes
checking for working strnlen... yes
checking for working strtonum... no
checking for working reallocarray... no
checking for working recallocarray... no
checking for library containing clock_gettime... none required
checking for LIBEVENT_CORE... no
checking for LIBEVENT... no
checking for library containing event_init... no
checking event2/event.h usability... no
checking event2/event.h presence... no
checking for event2/event.h... no
checking event.h usability... no
checking event.h presence... no
checking for event.h... no
configure: error: "libevent not found"
make[3]: *** [Makefile:49: /openwrt/build_dir/target-mips_24kc_musl/tmux-3.2a/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
