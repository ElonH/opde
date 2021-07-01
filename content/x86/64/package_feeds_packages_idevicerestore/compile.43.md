---
title: "compile.43"
date: 2021-07-01 09:10:23.274837
hidden: false
draft: false
weight: -43
---

build number: `43`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/idevicerestore/compile -j$(nproc) || make package/feeds/packages/idevicerestore/compile V=s
```

#### Compile.txt

``` bash
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/x86_64
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-openwrt-linux-gnu
checking target system type... x86_64-openwrt-linux-gnu
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for x86_64-openwrt-linux-strip... x86_64-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether make supports nested variables... (cached) yes
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
checking whether make supports the include directive... yes (GNU style)
checking dependency style of ccache_cc... gcc3
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache_cc... x86_64-openwrt-linux-musl-ld
checking if the linker (x86_64-openwrt-linux-musl-ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... x86_64-openwrt-linux-musl-gcc-nm
checking the name lister (x86_64-openwrt-linux-musl-gcc-nm) interface... BSD nm
checking whether ln -s works... yes
checking the maximum length of command line arguments... 3145728
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
checking for a working dd... /usr/bin/dd
checking how to truncate binary pipes... /usr/bin/dd bs=4096 count=1
checking for x86_64-openwrt-linux-mt... no
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
checking whether the ccache_cc linker (x86_64-openwrt-linux-musl-ld -m elf_x86_64) supports shared libraries... yes
checking whether -lc should be explicitly linked in... no
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... yes
checking pkg-config is at least version 0.9.0... yes
checking for libirecovery... yes
checking for libimobiledevice... yes
checking for libplist... yes
checking for libzip... yes
checking for libcurl... yes
checking for zlib... yes
checking for openssl... yes
checking whether we need platform-specific build settings... yes
checking whether ccache_cc is Clang... no
checking whether pthreads work with -pthread... yes
checking for joinable pthread attribute... PTHREAD_CREATE_JOINABLE
checking whether more special flags are required for pthreads... no
checking for PTHREAD_PRIO_INHERIT... yes
checking for strsep... yes
checking for strcspn... yes
checking for mkstemp... yes
checking for realpath... yes
checking for IDEVICE_E_TIMEOUT in enum idevice_error_t... yes
checking for RESTORE_E_RECEIVE_TIMEOUT in enum restored_error_t... yes
checking for enum idevice_connection_type... yes
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking whether make supports nested variables... (cached) yes
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating Makefile
config.status: creating src/Makefile
config.status: creating docs/Makefile
config.status: creating config.h
config.status: executing depfiles commands
config.status: executing libtool commands
configure: WARNING: unrecognized options: --disable-nls

Configuration for idevicerestore 1.0.0:
-------------------------------------------

  Install prefix: .........: /usr

  Now type 'make' to build idevicerestore 1.0.0,
  and then 'make install' for installation.

make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/idevicerestore-1.0.0'
make  all-recursive
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/idevicerestore-1.0.0'
Making all in src
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/idevicerestore-1.0.0/src'
  CC       idevicerestore-idevicerestore.o
  CC       idevicerestore-common.o
  CC       idevicerestore-tss.o
  CC       idevicerestore-fls.o
  CC       idevicerestore-mbn.o
  CC       idevicerestore-img3.o
  CC       idevicerestore-img4.o
  CC       idevicerestore-ftab.o
  CC       idevicerestore-ipsw.o
  CC       idevicerestore-normal.o
  CC       idevicerestore-dfu.o
  CC       idevicerestore-recovery.o
  CC       idevicerestore-restore.o
  CC       idevicerestore-asr.o
  CC       idevicerestore-fdr.o
  CC       idevicerestore-limera1n.o
  CC       idevicerestore-download.o
  CC       idevicerestore-locking.o
  CC       idevicerestore-socket.o
  CC       idevicerestore-thread.o
  CC       idevicerestore-jsmn.o
  CC       idevicerestore-json_plist.o
  CCLD     idevicerestore
libtool:   error: require no space between '-L' and '-lzip'
make[6]: *** [Makefile:496: idevicerestore] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/idevicerestore-1.0.0/src'
make[5]: *** [Makefile:434: all-recursive] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/idevicerestore-1.0.0'
make[4]: *** [Makefile:366: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/idevicerestore-1.0.0'
make[3]: *** [Makefile:50: /openwrt/build_dir/target-x86_64_musl/idevicerestore-1.0.0/.built] Error 2
```
