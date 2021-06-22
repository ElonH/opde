---
title: "compile.40"
date: 2021-06-22 10:51:10.649038
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
make package/feeds/packages/stunnel/compile -j$(nproc) || make package/feeds/packages/stunnel/compile V=s
```

#### Compile.txt

``` bash
autotools.mk: Found libtool v2.4 - applying patch to ./auto/ltmain.sh
bash: /openwrt/tools/libtool/files/libtool-v2.4.patch: No such file or directory
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/mips
configure: **************************************** initialization
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
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
checking whether make supports the include directive... yes (GNU style)
checking dependency style of ccache_cc... gcc3
checking whether make sets $(MAKE)... (cached) yes
checking whether make supports nested variables... (cached) yes
configure: **************************************** thread model
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking how to run the C preprocessor... ccache_cc -E
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
configure: PTHREAD mode selected
checking whether ccache_cc is Clang... no
checking whether pthreads work with -pthread... yes
checking for joinable pthread attribute... PTHREAD_CREATE_JOINABLE
checking whether more special flags are required for pthreads... no
checking for PTHREAD_PRIO_INHERIT... yes
configure: **************************************** compiler/linker flags
checking whether C compiler accepts -Wall... yes
checking whether C compiler accepts -Wextra... yes
checking whether C compiler accepts -Wpedantic... yes
checking whether C compiler accepts -Wformat=2... yes
checking whether C compiler accepts -Wconversion... yes
checking whether C compiler accepts -Wno-long-long... yes
checking whether C compiler accepts -Wno-deprecated-declarations... yes
checking whether C compiler accepts -fPIE... yes
checking whether C compiler accepts -fstack-protector... yes
checking whether the linker accepts -fPIE... yes
checking whether the linker accepts -pie... yes
checking whether the linker accepts -Wl,-z,relro... yes
checking whether the linker accepts -Wl,-z,now... yes
checking whether the linker accepts -Wl,-z,noexecstack... yes
checking whether C compiler accepts -D_FORTIFY_SOURCE=2... yes
configure: **************************************** libtool
checking how to print strings... printf
checking for a sed that does not truncate output... (cached) /openwrt/staging_dir/host/bin/sed
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
checking for mips-openwrt-linux-ar... mips-openwrt-linux-musl-gcc-ar
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
checking whether to build static libraries... no
configure: **************************************** types
checking for int8_t... yes
checking for int16_t... yes
checking for int32_t... yes
checking for int64_t... yes
checking for uint8_t... yes
checking for uint16_t... yes
checking for uint32_t... yes
checking for uint64_t... yes
checking for size_t... yes
checking for ssize_t... yes
checking for uid_t in sys/types.h... yes
checking for socklen_t... yes
checking for struct sockaddr_un... yes
checking for struct addrinfo... yes
configure: **************************************** PTY device files
configure: WARNING: cross-compilation: assuming /dev/ptmx and /dev/ptc are not available
configure: **************************************** entropy sources
configure: WARNING: cross-compilation: assuming entropy sources are not available
configure: **************************************** default group
configure: WARNING: cross-compilation: assuming nogroup is not available
checking for default group... nobody
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
configure: **************************************** header files
checking for stdint.h... (cached) yes
checking for inttypes.h... (cached) yes
checking malloc.h usability... yes
checking malloc.h presence... yes
checking for malloc.h... yes
checking ucontext.h usability... yes
checking ucontext.h presence... yes
checking for ucontext.h... yes
checking pthread.h usability... yes
checking pthread.h presence... yes
checking for pthread.h... yes
checking poll.h usability... yes
checking poll.h presence... yes
checking for poll.h... yes
checking tcpd.h usability... no
checking tcpd.h presence... no
checking for tcpd.h... no
checking stropts.h usability... yes
checking stropts.h presence... yes
checking for stropts.h... yes
checking grp.h usability... yes
checking grp.h presence... yes
checking for grp.h... yes
checking for unistd.h... (cached) yes
checking util.h usability... no
checking util.h presence... no
checking for util.h... no
checking libutil.h usability... no
checking libutil.h presence... no
checking for libutil.h... no
checking pty.h usability... yes
checking pty.h presence... yes
checking for pty.h... yes
checking limits.h usability... yes
checking limits.h presence... yes
checking for limits.h... yes
checking for sys/types.h... (cached) yes
checking sys/select.h usability... yes
checking sys/select.h presence... yes
checking for sys/select.h... yes
checking sys/poll.h usability... yes
checking sys/poll.h presence... yes
checking for sys/poll.h... yes
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking sys/un.h usability... yes
checking sys/un.h presence... yes
checking for sys/un.h... yes
checking sys/ioctl.h usability... yes
checking sys/ioctl.h presence... yes
checking for sys/ioctl.h... yes
checking sys/filio.h usability... no
checking sys/filio.h presence... no
checking for sys/filio.h... no
checking sys/resource.h usability... yes
checking sys/resource.h presence... yes
checking for sys/resource.h... yes
checking sys/uio.h usability... yes
checking sys/uio.h presence... yes
checking for sys/uio.h... yes
checking sys/syscall.h usability... yes
checking sys/syscall.h presence... yes
checking for sys/syscall.h... yes
checking sys/param.h usability... yes
checking sys/param.h presence... yes
checking for sys/param.h... yes
checking linux/sched.h usability... yes
checking linux/sched.h presence... yes
checking for linux/sched.h... yes
checking for struct msghdr.msg_control... yes
checking for linux/netfilter_ipv4.h... yes
configure: **************************************** libraries
checking for library containing gethostbyname... none required
checking for library containing yp_get_default_domain... no
checking for library containing socket... none required
checking for library containing openpty... none required
checking for library containing dlopen... none required
checking for library containing shl_load... no
configure: **************************************** library functions
checking for snprintf... yes
checking for vsnprintf... (cached) yes
checking for openpty... yes
checking for _getpty... no
checking for daemon... yes
checking for waitpid... yes
checking for wait4... yes
checking for setsid... yes
checking for setgroups... yes
checking for chroot... yes
checking for realpath... yes
checking for sysconf... yes
checking for getrlimit... yes
checking for pthread_sigmask... yes
checking for localtime_r... yes
checking for getcontext... no
checking for __makecontext_v2... no
checking for poll... yes
checking for gethostbyname2... yes
checking for endhostent... yes
checking for getnameinfo... yes
checking for getaddrinfo... yes
checking for broken poll() implementation... no
checking for pipe2... yes
checking for accept4... yes
configure: **************************************** optional features
checking whether to enable IPv6 support... yes (default)
checking whether to enable FIPS support... autodetecting
checking whether to enable systemd socket activation support... no
checking whether to enable TCP wrappers support... no
configure: **************************************** TLS
checking for TLS directory... not found
configure: error: 
Could not find your TLS library installation dir
Use --with-ssl option to fix this problem

make[3]: *** [Makefile:91: /openwrt/build_dir/target-mips_24kc_musl/stunnel-5.59/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
