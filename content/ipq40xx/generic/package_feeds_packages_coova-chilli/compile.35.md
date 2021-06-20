---
title: "compile.35"
date: 2021-06-20 00:36:26.154458
hidden: false
draft: false
weight: -35
---

build number: `35`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/coova-chilli/compile -j$(nproc) || make package/feeds/packages/coova-chilli/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-kernel510.patch using plaintext: 
patching file src/linux/xt_coova.c

Applying ./patches/100-fix_compile_kmod.patch using plaintext: 
patching file src/linux/Makefile
OpenWrt-libtoolize: putting auxiliary files in `.'.
OpenWrt-libtoolize: copying file `./ltmain.sh'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `m4'.
OpenWrt-libtoolize: copying file `m4/libtool.m4'
OpenWrt-libtoolize: copying file `m4/ltoptions.m4'
OpenWrt-libtoolize: copying file `m4/ltsugar.m4'
OpenWrt-libtoolize: copying file `m4/ltversion.m4'
OpenWrt-libtoolize: copying file `m4/lt~obsolete.m4'
configure.ac:17: installing './compile'
configure.ac:26: installing './config.guess'
configure.ac:26: installing './config.sub'
configure.ac:8: installing './install-sh'
configure.ac:8: installing './missing'
bstring/Makefile.am: installing './depcomp'
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/usr/share/aclocal -I m4 -I . --force -I m4
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
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
autoreconf: Leaving directory `.'
configure: loading site script /openwrt/include/site/arm
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for arm-openwrt-linux-strip... arm-openwrt-linux-muslgnueabi-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether the C++ compiler works... yes
checking for C++ compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C++ compiler... yes
checking whether ccache_cxx accepts -g... yes
checking for style of include used by make... GNU
checking dependency style of ccache_cxx... gcc3
checking for gawk... (cached) gawk
checking for arm-openwrt-linux-gcc... ccache_cc
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
checking whether ccache_cc understands -c and -o together... yes
checking dependency style of ccache_cc... gcc3
checking whether ccache_cc and cc understand -c and -o together... yes
checking for ccache_cc option to accept ISO C99... none needed
checking how to run the C preprocessor... ccache_cc -E
checking whether ln -s works... yes
checking whether make sets $(MAKE)... (cached) yes
checking build system type... x86_64-pc-linux-gnu
checking host system type... arm-openwrt-linux-gnu
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache_cc... arm-openwrt-linux-muslgnueabi-ld
checking if the linker (arm-openwrt-linux-muslgnueabi-ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... arm-openwrt-linux-muslgnueabi-gcc-nm
checking the name lister (arm-openwrt-linux-muslgnueabi-gcc-nm) interface... BSD nm
checking the maximum length of command line arguments... 3145728
checking whether the shell understands some XSI constructs... yes
checking whether the shell understands "+="... yes
checking how to convert x86_64-pc-linux-gnu file names to arm-openwrt-linux-gnu format... func_convert_file_noop
checking how to convert x86_64-pc-linux-gnu file names to toolchain format... func_convert_file_noop
checking for arm-openwrt-linux-muslgnueabi-ld option to reload object files... -r
checking for arm-openwrt-linux-objdump... arm-openwrt-linux-muslgnueabi-objdump
checking how to recognize dependent libraries... pass_all
checking for arm-openwrt-linux-dlltool... no
checking for dlltool... no
checking how to associate runtime and link libraries... printf %s\n
checking for arm-openwrt-linux-ar... arm-openwrt-linux-muslgnueabi-gcc-ar
checking for archiver @FILE support... @
checking for arm-openwrt-linux-strip... (cached) arm-openwrt-linux-muslgnueabi-strip
checking for arm-openwrt-linux-ranlib... arm-openwrt-linux-muslgnueabi-gcc-ranlib
checking command to parse arm-openwrt-linux-muslgnueabi-gcc-nm output from ccache_cc object... ok
checking for sysroot... no
checking for arm-openwrt-linux-mt... no
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
checking whether the ccache_cc linker (arm-openwrt-linux-muslgnueabi-ld) supports shared libraries... yes
checking whether -lc should be explicitly linked in... no
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... yes
checking how to run the C++ preprocessor... ccache_cxx -E
checking for ld used by ccache_cxx... arm-openwrt-linux-muslgnueabi-ld
checking if the linker (arm-openwrt-linux-muslgnueabi-ld) is GNU ld... yes
checking whether the ccache_cxx linker (arm-openwrt-linux-muslgnueabi-ld) supports shared libraries... yes
checking for ccache_cxx option to produce PIC... -fPIC -DPIC
checking if ccache_cxx PIC flag -fPIC -DPIC works... yes
checking if ccache_cxx static flag -static works... yes
checking if ccache_cxx supports -c -o file.o... yes
checking if ccache_cxx supports -c -o file.o... (cached) yes
checking whether the ccache_cxx linker (arm-openwrt-linux-muslgnueabi-ld) supports shared libraries... yes
checking dynamic linker characteristics... (cached) GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
linux
checking if if_packet.h has tpacket_stats defined... yes
checking if tpacket_auxdata struct has tp_vlan_tci member... yes
checking for ANSI C header files... (cached) yes
checking for sys/types.h... (cached) yes
checking for netinet/in.h... yes
checking for arpa/nameser.h... yes
checking for netdb.h... yes
checking for resolv.h... yes
checking arpa/inet.h usability... yes
checking arpa/inet.h presence... yes
checking for arpa/inet.h... yes
checking errno.h usability... yes
checking errno.h presence... yes
checking for errno.h... yes
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking dirent.h usability... yes
checking dirent.h presence... yes
checking for dirent.h... yes
checking for inttypes.h... (cached) yes
checking limits.h usability... yes
checking limits.h presence... yes
checking for limits.h... yes
checking for netdb.h... (cached) yes
checking for netinet/in.h... (cached) yes
checking netinet/tcp.h usability... yes
checking netinet/tcp.h presence... yes
checking for netinet/tcp.h... yes
checking for stdint.h... (cached) yes
checking stddef.h usability... yes
checking stddef.h presence... yes
checking for stddef.h... yes
checking for stdlib.h... (cached) yes
checking for string.h... (cached) yes
checking for strings.h... (cached) yes
checking sys/ioctl.h usability... yes
checking sys/ioctl.h presence... yes
checking for sys/ioctl.h... yes
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking linux/sysinfo.h usability... yes
checking linux/sysinfo.h presence... yes
checking for linux/sysinfo.h... yes
checking sys/sysinfo.h usability... yes
checking sys/sysinfo.h presence... yes
checking for sys/sysinfo.h... yes
checking sys/param.h usability... yes
checking sys/param.h presence... yes
checking for sys/param.h... yes
checking sys/time.h usability... yes
checking sys/time.h presence... yes
checking for sys/time.h... yes
checking time.h usability... yes
checking time.h presence... yes
checking for time.h... yes
checking sys/ipc.h usability... yes
checking sys/ipc.h presence... yes
checking for sys/ipc.h... yes
checking sys/msg.h usability... yes
checking sys/msg.h presence... yes
checking for sys/msg.h... yes
checking signal.h usability... yes
checking signal.h presence... yes
checking for signal.h... yes
checking sys/wait.h usability... yes
checking sys/wait.h presence... yes
checking for sys/wait.h... yes
checking sys/un.h usability... yes
checking sys/un.h presence... yes
checking for sys/un.h... yes
checking ifaddrs.h usability... yes
checking ifaddrs.h presence... yes
checking for ifaddrs.h... yes
checking for sys/stat.h... (cached) yes
checking for sys/types.h... (cached) yes
checking regex.h usability... yes
checking regex.h presence... yes
checking for regex.h... yes
checking syslog.h usability... yes
checking syslog.h presence... yes
checking for syslog.h... yes
checking poll.h usability... yes
checking poll.h presence... yes
checking for poll.h... yes
checking sys/epoll.h usability... yes
checking sys/epoll.h presence... yes
checking for sys/epoll.h... yes
checking for unistd.h... (cached) yes
checking endian.h usability... yes
checking endian.h presence... yes
checking for endian.h... yes
checking libgen.h usability... yes
checking libgen.h presence... yes
checking for libgen.h... yes
checking asm/types.h usability... yes
checking asm/types.h presence... yes
checking for asm/types.h... yes
checking pwd.h usability... yes
checking pwd.h presence... yes
checking for pwd.h... yes
checking grp.h usability... yes
checking grp.h presence... yes
checking for grp.h... yes
checking wchar.h usability... yes
checking wchar.h presence... yes
checking for wchar.h... yes
checking stdarg.h usability... yes
checking stdarg.h presence... yes
checking for stdarg.h... yes
checking for resolv.h... (cached) yes
checking for net/route.h... yes
checking for net/if.h... yes
checking for net/if_arp.h... yes
checking for net/if_tun.h... no
checking for net/ethernet.h... yes
checking for inttypes.h... (cached) yes
checking whether INFINITY is declared... yes
checking whether nan is declared... yes
checking whether isnan is declared... yes
checking whether isinf is declared... yes
checking whether _isnan is declared... no
checking whether _finite is declared... no
checking for an ANSI C-conforming const... yes
checking for uid_t in sys/types.h... yes
checking for inline... inline
checking for int16_t... yes
checking for int32_t... yes
checking for int8_t... yes
checking for mode_t... yes
checking for pid_t... yes
checking for size_t... yes
checking for ssize_t... yes
checking for uint16_t... yes
checking for uint32_t... yes
checking for uint64_t... yes
checking for uint8_t... yes
checking for ptrdiff_t... yes
checking for unistd.h... (cached) yes
checking for working chown... no
checking vfork.h usability... no
checking vfork.h presence... no
checking for vfork.h... no
checking for fork... yes
checking for vfork... yes
checking for working fork... cross
configure: WARNING: result yes guessed because of cross compilation
checking for working vfork... (cached) yes
checking whether ccache_cc needs -traditional... no
checking for working memcmp... (cached) yes
checking sys/select.h usability... yes
checking sys/select.h presence... yes
checking for sys/select.h... yes
checking for sys/socket.h... (cached) yes
checking types of arguments for select... int,fd_set *,struct timeval *
checking whether time.h and sys/time.h may both be included... yes
checking for sys/time.h... (cached) yes
checking for unistd.h... (cached) yes
checking for stdlib.h... (cached) yes
checking for sys/param.h... (cached) yes
checking for alarm... yes
checking for working mktime... no
checking for getpagesize... yes
checking for working mmap... no
checking for bzero... (cached) yes
checking for clock_gettime... yes
checking for dup2... yes
checking for gethostbyname... yes
checking for getprotoent... yes
checking for gettimeofday... (cached) yes
checking for inet_ntoa... yes
checking for memchr... yes
checking for memmove... yes
checking for memset... yes
checking for mkdir... yes
checking for munmap... yes
checking for regcomp... yes
checking for select... yes
checking for setenv... yes
checking for socket... yes
checking for strcasecmp... yes
checking for strchr... yes
checking for strcspn... yes
checking for strdup... yes
checking for strerror... (cached) yes
checking for strncasecmp... yes
checking for strndup... yes
checking for strrchr... yes
checking for strspn... yes
checking for strstr... yes
checking for strtol... yes
checking for getline... yes
checking for dirname... yes
checking for glob... yes
checking for getaddrinfo... (cached) yes
checking for getnameinfo... yes
checking for getifaddrs... yes
checking for sysinfo... yes
checking for strlcpy... yes
checking for tzset... yes
checking for snprintf... yes
checking for vsnprintf... (cached) yes
checking for vasprintf... yes
checking for res_init in -lresolv... yes
checking for clock_gettime in -lrt... yes
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating Makefile
config.status: creating bstring/Makefile
config.status: creating conf/Makefile
config.status: creating doc/Makefile
config.status: creating json/Makefile
config.status: creating miniportal/Makefile
config.status: creating src/Makefile
config.status: creating src/mssl/Makefile
config.status: creating www/Makefile
config.status: creating config.h
config.status: creating json/json_config.h
config.status: executing depfiles commands
config.status: executing libtool commands
make[4]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6'
make  all-recursive
make[5]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6'
Making all in bstring
make[6]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/bstring'
/bin/bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include   -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT bstrlib.lo -MD -MP -MF .deps/bstrlib.Tpo -c -o bstrlib.lo bstrlib.c
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT bstrlib.lo -MD -MP -MF .deps/bstrlib.Tpo -c bstrlib.c  -fPIC -DPIC -o .libs/bstrlib.o
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT bstrlib.lo -MD -MP -MF .deps/bstrlib.Tpo -c bstrlib.c -o bstrlib.o >/dev/null 2>&1
mv -f .deps/bstrlib.Tpo .deps/bstrlib.Plo
/bin/bash ../libtool  --tag=CC   --mode=link ccache_cc  -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error   -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/lib -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/lib -znow -zrelro  -o libbstring.la -rpath /usr/lib bstrlib.lo  -lrt -lresolv 
OpenWrt-libtool: link: ccache_cc -shared  -fPIC -DPIC  .libs/bstrlib.o   -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/lib -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/lib -lrt -lresolv  -Os -mfloat-abi=hard -fstack-protector -Wl,-z -Wl,now -Wl,-z -Wl,relro   -Wl,-soname -Wl,libbstring.so.0 -o .libs/libbstring.so.0.0.0
OpenWrt-libtool: link: (cd ".libs" && rm -f "libbstring.so.0" && ln -s "libbstring.so.0.0.0" "libbstring.so.0")
OpenWrt-libtool: link: (cd ".libs" && rm -f "libbstring.so" && ln -s "libbstring.so.0.0.0" "libbstring.so")
OpenWrt-libtool: link: arm-openwrt-linux-muslgnueabi-gcc-ar cru .libs/libbstring.a  bstrlib.o
/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/lib/gcc/arm-openwrt-linux-muslgnueabi/8.4.0/../../../../arm-openwrt-linux-muslgnueabi/bin/ar: `u' modifier ignored since `D' is the default (see `U')
OpenWrt-libtool: link: arm-openwrt-linux-muslgnueabi-gcc-ranlib .libs/libbstring.a
OpenWrt-libtool: link: ( cd ".libs" && rm -f "libbstring.la" && ln -s "../libbstring.la" "libbstring.la" )
make[6]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/bstring'
Making all in src
make[6]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/src'
Making all in linux
make[7]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/src/linux'
ccache_cc -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -fPIC -O2 -Wall -D_INIT=libxt_coova_init -c -o libxt_coova.o libxt_coova.c;
ccache_cc -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -shared -o libxt_coova.so libxt_coova.o;
make -C /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/linux-5.4.124 M=$PWD;
make[8]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/linux-5.4.124'
  AR      /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/src/linux/built-in.a
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/src/linux/xt_coova.o
  Building modules, stage 2.
  MODPOST 1 modules
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/src/linux/xt_coova.mod.o
  LD [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/src/linux/xt_coova.ko
make[8]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/linux-5.4.124'
rm libxt_coova.o
make[7]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/src/linux'
make[7]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/src'
depbase=`echo chilli.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT chilli.lo -MD -MP -MF $depbase.Tpo -c -o chilli.lo chilli.c &&\
mv -f $depbase.Tpo $depbase.Plo
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT chilli.lo -MD -MP -MF .deps/chilli.Tpo -c chilli.c  -fPIC -DPIC -o .libs/chilli.o
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT chilli.lo -MD -MP -MF .deps/chilli.Tpo -c chilli.c -o chilli.o >/dev/null 2>&1
depbase=`echo tun.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT tun.lo -MD -MP -MF $depbase.Tpo -c -o tun.lo tun.c &&\
mv -f $depbase.Tpo $depbase.Plo
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT tun.lo -MD -MP -MF .deps/tun.Tpo -c tun.c  -fPIC -DPIC -o .libs/tun.o
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT tun.lo -MD -MP -MF .deps/tun.Tpo -c tun.c -o tun.o >/dev/null 2>&1
depbase=`echo ippool.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT ippool.lo -MD -MP -MF $depbase.Tpo -c -o ippool.lo ippool.c &&\
mv -f $depbase.Tpo $depbase.Plo
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT ippool.lo -MD -MP -MF .deps/ippool.Tpo -c ippool.c  -fPIC -DPIC -o .libs/ippool.o
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT ippool.lo -MD -MP -MF .deps/ippool.Tpo -c ippool.c -o ippool.o >/dev/null 2>&1
depbase=`echo radius.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT radius.lo -MD -MP -MF $depbase.Tpo -c -o radius.lo radius.c &&\
mv -f $depbase.Tpo $depbase.Plo
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT radius.lo -MD -MP -MF .deps/radius.Tpo -c radius.c  -fPIC -DPIC -o .libs/radius.o
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT radius.lo -MD -MP -MF .deps/radius.Tpo -c radius.c -o radius.o >/dev/null 2>&1
depbase=`echo md5.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT md5.lo -MD -MP -MF $depbase.Tpo -c -o md5.lo md5.c &&\
mv -f $depbase.Tpo $depbase.Plo
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT md5.lo -MD -MP -MF .deps/md5.Tpo -c md5.c  -fPIC -DPIC -o .libs/md5.o
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT md5.lo -MD -MP -MF .deps/md5.Tpo -c md5.c -o md5.o >/dev/null 2>&1
depbase=`echo redir.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT redir.lo -MD -MP -MF $depbase.Tpo -c -o redir.lo redir.c &&\
mv -f $depbase.Tpo $depbase.Plo
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT redir.lo -MD -MP -MF .deps/redir.Tpo -c redir.c  -fPIC -DPIC -o .libs/redir.o
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT redir.lo -MD -MP -MF .deps/redir.Tpo -c redir.c -o redir.o >/dev/null 2>&1
depbase=`echo dhcp.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT dhcp.lo -MD -MP -MF $depbase.Tpo -c -o dhcp.lo dhcp.c &&\
mv -f $depbase.Tpo $depbase.Plo
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT dhcp.lo -MD -MP -MF .deps/dhcp.Tpo -c dhcp.c  -fPIC -DPIC -o .libs/dhcp.o
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT dhcp.lo -MD -MP -MF .deps/dhcp.Tpo -c dhcp.c -o dhcp.o >/dev/null 2>&1
depbase=`echo iphash.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT iphash.lo -MD -MP -MF $depbase.Tpo -c -o iphash.lo iphash.c &&\
mv -f $depbase.Tpo $depbase.Plo
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT iphash.lo -MD -MP -MF .deps/iphash.Tpo -c iphash.c  -fPIC -DPIC -o .libs/iphash.o
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT iphash.lo -MD -MP -MF .deps/iphash.Tpo -c iphash.c -o iphash.o >/dev/null 2>&1
depbase=`echo lookup.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT lookup.lo -MD -MP -MF $depbase.Tpo -c -o lookup.lo lookup.c &&\
mv -f $depbase.Tpo $depbase.Plo
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT lookup.lo -MD -MP -MF .deps/lookup.Tpo -c lookup.c  -fPIC -DPIC -o .libs/lookup.o
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT lookup.lo -MD -MP -MF .deps/lookup.Tpo -c lookup.c -o lookup.o >/dev/null 2>&1
depbase=`echo util.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT util.lo -MD -MP -MF $depbase.Tpo -c -o util.lo util.c &&\
mv -f $depbase.Tpo $depbase.Plo
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT util.lo -MD -MP -MF .deps/util.Tpo -c util.c  -fPIC -DPIC -o .libs/util.o
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT util.lo -MD -MP -MF .deps/util.Tpo -c util.c -o util.o >/dev/null 2>&1
depbase=`echo options.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT options.lo -MD -MP -MF $depbase.Tpo -c -o options.lo options.c &&\
mv -f $depbase.Tpo $depbase.Plo
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT options.lo -MD -MP -MF .deps/options.Tpo -c options.c  -fPIC -DPIC -o .libs/options.o
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT options.lo -MD -MP -MF .deps/options.Tpo -c options.c -o options.o >/dev/null 2>&1
depbase=`echo statusfile.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT statusfile.lo -MD -MP -MF $depbase.Tpo -c -o statusfile.lo statusfile.c &&\
mv -f $depbase.Tpo $depbase.Plo
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT statusfile.lo -MD -MP -MF .deps/statusfile.Tpo -c statusfile.c  -fPIC -DPIC -o .libs/statusfile.o
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT statusfile.lo -MD -MP -MF .deps/statusfile.Tpo -c statusfile.c -o statusfile.o >/dev/null 2>&1
depbase=`echo conn.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT conn.lo -MD -MP -MF $depbase.Tpo -c -o conn.lo conn.c &&\
mv -f $depbase.Tpo $depbase.Plo
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT conn.lo -MD -MP -MF .deps/conn.Tpo -c conn.c  -fPIC -DPIC -o .libs/conn.o
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT conn.lo -MD -MP -MF .deps/conn.Tpo -c conn.c -o conn.o >/dev/null 2>&1
depbase=`echo sig.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT sig.lo -MD -MP -MF $depbase.Tpo -c -o sig.lo sig.c &&\
mv -f $depbase.Tpo $depbase.Plo
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT sig.lo -MD -MP -MF .deps/sig.Tpo -c sig.c  -fPIC -DPIC -o .libs/sig.o
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT sig.lo -MD -MP -MF .deps/sig.Tpo -c sig.c -o sig.o >/dev/null 2>&1
depbase=`echo garden.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT garden.lo -MD -MP -MF $depbase.Tpo -c -o garden.lo garden.c &&\
mv -f $depbase.Tpo $depbase.Plo
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT garden.lo -MD -MP -MF .deps/garden.Tpo -c garden.c  -fPIC -DPIC -o .libs/garden.o
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT garden.lo -MD -MP -MF .deps/garden.Tpo -c garden.c -o garden.o >/dev/null 2>&1
depbase=`echo dns.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT dns.lo -MD -MP -MF $depbase.Tpo -c -o dns.lo dns.c &&\
mv -f $depbase.Tpo $depbase.Plo
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT dns.lo -MD -MP -MF .deps/dns.Tpo -c dns.c  -fPIC -DPIC -o .libs/dns.o
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT dns.lo -MD -MP -MF .deps/dns.Tpo -c dns.c -o dns.o >/dev/null 2>&1
depbase=`echo session.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT session.lo -MD -MP -MF $depbase.Tpo -c -o session.lo session.c &&\
mv -f $depbase.Tpo $depbase.Plo
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT session.lo -MD -MP -MF .deps/session.Tpo -c session.c  -fPIC -DPIC -o .libs/session.o
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT session.lo -MD -MP -MF .deps/session.Tpo -c session.c -o session.o >/dev/null 2>&1
depbase=`echo pkt.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT pkt.lo -MD -MP -MF $depbase.Tpo -c -o pkt.lo pkt.c &&\
mv -f $depbase.Tpo $depbase.Plo
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT pkt.lo -MD -MP -MF .deps/pkt.Tpo -c pkt.c  -fPIC -DPIC -o .libs/pkt.o
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT pkt.lo -MD -MP -MF .deps/pkt.Tpo -c pkt.c -o pkt.o >/dev/null 2>&1
depbase=`echo chksum.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT chksum.lo -MD -MP -MF $depbase.Tpo -c -o chksum.lo chksum.c &&\
mv -f $depbase.Tpo $depbase.Plo
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT chksum.lo -MD -MP -MF .deps/chksum.Tpo -c chksum.c  -fPIC -DPIC -o .libs/chksum.o
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT chksum.lo -MD -MP -MF .deps/chksum.Tpo -c chksum.c -o chksum.o >/dev/null 2>&1
depbase=`echo net.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT net.lo -MD -MP -MF $depbase.Tpo -c -o net.lo net.c &&\
mv -f $depbase.Tpo $depbase.Plo
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT net.lo -MD -MP -MF .deps/net.Tpo -c net.c  -fPIC -DPIC -o .libs/net.o
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT net.lo -MD -MP -MF .deps/net.Tpo -c net.c -o net.o >/dev/null 2>&1
depbase=`echo safe.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT safe.lo -MD -MP -MF $depbase.Tpo -c -o safe.lo safe.c &&\
mv -f $depbase.Tpo $depbase.Plo
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT safe.lo -MD -MP -MF .deps/safe.Tpo -c safe.c  -fPIC -DPIC -o .libs/safe.o
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT safe.lo -MD -MP -MF .deps/safe.Tpo -c safe.c -o safe.o >/dev/null 2>&1
depbase=`echo sfhash.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT sfhash.lo -MD -MP -MF $depbase.Tpo -c -o sfhash.lo sfhash.c &&\
mv -f $depbase.Tpo $depbase.Plo
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT sfhash.lo -MD -MP -MF .deps/sfhash.Tpo -c sfhash.c  -fPIC -DPIC -o .libs/sfhash.o
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT sfhash.lo -MD -MP -MF .deps/sfhash.Tpo -c sfhash.c -o sfhash.o >/dev/null 2>&1
depbase=`echo cmdsock.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT cmdsock.lo -MD -MP -MF $depbase.Tpo -c -o cmdsock.lo cmdsock.c &&\
mv -f $depbase.Tpo $depbase.Plo
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT cmdsock.lo -MD -MP -MF .deps/cmdsock.Tpo -c cmdsock.c  -fPIC -DPIC -o .libs/cmdsock.o
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT cmdsock.lo -MD -MP -MF .deps/cmdsock.Tpo -c cmdsock.c -o cmdsock.o >/dev/null 2>&1
depbase=`echo kcoova.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/bash ../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT kcoova.lo -MD -MP -MF $depbase.Tpo -c -o kcoova.lo kcoova.c &&\
mv -f $depbase.Tpo $depbase.Plo
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT kcoova.lo -MD -MP -MF .deps/kcoova.Tpo -c kcoova.c  -fPIC -DPIC -o .libs/kcoova.o
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -MT kcoova.lo -MD -MP -MF .deps/kcoova.Tpo -c kcoova.c -o kcoova.o >/dev/null 2>&1
/bin/bash ../libtool  --tag=CC   --mode=link ccache_cc -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error   -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/lib -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/lib -znow -zrelro  -o libchilli.la -rpath /usr/lib chilli.lo tun.lo ippool.lo radius.lo md5.lo redir.lo dhcp.lo iphash.lo lookup.lo util.lo options.lo statusfile.lo conn.lo sig.lo garden.lo dns.lo session.lo pkt.lo chksum.lo net.lo safe.lo    sfhash.lo        cmdsock.lo kcoova.lo   ../bstring/libbstring.la      -lrt -lresolv 
OpenWrt-libtool: link: ccache_cc -shared  -fPIC -DPIC  .libs/chilli.o .libs/tun.o .libs/ippool.o .libs/radius.o .libs/md5.o .libs/redir.o .libs/dhcp.o .libs/iphash.o .libs/lookup.o .libs/util.o .libs/options.o .libs/statusfile.o .libs/conn.o .libs/sig.o .libs/garden.o .libs/dns.o .libs/session.o .libs/pkt.o .libs/chksum.o .libs/net.o .libs/safe.o .libs/sfhash.o .libs/cmdsock.o .libs/kcoova.o   -Wl,-rpath -Wl,/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/bstring/.libs -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/lib -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/lib ../bstring/.libs/libbstring.so -lrt -lresolv  -Os -mfloat-abi=hard -fstack-protector -Wl,-z -Wl,now -Wl,-z -Wl,relro   -Wl,-soname -Wl,libchilli.so.0 -o .libs/libchilli.so.0.0.0
OpenWrt-libtool: link: (cd ".libs" && rm -f "libchilli.so.0" && ln -s "libchilli.so.0.0.0" "libchilli.so.0")
OpenWrt-libtool: link: (cd ".libs" && rm -f "libchilli.so" && ln -s "libchilli.so.0.0.0" "libchilli.so")
OpenWrt-libtool: link: arm-openwrt-linux-muslgnueabi-gcc-ar cru .libs/libchilli.a  chilli.o tun.o ippool.o radius.o md5.o redir.o dhcp.o iphash.o lookup.o util.o options.o statusfile.o conn.o sig.o garden.o dns.o session.o pkt.o chksum.o net.o safe.o sfhash.o cmdsock.o kcoova.o
/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/lib/gcc/arm-openwrt-linux-muslgnueabi/8.4.0/../../../../arm-openwrt-linux-muslgnueabi/bin/ar: `u' modifier ignored since `D' is the default (see `U')
OpenWrt-libtool: link: arm-openwrt-linux-muslgnueabi-gcc-ranlib .libs/libchilli.a
OpenWrt-libtool: link: ( cd ".libs" && rm -f "libchilli.la" && ln -s "../libchilli.la" "libchilli.la" )
depbase=`echo main.o | sed 's|[^/]*$|.deps/&|;s|\.o$||'`;\
ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT main.o -MD -MP -MF $depbase.Tpo -c -o main.o main.c &&\
mv -f $depbase.Tpo $depbase.Po
/bin/bash ../libtool  --tag=CC   --mode=link ccache_cc -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error   -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/lib -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/lib -znow -zrelro  -o chilli main.o libchilli.la  ../bstring/libbstring.la         -lrt -lresolv 
OpenWrt-libtool: link: ccache_cc -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z -Wl,now -Wl,-z -Wl,relro -DPIC -fpic -Wno-error -znow -zrelro -o .libs/chilli main.o  -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/lib -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/lib ./.libs/libchilli.so /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/bstring/.libs/libbstring.so ../bstring/.libs/libbstring.so -lrt -lresolv
depbase=`echo main-response.o | sed 's|[^/]*$|.deps/&|;s|\.o$||'`;\
ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT main-response.o -MD -MP -MF $depbase.Tpo -c -o main-response.o main-response.c &&\
mv -f $depbase.Tpo $depbase.Po
/bin/bash ../libtool  --tag=CC   --mode=link ccache_cc -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error   -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/lib -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/lib -znow -zrelro  -o chilli_response main-response.o libchilli.la  ../bstring/libbstring.la         -lrt -lresolv 
OpenWrt-libtool: link: ccache_cc -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z -Wl,now -Wl,-z -Wl,relro -DPIC -fpic -Wno-error -znow -zrelro -o .libs/chilli_response main-response.o  -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/lib -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/lib ./.libs/libchilli.so /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/bstring/.libs/libbstring.so ../bstring/.libs/libbstring.so -lrt -lresolv
depbase=`echo main-radconfig.o | sed 's|[^/]*$|.deps/&|;s|\.o$||'`;\
ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT main-radconfig.o -MD -MP -MF $depbase.Tpo -c -o main-radconfig.o main-radconfig.c &&\
mv -f $depbase.Tpo $depbase.Po
/bin/bash ../libtool  --tag=CC   --mode=link ccache_cc -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error   -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/lib -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/lib -znow -zrelro  -o chilli_radconfig main-radconfig.o libchilli.la  ../bstring/libbstring.la         -lrt -lresolv 
OpenWrt-libtool: link: ccache_cc -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z -Wl,now -Wl,-z -Wl,relro -DPIC -fpic -Wno-error -znow -zrelro -o .libs/chilli_radconfig main-radconfig.o  -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/lib -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/lib ./.libs/libchilli.so /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/bstring/.libs/libbstring.so ../bstring/.libs/libbstring.so -lrt -lresolv
cat cmdline.ggo  | gengetopt -C 
cp cmdline.c cmdline.c.orig
patch -p0 < cmdline.patch
patching file cmdline.c
Hunk #1 succeeded at 2316 (offset 414 lines).
depbase=`echo main-opt.o | sed 's|[^/]*$|.deps/&|;s|\.o$||'`;\
ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT main-opt.o -MD -MP -MF $depbase.Tpo -c -o main-opt.o main-opt.c &&\
mv -f $depbase.Tpo $depbase.Po
depbase=`echo cmdline.o | sed 's|[^/]*$|.deps/&|;s|\.o$||'`;\
ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT cmdline.o -MD -MP -MF $depbase.Tpo -c -o cmdline.o cmdline.c &&\
mv -f $depbase.Tpo $depbase.Po
/bin/bash ../libtool  --tag=CC   --mode=link ccache_cc -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error   -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/lib -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/lib -znow -zrelro  -o chilli_opt main-opt.o  cmdline.o libchilli.la  ../bstring/libbstring.la         -lrt -lresolv 
OpenWrt-libtool: link: ccache_cc -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z -Wl,now -Wl,-z -Wl,relro -DPIC -fpic -Wno-error -znow -zrelro -o .libs/chilli_opt main-opt.o cmdline.o  -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/lib -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/lib ./.libs/libchilli.so /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/bstring/.libs/libbstring.so ../bstring/.libs/libbstring.so -lrt -lresolv
depbase=`echo main-query.o | sed 's|[^/]*$|.deps/&|;s|\.o$||'`;\
ccache_cc -DHAVE_CONFIG_H -I. -I.. -I../json   -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error  -MT main-query.o -MD -MP -MF $depbase.Tpo -c -o main-query.o main-query.c &&\
mv -f $depbase.Tpo $depbase.Po
/bin/bash ../libtool  --tag=CC   --mode=link ccache_cc -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF='"/etc/chilli.conf"' -DDEFPIDFILE='"/var/run/chilli.pid"' -DDEFSTATEDIR='"/var/run"' -DSBINDIR='"/usr/sbin"'    -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error   -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/lib -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/lib -znow -zrelro  -o chilli_query main-query.o libchilli.la  ../bstring/libbstring.la         -lrt -lresolv 
OpenWrt-libtool: link: ccache_cc -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z -Wl,now -Wl,-z -Wl,relro -DPIC -fpic -Wno-error -znow -zrelro -o .libs/chilli_query main-query.o  -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/lib -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/lib ./.libs/libchilli.so /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/bstring/.libs/libbstring.so ../bstring/.libs/libbstring.so -lrt -lresolv
make[7]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/src'
make[6]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/src'
Making all in doc
make[6]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/doc'
rm -f chilli.8 chilli.8.tmp
sed -e 's,@SBINDIR\@,/usr/sbin,g' -e 's,@INITDIR\@,/etc/init.d,g' -e 's,@VARRUN\@,/var/run,g' -e 's,@ETCCHILLI\@,/etc/chilli,g' -e 's,@SYSCONFDIR\@,/etc,g' -e 's,@PREFIX\@,/usr,g' chilli.8.in >chilli.8.tmp
mv chilli.8.tmp chilli.8
rm -f chilli.conf.5 chilli.conf.5.tmp
sed -e 's,@SBINDIR\@,/usr/sbin,g' -e 's,@INITDIR\@,/etc/init.d,g' -e 's,@VARRUN\@,/var/run,g' -e 's,@ETCCHILLI\@,/etc/chilli,g' -e 's,@SYSCONFDIR\@,/etc,g' -e 's,@PREFIX\@,/usr,g' chilli.conf.5.in >chilli.conf.5.tmp
mv chilli.conf.5.tmp chilli.conf.5
rm -f chilli_query.1 chilli_query.1.tmp
sed -e 's,@SBINDIR\@,/usr/sbin,g' -e 's,@INITDIR\@,/etc/init.d,g' -e 's,@VARRUN\@,/var/run,g' -e 's,@ETCCHILLI\@,/etc/chilli,g' -e 's,@SYSCONFDIR\@,/etc,g' -e 's,@PREFIX\@,/usr,g' chilli_query.1.in >chilli_query.1.tmp
mv chilli_query.1.tmp chilli_query.1
rm -f chilli_response.1 chilli_response.1.tmp
sed -e 's,@SBINDIR\@,/usr/sbin,g' -e 's,@INITDIR\@,/etc/init.d,g' -e 's,@VARRUN\@,/var/run,g' -e 's,@ETCCHILLI\@,/etc/chilli,g' -e 's,@SYSCONFDIR\@,/etc,g' -e 's,@PREFIX\@,/usr,g' chilli_response.1.in >chilli_response.1.tmp
mv chilli_response.1.tmp chilli_response.1
rm -f chilli_radconfig.1 chilli_radconfig.1.tmp
sed -e 's,@SBINDIR\@,/usr/sbin,g' -e 's,@INITDIR\@,/etc/init.d,g' -e 's,@VARRUN\@,/var/run,g' -e 's,@ETCCHILLI\@,/etc/chilli,g' -e 's,@SYSCONFDIR\@,/etc,g' -e 's,@PREFIX\@,/usr,g' chilli_radconfig.1.in >chilli_radconfig.1.tmp
mv chilli_radconfig.1.tmp chilli_radconfig.1
rm -f chilli-radius.5 chilli-radius.5.tmp
sed -e 's,@SBINDIR\@,/usr/sbin,g' -e 's,@INITDIR\@,/etc/init.d,g' -e 's,@VARRUN\@,/var/run,g' -e 's,@ETCCHILLI\@,/etc/chilli,g' -e 's,@SYSCONFDIR\@,/etc,g' -e 's,@PREFIX\@,/usr,g' chilli-radius.5.in >chilli-radius.5.tmp
perl fmttxt.pl chilli-radius < attributes > chilli-radius.5
rm -f chilli-radius.5.tmp
rm -f chilli_opt.1 chilli_opt.1.tmp
sed -e 's,@SBINDIR\@,/usr/sbin,g' -e 's,@INITDIR\@,/etc/init.d,g' -e 's,@VARRUN\@,/var/run,g' -e 's,@ETCCHILLI\@,/etc/chilli,g' -e 's,@SYSCONFDIR\@,/etc,g' -e 's,@PREFIX\@,/usr,g' chilli_opt.1.in >chilli_opt.1.tmp
mv chilli_opt.1.tmp chilli_opt.1
rm -f chilli_rtmon.1 chilli_rtmon.1.tmp
sed -e 's,@SBINDIR\@,/usr/sbin,g' -e 's,@INITDIR\@,/etc/init.d,g' -e 's,@VARRUN\@,/var/run,g' -e 's,@ETCCHILLI\@,/etc/chilli,g' -e 's,@SYSCONFDIR\@,/etc,g' -e 's,@PREFIX\@,/usr,g' chilli_rtmon.1.in >chilli_rtmon.1.tmp
mv chilli_rtmon.1.tmp chilli_rtmon.1
rm -f chilli_redir.1 chilli_redir.1.tmp
sed -e 's,@SBINDIR\@,/usr/sbin,g' -e 's,@INITDIR\@,/etc/init.d,g' -e 's,@VARRUN\@,/var/run,g' -e 's,@ETCCHILLI\@,/etc/chilli,g' -e 's,@SYSCONFDIR\@,/etc,g' -e 's,@PREFIX\@,/usr,g' chilli_redir.1.in >chilli_redir.1.tmp
mv chilli_redir.1.tmp chilli_redir.1
rm -f chilli_proxy.1 chilli_proxy.1.tmp
sed -e 's,@SBINDIR\@,/usr/sbin,g' -e 's,@INITDIR\@,/etc/init.d,g' -e 's,@VARRUN\@,/var/run,g' -e 's,@ETCCHILLI\@,/etc/chilli,g' -e 's,@SYSCONFDIR\@,/etc,g' -e 's,@PREFIX\@,/usr,g' chilli_proxy.1.in >chilli_proxy.1.tmp
mv chilli_proxy.1.tmp chilli_proxy.1
rm -f chilli_radsec.1 chilli_radsec.1.tmp
sed -e 's,@SBINDIR\@,/usr/sbin,g' -e 's,@INITDIR\@,/etc/init.d,g' -e 's,@VARRUN\@,/var/run,g' -e 's,@ETCCHILLI\@,/etc/chilli,g' -e 's,@SYSCONFDIR\@,/etc,g' -e 's,@PREFIX\@,/usr,g' chilli_radsec.1.in >chilli_radsec.1.tmp
mv chilli_radsec.1.tmp chilli_radsec.1
rm -f chilli_script.1 chilli_script.1.tmp
sed -e 's,@SBINDIR\@,/usr/sbin,g' -e 's,@INITDIR\@,/etc/init.d,g' -e 's,@VARRUN\@,/var/run,g' -e 's,@ETCCHILLI\@,/etc/chilli,g' -e 's,@SYSCONFDIR\@,/etc,g' -e 's,@PREFIX\@,/usr,g' chilli_script.1.in >chilli_script.1.tmp
mv chilli_script.1.tmp chilli_script.1
make[6]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/doc'
Making all in www
make[6]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/www'
rm -f config.sh config.sh.tmp
sed -e 's,@SBINDIR\@,/usr/sbin,g' -e 's,@INITDIR\@,/etc/init.d,g' -e 's,@VARRUN\@,/var/run,g' -e 's,@ETCCHILLI\@,/etc/chilli,g' -e 's,@SYSCONFDIR\@,/etc,g' -e 's,@PREFIX\@,/usr,g' config.sh.in >config.sh.tmp
mv config.sh.tmp config.sh
make[6]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/www'
Making all in conf
make[6]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/conf'
rm -f functions functions.tmp
sed -e 's,@ETCDIR\@,/etc,g' -e 's,@SBINDIR\@,/usr/sbin,g' -e 's,@INITDIR\@,,g' -e 's,@VARTMP\@,/var/tmp,g' -e 's,@VARRUN\@,/var/run,g' -e 's,@ETCCHILLI\@,/etc/chilli,g' -e 's,@SYSCONFDIR\@,/etc,g' -e 's,@PREFIX\@,/usr,g' functions.in >functions.tmp
mv functions.tmp functions
rm -f up.sh up.sh.tmp
sed -e 's,@ETCDIR\@,/etc,g' -e 's,@SBINDIR\@,/usr/sbin,g' -e 's,@INITDIR\@,,g' -e 's,@VARTMP\@,/var/tmp,g' -e 's,@VARRUN\@,/var/run,g' -e 's,@ETCCHILLI\@,/etc/chilli,g' -e 's,@SYSCONFDIR\@,/etc,g' -e 's,@PREFIX\@,/usr,g' up.sh.in >up.sh.tmp
chmod +x up.sh.tmp
mv up.sh.tmp up.sh
rm -f down.sh down.sh.tmp
sed -e 's,@ETCDIR\@,/etc,g' -e 's,@SBINDIR\@,/usr/sbin,g' -e 's,@INITDIR\@,,g' -e 's,@VARTMP\@,/var/tmp,g' -e 's,@VARRUN\@,/var/run,g' -e 's,@ETCCHILLI\@,/etc/chilli,g' -e 's,@SYSCONFDIR\@,/etc,g' -e 's,@PREFIX\@,/usr,g' down.sh.in >down.sh.tmp
chmod +x down.sh.tmp
mv down.sh.tmp down.sh
rm -f newmulti.sh newmulti.sh.tmp
sed -e 's,@ETCDIR\@,/etc,g' -e 's,@SBINDIR\@,/usr/sbin,g' -e 's,@INITDIR\@,,g' -e 's,@VARTMP\@,/var/tmp,g' -e 's,@VARRUN\@,/var/run,g' -e 's,@ETCCHILLI\@,/etc/chilli,g' -e 's,@SYSCONFDIR\@,/etc,g' -e 's,@PREFIX\@,/usr,g' newmulti.sh.in >newmulti.sh.tmp
chmod +x newmulti.sh.tmp
mv newmulti.sh.tmp newmulti.sh
rm -f wpad.dat wpad.dat.tmp
sed -e 's,@ETCDIR\@,/etc,g' -e 's,@SBINDIR\@,/usr/sbin,g' -e 's,@INITDIR\@,,g' -e 's,@VARTMP\@,/var/tmp,g' -e 's,@VARRUN\@,/var/run,g' -e 's,@ETCCHILLI\@,/etc/chilli,g' -e 's,@SYSCONFDIR\@,/etc,g' -e 's,@PREFIX\@,/usr,g' wpad.dat.in >wpad.dat.tmp
mv wpad.dat.tmp wpad.dat
chmod a+x wpad.dat
rm -f chilli chilli.tmp
sed -e 's,@ETCDIR\@,/etc,g' -e 's,@SBINDIR\@,/usr/sbin,g' -e 's,@INITDIR\@,,g' -e 's,@VARTMP\@,/var/tmp,g' -e 's,@VARRUN\@,/var/run,g' -e 's,@ETCCHILLI\@,/etc/chilli,g' -e 's,@SYSCONFDIR\@,/etc,g' -e 's,@PREFIX\@,/usr,g' chilli.in >chilli.tmp
chmod +x chilli.tmp
mv chilli.tmp chilli
rm -f CoovaChilliLib.py CoovaChilliLib.py.tmp
sed -e 's,@ETCDIR\@,/etc,g' -e 's,@SBINDIR\@,/usr/sbin,g' -e 's,@INITDIR\@,,g' -e 's,@VARTMP\@,/var/tmp,g' -e 's,@VARRUN\@,/var/run,g' -e 's,@ETCCHILLI\@,/etc/chilli,g' -e 's,@SYSCONFDIR\@,/etc,g' -e 's,@PREFIX\@,/usr,g' CoovaChilliLib.py.in >CoovaChilliLib.py.tmp
mv CoovaChilliLib.py.tmp CoovaChilliLib.py
rm -f defaults defaults.tmp
sed -e 's,@ETCDIR\@,/etc,g' -e 's,@SBINDIR\@,/usr/sbin,g' -e 's,@INITDIR\@,,g' -e 's,@VARTMP\@,/var/tmp,g' -e 's,@VARRUN\@,/var/run,g' -e 's,@ETCCHILLI\@,/etc/chilli,g' -e 's,@SYSCONFDIR\@,/etc,g' -e 's,@PREFIX\@,/usr,g' defaults.in >defaults.tmp
mv defaults.tmp defaults
rm -f chilli.conf chilli.conf.tmp
sed -e 's,@ETCDIR\@,/etc,g' -e 's,@SBINDIR\@,/usr/sbin,g' -e 's,@INITDIR\@,,g' -e 's,@VARTMP\@,/var/tmp,g' -e 's,@VARRUN\@,/var/run,g' -e 's,@ETCCHILLI\@,/etc/chilli,g' -e 's,@SYSCONFDIR\@,/etc,g' -e 's,@PREFIX\@,/usr,g' chilli.conf.in >chilli.conf.tmp
mv chilli.conf.tmp chilli.conf
make[6]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/conf'
make[6]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6'
make[6]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6'
make[5]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6'
make[4]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6'
make[4]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6'
Making install in bstring
make[5]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/bstring'
make[6]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/bstring'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/lib'
 /bin/bash ../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libbstring.la '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libbstring.so.0.0.0 /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/lib/libbstring.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/lib && { ln -s -f libbstring.so.0.0.0 libbstring.so.0 || { rm -f libbstring.so.0 && ln -s libbstring.so.0.0.0 libbstring.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/lib && { ln -s -f libbstring.so.0.0.0 libbstring.so || { rm -f libbstring.so && ln -s libbstring.so.0.0.0 libbstring.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libbstring.lai /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/lib/libbstring.la
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libbstring.a /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/lib/libbstring.a
OpenWrt-libtool: install: chmod 644 /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/lib/libbstring.a
OpenWrt-libtool: install: arm-openwrt-linux-muslgnueabi-gcc-ranlib /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/lib/libbstring.a
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
make[6]: Nothing to be done for 'install-data-am'.
make[6]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/bstring'
make[5]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/bstring'
Making install in src
make[5]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/src'
Making install in linux
make[6]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/src/linux'
make -C /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/linux-5.4.124 M=$PWD modules_install;
make[7]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/linux-5.4.124'
  INSTALL /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/src/linux/xt_coova.ko
  DEPMOD  5.4.124
Warning: modules_install: missing 'System.map' file. Skipping depmod.
make[7]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/linux-5.4.124'
mkdir -p /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/lib/iptables/
cp libxt_coova.so /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/lib/iptables/
make[6]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/src/linux'
make[6]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/src'
make[7]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/src'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/lib'
 /bin/bash ../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libchilli.la '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libchilli.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/src; /bin/bash /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/libtool  --tag CC --mode=relink ccache_cc -D_GNU_SOURCE -Wall -fno-builtin -fno-strict-aliasing -fomit-frame-pointer -funroll-loops -pipe -I../bstring -DDEFCHILLICONF=\"/etc/chilli.conf\" -DDEFPIDFILE=\"/var/run/chilli.pid\" -DDEFSTATEDIR=\"/var/run\" -DSBINDIR=\"/usr/sbin\" -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6=coova-chilli-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -Wno-error -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/lib -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/lib -znow -zrelro -o libchilli.la -rpath /usr/lib chilli.lo tun.lo ippool.lo radius.lo md5.lo redir.lo dhcp.lo iphash.lo lookup.lo util.lo options.lo statusfile.lo conn.lo sig.lo garden.lo dns.lo session.lo pkt.lo chksum.lo net.lo safe.lo sfhash.lo cmdsock.lo kcoova.lo ../bstring/libbstring.la -lrt -lresolv -inst-prefix-dir /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install)
OpenWrt-libtool: relink: ccache_cc -shared  -fPIC -DPIC  .libs/chilli.o .libs/tun.o .libs/ippool.o .libs/radius.o .libs/md5.o .libs/redir.o .libs/dhcp.o .libs/iphash.o .libs/lookup.o .libs/util.o .libs/options.o .libs/statusfile.o .libs/conn.o .libs/sig.o .libs/garden.o .libs/dns.o .libs/session.o .libs/pkt.o .libs/chksum.o .libs/net.o .libs/safe.o .libs/sfhash.o .libs/cmdsock.o .libs/kcoova.o   -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/lib -L/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/lib -L/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/lib -lbstring -lrt -lresolv  -Os -mfloat-abi=hard -fstack-protector -Wl,-z -Wl,now -Wl,-z -Wl,relro   -Wl,-soname -Wl,libchilli.so.0 -o .libs/libchilli.so.0.0.0
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libchilli.so.0.0.0T /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/lib/libchilli.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/lib && { ln -s -f libchilli.so.0.0.0 libchilli.so.0 || { rm -f libchilli.so.0 && ln -s libchilli.so.0.0.0 libchilli.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/lib && { ln -s -f libchilli.so.0.0.0 libchilli.so || { rm -f libchilli.so && ln -s libchilli.so.0.0.0 libchilli.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libchilli.lai /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/lib/libchilli.la
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libchilli.a /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/lib/libchilli.a
OpenWrt-libtool: install: chmod 644 /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/lib/libchilli.a
OpenWrt-libtool: install: arm-openwrt-linux-muslgnueabi-gcc-ranlib /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/lib/libchilli.a
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/sbin'
  /bin/bash ../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c chilli chilli_response chilli_radconfig chilli_opt chilli_query '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/sbin'
OpenWrt-libtool: install: warning: `libchilli.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/bstring/libbstring.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../bstring/libbstring.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/chilli /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/sbin/chilli
OpenWrt-libtool: install: warning: `libchilli.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/bstring/libbstring.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../bstring/libbstring.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/chilli_response /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/sbin/chilli_response
OpenWrt-libtool: install: warning: `libchilli.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/bstring/libbstring.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../bstring/libbstring.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/chilli_radconfig /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/sbin/chilli_radconfig
OpenWrt-libtool: install: warning: `libchilli.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/bstring/libbstring.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../bstring/libbstring.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/chilli_opt /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/sbin/chilli_opt
OpenWrt-libtool: install: warning: `libchilli.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/bstring/libbstring.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../bstring/libbstring.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/chilli_query /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/sbin/chilli_query
make  install-exec-hook
make[8]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/src'
make[8]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/src'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/include/chilli'
 /openwrt/staging_dir/host/bin/install -c -m 644 chilli.h session.h garden.h radius.h options.h tun.h ippool.h md5.h redir.h dhcp.h iphash.h radius_wispr.h radius_coovachilli.h ssl.h dns.h net.h pkt.h conn.h lookup.h chilli_limits.h cmdline.h debug.h radius_pkt.h ../bstring/bstrlib.h ../config.h system.h cmdsock.h '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/include/chilli'
make[7]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/src'
make[6]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/src'
make[5]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/src'
Making install in doc
make[5]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/doc'
make[6]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/doc'
make[6]: Nothing to be done for 'install-exec-am'.
 /usr/bin/mkdir -p '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/man/man1'
 /openwrt/staging_dir/host/bin/install -c -m 644 chilli_query.1 chilli_response.1 chilli_radconfig.1 chilli_opt.1 chilli_rtmon.1 chilli_redir.1 chilli_proxy.1 chilli_radsec.1 chilli_script.1 '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/man/man1'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/man/man5'
 /openwrt/staging_dir/host/bin/install -c -m 644 chilli.conf.5 chilli-radius.5 '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/man/man5'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/man/man8'
 /openwrt/staging_dir/host/bin/install -c -m 644 chilli.8 '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/man/man8'
make[6]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/doc'
make[5]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/doc'
Making install in www
make[5]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/www'
make[6]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/www'
make[6]: Nothing to be done for 'install-exec-am'.
 /usr/bin/mkdir -p '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/etc/chilli'
 /openwrt/staging_dir/host/bin/install -c wwwsh '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/etc/chilli'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/etc/chilli/www'
 /openwrt/staging_dir/host/bin/install -c -m 644 chillijs.chi chillijs.chi.sh chilliform.chi chilliform.chi.sh coova.html coova.jpg coova.png wait.gif openid.gif ChilliLibrary.js chilliController.js json_html.tmpl config.sh '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/etc/chilli/www'
make[6]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/www'
make[5]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/www'
Making install in conf
make[5]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/conf'
make[6]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/conf'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/etc'
 /openwrt/staging_dir/host/bin/install -c -m 644 chilli.conf '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/etc'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/etc/chilli'
 /openwrt/staging_dir/host/bin/install -c -m 644 defaults gui-config-default.ini '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/etc/chilli'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/etc/chilli'
 /openwrt/staging_dir/host/bin/install -c functions up.sh down.sh newmulti.sh wpad.dat '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/etc/chilli'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/etc/init.d'
 /openwrt/staging_dir/host/bin/install -c chilli '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/etc/init.d'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/lib/python'
 /openwrt/staging_dir/host/bin/install -c CoovaChilliLib.py '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-install/usr/lib/python'
make[6]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/conf'
make[5]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/conf'
make[5]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6'
make[6]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6'
make[6]: Nothing to be done for 'install-exec-am'.
make[6]: Nothing to be done for 'install-data-am'.
make[6]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6'
make[5]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6'
make[4]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6'
rstrip.sh: /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-arm_cortex-a7_neon-vfpv4/coova-chilli/usr/sbin/chilli_opt: executable
rstrip.sh: /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-arm_cortex-a7_neon-vfpv4/coova-chilli/usr/sbin/chilli_response: executable
rstrip.sh: /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-arm_cortex-a7_neon-vfpv4/coova-chilli/usr/sbin/chilli_query: executable
rstrip.sh: /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-arm_cortex-a7_neon-vfpv4/coova-chilli/usr/sbin/chilli_radconfig: executable
rstrip.sh: /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-arm_cortex-a7_neon-vfpv4/coova-chilli/usr/sbin/chilli: executable
rstrip.sh: /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-arm_cortex-a7_neon-vfpv4/coova-chilli/usr/lib/libbstring.so.0.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-arm_cortex-a7_neon-vfpv4/coova-chilli/usr/lib/iptables/libxt_coova.so: shared object
rstrip.sh: /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-arm_cortex-a7_neon-vfpv4/coova-chilli/usr/lib/libchilli.so.0.0.0: shared object
Packaged contents of /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/coova-chilli-1.6/ipkg-arm_cortex-a7_neon-vfpv4/coova-chilli into /openwrt/bin/packages/arm_cortex-a7_neon-vfpv4/packages/coova-chilli_1.6-1_arm_cortex-a7_neon-vfpv4.ipk
Package kmod-ipt-coova is missing dependencies for the following libraries:
x_tables.ko
make[3]: *** [Makefile:162: /openwrt/bin/targets/ipq40xx/generic/packages/kmod-ipt-coova_5.4.124+1.6-1_arm_cortex-a7_neon-vfpv4.ipk] Error 1
```
