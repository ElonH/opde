---
title: "compile.40"
date: 2021-06-22 10:50:06.158401
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
make package/feeds/packages/libgpiod/compile -j$(nproc) || make package/feeds/packages/libgpiod/compile V=s
```

#### Compile.txt

``` bash
bash: /openwrt/staging_dir/target-mips_24kc_musl/host/bin/python3.9-config: No such file or directory
bash: /openwrt/staging_dir/target-mips_24kc_musl/host/bin/python3.9-config: No such file or directory
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
checking whether make supports the include directive... yes (GNU style)
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
checking for mips-openwrt-linux-ar... mips-openwrt-linux-musl-gcc-ar
checking the archiver (mips-openwrt-linux-musl-gcc-ar) interface... ar
checking for mips-openwrt-linux-gcc... (cached) ccache_cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether ccache_cc accepts -g... (cached) yes
checking for ccache_cc option to accept ISO C89... (cached) none needed
checking whether ccache_cc understands -c and -o together... (cached) yes
checking dependency style of ccache_cc... (cached) gcc3
checking whether we are using the GNU C++ compiler... yes
checking whether ccache_cxx accepts -g... yes
checking dependency style of ccache_cxx... gcc3
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking how to print strings... printf
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
checking for a working dd... /usr/bin/dd
checking how to truncate binary pipes... /usr/bin/dd bs=4096 count=1
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
checking for ANSI C header files... (cached) yes
checking for stdlib.h... (cached) yes
checking for GNU libc compatible malloc... (cached) yes
checking for ioctl... yes
checking for asprintf... yes
checking for scandir... yes
checking for alphasort... yes
checking for ppoll... yes
checking getopt.h usability... yes
checking getopt.h presence... yes
checking for getopt.h... yes
checking dirent.h usability... yes
checking dirent.h presence... yes
checking for dirent.h... yes
checking sys/poll.h usability... yes
checking sys/poll.h presence... yes
checking for sys/poll.h... yes
checking sys/sysmacros.h usability... yes
checking sys/sysmacros.h presence... yes
checking for sys/sysmacros.h... yes
checking linux/gpio.h usability... yes
checking linux/gpio.h presence... yes
checking for linux/gpio.h... yes
checking for basename... yes
checking for daemon... yes
checking for signalfd... yes
checking for setlinebuf... yes
checking sys/signalfd.h usability... yes
checking sys/signalfd.h presence... yes
checking for sys/signalfd.h... yes
checking whether /openwrt/staging_dir/hostpkg/bin/python3.9 version is >= 3.0... yes
checking for /openwrt/staging_dir/hostpkg/bin/python3.9 version... 3.9
checking for /openwrt/staging_dir/hostpkg/bin/python3.9 platform... linux
checking for /openwrt/staging_dir/hostpkg/bin/python3.9 script directory... ${prefix}/lib/python3.9/site-packages
checking for /openwrt/staging_dir/hostpkg/bin/python3.9 extension module directory... ${exec_prefix}/lib/python3.9/site-packages
checking for doxygen... false
configure: doxygen not found - documentation cannot be generated
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating libgpiod.pc
config.status: creating Makefile
config.status: creating include/Makefile
config.status: creating lib/Makefile
config.status: creating tools/Makefile
config.status: creating tests/Makefile
config.status: creating tests/mockup/Makefile
config.status: creating bindings/cxx/libgpiodcxx.pc
config.status: creating bindings/Makefile
config.status: creating bindings/cxx/Makefile
config.status: creating bindings/cxx/examples/Makefile
config.status: creating bindings/python/Makefile
config.status: creating bindings/python/examples/Makefile
config.status: creating man/Makefile
config.status: creating config.h
config.status: executing depfiles commands
config.status: executing libtool commands
configure: WARNING: unrecognized options: --disable-nls
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/libgpiod-1.4.4'
make  all-recursive
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/libgpiod-1.4.4'
Making all in include
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/libgpiod-1.4.4/include'
make[6]: Nothing to be done for 'all'.
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/libgpiod-1.4.4/include'
Making all in lib
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/libgpiod-1.4.4/lib'
  CC       libgpiod_la-core.lo
  CC       libgpiod_la-ctxless.lo
  CC       libgpiod_la-helpers.lo
  CC       libgpiod_la-iter.lo
  CC       libgpiod_la-misc.lo
  CCLD     libgpiod.la
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/libgpiod-1.4.4/lib'
Making all in bindings
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/libgpiod-1.4.4/bindings'
Making all in .
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/libgpiod-1.4.4/bindings'
make[7]: Nothing to be done for 'all-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/libgpiod-1.4.4/bindings'
Making all in python
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/libgpiod-1.4.4/bindings/python'
Making all in .
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/libgpiod-1.4.4/bindings/python'
  CC       gpiod_la-gpiodmodule.lo
In file included from /openwrt/staging_dir/hostpkg/include/python3.9/Python.h:63,
                 from gpiodmodule.c:8:
/openwrt/staging_dir/hostpkg/include/python3.9/pyport.h:741:2: error: #error "LONG_BIT definition appears wrong for platform (bad gcc/glibc config?)."
 #error "LONG_BIT definition appears wrong for platform (bad gcc/glibc config?)."
  ^~~~~
make[8]: *** [Makefile:525: gpiod_la-gpiodmodule.lo] Error 1
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/libgpiod-1.4.4/bindings/python'
make[7]: *** [Makefile:544: all-recursive] Error 1
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/libgpiod-1.4.4/bindings/python'
make[6]: *** [Makefile:390: all-recursive] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/libgpiod-1.4.4/bindings'
make[5]: *** [Makefile:502: all-recursive] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/libgpiod-1.4.4'
make[4]: *** [Makefile:411: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/libgpiod-1.4.4'
make[3]: *** [Makefile:108: /openwrt/build_dir/target-mips_24kc_musl/libgpiod-1.4.4/.built] Error 2
```
