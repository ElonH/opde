---
title: "compile.37"
date: 2021-06-20 22:38:00.053200
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
make package/feeds/packages/shadowsocksr-libev/compile -j$(nproc) || make package/feeds/packages/shadowsocksr-libev/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/0001-Add-ss-server-and-ss-check.patch using plaintext: 
patching file .gitignore
patching file Makefile.am
patching file Makefile.in
patching file configure
patching file configure.ac

Applying ./patches/0002-Revert-verify_simple-and-auth_simple.patch using plaintext: 
patching file src/obfs/obfs.c

Applying ./patches/0003-Refine-Usage.patch using plaintext: 
patching file src/utils.c

Applying ./patches/100-fix-gcc-10.patch using plaintext: 
patching file src/http.h
patching file src/tls.h

Applying ./patches/101-Fix-Werror-sizeof-pointer-memaccess.patch using plaintext: 
patching file src/local.c

Applying ./patches/102-Read-listening-mode-from-config.patch using plaintext: 
patching file src/jconf.c
patching file src/redir.c

Applying ./patches/103-Add-TPROXY-support-for-TCP-ssr-redir.patch using plaintext: 
patching file completions/bash/ss-redir
patching file src/jconf.c
patching file src/jconf.h
patching file src/redir.c
patching file src/utils.c
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force -I m4
autoreconf: configure.ac: tracing
autoreconf: configure.ac: adding subdirectory libsodium to autoreconf
autoreconf: Entering directory `libsodium'
autoreconf: running: /openwrt/staging_dir/host/bin/libtoolize --install --force
OpenWrt-libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, `build-aux'.
OpenWrt-libtoolize: linking file `build-aux/config.guess'
OpenWrt-libtoolize: linking file `build-aux/config.sub'
OpenWrt-libtoolize: linking file `build-aux/install-sh'
OpenWrt-libtoolize: linking file `build-aux/ltmain.sh'
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
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: configure.ac: not using Autoheader
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
configure.ac:150: installing 'build-aux/compile'
autoreconf: Leaving directory `libsodium'
OpenWrt-libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, `auto'.
OpenWrt-libtoolize: linking file `auto/config.guess'
OpenWrt-libtoolize: linking file `auto/config.sub'
OpenWrt-libtoolize: linking file `auto/install-sh'
OpenWrt-libtoolize: linking file `auto/ltmain.sh'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `m4'.
OpenWrt-libtoolize: linking file `m4/libtool.m4'
OpenWrt-libtoolize: linking file `m4/ltoptions.m4'
OpenWrt-libtoolize: linking file `m4/ltsugar.m4'
OpenWrt-libtoolize: linking file `m4/ltversion.m4'
OpenWrt-libtoolize: linking file `m4/lt~obsolete.m4'
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: Leaving directory `.'
configure: loading site script /openwrt/include/site/mips
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
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking for style of include used by make... GNU
checking whether make supports nested variables... yes
checking dependency style of ccache_cc... gcc3
checking for mips-openwrt-linux-ar... mips-openwrt-linux-musl-gcc-ar
checking the archiver (mips-openwrt-linux-musl-gcc-ar) interface... ar
checking whether make supports nested variables... (cached) yes
checking whether to enable maintainer-specific portions of Makefiles... no
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
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
checking for mips-openwrt-linux-ar... (cached) mips-openwrt-linux-musl-gcc-ar
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
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking for shl_load... no
checking for shl_load in -ldld... no
checking for dlopen... yes
checking whether a program can dlopen itself... cross
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... no
checking whether to build static libraries... yes
checking for pcre-config... pcre-config
checking for pcre headers in /openwrt/staging_dir/target-mips_24kc_musl/usr/include... ok
configure: adding /openwrt/staging_dir/target-mips_24kc_musl/usr/lib  to RPATH
checking for library containing pcre_exec... -lpcre
checking pcre.h usability... yes
checking pcre.h presence... yes
checking for pcre.h... yes
checking pcre/pcre.h usability... no
checking pcre/pcre.h presence... no
checking for pcre/pcre.h... no
checking for mips-openwrt-linux-gcc... (cached) ccache_cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether ccache_cc accepts -g... (cached) yes
checking for ccache_cc option to accept ISO C89... (cached) none needed
checking whether ccache_cc understands -c and -o together... (cached) yes
checking whether ln -s works... yes
checking whether make sets $(MAKE)... (cached) yes
checking for thread local storage (TLS) class... __thread
checking zlib.h usability... yes
checking zlib.h presence... yes
checking for zlib.h... yes
checking for compress2 in -lz... yes
checking for dlopen... (cached) yes
checking openssl/evp.h usability... no
checking openssl/evp.h presence... no
checking for openssl/evp.h... no
configure: error: OpenSSL header files not found.
make[3]: *** [Makefile:66: /openwrt/build_dir/target-mips_24kc_musl/shadowsocksr-libev-2.5.6/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
