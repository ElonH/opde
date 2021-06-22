---
title: "compile.40"
date: 2021-06-22 10:41:19.982137
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
make package/feeds/packages/netstinky/compile -j$(nproc) || make package/feeds/packages/netstinky/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-openssl-deprecated.patch using plaintext: 
patching file updates/ids_tls_update.c
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/mips
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
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports the include directive... yes (GNU style)
checking whether make supports nested variables... yes
checking dependency style of ccache_cc... gcc3
checking for mips-openwrt-linux-ar... mips-openwrt-linux-musl-gcc-ar
checking the archiver (mips-openwrt-linux-musl-gcc-ar) interface... ar
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
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
checking for shl_load... no
checking for shl_load in -ldld... no
checking for dlopen... yes
checking whether a program can dlopen itself... cross
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... yes
checking pkg-config is at least version 0.9.0... yes
checking for mips-openwrt-linux-gcc... (cached) ccache_cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether ccache_cc accepts -g... (cached) yes
checking for ccache_cc option to accept ISO C89... (cached) none needed
checking whether ccache_cc understands -c and -o together... (cached) yes
checking how to run the C preprocessor... ccache_cc -E
checking whether ln -s works... yes
checking whether make sets $(MAKE)... (cached) yes
checking for stdbool.h that conforms to C99... yes
checking for _Bool... yes
checking for inline... inline
checking for int16_t... yes
checking for int32_t... yes
checking for int64_t... yes
checking for int8_t... yes
checking for C/C++ restrict keyword... __restrict
checking for size_t... yes
checking for ssize_t... yes
checking for uint16_t... yes
checking for uint32_t... yes
checking for uint64_t... yes
checking for uint8_t... yes
checking for ptrdiff_t... yes
checking whether byte ordering is bigendian... (cached) yes
checking whether to enable assertions... yes
checking for ANSI C header files... (cached) yes
checking for stdbool.h that conforms to C99... (cached) yes
checking for _Bool... (cached) yes
checking whether time.h and sys/time.h may both be included... yes
checking for stdlib.h... (cached) yes
checking for GNU libc compatible malloc... (cached) yes
checking for sys/time.h... yes
checking for unistd.h... (cached) yes
checking for alarm... yes
checking for working mktime... no
checking for stdlib.h... (cached) yes
checking for GNU libc compatible realloc... (cached) yes
checking for working strnlen... yes
checking for sys/types.h... (cached) yes
checking arpa/inet.h usability... yes
checking arpa/inet.h presence... yes
checking for arpa/inet.h... yes
checking errno.h usability... yes
checking errno.h presence... yes
checking for errno.h... yes
checking getopt.h usability... yes
checking getopt.h presence... yes
checking for getopt.h... yes
checking limits.h usability... yes
checking limits.h presence... yes
checking for limits.h... yes
checking math.h usability... yes
checking math.h presence... yes
checking for math.h... yes
checking net/ethernet.h usability... yes
checking net/ethernet.h presence... yes
checking for net/ethernet.h... yes
checking for netinet/in.h... yes
checking for netinet/ip.h... yes
checking netinet/udp.h usability... yes
checking netinet/udp.h presence... yes
checking for netinet/udp.h... yes
checking poll.h usability... yes
checking poll.h presence... yes
checking for poll.h... yes
checking signal.h usability... yes
checking signal.h presence... yes
checking for signal.h... yes
checking stddef.h usability... yes
checking stddef.h presence... yes
checking for stddef.h... yes
checking for stdint.h... (cached) yes
checking for stdlib.h... (cached) yes
checking stdio.h usability... yes
checking stdio.h presence... yes
checking for stdio.h... yes
checking for string.h... (cached) yes
checking for strings.h... (cached) yes
checking sys/param.h usability... yes
checking sys/param.h presence... yes
checking for sys/param.h... yes
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking for sys/time.h... (cached) yes
checking for unistd.h... (cached) yes
checking wchar.h usability... yes
checking wchar.h presence... yes
checking for wchar.h... yes
checking endian.h usability... yes
checking endian.h presence... yes
checking for endian.h... yes
checking uv.h usability... yes
checking uv.h presence... yes
checking for uv.h... yes
checking for library containing uv_default_loop... -luv
checking pcap/pcap.h usability... yes
checking pcap/pcap.h presence... yes
checking for pcap/pcap.h... yes
checking for library containing pcap_create... -lpcap
checking whether OSSwapHostToBigInt32 is declared... no
checking whether OSSwapBigToHostInt32 is declared... no
checking whether OSSwapHostToBigInt64 is declared... no
checking whether OSSwapBigToHostInt64 is declared... no
checking for clock_gettime... yes
checking for gettimeofday... (cached) yes
checking for inet_ntoa... yes
checking for memcpy... yes
checking for memmove... yes
checking for memset... yes
checking for strcasecmp... yes
checking for strdup... yes
checking for strstr... yes
checking for strtol... yes
checking for strtoul... yes
checking for mips-openwrt-linux-pkg-config... /openwrt/staging_dir/host/bin/pkg-config
checking for include/openssl/ssl.h in /usr/local/ssl... no
checking for include/openssl/ssl.h in /usr/lib/ssl... no
checking for include/openssl/ssl.h in /usr/ssl... no
checking for include/openssl/ssl.h in /usr/pkg... no
checking for include/openssl/ssl.h in /usr/local... no
checking for include/openssl/ssl.h in /usr... yes
checking whether compiling and linking against OpenSSL works... no
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating Makefile
config.status: creating config.h
config.status: executing depfiles commands
config.status: executing libtool commands
configure: WARNING: unrecognized options: --disable-nls
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/nsids-1.0.0'
make  all-am
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/nsids-1.0.0'
ccache_cc -DHAVE_CONFIG_H -I.   -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include   -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/nsids-1.0.0=nsids-1.0.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -MT utils/nsids-byte_array.o -MD -MP -MF utils/.deps/nsids-byte_array.Tpo -c -o utils/nsids-byte_array.o `test -f 'utils/byte_array.c' || echo './'`utils/byte_array.c
mv -f utils/.deps/nsids-byte_array.Tpo utils/.deps/nsids-byte_array.Po
ccache_cc -DHAVE_CONFIG_H -I.   -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include   -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/nsids-1.0.0=nsids-1.0.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -MT utils/nsids-str.o -MD -MP -MF utils/.deps/nsids-str.Tpo -c -o utils/nsids-str.o `test -f 'utils/str.c' || echo './'`utils/str.c
mv -f utils/.deps/nsids-str.Tpo utils/.deps/nsids-str.Po
ccache_cc -DHAVE_CONFIG_H -I.   -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include   -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/nsids-1.0.0=nsids-1.0.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -MT utils/nsids-linked_list.o -MD -MP -MF utils/.deps/nsids-linked_list.Tpo -c -o utils/nsids-linked_list.o `test -f 'utils/linked_list.c' || echo './'`utils/linked_list.c
mv -f utils/.deps/nsids-linked_list.Tpo utils/.deps/nsids-linked_list.Po
ccache_cc -DHAVE_CONFIG_H -I.   -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include   -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/nsids-1.0.0=nsids-1.0.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -MT utils/nsids-file_processing.o -MD -MP -MF utils/.deps/nsids-file_processing.Tpo -c -o utils/nsids-file_processing.o `test -f 'utils/file_processing.c' || echo './'`utils/file_processing.c
mv -f utils/.deps/nsids-file_processing.Tpo utils/.deps/nsids-file_processing.Po
ccache_cc -DHAVE_CONFIG_H -I.   -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include   -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/nsids-1.0.0=nsids-1.0.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -MT nsids-dns.o -MD -MP -MF .deps/nsids-dns.Tpo -c -o nsids-dns.o `test -f 'dns.c' || echo './'`dns.c
mv -f .deps/nsids-dns.Tpo .deps/nsids-dns.Po
ccache_cc -DHAVE_CONFIG_H -I.   -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include   -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/nsids-1.0.0=nsids-1.0.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -MT nsids-ids_event_list.o -MD -MP -MF .deps/nsids-ids_event_list.Tpo -c -o nsids-ids_event_list.o `test -f 'ids_event_list.c' || echo './'`ids_event_list.c
mv -f .deps/nsids-ids_event_list.Tpo .deps/nsids-ids_event_list.Po
ccache_cc -DHAVE_CONFIG_H -I.   -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include   -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/nsids-1.0.0=nsids-1.0.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -MT nsids-ids_pcap.o -MD -MP -MF .deps/nsids-ids_pcap.Tpo -c -o nsids-ids_pcap.o `test -f 'ids_pcap.c' || echo './'`ids_pcap.c
mv -f .deps/nsids-ids_pcap.Tpo .deps/nsids-ids_pcap.Po
ccache_cc -DHAVE_CONFIG_H -I.   -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include   -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/nsids-1.0.0=nsids-1.0.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -MT nsids-ids_server.o -MD -MP -MF .deps/nsids-ids_server.Tpo -c -o nsids-ids_server.o `test -f 'ids_server.c' || echo './'`ids_server.c
mv -f .deps/nsids-ids_server.Tpo .deps/nsids-ids_server.Po
ccache_cc -DHAVE_CONFIG_H -I.   -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include   -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/nsids-1.0.0=nsids-1.0.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -MT nsids-main.o -MD -MP -MF .deps/nsids-main.Tpo -c -o nsids-main.o `test -f 'main.c' || echo './'`main.c
In file included from updates/ids_tls_update.h:21,
                 from main.c:42:
updates/../utils/uvtls/uv_tls.h:23:10: fatal error: openssl/ssl.h: No such file or directory
 #include <openssl/ssl.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
make[5]: *** [Makefile:1187: nsids-main.o] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/nsids-1.0.0'
make[4]: *** [Makefile:509: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/nsids-1.0.0'
make[3]: *** [Makefile:64: /openwrt/build_dir/target-mips_24kc_musl/nsids-1.0.0/.built] Error 2
```
