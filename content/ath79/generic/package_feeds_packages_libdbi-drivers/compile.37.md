---
title: "compile.37"
date: 2021-06-20 22:33:34.411824
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
make package/feeds/packages/libdbi-drivers/compile -j$(nproc) || make package/feeds/packages/libdbi-drivers/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001_libsqlite3_fix.patch using plaintext: 
patching file acinclude.m4

Applying ./patches/100-remove-date-to-fix-reproducible-builds.patch using plaintext: 
patching file drivers/db2/dbd_db2.c
patching file drivers/firebird/dbd_firebird.c
patching file drivers/freetds/dbd_freetds.c
patching file drivers/ingres/dbd_ingres.c
patching file drivers/msql/dbd_msql.c
patching file drivers/mysql/dbd_mysql.c
patching file drivers/oracle/dbd_oracle.c
patching file drivers/pgsql/dbd_pgsql.c
patching file drivers/sqlite/dbd_sqlite.c
patching file drivers/sqlite3/dbd_sqlite3.c
autoreconf: Entering directory `.'
autoreconf: configure.in: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force -I m4
aclocal.real: warning: autoconf input should be named 'configure.ac', not 'configure.in'
autoreconf: configure.in: tracing
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
aclocal.real: warning: autoconf input should be named 'configure.ac', not 'configure.in'
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
automake: warning: autoconf input should be named 'configure.ac', not 'configure.in'
configure.in:5: warning: AM_INIT_AUTOMAKE: two- and three-arguments forms are deprecated.  For more info, see:
configure.in:5: http://www.gnu.org/software/automake/manual/automake.html#Modernize-AM_005fINIT_005fAUTOMAKE-invocation
configure.in:34: installing './compile'
drivers/db2/Makefile.am:33: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
automake: warning: autoconf input should be named 'configure.ac', not 'configure.in'
drivers/firebird/Makefile.am:33: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
drivers/freetds/Makefile.am:32: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
drivers/ingres/Makefile.am:33: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
drivers/msql/Makefile.am:35: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
drivers/mysql/Makefile.am:37: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
drivers/oracle/Makefile.am:35: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
drivers/pgsql/Makefile.am:35: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
drivers/sqlite/Makefile.am:35: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
drivers/sqlite3/Makefile.am:35: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
tests/Makefile.am:17: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
parallel-tests: installing './test-driver'
tests/cgreen/Makefile.am:7: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
tests/cgreen/Makefile.am:9: warning: source file 'src/unit.c' is in a subdirectory,
tests/cgreen/Makefile.am:9: but option 'subdir-objects' is disabled
automake: warning: possible forward-incompatibility.
automake: At least a source file is in a subdirectory, but the 'subdir-objects'
automake: automake option hasn't been enabled.  For now, the corresponding output
automake: object file(s) will be placed in the top-level directory.  However,
automake: this behaviour will change in future Automake versions: they will
automake: unconditionally cause object files to be placed in the same subdirectory
automake: of the corresponding sources.
automake: You are advised to start using 'subdir-objects' option throughout your
automake: project, to avoid future incompatibilities.
tests/cgreen/Makefile.am:9: warning: source file 'src/messaging.c' is in a subdirectory,
tests/cgreen/Makefile.am:9: but option 'subdir-objects' is disabled
tests/cgreen/Makefile.am:9: warning: source file 'src/breadcrumb.c' is in a subdirectory,
tests/cgreen/Makefile.am:9: but option 'subdir-objects' is disabled
tests/cgreen/Makefile.am:9: warning: source file 'src/reporter.c' is in a subdirectory,
tests/cgreen/Makefile.am:9: but option 'subdir-objects' is disabled
tests/cgreen/Makefile.am:9: warning: source file 'src/assertions.c' is in a subdirectory,
tests/cgreen/Makefile.am:9: but option 'subdir-objects' is disabled
tests/cgreen/Makefile.am:9: warning: source file 'src/vector.c' is in a subdirectory,
tests/cgreen/Makefile.am:9: but option 'subdir-objects' is disabled
tests/cgreen/Makefile.am:9: warning: source file 'src/mocks.c' is in a subdirectory,
tests/cgreen/Makefile.am:9: but option 'subdir-objects' is disabled
tests/cgreen/Makefile.am:9: warning: source file 'src/constraint.c' is in a subdirectory,
tests/cgreen/Makefile.am:9: but option 'subdir-objects' is disabled
tests/cgreen/Makefile.am:9: warning: source file 'src/parameters.c' is in a subdirectory,
tests/cgreen/Makefile.am:9: but option 'subdir-objects' is disabled
tests/cgreen/Makefile.am:9: warning: source file 'src/text_reporter.c' is in a subdirectory,
tests/cgreen/Makefile.am:9: but option 'subdir-objects' is disabled
tests/cgreen/Makefile.am:9: warning: source file 'src/cdash_reporter.c' is in a subdirectory,
tests/cgreen/Makefile.am:9: but option 'subdir-objects' is disabled
autoreconf: Leaving directory `.'
configure: WARNING: unrecognized options: --disable-nls, --disable-rpath
configure: loading site script /openwrt/include/site/mips
checking whether to enable maintainer-specific portions of Makefiles... no
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
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
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking how to print strings... printf
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
checking whether to build static libraries... no
checking how to run the C preprocessor... ccache_cc -E
checking for libdbi framework... checking for MySQL support... yes
checking for MySQL includes... -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/mysql
checking for MySQL libraries... 
checking for PostgreSQL support... yes
checking for PostgreSQL includes... -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include
checking for PostgreSQL libraries... -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib
checking for SQLite support... no
checking for SQLite3 support... yes
checking for Msql support... no
checking for Oracle support... no
checking for Firebird/Interbase support... no
checking for Freetds support... no
checking for Ingres support... no
checking for IBM DB2 support... no
checking for strtoll... yes
checking for atoll... yes
checking for vasprintf... yes
checking for asprintf... yes
checking for libdbi library... yes: libs in /openwrt/staging_dir/target-mips_24kc_musl/usr/lib
checking for string.h... (cached) yes
checking for strings.h... (cached) yes
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating libdbi-drivers.spec
config.status: creating Makefile
config.status: creating doc/Makefile
config.status: creating doc/include/Makefile
config.status: creating drivers/Makefile
config.status: creating drivers/mysql/Makefile
config.status: creating drivers/pgsql/Makefile
config.status: creating drivers/sqlite/Makefile
config.status: creating drivers/sqlite3/Makefile
config.status: creating drivers/msql/Makefile
config.status: creating drivers/oracle/Makefile
config.status: creating drivers/firebird/Makefile
config.status: creating drivers/freetds/Makefile
config.status: creating drivers/ingres/Makefile
config.status: creating drivers/db2/Makefile
config.status: creating tests/Makefile
config.status: creating tests/cgreen/Makefile
config.status: creating tests/test_dbi.cfg
config.status: creating tests/plugin_settings.sh
config.status: creating config.h
config.status: executing depfiles commands
config.status: executing libtool commands
configure: WARNING: unrecognized options: --disable-nls, --disable-rpath
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/libdbi-drivers-0.9.0'
make  all-recursive
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/libdbi-drivers-0.9.0'
Making all in drivers
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/libdbi-drivers-0.9.0/drivers'
Making all in mysql
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/libdbi-drivers-0.9.0/drivers/mysql'
/bin/bash ../../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I../.. -I../.. -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/mysql  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include   -std=gnu99 -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libdbi-drivers-0.9.0=libdbi-drivers-0.9.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -MT dbd_mysql.lo -MD -MP -MF .deps/dbd_mysql.Tpo -c -o dbd_mysql.lo dbd_mysql.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I../.. -I../.. -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/mysql -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -std=gnu99 -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libdbi-drivers-0.9.0=libdbi-drivers-0.9.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -MT dbd_mysql.lo -MD -MP -MF .deps/dbd_mysql.Tpo -c dbd_mysql.c  -fPIC -DPIC -o .libs/dbd_mysql.o
dbd_mysql.c:54:10: fatal error: mysql.h: No such file or directory
 #include <mysql.h>
          ^~~~~~~~~
compilation terminated.
make[7]: *** [Makefile:502: dbd_mysql.lo] Error 1
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/libdbi-drivers-0.9.0/drivers/mysql'
make[6]: *** [Makefile:402: all-recursive] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/libdbi-drivers-0.9.0/drivers'
make[5]: *** [Makefile:453: all-recursive] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/libdbi-drivers-0.9.0'
make[4]: *** [Makefile:383: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/libdbi-drivers-0.9.0'
make[3]: *** [Makefile:106: /openwrt/build_dir/target-mips_24kc_musl/libdbi-drivers-0.9.0/.built] Error 2
```
