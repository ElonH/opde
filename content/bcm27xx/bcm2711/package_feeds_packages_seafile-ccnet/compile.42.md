---
title: "compile.42"
date: 2021-06-29 09:27:20.668702
hidden: false
draft: false
weight: -42
---

build number: `42`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/seafile-ccnet/compile -j$(nproc) || make package/feeds/packages/seafile-ccnet/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-Makefile.patch using plaintext: 
patching file lib/Makefile.am

Applying ./patches/011-no-python-compile.patch using plaintext: 
patching file python/ccnet/Makefile.am

Applying ./patches/020-Remove-API-deprecated-in-openssl-1.1.patch using plaintext: 
patching file lib/rsa.c
patching file net/common/processors/keepalive-proc.c
patching file net/common/processors/keepalive2-proc.c
patching file net/common/processors/sendsessionkey-proc.c
patching file net/common/processors/sendsessionkey-v2-proc.c
patching file net/server/user-mgr.c
patching file tools/ccnet-init.c

Applying ./patches/030-uci-conf.patch using plaintext: 
patching file net/common/rpc-service.c
patching file net/server/ccnet-server.c
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-aarch64_cortex-a72_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/aclocal -I m4 -I . --force -I m4
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
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
configure.ac:22: installing './compile'
configure.ac:11: installing './missing'
lib/Makefile.am: installing './depcomp'
net/server/Makefile.am:18: warning: source file '../common/ccnet-db.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
automake: warning: possible forward-incompatibility.
automake: At least a source file is in a subdirectory, but the 'subdir-objects'
automake: automake option hasn't been enabled.  For now, the corresponding output
automake: object file(s) will be placed in the top-level directory.  However,
automake: this behaviour will change in future Automake versions: they will
automake: unconditionally cause object files to be placed in the same subdirectory
automake: of the corresponding sources.
automake: You are advised to start using 'subdir-objects' option throughout your
automake: project, to avoid future incompatibilities.
net/server/Makefile.am:18: warning: source file '../common/session.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/peer-mgr.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/packet-io.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/message.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/perm-mgr.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/log.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/peer.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/algorithms.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/handshake.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/processor.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/getgateway.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/connect-mgr.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/message-manager.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/proc-factory.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/ccnet-config.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/rpc-service.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/peermgr-message.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/processors/sendmsg-proc.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/processors/rcvmsg-proc.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/processors/rcvcmd-proc.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/processors/putpubinfo-proc.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/processors/getpubinfo-proc.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/processors/keepalive2-proc.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/processors/mqserver-proc.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/processors/service-proxy-proc.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/processors/service-stub-proc.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/processors/rpcserver-proc.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/processors/threaded-rpcserver-proc.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/processors/echo-proc.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/processors/sendsessionkey-proc.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/processors/recvsessionkey-proc.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/processors/sendsessionkey-v2-proc.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
net/server/Makefile.am:18: warning: source file '../common/processors/recvsessionkey-v2-proc.c' is in a subdirectory,
net/server/Makefile.am:18: but option 'subdir-objects' is disabled
autoreconf: Leaving directory `.'
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/aarch64
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for aarch64-openwrt-linux-strip... aarch64-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking build system type... x86_64-pc-linux-gnu
checking for aarch64-openwrt-linux-gcc... ccache_cc
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
checking for an ANSI C-conforming const... yes
checking whether make sets $(MAKE)... (cached) yes
checking host system type... aarch64-openwrt-linux-gnu
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache_cc... aarch64-openwrt-linux-musl-ld
checking if the linker (aarch64-openwrt-linux-musl-ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... aarch64-openwrt-linux-musl-gcc-nm
checking the name lister (aarch64-openwrt-linux-musl-gcc-nm) interface... BSD nm
checking whether ln -s works... yes
checking the maximum length of command line arguments... 3145728
checking whether the shell understands some XSI constructs... yes
checking whether the shell understands "+="... yes
checking how to convert x86_64-pc-linux-gnu file names to aarch64-openwrt-linux-gnu format... func_convert_file_noop
checking how to convert x86_64-pc-linux-gnu file names to toolchain format... func_convert_file_noop
checking for aarch64-openwrt-linux-musl-ld option to reload object files... -r
checking for aarch64-openwrt-linux-objdump... aarch64-openwrt-linux-musl-objdump
checking how to recognize dependent libraries... pass_all
checking for aarch64-openwrt-linux-dlltool... no
checking for dlltool... no
checking how to associate runtime and link libraries... printf %s\n
checking for aarch64-openwrt-linux-ar... aarch64-openwrt-linux-musl-gcc-ar
checking for archiver @FILE support... @
checking for aarch64-openwrt-linux-strip... (cached) aarch64-openwrt-linux-musl-strip
checking for aarch64-openwrt-linux-ranlib... aarch64-openwrt-linux-musl-gcc-ranlib
checking command to parse aarch64-openwrt-linux-musl-gcc-nm output from ccache_cc object... ok
checking for sysroot... no
checking for aarch64-openwrt-linux-mt... no
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
checking whether the ccache_cc linker (aarch64-openwrt-linux-musl-ld) supports shared libraries... yes
checking whether -lc should be explicitly linked in... no
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... yes
checking sys/ioctl.h usability... yes
checking sys/ioctl.h presence... yes
checking for sys/ioctl.h... yes
checking sys/time.h usability... yes
checking sys/time.h presence... yes
checking for sys/time.h... yes
checking stdarg.h usability... yes
checking stdarg.h presence... yes
checking for stdarg.h... yes
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking for WIN32... no
checking for Mac... no
checking for Linux... compile in linux
checking for uuid_generate in -luuid... yes
found library uuid
checking for pthread_create in -lpthread... yes
found library pthread
checking for sqlite3_open in -lsqlite3... yes
found library sqlite3
checking for SHA1_Init in -lcrypto... yes
found library crypto
checking pkg-config is at least version 0.9.0... yes
checking for SSL... yes
checking for GLIB2... no
configure: error: Package requirements (glib-2.0 >= 2.16.0) were not met:

Package 'glib-2.0', required by 'virtual:world', not found

Consider adjusting the PKG_CONFIG_PATH environment variable if you
installed software in a non-standard prefix.

Alternatively, you may set the environment variables GLIB2_CFLAGS
and GLIB2_LIBS to avoid the need to call pkg-config.
See the pkg-config man page for more details.
make[3]: *** [Makefile:100: /openwrt/build_dir/target-aarch64_cortex-a72_musl/ccnet-server-7.1.5-server/.configured_a17fb5ef857664f03cd0ce37cc5ea591] Error 1
```
