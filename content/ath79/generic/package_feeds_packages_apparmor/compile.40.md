---
title: "compile.40"
date: 2021-06-22 10:45:15.529832
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
make package/feeds/packages/apparmor/compile -j$(nproc) || make package/feeds/packages/apparmor/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-autoconf-libapparmor.patch using plaintext: 
patching file libraries/libapparmor/Makefile

Applying ./patches/020-fix-ss-path.patch using plaintext: 
patching file utils/aa-unconfined

Applying ./patches/030-remove-pynotify2-dep.patch using plaintext: 
patching file utils/aa-notify

Applying ./patches/040-remove-bash-dep.patch using plaintext: 
patching file utils/aa-decode

Applying ./patches/050-disable-man-pages.patch using plaintext: 
patching file binutils/Makefile
patching file parser/Makefile
patching file utils/Makefile

Applying ./patches/060-openwrt-dnsmasq-profile.patch using plaintext: 
patching file profiles/apparmor.d/usr.sbin.dnsmasq
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/apparmor-3.0.1/libraries/libapparmor'
/openwrt/staging_dir/host/bin/aclocal
/openwrt/staging_dir/host/bin/autoconf --force
/openwrt/staging_dir/host/bin/libtoolize --automake -c --force
/openwrt/staging_dir/host/bin/automake -ac
configure.ac:8: warning: AM_INIT_AUTOMAKE: two- and three-arguments forms are deprecated.  For more info, see:
configure.ac:8: http://www.gnu.org/software/automake/manual/automake.html#Modernize-AM_005fINIT_005fAUTOMAKE-invocation
configure.ac:10: installing './compile'
configure.ac:88: installing './config.guess'
configure.ac:88: installing './config.sub'
configure.ac:8: installing './install-sh'
configure.ac:8: installing './missing'
doc/Makefile.am:10: warning: subst .2,.pod,$(man_MANS: non-POSIX variable name
doc/Makefile.am:10: (probably a GNU make extension)
doc/Makefile.am:10: warning: subst .3,.pod,$(man_MANS: non-POSIX variable name
doc/Makefile.am:10: (probably a GNU make extension)
doc/Makefile.am:17: warning: '%'-style pattern rules are a GNU make extension
doc/Makefile.am:26: warning: '%'-style pattern rules are a GNU make extension
src/Makefile.am:63: warning: '%'-style pattern rules are a GNU make extension
src/Makefile.am:1: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/Makefile.am: installing './depcomp'
configure.ac: installing './ylwrap'
parallel-tests: installing './test-driver'
testsuite/Makefile.am:8: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/apparmor-3.0.1/libraries/libapparmor'
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/mips
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking for style of include used by make... GNU
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
checking dependency style of ccache_cc... gcc3
checking for flex... flex
checking lex output file root... lex.yy
checking lex library... none needed
checking whether yytext is a pointer... no
checking for bison... bison -y
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking pkg-config is at least version 0.9.0... yes
checking for swig... /openwrt/staging_dir/hostpkg/bin/swig
checking whether the libapparmor debug output should be enabled... no
checking whether the libapparmor man pages should be generated... no
checking whether python bindings are enabled... yes
checking for python3... /openwrt/staging_dir/hostpkg/bin/python3
checking for python3.9... (cached) /openwrt/staging_dir/hostpkg/bin/python3
checking for mips-openwrt-linux-python3-config... (cached) /openwrt/staging_dir/target-mips_24kc_musl/host/bin/python3.9-config
checking for a version of Python >= '2.1.0'... yes
checking for the distutils Python package... yes
checking for Python include path... ./configure: line 4683: type: /openwrt/staging_dir/target-mips_24kc_musl/host/bin/python3.9-config: not found
-I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9
checking for Python library path... ./configure: line 4703: type: /openwrt/staging_dir/target-mips_24kc_musl/host/bin/python3.9-config: not found
-I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/python3.9
checking for Python site-packages path... /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/python3.9/site-packages
checking python extra libraries... ./configure: line 4746: type: /openwrt/staging_dir/target-mips_24kc_musl/host/bin/python3.9-config: not found
libpython3.9.a -lz -lcrypt -lpthread -ldl  -lutil -lm
checking python extra linking flags... ./configure: line 4764: type: /openwrt/staging_dir/target-mips_24kc_musl/host/bin/python3.9-config: not found
-L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/python3.9/config-3.9 -lpthread -ldl -lm -lz -lpython3.9
checking consistency of all components of python development environment... no
configure: error: 
  Could not link test program to Python. Maybe the main Python library has been
  installed in some non-standard library path. If so, pass it to configure,
  via the LDFLAGS environment variable.
  Example: ./configure LDFLAGS="-L/usr/non-standard-path/python/lib"
  ============================================================================
   ERROR!
   You probably have to install the development version of the Python package
   for your distribution.  The exact name of this package varies among them.
  ============================================================================
           
make[3]: *** [Makefile:219: /openwrt/build_dir/target-mips_24kc_musl/apparmor-3.0.1/.configured_a17fb5ef857664f03cd0ce37cc5ea591] Error 1
```
