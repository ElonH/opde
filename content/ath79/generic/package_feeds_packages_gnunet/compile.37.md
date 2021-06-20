---
title: "compile.37"
date: 2021-06-20 22:29:33.380486
hidden: false
draft: false
weight: -37
---

build number: `37`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/gnunet/compile -j$(nproc) || make package/feeds/packages/gnunet/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/100-fix-opus-and-pulse-library-detection.patch using plaintext: 
patching file configure.ac
Hunk #1 succeeded at 837 (offset 24 lines).
Hunk #2 succeeded at 882 (offset 24 lines).
Copying file ABOUT-NLS
Copying file build-aux/config.rpath
Copying file m4/gettext.m4
Copying file m4/host-cpu-c-abi.m4
Copying file m4/iconv.m4
Copying file m4/intlmacosx.m4
Copying file m4/lib-ld.m4
Copying file m4/lib-link.m4
Copying file m4/lib-prefix.m4
Copying file m4/nls.m4
Copying file m4/po.m4
Copying file m4/progtest.m4
Copying file po/Makefile.in.in
Copying file po/Makevars.template
Copying file po/Rules-quot
Copying file po/en@boldquot.header
Copying file po/en@quot.header
Copying file po/insert-header.sin
Copying file po/remove-potcdate.sin
autoreconf: Entering directory `.'
autoreconf: running: true --force
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force -I m4
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
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
autoreconf: Leaving directory `.'
configure: loading site script /openwrt/include/site/mips
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking target system type... mips-openwrt-linux-gnu
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether make supports nested variables... (cached) yes
checking for gawk... (cached) gawk
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
checking for ccache_cc option to accept ISO C99... none needed
checking for mips-openwrt-linux-gcc... mips-openwrt-linux-gcc
checking whether we are using the GNU Objective C compiler... no
checking whether mips-openwrt-linux-gcc accepts -g... no
checking dependency style of mips-openwrt-linux-gcc... gcc3
checking whether ln -s works... yes
checking whether make sets $(MAKE)... (cached) yes
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache_cc... mips-openwrt-linux-musl-ld
checking if the linker (mips-openwrt-linux-musl-ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... mips-openwrt-linux-musl-gcc-nm
checking the name lister (mips-openwrt-linux-musl-gcc-nm) interface... BSD nm
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
checking for mips-openwrt-linux-ar... mips-openwrt-linux-musl-gcc-ar
checking for archiver @FILE support... @
checking for mips-openwrt-linux-strip... (cached) mips-openwrt-linux-musl-strip
checking for mips-openwrt-linux-ranlib... mips-openwrt-linux-musl-gcc-ranlib
checking command to parse mips-openwrt-linux-musl-gcc-nm output from ccache_cc object... ok
checking for sysroot... no
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
checking for shl_load... no
checking for shl_load in -ldld... no
checking for dlopen... yes
checking whether a program can dlopen itself... cross
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... no
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking for _LARGEFILE_SOURCE value needed for large files... no
checking whether cc can use -fno-strict-aliasing... checking if ccache_cc supports -Wno-address-of-packed-member flag... no
checking if ccache_cc supports -Wno-tautological-constant-out-of-range-compare flag... no
checking for X... no
checking for build target... linux
checking whether unaligned 64-bit access works... no
checking for library containing gethostbyname... none required
checking for library containing memrchr... none required
checking for library containing memset_s... no
checking for library containing explicit_bzero... none required
checking for socket in -lsocket... no
checking for log in -lm... yes
checking for getloadavg in -lc... yes
checking for getopt... true
checking for pkgconf,... /openwrt/staging_dir/host/bin/pkg-config
checking for ssh... false
checking for SSH key... ./configure: line 11983: ssh: command not found
checking for a Python interpreter with version >= 3.4... python3
checking for python3... /openwrt/staging_dir/hostpkg/bin/python3
checking for python3 version... 3.9
checking for python3 platform... linux
checking for python3 script directory... ${prefix}/lib/python3.9/site-packages
checking for python3 extension module directory... ${exec_prefix}/lib/python3.9/site-packages
checking for perl... /openwrt/staging_dir/host/bin/perl
checking for awk... /openwrt/staging_dir/host/bin/awk
checking whether to install gnunet-logread... no
checking for mips-openwrt-linux-iptables... no
configure: WARNING: warning: 'iptables' not found.
checking for mips-openwrt-linux-ip6tables... no
configure: WARNING: warning: 'ip6tables' not found.
checking for mips-openwrt-linux-ip... no
configure: WARNING: warning: 'ip' not found.
checking for mips-openwrt-linux-ifconfig... no
checking for ifconfig... false
configure: WARNING: 'ifconfig' not found.
checking for adduser... /usr/sbin/adduser
checking for mips-openwrt-linux-sysctl... no
checking for sysctl... false
checking for mips-openwrt-linux-upnpc... no
configure: WARNING: warning: 'upnpc' binary not found.
checking for checkbashisms... no
checking for checkbashisms.pl... no
checking for uncrustify... no
checking for yapf... no
checking for yapf3.0... no
checking for yapf3.1... no
checking for yapf3.2... no
checking for yapf3.3... no
checking for yapf3.4... no
checking for yapf3.5... no
checking for yapf3.6... no
checking for yapf3.7... no
checking for yapf3.8... no
checking for yapf3.9... no
checking for yapf4.0... no
checking for struct tm.tm_gmtoff... yes
checking for getaddrinfo_a in -lanl... no
checking for libgcrypt-config... /openwrt/staging_dir/target-mips_24kc_musl/host/bin/libgcrypt-config
checking for LIBGCRYPT - version >= 1.9.0... yes (1.9.3)
checking LIBGCRYPT API version... okay
configure: WARNING: "Some subsystems do not work with gcrypt >=1.9.0"
checking whether gcry_mpi_set_opaque_copy is declared... yes
checking whether struct in6_ifreq is declared... no
checking if_tun.h usability... no
checking if_tun.h presence... no
checking for if_tun.h... no
checking linux/if_tun.h usability... yes
checking linux/if_tun.h presence... yes
checking for linux/if_tun.h... yes
checking whether to build documentation... no
checking whether to include generated texi2mdoc output in installation... no
checking for texi2mdoc binary... checking for texi2mdoc... no
checking for texi2man perl script... checking for texi2man... no
checking for mandoc binary... checking for mandoc... no
checking whether to build only documentation... no
checking whether to include man pages... yes
checking whether to enable texinfo4 switches... no
checking whether to poison freed memory... no
checking for libbluetooth... /openwrt/staging_dir/target-mips_24kc_musl/usr
checking bluetooth/bluetooth.h usability... yes
checking bluetooth/bluetooth.h presence... yes
checking for bluetooth/bluetooth.h... yes
checking for ba2str in -lbluetooth... yes
checking for libzbar... --with-zbar not specified
checking for zbar_processor_create in -lzbar... no
configure: WARNING: zbar not found
checking for libjansson... --with-jansson not specified
checking for json_loads in -ljansson... yes
checking jansson.h usability... yes
checking jansson.h presence... yes
checking for jansson.h... yes
configure: jansson was found
checking for libpulse... /openwrt/staging_dir/target-mips_24kc_musl/usr
checking pulse/simple.h usability... no
checking pulse/simple.h presence... no
checking for pulse/simple.h... no
checking for libopus... /openwrt/staging_dir/target-mips_24kc_musl/usr
checking opus/opus.h usability... yes
checking opus/opus.h presence... yes
checking for opus/opus.h... yes
checking whether OPUS_SET_GAIN is declared... yes
checking for libogg... /openwrt/staging_dir/target-mips_24kc_musl/usr
checking ogg/ogg.h usability... yes
checking ogg/ogg.h presence... yes
checking for ogg/ogg.h... yes
checking for ogg_stream_flush_fill in -logg... yes
checking pkg-config is at least version 0.9.0... yes
checking for GLIB... yes
checking pbc/pbc.h usability... yes
checking pbc/pbc.h presence... yes
checking for pbc/pbc.h... yes
checking gabe.h usability... yes
checking gabe.h presence... yes
checking for gabe.h... yes
checking for gstreamer... checking for GST... yes
checking conversation feature set to build... checking for gawk... (cached) gawk
checking for gnurl-config... /openwrt/staging_dir/target-mips_24kc_musl/usr/bin/gnurl-config
checking for the version of libgnurl... 7.72.0
checking for libgnurl >= version 7.34.0... yes
checking whether libgnurl is usable... yes
checking for curl_free... yes
checking for gawk... (cached) gawk
checking for curl-config... no
checking whether libcurl is usable... no
checking for library containing __atomic_load_8... -latomic
checking nss.h usability... no
checking nss.h presence... no
checking for nss.h... no
configure: WARNING: No GNU libc nss header, will not build NSS plugin
checking for kvm_open in -lkvm... no
checking for kstat_open in -lkstat... no
checking sodium.h usability... yes
checking sodium.h presence... yes
checking for sodium.h... yes
checking for crypto_scalarmult_ed25519_base_noclamp in -lsodium... yes
checking for libextractor... /openwrt/staging_dir/target-mips_24kc_musl/usr
checking extractor.h usability... yes
checking extractor.h presence... yes
checking for extractor.h... yes
checking for EXTRACTOR_plugin_add_defaults in -lextractor... yes
checking for libltdl... yes
checking ltdl.h usability... yes
checking ltdl.h presence... yes
checking for ltdl.h... yes
checking for lt_dlopenext in -lltdl... yes
libltdl found
checking for idn or idn2... checking for idn... checking idna.h usability... no
checking idna.h presence... no
checking for idna.h... no
checking idn/idna.h usability... no
checking idn/idna.h presence... no
checking for idn/idna.h... no
checking for idn2... checking idn2.h usability... yes
checking idn2.h presence... yes
checking for idn2.h... yes
configure: Found idn2.h
checking if libidn can be used... configure: Checking for libidn2
checking for idn2_to_unicode_8z8z in -lidn2... yes
checking zlib.h usability... yes
checking zlib.h presence... yes
checking for zlib.h... yes
checking for compress2 in -lz... yes
checking for ld... mips-openwrt-linux-musl-ld
checking if the linker (mips-openwrt-linux-musl-ld) is GNU ld... yes
checking for shared library run path origin... done
checking 32-bit host C ABI... yes
checking for ELF binary format... yes
checking for the common suffixes of directories in the library search path... lib,lib32,lib
checking for iconv... yes
checking for working iconv... guessing yes
checking how to link with libiconv... /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib/libiconv.a
checking for iconv declaration... 
         extern size_t iconv (iconv_t cd, char * *inbuf, size_t *inbytesleft, char * *outbuf, size_t *outbytesleft);
checking for libunistring... yes
checking how to link with libunistring... /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libunistring.so -Wl,-rpath -Wl,/openwrt/staging_dir/target-mips_24kc_musl/usr/lib
checking for libunistring version... 0.9.10
checking unistr.h usability... yes
checking unistr.h presence... yes
checking for unistr.h... yes
checking for dirent.h that defines DIR... yes
checking for library containing opendir... none required
checking for ANSI C header files... (cached) yes
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking math.h usability... yes
checking math.h presence... yes
checking for math.h... yes
checking errno.h usability... yes
checking errno.h presence... yes
checking for errno.h... yes
checking ctype.h usability... yes
checking ctype.h presence... yes
checking for ctype.h... yes
checking limits.h usability... yes
checking limits.h presence... yes
checking for limits.h... yes
checking stdio.h usability... yes
checking stdio.h presence... yes
checking for stdio.h... yes
checking for stdlib.h... (cached) yes
checking for string.h... (cached) yes
checking for unistd.h... (cached) yes
checking stdarg.h usability... yes
checking stdarg.h presence... yes
checking for stdarg.h... yes
checking signal.h usability... yes
checking signal.h presence... yes
checking for signal.h... yes
checking locale.h usability... yes
checking locale.h presence... yes
checking for locale.h... yes
checking for sys/stat.h... (cached) yes
checking for sys/types.h... (cached) yes
checking stdatomic.h usability... yes
checking stdatomic.h presence... yes
checking for stdatomic.h... yes
checking malloc.h usability... yes
checking malloc.h presence... yes
checking for malloc.h... yes
checking malloc/malloc.h usability... no
checking malloc/malloc.h presence... no
checking for malloc/malloc.h... no
checking malloc/malloc_np.h usability... no
checking malloc/malloc_np.h presence... no
checking for malloc/malloc_np.h... no
checking langinfo.h usability... yes
checking langinfo.h presence... yes
checking for langinfo.h... yes
checking sys/param.h usability... yes
checking sys/param.h presence... yes
checking for sys/param.h... yes
checking sys/mount.h usability... yes
checking sys/mount.h presence... yes
checking for sys/mount.h... yes
checking sys/statvfs.h usability... yes
checking sys/statvfs.h presence... yes
checking for sys/statvfs.h... yes
checking sys/select.h usability... yes
checking sys/select.h presence... yes
checking for sys/select.h... yes
checking sockLib.h usability... no
checking sockLib.h presence... no
checking for sockLib.h... no
checking sys/mman.h usability... yes
checking sys/mman.h presence... yes
checking for sys/mman.h... yes
checking sys/msg.h usability... yes
checking sys/msg.h presence... yes
checking for sys/msg.h... yes
checking sys/vfs.h usability... yes
checking sys/vfs.h presence... yes
checking for sys/vfs.h... yes
checking arpa/inet.h usability... yes
checking arpa/inet.h presence... yes
checking for arpa/inet.h... yes
checking for fcntl.h... (cached) yes
checking libintl.h usability... yes
checking libintl.h presence... yes
checking for libintl.h... yes
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
checking sys/time.h usability... yes
checking sys/time.h presence... yes
checking for sys/time.h... yes
checking for unistd.h... (cached) yes
checking kstat.h usability... no
checking kstat.h presence... no
checking for kstat.h... no
checking sys/sysinfo.h usability... yes
checking sys/sysinfo.h presence... yes
checking for sys/sysinfo.h... yes
checking kvm.h usability... no
checking kvm.h presence... no
checking for kvm.h... no
checking sys/file.h usability... yes
checking sys/file.h presence... yes
checking for sys/file.h... yes
checking sys/resource.h usability... yes
checking sys/resource.h presence... yes
checking for sys/resource.h... yes
checking ifaddrs.h usability... yes
checking ifaddrs.h presence... yes
checking for ifaddrs.h... yes
checking mach/mach.h usability... no
checking mach/mach.h presence... no
checking for mach/mach.h... no
checking stddef.h usability... yes
checking stddef.h presence... yes
checking for stddef.h... yes
checking sys/timeb.h usability... yes
checking sys/timeb.h presence... yes
checking for sys/timeb.h... yes
checking argz.h usability... no
checking argz.h presence... no
checking for argz.h... no
checking ucred.h usability... no
checking ucred.h presence... no
checking for ucred.h... no
checking sys/ucred.h usability... no
checking sys/ucred.h presence... no
checking for sys/ucred.h... no
checking endian.h usability... yes
checking endian.h presence... yes
checking for endian.h... yes
checking sys/endian.h usability... no
checking sys/endian.h presence... no
checking for sys/endian.h... no
checking execinfo.h usability... no
checking execinfo.h presence... no
checking for execinfo.h... no
checking byteswap.h usability... yes
checking byteswap.h presence... yes
checking for byteswap.h... yes
checking for sys/types.h... (cached) yes
checking for netinet/in_systm.h... yes
checking for netinet/in.h... (cached) yes
checking for netinet/ip.h... yes
checking for SQLite... "/openwrt/staging_dir/target-mips_24kc_musl/usr"
checking sqlite3.h usability... yes
checking sqlite3.h presence... yes
checking for sqlite3.h... yes
checking pkg-config is at least version 0.9.0... yes
checking for the PostgreSQL libraries CPPFLAGS... -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include 
checking for the PostgreSQL libraries LDFLAGS... -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib 
checking for the PostgreSQL libraries LIBS... -lpq 
checking for the PostgreSQL version... 13.2
checking libpq-fe.h usability... yes
checking libpq-fe.h presence... yes
checking for libpq-fe.h... yes
checking for the PostgreSQL library linking is working... yes
checking for libpq-fe.h... (cached) yes
checking for sigset_t... yes
checking for off_t... yes
checking for size_t... yes
checking for mysql... /openwrt/staging_dir/target-mips_24kc_musl/usr
checking mysql/mysql.h usability... no
checking mysql/mysql.h presence... no
checking for mysql/mysql.h... no
checking for MHD... no
configure: error: Package requirements (libmicrohttpd >= 0.9.63) were not met:

Package 'libmicrohttpd', required by 'virtual:world', not found

Consider adjusting the PKG_CONFIG_PATH environment variable if you
installed software in a non-standard prefix.

Alternatively, you may set the environment variables MHD_CFLAGS
and MHD_LIBS to avoid the need to call pkg-config.
See the pkg-config man page for more details.
make[3]: *** [Makefile:408: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/.configured_a17fb5ef857664f03cd0ce37cc5ea591] Error 1
```
