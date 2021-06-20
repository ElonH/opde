---
title: "compile.37"
date: 2021-06-20 22:26:36.873152
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
make package/feeds/packages/open-iscsi/compile -j$(nproc) || make package/feeds/packages/open-iscsi/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/0002-idmb_rec_write-check-for-tpgt-first.patch using plaintext: 
patching file usr/idbm.c

Applying ./patches/0003-idbm_rec_write-seperate-old-and-new-style-writes.patch using plaintext: 
patching file usr/idbm.c

Applying ./patches/0004-idbw_rec_write-pick-tpgt-from-existing-record.patch using plaintext: 
patching file usr/idbm.c

Applying ./patches/0015-remove-the-offload-boot-supported-ifdef.patch using plaintext: 
patching file usr/iface.c

Applying ./patches/0019-Coverity-scan-fixes.patch using plaintext: 
patching file iscsiuio/src/unix/libs/qedi.c
patching file iscsiuio/src/unix/main.c
patching file libopeniscsiusr/idbm.c
patching file usr/idbm.c
patching file usr/iscsid.c
patching file usr/initiator.c
OpenWrt-libtoolize: putting auxiliary files in `.'.
OpenWrt-libtoolize: copying file `./ltmain.sh'
OpenWrt-libtoolize: Consider adding `AC_CONFIG_MACRO_DIR([m4])' to configure.ac and
OpenWrt-libtoolize: rerunning libtoolize, to keep the correct libtool macros in-tree.
OpenWrt-libtoolize: Consider adding `-I m4' to ACLOCAL_AMFLAGS in Makefile.am.
OpenWrt-libtoolize: `AC_PROG_RANLIB' is rendered obsolete by `LT_INIT'
configure.ac:23: installing './compile'
configure.ac:54: installing './config.guess'
configure.ac:54: installing './config.sub'
configure.ac:19: installing './install-sh'
configure.ac:19: installing './missing'
Makefile.am: installing './COPYING' using GNU General Public License v3 file
Makefile.am:     Consider adding the COPYING file to the version control system
Makefile.am:     for your code, to avoid questions about which license your project uses
src/apps/brcm-iscsi/Makefile.am: installing './depcomp'
src/unix/Makefile.am:12: warning: source file '${top_srcdir}/../utils/sysdeps/sysdeps.c' is in a subdirectory,
src/unix/Makefile.am:12: but option 'subdir-objects' is disabled
automake: warning: possible forward-incompatibility.
automake: At least a source file is in a subdirectory, but the 'subdir-objects'
automake: automake option hasn't been enabled.  For now, the corresponding output
automake: object file(s) will be placed in the top-level directory.  However,
automake: this behaviour will change in future Automake versions: they will
automake: unconditionally cause object files to be placed in the same subdirectory
automake: of the corresponding sources.
automake: You are advised to start using 'subdir-objects' option throughout your
automake: project, to avoid future incompatibilities.
src/unix/libs/Makefile.am:10: warning: source file '../build_date.c' is in a subdirectory,
src/unix/libs/Makefile.am:10: but option 'subdir-objects' is disabled
configure: loading site script /openwrt/include/site/mips
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking for bash... /bin/bash
checking for mips-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... no
checking for ccache_cc option to accept ISO C89... none needed
checking whether ccache_cc understands -c and -o together... yes
checking for style of include used by make... GNU
checking dependency style of ccache_cc... gcc3
checking for mips-openwrt-linux-ranlib... mips-openwrt-linux-ranlib
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
checking whether ccache_cc needs -traditional... no
checking for an ANSI C-conforming const... yes
checking for inline... inline
checking for off_t... yes
checking for size_t... yes
checking for int8_t... yes
checking for uint8_t... yes
checking for int16_t... yes
checking for uint16_t... yes
checking for int32_t... yes
checking for uint32_t... yes
checking for int64_t... yes
checking for uint64_t... yes
checking size of short... (cached) 2
checking size of int... (cached) 4
checking size of long... (cached) 4
checking whether byte ordering is bigendian... (cached) yes
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache_cc... /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/mips-openwrt-linux-musl/bin/ld
checking if the linker (/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/mips-openwrt-linux-musl/bin/ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-nm -B
checking the name lister (/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-nm -B) interface... BSD nm
checking whether ln -s works... yes
checking the maximum length of command line arguments... 3145728
checking whether the shell understands some XSI constructs... yes
checking whether the shell understands "+="... yes
checking how to convert x86_64-pc-linux-gnu file names to mips-openwrt-linux-gnu format... func_convert_file_noop
checking how to convert x86_64-pc-linux-gnu file names to toolchain format... func_convert_file_noop
checking for /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/mips-openwrt-linux-musl/bin/ld option to reload object files... -r
checking for mips-openwrt-linux-objdump... mips-openwrt-linux-objdump
checking how to recognize dependent libraries... pass_all
checking for mips-openwrt-linux-dlltool... no
checking for dlltool... no
checking how to associate runtime and link libraries... printf %s\n
checking for mips-openwrt-linux-ar... mips-openwrt-linux-ar
checking for archiver @FILE support... @
checking for mips-openwrt-linux-strip... (cached) mips-openwrt-linux-strip
checking for mips-openwrt-linux-ranlib... (cached) mips-openwrt-linux-ranlib
checking command to parse /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-nm -B output from ccache_cc object... failed
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
checking whether the ccache_cc linker (/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/mips-openwrt-linux-musl/bin/ld) supports shared libraries... yes
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
Package libsystemd was not found in the pkg-config search path.
Perhaps you should add the directory containing `libsystemd.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libsystemd', required by 'virtual:world', not found
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating Makefile
config.status: creating src/Makefile
config.status: creating src/apps/Makefile
config.status: creating src/apps/dhcpc/Makefile
config.status: creating src/apps/brcm-iscsi/Makefile
config.status: creating src/uip/Makefile
config.status: creating src/unix/Makefile
config.status: creating src/unix/libs/Makefile
config.status: creating config.h
config.status: executing depfiles commands
config.status: executing libtool commands
config.status: executing default commands
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3'
make -C libopeniscsiusr
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/libopeniscsiusr'
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3=open-iscsi-2.1.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -flto -D_GNU_SOURCE -DNO_SYSTEMD  -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/include -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/usr -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/libopeniscsiusr   -c -o context.o context.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3=open-iscsi-2.1.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -flto -D_GNU_SOURCE -DNO_SYSTEMD  -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/include -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/usr -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/libopeniscsiusr   -c -o misc.o misc.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3=open-iscsi-2.1.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -flto -D_GNU_SOURCE -DNO_SYSTEMD  -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/include -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/usr -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/libopeniscsiusr   -c -o session.o session.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3=open-iscsi-2.1.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -flto -D_GNU_SOURCE -DNO_SYSTEMD  -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/include -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/usr -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/libopeniscsiusr   -c -o sysfs.o sysfs.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3=open-iscsi-2.1.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -flto -D_GNU_SOURCE -DNO_SYSTEMD  -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/include -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/usr -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/libopeniscsiusr   -c -o iface.o iface.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3=open-iscsi-2.1.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -flto -D_GNU_SOURCE -DNO_SYSTEMD  -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/include -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/usr -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/libopeniscsiusr   -c -o idbm.o idbm.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3=open-iscsi-2.1.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -flto -D_GNU_SOURCE -DNO_SYSTEMD  -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/include -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/usr -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/libopeniscsiusr   -c -o node.o node.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3=open-iscsi-2.1.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -flto -D_GNU_SOURCE -DNO_SYSTEMD  -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/include -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/usr -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/libopeniscsiusr   -c -o default.o default.c
CFLAGS= -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3=open-iscsi-2.1.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -flto -D_GNU_SOURCE -DNO_SYSTEMD -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/include -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/usr -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/libopeniscsiusr
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3=open-iscsi-2.1.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -flto -D_GNU_SOURCE -DNO_SYSTEMD  -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/include -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/usr -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/libopeniscsiusr -shared -Wl,-soname=libopeniscsiusr.so.0.2.0 -o libopeniscsiusr.so.0.2.0 context.o misc.o session.o sysfs.o iface.o idbm.o node.o default.o -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -lkmod  -L/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/libopeniscsiusr 
ln -sf libopeniscsiusr.so.0.2.0 libopeniscsiusr.so
ln -sf libopeniscsiusr.so.0.2.0 libopeniscsiusr.so.0
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3=open-iscsi-2.1.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -flto -D_GNU_SOURCE -DNO_SYSTEMD  -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/include -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/usr -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/libopeniscsiusr  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -lkmod  -L/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/libopeniscsiusr  tests/test_context.c libopeniscsiusr.so.0.2.0   -o tests/test_context
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3=open-iscsi-2.1.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -flto -D_GNU_SOURCE -DNO_SYSTEMD  -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/include -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/usr -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/libopeniscsiusr  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -lkmod  -L/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/libopeniscsiusr  tests/test_session.c libopeniscsiusr.so.0.2.0   -o tests/test_session
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3=open-iscsi-2.1.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -flto -D_GNU_SOURCE -DNO_SYSTEMD  -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/include -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/usr -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/libopeniscsiusr  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -lkmod  -L/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/libopeniscsiusr  tests/test_iface.c libopeniscsiusr.so.0.2.0   -o tests/test_iface
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3=open-iscsi-2.1.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -flto -D_GNU_SOURCE -DNO_SYSTEMD  -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/include -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/usr -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/libopeniscsiusr  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -lkmod  -L/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/libopeniscsiusr  tests/test_node.c libopeniscsiusr.so.0.2.0   -o tests/test_node
install: creating directory 'docs/man'
'docs/libopeniscsiusr.h.3' -> 'docs/man/libopeniscsiusr.h.3'
cat libopeniscsiusr/libopeniscsiusr.h libopeniscsiusr/libopeniscsiusr_common.h libopeniscsiusr/libopeniscsiusr_session.h libopeniscsiusr/libopeniscsiusr_iface.h libopeniscsiusr/libopeniscsiusr_node.h | \
    perl docs/doc-preclean.pl > "/openwrt/tmp/tmp.N20SXccuDb"
perl docs/kernel-doc -man "/openwrt/tmp/tmp.N20SXccuDb" | \
    perl docs/split-man.pl docs/man
Unescaped left brace in regex is deprecated here (and will be fatal in Perl 5.32), passed through in regex; marked by <-- HERE in m/({ <-- HERE .*})/ at docs/kernel-doc line 2176.
Creating docs/man/iscsi_log_priority_str.3
Creating docs/man/iscsi_strerror.3
Creating docs/man/iscsi_context_new.3
Creating docs/man/iscsi_context_free.3
Creating docs/man/iscsi_context_log_priority_set.3
Creating docs/man/iscsi_context_log_priority_get.3
Creating docs/man/iscsi_context_log_func_set.3
Creating docs/man/iscsi_context_userdata_set.3
Creating docs/man/iscsi_context_userdata_get.3
Creating docs/man/iscsi_sessions_get.3
Creating docs/man/iscsi_sessions_free.3
Creating docs/man/iscsi_session_get.3
Creating docs/man/iscsi_session_free.3
Creating docs/man/iscsi_default_iface_setup.3
Creating docs/man/iscsi_ifaces_get.3
Creating docs/man/iscsi_ifaces_free.3
Creating docs/man/iscsi_iface_get.3
Creating docs/man/iscsi_iface_free.3
Creating docs/man/iscsi_nodes_get.3
Creating docs/man/iscsi_nodes_free.3
Creating docs/man/iscsi_session_sid_get.3
Creating docs/man/iscsi_session_persistent_address_get.3
Creating docs/man/iscsi_session_persistent_port_get.3
Creating docs/man/iscsi_session_target_name_get.3
Creating docs/man/iscsi_session_username_get.3
Creating docs/man/iscsi_session_password_get.3
Creating docs/man/iscsi_session_username_in_get.3
Creating docs/man/iscsi_session_password_in_get.3
Creating docs/man/iscsi_session_recovery_tmo_get.3
Creating docs/man/iscsi_session_lu_reset_tmo_get.3
Creating docs/man/iscsi_session_tgt_reset_tmo_get.3
Creating docs/man/iscsi_session_abort_tmo_get.3
Creating docs/man/iscsi_session_tpgt_get.3
Creating docs/man/iscsi_session_address_get.3
Creating docs/man/iscsi_session_port_get.3
Creating docs/man/iscsi_session_iface_get.3
Creating docs/man/iscsi_iface_ipaddress_get.3
Creating docs/man/iscsi_iface_hwaddress_get.3
Creating docs/man/iscsi_iface_netdev_get.3
Creating docs/man/iscsi_iface_transport_name_get.3
Creating docs/man/iscsi_iface_iname_get.3
Creating docs/man/iscsi_iface_port_state_get.3
Creating docs/man/iscsi_iface_port_speed_get.3
Creating docs/man/iscsi_iface_name_get.3
Creating docs/man/iscsi_iface_dump_config.3
Creating docs/man/iscsi_iface_print_config.3
Creating docs/man/iscsi_is_default_iface.3
Creating docs/man/iscsi_node_dump_config.3
Creating docs/man/iscsi_node_print_config.3
Creating docs/man/iscsi_node_target_name_get.3
Creating docs/man/iscsi_node_conn_is_ipv6.3
Creating docs/man/iscsi_node_conn_address_get.3
Creating docs/man/iscsi_node_conn_port_get.3
Creating docs/man/iscsi_node_portal_get.3
Creating docs/man/iscsi_node_tpgt_get.3
Creating docs/man/iscsi_node_iface_name_get.3
rm -f "/openwrt/tmp/tmp.N20SXccuDb"
find docs/man -type f -name \*[0-9].gz
docs/man/iscsi_log_priority_str.3.gz
docs/man/iscsi_session_password_get.3.gz
docs/man/iscsi_context_userdata_set.3.gz
docs/man/iscsi_strerror.3.gz
docs/man/iscsi_node_print_config.3.gz
docs/man/iscsi_ifaces_free.3.gz
docs/man/iscsi_nodes_free.3.gz
docs/man/iscsi_node_conn_port_get.3.gz
docs/man/iscsi_node_conn_is_ipv6.3.gz
docs/man/iscsi_session_tgt_reset_tmo_get.3.gz
docs/man/iscsi_sessions_get.3.gz
docs/man/iscsi_iface_dump_config.3.gz
docs/man/iscsi_context_log_priority_set.3.gz
docs/man/iscsi_session_lu_reset_tmo_get.3.gz
docs/man/iscsi_session_iface_get.3.gz
docs/man/iscsi_session_recovery_tmo_get.3.gz
docs/man/iscsi_iface_iname_get.3.gz
docs/man/iscsi_node_conn_address_get.3.gz
docs/man/iscsi_iface_print_config.3.gz
docs/man/iscsi_session_get.3.gz
docs/man/iscsi_iface_transport_name_get.3.gz
docs/man/iscsi_session_free.3.gz
docs/man/iscsi_session_abort_tmo_get.3.gz
docs/man/iscsi_iface_port_speed_get.3.gz
docs/man/iscsi_context_log_func_set.3.gz
docs/man/iscsi_session_address_get.3.gz
docs/man/iscsi_node_iface_name_get.3.gz
docs/man/iscsi_iface_ipaddress_get.3.gz
docs/man/iscsi_context_new.3.gz
docs/man/iscsi_session_sid_get.3.gz
docs/man/iscsi_context_userdata_get.3.gz
docs/man/iscsi_iface_free.3.gz
docs/man/iscsi_session_username_in_get.3.gz
docs/man/iscsi_node_dump_config.3.gz
docs/man/iscsi_nodes_get.3.gz
docs/man/iscsi_node_target_name_get.3.gz
docs/man/iscsi_sessions_free.3.gz
docs/man/iscsi_session_persistent_address_get.3.gz
docs/man/iscsi_iface_netdev_get.3.gz
docs/man/libopeniscsiusr.h.3.gz
docs/man/iscsi_node_tpgt_get.3.gz
docs/man/iscsi_iface_hwaddress_get.3.gz
docs/man/iscsi_context_free.3.gz
docs/man/iscsi_ifaces_get.3.gz
docs/man/iscsi_session_target_name_get.3.gz
docs/man/iscsi_default_iface_setup.3.gz
docs/man/iscsi_session_port_get.3.gz
docs/man/iscsi_session_tpgt_get.3.gz
docs/man/iscsi_iface_name_get.3.gz
docs/man/iscsi_is_default_iface.3.gz
docs/man/iscsi_session_username_get.3.gz
docs/man/iscsi_iface_get.3.gz
docs/man/iscsi_iface_port_state_get.3.gz
docs/man/iscsi_session_persistent_port_get.3.gz
docs/man/iscsi_context_log_priority_get.3.gz
docs/man/iscsi_node_portal_get.3.gz
docs/man/iscsi_session_password_in_get.3.gz
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/libopeniscsiusr'
make -C utils/sysdeps
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/utils/sysdeps'
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3=open-iscsi-2.1.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -flto -D_GNU_SOURCE -DNO_SYSTEMD  -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/include -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/usr -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/libopeniscsiusr   -c -o sysdeps.o sysdeps.c
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/utils/sysdeps'
make -C utils/fwparam_ibft
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/utils/fwparam_ibft'
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3=open-iscsi-2.1.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -flto -D_GNU_SOURCE -DNO_SYSTEMD  -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/include -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/usr -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/libopeniscsiusr   -c -o fw_entry.o fw_entry.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3=open-iscsi-2.1.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -flto -D_GNU_SOURCE -DNO_SYSTEMD  -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/include -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/usr -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/libopeniscsiusr   -c -o fwparam_sysfs.o fwparam_sysfs.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3=open-iscsi-2.1.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -flto -D_GNU_SOURCE -DNO_SYSTEMD  -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/include -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/usr -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/libopeniscsiusr   -c -o prom_lex.o prom_lex.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3=open-iscsi-2.1.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -flto -D_GNU_SOURCE -DNO_SYSTEMD  -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/include -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/usr -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/libopeniscsiusr   -c -o prom_parse.tab.o prom_parse.tab.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3=open-iscsi-2.1.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -flto -D_GNU_SOURCE -DNO_SYSTEMD  -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/include -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/usr -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/libopeniscsiusr   -c -o fwparam_ppc.o fwparam_ppc.c
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/utils/fwparam_ibft'
make -C usr
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/usr'
cat: /lib/modules/5.8.0-1033-azure/build/Makefile: No such file or directory
cat: /lib/modules/5.8.0-1033-azure/build/Makefile: No such file or directory
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3=open-iscsi-2.1.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -flto -D_GNU_SOURCE -DNO_SYSTEMD  -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/include -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/usr -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/libopeniscsiusr   -c -o iscsi_util.o iscsi_util.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3=open-iscsi-2.1.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -flto -D_GNU_SOURCE -DNO_SYSTEMD  -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/include -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/usr -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/libopeniscsiusr   -c -o io.o io.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3=open-iscsi-2.1.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -flto -D_GNU_SOURCE -DNO_SYSTEMD  -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/include -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/usr -I/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/libopeniscsiusr   -c -o auth.o auth.c
auth.c:45:10: fatal error: openssl/evp.h: No such file or directory
 #include <openssl/evp.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
make[5]: *** [<builtin>: auth.o] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/usr'
make[4]: *** [Makefile:65: user] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3'
make[3]: *** [Makefile:100: /openwrt/build_dir/target-mips_24kc_musl/open-iscsi-2.1.3/.built] Error 2
```
