---
title: "compile.40"
date: 2021-06-22 10:50:44.057860
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
make package/feeds/packages/boinc/compile -j$(nproc) || make package/feeds/packages/boinc/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-avoidExtraDependencies using plaintext: 
patching file configure.ac

Applying ./patches/002-hosttypeRespected using plaintext: 
patching file client/cs_platforms.cpp
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force -I m4
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
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
configure.ac:54: installing './compile'
configure.ac:29: installing './missing'
api/Makefile.am:22: warning: source file '$(top_srcdir)/samples/image_libs/bmplib.cpp' is in a subdirectory,
api/Makefile.am:22: but option 'subdir-objects' is disabled
automake: warning: possible forward-incompatibility.
automake: At least a source file is in a subdirectory, but the 'subdir-objects'
automake: automake option hasn't been enabled.  For now, the corresponding output
automake: object file(s) will be placed in the top-level directory.  However,
automake: this behaviour will change in future Automake versions: they will
automake: unconditionally cause object files to be placed in the same subdirectory
automake: of the corresponding sources.
automake: You are advised to start using 'subdir-objects' option throughout your
automake: project, to avoid future incompatibilities.
api/Makefile.am:22: warning: source file '$(top_srcdir)/samples/image_libs/tgalib.cpp' is in a subdirectory,
api/Makefile.am:22: but option 'subdir-objects' is disabled
api/Makefile.am: installing './depcomp'
client/Makefile.am:4: warning: ':='-style assignments are not portable
client/Makefile.am:4: warning: filter-out -mfpu=vfpv3-d16,$(CXXFLAGS: non-POSIX variable name
client/Makefile.am:4: (probably a GNU make extension)
client/Makefile.am:126: warning: filter-out -mfpu=vfpv3-d16,$(boinc_client_CXXFLAGS: non-POSIX variable name
client/Makefile.am:126: (probably a GNU make extension)
client/Makefile.am:4: warning: 'CXXFLAGS' is a user variable, you should not override it;
client/Makefile.am:4: use 'AM_CXXFLAGS' instead
clientgui/Makefile.am:26: warning: source file 'common/wxPieCtrl.cpp' is in a subdirectory,
clientgui/Makefile.am:26: but option 'subdir-objects' is disabled
clientgui/Makefile.am:26: warning: source file 'gtk/taskbarex.cpp' is in a subdirectory,
clientgui/Makefile.am:26: but option 'subdir-objects' is disabled
lib/Makefile.am:96: warning: source file 'mac/mac_backtrace.cpp' is in a subdirectory,
lib/Makefile.am:96: but option 'subdir-objects' is disabled
lib/Makefile.am:96: warning: source file 'mac/mac_spawn.cpp' is in a subdirectory,
lib/Makefile.am:96: but option 'subdir-objects' is disabled
lib/Makefile.am:96: warning: source file 'mac/QBacktrace.c' is in a subdirectory,
lib/Makefile.am:96: but option 'subdir-objects' is disabled
lib/Makefile.am:96: warning: source file 'mac/QCrashReport.c' is in a subdirectory,
lib/Makefile.am:96: but option 'subdir-objects' is disabled
lib/Makefile.am:96: warning: source file 'mac/QMachOImage.c' is in a subdirectory,
lib/Makefile.am:96: but option 'subdir-objects' is disabled
lib/Makefile.am:96: warning: source file 'mac/QMachOImageList.c' is in a subdirectory,
lib/Makefile.am:96: but option 'subdir-objects' is disabled
lib/Makefile.am:96: warning: source file 'mac/QSymbols.c' is in a subdirectory,
lib/Makefile.am:96: but option 'subdir-objects' is disabled
lib/Makefile.am:96: warning: source file 'mac/QTaskMemory.c' is in a subdirectory,
lib/Makefile.am:96: but option 'subdir-objects' is disabled
lib/Makefile.am:96: warning: source file 'mac/mac_branding.cpp' is in a subdirectory,
lib/Makefile.am:96: but option 'subdir-objects' is disabled
sched/Makefile.am:11: warning: source file '../db/boinc_db.cpp' is in a subdirectory,
sched/Makefile.am:11: but option 'subdir-objects' is disabled
sched/Makefile.am:11: warning: source file '../db/db_base.cpp' is in a subdirectory,
sched/Makefile.am:11: but option 'subdir-objects' is disabled
sched/Makefile.am:11: warning: source file '../tools/process_result_template.cpp' is in a subdirectory,
sched/Makefile.am:11: but option 'subdir-objects' is disabled
sched/Makefile.am:11: warning: source file '../tools/process_input_template.cpp' is in a subdirectory,
sched/Makefile.am:11: but option 'subdir-objects' is disabled
sched/Makefile.am:11: warning: source file '../tools/backend_lib.cpp' is in a subdirectory,
sched/Makefile.am:11: but option 'subdir-objects' is disabled
sched/Makefile.am:157: warning: source file '../vda/sched_vda.cpp' is in a subdirectory,
sched/Makefile.am:157: but option 'subdir-objects' is disabled
sched/Makefile.am:198: warning: source file '../lib/synch.cpp' is in a subdirectory,
sched/Makefile.am:198: but option 'subdir-objects' is disabled
tools/Makefile.am:62: warning: source file '../lib/remote_submit.cpp' is in a subdirectory,
tools/Makefile.am:62: but option 'subdir-objects' is disabled
zip/Makefile.am:21: warning: source file './unzip/api.c' is in a subdirectory,
zip/Makefile.am:21: but option 'subdir-objects' is disabled
zip/Makefile.am:21: warning: source file './unzip/apihelp.c' is in a subdirectory,
zip/Makefile.am:21: but option 'subdir-objects' is disabled
zip/Makefile.am:21: warning: source file './unzip/crc32.c' is in a subdirectory,
zip/Makefile.am:21: but option 'subdir-objects' is disabled
zip/Makefile.am:21: warning: source file './unzip/explode.c' is in a subdirectory,
zip/Makefile.am:21: but option 'subdir-objects' is disabled
zip/Makefile.am:21: warning: source file './unzip/extract.c' is in a subdirectory,
zip/Makefile.am:21: but option 'subdir-objects' is disabled
zip/Makefile.am:21: warning: source file './unzip/fileio.c' is in a subdirectory,
zip/Makefile.am:21: but option 'subdir-objects' is disabled
zip/Makefile.am:21: warning: source file './unzip/globals.c' is in a subdirectory,
zip/Makefile.am:21: but option 'subdir-objects' is disabled
zip/Makefile.am:21: warning: source file './unzip/inflate.c' is in a subdirectory,
zip/Makefile.am:21: but option 'subdir-objects' is disabled
zip/Makefile.am:21: warning: source file './unzip/list.c' is in a subdirectory,
zip/Makefile.am:21: but option 'subdir-objects' is disabled
zip/Makefile.am:21: warning: source file './unzip/match.c' is in a subdirectory,
zip/Makefile.am:21: but option 'subdir-objects' is disabled
zip/Makefile.am:21: warning: source file './unzip/process.c' is in a subdirectory,
zip/Makefile.am:21: but option 'subdir-objects' is disabled
zip/Makefile.am:21: warning: source file './unzip/ttyio.c' is in a subdirectory,
zip/Makefile.am:21: but option 'subdir-objects' is disabled
zip/Makefile.am:21: warning: source file './unzip/unreduce.c' is in a subdirectory,
zip/Makefile.am:21: but option 'subdir-objects' is disabled
zip/Makefile.am:21: warning: source file './unzip/unshrink.c' is in a subdirectory,
zip/Makefile.am:21: but option 'subdir-objects' is disabled
zip/Makefile.am:21: warning: source file './unzip/unzip.c' is in a subdirectory,
zip/Makefile.am:21: but option 'subdir-objects' is disabled
zip/Makefile.am:21: warning: source file './unzip/zipinfo.c' is in a subdirectory,
zip/Makefile.am:21: but option 'subdir-objects' is disabled
zip/Makefile.am:21: warning: source file './zip/deflate.c' is in a subdirectory,
zip/Makefile.am:21: but option 'subdir-objects' is disabled
zip/Makefile.am:21: warning: source file './zip/trees.c' is in a subdirectory,
zip/Makefile.am:21: but option 'subdir-objects' is disabled
zip/Makefile.am:21: warning: source file './zip/util.c' is in a subdirectory,
zip/Makefile.am:21: but option 'subdir-objects' is disabled
zip/Makefile.am:21: warning: source file './zip/z_fileio.c' is in a subdirectory,
zip/Makefile.am:21: but option 'subdir-objects' is disabled
zip/Makefile.am:21: warning: source file './zip/z_globals.c' is in a subdirectory,
zip/Makefile.am:21: but option 'subdir-objects' is disabled
zip/Makefile.am:21: warning: source file './zip/zip.c' is in a subdirectory,
zip/Makefile.am:21: but option 'subdir-objects' is disabled
zip/Makefile.am:21: warning: source file './zip/zipfile.c' is in a subdirectory,
zip/Makefile.am:21: but option 'subdir-objects' is disabled
zip/Makefile.am:21: warning: source file './zip/zipup.c' is in a subdirectory,
zip/Makefile.am:21: but option 'subdir-objects' is disabled
zip/Makefile.am:49: warning: source file './unzip/win32/nt.c' is in a subdirectory,
zip/Makefile.am:49: but option 'subdir-objects' is disabled
zip/Makefile.am:49: warning: source file './unzip/win32/win32.c' is in a subdirectory,
zip/Makefile.am:49: but option 'subdir-objects' is disabled
zip/Makefile.am:49: warning: source file './zip/win32/win32_boinc.c' is in a subdirectory,
zip/Makefile.am:49: but option 'subdir-objects' is disabled
zip/Makefile.am:49: warning: source file './zip/win32/win32i64.c' is in a subdirectory,
zip/Makefile.am:49: but option 'subdir-objects' is disabled
zip/Makefile.am:49: warning: source file './zip/win32/z_nt.c' is in a subdirectory,
zip/Makefile.am:49: but option 'subdir-objects' is disabled
zip/Makefile.am:49: warning: source file './zip/win32/win32zip.c' is in a subdirectory,
zip/Makefile.am:49: but option 'subdir-objects' is disabled
zip/Makefile.am:57: warning: source file './unzip/unix/unix.c' is in a subdirectory,
zip/Makefile.am:57: but option 'subdir-objects' is disabled
zip/Makefile.am:57: warning: source file './zip/unix/z_unix.c' is in a subdirectory,
zip/Makefile.am:57: but option 'subdir-objects' is disabled
autoreconf: Leaving directory `.'
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/mips
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking target system type... mips-openwrt-linux-gnu
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... /usr/bin/gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether make supports nested variables... (cached) yes
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
checking for mips-openwrt-linux-g++... mips-openwrt-linux-g++
checking whether we are using the GNU Objective C++ compiler... no
checking whether mips-openwrt-linux-g++ accepts -g... no
checking dependency style of mips-openwrt-linux-g++... gcc3
checking how to run the C preprocessor... ccache_cc -E
checking whether make sets $(MAKE)... (cached) yes
checking for ln... /usr/bin/ln
checking whether '/usr/bin/ln' works... yes
checking whether ln -s works... yes
checking whether 'ln -s' really works or whether I'm deluding myself... it works
checking if C compiler supports -Wall... yes
checking if C++ compiler supports -Wall... yes
--- Configuring BOINC 7.16.16 (Release) ---
--- Build Components: (client libraries) ---
checking for docbook2x-man... no
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
checking whether we are compiling for cygwin... no
checking for winsock2.h... (cached) no
checking for winsock.h... (cached) no
checking windows.h usability... no
checking windows.h presence... no
checking for windows.h... no
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking dependency style of ccache_cc... gcc3
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
checking for mips-openwrt-linux-dlltool... dlltool
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
checking whether to build static libraries... yes
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
checking default bitness of compiler... 32
checking boinc platform... mips-openwrt-linux-musl
checking alternate boinc platform... mips-ath79-router-openwrt-musl
checking library extension... a
checking shared object extension... so
checking for pkg-config... /openwrt/staging_dir/host/bin/pkg-config
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
checking for dlopen in -ldl... yes
checking for gzopen in -lz... yes
checking for openssl... yes
OpenSSL found in /usr
checking for gawk... (cached) /usr/bin/gawk
checking for curl-config... no
checking whether libcurl is usable... no
configure: error: 
================================================================================
ERROR: could not find (recent enough) development-libs for libcurl.

  If libcurl-dev is installed on your system, make sure that the script
  'curl-config' is found in your PATH, and that
  'curl-config --version' gives something recent enough (see above).

  You can download libcurl from: http://curl.haxx.se/

================================================================================
        
make[3]: *** [Makefile:87: /openwrt/build_dir/target-mips_24kc_musl/boinc-client_release-7.16-7.16.16/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
