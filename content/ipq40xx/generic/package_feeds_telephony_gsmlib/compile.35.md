---
title: "compile.35"
date: 2021-06-20 00:31:30.912702
hidden: false
draft: false
weight: -35
---

build number: `35`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/telephony/gsmlib/compile -j$(nproc) || make package/feeds/telephony/gsmlib/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/01-update-autotools.patch using plaintext: 
patching file configure.in
patching file po/Makevars
patching file Makefile.am

Applying ./patches/02-fix-cross-compile.patch using plaintext: 
patching file configure.in

Applying ./patches/03-disable-Siemens-specific-code.patch using plaintext: 
patching file Makefile.am
autoreconf: Entering directory `.'
autoreconf: configure.in: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/usr/share/aclocal -I m4 -I . --force -I m4
aclocal.real: warning: autoconf input should be named 'configure.ac', not 'configure.in'
ERROR: Use of AM_GNU_GETTEXT without [external] argument is no longer supported.
configure.in:63: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body
../../lib/autoconf/lang.m4:193: AC_LANG_CONFTEST is expanded from...
../../lib/autoconf/general.m4:2729: _AC_RUN_IFELSE is expanded from...
../../lib/m4sugar/m4sh.m4:639: AS_IF is expanded from...
../../lib/autoconf/general.m4:2748: AC_RUN_IFELSE is expanded from...
configure.in:63: the top level
configure.in:115: warning: AM_INTL_SUBDIR is m4_require'd but not m4_defun'd
/openwrt/staging_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/usr/share/aclocal/gettext.m4:55: AM_GNU_GETTEXT is expanded from...
configure.in:115: the top level
ERROR: Use of AM_GNU_GETTEXT without [external] argument is no longer supported.
configure.in:63: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body
../../lib/autoconf/lang.m4:193: AC_LANG_CONFTEST is expanded from...
../../lib/autoconf/general.m4:2729: _AC_RUN_IFELSE is expanded from...
../../lib/m4sugar/m4sh.m4:639: AS_IF is expanded from...
../../lib/autoconf/general.m4:2748: AC_RUN_IFELSE is expanded from...
configure.in:63: the top level
configure.in:115: warning: AM_INTL_SUBDIR is m4_require'd but not m4_defun'd
/openwrt/staging_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/usr/share/aclocal/gettext.m4:55: AM_GNU_GETTEXT is expanded from...
configure.in:115: the top level
autoreconf: configure.in: tracing
ERROR: Use of AM_GNU_GETTEXT without [external] argument is no longer supported.
configure.in:63: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body
../../lib/autoconf/lang.m4:193: AC_LANG_CONFTEST is expanded from...
../../lib/autoconf/general.m4:2729: _AC_RUN_IFELSE is expanded from...
../../lib/m4sugar/m4sh.m4:639: AS_IF is expanded from...
../../lib/autoconf/general.m4:2748: AC_RUN_IFELSE is expanded from...
configure.in:63: the top level
configure.in:115: warning: AM_INTL_SUBDIR is m4_require'd but not m4_defun'd
aclocal.m4:9661: AM_GNU_GETTEXT is expanded from...
configure.in:115: the top level
autoreconf: configure.in: AM_GNU_GETTEXT is used, but not AM_GNU_GETTEXT_VERSION
autoreconf: running: /openwrt/staging_dir/host/bin/libtoolize --install --force
OpenWrt-libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, `scripts'.
OpenWrt-libtoolize: linking file `scripts/config.guess'
OpenWrt-libtoolize: linking file `scripts/config.sub'
OpenWrt-libtoolize: linking file `scripts/install-sh'
OpenWrt-libtoolize: linking file `scripts/ltmain.sh'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `m4'.
OpenWrt-libtoolize: linking file `m4/libtool.m4'
OpenWrt-libtoolize: You should add the contents of `m4/libtool.m4' to `aclocal.m4'.
OpenWrt-libtoolize: linking file `m4/ltoptions.m4'
OpenWrt-libtoolize: You should add the contents of `m4/ltoptions.m4' to `aclocal.m4'.
OpenWrt-libtoolize: linking file `m4/ltsugar.m4'
OpenWrt-libtoolize: You should add the contents of `m4/ltsugar.m4' to `aclocal.m4'.
OpenWrt-libtoolize: linking file `m4/ltversion.m4'
OpenWrt-libtoolize: linking file `m4/lt~obsolete.m4'
OpenWrt-libtoolize: You should add the contents of `m4/lt~obsolete.m4' to `aclocal.m4'.
aclocal.real: warning: autoconf input should be named 'configure.ac', not 'configure.in'
ERROR: Use of AM_GNU_GETTEXT without [external] argument is no longer supported.
configure.in:63: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body
../../lib/autoconf/lang.m4:193: AC_LANG_CONFTEST is expanded from...
../../lib/autoconf/general.m4:2729: _AC_RUN_IFELSE is expanded from...
../../lib/m4sugar/m4sh.m4:639: AS_IF is expanded from...
../../lib/autoconf/general.m4:2748: AC_RUN_IFELSE is expanded from...
configure.in:63: the top level
configure.in:115: warning: AM_INTL_SUBDIR is m4_require'd but not m4_defun'd
/openwrt/staging_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/usr/share/aclocal/gettext.m4:55: AM_GNU_GETTEXT is expanded from...
configure.in:115: the top level
ERROR: Use of AM_GNU_GETTEXT without [external] argument is no longer supported.
configure.in:63: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body
../../lib/autoconf/lang.m4:193: AC_LANG_CONFTEST is expanded from...
../../lib/autoconf/general.m4:2729: _AC_RUN_IFELSE is expanded from...
../../lib/m4sugar/m4sh.m4:639: AS_IF is expanded from...
../../lib/autoconf/general.m4:2748: AC_RUN_IFELSE is expanded from...
configure.in:63: the top level
configure.in:115: warning: AM_INTL_SUBDIR is m4_require'd but not m4_defun'd
/openwrt/staging_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/usr/share/aclocal/gettext.m4:55: AM_GNU_GETTEXT is expanded from...
configure.in:115: the top level
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
ERROR: Use of AM_GNU_GETTEXT without [external] argument is no longer supported.
configure.in:63: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body
../../lib/autoconf/lang.m4:193: AC_LANG_CONFTEST is expanded from...
../../lib/autoconf/general.m4:2729: _AC_RUN_IFELSE is expanded from...
../../lib/m4sugar/m4sh.m4:639: AS_IF is expanded from...
../../lib/autoconf/general.m4:2748: AC_RUN_IFELSE is expanded from...
configure.in:63: the top level
configure.in:115: warning: AM_INTL_SUBDIR is m4_require'd but not m4_defun'd
aclocal.m4:1241: AM_GNU_GETTEXT is expanded from...
configure.in:115: the top level
configure:16478: error: possibly undefined macro: AM_INTL_SUBDIR
      If this token and others are legitimate, please use m4_pattern_allow.
      See the Autoconf documentation.
autoreconf: /openwrt/staging_dir/host/bin/autoconf failed with exit status: 1
configure: loading site script /openwrt/include/site/arm
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking for arm-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
checking whether ccache_cc understands -c and -o together... yes
checking for textdomain in -lintl... no
checking whether build environment is sane... yes
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/gsmlib-1.10-20140304/scripts/missing: Unknown `--is-lightweight' option
Try `/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/gsmlib-1.10-20140304/scripts/missing --help' for more information
configure: WARNING: 'missing' script is too old or missing
checking for arm-openwrt-linux-strip... arm-openwrt-linux-muslgnueabi-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking for style of include used by make... GNU
checking whether make supports nested variables... yes
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
checking host system type... arm-openwrt-linux-gnu
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache_cc... arm-openwrt-linux-muslgnueabi-ld
checking if the linker (arm-openwrt-linux-muslgnueabi-ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... arm-openwrt-linux-muslgnueabi-gcc-nm
checking the name lister (arm-openwrt-linux-muslgnueabi-gcc-nm) interface... BSD nm
checking whether ln -s works... yes
checking the maximum length of command line arguments... 3145728
checking whether the shell understands some XSI constructs... yes
checking whether the shell understands "+="... yes
checking how to convert x86_64-pc-linux-gnu file names to arm-openwrt-linux-gnu format... func_convert_file_noop
checking how to convert x86_64-pc-linux-gnu file names to toolchain format... func_convert_file_noop
checking for arm-openwrt-linux-muslgnueabi-ld option to reload object files... -r
checking for arm-openwrt-linux-objdump... arm-openwrt-linux-muslgnueabi-objdump
checking how to recognize dependent libraries... pass_all
checking for arm-openwrt-linux-dlltool... no
checking for dlltool... no
checking how to associate runtime and link libraries... printf %s\n
checking for arm-openwrt-linux-ar... arm-openwrt-linux-muslgnueabi-gcc-ar
checking for archiver @FILE support... @
checking for arm-openwrt-linux-strip... (cached) arm-openwrt-linux-muslgnueabi-strip
checking for arm-openwrt-linux-ranlib... arm-openwrt-linux-muslgnueabi-gcc-ranlib
checking command to parse arm-openwrt-linux-muslgnueabi-gcc-nm output from ccache_cc object... ok
checking for sysroot... no
checking for arm-openwrt-linux-mt... no
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
checking whether the ccache_cc linker (arm-openwrt-linux-muslgnueabi-ld) supports shared libraries... yes
checking whether -lc should be explicitly linked in... no
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... yes
checking how to run the C preprocessor... ccache_cc -E
checking whether we are using the GNU C++ compiler... yes
checking whether ccache_cxx accepts -g... yes
checking dependency style of ccache_cxx... gcc3
checking how to run the C++ preprocessor... ccache_cxx -E
checking for ld used by ccache_cxx... arm-openwrt-linux-muslgnueabi-ld
checking if the linker (arm-openwrt-linux-muslgnueabi-ld) is GNU ld... yes
checking whether the ccache_cxx linker (arm-openwrt-linux-muslgnueabi-ld) supports shared libraries... yes
checking for ccache_cxx option to produce PIC... -fPIC -DPIC
checking if ccache_cxx PIC flag -fPIC -DPIC works... yes
checking if ccache_cxx static flag -static works... yes
checking if ccache_cxx supports -c -o file.o... yes
checking if ccache_cxx supports -c -o file.o... (cached) yes
checking whether the ccache_cxx linker (arm-openwrt-linux-muslgnueabi-ld) supports shared libraries... yes
checking dynamic linker characteristics... (cached) GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking if at least gcc 2.95 is available... cross-compiling (assuming yes)
checking for size_t... yes
checking for working alloca.h... yes
checking for alloca... yes
checking for getopt_long in -lc... yes
checking for alarm in -lc... yes
checking netinet/in.h usability... yes
checking netinet/in.h presence... yes
checking for netinet/in.h... yes
checking for string.h... (cached) yes
checking libintl.h usability... yes
checking libintl.h presence... yes
checking for libintl.h... yes
checking for an ANSI C-conforming const... yes
checking size of unsigned short int... 2
checking size of unsigned long int... 4
checking size of unsigned int... (cached) 4
checking whether NLS is requested... no
checking for msgfmt... /openwrt/staging_dir/hostpkg/bin/msgfmt
checking for gmsgfmt... /openwrt/staging_dir/hostpkg/bin/msgfmt
checking for xgettext... /openwrt/staging_dir/hostpkg/bin/xgettext
checking for msgmerge... /openwrt/staging_dir/hostpkg/bin/msgmerge
./configure: line 12384: AM_INTL_SUBDIR: command not found
checking for ld... arm-openwrt-linux-muslgnueabi-ld
checking if the linker (arm-openwrt-linux-muslgnueabi-ld) is GNU ld... yes
checking for shared library run path origin... done
checking 32-bit host C ABI... yes
checking for ELF binary format... yes
checking for the common suffixes of directories in the library search path... lib,lib32,lib
checking for CFPreferencesCopyAppValue... no
checking for CFLocaleCopyPreferredLanguages... no
checking whether to use NLS... no
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating Makefile
config.status: WARNING:  'Makefile.in' seems to ignore the --datarootdir setting
config.status: creating gsmlib/Makefile
config.status: WARNING:  'gsmlib/Makefile.in' seems to ignore the --datarootdir setting
config.status: creating tests/Makefile
config.status: WARNING:  'tests/Makefile.in' seems to ignore the --datarootdir setting
config.status: creating apps/Makefile
config.status: WARNING:  'apps/Makefile.in' seems to ignore the --datarootdir setting
config.status: creating win32/Makefile
config.status: WARNING:  'win32/Makefile.in' seems to ignore the --datarootdir setting
config.status: creating doc/Makefile
config.status: WARNING:  'doc/Makefile.in' seems to ignore the --datarootdir setting
config.status: creating scripts/Makefile
config.status: WARNING:  'scripts/Makefile.in' seems to ignore the --datarootdir setting
config.status: creating intl/Makefile
config.status: WARNING:  'intl/Makefile.in' seems to ignore the --datarootdir setting
config.status: creating po/Makefile.in
config.status: creating ext/Makefile
config.status: WARNING:  'ext/Makefile.in' seems to ignore the --datarootdir setting
config.status: creating gsm_config.h
config.status: executing depfiles commands
config.status: executing libtool commands
config.status: executing po-directories commands
config.status: creating po/POTFILES
config.status: creating po/Makefile
config.status: executing default commands
make[4]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/gsmlib-1.10-20140304'
cd . && automake-1.15 --gnu Makefile
automake-1.15: warning: autoconf input should be named 'configure.ac', not 'configure.in'
ERROR: Use of AM_GNU_GETTEXT without [external] argument is no longer supported.
configure.in:63: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body
../../lib/autoconf/lang.m4:193: AC_LANG_CONFTEST is expanded from...
../../lib/autoconf/general.m4:2729: _AC_RUN_IFELSE is expanded from...
../../lib/m4sugar/m4sh.m4:639: AS_IF is expanded from...
../../lib/autoconf/general.m4:2748: AC_RUN_IFELSE is expanded from...
configure.in:63: the top level
configure.in:115: warning: AM_INTL_SUBDIR is m4_require'd but not m4_defun'd
aclocal.m4:1241: AM_GNU_GETTEXT is expanded from...
configure.in:115: the top level
configure.in:28: warning: AM_INIT_AUTOMAKE: two- and three-arguments forms are deprecated.  For more info, see:
configure.in:28: http://www.gnu.org/software/automake/manual/automake.html#Modernize-AM_005fINIT_005fAUTOMAKE-invocation
configure.in:22: error: required file 'scripts/compile' not found
configure.in:22:   'automake --add-missing' can install 'compile'
make[4]: *** [Makefile:150: Makefile.in] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/gsmlib-1.10-20140304'
make[3]: *** [Makefile:94: /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/gsmlib-1.10-20140304/.built] Error 2
```
