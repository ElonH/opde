---
title: "compile.41"
date: 2021-06-23 23:13:13.733149
hidden: false
draft: false
weight: -41
---

build number: `41`

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
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-x86_64_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal -I m4 -I . --force -I m4
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
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-x86_64_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-x86_64_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
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
configure: loading site script /openwrt/include/site/x86_64
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for x86_64-openwrt-linux-strip... x86_64-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking build system type... x86_64-pc-linux-gnu
checking for x86_64-openwrt-linux-gcc... ccache_cc
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
checking host system type... x86_64-openwrt-linux-gnu
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache_cc... x86_64-openwrt-linux-musl-ld
checking if the linker (x86_64-openwrt-linux-musl-ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... x86_64-openwrt-linux-musl-gcc-nm
checking the name lister (x86_64-openwrt-linux-musl-gcc-nm) interface... BSD nm
checking whether ln -s works... yes
checking the maximum length of command line arguments... 3145728
checking whether the shell understands some XSI constructs... yes
checking whether the shell understands "+="... yes
checking how to convert x86_64-pc-linux-gnu file names to x86_64-openwrt-linux-gnu format... func_convert_file_noop
checking how to convert x86_64-pc-linux-gnu file names to toolchain format... func_convert_file_noop
checking for x86_64-openwrt-linux-musl-ld option to reload object files... -r
checking for x86_64-openwrt-linux-objdump... x86_64-openwrt-linux-musl-objdump
checking how to recognize dependent libraries... pass_all
checking for x86_64-openwrt-linux-dlltool... no
checking for dlltool... no
checking how to associate runtime and link libraries... printf %s\n
checking for x86_64-openwrt-linux-ar... x86_64-openwrt-linux-musl-gcc-ar
checking for archiver @FILE support... @
checking for x86_64-openwrt-linux-strip... (cached) x86_64-openwrt-linux-musl-strip
checking for x86_64-openwrt-linux-ranlib... x86_64-openwrt-linux-musl-gcc-ranlib
checking command to parse x86_64-openwrt-linux-musl-gcc-nm output from ccache_cc object... ok
checking for sysroot... no
checking for x86_64-openwrt-linux-mt... no
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
checking whether the ccache_cc linker (x86_64-openwrt-linux-musl-ld -m elf_x86_64) supports shared libraries... yes
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
checking for GLIB2... yes
checking for GOBJECT... yes
checking for SEARPC... yes
checking for LIBEVENT... yes
checking for MySQL... ./configure: line 9915: /openwrt/staging_dir/target-x86_64_musl/usr/bin/mysql_config: No such file or directory
./configure: line 9916: /openwrt/staging_dir/target-x86_64_musl/usr/bin/mysql_config: No such file or directory

checking whether /openwrt/staging_dir/hostpkg/bin/python3.9 version is >= 2.6... yes
checking for /openwrt/staging_dir/hostpkg/bin/python3.9 version... 3.9
checking for /openwrt/staging_dir/hostpkg/bin/python3.9 platform... linux
checking for /openwrt/staging_dir/hostpkg/bin/python3.9 script directory... ${prefix}/lib/python3.9/site-packages
checking for /openwrt/staging_dir/hostpkg/bin/python3.9 extension module directory... ${exec_prefix}/lib/python3.9/site-packages
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating Makefile
config.status: creating libccnet.pc
config.status: creating net/Makefile
config.status: creating net/server/Makefile
config.status: creating net/common/Makefile
config.status: creating lib/Makefile
config.status: creating tools/Makefile
config.status: creating include/Makefile
config.status: creating include/ccnet/Makefile
config.status: creating python/Makefile
config.status: creating python/ccnet/Makefile
config.status: creating config.h
config.status: executing depfiles commands
config.status: executing libtool commands
configure: WARNING: unrecognized options: --disable-nls
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ccnet-server-7.1.5-server'
make  all-recursive
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ccnet-server-7.1.5-server'
Making all in include
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ccnet-server-7.1.5-server/include'
Making all in ccnet
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ccnet-server-7.1.5-server/include/ccnet'
make[7]: Nothing to be done for 'all'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ccnet-server-7.1.5-server/include/ccnet'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ccnet-server-7.1.5-server/include'
make[7]: Nothing to be done for 'all-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ccnet-server-7.1.5-server/include'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ccnet-server-7.1.5-server/include'
Making all in lib
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ccnet-server-7.1.5-server/lib'
/openwrt/rules.mk:450: warning: overriding recipe for target 'check'
Makefile:847: warning: ignoring old recipe for target 'check'
[libsearpc]: generating rpc header files
/openwrt/staging_dir/hostpkg/bin/python3.9 "/openwrt/staging_dir/target-x86_64_musl/usr/bin/searpc-codegen.py" ../lib/rpc_table.py
loaded func_table from /openwrt/build_dir/target-x86_64_musl/ccnet-server-7.1.5-server/lib/rpc_table.py
[libsearpc]: done
rm -f ccnetobj.c
valac -C --pkg posix ccnetobj.vala
rm -f ccnet-object.h
valac --pkg posix ccnetobj.vala -C -H ccnet-object.h
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ccnet-server-7.1.5-server/lib'
/openwrt/rules.mk:450: warning: overriding recipe for target 'check'
Makefile:847: warning: ignoring old recipe for target 'check'
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT libccnet_la-ccnet-client.lo -MD -MP -MF .deps/libccnet_la-ccnet-client.Tpo -c -o libccnet_la-ccnet-client.lo `test -f 'ccnet-client.c' || echo './'`ccnet-client.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-ccnet-client.lo -MD -MP -MF .deps/libccnet_la-ccnet-client.Tpo -c ccnet-client.c  -fPIC -DPIC -o .libs/libccnet_la-ccnet-client.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
ccnet-client.c:559:13: warning: 'handle_packet' defined but not used [-Wunused-function]
 static void handle_packet (ccnet_packet *packet, void *vclient)
             ^~~~~~~~~~~~~
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-ccnet-client.lo -MD -MP -MF .deps/libccnet_la-ccnet-client.Tpo -c ccnet-client.c -o libccnet_la-ccnet-client.o >/dev/null 2>&1
mv -f .deps/libccnet_la-ccnet-client.Tpo .deps/libccnet_la-ccnet-client.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT libccnet_la-packet-io.lo -MD -MP -MF .deps/libccnet_la-packet-io.Tpo -c -o libccnet_la-packet-io.lo `test -f 'packet-io.c' || echo './'`packet-io.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-packet-io.lo -MD -MP -MF .deps/libccnet_la-packet-io.Tpo -c packet-io.c  -fPIC -DPIC -o .libs/libccnet_la-packet-io.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-packet-io.lo -MD -MP -MF .deps/libccnet_la-packet-io.Tpo -c packet-io.c -o libccnet_la-packet-io.o >/dev/null 2>&1
mv -f .deps/libccnet_la-packet-io.Tpo .deps/libccnet_la-packet-io.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT libccnet_la-libccnet_utils.lo -MD -MP -MF .deps/libccnet_la-libccnet_utils.Tpo -c -o libccnet_la-libccnet_utils.lo `test -f 'libccnet_utils.c' || echo './'`libccnet_utils.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-libccnet_utils.lo -MD -MP -MF .deps/libccnet_la-libccnet_utils.Tpo -c libccnet_utils.c  -fPIC -DPIC -o .libs/libccnet_la-libccnet_utils.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-libccnet_utils.lo -MD -MP -MF .deps/libccnet_la-libccnet_utils.Tpo -c libccnet_utils.c -o libccnet_la-libccnet_utils.o >/dev/null 2>&1
mv -f .deps/libccnet_la-libccnet_utils.Tpo .deps/libccnet_la-libccnet_utils.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT libccnet_la-message.lo -MD -MP -MF .deps/libccnet_la-message.Tpo -c -o libccnet_la-message.lo `test -f 'message.c' || echo './'`message.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-message.lo -MD -MP -MF .deps/libccnet_la-message.Tpo -c message.c  -fPIC -DPIC -o .libs/libccnet_la-message.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-message.lo -MD -MP -MF .deps/libccnet_la-message.Tpo -c message.c -o libccnet_la-message.o >/dev/null 2>&1
mv -f .deps/libccnet_la-message.Tpo .deps/libccnet_la-message.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT libccnet_la-proc-factory.lo -MD -MP -MF .deps/libccnet_la-proc-factory.Tpo -c -o libccnet_la-proc-factory.lo `test -f 'proc-factory.c' || echo './'`proc-factory.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-proc-factory.lo -MD -MP -MF .deps/libccnet_la-proc-factory.Tpo -c proc-factory.c  -fPIC -DPIC -o .libs/libccnet_la-proc-factory.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
proc-factory.c: In function 'ccnet_proc_factory_class_init':
proc-factory.c:29:5: warning: 'g_type_class_add_private' is deprecated [-Wdeprecated-declarations]
     g_type_class_add_private (klass, sizeof (CcnetProcFactoryPriv));
     ^~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/gobject/gobject.h:24,
                 from ../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/gobject/gbinding.h:29,
                 from ../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/glib-object.h:22,
                 from libccnet_utils.h:15,
                 from include.h:11,
                 from proc-factory.c:3:
../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/gobject/gtype.h:1307:10: note: declared here
 void     g_type_class_add_private       (gpointer                    g_class,
          ^~~~~~~~~~~~~~~~~~~~~~~~
proc-factory.c: In function 'ccnet_proc_factory_init':
proc-factory.c:35:13: warning: Deprecated pre-processor symbol, replace with 
     CcnetProcFactoryPriv *priv = GET_PRIV (factory);
             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        
proc-factory.c: In function 'ccnet_proc_factory_free':
proc-factory.c:44:13: warning: Deprecated pre-processor symbol, replace with 
     CcnetProcFactoryPriv *priv = GET_PRIV (factory);
             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        
proc-factory.c: In function 'ccnet_proc_factory_register_processor':
proc-factory.c:54:13: warning: Deprecated pre-processor symbol, replace with 
     CcnetProcFactoryPriv *priv = GET_PRIV (factory);
             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        
proc-factory.c: In function 'ccnet_proc_factory_get_proc_type':
proc-factory.c:97:13: warning: Deprecated pre-processor symbol, replace with 
     CcnetProcFactoryPriv *priv = GET_PRIV (factory);
             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-proc-factory.lo -MD -MP -MF .deps/libccnet_la-proc-factory.Tpo -c proc-factory.c -o libccnet_la-proc-factory.o >/dev/null 2>&1
mv -f .deps/libccnet_la-proc-factory.Tpo .deps/libccnet_la-proc-factory.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT libccnet_la-processor.lo -MD -MP -MF .deps/libccnet_la-processor.Tpo -c -o libccnet_la-processor.lo `test -f 'processor.c' || echo './'`processor.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-processor.lo -MD -MP -MF .deps/libccnet_la-processor.Tpo -c processor.c  -fPIC -DPIC -o .libs/libccnet_la-processor.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-processor.lo -MD -MP -MF .deps/libccnet_la-processor.Tpo -c processor.c -o libccnet_la-processor.o >/dev/null 2>&1
mv -f .deps/libccnet_la-processor.Tpo .deps/libccnet_la-processor.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT libccnet_la-buffer.lo -MD -MP -MF .deps/libccnet_la-buffer.Tpo -c -o libccnet_la-buffer.lo `test -f 'buffer.c' || echo './'`buffer.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-buffer.lo -MD -MP -MF .deps/libccnet_la-buffer.Tpo -c buffer.c  -fPIC -DPIC -o .libs/libccnet_la-buffer.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-buffer.lo -MD -MP -MF .deps/libccnet_la-buffer.Tpo -c buffer.c -o libccnet_la-buffer.o >/dev/null 2>&1
mv -f .deps/libccnet_la-buffer.Tpo .deps/libccnet_la-buffer.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT libccnet_la-peer.lo -MD -MP -MF .deps/libccnet_la-peer.Tpo -c -o libccnet_la-peer.lo `test -f 'peer.c' || echo './'`peer.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-peer.lo -MD -MP -MF .deps/libccnet_la-peer.Tpo -c peer.c  -fPIC -DPIC -o .libs/libccnet_la-peer.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-peer.lo -MD -MP -MF .deps/libccnet_la-peer.Tpo -c peer.c -o libccnet_la-peer.o >/dev/null 2>&1
mv -f .deps/libccnet_la-peer.Tpo .deps/libccnet_la-peer.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT libccnet_la-sendcmd-proc.lo -MD -MP -MF .deps/libccnet_la-sendcmd-proc.Tpo -c -o libccnet_la-sendcmd-proc.lo `test -f 'sendcmd-proc.c' || echo './'`sendcmd-proc.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-sendcmd-proc.lo -MD -MP -MF .deps/libccnet_la-sendcmd-proc.Tpo -c sendcmd-proc.c  -fPIC -DPIC -o .libs/libccnet_la-sendcmd-proc.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
sendcmd-proc.c: In function 'ccnet_sendcmd_proc_class_init':
sendcmd-proc.c:42:5: warning: 'g_type_class_add_private' is deprecated [-Wdeprecated-declarations]
     g_type_class_add_private (klass, sizeof (CcnetSendcmdProcPriv));
     ^~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/gobject/gobject.h:24,
                 from ../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/gobject/gbinding.h:29,
                 from ../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/glib-object.h:22,
                 from ../include/ccnet/ccnet-client.h:7,
                 from sendcmd-proc.c:8:
../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/gobject/gtype.h:1307:10: note: declared here
 void     g_type_class_add_private       (gpointer                    g_class,
          ^~~~~~~~~~~~~~~~~~~~~~~~
sendcmd-proc.c: In function 'send_cmd_start':
sendcmd-proc.c:56:13: warning: Deprecated pre-processor symbol, replace with 
     CcnetSendcmdProcPriv *priv = GET_PRIV (processor);
             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      
sendcmd-proc.c: In function 'handle_response':
sendcmd-proc.c:88:13: warning: Deprecated pre-processor symbol, replace with 
     CcnetSendcmdProcPriv *priv = GET_PRIV (processor);
             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-sendcmd-proc.lo -MD -MP -MF .deps/libccnet_la-sendcmd-proc.Tpo -c sendcmd-proc.c -o libccnet_la-sendcmd-proc.o >/dev/null 2>&1
mv -f .deps/libccnet_la-sendcmd-proc.Tpo .deps/libccnet_la-sendcmd-proc.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT libccnet_la-mqclient-proc.lo -MD -MP -MF .deps/libccnet_la-mqclient-proc.Tpo -c -o libccnet_la-mqclient-proc.lo `test -f 'mqclient-proc.c' || echo './'`mqclient-proc.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-mqclient-proc.lo -MD -MP -MF .deps/libccnet_la-mqclient-proc.Tpo -c mqclient-proc.c  -fPIC -DPIC -o .libs/libccnet_la-mqclient-proc.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-mqclient-proc.lo -MD -MP -MF .deps/libccnet_la-mqclient-proc.Tpo -c mqclient-proc.c -o libccnet_la-mqclient-proc.o >/dev/null 2>&1
mv -f .deps/libccnet_la-mqclient-proc.Tpo .deps/libccnet_la-mqclient-proc.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT libccnet_la-invoke-service-proc.lo -MD -MP -MF .deps/libccnet_la-invoke-service-proc.Tpo -c -o libccnet_la-invoke-service-proc.lo `test -f 'invoke-service-proc.c' || echo './'`invoke-service-proc.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-invoke-service-proc.lo -MD -MP -MF .deps/libccnet_la-invoke-service-proc.Tpo -c invoke-service-proc.c  -fPIC -DPIC -o .libs/libccnet_la-invoke-service-proc.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-invoke-service-proc.lo -MD -MP -MF .deps/libccnet_la-invoke-service-proc.Tpo -c invoke-service-proc.c -o libccnet_la-invoke-service-proc.o >/dev/null 2>&1
mv -f .deps/libccnet_la-invoke-service-proc.Tpo .deps/libccnet_la-invoke-service-proc.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT libccnet_la-marshal.lo -MD -MP -MF .deps/libccnet_la-marshal.Tpo -c -o libccnet_la-marshal.lo `test -f 'marshal.c' || echo './'`marshal.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-marshal.lo -MD -MP -MF .deps/libccnet_la-marshal.Tpo -c marshal.c  -fPIC -DPIC -o .libs/libccnet_la-marshal.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-marshal.lo -MD -MP -MF .deps/libccnet_la-marshal.Tpo -c marshal.c -o libccnet_la-marshal.o >/dev/null 2>&1
mv -f .deps/libccnet_la-marshal.Tpo .deps/libccnet_la-marshal.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT libccnet_la-cevent.lo -MD -MP -MF .deps/libccnet_la-cevent.Tpo -c -o libccnet_la-cevent.lo `test -f 'cevent.c' || echo './'`cevent.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-cevent.lo -MD -MP -MF .deps/libccnet_la-cevent.Tpo -c cevent.c  -fPIC -DPIC -o .libs/libccnet_la-cevent.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-cevent.lo -MD -MP -MF .deps/libccnet_la-cevent.Tpo -c cevent.c -o libccnet_la-cevent.o >/dev/null 2>&1
mv -f .deps/libccnet_la-cevent.Tpo .deps/libccnet_la-cevent.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT libccnet_la-timer.lo -MD -MP -MF .deps/libccnet_la-timer.Tpo -c -o libccnet_la-timer.lo `test -f 'timer.c' || echo './'`timer.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-timer.lo -MD -MP -MF .deps/libccnet_la-timer.Tpo -c timer.c  -fPIC -DPIC -o .libs/libccnet_la-timer.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-timer.lo -MD -MP -MF .deps/libccnet_la-timer.Tpo -c timer.c -o libccnet_la-timer.o >/dev/null 2>&1
mv -f .deps/libccnet_la-timer.Tpo .deps/libccnet_la-timer.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT libccnet_la-ccnet-session-base.lo -MD -MP -MF .deps/libccnet_la-ccnet-session-base.Tpo -c -o libccnet_la-ccnet-session-base.lo `test -f 'ccnet-session-base.c' || echo './'`ccnet-session-base.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-ccnet-session-base.lo -MD -MP -MF .deps/libccnet_la-ccnet-session-base.Tpo -c ccnet-session-base.c  -fPIC -DPIC -o .libs/libccnet_la-ccnet-session-base.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-ccnet-session-base.lo -MD -MP -MF .deps/libccnet_la-ccnet-session-base.Tpo -c ccnet-session-base.c -o libccnet_la-ccnet-session-base.o >/dev/null 2>&1
mv -f .deps/libccnet_la-ccnet-session-base.Tpo .deps/libccnet_la-ccnet-session-base.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT libccnet_la-job-mgr.lo -MD -MP -MF .deps/libccnet_la-job-mgr.Tpo -c -o libccnet_la-job-mgr.lo `test -f 'job-mgr.c' || echo './'`job-mgr.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-job-mgr.lo -MD -MP -MF .deps/libccnet_la-job-mgr.Tpo -c job-mgr.c  -fPIC -DPIC -o .libs/libccnet_la-job-mgr.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-job-mgr.lo -MD -MP -MF .deps/libccnet_la-job-mgr.Tpo -c job-mgr.c -o libccnet_la-job-mgr.o >/dev/null 2>&1
mv -f .deps/libccnet_la-job-mgr.Tpo .deps/libccnet_la-job-mgr.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT libccnet_la-rpcserver-proc.lo -MD -MP -MF .deps/libccnet_la-rpcserver-proc.Tpo -c -o libccnet_la-rpcserver-proc.lo `test -f 'rpcserver-proc.c' || echo './'`rpcserver-proc.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-rpcserver-proc.lo -MD -MP -MF .deps/libccnet_la-rpcserver-proc.Tpo -c rpcserver-proc.c  -fPIC -DPIC -o .libs/libccnet_la-rpcserver-proc.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
rpcserver-proc.c: In function 'ccnet_rpcserver_proc_class_init':
rpcserver-proc.c:43:5: warning: 'g_type_class_add_private' is deprecated [-Wdeprecated-declarations]
     g_type_class_add_private (klass, sizeof(CcnetRpcserverProcPriv));
     ^~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/gobject/gobject.h:24,
                 from ../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/gobject/gbinding.h:29,
                 from ../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/glib-object.h:22,
                 from libccnet_utils.h:15,
                 from include.h:11,
                 from rpcserver-proc.c:3:
../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/gobject/gtype.h:1307:10: note: declared here
 void     g_type_class_add_private       (gpointer                    g_class,
          ^~~~~~~~~~~~~~~~~~~~~~~~
rpcserver-proc.c: In function 'handle_update':
rpcserver-proc.c:66:13: warning: Deprecated pre-processor symbol, replace with 
     CcnetRpcserverProcPriv *priv = GET_PRIV (processor);
             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-rpcserver-proc.lo -MD -MP -MF .deps/libccnet_la-rpcserver-proc.Tpo -c rpcserver-proc.c -o libccnet_la-rpcserver-proc.o >/dev/null 2>&1
mv -f .deps/libccnet_la-rpcserver-proc.Tpo .deps/libccnet_la-rpcserver-proc.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT libccnet_la-threaded-rpcserver-proc.lo -MD -MP -MF .deps/libccnet_la-threaded-rpcserver-proc.Tpo -c -o libccnet_la-threaded-rpcserver-proc.lo `test -f 'threaded-rpcserver-proc.c' || echo './'`threaded-rpcserver-proc.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-threaded-rpcserver-proc.lo -MD -MP -MF .deps/libccnet_la-threaded-rpcserver-proc.Tpo -c threaded-rpcserver-proc.c  -fPIC -DPIC -o .libs/libccnet_la-threaded-rpcserver-proc.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
threaded-rpcserver-proc.c: In function 'release_resource':
threaded-rpcserver-proc.c:34:13: warning: Deprecated pre-processor symbol, replace with 
     CcnetThreadedRpcserverProcPriv *priv = GET_PRIV(processor);
             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
threaded-rpcserver-proc.c: In function 'ccnet_threaded_rpcserver_proc_class_init':
threaded-rpcserver-proc.c:52:5: warning: 'g_type_class_add_private' is deprecated [-Wdeprecated-declarations]
     g_type_class_add_private (klass, sizeof(CcnetThreadedRpcserverProcPriv));
     ^~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/gobject/gobject.h:24,
                 from ../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/gobject/gbinding.h:29,
                 from ../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/glib-object.h:22,
                 from libccnet_utils.h:15,
                 from include.h:11,
                 from threaded-rpcserver-proc.c:3:
../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/gobject/gtype.h:1307:10: note: declared here
 void     g_type_class_add_private       (gpointer                    g_class,
          ^~~~~~~~~~~~~~~~~~~~~~~~
threaded-rpcserver-proc.c: In function 'call_function_job':
threaded-rpcserver-proc.c:73:13: warning: Deprecated pre-processor symbol, replace with 
     CcnetThreadedRpcserverProcPriv *priv = GET_PRIV(processor);
             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
threaded-rpcserver-proc.c: In function 'call_function_done':
threaded-rpcserver-proc.c:89:13: warning: Deprecated pre-processor symbol, replace with 
     priv = GET_PRIV(processor);
             ^~~~~~~~~~~~~~~~~~~                             
threaded-rpcserver-proc.c: In function 'handle_update':
threaded-rpcserver-proc.c:121:13: warning: Deprecated pre-processor symbol, replace with 
     CcnetThreadedRpcserverProcPriv *priv = GET_PRIV (processor);
             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
threaded-rpcserver-proc.c:124:9: warning: 'g_memdup' is deprecated: Use 'g_memdup2' instead [-Wdeprecated-declarations]
         priv->call_buf = g_memdup (content, clen);
         ^~~~
In file included from ../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/glib.h:82,
                 from include.h:9,
                 from threaded-rpcserver-proc.c:3:
../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/glib/gstrfuncs.h:257:23: note: declared here
 gpointer              g_memdup         (gconstpointer mem,
                       ^~~~~~~~
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-threaded-rpcserver-proc.lo -MD -MP -MF .deps/libccnet_la-threaded-rpcserver-proc.Tpo -c threaded-rpcserver-proc.c -o libccnet_la-threaded-rpcserver-proc.o >/dev/null 2>&1
mv -f .deps/libccnet_la-threaded-rpcserver-proc.Tpo .deps/libccnet_la-threaded-rpcserver-proc.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT libccnet_la-ccnetobj.lo -MD -MP -MF .deps/libccnet_la-ccnetobj.Tpo -c -o libccnet_la-ccnetobj.lo `test -f 'ccnetobj.c' || echo './'`ccnetobj.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-ccnetobj.lo -MD -MP -MF .deps/libccnet_la-ccnetobj.Tpo -c ccnetobj.c  -fPIC -DPIC -o .libs/libccnet_la-ccnetobj.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
ccnetobj.c: In function 'ccnet_proc_set_peer_name':
ccnetobj.c:238:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_proc_get_peer_name (self);
            ^
ccnetobj.c: In function 'ccnet_email_user_set_email':
ccnetobj.c:474:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_email_user_get_email (self);
            ^
ccnetobj.c: In function 'ccnet_email_user_set_source':
ccnetobj.c:567:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_email_user_get_source (self);
            ^
ccnetobj.c: In function 'ccnet_email_user_set_role':
ccnetobj.c:594:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_email_user_get_role (self);
            ^
ccnetobj.c: In function 'ccnet_email_user_set_password':
ccnetobj.c:621:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_email_user_get_password (self);
            ^
ccnetobj.c: In function 'ccnet_email_user_set_reference_id':
ccnetobj.c:648:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_email_user_get_reference_id (self);
            ^
ccnetobj.c: In function 'ccnet_group_set_group_name':
ccnetobj.c:863:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_group_get_group_name (self);
            ^
ccnetobj.c: In function 'ccnet_group_set_creator_name':
ccnetobj.c:890:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_group_get_creator_name (self);
            ^
ccnetobj.c: In function 'ccnet_group_set_source':
ccnetobj.c:939:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_group_get_source (self);
            ^
ccnetobj.c: In function 'ccnet_group_user_set_user_name':
ccnetobj.c:1153:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_group_user_get_user_name (self);
            ^
ccnetobj.c: In function 'ccnet_organization_set_email':
ccnetobj.c:1344:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_organization_get_email (self);
            ^
ccnetobj.c: In function 'ccnet_organization_set_org_name':
ccnetobj.c:1393:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_organization_get_org_name (self);
            ^
ccnetobj.c: In function 'ccnet_organization_set_url_prefix':
ccnetobj.c:1420:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_organization_get_url_prefix (self);
            ^
ccnetobj.c: In function 'ccnet_organization_set_creator':
ccnetobj.c:1447:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_organization_get_creator (self);
            ^
ccnetobj.c: In function 'ccnet_peer_stat_set_id':
ccnetobj.c:1647:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_peer_stat_get_id (self);
            ^
ccnetobj.c: In function 'ccnet_peer_stat_set_name':
ccnetobj.c:1674:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_peer_stat_get_name (self);
            ^
ccnetobj.c: In function 'ccnet_peer_stat_set_ip':
ccnetobj.c:1701:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_peer_stat_get_ip (self);
            ^
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-ccnetobj.lo -MD -MP -MF .deps/libccnet_la-ccnetobj.Tpo -c ccnetobj.c -o libccnet_la-ccnetobj.o >/dev/null 2>&1
mv -f .deps/libccnet_la-ccnetobj.Tpo .deps/libccnet_la-ccnetobj.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT libccnet_la-async-rpc-proc.lo -MD -MP -MF .deps/libccnet_la-async-rpc-proc.Tpo -c -o libccnet_la-async-rpc-proc.lo `test -f 'async-rpc-proc.c' || echo './'`async-rpc-proc.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-async-rpc-proc.lo -MD -MP -MF .deps/libccnet_la-async-rpc-proc.Tpo -c async-rpc-proc.c  -fPIC -DPIC -o .libs/libccnet_la-async-rpc-proc.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
async-rpc-proc.c: In function 'release_resource':
async-rpc-proc.c:33:13: warning: Deprecated pre-processor symbol, replace with 
     CcnetAsyncRpcProcPriv *priv = GET_PRIV (processor);
             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     
async-rpc-proc.c: In function 'ccnet_async_rpc_proc_class_init':
async-rpc-proc.c:50:5: warning: 'g_type_class_add_private' is deprecated [-Wdeprecated-declarations]
     g_type_class_add_private (klass, sizeof(CcnetAsyncRpcProcPriv));
     ^~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/gobject/gobject.h:24,
                 from ../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/gobject/gbinding.h:29,
                 from ../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/glib-object.h:22,
                 from ../include/ccnet/peer.h:7,
                 from ../include/ccnet.h:11,
                 from async-rpc-proc.c:5:
../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/gobject/gtype.h:1307:10: note: declared here
 void     g_type_class_add_private       (gpointer                    g_class,
          ^~~~~~~~~~~~~~~~~~~~~~~~
async-rpc-proc.c: In function 'ccnet_async_rpc_proc_set_rpc':
async-rpc-proc.c:65:13: warning: Deprecated pre-processor symbol, replace with 
     CcnetAsyncRpcProcPriv *priv = GET_PRIV (proc);
             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~          
async-rpc-proc.c: In function 'start':
async-rpc-proc.c:77:13: warning: Deprecated pre-processor symbol, replace with 
     CcnetAsyncRpcProcPriv *priv = GET_PRIV (processor);
             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     
async-rpc-proc.c: In function 'handle_response':
async-rpc-proc.c:100:13: warning: Deprecated pre-processor symbol, replace with 
     CcnetAsyncRpcProcPriv *priv = GET_PRIV (processor);
             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-async-rpc-proc.lo -MD -MP -MF .deps/libccnet_la-async-rpc-proc.Tpo -c async-rpc-proc.c -o libccnet_la-async-rpc-proc.o >/dev/null 2>&1
mv -f .deps/libccnet_la-async-rpc-proc.Tpo .deps/libccnet_la-async-rpc-proc.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT libccnet_la-ccnet-rpc-wrapper.lo -MD -MP -MF .deps/libccnet_la-ccnet-rpc-wrapper.Tpo -c -o libccnet_la-ccnet-rpc-wrapper.lo `test -f 'ccnet-rpc-wrapper.c' || echo './'`ccnet-rpc-wrapper.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-ccnet-rpc-wrapper.lo -MD -MP -MF .deps/libccnet_la-ccnet-rpc-wrapper.Tpo -c ccnet-rpc-wrapper.c  -fPIC -DPIC -o .libs/libccnet_la-ccnet-rpc-wrapper.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -DCCNET_LIB -pthread -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT libccnet_la-ccnet-rpc-wrapper.lo -MD -MP -MF .deps/libccnet_la-ccnet-rpc-wrapper.Tpo -c ccnet-rpc-wrapper.c -o libccnet_la-ccnet-rpc-wrapper.o >/dev/null 2>&1
mv -f .deps/libccnet_la-ccnet-rpc-wrapper.Tpo .deps/libccnet_la-ccnet-rpc-wrapper.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT utils.lo -MD -MP -MF .deps/utils.Tpo -c -o utils.lo utils.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT utils.lo -MD -MP -MF .deps/utils.Tpo -c utils.c  -fPIC -DPIC -o .libs/utils.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
utils.c: In function 'get_current_time':
utils.c:916:5: warning: 'GTimeVal' is deprecated: Use 'GDateTime' instead [-Wdeprecated-declarations]
     GTimeVal tv;
     ^~~~~~~~
In file included from ../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/glib/galloca.h:32,
                 from ../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/glib.h:30,
                 from utils.h:10,
                 from utils.c:5:
../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/glib/gtypes.h:547:8: note: declared here
 struct _GTimeVal
        ^~~~~~~~~
utils.c:919:5: warning: 'g_get_current_time' is deprecated: Use 'g_get_real_time' instead [-Wdeprecated-declarations]
     g_get_current_time (&tv);
     ^~~~~~~~~~~~~~~~~~
In file included from ../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/glib/giochannel.h:33,
                 from ../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/glib.h:54,
                 from utils.h:10,
                 from utils.c:5:
../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/glib/gmain.h:681:8: note: declared here
 void   g_get_current_time                 (GTimeVal       *result);
        ^~~~~~~~~~~~~~~~~~
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT utils.lo -MD -MP -MF .deps/utils.Tpo -c utils.c -o utils.o >/dev/null 2>&1
mv -f .deps/utils.Tpo .deps/utils.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT db.lo -MD -MP -MF .deps/db.Tpo -c -o db.lo db.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT db.lo -MD -MP -MF .deps/db.Tpo -c db.c  -fPIC -DPIC -o .libs/db.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT db.lo -MD -MP -MF .deps/db.Tpo -c db.c -o db.o >/dev/null 2>&1
mv -f .deps/db.Tpo .deps/db.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT job-mgr.lo -MD -MP -MF .deps/job-mgr.Tpo -c -o job-mgr.lo job-mgr.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT job-mgr.lo -MD -MP -MF .deps/job-mgr.Tpo -c job-mgr.c  -fPIC -DPIC -o .libs/job-mgr.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT job-mgr.lo -MD -MP -MF .deps/job-mgr.Tpo -c job-mgr.c -o job-mgr.o >/dev/null 2>&1
mv -f .deps/job-mgr.Tpo .deps/job-mgr.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT rsa.lo -MD -MP -MF .deps/rsa.Tpo -c -o rsa.lo rsa.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT rsa.lo -MD -MP -MF .deps/rsa.Tpo -c rsa.c  -fPIC -DPIC -o .libs/rsa.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT rsa.lo -MD -MP -MF .deps/rsa.Tpo -c rsa.c -o rsa.o >/dev/null 2>&1
mv -f .deps/rsa.Tpo .deps/rsa.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT bloom-filter.lo -MD -MP -MF .deps/bloom-filter.Tpo -c -o bloom-filter.lo bloom-filter.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT bloom-filter.lo -MD -MP -MF .deps/bloom-filter.Tpo -c bloom-filter.c  -fPIC -DPIC -o .libs/bloom-filter.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT bloom-filter.lo -MD -MP -MF .deps/bloom-filter.Tpo -c bloom-filter.c -o bloom-filter.o >/dev/null 2>&1
mv -f .deps/bloom-filter.Tpo .deps/bloom-filter.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT marshal.lo -MD -MP -MF .deps/marshal.Tpo -c -o marshal.lo marshal.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT marshal.lo -MD -MP -MF .deps/marshal.Tpo -c marshal.c  -fPIC -DPIC -o .libs/marshal.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT marshal.lo -MD -MP -MF .deps/marshal.Tpo -c marshal.c -o marshal.o >/dev/null 2>&1
mv -f .deps/marshal.Tpo .deps/marshal.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT net.lo -MD -MP -MF .deps/net.Tpo -c -o net.lo net.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT net.lo -MD -MP -MF .deps/net.Tpo -c net.c  -fPIC -DPIC -o .libs/net.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT net.lo -MD -MP -MF .deps/net.Tpo -c net.c -o net.o >/dev/null 2>&1
mv -f .deps/net.Tpo .deps/net.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT timer.lo -MD -MP -MF .deps/timer.Tpo -c -o timer.lo timer.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT timer.lo -MD -MP -MF .deps/timer.Tpo -c timer.c  -fPIC -DPIC -o .libs/timer.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT timer.lo -MD -MP -MF .deps/timer.Tpo -c timer.c -o timer.o >/dev/null 2>&1
mv -f .deps/timer.Tpo .deps/timer.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT ccnet-session-base.lo -MD -MP -MF .deps/ccnet-session-base.Tpo -c -o ccnet-session-base.lo ccnet-session-base.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT ccnet-session-base.lo -MD -MP -MF .deps/ccnet-session-base.Tpo -c ccnet-session-base.c  -fPIC -DPIC -o .libs/ccnet-session-base.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT ccnet-session-base.lo -MD -MP -MF .deps/ccnet-session-base.Tpo -c ccnet-session-base.c -o ccnet-session-base.o >/dev/null 2>&1
mv -f .deps/ccnet-session-base.Tpo .deps/ccnet-session-base.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include    -MT ccnetobj.lo -MD -MP -MF .deps/ccnetobj.Tpo -c -o ccnetobj.lo ccnetobj.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT ccnetobj.lo -MD -MP -MF .deps/ccnetobj.Tpo -c ccnetobj.c  -fPIC -DPIC -o .libs/ccnetobj.o
cc1: note: someone does not honour COPTS correctly, passed 0 times
ccnetobj.c: In function 'ccnet_proc_set_peer_name':
ccnetobj.c:238:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_proc_get_peer_name (self);
            ^
ccnetobj.c: In function 'ccnet_email_user_set_email':
ccnetobj.c:474:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_email_user_get_email (self);
            ^
ccnetobj.c: In function 'ccnet_email_user_set_source':
ccnetobj.c:567:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_email_user_get_source (self);
            ^
ccnetobj.c: In function 'ccnet_email_user_set_role':
ccnetobj.c:594:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_email_user_get_role (self);
            ^
ccnetobj.c: In function 'ccnet_email_user_set_password':
ccnetobj.c:621:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_email_user_get_password (self);
            ^
ccnetobj.c: In function 'ccnet_email_user_set_reference_id':
ccnetobj.c:648:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_email_user_get_reference_id (self);
            ^
ccnetobj.c: In function 'ccnet_group_set_group_name':
ccnetobj.c:863:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_group_get_group_name (self);
            ^
ccnetobj.c: In function 'ccnet_group_set_creator_name':
ccnetobj.c:890:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_group_get_creator_name (self);
            ^
ccnetobj.c: In function 'ccnet_group_set_source':
ccnetobj.c:939:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_group_get_source (self);
            ^
ccnetobj.c: In function 'ccnet_group_user_set_user_name':
ccnetobj.c:1153:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_group_user_get_user_name (self);
            ^
ccnetobj.c: In function 'ccnet_organization_set_email':
ccnetobj.c:1344:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_organization_get_email (self);
            ^
ccnetobj.c: In function 'ccnet_organization_set_org_name':
ccnetobj.c:1393:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_organization_get_org_name (self);
            ^
ccnetobj.c: In function 'ccnet_organization_set_url_prefix':
ccnetobj.c:1420:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_organization_get_url_prefix (self);
            ^
ccnetobj.c: In function 'ccnet_organization_set_creator':
ccnetobj.c:1447:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_organization_get_creator (self);
            ^
ccnetobj.c: In function 'ccnet_peer_stat_set_id':
ccnetobj.c:1647:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_peer_stat_get_id (self);
            ^
ccnetobj.c: In function 'ccnet_peer_stat_set_name':
ccnetobj.c:1674:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_peer_stat_get_name (self);
            ^
ccnetobj.c: In function 'ccnet_peer_stat_set_ip':
ccnetobj.c:1701:12: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  old_value = ccnet_peer_stat_get_ip (self);
            ^
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -I../include -I../include/ccnet -I../lib -I../include -DG_LOG_DOMAIN=\"Ccnet\" -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -MT ccnetobj.lo -MD -MP -MF .deps/ccnetobj.Tpo -c ccnetobj.c -o ccnetobj.o >/dev/null 2>&1
mv -f .deps/ccnetobj.Tpo .deps/ccnetobj.Plo
/usr/bin/env bash ../libtool  --tag=CC   --mode=link ccache_cc   -no-undefined -version-info 0:0:0 -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib  -o libccnet.la -rpath /usr/lib libccnet_la-ccnet-client.lo libccnet_la-packet-io.lo libccnet_la-libccnet_utils.lo libccnet_la-message.lo libccnet_la-proc-factory.lo libccnet_la-processor.lo libccnet_la-buffer.lo libccnet_la-peer.lo libccnet_la-sendcmd-proc.lo libccnet_la-mqclient-proc.lo libccnet_la-invoke-service-proc.lo libccnet_la-marshal.lo libccnet_la-cevent.lo libccnet_la-timer.lo libccnet_la-ccnet-session-base.lo libccnet_la-job-mgr.lo libccnet_la-rpcserver-proc.lo libccnet_la-threaded-rpcserver-proc.lo libccnet_la-ccnetobj.lo libccnet_la-async-rpc-proc.lo libccnet_la-ccnet-rpc-wrapper.lo -lpthread -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lglib-2.0  -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lgobject-2.0 -lglib-2.0 -luuid   -lsqlite3 -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -levent  -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lsearpc -lgio-2.0 -lgobject-2.0 -lglib-2.0 -ljansson   
OpenWrt-libtool: link: ccache_cc -shared  -fPIC -DPIC  .libs/libccnet_la-ccnet-client.o .libs/libccnet_la-packet-io.o .libs/libccnet_la-libccnet_utils.o .libs/libccnet_la-message.o .libs/libccnet_la-proc-factory.o .libs/libccnet_la-processor.o .libs/libccnet_la-buffer.o .libs/libccnet_la-peer.o .libs/libccnet_la-sendcmd-proc.o .libs/libccnet_la-mqclient-proc.o .libs/libccnet_la-invoke-service-proc.o .libs/libccnet_la-marshal.o .libs/libccnet_la-cevent.o .libs/libccnet_la-timer.o .libs/libccnet_la-ccnet-session-base.o .libs/libccnet_la-job-mgr.o .libs/libccnet_la-rpcserver-proc.o .libs/libccnet_la-threaded-rpcserver-proc.o .libs/libccnet_la-ccnetobj.o .libs/libccnet_la-async-rpc-proc.o .libs/libccnet_la-ccnet-rpc-wrapper.o   -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib -lpthread -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -luuid -lsqlite3 -levent -lsearpc -lgio-2.0 -lgobject-2.0 -lglib-2.0 -ljansson  -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib   -Wl,-soname -Wl,libccnet.so.0 -o .libs/libccnet.so.0.0.0
OpenWrt-libtool: link: (cd ".libs" && rm -f "libccnet.so.0" && ln -s "libccnet.so.0.0.0" "libccnet.so.0")
OpenWrt-libtool: link: (cd ".libs" && rm -f "libccnet.so" && ln -s "libccnet.so.0.0.0" "libccnet.so")
OpenWrt-libtool: link: x86_64-openwrt-linux-musl-gcc-ar cru .libs/libccnet.a  libccnet_la-ccnet-client.o libccnet_la-packet-io.o libccnet_la-libccnet_utils.o libccnet_la-message.o libccnet_la-proc-factory.o libccnet_la-processor.o libccnet_la-buffer.o libccnet_la-peer.o libccnet_la-sendcmd-proc.o libccnet_la-mqclient-proc.o libccnet_la-invoke-service-proc.o libccnet_la-marshal.o libccnet_la-cevent.o libccnet_la-timer.o libccnet_la-ccnet-session-base.o libccnet_la-job-mgr.o libccnet_la-rpcserver-proc.o libccnet_la-threaded-rpcserver-proc.o libccnet_la-ccnetobj.o libccnet_la-async-rpc-proc.o libccnet_la-ccnet-rpc-wrapper.o
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
OpenWrt-libtool: link: x86_64-openwrt-linux-musl-gcc-ranlib .libs/libccnet.a
OpenWrt-libtool: link: ( cd ".libs" && rm -f "libccnet.la" && ln -s "../libccnet.la" "libccnet.la" )
/usr/bin/env bash ../libtool  --tag=CC   --mode=link ccache_cc   -no-undefined -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib  -o libccnetd.la  utils.lo db.lo job-mgr.lo rsa.lo bloom-filter.lo marshal.lo net.lo timer.lo ccnet-session-base.lo ccnetobj.lo -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lglib-2.0   -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lgobject-2.0 -lglib-2.0  -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lssl -lcrypto -lsqlite3 -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -levent   -luuid -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lsearpc -lgio-2.0 -lgobject-2.0 -lglib-2.0 -ljansson  
OpenWrt-libtool: link: x86_64-openwrt-linux-musl-gcc-ar cru .libs/libccnetd.a .libs/utils.o .libs/db.o .libs/job-mgr.o .libs/rsa.o .libs/bloom-filter.o .libs/marshal.o .libs/net.o .libs/timer.o .libs/ccnet-session-base.o .libs/ccnetobj.o 
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
OpenWrt-libtool: link: x86_64-openwrt-linux-musl-gcc-ranlib .libs/libccnetd.a
OpenWrt-libtool: link: ( cd ".libs" && rm -f "libccnetd.la" && ln -s "../libccnetd.la" "libccnetd.la" )
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ccnet-server-7.1.5-server/lib'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ccnet-server-7.1.5-server/lib'
Making all in net
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ccnet-server-7.1.5-server/net'
Making all in common
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ccnet-server-7.1.5-server/net/common'
make[7]: Nothing to be done for 'all'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ccnet-server-7.1.5-server/net/common'
Making all in server
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ccnet-server-7.1.5-server/net/server'
ccache_cc -DHAVE_CONFIG_H -I. -I../..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -DCCNET_SERVER -I../../net/common -I../../include -I../../include/ccnet -I../../lib -I../../include -I../../lib -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include   -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/ccnet-server-7.1.5-server=ccnet-server-7.1.5-server -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include  -MT ccnet-server.o -MD -MP -MF .deps/ccnet-server.Tpo -c -o ccnet-server.o ccnet-server.c
mv -f .deps/ccnet-server.Tpo .deps/ccnet-server.Po
ccache_cc -DHAVE_CONFIG_H -I. -I../..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -DCCNET_SERVER -I../../net/common -I../../include -I../../include/ccnet -I../../lib -I../../include -I../../lib -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include   -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/ccnet-server-7.1.5-server=ccnet-server-7.1.5-server -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include  -MT server-session.o -MD -MP -MF .deps/server-session.Tpo -c -o server-session.o server-session.c
mv -f .deps/server-session.Tpo .deps/server-session.Po
ccache_cc -DHAVE_CONFIG_H -I. -I../..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -DCCNET_SERVER -I../../net/common -I../../include -I../../include/ccnet -I../../lib -I../../include -I../../lib -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include   -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/ccnet-server-7.1.5-server=ccnet-server-7.1.5-server -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include  -MT user-mgr.o -MD -MP -MF .deps/user-mgr.Tpo -c -o user-mgr.o user-mgr.c
user-mgr.c: In function 'ccnet_user_manager_class_init':
user-mgr.c:63:5: warning: 'g_type_class_add_private' is deprecated [-Wdeprecated-declarations]
     g_type_class_add_private (klass, sizeof (CcnetUserManagerPriv));
     ^~~~~~~~~~~~~~~~~~~~~~~~
In file included from ../../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/gobject/gobject.h:24,
                 from ../../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/gobject/gbinding.h:29,
                 from ../../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/glib-object.h:22,
                 from ../../lib/utils.h:11,
                 from ../../net/common/common.h:28,
                 from user-mgr.c:3:
../../../../../staging_dir/target-x86_64_musl/usr/include/glib-2.0/gobject/gtype.h:1307:10: note: declared here
 void     g_type_class_add_private       (gpointer                    g_class,
          ^~~~~~~~~~~~~~~~~~~~~~~~
user-mgr.c: In function 'ccnet_user_manager_init':
user-mgr.c:69:13: warning: Deprecated pre-processor symbol, replace with 
     manager->priv = GET_PRIV(manager);
             ^~~~~~~~~~~~~~~~~~~~~~~~~~                      
user-mgr.c: In function 'hash_password_pbkdf2_sha256':
user-mgr.c:822:9: warning: 'RAND_pseudo_bytes' is deprecated [-Wdeprecated-declarations]
         RAND_pseudo_bytes (salt, sizeof(salt));
         ^~~~~~~~~~~~~~~~~
In file included from /openwrt/staging_dir/target-x86_64_musl/usr/include/openssl/rsa.h:13,
                 from ../../net/common/peer.h:9,
                 from user-mgr.c:13:
/openwrt/staging_dir/target-x86_64_musl/usr/include/openssl/rand.h:44:1: note: declared here
 DEPRECATEDIN_1_1_0(int RAND_pseudo_bytes(unsigned char *buf, int num))
 ^~~~~~~~~~~~~~~~~~
At top level:
user-mgr.c:1121:1: warning: 'get_ldap_emailuser_cb' defined but not used [-Wunused-function]
 get_ldap_emailuser_cb (CcnetDBRow *row, void *data)
 ^~~~~~~~~~~~~~~~~~~~~
mv -f .deps/user-mgr.Tpo .deps/user-mgr.Po
ccache_cc -DHAVE_CONFIG_H -I. -I../..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -DCCNET_SERVER -I../../net/common -I../../include -I../../include/ccnet -I../../lib -I../../include -I../../lib -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include   -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/ccnet-server-7.1.5-server=ccnet-server-7.1.5-server -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include  -MT group-mgr.o -MD -MP -MF .deps/group-mgr.Tpo -c -o group-mgr.o group-mgr.c
mv -f .deps/group-mgr.Tpo .deps/group-mgr.Po
ccache_cc -DHAVE_CONFIG_H -I. -I../..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -DCCNET_SERVER -I../../net/common -I../../include -I../../include/ccnet -I../../lib -I../../include -I../../lib -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include   -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/ccnet-server-7.1.5-server=ccnet-server-7.1.5-server -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include  -MT org-mgr.o -MD -MP -MF .deps/org-mgr.Tpo -c -o org-mgr.o org-mgr.c
mv -f .deps/org-mgr.Tpo .deps/org-mgr.Po
ccache_cc -DHAVE_CONFIG_H -I. -I../..  -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -DCCNET_SERVER -I../../net/common -I../../include -I../../include/ccnet -I../../lib -I../../include -I../../lib -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/searpc -I/openwrt/staging_dir/target-x86_64_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/glib-2.0/include -pthread -Wall -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include   -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/ccnet-server-7.1.5-server=ccnet-server-7.1.5-server -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include  -MT ccnet-db.o -MD -MP -MF .deps/ccnet-db.Tpo -c -o ccnet-db.o `test -f '../common/ccnet-db.c' || echo './'`../common/ccnet-db.c
../common/ccnet-db.c:10:10: fatal error: mysql.h: No such file or directory
 #include <mysql.h>
          ^~~~~~~~~
compilation terminated.
make[7]: *** [Makefile:559: ccnet-db.o] Error 1
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ccnet-server-7.1.5-server/net/server'
make[6]: *** [Makefile:386: all-recursive] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ccnet-server-7.1.5-server/net'
make[5]: *** [Makefile:491: all-recursive] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ccnet-server-7.1.5-server'
make[4]: *** [Makefile:400: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ccnet-server-7.1.5-server'
make[3]: *** [Makefile:99: /openwrt/build_dir/target-x86_64_musl/ccnet-server-7.1.5-server/.built] Error 2
```
