---
title: "compile.40"
date: 2021-06-22 10:42:16.504020
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
make package/feeds/packages/tor/compile -j$(nproc) || make package/feeds/packages/tor/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-torrc.patch using plaintext: 
patching file src/config/torrc.sample.in
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force -I m4
autoreconf: configure.ac: tracing
autoreconf: configure.ac: not using Libtool
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
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
checking whether make supports nested variables... (cached) yes
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
checking pkg-config is at least version 0.9.0... yes
checking for SYSTEMD... no
configure: Okay, checking for systemd a different way...
checking for SYSTEMD... no
checking for mips-openwrt-linux-ar... mips-openwrt-linux-musl-gcc-ar
checking the archiver (mips-openwrt-linux-musl-gcc-ar) interface... ar
checking for mips-openwrt-linux-gcc... (cached) ccache_cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether ccache_cc accepts -g... (cached) yes
checking for ccache_cc option to accept ISO C89... (cached) none needed
checking whether ccache_cc understands -c and -o together... (cached) yes
checking dependency style of ccache_cc... (cached) gcc3
checking how to run the C preprocessor... ccache_cc -E
checking whether make sets $(MAKE)... (cached) yes
checking for mips-openwrt-linux-ranlib... mips-openwrt-linux-musl-gcc-ranlib
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for perl... perl
checking for asciidoc... /usr/bin/asciidoc
checking for a2x... /usr/bin/a2x
checking for ccache_cc option to accept ISO C99... none needed
checking for Python 3... /openwrt/staging_dir/hostpkg/bin/python3
checking for flexible array members... yes
checking for working C99 mid-block declaration syntax... yes
checking for working C99 designated initializers... yes
checking for __attribute__((fallthrough))... yes
checking for win32... cross
checking for win32 (cross)... no
checking for MIPSpro compiler... no
checking whether byte ordering is bigendian... (cached) yes
checking for library containing socket... none required
checking for library containing gethostbyname... none required
checking for library containing dlopen... none required
checking for library containing inet_aton... none required
checking for library containing backtrace... no
checking for library containing clock_gettime... none required
checking for library containing pthread_create... none required
checking for library containing pthread_detach... none required
checking for _NSGetEnviron... no
checking for RtlSecureZeroMemory... no
checking for SecureZeroMemory... no
checking for accept4... yes
checking for backtrace... no
checking for backtrace_symbols_fd... no
checking for eventfd... yes
checking for explicit_bzero... yes
checking for timingsafe_memcmp... no
checking for flock... yes
checking for fsync... yes
checking for ftime... yes
checking for get_current_dir_name... yes
checking for getaddrinfo... (cached) yes
checking for getdelim... yes
checking for getifaddrs... yes
checking for getline... yes
checking for getrlimit... yes
checking for gettimeofday... (cached) yes
checking for gmtime_r... yes
checking for gnu_get_libc_version... no
checking for inet_aton... yes
checking for ioctl... yes
checking for issetugid... yes
checking for llround... yes
checking for localtime_r... yes
checking for lround... yes
checking for madvise... yes
checking for memmem... yes
checking for memset_s... no
checking for minherit... no
checking for mmap... yes
checking for pipe... yes
checking for pipe2... yes
checking for prctl... yes
checking for readpassphrase... no
checking for rint... yes
checking for sigaction... yes
checking for socketpair... yes
checking for statvfs... yes
checking for strncasecmp... yes
checking for strcasecmp... yes
checking for strlcat... yes
checking for strlcpy... yes
checking for strnlen... yes
checking for strptime... yes
checking for strtok_r... yes
checking for strtoull... yes
checking for sysconf... yes
checking for sysctl... no
checking for truncate... yes
checking for uname... yes
checking for usleep... yes
checking for vasprintf... yes
checking for _vscprintf... no
checking for a pre-Yosemite OS X build target... no
checking for mach_approximate_time... no
checking for a pre-Sierra OSX build target... no
checking for clock_gettime... yes
checking for getentropy... yes
checking pthread.h usability... yes
checking pthread.h presence... yes
checking for pthread.h... yes
checking for pthread_create... yes
checking for pthread_condattr_setclock... yes
checking for glob... yes
checking whether free(NULL) works... cross
checking for libevent directory... configure: WARNING: Could not find a linkable libevent.  If you have it installed somewhere unusual, you can specify an explicit path using --with-libevent-dir
configure: WARNING: On Debian, you can install libevent using "apt-get install libevent-dev"
configure: error: Missing libraries; unable to proceed.
make[3]: *** [Makefile:187: /openwrt/build_dir/target-mips_24kc_musl/tor-basic/tor-0.4.5.8/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
