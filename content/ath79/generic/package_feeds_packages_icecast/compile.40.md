---
title: "compile.40"
date: 2021-06-22 10:47:21.984939
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
make package/feeds/packages/icecast/compile -j$(nproc) || make package/feeds/packages/icecast/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-icecast-2.4.0-tremor.patch using plaintext: 
patching file m4/ogg.m4
patching file m4/vorbis.m4
patching file src/format_vorbis.c

Applying ./patches/005-no_examples_doc_win32.patch using plaintext: 
patching file Makefile.am

Applying ./patches/010-fix_libcurl_test_crap.patch using plaintext: 
patching file m4/xiph_curl.m4

Applying ./patches/015-add_with-openssl_option.patch using plaintext: 
patching file m4/xiph_openssl.m4

Applying ./patches/020-icecast_config_for_openwrt.patch using plaintext: 
patching file conf/icecast.xml.in
autoreconf: Entering directory `.'
autoreconf: configure.in: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force -I m4
aclocal.real: warning: autoconf input should be named 'configure.ac', not 'configure.in'
configure.in:105: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body
../../lib/autoconf/lang.m4:193: AC_LANG_CONFTEST is expanded from...
../../lib/autoconf/general.m4:2590: _AC_COMPILE_IFELSE is expanded from...
../../lib/autoconf/general.m4:2606: AC_COMPILE_IFELSE is expanded from...
m4/xiph_curl.m4:6: XIPH_PATH_CURL is expanded from...
configure.in:105: the top level
autoreconf: configure.in: tracing
configure.in:105: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body
../../lib/autoconf/lang.m4:193: AC_LANG_CONFTEST is expanded from...
../../lib/autoconf/general.m4:2590: _AC_COMPILE_IFELSE is expanded from...
../../lib/autoconf/general.m4:2606: AC_COMPILE_IFELSE is expanded from...
m4/xiph_curl.m4:6: XIPH_PATH_CURL is expanded from...
configure.in:105: the top level
autoreconf: running: /openwrt/staging_dir/host/bin/libtoolize --install --force
OpenWrt-libtoolize: putting auxiliary files in `.'.
OpenWrt-libtoolize: linking file `./config.guess'
OpenWrt-libtoolize: linking file `./config.sub'
OpenWrt-libtoolize: linking file `./install-sh'
OpenWrt-libtoolize: linking file `./ltmain.sh'
OpenWrt-libtoolize: putting macros in `m4'.
OpenWrt-libtoolize: linking file `m4/libtool.m4'
OpenWrt-libtoolize: linking file `m4/ltoptions.m4'
OpenWrt-libtoolize: linking file `m4/ltsugar.m4'
OpenWrt-libtoolize: linking file `m4/ltversion.m4'
OpenWrt-libtoolize: linking file `m4/lt~obsolete.m4'
OpenWrt-libtoolize: Consider adding `AC_CONFIG_MACRO_DIR([m4])' to configure.in and
OpenWrt-libtoolize: rerunning libtoolize, to keep the correct libtool macros in-tree.
aclocal.real: warning: autoconf input should be named 'configure.ac', not 'configure.in'
configure.in:105: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body
../../lib/autoconf/lang.m4:193: AC_LANG_CONFTEST is expanded from...
../../lib/autoconf/general.m4:2590: _AC_COMPILE_IFELSE is expanded from...
../../lib/autoconf/general.m4:2606: AC_COMPILE_IFELSE is expanded from...
m4/xiph_curl.m4:6: XIPH_PATH_CURL is expanded from...
configure.in:105: the top level
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
configure.in:105: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body
../../lib/autoconf/lang.m4:193: AC_LANG_CONFTEST is expanded from...
../../lib/autoconf/general.m4:2590: _AC_COMPILE_IFELSE is expanded from...
../../lib/autoconf/general.m4:2606: AC_COMPILE_IFELSE is expanded from...
m4/xiph_curl.m4:6: XIPH_PATH_CURL is expanded from...
configure.in:105: the top level
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
configure.in:105: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body
../../lib/autoconf/lang.m4:193: AC_LANG_CONFTEST is expanded from...
../../lib/autoconf/general.m4:2590: _AC_COMPILE_IFELSE is expanded from...
../../lib/autoconf/general.m4:2606: AC_COMPILE_IFELSE is expanded from...
m4/xiph_curl.m4:6: XIPH_PATH_CURL is expanded from...
configure.in:105: the top level
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
automake: warning: autoconf input should be named 'configure.ac', not 'configure.in'
configure.in:105: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body
../../lib/autoconf/lang.m4:193: AC_LANG_CONFTEST is expanded from...
../../lib/autoconf/general.m4:2590: _AC_COMPILE_IFELSE is expanded from...
../../lib/autoconf/general.m4:2606: AC_COMPILE_IFELSE is expanded from...
m4/xiph_curl.m4:6: XIPH_PATH_CURL is expanded from...
configure.in:105: the top level
automake: warning: autoconf input should be named 'configure.ac', not 'configure.in'
src/avl/Makefile.am:13: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/httpp/Makefile.am:12: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/net/Makefile.am:13: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/thread/Makefile.am:13: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
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
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache_cc... mips-openwrt-linux-musl-ld
checking if the linker (mips-openwrt-linux-musl-ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... mips-openwrt-linux-musl-gcc-nm
checking the name lister (mips-openwrt-linux-musl-gcc-nm) interface... BSD nm
checking whether ln -s works... yes
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
checking for mips-openwrt-linux-ranlib... mips-openwrt-linux-musl-gcc-ranlib
checking command to parse mips-openwrt-linux-musl-gcc-nm output from ccache_cc object... ok
checking for sysroot... no
checking for mips-openwrt-linux-mt... no
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
checking whether the ccache_cc linker (mips-openwrt-linux-musl-ld) supports shared libraries... yes
checking whether -lc should be explicitly linked in... no
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... yes
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking for ANSI C header files... (cached) yes
checking whether time.h and sys/time.h may both be included... yes
checking alloca.h usability... yes
checking alloca.h presence... yes
checking for alloca.h... yes
checking sys/timeb.h usability... yes
checking sys/timeb.h presence... yes
checking for sys/timeb.h... yes
checking for pwd.h... yes
checking for unistd.h... (cached) yes
checking for grp.h... yes
checking for sys/types.h... (cached) yes
checking for setuid... yes
checking for chroot... yes
checking for chown... yes
checking for strcasestr... yes
checking for __func__... yes
checking for localtime_r... yes
checking for poll... yes
checking for gettimeofday... (cached) yes
checking for ftime... yes
checking for library containing nanosleep... none required
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking for socklen_t... yes
checking for va_copy... va_copy
checking sys/select.h usability... yes
checking sys/select.h presence... yes
checking for sys/select.h... yes
checking sys/uio.h usability... yes
checking sys/uio.h presence... yes
checking for sys/uio.h... yes
checking winsock2.h usability... no
checking winsock2.h presence... no
checking for winsock2.h... no
checking for library containing sethostent... none required
checking for library containing getnameinfo... none required
checking for endhostent... yes
checking for getaddrinfo... (cached) yes
checking for inet_aton... yes
checking for writev... yes
checking for struct sockaddr_storage.ss_family... yes
checking for inet_pton... yes
checking for xsltSaveResultToString... yes
checking for Ogg... cross compiling; assumed OK... 
yes
checking for libvorbis... Theora support disabled by request
Speex support disabled by request
checking for kate_decode_init in -lkate... no
checking for the pthreads library -lpthreads... no
checking whether pthreads work without any flags... yes
checking for joinable pthread attribute... PTHREAD_CREATE_JOINABLE
checking if more special flags are required for pthreads... no
checking for pthread_spin_lock... yes
configure: error: /openwrt/staging_dir/target-mips_24kc_musl/usr/bin/curl-config cannot be executed
make[3]: *** [Makefile:86: /openwrt/build_dir/target-mips_24kc_musl/icecast-2.4.4/.configured_a17fb5ef857664f03cd0ce37cc5ea591] Error 1
```
