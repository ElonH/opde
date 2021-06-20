---
title: "compile.37"
date: 2021-06-20 22:27:32.412860
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
make package/feeds/packages/squid/compile -j$(nproc) || make package/feeds/packages/squid/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-glibc-compile.patch using plaintext: 
patching file src/tools.cc

Applying ./patches/010-no-buildbxxflags.patch using plaintext: 
patching file src/Makefile.am
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force 
autoreconf: configure.ac: tracing
autoreconf: configure.ac: adding subdirectory libltdl to autoreconf
autoreconf: Entering directory `libltdl'
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force -I m4
autoreconf: running: /openwrt/staging_dir/host/bin/libtoolize --install --force --ltdl
OpenWrt-libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, `../cfgaux'.
OpenWrt-libtoolize: linking file `../cfgaux/config.guess'
OpenWrt-libtoolize: linking file `../cfgaux/config.sub'
OpenWrt-libtoolize: linking file `../cfgaux/install-sh'
OpenWrt-libtoolize: linking file `../cfgaux/ltmain.sh'
OpenWrt-libtoolize: putting auxiliary files in `../cfgaux'.
OpenWrt-libtoolize: linking file `./config/compile'
OpenWrt-libtoolize: linking file `./config/config.guess'
OpenWrt-libtoolize: linking file `./config/config.sub'
OpenWrt-libtoolize: linking file `./config/depcomp'
OpenWrt-libtoolize: linking file `./config/install-sh'
OpenWrt-libtoolize: linking file `./config/missing'
OpenWrt-libtoolize: linking file `./config/ltmain.sh'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `m4'.
OpenWrt-libtoolize: linking file `m4/argz.m4'
OpenWrt-libtoolize: linking file `m4/libtool.m4'
OpenWrt-libtoolize: linking file `m4/ltdl.m4'
OpenWrt-libtoolize: linking file `m4/ltoptions.m4'
OpenWrt-libtoolize: linking file `m4/ltsugar.m4'
OpenWrt-libtoolize: linking file `m4/ltversion.m4'
OpenWrt-libtoolize: linking file `m4/lt~obsolete.m4'
OpenWrt-libtoolize: putting libltdl files in LT_CONFIG_LTDL_DIR, `.'.
OpenWrt-libtoolize: linking file `./COPYING.LIB'
OpenWrt-libtoolize: linking file `./README'
OpenWrt-libtoolize: linking file `./Makefile.am'
OpenWrt-libtoolize: linking file `./configure.ac'
OpenWrt-libtoolize: copying file `./aclocal.m4'
OpenWrt-libtoolize: linking file `./Makefile.in'
OpenWrt-libtoolize: linking file `./config-h.in'
OpenWrt-libtoolize: linking file `./configure'
OpenWrt-libtoolize: linking file `./argz_.h'
OpenWrt-libtoolize: linking file `./argz.c'
OpenWrt-libtoolize: linking file `./loaders/dld_link.c'
OpenWrt-libtoolize: linking file `./loaders/dlopen.c'
OpenWrt-libtoolize: linking file `./loaders/dyld.c'
OpenWrt-libtoolize: linking file `./loaders/load_add_on.c'
OpenWrt-libtoolize: linking file `./loaders/loadlibrary.c'
OpenWrt-libtoolize: linking file `./loaders/shl_load.c'
OpenWrt-libtoolize: linking file `./lt__dirent.c'
OpenWrt-libtoolize: linking file `./lt__strl.c'
OpenWrt-libtoolize: linking file `./libltdl/lt__alloc.h'
OpenWrt-libtoolize: linking file `./libltdl/lt__dirent.h'
OpenWrt-libtoolize: linking file `./libltdl/lt__glibc.h'
OpenWrt-libtoolize: linking file `./libltdl/lt__private.h'
OpenWrt-libtoolize: linking file `./libltdl/lt__strl.h'
OpenWrt-libtoolize: linking file `./libltdl/lt_dlloader.h'
OpenWrt-libtoolize: linking file `./libltdl/lt_error.h'
OpenWrt-libtoolize: linking file `./libltdl/lt_system.h'
OpenWrt-libtoolize: linking file `./libltdl/slist.h'
OpenWrt-libtoolize: linking file `./loaders/preopen.c'
OpenWrt-libtoolize: linking file `./lt__alloc.c'
OpenWrt-libtoolize: linking file `./lt_dlloader.c'
OpenWrt-libtoolize: linking file `./lt_error.c'
OpenWrt-libtoolize: linking file `./ltdl.c'
OpenWrt-libtoolize: linking file `./ltdl.h'
OpenWrt-libtoolize: linking file `./slist.c'
OpenWrt-libtoolize: Remember to add `LTDL_INIT' to configure.ac.
OpenWrt-libtoolize: Consider using `AC_CONFIG_AUX_DIR([config])' in configure.ac.
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
Makefile.am:113: warning: source file 'loaders/dld_link.c' is in a subdirectory,
Makefile.am:113: but option 'subdir-objects' is disabled
automake: warning: possible forward-incompatibility.
automake: At least a source file is in a subdirectory, but the 'subdir-objects'
automake: automake option hasn't been enabled.  For now, the corresponding output
automake: object file(s) will be placed in the top-level directory.  However,
automake: this behaviour will change in future Automake versions: they will
automake: unconditionally cause object files to be placed in the same subdirectory
automake: of the corresponding sources.
automake: You are advised to start using 'subdir-objects' option throughout your
automake: project, to avoid future incompatibilities.
Makefile.am:109: warning: source file 'loaders/dlopen.c' is in a subdirectory,
Makefile.am:109: but option 'subdir-objects' is disabled
Makefile.am:117: warning: source file 'loaders/dyld.c' is in a subdirectory,
Makefile.am:117: but option 'subdir-objects' is disabled
Makefile.am:67: warning: source file 'loaders/preopen.c' is in a subdirectory,
Makefile.am:67: but option 'subdir-objects' is disabled
Makefile.am:120: warning: source file 'loaders/load_add_on.c' is in a subdirectory,
Makefile.am:120: but option 'subdir-objects' is disabled
Makefile.am:123: warning: source file 'loaders/loadlibrary.c' is in a subdirectory,
Makefile.am:123: but option 'subdir-objects' is disabled
Makefile.am:126: warning: source file 'loaders/shl_load.c' is in a subdirectory,
Makefile.am:126: but option 'subdir-objects' is disabled
autoreconf: Leaving directory `libltdl'
OpenWrt-libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, `cfgaux'.
OpenWrt-libtoolize: linking file `cfgaux/config.guess'
OpenWrt-libtoolize: linking file `cfgaux/config.sub'
OpenWrt-libtoolize: linking file `cfgaux/install-sh'
OpenWrt-libtoolize: linking file `cfgaux/ltmain.sh'
OpenWrt-libtoolize: putting auxiliary files in `cfgaux'.
OpenWrt-libtoolize: linking file `libltdl/config/compile'
OpenWrt-libtoolize: linking file `libltdl/config/config.guess'
OpenWrt-libtoolize: linking file `libltdl/config/config.sub'
OpenWrt-libtoolize: linking file `libltdl/config/depcomp'
OpenWrt-libtoolize: linking file `libltdl/config/install-sh'
OpenWrt-libtoolize: linking file `libltdl/config/missing'
OpenWrt-libtoolize: linking file `libltdl/config/ltmain.sh'
OpenWrt-libtoolize: putting macros in `libltdl/m4'.
OpenWrt-libtoolize: linking file `libltdl/m4/argz.m4'
OpenWrt-libtoolize: linking file `libltdl/m4/libtool.m4'
OpenWrt-libtoolize: linking file `libltdl/m4/ltdl.m4'
OpenWrt-libtoolize: linking file `libltdl/m4/ltoptions.m4'
OpenWrt-libtoolize: linking file `libltdl/m4/ltsugar.m4'
OpenWrt-libtoolize: linking file `libltdl/m4/ltversion.m4'
OpenWrt-libtoolize: linking file `libltdl/m4/lt~obsolete.m4'
OpenWrt-libtoolize: putting libltdl files in `libltdl'.
OpenWrt-libtoolize: linking file `libltdl/COPYING.LIB'
OpenWrt-libtoolize: linking file `libltdl/README'
OpenWrt-libtoolize: linking file `libltdl/Makefile.am'
OpenWrt-libtoolize: linking file `libltdl/configure.ac'
OpenWrt-libtoolize: copying file `libltdl/aclocal.m4'
OpenWrt-libtoolize: linking file `libltdl/Makefile.in'
OpenWrt-libtoolize: linking file `libltdl/config-h.in'
OpenWrt-libtoolize: linking file `libltdl/configure'
OpenWrt-libtoolize: linking file `libltdl/argz_.h'
OpenWrt-libtoolize: linking file `libltdl/argz.c'
OpenWrt-libtoolize: linking file `libltdl/loaders/dld_link.c'
OpenWrt-libtoolize: linking file `libltdl/loaders/dlopen.c'
OpenWrt-libtoolize: linking file `libltdl/loaders/dyld.c'
OpenWrt-libtoolize: linking file `libltdl/loaders/load_add_on.c'
OpenWrt-libtoolize: linking file `libltdl/loaders/loadlibrary.c'
OpenWrt-libtoolize: linking file `libltdl/loaders/shl_load.c'
OpenWrt-libtoolize: linking file `libltdl/lt__dirent.c'
OpenWrt-libtoolize: linking file `libltdl/lt__strl.c'
OpenWrt-libtoolize: linking file `libltdl/libltdl/lt__alloc.h'
OpenWrt-libtoolize: linking file `libltdl/libltdl/lt__dirent.h'
OpenWrt-libtoolize: linking file `libltdl/libltdl/lt__glibc.h'
OpenWrt-libtoolize: linking file `libltdl/libltdl/lt__private.h'
OpenWrt-libtoolize: linking file `libltdl/libltdl/lt__strl.h'
OpenWrt-libtoolize: linking file `libltdl/libltdl/lt_dlloader.h'
OpenWrt-libtoolize: linking file `libltdl/libltdl/lt_error.h'
OpenWrt-libtoolize: linking file `libltdl/libltdl/lt_system.h'
OpenWrt-libtoolize: linking file `libltdl/libltdl/slist.h'
OpenWrt-libtoolize: linking file `libltdl/loaders/preopen.c'
OpenWrt-libtoolize: linking file `libltdl/lt__alloc.c'
OpenWrt-libtoolize: linking file `libltdl/lt_dlloader.c'
OpenWrt-libtoolize: linking file `libltdl/lt_error.c'
OpenWrt-libtoolize: linking file `libltdl/ltdl.c'
OpenWrt-libtoolize: linking file `libltdl/ltdl.h'
OpenWrt-libtoolize: linking file `libltdl/slist.c'
OpenWrt-libtoolize: Remember to add `LT_CONFIG_LTDL_DIR([libltdl])' to `configure.ac'.
OpenWrt-libtoolize: Consider using `AC_CONFIG_AUX_DIR([libltdl/config])' in configure.ac.
OpenWrt-libtoolize: Consider using `AC_CONFIG_MACRO_DIR([libltdl/m4])' in configure.ac.
OpenWrt-libtoolize: Consider adding `-I m4' to ACLOCAL_AMFLAGS in Makefile.am.
OpenWrt-libtoolize: `AC_PROG_RANLIB' is rendered obsolete by `LT_INIT'
doc/release-notes/Makefile.am:13: warning: '%'-style pattern rules are a GNU make extension
doc/release-notes/Makefile.am:22: warning: '%'-style pattern rules are a GNU make extension
doc/release-notes/Makefile.am:25: warning: '%'-style pattern rules are a GNU make extension
doc/release-notes/Makefile.am:30: warning: '%'-style pattern rules are a GNU make extension
autoreconf: Leaving directory `.'
configure: loading site script /openwrt/include/site/mips
configure: creating cache config.cache
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether UID '1000' is supported by ustar format... yes
checking whether GID '1000' is supported by ustar format... yes
checking how to create a ustar tar archive... gnutar
checking whether to enable maintainer-specific portions of Makefiles... no
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
checking whether we are using the GNU C++ compiler... yes
checking whether ccache_cxx accepts -g... yes
checking dependency style of ccache_cxx... gcc3
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
configure: CPU arch native optimization enabled: no
checking simplified host os... linux (version )
checking whether ccache_cxx supports C++11 features by default... yes
checking for mips-openwrt-linux-ranlib... mips-openwrt-linux-musl-gcc-ranlib
checking how to run the C preprocessor... ccache_cc -E
checking whether ln -s works... yes
checking for egrep... /openwrt/staging_dir/host/bin/egrep
checking for sh... /usr/bin/sh
checking for false... /usr/bin/false
checking for true... /usr/bin/true
checking for mv... /usr/bin/mv
checking for mkdir... /usr/bin/mkdir
checking for ln... /usr/bin/ln
checking for chmod... /usr/bin/chmod
checking for tr... /usr/bin/tr
checking for rm... /usr/bin/rm
checking pkg-config is at least version 0.9.0... yes
checking for perl... /openwrt/staging_dir/host/bin/perl
checking for pod2man... /usr/bin/pod2man
checking for linuxdoc... /usr/bin/false
configure: strict error checking enabled: yes
checking whether to use loadable modules... yes
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for fgrep... /usr/bin/fgrep
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
checking for mips-openwrt-linux-ar... mips-openwrt-linux-musl-gcc-ar
checking for archiver @FILE support... @
checking for mips-openwrt-linux-strip... (cached) mips-openwrt-linux-musl-strip
checking for mips-openwrt-linux-ranlib... (cached) mips-openwrt-linux-musl-gcc-ranlib
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
checking how to run the C++ preprocessor... ccache_cxx -E
checking for ld used by ccache_cxx... mips-openwrt-linux-musl-ld
checking if the linker (mips-openwrt-linux-musl-ld) is GNU ld... yes
checking whether the ccache_cxx linker (mips-openwrt-linux-musl-ld) supports shared libraries... yes
checking for ccache_cxx option to produce PIC... -fPIC -DPIC
checking if ccache_cxx PIC flag -fPIC -DPIC works... yes
checking if ccache_cxx static flag -static works... yes
checking if ccache_cxx supports -c -o file.o... yes
checking if ccache_cxx supports -c -o file.o... (cached) yes
checking whether the ccache_cxx linker (mips-openwrt-linux-musl-ld) supports shared libraries... yes
checking dynamic linker characteristics... (cached) GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking which extension is used for runtime loadable modules... .so
checking which variable specifies run-time module search path... LD_LIBRARY_PATH
checking for the default library search path... /lib /usr/lib /usr/local/lib /usr/local/lib/x86_64-linux-gnu /lib/x86_64-linux-gnu /usr/lib/x86_64-linux-gnu /lib32 /usr/lib32 /libx32 /usr/libx32 
checking for library containing dlopen... none required
checking for dlerror... yes
checking for shl_load... (cached) no
checking for shl_load in -ldld... (cached) no
checking for dld_link in -ldld... no
checking for _ prefix in compiled symbols... no
checking whether deplibs are loaded by dlopen... yes
checking for argz.h... no
checking for error_t... no
checking for argz_add... no
checking for argz_append... no
checking for argz_count... no
checking for argz_create_sep... no
checking for argz_insert... no
checking for argz_next... no
checking for argz_stringify... no
checking whether libtool supports -dlopen/-dlpreopen... yes
checking for ltdl.h... yes
checking whether lt_dlinterface_register is declared... yes
checking for lt_dladvise_preload in -lltdl... yes
checking where to find libltdl headers... 
checking where to find libltdl library... -lltdl
checking for unistd.h... yes
checking for dl.h... no
checking for sys/dl.h... no
checking for dld.h... no
checking for mach-o/dyld.h... no
checking for dirent.h... yes
checking for closedir... yes
checking for opendir... yes
checking for readdir... yes
checking for strlcat... yes
checking for strlcpy... yes
checking for library containing dlopen... (cached) none required
checking for dlerror... (cached) yes
checking for shl_load... (cached) no
checking for shl_load in -ldld... (cached) no
checking for dld_link in -ldld... (cached) no
checking what kind of compiler we're using... gcc
checking for compiler variant... gcc
checking whether compiler requires -Werror -Wno-deprecated-register... no
configure: inlining optimizations enabled: yes
configure: cbdata debugging enabled: no
configure: xmalloc stats display: no
configure: With dl
checking whether linking without -latomic works... yes
checking for library containing shm_open... none required
checking for DiskIO modules to be enabled...  AIO Blocking DiskDaemon DiskThreads IpcIo Mmapped
checking aio.h usability... yes
checking aio.h presence... yes
checking for aio.h... yes
checking for aio_read in -lrt... yes
configure: Native POSIX AIO support detected.
configure: Enabling AIO DiskIO module
configure: Enabling Blocking DiskIO module
configure: Enabling DiskDaemon DiskIO module
checking for pthread_create  in -lpthread... yes
configure: Enabling DiskThreads DiskIO module
configure: Enabling IpcIo DiskIO module
configure: Enabling Mmapped DiskIO module
configure: IO Modules built:  AIO Blocking DiskDaemon DiskThreads IpcIo Mmapped
checking for available StoreIO modules...  aufs diskd rock ufs
configure: Store modules built:  aufs diskd rock ufs
configure: Removal policies to build: lru
configure: Delay pools enabled
configure: Disabling ESI processor. libxml2 and libexpat not found.
checking whether to support eCAP... no, explicitly
configure: Web Cache Coordination Protocol enabled: yes
configure: Web Cache Coordination V2 Protocol enabled: yes
configure: Kill parent on shutdown hack enabled: yes
configure: SNMP support enabled: no
checking for windows.h... no
checking for sys/sockio.h... no
checking for sys/param.h... yes
checking for net/if_arp.h... yes
checking for net/route.h... yes
checking for net/if_dl.h... no
checking for sys/sysctl.h... no
configure: EUI (MAC address) controls enabled: yes
configure: HTCP support enabled: yes
configure: Using Nettle cryptographic library: no
checking for crypt in -lcrypt... yes
checking for MD5Init in -lmd5... no
configure: GnuTLS library support: no  
checking openssl/asn1.h usability... no
checking openssl/asn1.h presence... no
checking for openssl/asn1.h... no
checking openssl/bio.h usability... no
checking openssl/bio.h presence... no
checking for openssl/bio.h... no
checking openssl/bn.h usability... no
checking openssl/bn.h presence... no
checking for openssl/bn.h... no
checking openssl/crypto.h usability... no
checking openssl/crypto.h presence... no
checking for openssl/crypto.h... no
checking openssl/dh.h usability... no
checking openssl/dh.h presence... no
checking for openssl/dh.h... no
checking openssl/err.h usability... no
checking openssl/err.h presence... no
checking for openssl/err.h... no
checking openssl/evp.h usability... no
checking openssl/evp.h presence... no
checking for openssl/evp.h... no
checking openssl/lhash.h usability... no
checking openssl/lhash.h presence... no
checking for openssl/lhash.h... no
checking openssl/md5.h usability... no
checking openssl/md5.h presence... no
checking for openssl/md5.h... no
checking openssl/opensslv.h usability... no
checking openssl/opensslv.h presence... no
checking for openssl/opensslv.h... no
checking openssl/rsa.h usability... no
checking openssl/rsa.h presence... no
checking for openssl/rsa.h... no
checking openssl/ssl.h usability... no
checking openssl/ssl.h presence... no
checking for openssl/ssl.h... no
checking openssl/x509.h usability... no
checking openssl/x509.h presence... no
checking for openssl/x509.h... no
checking openssl/x509v3.h usability... no
checking openssl/x509v3.h presence... no
checking for openssl/x509v3.h... no
checking openssl/engine.h usability... no
checking openssl/engine.h presence... no
checking for openssl/engine.h... no
checking openssl/txt_db.h usability... no
checking openssl/txt_db.h presence... no
checking for openssl/txt_db.h... no
checking for LIBOPENSSL... no
checking for CRYPTO_new_ex_data in -lcrypto... no
configure: error: library 'crypto' is required for OpenSSL
make[3]: *** [Makefile:158: /openwrt/build_dir/target-mips_24kc_musl/squid-4.14/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
