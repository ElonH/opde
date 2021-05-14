---
title: "compile.17"
date: 2021-05-14 00:39:40.255924
hidden: false
draft: false
weight: -17
---

build number: `17`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/xtables-addons/compile -j$(nproc) || make package/feeds/packages/xtables-addons/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-fix-kernel-version-detection.patch using plaintext: 
patching file configure.ac

Applying ./patches/100-add-rtsp-conntrack.patch using plaintext: 
patching file extensions/rtsp/Kbuild
patching file extensions/rtsp/netfilter_helpers.h
patching file extensions/rtsp/netfilter_mime.h
patching file extensions/rtsp/nf_conntrack_rtsp.c
patching file extensions/rtsp/nf_conntrack_rtsp.h
patching file extensions/rtsp/nf_nat_rtsp.c
patching file extensions/Kbuild
patching file mconfig

Applying ./patches/200-add-lua-packetscript.patch using plaintext: 
patching file extensions/LUA/byte_array.c
patching file extensions/LUA/controller.c
patching file extensions/LUA/controller.h
patching file extensions/LUA/Kbuild
patching file extensions/LUA/libxt_LUA.c
patching file extensions/LUA/libxt_LUA.man
patching file extensions/LUA/lua/include/ctype.h
patching file extensions/LUA/lua/include/errno.h
patching file extensions/LUA/lua/include/locale.h
patching file extensions/LUA/lua/include/setjmp.h
patching file extensions/LUA/lua/include/stdio.h
patching file extensions/LUA/lua/include/stdlib.h
patching file extensions/LUA/lua/include/string.h
patching file extensions/LUA/lua/lapi.c
patching file extensions/LUA/lua/lapi.h
patching file extensions/LUA/lua/lauxlib.c
patching file extensions/LUA/lua/lauxlib.h
patching file extensions/LUA/lua/lbaselib.c
patching file extensions/LUA/lua/lcode.c
patching file extensions/LUA/lua/lcode.h
patching file extensions/LUA/lua/ldebug.c
patching file extensions/LUA/lua/ldebug.h
patching file extensions/LUA/lua/ldo.c
patching file extensions/LUA/lua/ldo.h
patching file extensions/LUA/lua/ldump.c
patching file extensions/LUA/lua/lfunc.c
patching file extensions/LUA/lua/lfunc.h
patching file extensions/LUA/lua/lgc.c
patching file extensions/LUA/lua/lgc.h
patching file extensions/LUA/lua/llex.c
patching file extensions/LUA/lua/llex.h
patching file extensions/LUA/lua/llimits.h
patching file extensions/LUA/lua/lmem.c
patching file extensions/LUA/lua/lmem.h
patching file extensions/LUA/lua/lobject.c
patching file extensions/LUA/lua/lobject.h
patching file extensions/LUA/lua/lopcodes.c
patching file extensions/LUA/lua/lopcodes.h
patching file extensions/LUA/lua/lparser.c
patching file extensions/LUA/lua/lparser.h
patching file extensions/LUA/lua/lstate.c
patching file extensions/LUA/lua/lstate.h
patching file extensions/LUA/lua/lstring.c
patching file extensions/LUA/lua/lstring.h
patching file extensions/LUA/lua/lstrlib.c
patching file extensions/LUA/lua/ltable.c
patching file extensions/LUA/lua/ltable.h
patching file extensions/LUA/lua/ltablib.c
patching file extensions/LUA/lua/ltm.c
patching file extensions/LUA/lua/ltm.h
patching file extensions/LUA/lua/luaconf.h
patching file extensions/LUA/lua/lua.h
patching file extensions/LUA/lua/lualib.h
patching file extensions/LUA/lua/lundump.c
patching file extensions/LUA/lua/lundump.h
patching file extensions/LUA/lua/lvm.c
patching file extensions/LUA/lua/lvm.h
patching file extensions/LUA/lua/lzio.c
patching file extensions/LUA/lua/lzio.h
patching file extensions/LUA/Makefile
patching file extensions/LUA/Makefile.am
patching file extensions/LUA/Makefile.in
patching file extensions/LUA/Mbuild
patching file extensions/LUA/nf_lua.c
patching file extensions/LUA/prot_buf_dynamic.c
patching file extensions/LUA/prot_buf_ethernet.c
patching file extensions/LUA/prot_buf_helpers.c
patching file extensions/LUA/prot_buf_icmp.c
patching file extensions/LUA/prot_buf_ip.c
patching file extensions/LUA/prot_buf_raw.c
patching file extensions/LUA/prot_buf_tcp.c
patching file extensions/LUA/prot_buf_tftp.c
patching file extensions/LUA/prot_buf_udp.c
patching file extensions/LUA/xt_LUA.h
patching file extensions/LUA/xt_LUA_target.c
patching file extensions/Kbuild
patching file extensions/Mbuild
patching file mconfig

Applying ./patches/201-fix-lua-packetscript.patch using plaintext: 
patching file extensions/LUA/xt_LUA_target.c
patching file extensions/LUA/lua/llimits.h
patching file extensions/LUA/lua/lapi.c
patching file extensions/LUA/lua/ltable.c
patching file extensions/LUA/lua/luaconf.h
patching file extensions/LUA/lua/llex.h

Applying ./patches/210-freebsd-build-fix.patch using plaintext: 
patching file extensions/LUA/Makefile
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-aarch64_cortex-a72_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/aclocal -I m4 -I . --force -I m4
autoreconf: configure.ac: tracing
autoreconf: running: /openwrt/staging_dir/host/bin/libtoolize --install --force
OpenWrt-libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, `build-aux'.
OpenWrt-libtoolize: linking file `build-aux/config.guess'
OpenWrt-libtoolize: linking file `build-aux/config.sub'
OpenWrt-libtoolize: linking file `build-aux/install-sh'
OpenWrt-libtoolize: linking file `build-aux/ltmain.sh'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `m4'.
OpenWrt-libtoolize: linking file `m4/libtool.m4'
OpenWrt-libtoolize: linking file `m4/ltoptions.m4'
OpenWrt-libtoolize: linking file `m4/ltsugar.m4'
OpenWrt-libtoolize: linking file `m4/ltversion.m4'
OpenWrt-libtoolize: linking file `m4/lt~obsolete.m4'
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
Makefile.am:6: warning: ':='-style assignments are not portable
Makefile.am:21: warning: ':='-style assignments are not portable
Makefile.am:21: warning: shell mktemp -dtu: non-POSIX variable name
Makefile.am:21: (probably a GNU make extension)
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
checking for aarch64-openwrt-linux-ar... aarch64-openwrt-linux-musl-gcc-ar
checking the archiver (aarch64-openwrt-linux-musl-gcc-ar) interface... ar
checking build system type... x86_64-pc-linux-gnu
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
checking for aarch64-openwrt-linux-ar... (cached) aarch64-openwrt-linux-musl-gcc-ar
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
checking whether to build static libraries... no
checking linux/netfilter/x_tables.h usability... yes
checking linux/netfilter/x_tables.h presence... yes
checking for linux/netfilter/x_tables.h... yes
checking pkg-config is at least version 0.9.0... yes
checking for libxtables... yes
checking Xtables module directory... /usr/lib/iptables
checking kernel version that we will build against... Makefile:671: arch/x86/Makefile: No such file or directory
make[4]: *** No rule to make target 'arch/x86/Makefile'.  Stop.
0.0.0.0 in /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/linux-5.4.117
WARNING: That kernel version is not officially supported.
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating Makefile
config.status: creating Makefile.iptrules
config.status: creating Makefile.mans
config.status: creating geoip/Makefile
config.status: creating extensions/Makefile
config.status: creating extensions/ACCOUNT/Makefile
config.status: creating extensions/pknock/Makefile
config.status: creating config.h
config.status: executing depfiles commands
config.status: executing libtool commands
configure: WARNING: unrecognized options: --disable-nls
make[4]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
make  all-recursive
make[5]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
Making all in extensions
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions'
Xtables-addons 3.13 - Linux 5.4.117
if [ -n "/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/linux-5.4.117" ]; then make -C /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/linux-5.4.117 M=/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions modules; fi;
make[7]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/linux-5.4.117'
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT/xt_ACCOUNT.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/xt_LUA_target.o
/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/xt_LUA_target.c: In function 'load_script_into_state':
/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/xt_LUA_target.c:139:19: warning: logical not is only applied to the left hand side of comparison [-Wlogical-not-parentheses]
  if (!script_size > 0) {
                   ^
/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/xt_LUA_target.c:139:6: note: add parentheses around left hand side expression to silence this warning
  if (!script_size > 0) {
      ^~~~~~~~~~~~
      (           )
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/nf_lua.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/prot_buf_helpers.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/byte_array.o
/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/byte_array.c: In function 'byte_array_to_string':
/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/byte_array.c:110:2: warning: ISO C90 forbids variable length array 'buf' [-Wvla]
  uint8_t buf[(array->length * 3) + 255];
  ^~~~~~~
/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/byte_array.c:112:2: warning: ISO C90 forbids variable length array 'res' [-Wvla]
  char res[255 + (array->length * 3)]; /* make sure the buffer is big enough*/
  ^~~~
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/controller.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/prot_buf_ethernet.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/prot_buf_icmp.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/prot_buf_ip.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/prot_buf_raw.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/prot_buf_tcp.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/prot_buf_udp.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/prot_buf_tftp.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/prot_buf_dynamic.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/lapi.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/lbaselib.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/lcode.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/ldebug.o
/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/ldebug.c: In function 'symbexec':
/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/ldebug.c:267:22: warning: this statement may fall through [-Wimplicit-fallthrough=]
 #define check(x)  if (!(x)) return 0;
                      ^
/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/ldebug.c:271:26: note: in expansion of macro 'check'
 #define checkreg(pt,reg) check((reg) < (pt)->maxstacksize)
                          ^~~~~
/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/ldebug.c:413:9: note: in expansion of macro 'checkreg'
         checkreg(pt, a+3);
         ^~~~~~~~
/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/ldebug.c:415:7: note: here
       case OP_JMP: {
       ^~~~
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/ldo.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/ldump.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/lfunc.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/lgc.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/llex.o
/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/llex.c: In function 'llex':
/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/llex.c:366:14: warning: this statement may fall through [-Wimplicit-fallthrough=]
         else luaX_lexerror(ls, "invalid long string delimiter", TK_STRING);
              ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/llex.c:368:7: note: here
       case '=': {
       ^~~~
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/lmem.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/lobject.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/lopcodes.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/lparser.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/lstate.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/lstring.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/lstrlib.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/ltable.o
/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/ltable.c: In function 'luaH_get':
/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/ltable.c:472:23: warning: this statement may fall through [-Wimplicit-fallthrough=]
     case LUA_TNUMBER: {
                       ^
/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/ltable.c:480:5: note: here
     default: {
     ^~~~~~~
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/ltablib.o
/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/ltablib.c: In function 'addfield':
/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/ltablib.c:137:3: warning: this 'if' clause does not guard... [-Wmisleading-indentation]
   if (!lua_isstring(L, -1))
   ^~
/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/ltablib.c:140:5: note: ...this statement, but the latter is misleadingly indented as if it were guarded by the 'if'
     luaL_addvalue(b);
     ^~~~~~~~~~~~~
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/ltm.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/lundump.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/lvm.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/lzio.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/lua/lauxlib.o
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/xt_LUA.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock/xt_pknock.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/rtsp/nf_nat_rtsp.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/rtsp/nf_conntrack_rtsp.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/compat_xtables.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_CHAOS.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_DELUDE.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_DHCPMAC.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_DNETMAP.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_ECHO.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_IPMARK.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_LOGMARK.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_PROTO.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_SYSRQ.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_TARPIT.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_condition.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_fuzzy.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_geoip.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_iface.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_ipp2p.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_ipv4options.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_length2.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_lscan.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_psd.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_quota2.o
  Building modules, stage 2.
  MODPOST 26 modules
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT/xt_ACCOUNT.mod.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/xt_LUA.mod.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/compat_xtables.mod.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock/xt_pknock.mod.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/rtsp/nf_conntrack_rtsp.mod.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/rtsp/nf_nat_rtsp.mod.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_CHAOS.mod.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_DELUDE.mod.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_DHCPMAC.mod.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_DNETMAP.mod.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_ECHO.mod.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_IPMARK.mod.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_LOGMARK.mod.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_PROTO.mod.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_SYSRQ.mod.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_TARPIT.mod.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_condition.mod.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_fuzzy.mod.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_geoip.mod.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_iface.mod.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_ipp2p.mod.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_ipv4options.mod.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_length2.mod.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_lscan.mod.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_psd.mod.o
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_quota2.mod.o
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT/xt_ACCOUNT.ko
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/xt_LUA.ko
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/compat_xtables.ko
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock/xt_pknock.ko
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/rtsp/nf_conntrack_rtsp.ko
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/rtsp/nf_nat_rtsp.ko
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_CHAOS.ko
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_DELUDE.ko
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_DHCPMAC.ko
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_DNETMAP.ko
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_ECHO.ko
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_IPMARK.ko
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_LOGMARK.ko
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_PROTO.ko
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_SYSRQ.ko
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_TARPIT.ko
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_condition.ko
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_fuzzy.ko
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_geoip.ko
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_iface.ko
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_ipp2p.ko
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_ipv4options.ko
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_length2.ko
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_lscan.ko
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_psd.ko
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_quota2.ko
make[7]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/linux-5.4.117'
make -f ../Makefile.iptrules all;
make[7]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions'
  CC     libxt_CHAOS.oo
  CC     libxt_DELUDE.oo
  CC     libxt_DHCPMAC.oo
  CC     libxt_dhcpmac.oo
  CC     libxt_DNETMAP.oo
  CC     libxt_ECHO.oo
  CC     libxt_IPMARK.oo
  CC     libxt_LOGMARK.oo
  CC     libxt_PROTO.oo
  CC     libxt_SYSRQ.oo
  CC     libxt_TARPIT.oo
  CC     libxt_condition.oo
  CC     libxt_fuzzy.oo
  CC     libxt_geoip.oo
  CC     libxt_iface.oo
  CC     libxt_ipp2p.oo
  CC     libxt_ipv4options.oo
  CC     libxt_length2.oo
  CC     libxt_lscan.oo
  CC     libxt_psd.oo
  CC     libxt_quota2.oo
  CC     libxt_gradm.oo
  CCLD   libxt_CHAOS.so
  CCLD   libxt_DELUDE.so
  CCLD   libxt_DHCPMAC.so
  CCLD   libxt_dhcpmac.so
  CCLD   libxt_DNETMAP.so
  CCLD   libxt_ECHO.so
  CCLD   libxt_IPMARK.so
  CCLD   libxt_LOGMARK.so
  CCLD   libxt_PROTO.so
  CCLD   libxt_SYSRQ.so
  CCLD   libxt_TARPIT.so
  CCLD   libxt_condition.so
  CCLD   libxt_fuzzy.so
  CCLD   libxt_geoip.so
  CCLD   libxt_iface.so
  CCLD   libxt_ipp2p.so
  CCLD   libxt_ipv4options.so
  CCLD   libxt_length2.so
  CCLD   libxt_lscan.so
  CCLD   libxt_psd.so
  CCLD   libxt_quota2.so
  CCLD   libxt_gradm.so
make[8]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT'
depbase=`echo libxt_ACCOUNT_cl.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/bash ../../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I../..  -D_LARGEFILE_SOURCE=1 -D_LARGE_FILES -D_FILE_OFFSET_BITS=64 	-D_REENTRANT -I../../include -I/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include  -Wall -Waggregate-return -Wmissing-declarations 	-Wmissing-prototypes -Wredundant-decls -Wshadow -Wstrict-prototypes 	-Winline -pipe -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13=xtables-addons-3.13 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -MT libxt_ACCOUNT_cl.lo -MD -MP -MF $depbase.Tpo -c -o libxt_ACCOUNT_cl.lo libxt_ACCOUNT_cl.c &&\
mv -f $depbase.Tpo $depbase.Plo
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I../.. -D_LARGEFILE_SOURCE=1 -D_LARGE_FILES -D_FILE_OFFSET_BITS=64 -D_REENTRANT -I../../include -I/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include -Wall -Waggregate-return -Wmissing-declarations -Wmissing-prototypes -Wredundant-decls -Wshadow -Wstrict-prototypes -Winline -pipe -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13=xtables-addons-3.13 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -MT libxt_ACCOUNT_cl.lo -MD -MP -MF .deps/libxt_ACCOUNT_cl.Tpo -c libxt_ACCOUNT_cl.c  -fPIC -DPIC -o .libs/libxt_ACCOUNT_cl.o
depbase=`echo iptaccount.o | sed 's|[^/]*$|.deps/&|;s|\.o$||'`;\
ccache_cc -DHAVE_CONFIG_H -I. -I../..  -D_LARGEFILE_SOURCE=1 -D_LARGE_FILES -D_FILE_OFFSET_BITS=64 	-D_REENTRANT -I../../include -I/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include  -Wall -Waggregate-return -Wmissing-declarations 	-Wmissing-prototypes -Wredundant-decls -Wshadow -Wstrict-prototypes 	-Winline -pipe -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13=xtables-addons-3.13 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -MT iptaccount.o -MD -MP -MF $depbase.Tpo -c -o iptaccount.o iptaccount.c &&\
mv -f $depbase.Tpo $depbase.Po
make -f ../../Makefile.iptrules all;
make[9]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT'
  CC     libxt_ACCOUNT.oo
  CCLD   libxt_ACCOUNT.so
make[9]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT'
/bin/bash ../../libtool  --tag=CC   --mode=link ccache_cc -Wall -Waggregate-return -Wmissing-declarations 	-Wmissing-prototypes -Wredundant-decls -Wshadow -Wstrict-prototypes 	-Winline -pipe -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13=xtables-addons-3.13 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro   -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro  -o libxt_ACCOUNT_cl.la -rpath /usr/lib libxt_ACCOUNT_cl.lo  
OpenWrt-libtool: link: ccache_cc -shared  -fPIC -DPIC  .libs/libxt_ACCOUNT_cl.o   -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib  -Os -fstack-protector -Wl,-z -Wl,now -Wl,-z -Wl,relro   -Wl,-soname -Wl,libxt_ACCOUNT_cl.so.0 -o .libs/libxt_ACCOUNT_cl.so.0.0.0
OpenWrt-libtool: link: (cd ".libs" && rm -f "libxt_ACCOUNT_cl.so.0" && ln -s "libxt_ACCOUNT_cl.so.0.0.0" "libxt_ACCOUNT_cl.so.0")
OpenWrt-libtool: link: (cd ".libs" && rm -f "libxt_ACCOUNT_cl.so" && ln -s "libxt_ACCOUNT_cl.so.0.0.0" "libxt_ACCOUNT_cl.so")
OpenWrt-libtool: link: ( cd ".libs" && rm -f "libxt_ACCOUNT_cl.la" && ln -s "../libxt_ACCOUNT_cl.la" "libxt_ACCOUNT_cl.la" )
/bin/bash ../../libtool  --tag=CC   --mode=link ccache_cc -Wall -Waggregate-return -Wmissing-declarations 	-Wmissing-prototypes -Wredundant-decls -Wshadow -Wstrict-prototypes 	-Winline -pipe -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13=xtables-addons-3.13 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro   -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro  -o iptaccount iptaccount.o libxt_ACCOUNT_cl.la 
OpenWrt-libtool: link: ccache_cc -Wall -Waggregate-return -Wmissing-declarations -Wmissing-prototypes -Wredundant-decls -Wshadow -Wstrict-prototypes -Winline -pipe -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13=xtables-addons-3.13 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z -Wl,now -Wl,-z -Wl,relro -znow -zrelro -o .libs/iptaccount iptaccount.o  -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib ./.libs/libxt_ACCOUNT_cl.so
make[8]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT'
make[8]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock'
depbase=`echo pknlusr.o | sed 's|[^/]*$|.deps/&|;s|\.o$||'`;\
ccache_cc -DHAVE_CONFIG_H -I. -I../..  -D_LARGEFILE_SOURCE=1 -D_LARGE_FILES -D_FILE_OFFSET_BITS=64 	-D_REENTRANT -I../../include -I/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include  -Wall -Waggregate-return -Wmissing-declarations 	-Wmissing-prototypes -Wredundant-decls -Wshadow -Wstrict-prototypes 	-Winline -pipe -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13=xtables-addons-3.13 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -MT pknlusr.o -MD -MP -MF $depbase.Tpo -c -o pknlusr.o pknlusr.c &&\
mv -f $depbase.Tpo $depbase.Po
make -f ../../Makefile.iptrules all;
make[9]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock'
  CC     libxt_pknock.oo
  CCLD   libxt_pknock.so
make[9]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock'
/bin/bash ../../libtool  --tag=CC   --mode=link ccache_cc -Wall -Waggregate-return -Wmissing-declarations 	-Wmissing-prototypes -Wredundant-decls -Wshadow -Wstrict-prototypes 	-Winline -pipe -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13=xtables-addons-3.13 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro   -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro  -o pknlusr pknlusr.o  
OpenWrt-libtool: link: ccache_cc -Wall -Waggregate-return -Wmissing-declarations -Wmissing-prototypes -Wredundant-decls -Wshadow -Wstrict-prototypes -Winline -pipe -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13=xtables-addons-3.13 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z -Wl,now -Wl,-z -Wl,relro -znow -zrelro -o pknlusr pknlusr.o  -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib
make[8]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock'
make[8]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA'
make[9]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
make[9]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
make[9]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
make[9]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
make -f ../../Makefile.iptrules all;
make[9]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA'
  CC     libxt_LUA.oo
libxt_LUA.c: In function 'lua_tg_init':
libxt_LUA.c:63:52: warning: argument to 'sizeof' in 'strncpy' call is the same expression as the source; did you mean to use the size of the destination? [-Wsizeof-pointer-memaccess]
  strncpy(info->function, "process_packet\0", sizeof("process_packet\0"));
                                                    ^
  CCLD   libxt_LUA.so
make[9]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA'
make[8]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA'
make[7]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions'
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions'
Making all in extensions/ACCOUNT
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT'
make -f ../../Makefile.iptrules all;
make[7]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT'
make[7]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT'
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT'
Making all in extensions/pknock
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock'
make -f ../../Makefile.iptrules all;
make[7]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock'
make[7]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock'
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock'
Making all in geoip
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/geoip'
make[6]: Nothing to be done for 'all'.
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/geoip'
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
make -f Makefile.mans all;
make[7]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
for ext in ./extensions/libxt_condition.man ./extensions/libxt_dhcpmac.man ./extensions/libxt_fuzzy.man ./extensions/libxt_geoip.man ./extensions/libxt_gradm.man ./extensions/libxt_iface.man ./extensions/libxt_ipp2p.man ./extensions/libxt_ipv4options.man ./extensions/libxt_length2.man ./extensions/libxt_lscan.man ./extensions/libxt_psd.man ./extensions/libxt_quota2.man ./extensions/pknock/libxt_pknock.man; do name="${ext%.man}"; name="${name##*/libxt_}"; if [ -f "$ext" ]; then echo ".SS $name"; cat "$ext" || exit $?; continue; fi; done >matches.man;
for ext in ./extensions/ACCOUNT/libxt_ACCOUNT.man ./extensions/LUA/libxt_LUA.man ./extensions/libxt_CHAOS.man ./extensions/libxt_DELUDE.man ./extensions/libxt_DHCPMAC.man ./extensions/libxt_DNETMAP.man ./extensions/libxt_ECHO.man ./extensions/libxt_IPMARK.man ./extensions/libxt_LOGMARK.man ./extensions/libxt_PROTO.man ./extensions/libxt_SYSRQ.man ./extensions/libxt_TARPIT.man; do name="${ext%.man}"; name="${name##*/libxt_}"; if [ -f "$ext" ]; then echo ".SS $name"; cat "$ext" || exit $?; continue; fi; done >targets.man;
sed -e '/@MATCHES@/ r matches.man' -e '/@TARGET@/ r targets.man' xtables-addons.8.in >xtables-addons.8;
make[7]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
make[5]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
make[4]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
grep: /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/./Module.symvers: No such file or directory
make[4]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
Making install in extensions
make[5]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions'
Xtables-addons 3.13 - Linux 5.4.117
if [ -n "/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/linux-5.4.117" ]; then make -C /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/linux-5.4.117 M=/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions modules; fi;
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/linux-5.4.117'
  Building modules, stage 2.
  MODPOST 26 modules
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/linux-5.4.117'
make -f ../Makefile.iptrules all;
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions'
make[7]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT'
make -f ../../Makefile.iptrules all;
make[8]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT'
make[8]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT'
make[7]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT'
make[7]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock'
make -f ../../Makefile.iptrules all;
make[8]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock'
make[8]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock'
make[7]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock'
make[7]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA'
make[8]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
make[8]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
make[8]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
make[8]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
make -f ../../Makefile.iptrules all;
make[8]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA'
make[8]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA'
make[7]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA'
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions'
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions'
if [ -n "/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/linux-5.4.117" ]; then make -C /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/linux-5.4.117 M=/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions INSTALL_MOD_PATH=/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install ext-mod-dir='${INSTALL_MOD_DIR}' modules_install; fi;
make[7]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/linux-5.4.117'
  INSTALL /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT/xt_ACCOUNT.ko
  INSTALL /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA/xt_LUA.ko
  INSTALL /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/compat_xtables.ko
  INSTALL /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock/xt_pknock.ko
  INSTALL /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/rtsp/nf_conntrack_rtsp.ko
  INSTALL /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/rtsp/nf_nat_rtsp.ko
  INSTALL /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_CHAOS.ko
  INSTALL /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_DELUDE.ko
  INSTALL /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_DHCPMAC.ko
  INSTALL /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_DNETMAP.ko
  INSTALL /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_ECHO.ko
  INSTALL /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_IPMARK.ko
  INSTALL /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_LOGMARK.ko
  INSTALL /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_PROTO.ko
  INSTALL /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_SYSRQ.ko
  INSTALL /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_TARPIT.ko
  INSTALL /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_condition.ko
  INSTALL /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_fuzzy.ko
  INSTALL /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_geoip.ko
  INSTALL /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_iface.ko
  INSTALL /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_ipp2p.ko
  INSTALL /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_ipv4options.ko
  INSTALL /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_length2.ko
  INSTALL /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_lscan.ko
  INSTALL /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_psd.ko
  INSTALL /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/xt_quota2.ko
  DEPMOD  5.4.117
Warning: modules_install: missing 'System.map' file. Skipping depmod.
make[7]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/linux-5.4.117'
make -f ../Makefile.iptrules install;
make[7]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions'
make[8]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT'
make -f ../../Makefile.iptrules all;
make[9]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT'
make[9]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT'
make[9]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT'
make -f ../../Makefile.iptrules install;
make[10]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT'
install -dm0755 "/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install//usr/lib/iptables";
make[10]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libxt_ACCOUNT_cl.la '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libxt_ACCOUNT_cl.so.0.0.0 /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/lib/libxt_ACCOUNT_cl.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/lib && { ln -s -f libxt_ACCOUNT_cl.so.0.0.0 libxt_ACCOUNT_cl.so.0 || { rm -f libxt_ACCOUNT_cl.so.0 && ln -s libxt_ACCOUNT_cl.so.0.0.0 libxt_ACCOUNT_cl.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/lib && { ln -s -f libxt_ACCOUNT_cl.so.0.0.0 libxt_ACCOUNT_cl.so || { rm -f libxt_ACCOUNT_cl.so && ln -s libxt_ACCOUNT_cl.so.0.0.0 libxt_ACCOUNT_cl.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libxt_ACCOUNT_cl.lai /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/lib/libxt_ACCOUNT_cl.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/sbin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c iptaccount '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/sbin'
OpenWrt-libtool: install: warning: `libxt_ACCOUNT_cl.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/iptaccount /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/sbin/iptaccount
 /usr/bin/mkdir -p '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/man/man8'
 /openwrt/staging_dir/host/bin/install -c -m 644 iptaccount.8 '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/man/man8'
make[9]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT'
make[8]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT'
make[8]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock'
make -f ../../Makefile.iptrules all;
make[9]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock'
make[9]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock'
make[9]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock'
make -f ../../Makefile.iptrules install;
make[10]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock'
install -dm0755 "/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install//usr/lib/iptables";
make[10]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/sbin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c pknlusr '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/sbin'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c pknlusr /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/sbin/pknlusr
 /usr/bin/mkdir -p '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/man/man8'
 /openwrt/staging_dir/host/bin/install -c -m 644 pknlusr.8 '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/man/man8'
make[9]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock'
make[8]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock'
make[8]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA'
make[9]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
make[9]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
make[9]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
make[9]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
make -f ../../Makefile.iptrules all;
make[9]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA'
make[9]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA'
make[9]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA'
make[10]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
make[10]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
make[10]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
make[10]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
make -f ../../Makefile.iptrules install;
make[10]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA'
install -dm0755 "/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install//usr/lib/iptables";
make[10]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA'
make[9]: Nothing to be done for 'install-data-am'.
make[9]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA'
make[8]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/LUA'
install -dm0755 "/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install//usr/lib/iptables";
make[7]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions'
make[6]: Nothing to be done for 'install-data-am'.
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions'
make[5]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions'
Making install in extensions/ACCOUNT
make[5]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT'
make -f ../../Makefile.iptrules all;
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT'
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT'
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT'
make -f ../../Makefile.iptrules install;
make[7]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT'
install -dm0755 "/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install//usr/lib/iptables";
make[7]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libxt_ACCOUNT_cl.la '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libxt_ACCOUNT_cl.so.0.0.0 /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/lib/libxt_ACCOUNT_cl.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/lib && { ln -s -f libxt_ACCOUNT_cl.so.0.0.0 libxt_ACCOUNT_cl.so.0 || { rm -f libxt_ACCOUNT_cl.so.0 && ln -s libxt_ACCOUNT_cl.so.0.0.0 libxt_ACCOUNT_cl.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/lib && { ln -s -f libxt_ACCOUNT_cl.so.0.0.0 libxt_ACCOUNT_cl.so || { rm -f libxt_ACCOUNT_cl.so && ln -s libxt_ACCOUNT_cl.so.0.0.0 libxt_ACCOUNT_cl.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libxt_ACCOUNT_cl.lai /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/lib/libxt_ACCOUNT_cl.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/sbin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c iptaccount '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/sbin'
OpenWrt-libtool: install: warning: `libxt_ACCOUNT_cl.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/iptaccount /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/sbin/iptaccount
 /usr/bin/mkdir -p '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/man/man8'
 /openwrt/staging_dir/host/bin/install -c -m 644 iptaccount.8 '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/man/man8'
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT'
make[5]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/ACCOUNT'
Making install in extensions/pknock
make[5]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock'
make -f ../../Makefile.iptrules all;
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock'
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock'
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock'
make -f ../../Makefile.iptrules install;
make[7]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock'
install -dm0755 "/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install//usr/lib/iptables";
make[7]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/sbin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c pknlusr '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/sbin'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c pknlusr /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/sbin/pknlusr
 /usr/bin/mkdir -p '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/man/man8'
 /openwrt/staging_dir/host/bin/install -c -m 644 pknlusr.8 '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/man/man8'
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock'
make[5]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/extensions/pknock'
Making install in geoip
make[5]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/geoip'
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/geoip'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/bin'
 /openwrt/staging_dir/host/bin/install -c xt_geoip_fetch xt_geoip_fetch_maxmind '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/bin'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/lib/xtables-addons'
 /openwrt/staging_dir/host/bin/install -c xt_geoip_build xt_geoip_build_maxmind xt_geoip_dl xt_geoip_dl_maxmind '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/lib/xtables-addons'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/man/man1'
 /openwrt/staging_dir/host/bin/install -c -m 644 xt_geoip_build.1 xt_geoip_dl.1 xt_geoip_fetch.1 '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/man/man1'
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/geoip'
make[5]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/geoip'
make[5]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
make -f Makefile.mans all;
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
make[6]: Nothing to be done for 'install-exec-am'.
make -f Makefile.mans all;
make[7]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
make[7]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/man/man8'
 /openwrt/staging_dir/host/bin/install -c -m 644 xtables-addons.8 '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-install/usr/man/man8'
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
make[5]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
make[4]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13'
rstrip.sh: /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-aarch64_cortex-a72/kmod-ipt-compat-xtables/lib/modules/5.4.117/compat_xtables.ko: relocatable
Packaged contents of /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/xtables-addons-3.13/ipkg-aarch64_cortex-a72/kmod-ipt-compat-xtables into /openwrt/bin/targets/bcm27xx/bcm2711/packages/kmod-ipt-compat-xtables_5.4.117+3.13-4_aarch64_cortex-a72.ipk
Package kmod-ipt-nathelper-rtsp is missing dependencies for the following libraries:
nf_conntrack.ko
nf_nat.ko
make[3]: *** [Makefile:185: /openwrt/bin/targets/bcm27xx/bcm2711/packages/kmod-ipt-nathelper-rtsp_5.4.117+3.13-4_aarch64_cortex-a72.ipk] Error 1
```
