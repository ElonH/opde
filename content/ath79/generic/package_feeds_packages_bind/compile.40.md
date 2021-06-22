---
title: "compile.40"
date: 2021-06-22 10:50:06.151409
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
make package/feeds/packages/bind/compile -j$(nproc) || make package/feeds/packages/bind/compile V=s
```

#### Compile.txt

``` bash
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force 
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
autoreconf: configure.ac: tracing
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
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
OpenWrt-libtoolize: Consider adding `-I m4' to ACLOCAL_AMFLAGS in Makefile.am.
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
autoreconf: Leaving directory `.'
configure: WARNING: unrecognized options: --disable-nls, --with-libtool, --without-python
configure: loading site script /openwrt/include/site/mips
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking target system type... mips-openwrt-linux-gnu
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking how to create a pax tar archive... gnutar
checking whether make supports nested variables... (cached) yes
checking whether to enable maintainer-specific portions of Makefiles... no
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
checking for ccache_cc option to accept ISO C99... none needed
checking for build system executable suffix... no
checking whether byte ordering is bigendian... (cached) yes
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking for _LARGEFILE_SOURCE value needed for large files... no
checking whether make sets $(MAKE)... (cached) yes
checking for mips-openwrt-linux-ar... mips-openwrt-linux-musl-gcc-ar
checking the archiver (mips-openwrt-linux-musl-gcc-ar) interface... ar
checking whether ln -s works... yes
checking for a POSIX-compatible shell... /bin/bash
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache_cc... mips-openwrt-linux-musl-ld
checking if the linker (mips-openwrt-linux-musl-ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... mips-openwrt-linux-musl-gcc-nm
checking the name lister (mips-openwrt-linux-musl-gcc-nm) interface... BSD nm
checking the maximum length of command line arguments... 3145728
checking whether the shell understands some XSI constructs... yes
checking whether the shell understands "+="... yes
checking how to convert x86_64-pc-linux-gnu file names to mips-openwrt-linux-gnu format... func_convert_file_noop
checking how to convert x86_64-pc-linux-gnu file names to toolchain format... func_convert_file_noop
checking for mips-openwrt-linux-musl-ld option to reload object files... -r
checking for mips-openwrt-linux-objdump... mips-openwrt-linux-musl-objdump
checking how to recognize dependent libraries... pass_all
checking for mips-openwrt-linux-dlltool... no
checking for dlltool... no
checking how to associate runtime and link libraries... printf %s\n
checking for mips-openwrt-linux-ar... (cached) mips-openwrt-linux-musl-gcc-ar
checking for archiver @FILE support... @
checking for mips-openwrt-linux-strip... (cached) mips-openwrt-linux-musl-strip
checking for mips-openwrt-linux-ranlib... mips-openwrt-linux-musl-gcc-ranlib
checking command to parse mips-openwrt-linux-musl-gcc-nm output from ccache_cc object... ok
checking for sysroot... no
checking for mips-openwrt-linux-mt... no
checking for mt... no
checking if : is a manifest tool... no
checking for dlfcn.h... yes
checking for objdir... .libs
checking if ccache_cc supports -fno-rtti -fno-exceptions... no
checking for ccache_cc option to produce PIC... -fPIC -DPIC
checking if ccache_cc PIC flag -fPIC -DPIC works... yes
checking if ccache_cc static flag -static works... yes
checking if ccache_cc supports -c -o file.o... yes
checking if ccache_cc supports -c -o file.o... (cached) yes
checking whether the ccache_cc linker (mips-openwrt-linux-musl-ld) supports shared libraries... yes
checking whether -lc should be explicitly linked in... no
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking for shl_load... no
checking for shl_load in -ldld... no
checking for dlopen... yes
checking whether a program can dlopen itself... cross
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... no
checking whether C compiler accepts -fno-strict-aliasing... yes
checking whether C compiler accepts -Werror -fno-delete-null-pointer-checks... yes
checking whether C compiler accepts -fdiagnostics-show-option... yes
checking pkg-config is at least version 0.9.0... yes
checking whether to enable fuzzing mode... no
checking whether to emulate atomics with mutexes... no
checking for perl5... no
checking for perl... /openwrt/staging_dir/host/bin/perl
checking for perl module: Digest::HMAC... no
checking for perl module: File::Fetch... yes
checking for perl module: Net::DNS... no
checking for perl module: Net::DNS::Nameserver... no
checking for perl module: Time::HiRes... yes
checking for a Python interpreter with version >= 3.4... python
checking for python... /openwrt/staging_dir/host/bin/python
checking for python version... 3.8
checking for python platform... linux
checking for python script directory... ${prefix}/lib/python3.8/site-packages
checking for python extension module directory... ${exec_prefix}/lib/python3.8/site-packages
checking for pytest-3... no
checking for py.test-3... no
checking for pytest... no
checking for pytest-pypy... no
configure: WARNING: pytest not found, some system tests will be skipped
checking for python module: dns... no
checking for xsltproc... /usr/bin/xsltproc
checking for fcntl.h... yes
checking for regex.h... yes
checking for sys/time.h... yes
checking for unistd.h... (cached) yes
checking for sys/mman.h... yes
checking for sys/sockio.h... no
checking for sys/select.h... yes
checking for sys/param.h... yes
checking for sys/sysctl.h... no
checking for net/if6.h... no
checking for sys/socket.h... yes
checking for net/route.h... yes
checking for linux/netlink.h... yes
checking for linux/rtnetlink.h... yes
checking threads.h usability... yes
checking threads.h presence... yes
checking for threads.h... yes
checking for thread local storage (TLS) class... _Thread_local
checking for an ANSI C-conforming const... yes
checking for inline... inline
checking for working volatile... yes
checking for sysctlbyname... no
checking for mmap... yes
checking for seteuid... yes
checking for setresuid... (cached) no
checking for setegid... yes
checking for setresgid... yes
checking for size_t... yes
checking for ssize_t... yes
checking for uintptr_t... yes
checking for uname... yes
checking for __attribute__((noreturn))... yes
checking for __attribute__((malloc))... yes
checking for extended malloc attributes... no
checking for __attribute__((returns_nonnull))... yes
checking for kqueue... no
checking for epoll_create1... yes
checking sys/devpoll.h usability... no
checking sys/devpoll.h presence... no
checking for sys/devpoll.h... no
checking devpoll.h usability... no
checking devpoll.h presence... no
checking for devpoll.h... no
checking for MAXMINDDB... no
checking whether ccache_cc is Clang... no
checking whether pthreads work with "-pthread" and "-lpthread"... yes
checking for joinable pthread attribute... PTHREAD_CREATE_JOINABLE
checking whether more special flags are required for pthreads... no
checking for PTHREAD_PRIO_INHERIT... yes
checking for pthread_attr_getstacksize... yes
checking for pthread_attr_setstacksize... yes
checking for PTHREAD_MUTEX_ADAPTIVE_NP... using standard lock type
checking sched.h usability... yes
checking sched.h presence... yes
checking for sched.h... yes
checking for library containing sched_yield... none required
checking for sched_yield... yes
checking for pthread_yield... no
checking for pthread_yield_np... no
checking sys/cpuset.h usability... no
checking sys/cpuset.h presence... no
checking for sys/cpuset.h... no
checking sys/procset.h usability... no
checking sys/procset.h presence... no
checking for sys/procset.h... no
checking for pthread_setaffinity_np... yes
checking for cpuset_setaffinity... no
checking for processor_bind... no
checking for sched_setaffinity... yes
checking for pthread_setname_np... yes
checking for pthread_set_name_np... no
checking for pthread_np.h... no
checking for libuv... checking for LIBUV... yes
checking for uv_handle_get_data... yes
checking for uv_handle_set_data... yes
checking for uv_import... no
checking for uv_udp_connect... yes
checking for uv_translate_sys_error... yes
checking for uv_sleep... yes
checking for libnghttp2... checking for LIBNGHTTP2... yes
checking for flockfile... yes
checking for getc_unlocked... yes
checking for sysconf... yes
checking for OPENSSL... no
checking for include/openssl/ssl.h in /openwrt/staging_dir/target-mips_24kc_musl/usr... no
checking whether compiling and linking against OpenSSL works... no
configure: error: in `/openwrt/build_dir/target-mips_24kc_musl/bind-9.17.13':
configure: error: OpenSSL/LibreSSL not found
See `config.log' for more details
make[3]: *** [Makefile:266: /openwrt/build_dir/target-mips_24kc_musl/bind-9.17.13/.configured_1cda62df6c0c9dacd38158408a374076] Error 1
```
