---
title: "compile.42"
date: 2021-06-29 09:38:24.605008
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
make package/feeds/packages/nbd/compile -j$(nproc) || make package/feeds/packages/nbd/compile V=s
```

#### Compile.txt

``` bash
configure: WARNING: unrecognized options: --disable-nls, --disable-glibtest, --with-syslog
configure: loading site script /openwrt/include/site/aarch64
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for aarch64-openwrt-linux-strip... aarch64-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether to enable maintainer-specific portions of Makefiles... yes
checking build system type... x86_64-pc-linux-gnu
checking host system type... aarch64-openwrt-linux-gnu
checking how to print strings... printf
checking whether make supports the include directive... yes (GNU style)
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
checking whether Large File Support should be enabled... yes
checking whether syslog logging is requested... no
checking whether a debugging version is requested... no
checking for ccache_cc option to accept ISO C99... none needed
checking how to run the C preprocessor... ccache_cc -E
checking pkg-config is at least version 0.9.0... yes
checking whether byte ordering is bigendian... (cached) no
checking for inline... inline
checking for an ANSI C-conforming const... yes
checking size of unsigned short int... 2
checking size of unsigned int... (cached) 4
checking size of unsigned long int... 8
checking size of unsigned long long int... 8
checking for dirent.h that defines DIR... yes
checking for library containing opendir... none required
checking for struct dirent.d_type... yes
checking for llseek... no
checking for alarm... yes
checking for gethostbyname... yes
checking for inet_ntoa... yes
checking for memset... yes
checking for socket... yes
checking for strerror... (cached) yes
checking for strstr... yes
checking for mkstemp... yes
checking for fdatasync... yes
checking for fallocate... yes
checking linux/falloc.h usability... yes
checking linux/falloc.h presence... yes
checking for linux/falloc.h... yes
checking whether FALLOC_FL_PUNCH_HOLE is declared... yes
checking for FALLOC_FL_PUNCH_HOLE support... yes
checking for splice... yes
checking whether F_SETPIPE_SZ is declared... yes
checking for F_SETPIPE_SZ support... yes
checking for winioctl.h... no
checking for sync_file_range... yes
checking for pid_t... yes
checking vfork.h usability... no
checking vfork.h presence... no
checking for vfork.h... no
checking for fork... yes
checking for vfork... yes
checking for working fork... cross
configure: WARNING: result yes guessed because of cross compilation
checking for working vfork... (cached) yes
(cached) checking whether client should be built... yes
checking whether to expect tlshuge test to fail... no
checking for library containing bind... none required
checking for library containing inet_ntoa... none required
checking for library containing daemon... none required
checking for sys/mount.h... yes
checking arpa/inet.h usability... yes
checking arpa/inet.h presence... yes
checking for arpa/inet.h... yes
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking netdb.h usability... yes
checking netdb.h presence... yes
checking for netdb.h... yes
checking netinet/in.h usability... yes
checking netinet/in.h presence... yes
checking for netinet/in.h... yes
checking sys/ioctl.h usability... yes
checking sys/ioctl.h presence... yes
checking for sys/ioctl.h... yes
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking syslog.h usability... yes
checking syslog.h presence... yes
checking for syslog.h... yes
checking linux/types.h usability... yes
checking linux/types.h presence... yes
checking for linux/types.h... yes
checking sys/dirent.h usability... no
checking sys/dirent.h presence... no
checking for sys/dirent.h... no
checking sys/uio.h usability... yes
checking sys/uio.h presence... yes
checking for sys/uio.h... yes
checking for GLIB... no
configure: error: Missing glib
make[3]: *** [Makefile:77: /openwrt/build_dir/target-aarch64_cortex-a72_musl/nbd-3.19/.configured_a17fb5ef857664f03cd0ce37cc5ea591] Error 1
```
