---
title: "compile.37"
date: 2021-06-20 22:39:07.404429
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
make package/feeds/packages/curl/compile -j$(nproc) || make package/feeds/packages/curl/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/200-no_docs_tests.patch using plaintext: 
patching file Makefile.am
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force -I m4
autoreconf: configure.ac: tracing
autoreconf: configure.ac: subdirectory ares not present
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
OpenWrt-libtoolize: Remember to add `LT_INIT' to configure.ac.
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
Makefile.am:309: error: '#' comment at start of rule is unportable
Makefile.am:310: error: '#' comment at start of rule is unportable
autoreconf: /openwrt/staging_dir/host/bin/automake failed with exit status: 1
configure: loading site script /openwrt/include/site/mips
checking whether to enable maintainer-specific portions of Makefiles... no
checking whether make supports nested variables... yes
checking whether to enable debug build options... no
checking whether to enable compiler optimizer... (assumed) yes
checking whether to enable strict compiler warnings... no
checking whether to enable compiler warnings as errors... no
checking whether to enable curl debug memory tracking... no
checking whether to enable hiding of library internal symbols... yes
checking whether to enable c-ares for DNS lookups... no
checking whether to disable dependency on -lrt... (assumed no)
checking whether to enable ECH support... no
checking for path separator... :
checking for sed... /openwrt/staging_dir/host/bin/sed
checking for grep... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
configure: using CFLAGS: -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/curl-7.77.0=curl-7.77.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -ffunction-sections -fdata-sections 
configure: CFLAGS note: CFLAGS should only be used to specify C compiler flags, not macro definitions. Use CPPFLAGS for: -D_FORTIFY_SOURCE=1
configure: CFLAGS note: CFLAGS should only be used to specify C compiler flags, not macro definitions. Use CPPFLAGS for: -DPIC
configure: WARNING: Continuing even with errors mentioned immediately above this line.
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
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
checking how to run the C preprocessor... ccache_cc -E
checking for a sed that does not truncate output... (cached) /openwrt/staging_dir/host/bin/sed
checking for code coverage support... no
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking for style of include used by make... GNU
checking dependency style of ccache_cc... gcc3
checking curl version... 7.77.0
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking for grep that handles long lines and -e... (cached) /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking if OS is AIX (to define _ALL_SOURCE)... no
checking if _THREAD_SAFE is already defined... no
checking if _THREAD_SAFE is actually needed... no
checking if _THREAD_SAFE is onwards defined... no
checking if _REENTRANT is already defined... no
checking if _REENTRANT is actually needed... no
checking if _REENTRANT is onwards defined... no
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking how to print strings... printf
checking for a sed that does not truncate output... (cached) /openwrt/staging_dir/host/bin/sed
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
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
checking whether to build static libraries... yes
checking whether to build shared libraries with -version-info... yes
checking whether to build shared libraries with -no-undefined... no
checking whether to build shared libraries with -mimpure-text... no
checking whether to build shared libraries with PIC... yes
checking whether to build static libraries with PIC... no
checking whether to build shared libraries only... no
checking whether to build static libraries only... no
checking for inline... inline
checking if cpp -P is needed... yes
checking if cpp -P works... yes
checking if compiler is DEC/Compaq/HP C... no
checking if compiler is HP-UX C... no
checking if compiler is IBM C... no
checking if compiler is Intel C... no
checking if compiler is clang... no
checking if compiler is GNU C... yes
checking if compiler is LCC... no
checking if compiler is SGI MIPSpro C... no
checking if compiler is SGI MIPS C... no
checking if compiler is SunPro C... no
checking if compiler is Tiny C... no
checking if compiler is Watcom C... no
checking if compiler accepts some basic options... yes
configure: compiler options added: -Werror-implicit-function-declaration 
checking if compiler accepts debug disabling options... yes
configure: compiler options added: 
checking if compiler optimizer assumed setting might be used... no
checking if compiler accepts strict warning options... yes
configure: compiler options added: -Wno-system-headers 
checking if compiler halts on compilation errors... yes
checking if compiler halts on negative sized arrays... yes
checking if compiler halts on function prototype mismatch... yes
checking if compiler supports hiding library internal symbols... yes
checking for windows.h... no
checking whether build target is a native Windows one... no
checking whether build target supports WIN32 file API... no
checking whether build target supports WIN32 crypto API... no
checking for good-to-use Darwin CFLAGS... no
checking whether to link macOS SystemConfiguration framework... no
checking to see if the compiler supports __builtin_available()... no
checking whether to support http... yes
checking whether to support ftp... yes
checking whether to support file... yes
checking whether to support ldap... yes
checking whether to support ldaps... yes
checking whether to support rtsp... no
checking whether to support proxies... yes
checking whether to support dict... no
checking whether to support telnet... no
checking whether to support tftp... yes
checking whether to support pop3... no
checking whether to support imap... no
checking whether to support smb... no
checking whether to support smtp... no
checking whether to support gopher... no
checking whether to support mqtt... no
checking whether to provide built-in manual... no
checking whether to enable generation of C code... no
checking whether to use libgcc... no
checking if X/Open network library is required... no
checking for gethostbyname... yes
checking for windows.h... (cached) no
checking for winsock.h... (cached) no
checking for winsock2.h... (cached) no
checking for proto/bsdsocket.h... no
checking for connect in libraries... yes
checking for sys/types.h... (cached) yes
checking sys/time.h usability... yes
checking sys/time.h presence... yes
checking for sys/time.h... yes
checking for monotonic clock_gettime... yes
checking for clock_gettime in libraries... no additional lib required
configure: WARNING: zlib disabled
checking for BrotliDecoderDecompress in -lbrotlidec... no
checking brotli/decode.h usability... no
checking brotli/decode.h presence... no
checking for brotli/decode.h... no
checking for lber.h... yes
checking for ldap.h... yes
checking for ldapssl.h... no
checking for ldap_ssl.h... no
checking for LDAP libraries... -lldap -llber
checking for ldap_url_parse... yes
checking for ldap_init_fd... yes
checking whether to enable IPv6... yes
checking if struct sockaddr_in6 has sin6_scope_id member... yes
checking if argv can be written to... no
configure: WARNING: the previous check could not be made default was used
checking if GSS-API support is requested... no
checking whether to enable Windows native SSL/TLS... no
checking whether to enable Secure Transport... no
checking whether to enable Amiga native SSL/TLS (AmiSSL)... no
configure: error: /openwrt/staging_dir/target-mips_24kc_musl/usr is a bad --with-openssl prefix!
make[3]: *** [Makefile:188: /openwrt/build_dir/target-mips_24kc_musl/curl-7.77.0/.configured_10cb4f77e275e6294b74a4d670249097] Error 1
```
