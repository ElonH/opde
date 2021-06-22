---
title: "compile.40"
date: 2021-06-22 10:38:26.234808
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
make package/feeds/telephony/sofia-sip/compile -j$(nproc) || make package/feeds/telephony/sofia-sip/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/01-disable-libcheck.patch using plaintext: 
patching file configure.ac

Applying ./patches/02-NUA_handles-mem-leak-fix.patch using plaintext: 
patching file libsofia-sip-ua/nua/nua.c
patching file libsofia-sip-ua/nua/nua_common.c
patching file libsofia-sip-ua/nua/nua_stack.c
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force -I m4
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
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
configure.ac:41: installing './compile'
configure.ac:37: installing './missing'
libsofia-sip-ua-glib/su-glib/Makefile.am: installing './depcomp'
parallel-tests: installing './test-driver'
autoreconf: Leaving directory `.'
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/mips
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking target system type... mips-openwrt-linux-gnu
checking cached information... ok
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking for style of include used by make... GNU
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
checking for compilation environment... 
checking for mips-openwrt-linux-gcc... (cached) ccache_cc
checking for mips-openwrt-linux-gcc... (cached) ccache_cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether ccache_cc accepts -g... (cached) yes
checking for ccache_cc option to accept ISO C89... (cached) none needed
checking whether ccache_cc understands -c and -o together... (cached) yes
checking dependency style of ccache_cc... (cached) gcc3
checking for maximum warnings compiler flag... 
checking how to run the C preprocessor... ccache_cc -E
checking for etags... echo
checking for mips-openwrt-linux-ar... mips-openwrt-linux-musl-gcc-ar
checking for mips-openwrt-linux-ld... mips-openwrt-linux-musl-ld
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache_cc... mips-openwrt-linux-musl-ld
checking if the linker (mips-openwrt-linux-musl-ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... mips-openwrt-linux-musl-gcc-nm
checking the name lister (mips-openwrt-linux-musl-gcc-nm) interface... BSD nm
checking whether ln -s works... yes
checking the maximum length of command line arguments... 3145728
checking whether the shell understands some XSI constructs... yes
checking whether the shell understands "+="... yes
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
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... yes
checking for doxygen... echo
checking for C compiler vendor... gnu
checking for ANSI C header files... (cached) yes
checking return type of signal handlers... void
checking for long long... yes
checking whether IO functions support C99 size specifiers... yes
checking for an ANSI C-conforming const... yes
checking for inline... inline
checking for inline... (cached) inline
checking whether byte ordering is bigendian... (cached) yes
checking whether ccache_cc recognizes __func__... yes
checking whether ccache_cc recognizes __FUNCTION__... yes
checking whether ccache_cc recognizes field names in struct initialization... yes
checking whether time.h and sys/time.h may both be included... yes
checking for size_t... yes
checking for sa_len... no
checking /dev/urandom... yes
checking for sys/types.h... (cached) yes
checking for stdint.h... (cached) yes
checking for inttypes.h... (cached) yes
checking pthread.h usability... yes
checking pthread.h presence... yes
checking for pthread.h... yes
checking for stack suitable for tags... no
checking for graceful free(0)... no
checking for sockaddr_in6... yes
checking for unistd.h... (cached) yes
checking sys/time.h usability... yes
checking sys/time.h presence... yes
checking for sys/time.h... yes
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking dirent.h usability... yes
checking dirent.h presence... yes
checking for dirent.h... yes
checking winsock2.h usability... no
checking winsock2.h presence... no
checking for winsock2.h... no
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking sys/ioctl.h usability... yes
checking sys/ioctl.h presence... yes
checking for sys/ioctl.h... yes
checking sys/filio.h usability... no
checking sys/filio.h presence... no
checking for sys/filio.h... no
checking sys/sockio.h usability... no
checking sys/sockio.h presence... no
checking for sys/sockio.h... no
checking sys/select.h usability... yes
checking sys/select.h presence... yes
checking for sys/select.h... yes
checking sys/epoll.h usability... yes
checking sys/epoll.h presence... yes
checking for sys/epoll.h... yes
checking sys/devpoll.h usability... no
checking sys/devpoll.h presence... no
checking for sys/devpoll.h... no
checking for netinet/in.h... yes
checking for arpa/inet.h... yes
checking for netdb.h... yes
checking for net/if.h... yes
checking for net/if_types.h... no
checking for ifaddr.h... no
checking for netpacket/packet.h... yes
checking whether MSG_TRUNC is declared... yes
checking whether SO_RCVBUFFORCE is declared... yes
checking whether SO_SNDBUFFORCE is declared... yes
checking whether IP_ADD_MEMBERSHIP is declared... yes
checking whether IP_MULTICAST_LOOP is declared... yes
checking whether IP_MTU_DISCOVER is declared... yes
checking for struct addrinfo... yes
checking for struct sockaddr_storage... yes
checking for field ifr_index in struct ifreq... no
checking for field ifr_ifindex in struct ifreq... yes
checking for struct ifconf... yes
checking for ioctl SIOCGIFNUM... sys/sockio.h missing
checking for pthread_create in -lpthread... yes
checking for socketpair in -lsocket... no
checking for library containing clock_gettime... none required
checking for clock_gettime... yes
checking for clock_getcpuclockid... yes
checking whether CLOCK_MONOTONIC is declared... yes
checking for library containing socket... none required
checking for library containing inet_ntop... none required
checking for library containing getipnodebyname... no
checking for library containing gethostbyname... none required
checking for library containing getaddrinfo... none required
checking for working alloca.h... yes
checking for alloca... yes
checking for gettimeofday... (cached) yes
checking for strerror... (cached) yes
checking for random... yes
checking for initstate... yes
checking for tcsetattr... yes
checking for flock... yes
checking for socketpair... yes
checking for gethostname... yes
checking for gethostbyname... yes
checking for getipnodebyname... no
checking for poll... yes
checking for epoll_create... yes
checking for kqueue... no
checking for select... yes
checking for if_nameindex... yes
checking for signal... yes
checking for alarm... yes
checking for strnlen... yes
checking for getaddrinfo... (cached) yes
checking for getnameinfo... yes
checking for freeaddrinfo... yes
checking for gai_strerror... yes
checking for getifaddrs... yes
checking for getline... yes
checking for getdelim... yes
checking for getpass... yes
checking for memmem... yes
checking for memccpy... yes
checking for memspn... no
checking for memcspn... no
checking for strtoull... yes
checking for inet_ntop... yes
checking for inet_pton... yes
checking for poll... (cached) yes
checking whether SIGPIPE is declared... yes
checking for openssl... checking for openssl/tls1.h... no
configure: WARNING: OpenSSL include files were not found
checking for IP_RECVERR... yes
checking for IPV6_RECVERR... yes
checking for netinet/tcp.h... yes
checking for netinet/sctp.h... (cached) no
checking for we_do_not_want_check >= 0.9.4... checking fnmatch.h usability... yes
checking fnmatch.h presence... yes
checking for fnmatch.h... yes
checking for pthread_setschedparam in -lpthread... yes
checking for compress in -lz... yes
checking for dlopen in -ldl... yes
configure: WARNING: ** STUN support disabled **
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating Makefile
config.status: creating packages/Makefile
config.status: creating packages/sofia-sip-ua.pc
config.status: creating packages/sofia-sip-ua-glib.pc
config.status: creating libsofia-sip-ua/Makefile
config.status: creating libsofia-sip-ua/bnf/Makefile
config.status: creating libsofia-sip-ua/bnf/Doxyfile
config.status: creating libsofia-sip-ua/docs/Makefile
config.status: creating libsofia-sip-ua/docs/Doxyfile
config.status: creating libsofia-sip-ua/docs/Doxyfile.version
config.status: creating libsofia-sip-ua/docs/sofia-footer.html
config.status: creating libsofia-sip-ua/features/Doxyfile
config.status: creating libsofia-sip-ua/features/Makefile
config.status: creating libsofia-sip-ua/http/Doxyfile
config.status: creating libsofia-sip-ua/http/Makefile
config.status: creating libsofia-sip-ua/ipt/Doxyfile
config.status: creating libsofia-sip-ua/ipt/Makefile
config.status: creating libsofia-sip-ua/iptsec/Doxyfile
config.status: creating libsofia-sip-ua/iptsec/Makefile
config.status: creating libsofia-sip-ua/msg/Doxyfile
config.status: creating libsofia-sip-ua/msg/Makefile
config.status: creating libsofia-sip-ua/nea/Doxyfile
config.status: creating libsofia-sip-ua/nea/Makefile
config.status: creating libsofia-sip-ua/nta/Doxyfile
config.status: creating libsofia-sip-ua/nta/Makefile
config.status: creating libsofia-sip-ua/nth/Doxyfile
config.status: creating libsofia-sip-ua/nth/Makefile
config.status: creating libsofia-sip-ua/nua/Doxyfile
config.status: creating libsofia-sip-ua/nua/Makefile
config.status: creating libsofia-sip-ua/sdp/Doxyfile
config.status: creating libsofia-sip-ua/sdp/Makefile
config.status: creating libsofia-sip-ua/sip/Doxyfile
config.status: creating libsofia-sip-ua/sip/Makefile
config.status: creating libsofia-sip-ua/soa/Doxyfile
config.status: creating libsofia-sip-ua/soa/Makefile
config.status: creating libsofia-sip-ua/sresolv/Doxyfile
config.status: creating libsofia-sip-ua/sresolv/Makefile
config.status: creating libsofia-sip-ua/stun/Doxyfile
config.status: creating libsofia-sip-ua/stun/Makefile
config.status: creating libsofia-sip-ua/su/Doxyfile
config.status: creating libsofia-sip-ua/su/Makefile
config.status: creating libsofia-sip-ua/tport/Doxyfile
config.status: creating libsofia-sip-ua/tport/Makefile
config.status: creating libsofia-sip-ua/url/Doxyfile
config.status: creating libsofia-sip-ua/url/Makefile
config.status: creating libsofia-sip-ua/features/sofia-sip/sofia_features.h
config.status: creating s2check/Makefile
config.status: creating libsofia-sip-ua-glib/Makefile
config.status: creating libsofia-sip-ua-glib/su-glib/Makefile
config.status: creating libsofia-sip-ua-glib/su-glib/Doxyfile
config.status: creating utils/Makefile
config.status: creating utils/Doxyfile
config.status: creating tests/Makefile
config.status: creating win32/Makefile
config.status: creating win32/config.h
config.status: creating open_c/Makefile
config.status: creating open_c/config.h
config.status: creating packages/sofia-sip-1.13.3.spec
config.status: creating config.h
config.status: creating libsofia-sip-ua/su/sofia-sip/su_configure.h
config.status: executing depfiles commands
config.status: executing libtool commands
config.status: executing version commands
configure: WARNING: unrecognized options: --disable-nls
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3'
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua'
Making built-sources in su
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/su'
gawk -f ../../libsofia-sip-ua/su/tag_dll.awk NODLL=1  REF=su_tag_ref.c su_tag.c
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/su'
Making built-sources in features
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/features'
make[6]: Nothing to be done for 'built-sources'.
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/features'
Making built-sources in bnf
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/bnf'
make[6]: Nothing to be done for 'built-sources'.
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/bnf'
Making built-sources in sresolv
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/sresolv'
make[6]: Nothing to be done for 'built-sources'.
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/sresolv'
Making built-sources in ipt
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/ipt'
make[6]: Nothing to be done for 'built-sources'.
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/ipt'
Making built-sources in sdp
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/sdp'
gawk -f ../../libsofia-sip-ua/su/tag_dll.awk NODLL=1  REF=sdp_tag_ref.c sdp_tag.c
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/sdp'
Making built-sources in url
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/url'
gawk -f ../../libsofia-sip-ua/su/tag_dll.awk NODLL=1 DLLREF=1 REF=url_tag_ref.c url_tag.c
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/url'
Making built-sources in msg
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/msg'
LC_ALL=C gawk -f ./msg_parser.awk module=msg NO_FIRST=1 NO_MIDDLE=1 \
	PR=sofia-sip/msg_protos.h TEMPLATE=./sofia-sip/msg_protos.h.in \
	./sofia-sip/msg_mime.h
LC_ALL=C gawk -f ./msg_parser.awk module=msg NO_FIRST=1 NO_LAST=1 \
	PR=sofia-sip/msg_mime_protos.h TEMPLATE=./sofia-sip/msg_mime_protos.h.in \
	./sofia-sip/msg_mime.h
multipart mismatch with Recursive multipart ()
LC_ALL=C gawk -f ./msg_parser.awk module=msg_multipart \
	tprefix=msg prefix=mp MC_HASH_SIZE=127 MC_SHORT_SIZE=26 \
	PT=msg_mime_table.c TEMPLATE=./msg_mime_table.c.in \
	./sofia-sip/msg_mime.h
LC_ALL=C gawk -f ./msg_parser.awk module=msg_test prefix=msg \
	MC_HASH_SIZE=127 multipart=msg_multipart \
	PT=test_table.c TEMPLATE=./test_table.c.in ./test_class.h
LC_ALL=C gawk -f ./msg_parser.awk module=msg_test NO_MIDDLE=1 NO_LAST=1 \
	PR=test_protos.h TEMPLATE=./test_protos.h.in ./test_class.h
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/msg'
Making built-sources in sip
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/sip'
LC_ALL=C gawk -f ./../msg/msg_parser.awk module=sip PR=sofia-sip/sip_hclasses.h TEMPLATE=./sofia-sip/sip_hclasses.h.in \
	./sofia-sip/sip.h
LC_ALL=C gawk -f ./../msg/msg_parser.awk module=sip PR=sofia-sip/sip_protos.h TEMPLATE=./sofia-sip/sip_protos.h.in \
	 ./sofia-sip/sip.h
LC_ALL=C gawk -f ./../msg/msg_parser.awk module=sip PR=sofia-sip/sip_tag.h TEMPLATE=./sofia-sip/sip_tag.h.in \
	./sofia-sip/sip.h
LC_ALL=C gawk -f ./../msg/msg_parser.awk module=sip PR=sofia-sip/sip_extra.h NO_FIRST=1 NO_LAST=1 \
	PACKAGE_NAME="sofia-sip" \
	PACKAGE_VERSION="1.13.3" \
	TEMPLATE1=./sofia-sip/sip_hclasses.h.in \
	TEMPLATE2=./sofia-sip/sip_protos.h.in \
	TEMPLATE3=./sofia-sip/sip_tag.h.in \
	TEMPLATE=./sofia-sip/sip_extra.h.in ./sip_extra_headers.txt
Suppress-Body-If-Match header is experimental
Suppress-Notify-If-Match header is experimental
LC_ALL=C gawk -f ./../msg/msg_parser.awk module=sip PR=sip_tag.c TEMPLATE=./sip_tag.c.in \
	./sofia-sip/sip.h ./sip_extra_headers.txt
Suppress-Body-If-Match header is experimental
Suppress-Notify-If-Match header is experimental
LC_ALL=C gawk -f ./../msg/msg_parser.awk module=sip PT=sip_parser_table.c TEMPLATE=./sip_parser_table.c.in \
	FLAGFILE=./sip_bad_mask \
	MC_HASH_SIZE=127 MC_SHORT_SIZE=26 \
	./sofia-sip/sip.h ./sip_extra_headers.txt
Suppress-Body-If-Match header is experimental
Suppress-Notify-If-Match header is experimental
gawk -f ../../libsofia-sip-ua/su/tag_dll.awk NODLL=1  REF=sip_tag_ref.c sip_tag.c
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/sip'
Making built-sources in http
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/http'
LC_ALL=C gawk -f ./../msg/msg_parser.awk module=http PR=sofia-sip/http_protos.h TEMPLATE=./sofia-sip/http_protos.h.in ./sofia-sip/http.h
LC_ALL=C gawk -f ./../msg/msg_parser.awk module=http PR=sofia-sip/http_tag.h TEMPLATE=./sofia-sip/http_tag.h.in ./sofia-sip/http.h
LC_ALL=C gawk -f ./../msg/msg_parser.awk module=http PR=http_tag.c TEMPLATE=./http_tag.c.in ./sofia-sip/http.h
LC_ALL=C gawk -f ./../msg/msg_parser.awk module=http PT=http_parser_table.c TEMPLATE=./http_parser_table.c.in \
	MC_HASH_SIZE=127 ./sofia-sip/http.h
gawk -f ../../libsofia-sip-ua/su/tag_dll.awk NODLL=1 DLLREF=1 REF=http_tag_ref.c http_tag.c
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/http'
Making built-sources in stun
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/stun'
gawk -f ../../libsofia-sip-ua/su/tag_dll.awk NODLL=1 LIST=stun_tag_list REF=stun_tag_ref.c stun_tag.c
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/stun'
Making built-sources in soa
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/soa'
gawk -f ../../libsofia-sip-ua/su/tag_dll.awk NODLL=1 LIST=soa_tag_list REF=soa_tag_ref.c soa_tag.c
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/soa'
Making built-sources in tport
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/tport'
gawk -f ../../libsofia-sip-ua/su/tag_dll.awk NODLL=1  REF=tport_tag_ref.c tport_tag.c
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/tport'
Making built-sources in nta
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/nta'
gawk -f ../../libsofia-sip-ua/su/tag_dll.awk NODLL=1 LIST=nta_tag_list REF=nta_tag_ref.c nta_tag.c
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/nta'
Making built-sources in nth
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/nth'
gawk -f ../../libsofia-sip-ua/su/tag_dll.awk NODLL=1  REF=nth_tag_ref.c nth_tag.c
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/nth'
Making built-sources in nea
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/nea'
gawk -f ../../libsofia-sip-ua/su/tag_dll.awk NODLL=1  REF=nea_tag_ref.c nea_tag.c
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/nea'
Making built-sources in iptsec
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/iptsec'
gawk -f ../../libsofia-sip-ua/su/tag_dll.awk NODLL=1  REF=auth_tag_ref.c auth_tag.c
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/iptsec'
Making built-sources in nua
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/nua'
gawk -f ../../libsofia-sip-ua/su/tag_dll.awk NODLL=1 LIST=nua_tag_list REF=nua_tag_ref.c nua_tag.c
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/nua'
Making built-sources in docs
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/docs'
gawk 'END { b="\\"; q="\\\""; \
	print "# Autogenerated aliases for RFCs "from" .. "to ; \
	print "ALIASES += " b; \
	for (i=from; i < to; i++) { \
	  print "RFC"i"=\"<a href="q site i type q">RFC "i"</a>\" "b; \
	}}' \
site=http://www.faqs.org/rfcs/rfc type=.html \
from=700 to=5500 \
/dev/null > Doxyfile.rfc
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/docs'
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua'
make  all-recursive
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3'
Making all in libsofia-sip-ua
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua'
Making built-sources in su
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/su'
make[7]: Nothing to be done for 'built-sources'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/su'
Making built-sources in features
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/features'
make[7]: Nothing to be done for 'built-sources'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/features'
Making built-sources in bnf
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/bnf'
make[7]: Nothing to be done for 'built-sources'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/bnf'
Making built-sources in sresolv
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/sresolv'
make[7]: Nothing to be done for 'built-sources'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/sresolv'
Making built-sources in ipt
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/ipt'
make[7]: Nothing to be done for 'built-sources'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/ipt'
Making built-sources in sdp
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/sdp'
make[7]: Nothing to be done for 'built-sources'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/sdp'
Making built-sources in url
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/url'
make[7]: Nothing to be done for 'built-sources'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/url'
Making built-sources in msg
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/msg'
make[7]: Nothing to be done for 'built-sources'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/msg'
Making built-sources in sip
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/sip'
make[7]: Nothing to be done for 'built-sources'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/sip'
Making built-sources in http
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/http'
make[7]: Nothing to be done for 'built-sources'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/http'
Making built-sources in stun
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/stun'
make[7]: Nothing to be done for 'built-sources'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/stun'
Making built-sources in soa
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/soa'
make[7]: Nothing to be done for 'built-sources'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/soa'
Making built-sources in tport
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/tport'
make[7]: Nothing to be done for 'built-sources'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/tport'
Making built-sources in nta
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/nta'
make[7]: Nothing to be done for 'built-sources'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/nta'
Making built-sources in nth
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/nth'
make[7]: Nothing to be done for 'built-sources'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/nth'
Making built-sources in nea
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/nea'
make[7]: Nothing to be done for 'built-sources'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/nea'
Making built-sources in iptsec
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/iptsec'
make[7]: Nothing to be done for 'built-sources'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/iptsec'
Making built-sources in nua
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/nua'
make[7]: Nothing to be done for 'built-sources'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/nua'
Making built-sources in docs
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/docs'
make[7]: Nothing to be done for 'built-sources'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/docs'
Making all in su
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/su'
make  all-am
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/su'
	 LTCOMPILE su.lo
	 LTCOMPILE su_errno.lo
	 LTCOMPILE su_addrinfo.lo
	 LTCOMPILE su_alloc.lo
	 LTCOMPILE su_alloc_lock.lo
	 LTCOMPILE su_strdup.lo
	 LTCOMPILE su_sprintf.lo
	 LTCOMPILE su_strlst.lo
	 LTCOMPILE su_vector.lo
	 LTCOMPILE su_time.lo
	 LTCOMPILE su_time0.lo
	 LTCOMPILE su_wait.lo
	 LTCOMPILE su_root.lo
	 LTCOMPILE su_timer.lo
	 LTCOMPILE su_port.lo
	 LTCOMPILE su_base_port.lo
	 LTCOMPILE su_pthread_port.lo
	 LTCOMPILE su_socket_port.lo
	 LTCOMPILE su_poll_port.lo
	 LTCOMPILE su_epoll_port.lo
	 LTCOMPILE su_select_port.lo
	 LTCOMPILE su_kqueue_port.lo
	 LTCOMPILE su_devpoll_port.lo
	 LTCOMPILE su_localinfo.lo
	 LTCOMPILE su_os_nw.lo
	 LTCOMPILE su_taglist.lo
	 LTCOMPILE su_tag.lo
	 LTCOMPILE su_tag_io.lo
	 LTCOMPILE su_log.lo
	 LTCOMPILE su_global_log.lo
	 LTCOMPILE su_default_log.lo
	 LTCOMPILE su_md5.lo
	 LTCOMPILE su_uniqueid.lo
	 LTCOMPILE su_bm.lo
	 LTCOMPILE smoothsort.lo
	 LTCOMPILE su_string.lo
	 LTCOMPILE string0.lo
	 LTCOMPILE memspn.lo
	 LTCOMPILE memcspn.lo
	 COMPILE addrinfo.o
	 COMPILE localinfo.o
	 LINK libsu.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
	 LINK addrinfo
	 LINK localinfo
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/su'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/su'
Making all in features
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/features'
	 LTCOMPILE features.lo
	 LINK libfeatures.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/features'
Making all in bnf
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/bnf'
	 LTCOMPILE bnf.lo
	 LINK libbnf.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/bnf'
Making all in sresolv
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/sresolv'
	 LTCOMPILE sres.lo
	 LTCOMPILE sres_cache.lo
	 LTCOMPILE sres_blocking.lo
	 LTCOMPILE sresolv.lo
	 LTCOMPILE sres_sip.lo
	 LINK libsresolv.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/sresolv'
Making all in ipt
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/ipt'
	 LTCOMPILE base64.lo
	 LTCOMPILE token64.lo
	 LINK libipt.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/ipt'
Making all in sdp
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/sdp'
make  all-am
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/sdp'
	 LTCOMPILE sdp.lo
	 LTCOMPILE sdp_parse.lo
	 LTCOMPILE sdp_print.lo
	 LTCOMPILE sdp_tag.lo
	 LTCOMPILE sdp_tag_ref.lo
	 LINK libsdp.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/sdp'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/sdp'
Making all in url
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/url'
make  all-am
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/url'
	 LTCOMPILE url.lo
	 LTCOMPILE url_tag.lo
	 LTCOMPILE url_tag_ref.lo
	 LINK liburl.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/url'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/url'
Making all in msg
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/msg'
make  all-am
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/msg'
	 COMPILE test_class.o
	 COMPILE test_table.o
	 COMPILE test_inlined.o
	 LTCOMPILE msg.lo
	 LTCOMPILE msg_tag.lo
	 LTCOMPILE msg_inlined.lo
	 LTCOMPILE msg_mime.lo
	 LTCOMPILE msg_mime_table.lo
	 LTCOMPILE msg_header_copy.lo
	 LTCOMPILE msg_header_make.lo
	 LTCOMPILE msg_parser.lo
	 LTCOMPILE msg_mclass.lo
	 LTCOMPILE msg_parser_util.lo
	 LTCOMPILE msg_basic.lo
	 LTCOMPILE msg_generic.lo
	 LTCOMPILE msg_date.lo
	 LTCOMPILE msg_auth.lo
rm -f libtest_msg.a
mips-openwrt-linux-musl-gcc-ar cru libtest_msg.a test_class.o test_table.o test_inlined.o 
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
mips-openwrt-linux-musl-gcc-ranlib libtest_msg.a
	 LINK libmsg.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/msg'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/msg'
Making all in sip
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/sip'
make  all-am
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/sip'
	 LTCOMPILE sip_parser.lo
	 LTCOMPILE sip_header.lo
	 LTCOMPILE sip_util.lo
	 LTCOMPILE sip_pref_util.lo
	 LTCOMPILE sip_basic.lo
	 LTCOMPILE sip_extra.lo
	 LTCOMPILE sip_feature.lo
	 LTCOMPILE sip_mime.lo
	 LTCOMPILE sip_security.lo
	 LTCOMPILE sip_event.lo
	 LTCOMPILE sip_prack.lo
	 LTCOMPILE sip_refer.lo
	 LTCOMPILE sip_session.lo
	 LTCOMPILE sip_caller_prefs.lo
	 LTCOMPILE sip_reason.lo
	 LTCOMPILE sip_status.lo
	 LTCOMPILE sip_time.lo
	 LTCOMPILE sip_tag_class.lo
	 LTCOMPILE sip_inlined.lo
	 LTCOMPILE sip_tag.lo
	 LTCOMPILE sip_parser_table.lo
	 LTCOMPILE sip_tag_ref.lo
	 LINK libsip.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/sip'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/sip'
Making all in http
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/http'
make  all-am
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/http'
	 LTCOMPILE http_parser.lo
	 LTCOMPILE http_header.lo
	 LTCOMPILE http_basic.lo
	 LTCOMPILE http_extra.lo
	 LTCOMPILE http_inlined.lo
	 LTCOMPILE http_status.lo
	 LTCOMPILE http_tag_class.lo
	 LTCOMPILE http_tag.lo
	 LTCOMPILE http_parser_table.lo
	 LTCOMPILE http_tag_ref.lo
	 LINK libhttp.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/http'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/http'
Making all in soa
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/soa'
make  all-am
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/soa'
	 LTCOMPILE soa.lo
	 LTCOMPILE soa_static.lo
	 LTCOMPILE soa_tag.lo
	 LTCOMPILE soa_tag_ref.lo
	 LINK libsoa.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/soa'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/soa'
Making all in tport
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/tport'
make  all-am
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/tport'
	 LTCOMPILE tport.lo
	 LTCOMPILE tport_logging.lo
	 LTCOMPILE tport_stub_sigcomp.lo
	 LTCOMPILE tport_type_udp.lo
	 LTCOMPILE tport_type_tcp.lo
	 LTCOMPILE tport_type_sctp.lo
	 LTCOMPILE tport_tag.lo
	 LTCOMPILE tport_tag_ref.lo
	 LTCOMPILE tport_type_connect.lo
	 LTCOMPILE tport_type_ws.lo
In file included from tport_ws.h:43,
                 from tport_type_ws.c:38:
ws.h:26:10: fatal error: openssl/ssl.h: No such file or directory
 #include <openssl/ssl.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
make[8]: *** [Makefile:1468: tport_type_ws.lo] Error 1
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/tport'
make[7]: *** [Makefile:750: all] Error 2
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua/tport'
make[6]: *** [Makefile:611: all-recursive] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/libsofia-sip-ua'
make[5]: *** [Makefile:503: all-recursive] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3'
make[4]: *** [Makefile:424: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3'
make[3]: *** [Makefile:93: /openwrt/build_dir/target-mips_24kc_musl/sofia-sip-1.13.3/.built] Error 2
```
