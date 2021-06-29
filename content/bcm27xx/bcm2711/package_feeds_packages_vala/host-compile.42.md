---
title: "host-compile.42"
date: 2021-06-29 09:31:48.754572
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
make package/feeds/packages/vala/host-compile -j$(nproc) || make package/feeds/packages/vala/host-compile V=s
```

#### Compile.txt

``` bash
+ curl -f --connect-timeout 20 --retry 5 --location --insecure https://download.gnome.org/sources/vala/0.52/vala-0.52.3.tar.xz
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0

100 3492k  100 3492k    0     0  8476k      0 --:--:-- --:--:-- --:--:-- 8476k
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether to enable maintainer-specific portions of Makefiles... yes
checking for x86_64-pc-linux-gnu-gcc... ccache gcc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... no
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache gcc accepts -g... yes
checking for ccache gcc option to accept ISO C89... none needed
checking whether ccache gcc understands -c and -o together... yes
checking whether make supports the include directive... yes (GNU style)
checking dependency style of ccache gcc... gcc3
checking whether ln -s works... yes
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-pc-linux-gnu
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache gcc... /usr/bin/ld
checking if the linker (/usr/bin/ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... /usr/bin/nm -B
checking the name lister (/usr/bin/nm -B) interface... BSD nm
checking the maximum length of command line arguments... 3145728
checking how to convert x86_64-pc-linux-gnu file names to x86_64-pc-linux-gnu format... func_convert_file_noop
checking how to convert x86_64-pc-linux-gnu file names to toolchain format... func_convert_file_noop
checking for /usr/bin/ld option to reload object files... -r
checking for x86_64-pc-linux-gnu-objdump... no
checking for objdump... objdump
checking how to recognize dependent libraries... pass_all
checking for x86_64-pc-linux-gnu-dlltool... no
checking for dlltool... no
checking how to associate runtime and link libraries... printf %s\n
checking for x86_64-pc-linux-gnu-ar... no
checking for ar... ar
checking for archiver @FILE support... @
checking for x86_64-pc-linux-gnu-strip... no
checking for strip... strip
checking for x86_64-pc-linux-gnu-ranlib... no
checking for ranlib... ranlib
checking command to parse /usr/bin/nm -B output from ccache gcc object... ok
checking for sysroot... no
checking for a working dd... /usr/bin/dd
checking how to truncate binary pipes... /usr/bin/dd bs=4096 count=1
checking for x86_64-pc-linux-gnu-mt... no
checking for mt... no
checking if : is a manifest tool... no
checking how to run the C preprocessor... ccache gcc -E
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
checking if ccache gcc supports -fno-rtti -fno-exceptions... no
checking for ccache gcc option to produce PIC... -fPIC -DPIC
checking if ccache gcc PIC flag -fPIC -DPIC works... yes
checking if ccache gcc static flag -static works... yes
checking if ccache gcc supports -c -o file.o... yes
checking if ccache gcc supports -c -o file.o... (cached) yes
checking whether the ccache gcc linker (/usr/bin/ld -m elf_x86_64) supports shared libraries... yes
checking whether -lc should be explicitly linked in... no
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... no
checking pkg-config is at least version 0.21... yes
checking for flex... flex
checking lex output file root... lex.yy
checking lex library... -lfl
checking whether yytext is a pointer... yes
checking for bison... bison -y
checking for valac... valac
checking whether C compiler accepts -Werror=init-self... yes
checking whether C compiler accepts -Werror=implicit... yes
checking whether C compiler accepts -Werror=implicit-fallthrough... yes
checking whether C compiler accepts -Werror=pointer-arith... yes
checking whether C compiler accepts -Werror=redundant-decls... yes
checking whether C compiler accepts -Werror=return-local-addr... yes
checking whether C compiler accepts -Werror=return-stack-address... no
checking whether C compiler accepts -Werror=return-type... yes
checking whether C compiler accepts -Werror=sequence-point... yes
checking whether C compiler accepts -Werror=uninitialized... yes
checking whether C compiler accepts -Werror=int-to-pointer-cast... yes
checking whether C compiler accepts -Werror=pointer-to-int-cast... yes
checking whether C compiler accepts -Werror=compare-distinct-pointer-types... no
checking whether C compiler accepts -Werror=empty-body... yes
checking whether C compiler accepts -Wformat=2... yes
checking whether C compiler accepts -Werror=format-security... yes
checking whether C compiler accepts -Werror=format-nonliteral... yes
checking whether C compiler accepts -Werror=int-conversion... yes
checking whether C compiler accepts -Werror=duplicated-branches... yes
checking whether C compiler accepts -Werror=duplicated-cond... yes
checking whether C compiler accepts -Werror=declaration-after-statement... yes
checking whether C compiler accepts -Werror=maybe-uninitialized... yes
checking whether C compiler accepts -Werror=missing-braces... yes
checking whether C compiler accepts -Werror=missing-declarations... yes
checking whether C compiler accepts -Werror=missing-prototypes... yes
checking whether C compiler accepts -Werror=strict-prototypes... no
checking whether C compiler accepts -Werror=tautological-pointer-compare... no
checking whether C compiler accepts -Werror=address... yes
checking whether C compiler accepts -Werror=array-bounds... yes
checking whether C compiler accepts -Werror=enum-conversion... no
checking for glib-2.0 >= 2.48.0 gobject-2.0 >= 2.48.0... no
configure: error: Package requirements (glib-2.0 >= 2.48.0 gobject-2.0 >= 2.48.0) were not met:

Package 'glib-2.0', required by 'virtual:world', not found
Package 'gobject-2.0', required by 'virtual:world', not found

Consider adjusting the PKG_CONFIG_PATH environment variable if you
installed software in a non-standard prefix.

Alternatively, you may set the environment variables GLIB_CFLAGS
and GLIB_LIBS to avoid the need to call pkg-config.
See the pkg-config man page for more details.
make[3]: *** [Makefile:52: /openwrt/build_dir/hostpkg/vala-0.52.3/.configured] Error 1
```
