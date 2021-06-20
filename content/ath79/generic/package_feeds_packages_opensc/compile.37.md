---
title: "compile.37"
date: 2021-06-20 22:39:07.400287
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
make package/feeds/packages/opensc/compile -j$(nproc) || make package/feeds/packages/opensc/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-openssl-deprecated.patch using plaintext: 
patching file src/libopensc/sc-ossl-compat.h
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force -I m4
autoreconf: configure.ac: tracing
autoreconf: running: /openwrt/staging_dir/host/bin/libtoolize --install --force
OpenWrt-libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, `.'.
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
checking whether make supports nested variables... (cached) yes
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
checking whether we are using the GNU C++ compiler... yes
checking whether ccache_cxx accepts -g... yes
checking dependency style of ccache_cxx... gcc3
checking for mips-openwrt-linux-gcc... mips-openwrt-linux-gcc
checking whether we are using the GNU Objective C compiler... no
checking whether mips-openwrt-linux-gcc accepts -g... no
checking dependency style of mips-openwrt-linux-gcc... gcc3
checking pkg-config is at least version 0.9.0... yes
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
checking whether byte ordering is bigendian... (cached) yes
checking whether to build with code coverage support... no
checking whether C compiler accepts -Wunknown-warning-option... no
checking how to run the C preprocessor... ccache_cc -E
checking whether ln -s works... yes
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking whether make sets $(MAKE)... (cached) yes
checking how to print strings... printf
checking for a sed that does not truncate output... (cached) /openwrt/staging_dir/host/bin/sed
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
checking for mips-openwrt-linux-windres... no
checking for windres... no
checking for xsltproc... xsltproc
checking for git... git
checking xsl-stylesheets... /usr/share/xml/docbook/stylesheet/nwalsh
checking git checkout... no
checking for inline... inline
checking for ANSI C header files... (cached) yes
checking for sys/wait.h that is POSIX.1 compatible... yes
checking whether to enable assertions... yes
checking errno.h usability... yes
checking errno.h presence... yes
checking for errno.h... yes
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking for stdlib.h... (cached) yes
checking for inttypes.h... (cached) yes
checking for string.h... (cached) yes
checking for strings.h... (cached) yes
checking sys/time.h usability... yes
checking sys/time.h presence... yes
checking for sys/time.h... yes
checking for unistd.h... (cached) yes
checking sys/mman.h usability... yes
checking sys/mman.h presence... yes
checking for sys/mman.h... yes
checking sys/endian.h usability... no
checking sys/endian.h presence... no
checking for sys/endian.h... no
checking endian.h usability... yes
checking endian.h presence... yes
checking for endian.h... yes
checking for an ANSI C-conforming const... yes
checking for uid_t in sys/types.h... yes
checking for size_t... yes
checking whether time.h and sys/time.h may both be included... yes
checking for error_at_line... no
checking whether lstat correctly handles trailing slash... (cached) yes
checking whether stat accepts an empty string... (cached) no
checking for vprintf... yes
checking for _doprnt... no
checking for getpass... yes
checking for gettimeofday... (cached) yes
checking for getline... yes
checking for memset... yes
checking for mkdir... yes
checking for strdup... yes
checking for strerror... (cached) yes
checking for memset_s... no
checking for explicit_bzero... yes
checking for strnlen... yes
checking for sigaction... yes
checking size of void *... (cached) 4
checking for socket in -lsocket... no
checking for library containing dlopen... none required
checking whether ccache_cc is Clang... no
checking whether pthreads work with -pthread... yes
checking for joinable pthread attribute... PTHREAD_CREATE_JOINABLE
checking whether more special flags are required for pthreads... no
checking for PTHREAD_PRIO_INHERIT... yes
checking for GIO2... yes
checking gio/gio.h usability... yes
checking gio/gio.h presence... no
configure: WARNING: gio/gio.h: accepted by the compiler, rejected by the preprocessor!
configure: WARNING: gio/gio.h: proceeding with the compiler's result
checking for gio/gio.h... yes
checking for g_application_send_notification... yes
checking for CMOCKA... no
checking setjmp.h usability... yes
checking setjmp.h presence... yes
checking for setjmp.h... yes
checking for cmocka.h... no
checking for inflate in -lz... yes
checking zlib.h usability... yes
checking zlib.h presence... yes
checking for zlib.h... yes
checking for readline in -lreadline... yes
checking readline/readline.h usability... yes
checking readline/readline.h presence... yes
checking for readline/readline.h... yes
checking for OPENSSL... no
checking for RSA_version in -lcrypto... no
checking openssl/crypto.h usability... no
checking openssl/crypto.h presence... no
checking for openssl/crypto.h... no
configure: WARNING: libeac not found by pkg-config
checking eac/eac.h usability... no
checking eac/eac.h presence... no
checking for eac/eac.h... no
configure: WARNING: OpenPACE headers not found
checking for EAC_CTX_init_pace... configure: WARNING: Cannot link against libeac
configure: WARNING: use --enable-cvcdir=DIR
configure: WARNING: use --enable-x509dir=DIR
checking for PCSC... yes
checking winscard.h usability... yes
checking winscard.h presence... no
configure: WARNING: winscard.h: accepted by the compiler, rejected by the preprocessor!
configure: WARNING: winscard.h: proceeding with the compiler's result
checking for winscard.h... yes
checking pcsclite.h usability... yes
checking pcsclite.h presence... no
configure: WARNING: pcsclite.h: accepted by the compiler, rejected by the preprocessor!
configure: WARNING: pcsclite.h: proceeding with the compiler's result
checking for pcsclite.h... yes
completion detect
checking for BASH_COMPLETION... no
checking XSLTPROC requirement... ok
checking for gengetopt... /openwrt/staging_dir/host/bin/gengetopt
checking for clang-tidy... not found
checking getopt.h usability... yes
checking getopt.h presence... yes
checking for getopt.h... yes
checking for getopt_long... yes
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating Makefile
config.status: creating doc/Makefile
config.status: creating doc/tools/Makefile
config.status: creating doc/files/Makefile
config.status: creating etc/Makefile
config.status: creating tests/Makefile
config.status: creating src/Makefile
config.status: creating src/common/Makefile
config.status: creating src/ui/Makefile
config.status: creating src/libopensc/Makefile
config.status: creating src/sm/Makefile
config.status: creating src/pkcs11/Makefile
config.status: creating src/pkcs11/versioninfo-pkcs11.rc
config.status: creating src/pkcs11/versioninfo-pkcs11-spy.rc
config.status: creating src/pkcs11/opensc-pkcs11.pc
config.status: creating src/pkcs15init/Makefile
config.status: creating src/scconf/Makefile
config.status: creating src/tests/Makefile
config.status: creating src/tests/regression/Makefile
config.status: creating src/tests/p11test/Makefile
config.status: creating src/tests/fuzzing/Makefile
config.status: creating src/tests/unittests/Makefile
config.status: creating src/tools/Makefile
config.status: creating src/tools/versioninfo-tools.rc
config.status: creating src/tools/versioninfo-opensc-notify.rc
config.status: creating src/smm/Makefile
config.status: creating src/minidriver/Makefile
config.status: creating src/minidriver/versioninfo-minidriver.rc
config.status: creating src/minidriver/opensc-minidriver.inf
config.status: creating win32/Makefile
config.status: creating win32/versioninfo.rc
config.status: creating win32/versioninfo-customactions.rc
config.status: creating win32/winconfig.h
config.status: creating win32/OpenSC.iss
config.status: creating win32/OpenSC.wxs
config.status: creating MacOSX/Makefile
config.status: creating MacOSX/build-package
config.status: creating MacOSX/Distribution.xml
config.status: creating MacOSX/resources/Welcome.html
config.status: creating config.h
config.status: executing depfiles commands
config.status: executing libtool commands
configure: WARNING: unrecognized options: --disable-nls

OpenSC has been configured with the following options:


Version:                 0.21.0
Version fix:             0
Version revision:        0
Git revision:            No Git revision info available

Copyright:               OpenSC Project
Company:                 OpenSC Project
Company URL:             https://github.com/OpenSC
Comments:                Provided under the terms of the GNU Lesser General Public License (LGPLv2.1+).
Product name:            OpenSC smartcard framework
Product updates:         https://github.com/OpenSC/OpenSC/releases
Product URL:             https://github.com/OpenSC/OpenSC

User binaries:           /usr/bin
Configuration files:     /etc
Bash completion:         /etc/bash_completion.d
XSL stylesheets:         /usr/share/xml/docbook/stylesheet/nwalsh

man support:             yes
doc support:             no
thread locking support:  yes
zlib support:            yes
readline support:        yes
OpenSSL support:         no
OpenSSL secure memory:   no
PC/SC support:           yes
CryptoTokenKit support:  no
OpenCT support:          no
CT-API support:          no
minidriver support:      no
SM support:              yes
SM default module:       libsmm-local.so
SM default path:         /usr/lib
DNIe UI support:         no
Notification support:    no
Code coverage:           no

PC/SC default provider:  libpcsclite.so.1
PKCS11 default provider: /usr/lib/opensc-pkcs11.so
PKCS11 onepin provider:  /usr/lib/onepin-opensc-pkcs11.so

Host:                    mips-openwrt-linux-gnu
Compiler:                ccache_cc
Preprocessor flags:      -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include 
Compiler flags:          -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0=opensc-0.21.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro 
Linker flags:            -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro 
Libraries:               

READLINE_CFLAGS:         
READLINE_LIBS:           -lreadline 
ZLIB_CFLAGS:             
ZLIB_LIBS:               -lz
OPENSSL_CFLAGS:          
OPENSSL_LIBS:            
OPENPACE_CFLAGS:         
OPENPACE_LIBS:           
OPENCT_CFLAGS:           
OPENCT_LIBS:             
PCSC_CFLAGS:             -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/PCSC -pthread 
CRYPTOTOKENKIT_CFLAGS:   
GIO2_CFLAGS:             -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread 
GIO2_LIBS:               -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lgio-2.0 -lgobject-2.0 -lglib-2.0 
FUZZING_LIBS:            

make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0'
make  all-recursive
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0'
Making all in etc
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/etc'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/etc'
Making all in src
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src'
Making all in common
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/common'
  CC       compat_dummy.lo
  CC       compat_strlcat.lo
  CC       compat_strlcpy.lo
  CC       compat_strnlen.lo
  CC       compat_getpass.lo
  CC       compat_getopt.lo
  CC       compat_report_rangecheckfailure.lo
  CC       compat___iob_func.lo
  CC       simclist.lo
  CCLD     libcompat.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CC       libpkcs11.lo
  CCLD     libpkcs11.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CC       libscdl.lo
  CCLD     libscdl.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CC       compat_getopt_main.o
  CCLD     compat_getopt_main
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/common'
Making all in scconf
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/scconf'
  CC       scconf.lo
  CC       parse.lo
  CC       write.lo
  CC       sclex.lo
  CCLD     libscconf.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/scconf'
Making all in ui
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/ui'
  CC       strings.lo
  CCLD     libstrings.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CC       notify.lo
  CCLD     libnotify.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/ui'
Making all in pkcs15init
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/pkcs15init'
  CC       pkcs15-lib.lo
  CC       profile.lo
  CC       pkcs15-westcos.lo
  CC       pkcs15-gpk.lo
  CC       pkcs15-miocos.lo
  CC       pkcs15-cflex.lo
  CC       pkcs15-cardos.lo
  CC       pkcs15-jcop.lo
  CC       pkcs15-starcos.lo
  CC       pkcs15-setcos.lo
  CC       pkcs15-incrypto34.lo
  CC       pkcs15-muscle.lo
  CC       pkcs15-asepcos.lo
  CC       pkcs15-rutoken.lo
  CC       pkcs15-entersafe.lo
  CC       pkcs15-epass2003.lo
  CC       pkcs15-rtecp.lo
  CC       pkcs15-myeid.lo
  CC       pkcs15-oberthur.lo
  CC       pkcs15-oberthur-awp.lo
  CC       pkcs15-authentic.lo
  CC       pkcs15-iasecc.lo
  CC       pkcs15-openpgp.lo
  CC       pkcs15-sc-hsm.lo
  CC       pkcs15-isoApplet.lo
  CC       pkcs15-gids.lo
  CCLD     libpkcs15init.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/pkcs15init'
Making all in sm
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/sm'
  CC       sm-iso.lo
  CCLD     libsmiso.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CC       libsmeac_la-sm-eac.lo
  CCLD     libsmeac.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/sm'
Making all in libopensc
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/libopensc'
  CC       libopensc_la-sc.lo
  CC       libopensc_la-ctx.lo
  CC       libopensc_la-log.lo
  CC       libopensc_la-errors.lo
  CC       libopensc_la-asn1.lo
  CC       libopensc_la-base64.lo
  CC       libopensc_la-sec.lo
  CC       libopensc_la-card.lo
  CC       libopensc_la-iso7816.lo
  CC       libopensc_la-dir.lo
  CC       libopensc_la-ef-atr.lo
  CC       libopensc_la-ef-gdo.lo
  CC       libopensc_la-padding.lo
  CC       libopensc_la-apdu.lo
  CC       libopensc_la-simpletlv.lo
  CC       libopensc_la-gp.lo
  CC       libopensc_la-pkcs15.lo
  CC       libopensc_la-pkcs15-cert.lo
  CC       libopensc_la-pkcs15-data.lo
  CC       libopensc_la-pkcs15-pin.lo
  CC       libopensc_la-pkcs15-prkey.lo
  CC       libopensc_la-pkcs15-pubkey.lo
  CC       libopensc_la-pkcs15-skey.lo
  CC       libopensc_la-pkcs15-sec.lo
  CC       libopensc_la-pkcs15-algo.lo
  CC       libopensc_la-pkcs15-cache.lo
  CC       libopensc_la-pkcs15-syn.lo
  CC       libopensc_la-muscle.lo
  CC       libopensc_la-muscle-filesystem.lo
  CC       libopensc_la-ctbcs.lo
  CC       libopensc_la-reader-ctapi.lo
  CC       libopensc_la-reader-pcsc.lo
  CC       libopensc_la-reader-openct.lo
  CC       libopensc_la-reader-tr03119.lo
  CC       libopensc_la-card-setcos.lo
  CC       libopensc_la-card-miocos.lo
  CC       libopensc_la-card-flex.lo
  CC       libopensc_la-card-gpk.lo
  CC       libopensc_la-card-cardos.lo
  CC       libopensc_la-card-tcos.lo
  CC       libopensc_la-card-default.lo
  CC       libopensc_la-card-mcrd.lo
  CC       libopensc_la-card-starcos.lo
  CC       libopensc_la-card-openpgp.lo
  CC       libopensc_la-card-jcop.lo
  CC       libopensc_la-card-oberthur.lo
  CC       libopensc_la-card-belpic.lo
  CC       libopensc_la-card-atrust-acos.lo
  CC       libopensc_la-card-entersafe.lo
  CC       libopensc_la-card-epass2003.lo
  CC       libopensc_la-card-coolkey.lo
  CC       libopensc_la-card-incrypto34.lo
  CC       libopensc_la-card-piv.lo
  CC       libopensc_la-card-cac-common.lo
  CC       libopensc_la-card-cac.lo
  CC       libopensc_la-card-cac1.lo
  CC       libopensc_la-card-muscle.lo
  CC       libopensc_la-card-asepcos.lo
  CC       libopensc_la-card-akis.lo
  CC       libopensc_la-card-gemsafeV1.lo
  CC       libopensc_la-card-rutoken.lo
  CC       libopensc_la-card-rtecp.lo
  CC       libopensc_la-card-westcos.lo
  CC       libopensc_la-card-myeid.lo
  CC       libopensc_la-card-itacns.lo
  CC       libopensc_la-card-authentic.lo
  CC       libopensc_la-card-iasecc.lo
  CC       libopensc_la-iasecc-sdo.lo
  CC       libopensc_la-iasecc-sm.lo
  CC       libopensc_la-card-sc-hsm.lo
  CC       libopensc_la-card-dnie.lo
  CC       libopensc_la-cwa14890.lo
  CC       libopensc_la-cwa-dnie.lo
  CC       libopensc_la-card-isoApplet.lo
  CC       libopensc_la-card-masktech.lo
  CC       libopensc_la-card-gids.lo
  CC       libopensc_la-card-jpki.lo
  CC       libopensc_la-card-npa.lo
  CC       libopensc_la-card-esteid2018.lo
  CC       libopensc_la-card-idprime.lo
  CC       libopensc_la-card-edo.lo
  CC       libopensc_la-pkcs15-openpgp.lo
  CC       libopensc_la-pkcs15-starcert.lo
  CC       libopensc_la-pkcs15-cardos.lo
  CC       libopensc_la-pkcs15-tcos.lo
  CC       libopensc_la-pkcs15-esteid.lo
  CC       libopensc_la-pkcs15-gemsafeGPK.lo
  CC       libopensc_la-pkcs15-actalis.lo
  CC       libopensc_la-pkcs15-atrust-acos.lo
  CC       libopensc_la-pkcs15-tccardos.lo
  CC       libopensc_la-pkcs15-piv.lo
  CC       libopensc_la-pkcs15-cac.lo
  CC       libopensc_la-pkcs15-esinit.lo
  CC       libopensc_la-pkcs15-westcos.lo
  CC       libopensc_la-pkcs15-pteid.lo
  CC       libopensc_la-pkcs15-oberthur.lo
  CC       libopensc_la-pkcs15-itacns.lo
  CC       libopensc_la-pkcs15-gemsafeV1.lo
  CC       libopensc_la-pkcs15-sc-hsm.lo
  CC       libopensc_la-pkcs15-coolkey.lo
  CC       libopensc_la-pkcs15-din-66291.lo
  CC       libopensc_la-pkcs15-idprime.lo
  CC       libopensc_la-pkcs15-dnie.lo
  CC       libopensc_la-pkcs15-gids.lo
  CC       libopensc_la-pkcs15-iasecc.lo
  CC       libopensc_la-pkcs15-jpki.lo
  CC       libopensc_la-pkcs15-esteid2018.lo
  CC       libopensc_la-compression.lo
  CC       libopensc_la-p15card-helper.lo
  CC       libopensc_la-sm.lo
  CC       libopensc_la-aux-data.lo
  OBJCLD   libopensc.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/libopensc'
Making all in pkcs11
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/pkcs11'
  CC       opensc_pkcs11_la-pkcs11-global.lo
  CC       opensc_pkcs11_la-pkcs11-session.lo
  CC       opensc_pkcs11_la-pkcs11-object.lo
  CC       opensc_pkcs11_la-misc.lo
  CC       opensc_pkcs11_la-slot.lo
  CC       opensc_pkcs11_la-mechanism.lo
  CC       opensc_pkcs11_la-openssl.lo
  CC       opensc_pkcs11_la-framework-pkcs15.lo
  CC       opensc_pkcs11_la-framework-pkcs15init.lo
  CC       opensc_pkcs11_la-debug.lo
  CC       opensc_pkcs11_la-pkcs11-display.lo
  CCLD     opensc-pkcs11.la
  CC       pkcs11_spy_la-pkcs11-spy.lo
  CC       pkcs11_spy_la-pkcs11-display.lo
  CCLD     pkcs11-spy.la
  CC       onepin_opensc_pkcs11_la-pkcs11-global.lo
  CC       onepin_opensc_pkcs11_la-pkcs11-session.lo
  CC       onepin_opensc_pkcs11_la-pkcs11-object.lo
  CC       onepin_opensc_pkcs11_la-misc.lo
  CC       onepin_opensc_pkcs11_la-slot.lo
  CC       onepin_opensc_pkcs11_la-mechanism.lo
  CC       onepin_opensc_pkcs11_la-openssl.lo
  CC       onepin_opensc_pkcs11_la-framework-pkcs15.lo
  CC       onepin_opensc_pkcs11_la-framework-pkcs15init.lo
  CC       onepin_opensc_pkcs11_la-debug.lo
  CC       onepin_opensc_pkcs11_la-pkcs11-display.lo
  CCLD     onepin-opensc-pkcs11.la
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/pkcs11'
Making all in tools
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tools'
  CC       opensc-tool.o
  CC       util.o
  CCLD     opensc-tool
  CC       opensc-explorer.o
  CCLD     opensc-explorer
  CC       opensc_notify-opensc-notify.o
  CC       opensc_notify-opensc-notify-cmdline.o
  CCLD     opensc-notify
  CC       pkcs15-tool.o
  CC       ../pkcs11/pkcs11-display.o
  CCLD     pkcs15-tool
  CC       pkcs15-crypt.o
  CCLD     pkcs15-crypt
  CC       pkcs11-tool.o
  CCLD     pkcs11-tool
  CC       pkcs11_register-pkcs11-register.o
  CC       pkcs11_register-fread_to_eof.o
  CC       pkcs11_register-pkcs11-register-cmdline.o
  CCLD     pkcs11-register
  CC       cardos-tool.o
  CCLD     cardos-tool
  CC       eidenv.o
  CCLD     eidenv
  CC       openpgp-tool.o
  CCLD     openpgp-tool
  CC       iasecc-tool.o
  CCLD     iasecc-tool
  CC       egk_tool-egk-tool.o
  CC       egk_tool-util.o
  CC       egk_tool-egk-tool-cmdline.o
  CCLD     egk-tool
  CC       opensc_asn1-opensc-asn1.o
  CC       opensc_asn1-fread_to_eof.o
  CC       opensc_asn1-opensc-asn1-cmdline.o
  CCLD     opensc-asn1
  CC       goid_tool-goid-tool.o
  CC       goid_tool-util.o
  CC       goid_tool-fread_to_eof.o
  CC       goid_tool-goid-tool-cmdline.o
  CCLD     goid-tool
  CC       sceac_example-sceac-example.o
  CCLD     sceac-example
/openwrt/staging_dir/host/bin/sed -e 's,[@]bindir[@],/usr/bin,g' -e 's,[@]CVCDIR[@],,g' -e 's,[@]PACKAGE[@],opensc,g' -e 's,[@]PACKAGE_BUGREPORT[@],https://github.com/OpenSC/OpenSC/issues,g' -e 's,[@]PACKAGE_NAME[@],OpenSC,g' -e 's,[@]PACKAGE_TARNAME[@],opensc,g' -e 's,[@]PACKAGE_URL[@],https://github.com/OpenSC/OpenSC,g' -e 's,[@]PACKAGE_SUMMARY[@],,g' -e 's,[@]PACKAGE_VERSION[@],"0.21.0",g' -e 's,[@]DEFAULT_PKCS11_PROVIDER[@],"/usr/lib/opensc-pkcs11.so",g' -e 's,[@]VDFORMAT[@],XML,g' -e 's,[@]X509DIR[@],,g' < org.opensc.notify.desktop.in > org.opensc.notify.desktop
/openwrt/staging_dir/host/bin/sed -e 's,[@]bindir[@],/usr/bin,g' -e 's,[@]CVCDIR[@],,g' -e 's,[@]PACKAGE[@],opensc,g' -e 's,[@]PACKAGE_BUGREPORT[@],https://github.com/OpenSC/OpenSC/issues,g' -e 's,[@]PACKAGE_NAME[@],OpenSC,g' -e 's,[@]PACKAGE_TARNAME[@],opensc,g' -e 's,[@]PACKAGE_URL[@],https://github.com/OpenSC/OpenSC,g' -e 's,[@]PACKAGE_SUMMARY[@],,g' -e 's,[@]PACKAGE_VERSION[@],"0.21.0",g' -e 's,[@]DEFAULT_PKCS11_PROVIDER[@],"/usr/lib/opensc-pkcs11.so",g' -e 's,[@]VDFORMAT[@],XML,g' -e 's,[@]X509DIR[@],,g' < org.opensc-project.mac.pkcs11-register.plist.in > org.opensc-project.mac.pkcs11-register.plist
/openwrt/staging_dir/host/bin/sed -e 's,[@]bindir[@],/usr/bin,g' -e 's,[@]CVCDIR[@],,g' -e 's,[@]PACKAGE[@],opensc,g' -e 's,[@]PACKAGE_BUGREPORT[@],https://github.com/OpenSC/OpenSC/issues,g' -e 's,[@]PACKAGE_NAME[@],OpenSC,g' -e 's,[@]PACKAGE_TARNAME[@],opensc,g' -e 's,[@]PACKAGE_URL[@],https://github.com/OpenSC/OpenSC,g' -e 's,[@]PACKAGE_SUMMARY[@],,g' -e 's,[@]PACKAGE_VERSION[@],"0.21.0",g' -e 's,[@]DEFAULT_PKCS11_PROVIDER[@],"/usr/lib/opensc-pkcs11.so",g' -e 's,[@]VDFORMAT[@],XML,g' -e 's,[@]X509DIR[@],,g' < org.opensc-project.mac.opensc-notify.plist.in > org.opensc-project.mac.opensc-notify.plist
/openwrt/staging_dir/host/bin/sed -e 's,[@]bindir[@],/usr/bin,g' -e 's,[@]CVCDIR[@],,g' -e 's,[@]PACKAGE[@],opensc,g' -e 's,[@]PACKAGE_BUGREPORT[@],https://github.com/OpenSC/OpenSC/issues,g' -e 's,[@]PACKAGE_NAME[@],OpenSC,g' -e 's,[@]PACKAGE_TARNAME[@],opensc,g' -e 's,[@]PACKAGE_URL[@],https://github.com/OpenSC/OpenSC,g' -e 's,[@]PACKAGE_SUMMARY[@],,g' -e 's,[@]PACKAGE_VERSION[@],"0.21.0",g' -e 's,[@]DEFAULT_PKCS11_PROVIDER[@],"/usr/lib/opensc-pkcs11.so",g' -e 's,[@]VDFORMAT[@],XML,g' -e 's,[@]X509DIR[@],,g' < pkcs11-register.desktop.in > pkcs11-register.desktop
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tools'
Making all in minidriver
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/minidriver'
make[7]: Nothing to be done for 'all'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/minidriver'
Making all in tests
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests'
Making all in regression
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests/regression'
make[8]: Nothing to be done for 'all'.
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests/regression'
Making all in p11test
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests/p11test'
make[8]: Nothing to be done for 'all'.
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests/p11test'
Making all in fuzzing
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests/fuzzing'
make[8]: Nothing to be done for 'all'.
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests/fuzzing'
Making all in unittests
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests/unittests'
make[8]: Nothing to be done for 'all'.
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests/unittests'
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests'
  CC       base64.o
  CC       sc-test.o
  CCLD     base64
  CC       lottery.o
  CCLD     lottery
  CC       p15dump.o
  CC       print.o
  CCLD     p15dump
  CC       pintest.o
  CCLD     pintest
  CC       prngtest.o
  CCLD     prngtest
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests'
Making all in smm
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/smm'
make[7]: Nothing to be done for 'all'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/smm'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src'
make[7]: Nothing to be done for 'all-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src'
Making all in win32
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/win32'
make[6]: Nothing to be done for 'all'.
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/win32'
Making all in doc
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/doc'
Making all in tools
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/doc/tools'
sed -e 's|@pkgdatadir[@]|/usr/share/opensc|g' < piv-tool.1.xml \
| xsltproc --nonet --path "./..:/usr/share/xml/docbook/stylesheet/nwalsh/manpages" --xinclude -o piv-tool.1 man.xsl piv-tool.1.xml
Note: Writing piv-tool.1
sed -e 's|@pkgdatadir[@]|/usr/share/opensc|g' < opensc-asn1.1.xml \
| xsltproc --nonet --path "./..:/usr/share/xml/docbook/stylesheet/nwalsh/manpages" --xinclude -o opensc-asn1.1 man.xsl opensc-asn1.1.xml
Note: Writing opensc-asn1.1
sed -e 's|@pkgdatadir[@]|/usr/share/opensc|g' < cardos-tool.1.xml \
| xsltproc --nonet --path "./..:/usr/share/xml/docbook/stylesheet/nwalsh/manpages" --xinclude -o cardos-tool.1 man.xsl cardos-tool.1.xml
Note: Writing cardos-tool.1
sed -e 's|@pkgdatadir[@]|/usr/share/opensc|g' < sc-hsm-tool.1.xml \
| xsltproc --nonet --path "./..:/usr/share/xml/docbook/stylesheet/nwalsh/manpages" --xinclude -o sc-hsm-tool.1 man.xsl sc-hsm-tool.1.xml
Note: Writing sc-hsm-tool.1
sed -e 's|@pkgdatadir[@]|/usr/share/opensc|g' < opensc-notify.1.xml \
| xsltproc --nonet --path "./..:/usr/share/xml/docbook/stylesheet/nwalsh/manpages" --xinclude -o opensc-notify.1 man.xsl opensc-notify.1.xml
Note: Writing opensc-notify.1
sed -e 's|@pkgdatadir[@]|/usr/share/opensc|g' < westcos-tool.1.xml \
| xsltproc --nonet --path "./..:/usr/share/xml/docbook/stylesheet/nwalsh/manpages" --xinclude -o westcos-tool.1 man.xsl westcos-tool.1.xml
Note: Writing westcos-tool.1
sed -e 's|@pkgdatadir[@]|/usr/share/opensc|g' < opensc-explorer.1.xml \
| xsltproc --nonet --path "./..:/usr/share/xml/docbook/stylesheet/nwalsh/manpages" --xinclude -o opensc-explorer.1 man.xsl opensc-explorer.1.xml
Note: Writing opensc-explorer.1
sed -e 's|@pkgdatadir[@]|/usr/share/opensc|g' < npa-tool.1.xml \
| xsltproc --nonet --path "./..:/usr/share/xml/docbook/stylesheet/nwalsh/manpages" --xinclude -o npa-tool.1 man.xsl npa-tool.1.xml
Note: Writing npa-tool.1
sed -e 's|@pkgdatadir[@]|/usr/share/opensc|g' < cryptoflex-tool.1.xml \
| xsltproc --nonet --path "./..:/usr/share/xml/docbook/stylesheet/nwalsh/manpages" --xinclude -o cryptoflex-tool.1 man.xsl cryptoflex-tool.1.xml
Note: Writing cryptoflex-tool.1
sed -e 's|@pkgdatadir[@]|/usr/share/opensc|g' < openpgp-tool.1.xml \
| xsltproc --nonet --path "./..:/usr/share/xml/docbook/stylesheet/nwalsh/manpages" --xinclude -o openpgp-tool.1 man.xsl openpgp-tool.1.xml
Note: Writing openpgp-tool.1
sed -e 's|@pkgdatadir[@]|/usr/share/opensc|g' < eidenv.1.xml \
| xsltproc --nonet --path "./..:/usr/share/xml/docbook/stylesheet/nwalsh/manpages" --xinclude -o eidenv.1 man.xsl eidenv.1.xml
Note: Writing eidenv.1
sed -e 's|@pkgdatadir[@]|/usr/share/opensc|g' < pkcs11-tool.1.xml \
| xsltproc --nonet --path "./..:/usr/share/xml/docbook/stylesheet/nwalsh/manpages" --xinclude -o pkcs11-tool.1 man.xsl pkcs11-tool.1.xml
Note: Writing pkcs11-tool.1
sed -e 's|@pkgdatadir[@]|/usr/share/opensc|g' < pkcs15-init.1.xml \
| xsltproc --nonet --path "./..:/usr/share/xml/docbook/stylesheet/nwalsh/manpages" --xinclude -o pkcs15-init.1 man.xsl pkcs15-init.1.xml
Note: Writing pkcs15-init.1
sed -e 's|@pkgdatadir[@]|/usr/share/opensc|g' < gids-tool.1.xml \
| xsltproc --nonet --path "./..:/usr/share/xml/docbook/stylesheet/nwalsh/manpages" --xinclude -o gids-tool.1 man.xsl gids-tool.1.xml
Note: Writing gids-tool.1
sed -e 's|@pkgdatadir[@]|/usr/share/opensc|g' < dnie-tool.1.xml \
| xsltproc --nonet --path "./..:/usr/share/xml/docbook/stylesheet/nwalsh/manpages" --xinclude -o dnie-tool.1 man.xsl dnie-tool.1.xml
Note: Writing dnie-tool.1
sed -e 's|@pkgdatadir[@]|/usr/share/opensc|g' < iasecc-tool.1.xml \
| xsltproc --nonet --path "./..:/usr/share/xml/docbook/stylesheet/nwalsh/manpages" --xinclude -o iasecc-tool.1 man.xsl iasecc-tool.1.xml
Note: Writing iasecc-tool.1
sed -e 's|@pkgdatadir[@]|/usr/share/opensc|g' < pkcs15-crypt.1.xml \
| xsltproc --nonet --path "./..:/usr/share/xml/docbook/stylesheet/nwalsh/manpages" --xinclude -o pkcs15-crypt.1 man.xsl pkcs15-crypt.1.xml
Note: Writing pkcs15-crypt.1
sed -e 's|@pkgdatadir[@]|/usr/share/opensc|g' < egk-tool.1.xml \
| xsltproc --nonet --path "./..:/usr/share/xml/docbook/stylesheet/nwalsh/manpages" --xinclude -o egk-tool.1 man.xsl egk-tool.1.xml
Note: Writing egk-tool.1
sed -e 's|@pkgdatadir[@]|/usr/share/opensc|g' < goid-tool.1.xml \
| xsltproc --nonet --path "./..:/usr/share/xml/docbook/stylesheet/nwalsh/manpages" --xinclude -o goid-tool.1 man.xsl goid-tool.1.xml
Note: Writing goid-tool.1
sed -e 's|@pkgdatadir[@]|/usr/share/opensc|g' < opensc-tool.1.xml \
| xsltproc --nonet --path "./..:/usr/share/xml/docbook/stylesheet/nwalsh/manpages" --xinclude -o opensc-tool.1 man.xsl opensc-tool.1.xml
Note: Writing opensc-tool.1
sed -e 's|@pkgdatadir[@]|/usr/share/opensc|g' < pkcs15-tool.1.xml \
| xsltproc --nonet --path "./..:/usr/share/xml/docbook/stylesheet/nwalsh/manpages" --xinclude -o pkcs15-tool.1 man.xsl pkcs15-tool.1.xml
Note: Writing pkcs15-tool.1
sed -e 's|@pkgdatadir[@]|/usr/share/opensc|g' < netkey-tool.1.xml \
| xsltproc --nonet --path "./..:/usr/share/xml/docbook/stylesheet/nwalsh/manpages" --xinclude -o netkey-tool.1 man.xsl netkey-tool.1.xml
Note: Writing netkey-tool.1
sed -e 's|@pkgdatadir[@]|/usr/share/opensc|g' < pkcs11-register.1.xml \
| xsltproc --nonet --path "./..:/usr/share/xml/docbook/stylesheet/nwalsh/manpages" --xinclude -o pkcs11-register.1 man.xsl pkcs11-register.1.xml
Note: Writing pkcs11-register.1
piv-tool.1.xml piv-tool
opensc-asn1.1.xml opensc-asn1
cardos-tool.1.xml cardos-tool
sc-hsm-tool.1.xml sc-hsm-tool
opensc-notify.1.xml opensc-notify
westcos-tool.1.xml westcos-tool
opensc-explorer.1.xml opensc-explorer
npa-tool.1.xml npa-tool
cryptoflex-tool.1.xml cryptoflex-tool
openpgp-tool.1.xml openpgp-tool
eidenv.1.xml eidenv
pkcs11-tool.1.xml pkcs11-tool
pkcs15-init.1.xml pkcs15-init
gids-tool.1.xml gids-tool
dnie-tool.1.xml dnie-tool
iasecc-tool.1.xml iasecc-tool
pkcs15-crypt.1.xml pkcs15-crypt
egk-tool.1.xml egk-tool
goid-tool.1.xml goid-tool
opensc-tool.1.xml opensc-tool
pkcs15-tool.1.xml pkcs15-tool
netkey-tool.1.xml netkey-tool
pkcs11-register.1.xml pkcs11-register
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/doc/tools'
Making all in files
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/doc/files'
sed -e 's|@pkgdatadir[@]|/usr/share/opensc|g' < pkcs15-profile.5.xml \
| xsltproc --nonet --path "./..:/usr/share/xml/docbook/stylesheet/nwalsh/manpages" --xinclude -o pkcs15-profile.5 man.xsl pkcs15-profile.5.xml
Warn: meta author : no refentry/info/author                        pkcs15-profile
Note: meta author : see http://docbook.sf.net/el/author            pkcs15-profile
Warn: meta author : no author data, so inserted a fixme            pkcs15-profile
Note: Writing pkcs15-profile.5
sed \
	-e 's|@sysconfdir[@]|/etc|g' \
	-e 's|@docdir[@]|/usr/share/doc/opensc|g' \
	-e 's|@libdir[@]|/usr/lib|g' \
	-e 's|@DYN_LIB_EXT[@]|.so|g' \
	-e 's|@DEFAULT_PCSC_PROVIDER[@]|libpcsclite.so.1|g' \
	-e 's|@PROFILE_DIR_DEFAULT[@]|/usr/share/opensc|g' \
	-e 's|@DEFAULT_SM_MODULE[@]|libsmm-local.so|g' \
	< opensc.conf.5.xml.in > opensc.conf.5.xml
xsltproc --nonet --path "./..:/usr/share/xml/docbook/stylesheet/nwalsh/manpages" --xinclude -o opensc.conf.5 man.xsl opensc.conf.5.xml
Warn: meta author : no refentry/info/author                        opensc.conf
Note: meta author : see http://docbook.sf.net/el/author            opensc.conf
Warn: meta author : no author data, so inserted a fixme            opensc.conf
Note: Writing opensc.conf.5
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/doc/files'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/doc'
make[7]: Nothing to be done for 'all-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/doc'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/doc'
Making all in MacOSX
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/MacOSX'
make[6]: Nothing to be done for 'all'.
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/MacOSX'
Making all in tests
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/tests'
make[6]: Nothing to be done for 'all'.
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/tests'
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0'
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0'
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0'
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0'
Making install in etc
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/etc'
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/etc'
make  install-exec-hook
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/etc'
/usr/bin/mkdir -p "/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/etc"
if [ -f "/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/etc/opensc.conf" ]; then \
	/openwrt/staging_dir/host/bin/install -c -m 644 ./opensc.conf "/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/etc/opensc.conf.new"; \
else \
	/openwrt/staging_dir/host/bin/install -c -m 644 ./opensc.conf "/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/etc/opensc.conf"; \
fi
/usr/bin/mkdir -p "/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/share/doc/opensc"
/openwrt/staging_dir/host/bin/install -c -m 644 opensc.conf.example "/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/share/doc/opensc/opensc.conf";
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/etc'
make[6]: Nothing to be done for 'install-data-am'.
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/etc'
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/etc'
Making install in src
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src'
Making install in common
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/common'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/common'
make[7]: Nothing to be done for 'install-exec-am'.
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/common'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/common'
Making install in scconf
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/scconf'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/scconf'
make[7]: Nothing to be done for 'install-exec-am'.
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/scconf'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/scconf'
Making install in ui
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/ui'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/ui'
make[7]: Nothing to be done for 'install-exec-am'.
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/ui'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/ui'
Making install in pkcs15init
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/pkcs15init'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/pkcs15init'
make[7]: Nothing to be done for 'install-exec-am'.
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/share/opensc'
 /openwrt/staging_dir/host/bin/install -c -m 644 cyberflex.profile flex.profile gpk.profile miocos.profile cardos.profile incrypto34.profile jcop.profile oberthur.profile starcos.profile setcos.profile pkcs15.profile muscle.profile rutoken.profile asepcos.profile entersafe.profile epass2003.profile rutoken_ecp.profile rutoken_lite.profile westcos.profile myeid.profile authentic.profile iasecc.profile ias_adele_admin1.profile ias_adele_admin2.profile ias_adele_common.profile iasecc_generic_pki.profile iasecc_admin_eid.profile iasecc_generic_oberthur.profile openpgp.profile sc-hsm.profile isoApplet.profile gids.profile '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/share/opensc'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/pkcs15init'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/pkcs15init'
Making install in sm
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/sm'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/sm'
make[7]: Nothing to be done for 'install-exec-am'.
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/sm'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/sm'
Making install in libopensc
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/libopensc'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/libopensc'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libopensc.la '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libopensc.so.7.0.0 /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/lib/libopensc.so.7.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/lib && { ln -s -f libopensc.so.7.0.0 libopensc.so.7 || { rm -f libopensc.so.7 && ln -s libopensc.so.7.0.0 libopensc.so.7; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/lib && { ln -s -f libopensc.so.7.0.0 libopensc.so || { rm -f libopensc.so && ln -s libopensc.so.7.0.0 libopensc.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libopensc.lai /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/lib/libopensc.la
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libopensc.a /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/lib/libopensc.a
OpenWrt-libtool: install: chmod 644 /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/lib/libopensc.a
OpenWrt-libtool: install: mips-openwrt-linux-musl-gcc-ranlib /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/lib/libopensc.a
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/libopensc'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/libopensc'
Making install in pkcs11
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/pkcs11'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/pkcs11'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   opensc-pkcs11.la pkcs11-spy.la onepin-opensc-pkcs11.la '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `opensc-pkcs11.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/pkcs11; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/libtool  --silent --tag CC --mode=relink ccache_cc -pthread -DPKCS11_THREAD_LOCKING -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0=opensc-0.21.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -export-symbols ./pkcs11.exports -module -shared -avoid-version -no-undefined -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -o opensc-pkcs11.la -rpath /usr/lib opensc_pkcs11_la-pkcs11-global.lo opensc_pkcs11_la-pkcs11-session.lo opensc_pkcs11_la-pkcs11-object.lo opensc_pkcs11_la-misc.lo opensc_pkcs11_la-slot.lo opensc_pkcs11_la-mechanism.lo opensc_pkcs11_la-openssl.lo opensc_pkcs11_la-framework-pkcs15.lo opensc_pkcs11_la-framework-pkcs15init.lo opensc_pkcs11_la-debug.lo opensc_pkcs11_la-pkcs11-display.lo ../../src/libopensc/libopensc.la ../../src/common/libscdl.la ../../src/common/libcompat.la -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install)
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/opensc-pkcs11.soT /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/lib/opensc-pkcs11.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/opensc-pkcs11.lai /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/lib/opensc-pkcs11.la
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/pkcs11-spy.so /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/lib/pkcs11-spy.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/pkcs11-spy.lai /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/lib/pkcs11-spy.la
OpenWrt-libtool: install: warning: relinking `onepin-opensc-pkcs11.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/pkcs11; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/libtool  --silent --tag CC --mode=relink ccache_cc -DMODULE_APP_NAME=\"onepin-opensc-pkcs11\" -pthread -DPKCS11_THREAD_LOCKING -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0=opensc-0.21.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -export-symbols ./pkcs11.exports -module -shared -avoid-version -no-undefined -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -o onepin-opensc-pkcs11.la -rpath /usr/lib onepin_opensc_pkcs11_la-pkcs11-global.lo onepin_opensc_pkcs11_la-pkcs11-session.lo onepin_opensc_pkcs11_la-pkcs11-object.lo onepin_opensc_pkcs11_la-misc.lo onepin_opensc_pkcs11_la-slot.lo onepin_opensc_pkcs11_la-mechanism.lo onepin_opensc_pkcs11_la-openssl.lo onepin_opensc_pkcs11_la-framework-pkcs15.lo onepin_opensc_pkcs11_la-framework-pkcs15init.lo onepin_opensc_pkcs11_la-debug.lo onepin_opensc_pkcs11_la-pkcs11-display.lo ../../src/libopensc/libopensc.la ../../src/common/libscdl.la ../../src/common/libcompat.la -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install)
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/onepin-opensc-pkcs11.soT /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/lib/onepin-opensc-pkcs11.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/onepin-opensc-pkcs11.lai /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/lib/onepin-opensc-pkcs11.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
make  install-exec-hook
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/pkcs11'
/usr/bin/mkdir -p "/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/lib/pkcs11"
for l in opensc-pkcs11.so onepin-opensc-pkcs11.so pkcs11-spy.so; do \
	rm -f "/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/lib/pkcs11/$l"; \
	ln -s ../$l "/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/lib/pkcs11/$l"; \
done
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/pkcs11'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/lib/pkgconfig'
 /openwrt/staging_dir/host/bin/install -c -m 644 opensc-pkcs11.pc '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/lib/pkgconfig'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/pkcs11'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/pkcs11'
Making install in tools
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tools'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tools'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c opensc-tool opensc-explorer opensc-notify pkcs15-tool pkcs15-crypt pkcs11-tool pkcs11-register cardos-tool eidenv openpgp-tool iasecc-tool egk-tool opensc-asn1 goid-tool '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `../../src/libopensc/libopensc.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/opensc-tool /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/bin/opensc-tool
OpenWrt-libtool: install: warning: `../../src/libopensc/libopensc.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/opensc-explorer /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/bin/opensc-explorer
OpenWrt-libtool: install: warning: `../../src/libopensc/libopensc.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/opensc-notify /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/bin/opensc-notify
OpenWrt-libtool: install: warning: `../../src/libopensc/libopensc.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/pkcs15-tool /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/bin/pkcs15-tool
OpenWrt-libtool: install: warning: `../../src/libopensc/libopensc.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/pkcs15-crypt /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/bin/pkcs15-crypt
OpenWrt-libtool: install: warning: `../../src/libopensc/libopensc.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/pkcs11-tool /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/bin/pkcs11-tool
OpenWrt-libtool: install: warning: `../../src/libopensc/libopensc.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/pkcs11-register /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/bin/pkcs11-register
OpenWrt-libtool: install: warning: `../../src/libopensc/libopensc.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/cardos-tool /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/bin/cardos-tool
OpenWrt-libtool: install: warning: `../../src/libopensc/libopensc.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/eidenv /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/bin/eidenv
OpenWrt-libtool: install: warning: `../../src/libopensc/libopensc.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/openpgp-tool /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/bin/openpgp-tool
OpenWrt-libtool: install: warning: `../../src/libopensc/libopensc.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/iasecc-tool /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/bin/iasecc-tool
OpenWrt-libtool: install: warning: `../../src/libopensc/libopensc.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/egk-tool /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/bin/egk-tool
OpenWrt-libtool: install: warning: `../../src/libopensc/libopensc.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/opensc-asn1 /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/bin/opensc-asn1
OpenWrt-libtool: install: warning: `../../src/libopensc/libopensc.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/goid-tool /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/bin/goid-tool
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/share/applications'
 /openwrt/staging_dir/host/bin/install -c -m 644 org.opensc.notify.desktop '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/share/applications'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/etc/xdg/autostart'
 /openwrt/staging_dir/host/bin/install -c -m 644 pkcs11-register.desktop '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/etc/xdg/autostart'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tools'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tools'
Making install in minidriver
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/minidriver'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/minidriver'
make  install-exec-hook
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/minidriver'
make[8]: Nothing to be done for 'install-exec-hook'.
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/minidriver'
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/minidriver'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/minidriver'
Making install in tests
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests'
Making install in regression
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests/regression'
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests/regression'
make[8]: Nothing to be done for 'install-exec-am'.
make[8]: Nothing to be done for 'install-data-am'.
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests/regression'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests/regression'
Making install in p11test
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests/p11test'
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests/p11test'
make[8]: Nothing to be done for 'install-exec-am'.
make[8]: Nothing to be done for 'install-data-am'.
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests/p11test'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests/p11test'
Making install in fuzzing
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests/fuzzing'
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests/fuzzing'
make[8]: Nothing to be done for 'install-exec-am'.
make[8]: Nothing to be done for 'install-data-am'.
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests/fuzzing'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests/fuzzing'
Making install in unittests
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests/unittests'
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests/unittests'
make[8]: Nothing to be done for 'install-exec-am'.
make[8]: Nothing to be done for 'install-data-am'.
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests/unittests'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests/unittests'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests'
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests'
make[8]: Nothing to be done for 'install-exec-am'.
make[8]: Nothing to be done for 'install-data-am'.
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/tests'
Making install in smm
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/smm'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/smm'
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/smm'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src/smm'
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src'
make[7]: Nothing to be done for 'install-exec-am'.
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src'
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/src'
Making install in win32
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/win32'
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/win32'
make  install-exec-hook
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/win32'
make[7]: Nothing to be done for 'install-exec-hook'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/win32'
make[6]: Nothing to be done for 'install-data-am'.
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/win32'
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/win32'
Making install in doc
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/doc'
Making install in tools
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/doc/tools'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/doc/tools'
make[7]: Nothing to be done for 'install-exec-am'.
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/etc/bash_completion.d'
 /openwrt/staging_dir/host/bin/install -c -m 644 piv-tool cardos-tool opensc-notify sc-hsm-tool opensc-asn1 westcos-tool npa-tool cryptoflex-tool openpgp-tool eidenv iasecc-tool pkcs11-tool pkcs15-init gids-tool dnie-tool goid-tool pkcs15-crypt egk-tool opensc-explorer opensc-tool pkcs15-tool netkey-tool pkcs11-register '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/etc/bash_completion.d'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/man/man1'
 /openwrt/staging_dir/host/bin/install -c -m 644 piv-tool.1 cardos-tool.1 opensc-notify.1 sc-hsm-tool.1 opensc-asn1.1 westcos-tool.1 npa-tool.1 cryptoflex-tool.1 openpgp-tool.1 eidenv.1 iasecc-tool.1 pkcs11-tool.1 pkcs15-init.1 gids-tool.1 dnie-tool.1 goid-tool.1 pkcs15-crypt.1 egk-tool.1 opensc-explorer.1 opensc-tool.1 pkcs15-tool.1 netkey-tool.1 pkcs11-register.1 '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/man/man1'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/doc/tools'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/doc/tools'
Making install in files
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/doc/files'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/doc/files'
make[7]: Nothing to be done for 'install-exec-am'.
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/man/man5'
 /openwrt/staging_dir/host/bin/install -c -m 644 pkcs15-profile.5 opensc.conf.5 '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/man/man5'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/doc/files'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/doc/files'
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/doc'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/doc'
make[7]: Nothing to be done for 'install-exec-am'.
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/doc'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/doc'
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/doc'
Making install in MacOSX
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/MacOSX'
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/MacOSX'
make[6]: Nothing to be done for 'install-exec-am'.
make[6]: Nothing to be done for 'install-data-am'.
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/MacOSX'
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/MacOSX'
Making install in tests
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/tests'
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/tests'
make[6]: Nothing to be done for 'install-exec-am'.
make[6]: Nothing to be done for 'install-data-am'.
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/tests'
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/tests'
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0'
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0'
make[6]: Nothing to be done for 'install-exec-am'.
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/share/doc/opensc'
 /openwrt/staging_dir/host/bin/install -c -m 644 NEWS '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/share/doc/opensc'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0'
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0'
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0'
cp: cannot stat '/openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/ipkg-install/usr/lib/libsmm-local.so*': No such file or directory
make[3]: *** [Makefile:226: /openwrt/build_dir/target-mips_24kc_musl/opensc-0.21.0/.pkgdir/libopensc.installed] Error 1
```
