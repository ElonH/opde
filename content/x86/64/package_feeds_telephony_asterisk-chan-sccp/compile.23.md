---
title: "compile.23"
date: 2021-05-26 23:57:41.748508
hidden: false
draft: false
weight: -23
---

build number: `23`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/telephony/asterisk-chan-sccp/compile -j$(nproc) || make package/feeds/telephony/asterisk-chan-sccp/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/01-prevent-extra-optimization.patch using plaintext: 
patching file autoconf/extra.m4
Hunk #1 succeeded at 516 with fuzz 2 (offset 25 lines).

Applying ./patches/100-reproducible-builds.patch using plaintext: 
patching file src/chan_sccp.c
Hunk #1 succeeded at 198 (offset 12 lines).
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-x86_64_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal -I m4 -I . --force -I autoconf
autoreconf: configure.ac: tracing
autoreconf: configure.ac: subdirectory libltdl not present
autoreconf: running: /openwrt/staging_dir/host/bin/libtoolize --install --force
OpenWrt-libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, `autoconf'.
OpenWrt-libtoolize: linking file `autoconf/config.guess'
OpenWrt-libtoolize: linking file `autoconf/config.sub'
OpenWrt-libtoolize: linking file `autoconf/install-sh'
OpenWrt-libtoolize: linking file `autoconf/ltmain.sh'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `autoconf'.
OpenWrt-libtoolize: linking file `autoconf/libtool.m4'
OpenWrt-libtoolize: linking file `autoconf/ltoptions.m4'
OpenWrt-libtoolize: linking file `autoconf/ltsugar.m4'
OpenWrt-libtoolize: linking file `autoconf/ltversion.m4'
OpenWrt-libtoolize: linking file `autoconf/lt~obsolete.m4'
OpenWrt-libtoolize: Remember to add `LT_INIT' to configure.ac.
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-x86_64_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-x86_64_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
autoreconf: Leaving directory `.'
configure: loading site script /openwrt/include/site/x86_64
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
checking host system type... x86_64-openwrt-linux-gnu
checking target system type... x86_64-openwrt-linux-gnu

Checking AutoMake:
checking whether to enable maintainer-specific portions of Makefiles... no
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for x86_64-openwrt-linux-strip... x86_64-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking for style of include used by make... GNU
checking whether make supports nested variables... yes
checking dependency style of ccache_cc... gcc3
checking whether make supports nested variables... (cached) yes

Checking build environment:
checking for x86_64-openwrt-linux-uname... no
checking for uname... /usr/bin/uname
configure: WARNING: using cross tools not prefixed with host triplet
checking for date... /usr/bin/date
checking for uname... /usr/bin/uname
checking for gsed... no
checking for sed... /openwrt/staging_dir/host/bin/sed
checking for id... /usr/bin/id
checking for RAII support... checking gcc version > 4.3... yes
checking for gcc -fnested-functions... no
checking whether C compiler accepts -fstack-protector... yes
checking whether C compiler accepts -Wno-long-long... yes
checking whether C compiler accepts -Wno-ignored-qualifiers... yes
checking whether C compiler accepts -Wno-missing-field-initializers... yes
checking if pointers to integers require aligned access... no
checking whether uint64_t misalignment causes a buserror on this system... no
checking whether we are using the GNU C++ compiler... yes
checking whether ccache_cxx accepts -g... yes
checking dependency style of ccache_cxx... gcc3

Checking host platform:
Running on: x86_64-openwrt-linux-gnu
checking for x86_64-openwrt-linux-gcc... (cached) ccache_cc
checking for x86_64-openwrt-linux-ld... x86_64-openwrt-linux-musl-ld
checking for x86_64-openwrt-linux-ranlib... x86_64-openwrt-linux-musl-gcc-ranlib

Checking Atomic Functions:
checking ia64intrin.h usability... no
checking ia64intrin.h presence... no
checking for ia64intrin.h... no
checking ia32intrin.h usability... no
checking ia32intrin.h presence... no
checking for ia32intrin.h... no
checking whether compiler supports builtin atomic CAS-32... yes
checking whether compiler supports builtin atomic CAS-64... yes
checking whether compiler supports builtin atomic CAS-ptr... yes
checking whether compiler supports builtin atomic incr... yes
checking whether ia64intrin.h is required... no
checking whether the compiler supports CMPXCHG16B... yes
checking whether the CPU supports CMPXCHG16B... assuming no

Checking for standard programs:
checking how to print strings... printf
checking for a sed that does not truncate output... (cached) /openwrt/staging_dir/host/bin/sed
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache_cc... x86_64-openwrt-linux-musl-ld
checking if the linker (x86_64-openwrt-linux-musl-ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... x86_64-openwrt-linux-musl-gcc-nm
checking the name lister (x86_64-openwrt-linux-musl-gcc-nm) interface... BSD nm
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
checking for x86_64-openwrt-linux-ranlib... (cached) x86_64-openwrt-linux-musl-gcc-ranlib
checking command to parse x86_64-openwrt-linux-musl-gcc-nm output from ccache_cc object... ok
checking for sysroot... no
checking for x86_64-openwrt-linux-mt... no
checking for mt... no
checking if : is a manifest tool... no
checking for dlfcn.h... yes
checking for git... /openwrt/staging_dir/host/bin/git
checking for bash... /bin/bash
checking for bash... /openwrt/staging_dir/host/bin/bash
checking for gm4... /openwrt/staging_dir/host/bin/m4
checking for ggrep... (cached) /openwrt/staging_dir/host/bin/grep
checking for cat... /usr/bin/cat
checking for uname... (cached) /usr/bin/uname
checking for rpmbuild... no
checking for objcopy... /usr/bin/objcopy
checking for gdb... no
checking for head... /usr/bin/head
checking for cut... /usr/bin/cut
checking for tr... /usr/bin/tr
checking for gawk... /usr/bin/gawk
checking for pkg-config... /openwrt/staging_dir/host/bin/pkg-config
checking for openssl... /openwrt/staging_dir/host/bin/openssl
checking for x86_64-openwrt-linux-clang... (cached) ccache_cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether ccache_cc accepts -g... (cached) yes
checking for ccache_cc option to accept ISO C89... (cached) none needed
checking whether ccache_cc understands -c and -o together... (cached) yes
checking whether ccache_cc and cc understand -c and -o together... yes
checking whether ccache_cc needs -traditional... no
checking how to run the C preprocessor... ccache_cc -E
checking for gawk... (cached) gawk
checking whether ln -s works... yes
checking whether make sets $(MAKE)... (cached) yes
checking for an ANSI C-conforming const... yes
checking for inline... inline
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
checking for the pthreads library -lpthreads... no
checking whether pthreads work without any flags... yes
checking for joinable pthread attribute... PTHREAD_CREATE_JOINABLE
checking if more special flags are required for pthreads... no
checking for ccache... /openwrt/staging_dir/host/bin/ccache
checking which extension is used for runtime loadable modules... .so
checking which variable specifies run-time module search path... LD_LIBRARY_PATH
checking for the default library search path... /lib /usr/lib /usr/local/lib /usr/local/lib/x86_64-linux-gnu /lib/x86_64-linux-gnu /usr/lib/x86_64-linux-gnu /lib32 /usr/lib32 /libx32 /usr/libx32 
checking for library containing dlopen... none required
checking for dlerror... yes
checking for shl_load... no
checking for shl_load in -ldld... no
checking for dld_link in -ldld... no
checking for _ prefix in compiled symbols... no
checking whether deplibs are loaded by dlopen... yes
checking for argz.h... no
checking for error_t... no
checking for argz_add... no
checking for argz_append... no
checking for argz_count... no
checking for argz_create_sep... no
checking for argz_insert... no
checking for argz_next... no
checking for argz_stringify... no
checking whether libtool supports -dlopen/-dlpreopen... yes

Checking Libtool:
checking for ltdl.h... yes
checking whether lt_dlinterface_register is declared... yes
checking for lt_dladvise_preload in -lltdl... yes
checking where to find libltdl headers... 
checking where to find libltdl library... -lltdl
checking for unistd.h... (cached) yes
checking for dl.h... no
checking for sys/dl.h... no
checking for dld.h... no
checking for mach-o/dyld.h... no
checking for dirent.h... yes
checking for closedir... yes
checking for opendir... yes
checking for readdir... yes
checking for strlcat... yes
checking for strlcpy... yes
checking for lt_dladvise_init in -lltdl... yes
libtool: setup done

Checking for Required Libraries:
checking for ld... x86_64-openwrt-linux-musl-ld -m elf_x86_64
checking if the linker (x86_64-openwrt-linux-musl-ld -m elf_x86_64) is GNU ld... yes
checking for shared library run path origin... done
checking 32-bit host C ABI... no
checking for ELF binary format... yes
checking for the common suffixes of directories in the library search path... lib,lib,lib64
checking for iconv... yes
checking for working iconv... guessing yes
checking how to link with libiconv... -liconv
checking for iconv declaration... 
         extern size_t iconv (iconv_t cd, char * *inbuf, size_t *inbytesleft, char * *outbuf, size_t *outbytesleft);
checking for main in -lc... yes
checking for main in -lpthread... yes
checking for main in -lsocket... no
checking sys/ioctl.h usability... yes
checking sys/ioctl.h presence... yes
checking for sys/ioctl.h... yes
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking netinet/in.h usability... yes
checking netinet/in.h presence... yes
checking for netinet/in.h... yes
checking pthread.h usability... yes
checking pthread.h presence... yes
checking for pthread.h... yes
checking xlocale.h usability... no
checking xlocale.h presence... no
checking for xlocale.h... no
checking for main in -liconv... yes
checking for gethostbyname... yes
checking for inet_ntoa... yes
checking for mkdir... yes
checking for ANSI C header files... (cached) yes
checking for stdbool.h that conforms to C99... yes
checking for _Bool... yes
checking for netinet/in.h... (cached) yes
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking signal.h usability... yes
checking signal.h presence... yes
checking for signal.h... yes
checking sys/signal.h usability... yes
checking sys/signal.h presence... yes
checking for sys/signal.h... yes
checking stdio.h usability... yes
checking stdio.h presence... yes
checking for stdio.h... yes
checking errno.h usability... yes
checking errno.h presence... yes
checking for errno.h... yes
checking ctype.h usability... yes
checking ctype.h presence... yes
checking for ctype.h... yes
checking assert.h usability... yes
checking assert.h presence... yes
checking for assert.h... yes
checking sys/sysinfo.h usability... yes
checking sys/sysinfo.h presence... yes
checking for sys/sysinfo.h... yes
checking whether struct tm is in sys/time.h or time.h... time.h
checking for struct tm.tm_zone... yes
checking for EVP_EncryptInit in -lcrypto... yes
checking for SSL_CTX_new in -lssl... yes
checking sizeof(long long) == sizeof(long)... no
checking endian.h usability... yes
checking endian.h presence... yes
checking for endian.h... yes
checking whether byte ordering is bigendian... (cached) no

Checking Configure Options:
checking Search Path: /openwrt/staging_dir/target-x86_64_musl/usr... not-found
configure: Either install asterisk and asterisk-devel packages using your package manager.
configure: If you compiled asterisk manually, make sure you also run `make install-headers` so chan-sccp can find them.
configure: Or run ./configure --with-asterisk=PATH with PATH pointing to the directory where you installed asterisk
configure: error: Could not find pbx headers or libraries - these are required.
make[3]: *** [Makefile:76: /openwrt/build_dir/target-x86_64_musl/asterisk-chan-sccp-2020-12-19-968caa45/.configured_a17fb5ef857664f03cd0ce37cc5ea591] Error 1
```
