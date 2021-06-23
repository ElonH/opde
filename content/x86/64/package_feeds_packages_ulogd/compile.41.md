---
title: "compile.41"
date: 2021-06-23 23:08:17.564190
hidden: false
draft: false
weight: -41
---

build number: `41`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/ulogd/compile -j$(nproc) || make package/feeds/packages/ulogd/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-json-remote.patch using plaintext: 
patching file output/ulogd_output_JSON.c
patching file ulogd.conf.in

Applying ./patches/020-fix-musl.patch using plaintext: 
patching file src/ulogd.c

Applying ./patches/030-ipfix-add.patch using plaintext: 
patching file configure.ac
patching file include/ulogd/ulogd.h
patching file output/Makefile.am
patching file output/ipfix/Makefile.am
patching file output/ipfix/ipfix.c
patching file output/ipfix/ipfix.h
patching file output/ipfix/ulogd_output_IPFIX.c

Applying ./patches/040-ipfix-template.patch using plaintext: 
patching file include/ulogd/ipfix_protocol.h
patching file output/ipfix/ipfix.c
patching file output/ipfix/ipfix.h
patching file output/ipfix/ulogd_output_IPFIX.c
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-x86_64_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal -I m4 -I . --force -I m4
autoreconf: configure.ac: tracing
autoreconf: running: /openwrt/staging_dir/host/bin/libtoolize --install --force
OpenWrt-libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, `build-aux'.
OpenWrt-libtoolize: linking file `build-aux/config.guess'
OpenWrt-libtoolize: linking file `build-aux/config.sub'
OpenWrt-libtoolize: linking file `build-aux/install-sh'
OpenWrt-libtoolize: linking file `build-aux/ltmain.sh'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `m4'.
OpenWrt-libtoolize: linking file `m4/libtool.m4'
OpenWrt-libtoolize: linking file `m4/ltoptions.m4'
OpenWrt-libtoolize: linking file `m4/ltsugar.m4'
OpenWrt-libtoolize: linking file `m4/ltversion.m4'
OpenWrt-libtoolize: linking file `m4/lt~obsolete.m4'
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-x86_64_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-x86_64_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
autoreconf: Leaving directory `.'
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/x86_64
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for x86_64-openwrt-linux-strip... x86_64-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking how to create a pax tar archive... gnutar
checking for style of include used by make... GNU
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
checking dependency style of ccache_cc... gcc3
checking for x86_64-openwrt-linux-ar... x86_64-openwrt-linux-musl-gcc-ar
checking the archiver (x86_64-openwrt-linux-musl-gcc-ar) interface... ar
checking whether make supports nested variables... (cached) yes
checking whether make sets $(MAKE)... (cached) yes
checking for x86_64-openwrt-linux-gcc... (cached) ccache_cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether ccache_cc accepts -g... (cached) yes
checking for ccache_cc option to accept ISO C89... (cached) none needed
checking whether ccache_cc understands -c and -o together... (cached) yes
checking dependency style of ccache_cc... (cached) gcc3
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-openwrt-linux-gnu
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
checking whether the shell understands some XSI constructs... yes
checking whether the shell understands "+="... yes
checking how to convert x86_64-pc-linux-gnu file names to x86_64-openwrt-linux-gnu format... func_convert_file_noop
checking how to convert x86_64-pc-linux-gnu file names to toolchain format... func_convert_file_noop
checking for x86_64-openwrt-linux-musl-ld option to reload object files... -r
checking for x86_64-openwrt-linux-objdump... x86_64-openwrt-linux-musl-objdump
checking how to recognize dependent libraries... pass_all
checking for x86_64-openwrt-linux-dlltool... no
checking for dlltool... no
checking how to associate runtime and link libraries... printf %s\n
checking for x86_64-openwrt-linux-ar... (cached) x86_64-openwrt-linux-musl-gcc-ar
checking for archiver @FILE support... @
checking for x86_64-openwrt-linux-strip... (cached) x86_64-openwrt-linux-musl-strip
checking for x86_64-openwrt-linux-ranlib... x86_64-openwrt-linux-musl-gcc-ranlib
checking command to parse x86_64-openwrt-linux-musl-gcc-nm output from ccache_cc object... ok
checking for sysroot... no
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
checking whether to build static libraries... no
checking for library containing dlopen... none required
checking for dirent.h that defines DIR... yes
checking for library containing opendir... none required
checking for ANSI C header files... (cached) yes
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking for unistd.h... (cached) yes
checking for an ANSI C-conforming const... yes
checking for size_t... yes
checking whether struct tm is in sys/time.h or time.h... time.h
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking for vprintf... yes
checking for _doprnt... no
checking for socket... yes
checking for strerror... (cached) yes
checking for library containing pthread_create... none required
checking pkg-config is at least version 0.9.0... yes
checking for LIBNFNETLINK... yes
checking for LIBNETFILTER_LOG... yes
checking for LIBNETFILTER_CONNTRACK... yes
checking for LIBMNL... yes
checking for LIBNETFILTER_ACCT... yes
checking for PostgreSQL pg_config program... checking for PostgreSQL includes in /openwrt/staging_dir/target-x86_64_musl/usr/include... yes
checking for PostgreSQL libraries in /openwrt/staging_dir/target-x86_64_musl/usr/lib... yes
checking for MySQL mysql_config program... checking for MySQL includes in /openwrt/staging_dir/target-x86_64_musl/usr/include/mysql... configure: WARNING: mysql.h not found
checking for MySQL libraries in /openwrt/staging_dir/target-x86_64_musl/usr/lib/mysql... configure: WARNING: libmysqlclient.so not found
checking mysql.h usability... no
checking mysql.h presence... no
checking for mysql.h... no
configure: WARNING: mysql.h not found
checking for mysql_close in -lmysqlclient... no
configure: WARNING: libmysqlclient.so not found
checking for libsqlite3... yes
checking for libdbi includes in /openwrt/staging_dir/target-x86_64_musl/usr/include/dbi... yes
checking for libdbi in /openwrt/staging_dir/target-x86_64_musl/usr/lib... yes
checking for library containing pcap_close... -lpcap
checking for libjansson... yes
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating include/Makefile
config.status: creating include/ulogd/Makefile
config.status: creating include/libipulog/Makefile
config.status: creating include/linux/Makefile
config.status: creating include/linux/netfilter/Makefile
config.status: creating include/linux/netfilter_ipv4/Makefile
config.status: creating libipulog/Makefile
config.status: creating input/Makefile
config.status: creating input/packet/Makefile
config.status: creating input/flow/Makefile
config.status: creating input/sum/Makefile
config.status: creating filter/Makefile
config.status: creating filter/raw2packet/Makefile
config.status: creating filter/packet2flow/Makefile
config.status: creating output/Makefile
config.status: creating output/pcap/Makefile
config.status: creating output/mysql/Makefile
config.status: creating output/pgsql/Makefile
config.status: creating output/sqlite3/Makefile
config.status: creating output/dbi/Makefile
config.status: creating output/ipfix/Makefile
config.status: creating src/Makefile
config.status: creating Makefile
config.status: creating Rules.make
config.status: creating config.h
config.status: executing depfiles commands
config.status: executing libtool commands
configure: WARNING: unrecognized options: --disable-nls

Ulogd configuration:
  Default plugins directory:		/usr/lib/ulogd
  Input plugins:
    NFLOG plugin:			yes
    NFCT plugin:			yes
    NFACCT plugin:			yes
    ULOG plugin:			yes
  Output plugins:
    PCAP plugin:			yes
    PGSQL plugin:			yes
    MySQL plugin:			no
    SQLITE3 plugin:			yes
    DBI plugin:				yes
    JSON plugin:			yes

You can now run 'make' and 'make install'
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7'
make  all-recursive
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7'
Making all in include
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include'
Making all in ulogd
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/ulogd'
make[7]: Nothing to be done for 'all'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/ulogd'
Making all in libipulog
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/libipulog'
make[7]: Nothing to be done for 'all'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/libipulog'
Making all in linux
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/linux'
Making all in netfilter
make[8]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/linux/netfilter'
make[8]: Nothing to be done for 'all'.
make[8]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/linux/netfilter'
Making all in netfilter_ipv4
make[8]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/linux/netfilter_ipv4'
make[8]: Nothing to be done for 'all'.
make[8]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/linux/netfilter_ipv4'
make[8]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/linux'
make[8]: Nothing to be done for 'all-am'.
make[8]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/linux'
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/linux'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include'
make[7]: Nothing to be done for 'all-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include'
Making all in libipulog
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/libipulog'
  CC       libipulog.lo
  CCLD     libipulog.la
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/libipulog'
Making all in src
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/src'
  CC       ulogd.o
  CC       select.o
  CC       timer.o
  CC       rbtree.o
  CC       conffile.o
  CC       hash.o
  CC       addr.o
  CCLD     ulogd
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/src'
Making all in input
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/input'
Making all in packet
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/input/packet'
  CC       ulogd_inppkt_UNIXSOCK.lo
  CC       ulogd_inppkt_ULOG.lo
  CC       ulogd_inppkt_NFLOG.lo
  CCLD     ulogd_inppkt_UNIXSOCK.la
  CCLD     ulogd_inppkt_ULOG.la
  CCLD     ulogd_inppkt_NFLOG.la
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/input/packet'
Making all in flow
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/input/flow'
  CC       ulogd_inpflow_NFCT.lo
In file included from ulogd_inpflow_NFCT.c:41:
../../include/ulogd/jhash.h: In function 'jhash':
../../include/ulogd/jhash.h:69:13: warning: this statement may fall through [-Wimplicit-fallthrough=]
  case 11: c += ((u32)k[10]<<24);
           ~~^~~~~~~~~~~~~~~~~~~
../../include/ulogd/jhash.h:70:2: note: here
  case 10: c += ((u32)k[9]<<16);
  ^~~~
../../include/ulogd/jhash.h:70:13: warning: this statement may fall through [-Wimplicit-fallthrough=]
  case 10: c += ((u32)k[9]<<16);
           ~~^~~~~~~~~~~~~~~~~~
../../include/ulogd/jhash.h:71:2: note: here
  case 9 : c += ((u32)k[8]<<8);
  ^~~~
../../include/ulogd/jhash.h:71:13: warning: this statement may fall through [-Wimplicit-fallthrough=]
  case 9 : c += ((u32)k[8]<<8);
           ~~^~~~~~~~~~~~~~~~~
../../include/ulogd/jhash.h:72:2: note: here
  case 8 : b += ((u32)k[7]<<24);
  ^~~~
../../include/ulogd/jhash.h:72:13: warning: this statement may fall through [-Wimplicit-fallthrough=]
  case 8 : b += ((u32)k[7]<<24);
           ~~^~~~~~~~~~~~~~~~~~
../../include/ulogd/jhash.h:73:2: note: here
  case 7 : b += ((u32)k[6]<<16);
  ^~~~
../../include/ulogd/jhash.h:73:13: warning: this statement may fall through [-Wimplicit-fallthrough=]
  case 7 : b += ((u32)k[6]<<16);
           ~~^~~~~~~~~~~~~~~~~~
../../include/ulogd/jhash.h:74:2: note: here
  case 6 : b += ((u32)k[5]<<8);
  ^~~~
../../include/ulogd/jhash.h:74:13: warning: this statement may fall through [-Wimplicit-fallthrough=]
  case 6 : b += ((u32)k[5]<<8);
           ~~^~~~~~~~~~~~~~~~~
../../include/ulogd/jhash.h:75:2: note: here
  case 5 : b += k[4];
  ^~~~
../../include/ulogd/jhash.h:75:13: warning: this statement may fall through [-Wimplicit-fallthrough=]
  case 5 : b += k[4];
           ~~^~~~~~~
../../include/ulogd/jhash.h:76:2: note: here
  case 4 : a += ((u32)k[3]<<24);
  ^~~~
../../include/ulogd/jhash.h:76:13: warning: this statement may fall through [-Wimplicit-fallthrough=]
  case 4 : a += ((u32)k[3]<<24);
           ~~^~~~~~~~~~~~~~~~~~
../../include/ulogd/jhash.h:77:2: note: here
  case 3 : a += ((u32)k[2]<<16);
  ^~~~
../../include/ulogd/jhash.h:77:13: warning: this statement may fall through [-Wimplicit-fallthrough=]
  case 3 : a += ((u32)k[2]<<16);
           ~~^~~~~~~~~~~~~~~~~~
../../include/ulogd/jhash.h:78:2: note: here
  case 2 : a += ((u32)k[1]<<8);
  ^~~~
../../include/ulogd/jhash.h:78:13: warning: this statement may fall through [-Wimplicit-fallthrough=]
  case 2 : a += ((u32)k[1]<<8);
           ~~^~~~~~~~~~~~~~~~~
../../include/ulogd/jhash.h:79:2: note: here
  case 1 : a += k[0];
  ^~~~
  CCLD     ulogd_inpflow_NFCT.la
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/input/flow'
Making all in sum
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/input/sum'
  CC       ulogd_inpflow_NFACCT.lo
  CCLD     ulogd_inpflow_NFACCT.la
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/input/sum'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/input'
make[7]: Nothing to be done for 'all-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/input'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/input'
Making all in filter
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/filter'
Making all in raw2packet
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/filter/raw2packet'
  CC       ulogd_raw2packet_BASE.lo
  CCLD     ulogd_raw2packet_BASE.la
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/filter/raw2packet'
Making all in packet2flow
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/filter/packet2flow'
make[7]: Nothing to be done for 'all'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/filter/packet2flow'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/filter'
  CC       ulogd_filter_IFINDEX.lo
  CC       ulogd_filter_PWSNIFF.lo
  CC       ulogd_filter_PRINTPKT.lo
  CC       ulogd_filter_PRINTFLOW.lo
  CC       ../util/printflow.lo
  CC       ulogd_filter_IP2STR.lo
  CC       ulogd_filter_IP2BIN.lo
  CC       ulogd_filter_HWHDR.lo
ulogd_filter_HWHDR.c: In function 'interp_mac2str':
ulogd_filter_HWHDR.c:212:4: warning: this statement may fall through [-Wimplicit-fallthrough=]
    parse_ethernet(ret, inp);
    ^~~~~~~~~~~~~~~~~~~~~~~~
ulogd_filter_HWHDR.c:213:3: note: here
   default:
   ^~~~~~~
  CC       ulogd_filter_MARK.lo
  CC       ulogd_filter_IP2HBIN.lo
  CCLD     ulogd_filter_IFINDEX.la
  CCLD     ulogd_filter_PWSNIFF.la
  CC       ../util/printpkt.lo
  CCLD     ulogd_filter_PRINTFLOW.la
  CCLD     ulogd_filter_IP2STR.la
  CCLD     ulogd_filter_IP2BIN.la
  CCLD     ulogd_filter_HWHDR.la
  CCLD     ulogd_filter_MARK.la
  CCLD     ulogd_filter_IP2HBIN.la
  CCLD     ulogd_filter_PRINTPKT.la
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/filter'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/filter'
Making all in output
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output'
Making all in pcap
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/pcap'
  CC       ulogd_output_PCAP.lo
  CCLD     ulogd_output_PCAP.la
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/pcap'
Making all in mysql
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/mysql'
make[7]: Nothing to be done for 'all'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/mysql'
Making all in pgsql
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/pgsql'
  CC       ulogd_output_PGSQL.lo
  CC       ../../util/db.lo
In file included from ../../util/db.c:37:
../../util/db.c: In function '__format_query_db':
../../include/ulogd/ulogd.h:306:2: warning: this statement may fall through [-Wimplicit-fallthrough=]
  __ulogd_log(level, __FILE__, __LINE__, format, ## args)
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
../../util/db.c:389:4: note: in expansion of macro 'ulogd_log'
    ulogd_log(ULOGD_NOTICE,
    ^~~~~~~~~
../../util/db.c:391:3: note: here
   default:
   ^~~~~~~
  CCLD     ulogd_output_PGSQL.la
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/pgsql'
Making all in sqlite3
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/sqlite3'
  CC       ulogd_output_SQLITE3.lo
  CCLD     ulogd_output_SQLITE3.la
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/sqlite3'
Making all in dbi
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/dbi'
  CC       ulogd_output_DBI.lo
ulogd_output_DBI.c: In function 'open_db_dbi':
ulogd_output_DBI.c:202:2: warning: 'dbi_driver_open' is deprecated [-Wdeprecated-declarations]
  driver = dbi_driver_open(dbtype);
  ^~~~~~
In file included from ulogd_output_DBI.c:22:
../../../../../staging_dir/target-x86_64_musl/usr/include/dbi/dbi.h:180:34: note: declared here
 dbi_driver LIBDBI_API_DEPRECATED dbi_driver_open(const char *name); /* goes thru linked list until it finds the right one */
                                  ^~~~~~~~~~~~~~~
ulogd_output_DBI.c:209:2: warning: 'dbi_conn_new' is deprecated [-Wdeprecated-declarations]
  pi->dbh = dbi_conn_new(dbtype);
  ^~
In file included from ulogd_output_DBI.c:22:
../../../../../staging_dir/target-x86_64_musl/usr/include/dbi/dbi.h:199:32: note: declared here
 dbi_conn LIBDBI_API_DEPRECATED dbi_conn_new(const char *name); /* shortcut for dbi_conn_open(dbi_driver_open("foo")) */
                                ^~~~~~~~~~~~
ulogd_output_DBI.c: In function 'init':
ulogd_output_DBI.c:327:2: warning: 'dbi_initialize' is deprecated [-Wdeprecated-declarations]
  dbi_initialize(NULL);
  ^~~~~~~~~~~~~~
In file included from ulogd_output_DBI.c:22:
../../../../../staging_dir/target-x86_64_musl/usr/include/dbi/dbi.h:169:27: note: declared here
 int LIBDBI_API_DEPRECATED dbi_initialize(const char *driverdir);
                           ^~~~~~~~~~~~~~
  CCLD     ulogd_output_DBI.la
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/dbi'
Making all in ipfix
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/ipfix'
  CC       ulogd_output_IPFIX.lo
  CC       ipfix.lo
  CCLD     ulogd_output_IPFIX.la
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/ipfix'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output'
  CC       ulogd_output_LOGEMU.lo
  CC       ulogd_output_SYSLOG.lo
  CC       ulogd_output_OPRINT.lo
  CC       ulogd_output_GPRINT.lo
  CC       ulogd_output_NACCT.lo
  CC       ulogd_output_XML.lo
  CC       ulogd_output_GRAPHITE.lo
  CC       ulogd_output_JSON.lo
  CCLD     ulogd_output_LOGEMU.la
  CCLD     ulogd_output_SYSLOG.la
  CCLD     ulogd_output_OPRINT.la
  CCLD     ulogd_output_GPRINT.la
  CCLD     ulogd_output_NACCT.la
  CCLD     ulogd_output_XML.la
  CCLD     ulogd_output_GRAPHITE.la
  CCLD     ulogd_output_JSON.la
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7'
sed -e 's,@pkglibdir\@,/usr/lib/ulogd,g' ./ulogd.conf.in >ulogd.conf
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7'
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7'
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7'
Making install in include
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include'
Making install in ulogd
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/ulogd'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/ulogd'
make[7]: Nothing to be done for 'install-exec-am'.
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/ulogd'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/ulogd'
Making install in libipulog
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/libipulog'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/libipulog'
make[7]: Nothing to be done for 'install-exec-am'.
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/libipulog'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/libipulog'
Making install in linux
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/linux'
Making install in netfilter
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/linux/netfilter'
make[8]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/linux/netfilter'
make[8]: Nothing to be done for 'install-exec-am'.
make[8]: Nothing to be done for 'install-data-am'.
make[8]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/linux/netfilter'
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/linux/netfilter'
Making install in netfilter_ipv4
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/linux/netfilter_ipv4'
make[8]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/linux/netfilter_ipv4'
make[8]: Nothing to be done for 'install-exec-am'.
make[8]: Nothing to be done for 'install-data-am'.
make[8]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/linux/netfilter_ipv4'
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/linux/netfilter_ipv4'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/linux'
make[8]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/linux'
make[8]: Nothing to be done for 'install-exec-am'.
make[8]: Nothing to be done for 'install-data-am'.
make[8]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/linux'
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/linux'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include/linux'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include'
make[7]: Nothing to be done for 'install-exec-am'.
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/include'
Making install in libipulog
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/libipulog'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/libipulog'
make[6]: Nothing to be done for 'install-exec-am'.
make[6]: Nothing to be done for 'install-data-am'.
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/libipulog'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/libipulog'
Making install in src
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/src'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/src'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/sbin'
  /bin/bash ../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c ulogd '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/sbin'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c ulogd /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/sbin/ulogd
make[6]: Nothing to be done for 'install-data-am'.
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/src'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/src'
Making install in input
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/input'
Making install in packet
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/input/packet'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/input/packet'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   ulogd_inppkt_UNIXSOCK.la ulogd_inppkt_ULOG.la ulogd_inppkt_NFLOG.la '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_inppkt_UNIXSOCK.so /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_inppkt_UNIXSOCK.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_inppkt_UNIXSOCK.lai /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_inppkt_UNIXSOCK.la
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_inppkt_ULOG.so /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_inppkt_ULOG.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_inppkt_ULOG.lai /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_inppkt_ULOG.la
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_inppkt_NFLOG.so /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_inppkt_NFLOG.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_inppkt_NFLOG.lai /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_inppkt_NFLOG.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/ulogd'
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/input/packet'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/input/packet'
Making install in flow
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/input/flow'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/input/flow'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   ulogd_inpflow_NFCT.la '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_inpflow_NFCT.so /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_inpflow_NFCT.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_inpflow_NFCT.lai /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_inpflow_NFCT.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/ulogd'
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/input/flow'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/input/flow'
Making install in sum
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/input/sum'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/input/sum'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   ulogd_inpflow_NFACCT.la '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_inpflow_NFACCT.so /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_inpflow_NFACCT.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_inpflow_NFACCT.lai /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_inpflow_NFACCT.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/ulogd'
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/input/sum'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/input/sum'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/input'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/input'
make[7]: Nothing to be done for 'install-exec-am'.
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/input'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/input'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/input'
Making install in filter
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/filter'
Making install in raw2packet
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/filter/raw2packet'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/filter/raw2packet'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   ulogd_raw2packet_BASE.la '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_raw2packet_BASE.so /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_raw2packet_BASE.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_raw2packet_BASE.lai /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_raw2packet_BASE.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/ulogd'
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/filter/raw2packet'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/filter/raw2packet'
Making install in packet2flow
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/filter/packet2flow'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/filter/packet2flow'
make[7]: Nothing to be done for 'install-exec-am'.
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/filter/packet2flow'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/filter/packet2flow'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/filter'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/filter'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd'
 /bin/bash ../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   ulogd_filter_IFINDEX.la ulogd_filter_PWSNIFF.la ulogd_filter_PRINTPKT.la ulogd_filter_PRINTFLOW.la ulogd_filter_IP2STR.la ulogd_filter_IP2BIN.la ulogd_filter_HWHDR.la ulogd_filter_MARK.la ulogd_filter_IP2HBIN.la '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_filter_IFINDEX.so /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_filter_IFINDEX.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_filter_IFINDEX.lai /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_filter_IFINDEX.la
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_filter_PWSNIFF.so /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_filter_PWSNIFF.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_filter_PWSNIFF.lai /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_filter_PWSNIFF.la
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_filter_PRINTPKT.so /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_filter_PRINTPKT.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_filter_PRINTPKT.lai /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_filter_PRINTPKT.la
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_filter_PRINTFLOW.so /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_filter_PRINTFLOW.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_filter_PRINTFLOW.lai /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_filter_PRINTFLOW.la
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_filter_IP2STR.so /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_filter_IP2STR.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_filter_IP2STR.lai /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_filter_IP2STR.la
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_filter_IP2BIN.so /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_filter_IP2BIN.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_filter_IP2BIN.lai /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_filter_IP2BIN.la
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_filter_HWHDR.so /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_filter_HWHDR.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_filter_HWHDR.lai /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_filter_HWHDR.la
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_filter_MARK.so /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_filter_MARK.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_filter_MARK.lai /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_filter_MARK.la
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_filter_IP2HBIN.so /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_filter_IP2HBIN.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_filter_IP2HBIN.lai /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_filter_IP2HBIN.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/ulogd'
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/filter'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/filter'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/filter'
Making install in output
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output'
Making install in pcap
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/pcap'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/pcap'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   ulogd_output_PCAP.la '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_output_PCAP.so /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_output_PCAP.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_output_PCAP.lai /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_output_PCAP.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/ulogd'
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/pcap'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/pcap'
Making install in mysql
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/mysql'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/mysql'
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/mysql'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/mysql'
Making install in pgsql
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/pgsql'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/pgsql'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   ulogd_output_PGSQL.la '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_output_PGSQL.so /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_output_PGSQL.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_output_PGSQL.lai /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_output_PGSQL.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/ulogd'
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/pgsql'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/pgsql'
Making install in sqlite3
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/sqlite3'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/sqlite3'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   ulogd_output_SQLITE3.la '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_output_SQLITE3.so /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_output_SQLITE3.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_output_SQLITE3.lai /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_output_SQLITE3.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/ulogd'
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/sqlite3'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/sqlite3'
Making install in dbi
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/dbi'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/dbi'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   ulogd_output_DBI.la '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_output_DBI.so /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_output_DBI.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_output_DBI.lai /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_output_DBI.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/ulogd'
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/dbi'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/dbi'
Making install in ipfix
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/ipfix'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/ipfix'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   ulogd_output_IPFIX.la '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_output_IPFIX.so /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_output_IPFIX.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_output_IPFIX.lai /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_output_IPFIX.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/ulogd'
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/ipfix'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output/ipfix'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd'
 /bin/bash ../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   ulogd_output_LOGEMU.la ulogd_output_SYSLOG.la ulogd_output_OPRINT.la ulogd_output_GPRINT.la ulogd_output_NACCT.la ulogd_output_XML.la ulogd_output_GRAPHITE.la ulogd_output_JSON.la '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_output_LOGEMU.so /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_output_LOGEMU.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_output_LOGEMU.lai /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_output_LOGEMU.la
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_output_SYSLOG.so /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_output_SYSLOG.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_output_SYSLOG.lai /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_output_SYSLOG.la
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_output_OPRINT.so /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_output_OPRINT.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_output_OPRINT.lai /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_output_OPRINT.la
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_output_GPRINT.so /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_output_GPRINT.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_output_GPRINT.lai /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_output_GPRINT.la
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_output_NACCT.so /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_output_NACCT.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_output_NACCT.lai /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_output_NACCT.la
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_output_XML.so /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_output_XML.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_output_XML.lai /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_output_XML.la
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_output_GRAPHITE.so /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_output_GRAPHITE.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_output_GRAPHITE.lai /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_output_GRAPHITE.la
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_output_JSON.so /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_output_JSON.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/ulogd_output_JSON.lai /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_output_JSON.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/ulogd'
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/output'
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7'
make[6]: Nothing to be done for 'install-exec-am'.
 /usr/bin/mkdir -p '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/man/man8'
 /openwrt/staging_dir/host/bin/install -c -m 644 ulogd.8 '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/man/man8'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7'
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7'
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-x86_64/ulogd/usr/sbin/ulogd: executable
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-x86_64/ulogd/usr/lib/ulogd/ulogd_raw2packet_BASE.so: shared object
Packaged contents of /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-x86_64/ulogd into /openwrt/bin/packages/x86_64/packages/ulogd_2.0.7-6_x86_64.ipk
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-x86_64/ulogd-mod-dbi/usr/lib/ulogd/ulogd_output_DBI.so: shared object
Packaged contents of /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-x86_64/ulogd-mod-dbi into /openwrt/bin/packages/x86_64/packages/ulogd-mod-dbi_2.0.7-6_x86_64.ipk
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-x86_64/ulogd-mod-json/usr/lib/ulogd/ulogd_output_JSON.so: shared object
Packaged contents of /openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-x86_64/ulogd-mod-json into /openwrt/bin/packages/x86_64/packages/ulogd-mod-json_2.0.7-6_x86_64.ipk
cp: cannot stat '/openwrt/build_dir/target-x86_64_musl/ulogd-2.0.7/ipkg-install/usr/lib/ulogd/ulogd_output_MYSQL.so': No such file or directory
make[3]: *** [Makefile:202: /openwrt/bin/packages/x86_64/packages/ulogd-mod-mysql_2.0.7-6_x86_64.ipk] Error 1
```
