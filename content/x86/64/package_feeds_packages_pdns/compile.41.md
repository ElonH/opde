---
title: "compile.41"
date: 2021-06-23 23:13:13.736659
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
make package/feeds/packages/pdns/compile -j$(nproc) || make package/feeds/packages/pdns/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/100-pdns-disable-pdns.conf-dist.patch using plaintext: 
patching file pdns/Makefile.am
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-x86_64_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal -I m4 -I . --force -I m4
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
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-x86_64_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-x86_64_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
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
checking whether UID '1000' is supported by ustar format... yes
checking whether GID '1000' is supported by ustar format... yes
checking how to create a ustar tar archive... gnutar
checking whether make supports nested variables... (cached) yes
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-openwrt-linux-gnu
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
checking for bison... bison -y
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking if bison is the parser generator... yes
checking for flex... flex
checking lex output file root... lex.yy
checking lex library... none needed
checking whether yytext is a pointer... no
checking if the lexer is flex... yes
checking whether make sets $(MAKE)... (cached) yes
checking whether we are using the GNU C++ compiler... yes
checking whether ccache_cxx accepts -g... yes
checking dependency style of ccache_cxx... gcc3
checking whether -latomic is needed for __atomic builtins... no
checking for pthread_np.h... no
checking for 2-arg pthread_setname_np... yes
checking pkg-config is at least version 0.9.0... yes
checking for grep that handles long lines and -e... (cached) /openwrt/staging_dir/host/bin/grep
checking which Lua implementation to use... lua
checking for LUA... yes
checking how to run the C++ preprocessor... ccache_cxx -E
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
checking lua.hpp usability... yes
checking lua.hpp presence... yes
checking for lua.hpp... yes
checking whether ccache_cxx supports C++11 features by default... yes
checking whether we will enable compiler security checks... yes
checking whether C++ compiler handles -Werror -Wunknown-warning-option... no
checking whether C++ compiler handles -pie... yes
checking whether C++ compiler handles -fstack-protector... yes
checking whether C++ compiler handles --param ssp-buffer-size=4... yes
checking whether C++ compiler handles -D_FORTIFY_SOURCE=2... no
checking for how to force completely read-only GOT table... -Wl,-z -Wl,relro -Wl,-z -Wl,now
checking for library containing inet_aton... none required
checking for library containing gethostbyname... none required
checking for library containing socket... none required
checking for library containing gethostent... none required
checking for recvmmsg... yes
checking for sendmmsg... yes
checking for accept4... yes
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
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
checking for shl_load... no
checking for shl_load in -ldld... no
checking for dlopen... yes
checking whether a program can dlopen itself... cross
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... no
checking how to run the C++ preprocessor... ccache_cxx -E
checking for ld used by ccache_cxx... x86_64-openwrt-linux-musl-ld -m elf_x86_64
checking if the linker (x86_64-openwrt-linux-musl-ld -m elf_x86_64) is GNU ld... yes
checking whether the ccache_cxx linker (x86_64-openwrt-linux-musl-ld -m elf_x86_64) supports shared libraries... yes
checking for ccache_cxx option to produce PIC... -fPIC -DPIC
checking if ccache_cxx PIC flag -fPIC -DPIC works... yes
checking if ccache_cxx static flag -static works... yes
checking if ccache_cxx supports -c -o file.o... yes
checking if ccache_cxx supports -c -o file.o... (cached) yes
checking whether the ccache_cxx linker (x86_64-openwrt-linux-musl-ld -m elf_x86_64) supports shared libraries... yes
checking dynamic linker characteristics... (cached) GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether struct tm is in sys/time.h or time.h... time.h
checking for tm_gmtoff in struct tm... yes
checking pkg-config is at least version 0.9.0... yes
checking sys/mman.h usability... yes
checking sys/mman.h presence... yes
checking for sys/mman.h... yes
checking for mmap... yes
checking whether we will be linking in libsodium... no
checking whether we will be linking in libdecaf... no
checking for x86_64-openwrt-linux-pkg-config... /openwrt/staging_dir/host/bin/pkg-config
checking whether compiling and linking against OpenSSL's libcrypto works... yes
checking for RAND_bytes... yes
checking for RAND_pseudo_bytes... yes
checking for CRYPTO_memcmp... yes
checking for OPENSSL_init_crypto... yes
checking for EVP_MD_CTX_new... yes
checking for EVP_MD_CTX_free... yes
checking for RSA_get0_key... yes
checking /openwrt/staging_dir/target-x86_64_musl/usr/include/openssl/ecdsa.h usability... yes
checking /openwrt/staging_dir/target-x86_64_musl/usr/include/openssl/ecdsa.h presence... yes
checking for /openwrt/staging_dir/target-x86_64_musl/usr/include/openssl/ecdsa.h... yes
checking whether NID_X9_62_prime256v1 is declared... yes
checking whether NID_secp384r1 is declared... yes
checking whether NID_ED25519 is declared... yes
checking whether NID_ED448 is declared... yes
checking for ragel... no
checking for library containing clock_gettime... none required
checking for Boost headers version >= 1.42.0... yes
checking for Boost's header version... 1_76
checking for the toolset name used by Boost for ccache_cxx... configure: WARNING: could not figure out which toolset name to use for ccache_cxx

checking boost/program_options.hpp usability... yes
checking boost/program_options.hpp presence... yes
checking for boost/program_options.hpp... yes
checking for the Boost program_options library... yes
checking whether to enable unit test building... no
checking whether to enable backend unit test building... no
checking whether to enable reproducible builds.... yes
checking whether to enable fuzzing targets... no
checking whether user requires sqlite3... no
checking for a Python interpreter with version >= 3.6... python
checking for python... /openwrt/staging_dir/host/bin/python
checking for python version... 3.8
checking for python platform... linux
checking for python script directory... ${prefix}/lib/python3.8/site-packages
checking for python extension module directory... ${exec_prefix}/lib/python3.8/site-packages
checking python module: venv... yes
checking for strcasestr... yes
checking for localtime_r... yes
checking for gmtime_r... yes
checking for recvmmsg... (cached) yes
checking for sched_setscheduler... yes
checking for getrandom... yes
checking for arc4random... no
checking whether to enable verbose logging... no
checking whether to enable PKCS11 support... yes
checking for P11KIT1... yes
checking for p11_kit_module_for_name in -lp11-kit... yes
checking for GEOIP... no
checking for MMDB... no
checking maxminddb.h usability... yes
checking maxminddb.h presence... yes
checking for maxminddb.h... yes
checking for MMDB_open in -lmaxminddb... yes
checking for YAML... yes
checking for MySQL library directory... configure: error: Did not find the mysql library dir in '/openwrt/staging_dir/target-x86_64_musl/usr/lib/mysql /openwrt/staging_dir/target-x86_64_musl/usr/mysql /openwrt/staging_dir/target-x86_64_musl/usr'
make[3]: *** [Makefile:253: /openwrt/build_dir/target-x86_64_musl/pdns-4.4.1/.configured_d85856df219efb44d9ad3ffb3710fd17] Error 1
```
