---
title: "compile.42"
date: 2021-06-29 09:28:26.552402
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
make package/feeds/packages/mc/compile -j$(nproc) || make package/feeds/packages/mc/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-subshell.patch using plaintext: 
patching file src/subshell/common.c

Applying ./patches/020-fix-mouse-handling-newer-terminfo.patch using plaintext: 
patching file lib/tty/tty.c

Applying ./patches/030-fix-cchat_t.patch using plaintext: 
patching file lib/tty/tty-ncurses.h
Copying file ABOUT-NLS
Copying file config/config.rpath
Copying file m4/gettext.m4
Copying file m4/host-cpu-c-abi.m4
Copying file m4/iconv.m4
Copying file m4/intlmacosx.m4
Copying file m4/lib-ld.m4
Copying file m4/lib-link.m4
Copying file m4/lib-prefix.m4
Copying file m4/nls.m4
Copying file m4/po.m4
Copying file m4/progtest.m4
Copying file po/Makefile.in.in
Copying file po/Makevars.template
Copying file po/Rules-quot
Copying file po/en@boldquot.header
Copying file po/en@quot.header
Copying file po/insert-header.sin
Copying file po/remove-potcdate.sin
autoreconf: Entering directory `.'
autoreconf: running: true --force
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-aarch64_cortex-a72_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/aclocal -I m4 -I . --force -I m4
autoreconf: configure.ac: tracing
autoreconf: configure.ac: adding subdirectory src/vfs/smbfs/helpers to autoreconf
autoreconf: Entering directory `src/vfs/smbfs/helpers'
autoreconf: configure.ac: not using Gettext
autoreconf: configure.ac: not using aclocal
autoreconf: configure.ac: not using Libtool
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: configure.ac: not using Automake
autoreconf: Leaving directory `src/vfs/smbfs/helpers'
autoreconf: running: /openwrt/staging_dir/host/bin/libtoolize --install --force
OpenWrt-libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, `config'.
OpenWrt-libtoolize: linking file `config/config.guess'
OpenWrt-libtoolize: linking file `config/config.sub'
OpenWrt-libtoolize: linking file `config/install-sh'
OpenWrt-libtoolize: linking file `config/ltmain.sh'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `m4'.
OpenWrt-libtoolize: linking file `m4/libtool.m4'
OpenWrt-libtoolize: linking file `m4/ltoptions.m4'
OpenWrt-libtoolize: linking file `m4/ltsugar.m4'
OpenWrt-libtoolize: linking file `m4/ltversion.m4'
OpenWrt-libtoolize: linking file `m4/lt~obsolete.m4'
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
configure.ac:13: warning: AM_INIT_AUTOMAKE: two- and three-arguments forms are deprecated.  For more info, see:
configure.ac:13: http://www.gnu.org/software/automake/manual/automake.html#Modernize-AM_005fINIT_005fAUTOMAKE-invocation
autoreconf: Leaving directory `.'
autoreconf: Entering directory `.'
autoreconf: running: true --force
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-aarch64_cortex-a72_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/aclocal -I m4 -I . --force -I m4
autoreconf: configure.ac: tracing
autoreconf: configure.ac: adding subdirectory src/vfs/smbfs/helpers to autoreconf
autoreconf: Entering directory `src/vfs/smbfs/helpers'
autoreconf: configure.ac: not using Gettext
autoreconf: configure.ac: not using aclocal
autoreconf: configure.ac: not using Libtool
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: configure.ac: not using Automake
autoreconf: Leaving directory `src/vfs/smbfs/helpers'
autoreconf: running: /openwrt/staging_dir/host/bin/libtoolize --install --force
OpenWrt-libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, `config'.
OpenWrt-libtoolize: linking file `config/config.guess'
OpenWrt-libtoolize: linking file `config/config.sub'
OpenWrt-libtoolize: linking file `config/install-sh'
OpenWrt-libtoolize: linking file `config/ltmain.sh'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `m4'.
OpenWrt-libtoolize: linking file `m4/libtool.m4'
OpenWrt-libtoolize: linking file `m4/ltoptions.m4'
OpenWrt-libtoolize: linking file `m4/ltsugar.m4'
OpenWrt-libtoolize: linking file `m4/ltversion.m4'
OpenWrt-libtoolize: linking file `m4/lt~obsolete.m4'
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
configure.ac:13: warning: AM_INIT_AUTOMAKE: two- and three-arguments forms are deprecated.  For more info, see:
configure.ac:13: http://www.gnu.org/software/automake/manual/automake.html#Modernize-AM_005fINIT_005fAUTOMAKE-invocation
autoreconf: Leaving directory `.'
configure: loading site script /openwrt/include/site/aarch64
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for aarch64-openwrt-linux-strip... aarch64-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether make supports nested variables... (cached) yes
checking whether to enable maintainer-specific portions of Makefiles... no
checking build system type... x86_64-pc-linux-gnu
checking host system type... aarch64-openwrt-linux-gnu
checking for style of include used by make... GNU
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
checking for ccache_cc option to accept ISO Standard C... (cached) none needed
checking whether ccache_cc accepts -Wassign-enum... no
checking whether ccache_cc accepts -Wbad-function-cast... yes
checking whether ccache_cc accepts -Wcomment... yes
checking whether ccache_cc accepts -Wconditional-uninitialized... no
checking whether ccache_cc accepts -Wdeclaration-after-statement... yes
checking whether ccache_cc accepts -Wfloat-conversion... yes
checking whether ccache_cc accepts -Wfloat-equal... yes
checking whether ccache_cc accepts -Wformat... yes
checking whether ccache_cc accepts -Wformat-security... yes
checking whether ccache_cc accepts -Wformat-signedness... yes
checking whether ccache_cc accepts -Wimplicit... yes
checking whether ccache_cc accepts -Wimplicit-fallthrough... yes
checking whether ccache_cc accepts -Wignored-qualifiers... yes
checking whether ccache_cc accepts -Wlogical-not-parentheses... yes
checking whether ccache_cc accepts -Wmaybe-uninitialized... yes
checking whether ccache_cc accepts -Wmissing-braces... yes
checking whether ccache_cc accepts -Wmissing-declarations... yes
checking whether ccache_cc accepts -Wmissing-field-initializers... yes
checking whether ccache_cc accepts -Wmissing-format-attribute... yes
checking whether ccache_cc accepts -Wmissing-parameter-type... yes
checking whether ccache_cc accepts -Wmissing-prototypes... yes
checking whether ccache_cc accepts -Wmissing-variable-declarations... no
checking whether ccache_cc accepts -Wnested-externs... yes
checking whether ccache_cc accepts -Wno-long-long... yes
checking whether ccache_cc accepts -Wno-unreachable-code... yes
checking whether ccache_cc accepts -Wparentheses... yes
checking whether ccache_cc accepts -Wpointer-arith... yes
checking whether ccache_cc accepts -Wpointer-sign... yes
checking whether ccache_cc accepts -Wredundant-decls... yes
checking whether ccache_cc accepts -Wreturn-type... yes
checking whether ccache_cc accepts -Wsequence-point... yes
checking whether ccache_cc accepts -Wshadow... yes
checking whether ccache_cc accepts -Wsign-compare... yes
checking whether ccache_cc accepts -Wstrict-prototypes... yes
checking whether ccache_cc accepts -Wswitch... yes
checking whether ccache_cc accepts -Wswitch-default... yes
checking whether ccache_cc accepts -Wtype-limits... yes
checking whether ccache_cc accepts -Wundef... yes
checking whether ccache_cc accepts -Wuninitialized... yes
checking whether ccache_cc accepts -Wunreachable-code... yes
checking whether ccache_cc accepts -Wunused-but-set-variable... yes
checking whether ccache_cc accepts -Wunused-function... yes
checking whether ccache_cc accepts -Wunused-label... yes
checking whether ccache_cc accepts -Wunused-parameter... yes
checking whether ccache_cc accepts -Wunused-result... yes
checking whether ccache_cc accepts -Wunused-value... yes
checking whether ccache_cc accepts -Wunused-variable... yes
checking whether ccache_cc accepts -Wwrite-strings... yes
checking for __attribute__((fallthrough))... no
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
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
checking pkg-config is at least version 0.9.0... yes
checking whether ln -s works... yes
checking for nroff... false
checking for file... true
checking for -L option to file command... yes
checking for gnome-moz-remote... no
checking for mozilla... no
checking for firefox... no
checking for konqueror... no
checking for opera... no
checking for aarch64-openwrt-linux-ar... (cached) aarch64-openwrt-linux-musl-gcc-ar
checking for sighandler_t... yes
checking for GLIB... no
configure: error: glib-2.0 not found or version too old (must be >= 2.30)
make[3]: *** [Makefile:132: /openwrt/build_dir/target-aarch64_cortex-a72_musl/mc-4.8.26/.configured_769c1a9434429b9814d86bc59910b604] Error 1
```
