---
title: "compile.40"
date: 2021-06-22 10:50:44.058937
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
make package/feeds/packages/mutt/compile -j$(nproc) || make package/feeds/packages/mutt/compile V=s
```

#### Compile.txt

``` bash
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force -I m4
autoreconf: configure.ac: tracing
autoreconf: configure.ac: not using Libtool
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
autoreconf: Leaving directory `.'
configure: loading site script /openwrt/include/site/mips
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking for style of include used by make... GNU
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
checking dependency style of ccache_cc... gcc3
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
checking minix/config.h usability... no
checking minix/config.h presence... no
checking for minix/config.h... no
checking whether it is safe to define __EXTENSIONS__... yes
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking for prefix... /usr
checking for mips-openwrt-linux-gcc... (cached) ccache_cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether ccache_cc accepts -g... (cached) yes
checking for ccache_cc option to accept ISO C89... (cached) none needed
checking whether ccache_cc understands -c and -o together... (cached) yes
checking dependency style of ccache_cc... (cached) gcc3
checking for ccache_cc option to accept ISO C99... none needed
checking for library containing strerror... none required
checking how to run the C preprocessor... ccache_cc -E
checking whether make sets $(MAKE)... (cached) yes
checking for mips-openwrt-linux-ranlib... mips-openwrt-linux-musl-gcc-ranlib
checking for mips-openwrt-linux-ar... mips-openwrt-linux-musl-gcc-ar
checking for GNU make... yes
checking for inline... inline
checking for an ANSI C-conforming const... yes
checking whether byte ordering is bigendian... (cached) yes
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking for _LARGEFILE_SOURCE value needed for large files... no
checking size of off_t... (cached) 8
checking for dbx... no
checking for gdb... no
checking for sdb... no
checking for inttypes.h... (cached) yes
checking for uint32_t... yes
checking size of short... (cached) 2
checking size of int... (cached) 4
checking size of long... (cached) 4
checking size of long long... (cached) 8
checking for unsigned long long int... yes
checking for long long int... yes
checking for sendmail... /usr/sbin/sendmail
checking whether to build with GPGME support... no
checking for ispell... no
checking for initscr... no
checking for waddnwstr in -lncurses... yes
checking for initscr in -lncurses... yes
checking for tgetent in -ltinfo... no
checking ncurses/ncurses.h usability... no
checking ncurses/ncurses.h presence... no
checking for ncurses/ncurses.h... no
checking ncurses.h usability... yes
checking ncurses.h presence... yes
checking for ncurses.h... yes
checking for start_color declaration... yes
checking for typeahead declaration... yes
checking for bkgdset declaration... yes
checking for curs_set declaration... yes
checking for meta declaration... yes
checking for use_default_colors declaration... yes
checking for resizeterm declaration... yes
checking for use_extended_names... yes
checking for ANSI C header files... (cached) yes
checking stdarg.h usability... yes
checking stdarg.h presence... yes
checking for stdarg.h... yes
checking sys/ioctl.h usability... yes
checking sys/ioctl.h presence... yes
checking for sys/ioctl.h... yes
checking ioctl.h usability... no
checking ioctl.h presence... no
checking for ioctl.h... no
checking sysexits.h usability... yes
checking sysexits.h presence... yes
checking for sysexits.h... yes
checking sys/time.h usability... yes
checking sys/time.h presence... yes
checking for sys/time.h... yes
checking sys/resource.h usability... yes
checking sys/resource.h presence... yes
checking for sys/resource.h... yes
checking unix.h usability... no
checking unix.h presence... no
checking for unix.h... no
checking for setrlimit... yes
checking for getsid... yes
checking for fgets_unlocked... yes
checking for fgetc_unlocked... yes
checking for sig_atomic_t in signal.h... yes, non volatile
checking whether sys_siglist is declared... (cached) no
checking for pid_t... yes
checking for ssize_t... yes
checking for fgetpos... yes
checking for memmove... yes
checking for setegid... yes
checking for srand48... yes
checking for strerror... (cached) yes
checking for setenv... yes
checking for strcasecmp... yes
checking for strdup... yes
checking for strsep... yes
checking for strtok_r... yes
checking for wcscasecmp... yes
checking for strcasestr... yes
checking for mkdtemp... yes
checking for getopt... yes
checking getopt.h usability... yes
checking getopt.h presence... yes
checking for getopt.h... yes
checking for snprintf... yes
checking for vsnprintf... (cached) yes
checking whether your system's snprintf is C99 compliant... no
checking whether your system's vsnprintf is C99 compliant... no
checking for va_copy... va_copy
checking for ftruncate... yes
checking for strftime... (cached) yes
checking for futimens... yes
checking for struct timespec... yes
checking for struct stat.st_atim.tv_nsec... yes
checking for struct stat.st_mtim.tv_nsec... yes
checking for struct stat.st_ctim.tv_nsec... yes
checking for utimensat... yes
checking for clock_gettime... yes
checking for fchdir... yes
checking for regcomp... yes
checking whether your system's regexp library is completely broken... yes
Using the included GNU regex instead.
checking if /var/mail is world writable... no
checking if /var/mail is group writable... no
checking where to put the documentation... ${datarootdir}/doc/mutt
checking for gethostent... yes
checking for setsockopt... yes
checking for getaddrinfo... (cached) yes
checking sys/select.h usability... yes
checking sys/select.h presence... yes
checking for sys/select.h... yes
checking for socklen_t... yes
checking zlib.h usability... yes
checking zlib.h presence... yes
checking for zlib.h... yes
checking for deflate in -lz... yes
checking for deflate in -lz... (cached) yes
checking for X509_STORE_CTX_new in -lcrypto... no
configure: error: Unable to find SSL library
make[3]: *** [Makefile:62: /openwrt/build_dir/target-mips_24kc_musl/mutt-1.14.7/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
