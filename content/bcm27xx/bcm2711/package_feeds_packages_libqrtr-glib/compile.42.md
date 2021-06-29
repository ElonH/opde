---
title: "compile.42"
date: 2021-06-29 09:38:24.594740
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
make package/feeds/packages/libqrtr-glib/compile -j$(nproc) || make package/feeds/packages/libqrtr-glib/compile V=s
```

#### Compile.txt

``` bash
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/aarch64
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for aarch64-openwrt-linux-strip... aarch64-openwrt-linux-musl-strip
checking for a race-free mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether UID '1000' is supported by ustar format... yes
checking whether GID '1000' is supported by ustar format... yes
checking how to create a ustar tar archive... gnutar
checking whether to enable maintainer-specific portions of Makefiles... yes
checking whether make supports nested variables... (cached) yes
checking for aarch64-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether the compiler supports GNU C... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to enable C11 features... none needed
checking whether ccache_cc understands -c and -o together... yes
checking whether make supports the include directive... yes (GNU style)
checking dependency style of ccache_cc... gcc3
checking build system type... x86_64-pc-linux-gnu
checking host system type... aarch64-openwrt-linux-gnu
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
checking for a working dd... /usr/bin/dd
checking how to truncate binary pipes... /usr/bin/dd bs=4096 count=1
checking for aarch64-openwrt-linux-mt... no
checking for mt... no
checking if : is a manifest tool... no
checking for stdio.h... yes
checking for stdlib.h... yes
checking for string.h... yes
checking for inttypes.h... yes
checking for stdint.h... yes
checking for strings.h... yes
checking for sys/stat.h... yes
checking for sys/types.h... yes
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
checking whether to build static libraries... no
checking whether C compiler accepts -Werror=unknown-warning-option... no
checking whether C compiler accepts -Wno-suggest-attribute=format... yes
checking whether C compiler accepts -fno-strict-aliasing... yes
checking whether C compiler accepts -Wnested-externs... yes
checking whether C compiler accepts -Wmissing-prototypes... yes
checking whether C compiler accepts -Wstrict-prototypes... yes
checking whether C compiler accepts -Wdeclaration-after-statement... yes
checking whether C compiler accepts -Wimplicit-function-declaration... yes
checking whether C compiler accepts -Wold-style-definition... yes
checking whether C compiler accepts -Wjump-misses-init... yes
checking whether C compiler accepts -Wall... yes
checking whether C compiler accepts -Wextra... yes
checking whether C compiler accepts -Wundef... yes
checking whether C compiler accepts -Wwrite-strings... yes
checking whether C compiler accepts -Wpointer-arith... yes
checking whether C compiler accepts -Wmissing-declarations... yes
checking whether C compiler accepts -Wredundant-decls... yes
checking whether C compiler accepts -Wno-unused-parameter... yes
checking whether C compiler accepts -Wno-missing-field-initializers... yes
checking whether C compiler accepts -Wformat=2... yes
checking whether C compiler accepts -Wcast-align... yes
checking whether C compiler accepts -Wformat-nonliteral... yes
checking whether C compiler accepts -Wformat-security... yes
checking whether C compiler accepts -Wsign-compare... yes
checking whether C compiler accepts -Wstrict-aliasing... yes
checking whether C compiler accepts -Wshadow... yes
checking whether C compiler accepts -Winline... yes
checking whether C compiler accepts -Wpacked... yes
checking whether C compiler accepts -Wmissing-format-attribute... yes
checking whether C compiler accepts -Wmissing-noreturn... yes
checking whether C compiler accepts -Winit-self... yes
checking whether C compiler accepts -Wredundant-decls... (cached) yes
checking whether C compiler accepts -Wmissing-include-dirs... yes
checking whether C compiler accepts -Wunused-but-set-variable... yes
checking whether C compiler accepts -Warray-bounds... yes
checking whether C compiler accepts -Wreturn-type... yes
checking whether C compiler accepts -Wswitch-enum... yes
checking whether C compiler accepts -Wswitch-default... yes
checking whether C compiler accepts -Wduplicated-cond... yes
checking whether C compiler accepts -Wduplicated-branches... yes
checking whether C compiler accepts -Wlogical-op... yes
checking whether C compiler accepts -Wrestrict... yes
checking whether C compiler accepts -Wnull-dereference... yes
checking whether C compiler accepts -Wdouble-promotion... yes
checking whether C compiler accepts -Wno-error=unused-parameter... yes
checking whether C compiler accepts -Wno-error=missing-field-initializers... yes
checking whether C compiler accepts -Werror=unknown-warning-option... (cached) no
checking whether the linker accepts -Wl,--as-needed... yes
checking whether the linker accepts -Wl,--as-needed... yes
checking whether the linker accepts -Wl,-z,relro... yes
checking whether the linker accepts -Wl,-z,relro... yes
checking whether the linker accepts -Wl,-z,now... yes
checking whether the linker accepts -Wl,-z,now... yes
checking whether the linker accepts -Wl,-z,noexecstack... yes
checking whether the linker accepts -Wl,-z,noexecstack... yes
checking whether the linker accepts -Wl,--no-as-needed... yes
checking whether the linker accepts -Wl,--fatal-warnings... yes
checking whether the linker accepts -Wl,-fatal_warnings... no
checking whether the linker accepts -Wl,--no-as-needed... yes
checking whether C compiler accepts -Werror=unknown-warning-option... (cached) no
checking whether C compiler accepts -Wno-suggest-attribute=format... (cached) yes
checking whether C compiler accepts -fno-strict-aliasing... (cached) yes
checking whether C compiler accepts -Wnested-externs... (cached) yes
checking whether C compiler accepts -Wmissing-prototypes... (cached) yes
checking whether C compiler accepts -Wstrict-prototypes... (cached) yes
checking whether C compiler accepts -Wdeclaration-after-statement... (cached) yes
checking whether C compiler accepts -Wimplicit-function-declaration... (cached) yes
checking whether C compiler accepts -Wold-style-definition... (cached) yes
checking whether C compiler accepts -Wjump-misses-init... (cached) yes
checking whether C compiler accepts -Wall... (cached) yes
checking whether C compiler accepts -Wextra... (cached) yes
checking whether C compiler accepts -Wundef... (cached) yes
checking whether C compiler accepts -Wwrite-strings... (cached) yes
checking whether C compiler accepts -Wpointer-arith... (cached) yes
checking whether C compiler accepts -Wmissing-declarations... (cached) yes
checking whether C compiler accepts -Wredundant-decls... (cached) yes
checking whether C compiler accepts -Wno-unused-parameter... (cached) yes
checking whether C compiler accepts -Wno-missing-field-initializers... (cached) yes
checking whether C compiler accepts -Wformat=2... (cached) yes
checking whether C compiler accepts -Wcast-align... (cached) yes
checking whether C compiler accepts -Wformat-nonliteral... (cached) yes
checking whether C compiler accepts -Wformat-security... (cached) yes
checking whether C compiler accepts -Wsign-compare... (cached) yes
checking whether C compiler accepts -Wstrict-aliasing... (cached) yes
checking whether C compiler accepts -Wshadow... (cached) yes
checking whether C compiler accepts -Winline... (cached) yes
checking whether C compiler accepts -Wpacked... (cached) yes
checking whether C compiler accepts -Wmissing-format-attribute... (cached) yes
checking whether C compiler accepts -Wmissing-noreturn... (cached) yes
checking whether C compiler accepts -Winit-self... (cached) yes
checking whether C compiler accepts -Wredundant-decls... (cached) yes
checking whether C compiler accepts -Wmissing-include-dirs... (cached) yes
checking whether C compiler accepts -Wunused-but-set-variable... (cached) yes
checking whether C compiler accepts -Warray-bounds... (cached) yes
checking whether C compiler accepts -Wreturn-type... (cached) yes
checking whether C compiler accepts -Wswitch-enum... (cached) yes
checking whether C compiler accepts -Wswitch-default... (cached) yes
checking whether C compiler accepts -Wduplicated-cond... (cached) yes
checking whether C compiler accepts -Wduplicated-branches... (cached) yes
checking whether C compiler accepts -Wlogical-op... (cached) yes
checking whether C compiler accepts -Wrestrict... (cached) yes
checking whether C compiler accepts -Wnull-dereference... (cached) yes
checking whether C compiler accepts -Wdouble-promotion... (cached) yes
checking whether C compiler accepts -Wno-cast-function-type... yes
checking whether C compiler accepts -Wno-packed... yes
checking whether C compiler accepts -Wno-error=unused-parameter... (cached) yes
checking whether C compiler accepts -Wno-error=missing-field-initializers... (cached) yes
checking whether C compiler accepts -Wno-error=cast-function-type... yes
checking whether C compiler accepts -Wno-error=packed... yes
checking pkg-config is at least version 0.9.0... yes
checking for GLIB... no
configure: error: Package requirements (glib-2.0 >= 2.48
                  gobject-2.0
                  gio-2.0
                  gio-unix-2.0) were not met:

Package 'glib-2.0', required by 'virtual:world', not found
Package 'gobject-2.0', required by 'virtual:world', not found
Package 'gio-2.0', required by 'virtual:world', not found
Package 'gio-unix-2.0', required by 'virtual:world', not found

Consider adjusting the PKG_CONFIG_PATH environment variable if you
installed software in a non-standard prefix.

Alternatively, you may set the environment variables GLIB_CFLAGS
and GLIB_LIBS to avoid the need to call pkg-config.
See the pkg-config man page for more details.
make[3]: *** [Makefile:75: /openwrt/build_dir/target-aarch64_cortex-a72_musl/libqrtr-glib-1.0.0/.configured_a17fb5ef857664f03cd0ce37cc5ea591] Error 1
```
