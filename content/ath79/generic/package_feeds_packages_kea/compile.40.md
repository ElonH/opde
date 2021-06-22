---
title: "compile.40"
date: 2021-06-22 10:38:26.222614
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
make package/feeds/packages/kea/compile -j$(nproc) || make package/feeds/packages/kea/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-fix-cross-compile.patch using plaintext: 
patching file configure.ac

Applying ./patches/002-fix-host-compile.patch using plaintext: 
patching file m4macros/ax_crypto.m4

Applying ./patches/003-no-test-compile.patch using plaintext: 
patching file src/bin/admin/Makefile.am
patching file src/bin/agent/Makefile.am
patching file src/bin/d2/Makefile.am
patching file src/bin/dhcp4/Makefile.am
patching file src/bin/dhcp6/Makefile.am
patching file src/bin/keactrl/Makefile.am
patching file src/bin/lfc/Makefile.am
patching file src/bin/netconf/Makefile.am
patching file src/bin/perfdhcp/Makefile.am
patching file src/bin/shell/Makefile.am
patching file src/hooks/dhcp/high_availability/Makefile.am
patching file src/hooks/dhcp/lease_cmds/Makefile.am
patching file src/hooks/dhcp/stat_cmds/Makefile.am
patching file src/hooks/dhcp/user_chk/Makefile.am
patching file src/lib/asiodns/Makefile.am
patching file src/lib/asiolink/Makefile.am
patching file src/lib/cc/Makefile.am
patching file src/lib/cfgrpt/Makefile.am
patching file src/lib/config/Makefile.am
patching file src/lib/config_backend/Makefile.am
patching file src/lib/cql/Makefile.am
patching file src/lib/cryptolink/Makefile.am
patching file src/lib/database/Makefile.am
patching file src/lib/dhcp/Makefile.am
patching file src/lib/dhcp_ddns/Makefile.am
patching file src/lib/dhcpsrv/Makefile.am
patching file src/lib/dns/Makefile.am
patching file src/lib/eval/Makefile.am
patching file src/lib/exceptions/Makefile.am
patching file src/lib/hooks/Makefile.am
patching file src/lib/http/Makefile.am
patching file src/lib/log/Makefile.am
patching file src/lib/log/interprocess/Makefile.am
patching file src/lib/mysql/Makefile.am
patching file src/lib/pgsql/Makefile.am
patching file src/lib/process/Makefile.am
patching file src/lib/stats/Makefile.am
patching file src/lib/util/Makefile.am
patching file src/lib/yang/Makefile.am

Applying ./patches/004-replace-rev-with-awk.patch using plaintext: 
patching file src/bin/keactrl/keactrl.in

Applying ./patches/010-openssl-deprecated.patch using plaintext: 
patching file src/lib/cryptolink/openssl_link.cc

Applying ./patches/020-shared_ptr.patch using plaintext: 
patching file m4macros/ax_cpp11.m4
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force -I m4macros ${ACLOCAL_FLAGS}
autoreconf: configure.ac: tracing
autoreconf: running: /openwrt/staging_dir/host/bin/libtoolize --install --force
OpenWrt-libtoolize: putting auxiliary files in `.'.
OpenWrt-libtoolize: linking file `./config.guess'
OpenWrt-libtoolize: linking file `./config.sub'
OpenWrt-libtoolize: linking file `./install-sh'
OpenWrt-libtoolize: linking file `./ltmain.sh'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `m4macros'.
OpenWrt-libtoolize: linking file `m4macros/libtool.m4'
OpenWrt-libtoolize: linking file `m4macros/ltoptions.m4'
OpenWrt-libtoolize: linking file `m4macros/ltsugar.m4'
OpenWrt-libtoolize: linking file `m4macros/ltversion.m4'
OpenWrt-libtoolize: linking file `m4macros/lt~obsolete.m4'
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
checking whether the C++ compiler works... yes
checking for C++ compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C++ compiler... yes
checking whether ccache_cxx accepts -g... yes
checking for style of include used by make... GNU
checking dependency style of ccache_cxx... gcc3
checking whether this is a tarball or git source... "tarball"
checking whether this is a development or stable version... 0
checking for pkg-config... /openwrt/staging_dir/host/bin/pkg-config
checking how to print strings... printf
checking for mips-openwrt-linux-gcc... ccache_cc
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
checking whether ccache_cc understands -c and -o together... yes
checking dependency style of ccache_cc... gcc3
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
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
checking whether __SUNPRO_CC is declared... no
checking whether __clang__ is declared... no
checking std::unique_ptr support... yes
checking cbegin/cend support... yes
checking final method support... yes
checking override method support... yes
checking aggregate initialization support... yes
checking variadic template support... yes
checking static_assert support... yes
checking template alias... yes
checking constexpr support... yes
checking enum class support... yes
checking range-for support... yes
checking lambda support... yes
checking thread support... yes
checking mutex support... yes
checking condition variable support... yes
checking atomic support... yes
checking chrono support... yes
checking for std::is_base_of... yes
checking for different std::chrono::duration types... no
checking C++ version... 201703
checking whether -Wl,-R flag is available in linker... yes
configure: WARNING: "Detected musl libc: musl dlclose() is a noop"
checking whether ccache_cxx supports -Wno-missing-field-initializers... yes
checking for library containing inet_pton... none required
checking for library containing recvfrom... none required
checking for library containing nanosleep... none required
checking for library containing dlsym... none required
checking for stdbool.h that conforms to C99... no
checking for _Bool... no
checking for size_t... yes
checking for ssize_t... yes
checking OS type... Linux
checking for sa_len in struct sockaddr... no
checking for usuable C++11 regex... no
checking for OpenSSL library... configure: error: OpenSSL not found at /openwrt/staging_dir/target-mips_24kc_musl/usr
make[3]: *** [Makefile:266: /openwrt/build_dir/target-mips_24kc_musl/kea-1.8.2/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
