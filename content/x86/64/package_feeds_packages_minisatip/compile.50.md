---
title: "compile.50"
date: 2021-02-25 14:20:49.082534
hidden: false
draft: false
weight: -50
---

build number: `50`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/minisatip/compile -j$(nproc) || make package/feeds/packages/minisatip/compile V=s
```

#### Compile.txt

``` bash
configure: WARNING: unrecognized options: --disable-nls
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
checking for main in -lrt... yes
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
checking for stdint.h... (cached) yes
checking for stdlib.h... (cached) yes
checking for string.h... (cached) yes
checking sys/ioctl.h usability... yes
checking sys/ioctl.h presence... yes
checking for sys/ioctl.h... yes
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking sys/time.h usability... yes
checking sys/time.h presence... yes
checking for sys/time.h... yes
checking syslog.h usability... yes
checking syslog.h presence... yes
checking for syslog.h... yes
checking for unistd.h... (cached) yes
checking for int16_t... yes
checking for int64_t... yes
checking for int8_t... yes
checking for size_t... yes
checking for uint16_t... yes
checking for uint32_t... yes
checking for uint64_t... yes
checking for uint8_t... yes
checking for stdlib.h... (cached) yes
checking for GNU libc compatible malloc... (cached) yes
checking for stdlib.h... (cached) yes
checking for unistd.h... (cached) yes
checking for sys/param.h... yes
checking for getpagesize... yes
checking for working mmap... no
checking for bzero... (cached) yes
checking for clock_gettime... yes
checking for dup2... yes
checking for gethostbyname... yes
checking for gettimeofday... (cached) yes
checking for inet_ntoa... yes
checking for memset... yes
checking for munmap... yes
checking for socket... yes
checking for strchr... yes
checking for strerror... (cached) yes
checking for strncasecmp... yes
checking for strstr... yes
configure:  == Checking LINUX DVB == 
checking linux/dvb/frontend.h usability... yes
checking linux/dvb/frontend.h presence... yes
checking for linux/dvb/frontend.h... yes
configure:  == Checking DVBEN50221 == 
checking libdvben50221/en50221_app_dvb.h usability... no
checking libdvben50221/en50221_app_dvb.h presence... no
checking for libdvben50221/en50221_app_dvb.h... no
configure:  == Checking Embedded == 
checking for backtrace... no
configure:  == Checking DVBCSA == 
checking dvbcsa/dvbcsa.h usability... yes
checking dvbcsa/dvbcsa.h presence... yes
checking for dvbcsa/dvbcsa.h... yes
configure:  == Checking NETCVCLIENT == 
checking netceiver.h usability... cat: confdefs.h: No such file or directory
no
checking netceiver.h presence... cat: confdefs.h: No such file or directory
no
checking for netceiver.h... no
configure: creating ./config.status
config.status: creating src/Makefile
config.status: creating tests/Makefile
config.status: creating Makefile
configure: WARNING: unrecognized options: --disable-nls

minisatip configuration


Linux DVB:				  enabled
Common Interface (needs DVBEN50221):	  disabled
OpenSSL (AES as part of DVBAPI):	  disabled
Embedded system:			  enabled
DVBCSA (needs libdvbcsa):		  enabled
Netceiver support:			  disabled
SatIP Client:				  enabled
Static:					  disabled
dvbapi:					  enabled
axe:					  disabled
enigma:					  disabled

make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/minisatip-1.0.4'
make -C src
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/minisatip-1.0.4/src'
ccache_cc -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/minisatip-1.0.4=minisatip-1.0.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include    -DDISABLE_DVBAES -DDISABLE_DVBCA -DDISABLE_NETCVCLIENT -DDISABLE_DDCI -DDISABLE_T2MI -DNO_BACKTRACE -c minisatip.c -o ../build/minisatip.o
ccache_cc -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/minisatip-1.0.4=minisatip-1.0.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include    -DDISABLE_DVBAES -DDISABLE_DVBCA -DDISABLE_NETCVCLIENT -DDISABLE_DDCI -DDISABLE_T2MI -DNO_BACKTRACE -c socketworks.c -o ../build/socketworks.o
ccache_cc -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/minisatip-1.0.4=minisatip-1.0.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include    -DDISABLE_DVBAES -DDISABLE_DVBCA -DDISABLE_NETCVCLIENT -DDISABLE_DDCI -DDISABLE_T2MI -DNO_BACKTRACE -c stream.c -o ../build/stream.o
ccache_cc -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/minisatip-1.0.4=minisatip-1.0.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include    -DDISABLE_DVBAES -DDISABLE_DVBCA -DDISABLE_NETCVCLIENT -DDISABLE_DDCI -DDISABLE_T2MI -DNO_BACKTRACE -c adapter.c -o ../build/adapter.o
ccache_cc -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/minisatip-1.0.4=minisatip-1.0.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include    -DDISABLE_DVBAES -DDISABLE_DVBCA -DDISABLE_NETCVCLIENT -DDISABLE_DDCI -DDISABLE_T2MI -DNO_BACKTRACE -c utils.c -o ../build/utils.o
ccache_cc -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/minisatip-1.0.4=minisatip-1.0.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include    -DDISABLE_DVBAES -DDISABLE_DVBCA -DDISABLE_NETCVCLIENT -DDISABLE_DDCI -DDISABLE_T2MI -DNO_BACKTRACE -c csa.c -o ../build/csa.o
ccache_cc -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/minisatip-1.0.4=minisatip-1.0.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include    -DDISABLE_DVBAES -DDISABLE_DVBCA -DDISABLE_NETCVCLIENT -DDISABLE_DDCI -DDISABLE_T2MI -DNO_BACKTRACE -c dvbapi.c -o ../build/dvbapi.o
ccache_cc -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/minisatip-1.0.4=minisatip-1.0.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include    -DDISABLE_DVBAES -DDISABLE_DVBCA -DDISABLE_NETCVCLIENT -DDISABLE_DDCI -DDISABLE_T2MI -DNO_BACKTRACE -c pmt.c -o ../build/pmt.o
ccache_cc -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/minisatip-1.0.4=minisatip-1.0.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include    -DDISABLE_DVBAES -DDISABLE_DVBCA -DDISABLE_NETCVCLIENT -DDISABLE_DDCI -DDISABLE_T2MI -DNO_BACKTRACE -c tables.c -o ../build/tables.o
ccache_cc -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/minisatip-1.0.4=minisatip-1.0.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include    -DDISABLE_DVBAES -DDISABLE_DVBCA -DDISABLE_NETCVCLIENT -DDISABLE_DDCI -DDISABLE_T2MI -DNO_BACKTRACE -c satipc.c -o ../build/satipc.o
ccache_cc -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/minisatip-1.0.4=minisatip-1.0.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include    -DDISABLE_DVBAES -DDISABLE_DVBCA -DDISABLE_NETCVCLIENT -DDISABLE_DDCI -DDISABLE_T2MI -DNO_BACKTRACE -c dvb.c -o ../build/dvb.o
ccache_cc -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/minisatip-1.0.4=minisatip-1.0.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include    -DDISABLE_DVBAES -DDISABLE_DVBCA -DDISABLE_NETCVCLIENT -DDISABLE_DDCI -DDISABLE_T2MI -DNO_BACKTRACE -o ../minisatip  ../build/minisatip.o  ../build/socketworks.o  ../build/stream.o  ../build/adapter.o  ../build/utils.o  ../build/csa.o  ../build/dvbapi.o  ../build/pmt.o  ../build/tables.o  ../build/satipc.o  ../build/dvb.o -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  -lpthread -lrt -ldvbcsa 
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/minisatip-1.0.4/src'
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/minisatip-1.0.4'
Package minisatip is missing dependencies for the following libraries:
libdvbcsa.so.1
make[3]: *** [Makefile:75: /openwrt/bin/packages/x86_64/packages/minisatip_1.0.4-1_x86_64.ipk] Error 1
```
