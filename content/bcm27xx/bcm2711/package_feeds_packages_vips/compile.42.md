---
title: "compile.42"
date: 2021-06-29 09:23:42.966526
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
make package/feeds/packages/vips/compile -j$(nproc) || make package/feeds/packages/vips/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-no_introspection.patch using plaintext: 
patching file configure.ac
patching file libvips/Makefile.am

Applying ./patches/010-reproducible-build.patch using plaintext: 
patching file configure.ac
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-aarch64_cortex-a72_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/aclocal -I m4 -I . --force -I m4
autoreconf: configure.ac: tracing
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
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
autoreconf: Leaving directory `.'
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/aarch64
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for aarch64-openwrt-linux-strip... aarch64-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking build system type... x86_64-pc-linux-gnu
checking host system type... aarch64-openwrt-linux-gnu
checking for native Win32... no
checking for binary open needed... no
checking for Mac OS X... no
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
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
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
checking whether the ccache_cc linker (aarch64-openwrt-linux-musl-ld) supports shared libraries... yes
checking whether -lc should be explicitly linked in... no
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... yes
checking for gawk... (cached) gawk
checking for aarch64-openwrt-linux-gcc... (cached) ccache_cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether ccache_cc accepts -g... (cached) yes
checking for ccache_cc option to accept ISO C89... (cached) none needed
checking whether ccache_cc understands -c and -o together... (cached) yes
checking dependency style of ccache_cc... (cached) gcc3
checking for ccache_cc option to accept ISO C99... none needed
checking for ccache_cc option to accept ISO Standard C... (cached) none needed
checking whether we are using the GNU C++ compiler... yes
checking whether ccache_cxx accepts -g... yes
checking dependency style of ccache_cxx... gcc3
checking how to run the C++ preprocessor... ccache_cxx -E
checking for ld used by ccache_cxx... aarch64-openwrt-linux-musl-ld
checking if the linker (aarch64-openwrt-linux-musl-ld) is GNU ld... yes
checking whether the ccache_cxx linker (aarch64-openwrt-linux-musl-ld) supports shared libraries... yes
checking for ccache_cxx option to produce PIC... -fPIC -DPIC
checking if ccache_cxx PIC flag -fPIC -DPIC works... yes
checking if ccache_cxx static flag -static works... yes
checking if ccache_cxx supports -c -o file.o... yes
checking if ccache_cxx supports -c -o file.o... (cached) yes
checking whether the ccache_cxx linker (aarch64-openwrt-linux-musl-ld) supports shared libraries... yes
checking dynamic linker characteristics... (cached) GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether ln -s works... yes
checking if malloc debugging is wanted... no
checking locale.h usability... yes
checking locale.h presence... yes
checking for locale.h... yes
checking for LC_MESSAGES... yes
checking for CFPreferencesCopyAppValue... no
checking for CFLocaleCopyCurrent... no
checking libintl.h usability... yes
checking libintl.h presence... yes
checking for libintl.h... yes
checking for ngettext in libc... yes
checking for dgettext in libc... yes
checking for bind_textdomain_codeset... yes
checking for msgfmt... /openwrt/staging_dir/hostpkg/bin/msgfmt
checking for dcgettext... yes
checking if msgfmt accepts -c... yes
checking for gmsgfmt... /openwrt/staging_dir/hostpkg/bin/msgfmt
checking for xgettext... /openwrt/staging_dir/hostpkg/bin/xgettext
checking for catalogs to be installed...  en_GB de
checking for ccache_cc version... 8.4.0
checking for dirent.h that defines DIR... yes
checking for library containing opendir... none required
checking for ANSI C header files... (cached) yes
checking errno.h usability... yes
checking errno.h presence... yes
checking for errno.h... yes
checking math.h usability... yes
checking math.h presence... yes
checking for math.h... yes
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking limits.h usability... yes
checking limits.h presence... yes
checking for limits.h... yes
checking for stdlib.h... (cached) yes
checking for string.h... (cached) yes
checking sys/file.h usability... yes
checking sys/file.h presence... yes
checking for sys/file.h... yes
checking sys/ioctl.h usability... yes
checking sys/ioctl.h presence... yes
checking for sys/ioctl.h... yes
checking sys/param.h usability... yes
checking sys/param.h presence... yes
checking for sys/param.h... yes
checking sys/time.h usability... yes
checking sys/time.h presence... yes
checking for sys/time.h... yes
checking sys/mman.h usability... yes
checking sys/mman.h presence... yes
checking for sys/mman.h... yes
checking for sys/types.h... (cached) yes
checking for sys/stat.h... (cached) yes
checking for unistd.h... (cached) yes
checking io.h usability... no
checking io.h presence... no
checking for io.h... no
checking direct.h usability... no
checking direct.h presence... no
checking for direct.h... no
checking windows.h usability... no
checking windows.h presence... no
checking for windows.h... no
checking for aarch64-openwrt-linux-dllwrap... no
checking for dllwrap... no
checking for aarch64-openwrt-linux-dlltool... false
checking for aarch64-openwrt-linux-objdump... (cached) aarch64-openwrt-linux-musl-objdump
checking for aarch64-openwrt-linux-ranlib... (cached) aarch64-openwrt-linux-musl-gcc-ranlib
checking for aarch64-openwrt-linux-strip... (cached) aarch64-openwrt-linux-musl-strip
checking for aarch64-openwrt-linux-ar... (cached) aarch64-openwrt-linux-musl-gcc-ar
checking for aarch64-openwrt-linux-as... ccache_cc -c -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/vips-8.10.6=vips-8.10.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include
checking for aarch64-openwrt-linux-ld... aarch64-openwrt-linux-musl-ld
checking for C/C++ restrict keyword... __restrict
checking for __attribute__((vector_size))... yes
checking for an ANSI C-conforming const... yes
checking for mode_t... yes
checking for off_t... yes
checking for size_t... yes
checking for ccache_cc with working vector support... yes
checking for C++ vector shuffle... yes
checking for C++ vector arithmetic... yes
checking for C++ signed constants in vector templates... yes
checking for working memcmp... (cached) yes
checking for stdlib.h... (cached) yes
checking for unistd.h... (cached) yes
checking for sys/param.h... (cached) yes
checking for getpagesize... yes
checking for working mmap... no
checking for vprintf... yes
checking for _doprnt... no
checking for getcwd... (cached) yes
checking for gettimeofday... (cached) yes
checking for getwd... no
checking for memset... yes
checking for munmap... yes
checking for putenv... yes
checking for realpath... yes
checking for strcasecmp... yes
checking for strchr... yes
checking for strcspn... yes
checking for strdup... yes
checking for strerror... (cached) yes
checking for strrchr... yes
checking for strspn... yes
checking for vsnprintf... (cached) yes
checking for realpath... (cached) yes
checking for mkstemp... yes
checking for mktemp... yes
checking for random... yes
checking for rand... yes
checking for sysconf... yes
checking for atexit... yes
checking for _aligned_malloc... no
checking for posix_memalign... yes
checking for memalign... yes
checking for cbrt in -lm... yes
checking for hypot in -lm... yes
checking for atan2 in -lm... yes
checking pkg-config is at least version 0.9.0... yes
checking for glib-2.0 >= 2.15 gmodule-2.0 gobject-2.0 gio-2.0... no
configure: error: Package requirements (glib-2.0 >= 2.15 gmodule-2.0 gobject-2.0 gio-2.0) were not met:

Package 'glib-2.0', required by 'virtual:world', not found
Package 'gmodule-2.0', required by 'virtual:world', not found
Package 'gobject-2.0', required by 'virtual:world', not found
Package 'gio-2.0', required by 'virtual:world', not found

Consider adjusting the PKG_CONFIG_PATH environment variable if you
installed software in a non-standard prefix.

Alternatively, you may set the environment variables REQUIRED_CFLAGS
and REQUIRED_LIBS to avoid the need to call pkg-config.
See the pkg-config man page for more details.
make[3]: *** [Makefile:92: /openwrt/build_dir/target-aarch64_cortex-a72_musl/vips-8.10.6/.configured_a17fb5ef857664f03cd0ce37cc5ea591] Error 1
```
