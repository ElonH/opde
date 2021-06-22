---
title: "compile.40"
date: 2021-06-22 10:37:31.193190
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
checking for MHD... yes
checking whether NLS is requested... no
checking for msgfmt... /openwrt/staging_dir/hostpkg/bin/msgfmt
checking for gmsgfmt... /openwrt/staging_dir/hostpkg/bin/msgfmt
checking for xgettext... /openwrt/staging_dir/hostpkg/bin/xgettext
checking for msgmerge... /openwrt/staging_dir/hostpkg/bin/msgmerge
checking for CFPreferencesCopyAppValue... no
checking for CFLocaleCopyPreferredLanguages... no
checking whether to use NLS... no
checking for pid_t... yes
checking for size_t... (cached) yes
checking for mode_t... yes
checking whether time.h and sys/time.h may both be included... yes
checking whether stat file-mode macros are broken... no
checking for stdbool.h that conforms to C99... yes
checking for _Bool... yes
checking whether struct tm is in sys/time.h or time.h... time.h
checking for struct sockaddr_in.sin_len... no
checking for struct sockaddr_un.sun_len... no
checking whether closedir returns void... yes
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
checking for sys/select.h... (cached) yes
checking for sys/socket.h... (cached) yes
checking types of arguments for select... int,fd_set *,struct timeval *
checking for uid_t in sys/types.h... yes
checking for unistd.h... (cached) yes
checking for working chown... no
checking return type of signal handlers... void
checking whether lstat correctly handles trailing slash... (cached) yes
checking whether stat accepts an empty string... (cached) no
checking for strftime... (cached) yes
checking for vprintf... yes
checking for _doprnt... no
checking for sys/wait.h that is POSIX.1 compatible... yes
checking for off_t... (cached) yes
checking for uid_t in sys/types.h... (cached) yes
checking for atoll... yes
checking for stat64... yes
checking for strnlen... yes
checking for mremap... yes
checking for getrlimit... yes
checking for setrlimit... yes
checking for sysconf... yes
checking for initgroups... yes
checking for strndup... yes
checking for gethostbyname2... yes
checking for getpeerucred... no
checking for getpeereid... no
checking for setresuid... (cached) no
checking for getnameinfo... yes
checking for gethostname... yes
checking for gethostbyname... yes
checking for gethostbyaddr... yes
checking for getaddrinfo... (cached) yes
checking for getaddrinfo_a... no
checking for getifaddrs... yes
checking for freeifaddrs... yes
checking for getresgid... yes
checking for mallinfo... no
checking for malloc_size... no
checking for malloc_usable_size... yes
checking for getrusage... yes
checking for random... yes
checking for srandom... yes
checking for stat... yes
checking for statfs... yes
checking for statvfs... yes
checking for wait4... yes
checking for timegm... yes
checking for sudo... no
checking for doas... checking for doas... no
checking for gnunetdns group name... gnunetdns
checking for gnutls... /openwrt/staging_dir/target-mips_24kc_musl/usr
checking gnutls/abstract.h usability... no
checking gnutls/abstract.h presence... no
checking for gnutls/abstract.h... no
checking gnutls/dane.h usability... no
checking gnutls/dane.h presence... no
checking for gnutls/dane.h... no
checking if GNUnet is being configured to run on the SuperMUC... 
checking if NSE has to send timestamp information to testbed logger... no
checking whether to run tests... 
checking whether to compile in benchmarks (currently for http and crypto)... no
checking whether to run expensive tests... no
checking whether to enable ports for gnunet-java... no
checking whether to run benchmarks during make check... no
checking whether to compile gnunet-testing... yes
checking whether to compile experimental code... yes
checking whether to compile malicious code... no
checking whether to start peer's services on demand by default... yes
checking whether to create expensive statistics on memory use... 0
checking whether __thread is supported... yes
checking whether to compile with support for code coverage analysis... no
checking for svnversion... /usr/bin/svnversion
checking for git... /openwrt/staging_dir/host/bin/git
checking for source being under a VCS... checking for git... (cached) /openwrt/staging_dir/host/bin/git
checking for source being under a VCS... fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
no
checking VCS version... "release"
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating Makefile
config.status: creating bin/Makefile
config.status: creating contrib/Makefile
config.status: creating contrib/hellos/Makefile
config.status: creating contrib/services/Makefile
config.status: creating contrib/services/openrc/Makefile
config.status: creating contrib/services/systemd/Makefile
config.status: creating contrib/scripts/Makefile
config.status: creating contrib/scripts/gnunet-logread/Makefile
config.status: creating doc/Makefile
config.status: creating doc/man/Makefile
config.status: creating doc/doxygen/Makefile
config.status: creating doc/handbook/Makefile
config.status: creating doc/tutorial/Makefile
config.status: creating m4/Makefile
config.status: creating po/Makefile.in
config.status: creating src/Makefile
config.status: creating src/arm/Makefile
config.status: creating src/arm/arm.conf
config.status: creating src/ats/Makefile
config.status: creating src/ats/ats.conf
config.status: creating src/ats-tool/Makefile
config.status: creating src/ats-tests/Makefile
config.status: creating src/auction/Makefile
config.status: creating src/block/Makefile
config.status: creating src/cadet/Makefile
config.status: creating src/cadet/cadet.conf
config.status: creating src/core/Makefile
config.status: creating src/core/core.conf
config.status: creating src/consensus/Makefile
config.status: creating src/consensus/consensus.conf
config.status: creating src/conversation/Makefile
config.status: creating src/conversation/conversation.conf
config.status: creating src/curl/Makefile
config.status: creating src/datacache/Makefile
config.status: creating src/datastore/Makefile
config.status: creating src/datastore/datastore.conf
config.status: creating src/dht/Makefile
config.status: creating src/dht/dht.conf
config.status: creating src/dns/Makefile
config.status: creating src/dns/dns.conf
config.status: creating src/exit/Makefile
config.status: creating src/fragmentation/Makefile
config.status: creating src/fs/Makefile
config.status: creating src/fs/fs.conf
config.status: creating src/gns/Makefile
config.status: creating src/gns/gns.conf
config.status: creating src/gns/nss/Makefile
config.status: creating src/gnsrecord/Makefile
config.status: creating src/hello/Makefile
config.status: creating src/identity/Makefile
config.status: creating src/identity/identity.conf
config.status: creating src/include/Makefile
config.status: creating src/integration-tests/Makefile
config.status: creating src/json/Makefile
config.status: creating src/hostlist/Makefile
config.status: creating src/my/Makefile
config.status: creating src/mysql/Makefile
config.status: creating src/namecache/Makefile
config.status: creating src/namecache/namecache.conf
config.status: creating src/namestore/Makefile
config.status: creating src/namestore/namestore.conf
config.status: creating src/nat/Makefile
config.status: creating src/nat/nat.conf
config.status: creating src/nat-auto/Makefile
config.status: creating src/nat-auto/nat-auto.conf
config.status: creating src/nse/Makefile
config.status: creating src/nse/nse.conf
config.status: creating src/nt/Makefile
config.status: creating src/peerinfo/Makefile
config.status: creating src/peerinfo/peerinfo.conf
config.status: creating src/peerinfo-tool/Makefile
config.status: creating src/peerstore/Makefile
config.status: creating src/peerstore/peerstore.conf
config.status: creating src/pq/Makefile
config.status: creating src/pt/Makefile
config.status: creating src/regex/Makefile
config.status: creating src/regex/regex.conf
config.status: creating src/revocation/Makefile
config.status: creating src/revocation/revocation.conf
config.status: creating src/rps/Makefile
config.status: creating src/rps/rps.conf
config.status: creating src/secretsharing/Makefile
config.status: creating src/secretsharing/secretsharing.conf
config.status: creating src/scalarproduct/Makefile
config.status: creating src/scalarproduct/scalarproduct.conf
config.status: creating src/set/Makefile
config.status: creating src/set/set.conf
config.status: creating src/seti/Makefile
config.status: creating src/seti/seti.conf
config.status: creating src/setu/Makefile
config.status: creating src/setu/setu.conf
config.status: creating src/sq/Makefile
config.status: creating src/statistics/Makefile
config.status: creating src/statistics/statistics.conf
config.status: creating src/template/Makefile
config.status: creating src/testbed/Makefile
config.status: creating src/testbed/testbed.conf
config.status: creating src/testbed-logger/Makefile
config.status: creating src/testbed-logger/testbed-logger.conf
config.status: creating src/testing/Makefile
config.status: creating src/topology/Makefile
config.status: creating src/transport/Makefile
config.status: creating src/transport/transport.conf
config.status: creating src/util/Makefile
config.status: creating src/util/resolver.conf
config.status: creating src/vpn/Makefile
config.status: creating src/vpn/vpn.conf
config.status: creating src/zonemaster/Makefile
config.status: creating src/zonemaster/zonemaster.conf
config.status: creating src/rest/Makefile
config.status: creating src/abe/Makefile
config.status: creating src/reclaim/Makefile
config.status: creating src/messenger/Makefile
config.status: creating src/messenger/messenger.conf
config.status: creating pkgconfig/Makefile
config.status: creating pkgconfig/gnunetarm.pc
config.status: creating pkgconfig/gnunetats.pc
config.status: creating pkgconfig/gnunetblock.pc
config.status: creating pkgconfig/gnunetcadet.pc
config.status: creating pkgconfig/gnunetconsensus.pc
config.status: creating pkgconfig/gnunetconversation.pc
config.status: creating pkgconfig/gnunetcore.pc
config.status: creating pkgconfig/gnunetdatacache.pc
config.status: creating pkgconfig/gnunetdatastore.pc
config.status: creating pkgconfig/gnunetdht.pc
config.status: creating pkgconfig/gnunetdns.pc
config.status: creating pkgconfig/gnunetenv.pc
config.status: creating pkgconfig/gnunetfragmentation.pc
config.status: creating pkgconfig/gnunetfs.pc
config.status: creating pkgconfig/gnunetgns.pc
config.status: creating pkgconfig/gnunethello.pc
config.status: creating pkgconfig/gnunetidentity.pc
config.status: creating pkgconfig/gnunetmicrophone.pc
config.status: creating pkgconfig/gnunetmysql.pc
config.status: creating pkgconfig/gnunetnamestore.pc
config.status: creating pkgconfig/gnunetnat.pc
config.status: creating pkgconfig/gnunetnse.pc
config.status: creating pkgconfig/gnunetpeerinfo.pc
config.status: creating pkgconfig/gnunetpq.pc
config.status: creating pkgconfig/gnunetregex.pc
config.status: creating pkgconfig/gnunetrevocation.pc
config.status: creating pkgconfig/gnunetrps.pc
config.status: creating pkgconfig/gnunetscalarproduct.pc
config.status: creating pkgconfig/gnunetset.pc
config.status: creating pkgconfig/gnunetspeaker.pc
config.status: creating pkgconfig/gnunetstatistics.pc
config.status: creating pkgconfig/gnunettestbed.pc
config.status: creating pkgconfig/gnunettesting.pc
config.status: creating pkgconfig/gnunettransport.pc
config.status: creating pkgconfig/gnunetutil.pc
config.status: creating pkgconfig/gnunetvpn.pc
config.status: creating gnunet_config.h
config.status: executing depfiles commands
config.status: executing libtool commands
config.status: executing po-directories commands
config.status: creating po/POTFILES
config.status: creating po/Makefile
configure: Using libgnurl as HTTP client library.
configure: WARNING: GnuTLS not found, gnunet-gns-proxy will not be built
configure:
Detected system
===============

GNUnet version:                 0.14.1

Host setup:                     mips-openwrt-linux-gnu
Install prefix:                 /usr
Compiler:                       ccache_cc
CFLAGS:                         -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include 
CPPFLAGS:                       -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include 
LDFLAGS:                        -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio  -Wl,--unresolved-symbols=report-all
LIBS:                           -lm 
Build Target:                   linux

Default Interface:              eth0

MySQL:                          no
PostgreSQL:                     yes
sqlite3:                        yes
http client:                    curl-gnutls
bluetooth:                      yes
iptables:                       no (optional, DNS query interception will not work)
ifconfig:                       no (optional, some features will not work)
upnpc:                          no (optional, NAT traversal using UPnPc will not work)
gnutls:                         no (gnunet-gns-proxy will not be built)
libzbar:                        no (gnunet-qr will not be built)
java:                           
libidn:                         libidn2
libopus:                        yes
gstreamer:                      yes
libpulse:                       no
libextractor:                   yes
texi2mdoc:                      yes
mandoc:                         yes

GNUnet configuration:
=====================
transports:                     tcp udp unix http wlan bluetooth
conversation:                   yes (xgst)
database backends:              postgres sqlite 
experimental:                   yes

texinfo manual:                 no
transpiled mdocml manual:       no

configure: WARNING: Please make sure NOW to create a user and group 'gnunet' and additionally a group 'gnunetdns'. Make sure that '/var/lib/gnunet' is owned (and writable) by user 'gnunet'.
configure: To do this on this system, run:
# addgroup gnunetdns
# adduser --system --disabled-login --home /var/lib/gnunet gnunet

configure: WARNING: Each user of GNUnet should be added to the 'gnunet' group.
configure: To do this on this system, run:
# adduser USERNAME gnunet
   for each of your users, replacing "USERNAME" with the respective login name. Users may have to login again for the changes to take effect.

configure: For detailed setup instructions, type 'info gnunet' after the installation or visit https://docs.gnunet.org/
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1'
make  all-recursive
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1'
Making all in m4
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/m4'
make[6]: Nothing to be done for 'all'.
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/m4'
Making all in bin
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/bin'
make[6]: Nothing to be done for 'all'.
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/bin'
Making all in src
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src'
Making all in include
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/include'
Making all in .
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/include'
make[8]: Nothing to be done for 'all-am'.
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/include'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/include'
Making all in util
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util'
  CC       bandwidth.lo
  CC       bio.lo
  CC       buffer.lo
  CC       client.lo
  CC       common_allocation.lo
  CC       common_endian.lo
  CC       common_logging.lo
  CC       configuration.lo
  CC       configuration_loader.lo
  CC       consttime_memcmp.lo
  CC       container_bloomfilter.lo
  CC       container_heap.lo
  CC       container_meta_data.lo
  CC       container_multihashmap.lo
  CC       container_multishortmap.lo
  CC       container_multiuuidmap.lo
  CC       container_multipeermap.lo
  CC       container_multihashmap32.lo
  CC       crypto_symmetric.lo
  CC       crypto_crc.lo
  CC       crypto_ecc.lo
  CC       crypto_ecc_setup.lo
  CC       crypto_hash.lo
  CC       crypto_hash_file.lo
  CC       crypto_hkdf.lo
  CC       crypto_kdf.lo
  CC       crypto_mpi.lo
  CC       crypto_paillier.lo
  CC       crypto_pow.lo
  CC       crypto_random.lo
  CC       crypto_rsa.lo
  CC       disk.lo
  CC       dnsparser.lo
  CC       dnsstub.lo
  CC       getopt.lo
  CC       getopt_helpers.lo
  CC       helper.lo
  CC       load.lo
  CC       mst.lo
  CC       mq.lo
  CC       nc.lo
  CC       network.lo
  CC       op.lo
  CC       os_installation.lo
  CC       os_network.lo
  CC       os_priority.lo
  CC       peer.lo
  CC       plugin.lo
  CC       program.lo
  CC       regex.lo
  CC       resolver_api.lo
  CC       scheduler.lo
  CC       service.lo
  CC       signal.lo
  CC       strings.lo
  CC       time.lo
  CC       tun.lo
  CC       uri.lo
  CC       speedup.lo
  CC       proc_compat.lo
  CC       test_plugin_plug.lo
  CC       gnunet-base32.o
  CC       gnunet-config.o
  CC       gnunet-crypto-tvg.o
  CC       gnunet-resolver.o
  CC       gnunet-ecc.o
  CC       gnunet-scrypt.o
  CC       gnunet-uri.o
  CC       gnunet-service-resolver.o
  CC       gnunet-timeout.o
  CC       gnunet-config-diff.o
  CC       test_common_logging_dummy.o
  CCLD     libgnunetutil.la
  CCLD     libgnunet_plugin_test.la
  CCLD     gnunet-base32
  CCLD     gnunet-config
  CCLD     gnunet-crypto-tvg
  CCLD     gnunet-resolver
  CCLD     gnunet-ecc
  CCLD     gnunet-scrypt
  CCLD     gnunet-uri
  CCLD     gnunet-service-resolver
  CCLD     gnunet-timeout
  CCLD     gnunet-config-diff
  CCLD     test_common_logging_dummy
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util'
Making all in nt
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nt'
  CC       nt.lo
  CCLD     libgnunetnt.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nt'
Making all in hello
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hello'
  CC       hello.lo
  CC       address.lo
  CC       hello-ng.lo
  CC       gnunet-hello.o
  CCLD     libgnunethello.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-hello
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hello'
Making all in block
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/block'
  CC       block.lo
  CC       bg_bf.lo
  CC       plugin_block_template.lo
  CC       plugin_block_test.lo
  CCLD     libgnunetblock.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunetblockgroup.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_block_template.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CCLD     libgnunet_plugin_block_test.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/block'
Making all in statistics
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics'
  CC       statistics_api.lo
  CC       gnunet-statistics.o
  CC       gnunet-service-statistics.o
  CCLD     libgnunetstatistics.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-statistics
  CCLD     gnunet-service-statistics
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics'
Making all in arm
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/arm'
  CC       arm_api.lo
  CC       arm_monitor_api.lo
  CC       gnunet-arm.o
  CC       gnunet-service-arm.o
  CC       mockup-service.o
  CCLD     libgnunetarm.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-service-arm
  CCLD     mockup-service
  CCLD     gnunet-arm
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/arm'
Making all in testing
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/testing'
  CC       testing.lo
  CC       testing_api_cmd_batch.lo
  CC       testing_api_cmd_hello_world.lo
  CC       testing_api_cmd_hello_world_birth.lo
  CC       testing_api_loop.lo
  CC       testing_api_trait_cmd.lo
  CC       testing_api_trait_process.lo
  CC       testing_api_traits.lo
  CC       gnunet-testing.o
  CC       list-keys.o
  CCLD     libgnunettesting.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     list-keys
  CCLD     gnunet-testing
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/testing'
Making all in json
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/json'
  CC       libgnunetjson_la-json.lo
  CC       libgnunetjson_la-json_mhd.lo
  CC       libgnunetjson_la-json_generator.lo
  CC       libgnunetjson_la-json_helper.lo
  CCLD     libgnunetjson.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/json'
Making all in curl
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/curl'
  CC       libgnunetcurl_la-curl.lo
  CC       libgnunetcurl_la-curl_reschedule.lo
  CCLD     libgnunetcurl.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/curl'
Making all in rest
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/rest'
  CC       libgnunetrest_la-rest.lo
  CC       libgnunet_plugin_rest_copying_la-plugin_rest_copying.lo
  CC       libgnunet_plugin_rest_config_la-plugin_rest_config.lo
  CC       gnunet_rest_server-gnunet-rest-server.o
  CCLD     libgnunetrest.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-rest-server
  CCLD     libgnunet_plugin_rest_copying.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_rest_config.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/rest'
Making all in peerinfo
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/peerinfo'
  CC       peerinfo_api.lo
  CC       peerinfo_api_notify.lo
  CC       gnunet-service-peerinfo.o
  CCLD     libgnunetpeerinfo.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-service-peerinfo
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/peerinfo'
Making all in sq
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/sq'
  CC       sq.lo
  CC       sq_exec.lo
  CC       sq_prepare.lo
  CC       sq_query_helper.lo
  CC       sq_result_helper.lo
  CCLD     libgnunetsq.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/sq'
Making all in pq
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/pq'
  CC       pq.lo
  CC       pq_connect.lo
  CC       pq_eval.lo
  CC       pq_exec.lo
  CC       pq_prepare.lo
  CC       pq_query_helper.lo
  CC       pq_result_helper.lo
  CCLD     libgnunetpq.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/pq'
Making all in datacache
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/datacache'
  CC       datacache.lo
  CC       plugin_datacache_template.lo
  CC       plugin_datacache_sqlite.lo
  CC       libgnunet_plugin_datacache_postgres_la-plugin_datacache_postgres.lo
  CC       plugin_datacache_heap.lo
  CCLD     libgnunetdatacache.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_datacache_template.la
  CCLD     libgnunet_plugin_datacache_sqlite.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CCLD     libgnunet_plugin_datacache_postgres.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_datacache_heap.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/datacache'
Making all in datastore
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/datastore'
  CC       datastore_api.lo
  CC       plugin_datastore_template.lo
  CC       plugin_datastore_sqlite.lo
  CC       libgnunet_plugin_datastore_postgres_la-plugin_datastore_postgres.lo
  CC       plugin_datastore_heap.lo
  CC       gnunet-datastore.o
  CC       gnunet-service-datastore.o
  CCLD     libgnunetdatastore.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_datastore_template.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CCLD     libgnunet_plugin_datastore_sqlite.la
  CCLD     libgnunet_plugin_datastore_postgres.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_datastore_heap.la
  CCLD     gnunet-datastore
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-service-datastore
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/datastore'
Making all in template
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/template'
  CC       gnunet-template.o
  CC       gnunet-service-template.o
  CCLD     gnunet-template
  CCLD     gnunet-service-template
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/template'
Making all in peerstore
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/peerstore'
  CC       peerstore_api.lo
  CC       peerstore_common.lo
  CC       plugin_peerstore_sqlite.lo
In file included from ../../src/include/gnunet_crypto_lib.h:60,
                 from ../../src/include/gnunet_util_lib.h:64,
                 from peerstore_api.c:27:
peerstore_api.c: In function 'GNUNET_PEERSTORE_store':
peerstore_api.c:537:8: warning: format '%lu' expects argument of type 'long unsigned int', but argument 4 has type 'size_t' {aka 'unsigned int'} [-Wformat=]
        "Storing value (size: %lu) for subsytem `%s', peer `%s', key `%s'\n",
        ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        size,
        ~~~~
../../src/include/gnunet_common.h:521:50: note: in definition of macro 'GNUNET_log_from'
           GNUNET_log_from_nocheck ((kind), comp, __VA_ARGS__);            \
                                                  ^~~~~~~~~~~
peerstore_api.c:536:3: note: in expansion of macro 'LOG'
   LOG (GNUNET_ERROR_TYPE_DEBUG,
   ^~~
  CC       plugin_peerstore_flat.lo
  CC       gnunet-peerstore.o
  CC       gnunet_service_peerstore-gnunet-service-peerstore.o
  CC       gnunet_service_peerstore-peerstore_common.o
  CCLD     libgnunetpeerstore.la
  CCLD     gnunet-service-peerstore
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_peerstore_sqlite.la
  CCLD     libgnunet_plugin_peerstore_flat.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-peerstore
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/peerstore'
Making all in ats
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats'
  CC       ats_api_connectivity.lo
  CC       ats_api_scheduling.lo
  CC       ats_api_scanner.lo
  CC       ats_api_performance.lo
  CC       plugin_ats_proportional.lo
  CC       gnunet-service-ats.o
  CC       gnunet-service-ats_addresses.o
  CC       gnunet-service-ats_connectivity.o
  CC       gnunet-service-ats_normalization.o
  CC       gnunet-service-ats_performance.o
  CC       gnunet-service-ats_plugins.o
  CC       gnunet-service-ats_preferences.o
  CC       gnunet-service-ats_scheduling.o
  CC       gnunet-service-ats_reservations.o
  CCLD     libgnunetats.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_ats_proportional.la
  CCLD     gnunet-service-ats
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats'
Making all in nat
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nat'
  CC       nat_api.lo
  CC       nat_api_stun.lo
  CC       gnunet-nat.o
  CC       gnunet-helper-nat-server.o
  CC       gnunet-helper-nat-client.o
  CC       gnunet-service-nat.o
  CC       gnunet-service-nat_externalip.o
  CC       gnunet-service-nat_stun.o
  CC       gnunet-service-nat_mini.o
  CC       gnunet-service-nat_helper.o
  CCLD     libgnunetnatnew.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-helper-nat-server
  CCLD     gnunet-helper-nat-client
  CCLD     gnunet-service-nat
  CCLD     gnunet-nat
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nat'
Making all in nat-auto
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nat-auto'
  CC       nat_auto_api.lo
  CC       nat_auto_api_test.lo
  CC       gnunet-nat-auto.o
  CC       gnunet-nat-server.o
  CC       gnunet-service-nat-auto.o
  CCLD     libgnunetnatauto.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-nat-server
  CCLD     gnunet-service-nat-auto
  CCLD     gnunet-nat-auto
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nat-auto'
Making all in fragmentation
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/fragmentation'
  CC       fragmentation.lo
  CC       defragmentation.lo
  CCLD     libgnunetfragmentation.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/fragmentation'
Making all in transport
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/transport'
  CC       transport_api_address_to_string.lo
  CC       transport_api_blacklist.lo
  CC       transport_api_core.lo
  CC       transport_api_hello_get.lo
  CC       transport_api_manipulation.lo
  CC       transport_api_monitor_peers.lo
  CC       transport_api_monitor_plugins.lo
  CC       transport_api_offer_hello.lo
  CC       transport_api2_application.lo
  CC       transport_api2_core.lo
  CC       transport_api2_communication.lo
  CC       transport_api2_monitor.lo
  CC       transport-testing.lo
  CC       transport-testing-filenames.lo
  CC       transport-testing-loggers.lo
  CC       transport-testing-main.lo
  CC       transport-testing-send.lo
  CC       transport-testing2.lo
  CC       transport-testing-filenames2.lo
  CC       transport-testing-loggers2.lo
  CC       transport-testing-main2.lo
  CC       transport-testing-send2.lo
  CC       transport-testing-communicator.lo
  CC       plugin_transport_template.lo
  CC       plugin_transport_tcp.lo
  CC       plugin_transport_unix.lo
  CC       libgnunet_plugin_transport_http_client_la-plugin_transport_http_client.lo
  CC       libgnunet_plugin_transport_http_client_la-plugin_transport_http_common.lo
  CC       libgnunet_plugin_transport_https_client_la-plugin_transport_http_client.lo
  CC       libgnunet_plugin_transport_https_client_la-plugin_transport_http_common.lo
  CC       libgnunet_plugin_transport_http_server_la-plugin_transport_http_server.lo
  CC       libgnunet_plugin_transport_http_server_la-plugin_transport_http_common.lo
  CC       libgnunet_plugin_transport_https_server_la-plugin_transport_http_server.lo
  CC       libgnunet_plugin_transport_https_server_la-plugin_transport_http_common.lo
  CC       libgnunet_plugin_transport_wlan_la-plugin_transport_wlan.lo
  CC       libgnunet_plugin_transport_bluetooth_la-plugin_transport_wlan.lo
  CC       plugin_transport_udp.lo
  CC       plugin_transport_udp_broadcasting.lo
  CC       gnunet-transport.o
  CC       gnunet-helper-transport-wlan.o
plugin_transport_udp.c: In function 'udp_select_send':
plugin_transport_udp.c:3135:5: warning: 'session' may be used uninitialized in this function [-Wmaybe-uninitialized]
     notify_session_monitor (session->plugin,
     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                             session,
                             ~~~~~~~~
                             GNUNET_TRANSPORT_SS_UPDATE);
                             ~~~~~~~~~~~~~~~~~~~~~~~~~~~
plugin_transport_udp.c:3072:30: note: 'session' was declared here
   struct GNUNET_ATS_Session *session;
                              ^~~~~~~
  CC       gnunet-helper-transport-wlan-dummy.o
  CC       gnunet-helper-transport-bluetooth.o
  CC       gnunet_service_transport-gnunet-service-transport.o
  CC       gnunet_service_transport-gnunet-service-transport_ats.o
  CC       gnunet_service_transport-gnunet-service-transport_hello.o
  CC       gnunet_service_transport-gnunet-service-transport_neighbours.o
  CC       gnunet_service_transport-gnunet-service-transport_plugins.o
  CC       gnunet_service_transport-gnunet-service-transport_validation.o
  CC       gnunet_service_transport-gnunet-service-transport_manipulation.o
  CC       gnunet-service-tng.o
  CC       gnunet-communicator-unix.o
  CC       gnunet-communicator-udp.o
In file included from ../../src/include/gnunet_crypto_lib.h:60,
                 from ../../src/include/gnunet_util_lib.h:64,
                 from gnunet-communicator-udp.c:41:
gnunet-communicator-udp.c: In function 'sock_read':
gnunet-communicator-udp.c:2255:15: warning: format '%lu' expects argument of type 'long unsigned int', but argument 3 has type 'ssize_t' {aka 'int'} [-Wformat=]
               "Read %lu bytes\n", rcvd);
               ^~~~~~~~~~~~~~~~~~  ~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
gnunet-communicator-udp.c: In function 'check_for_rekeying':
gnunet-communicator-udp.c:2694:15: warning: format '%lu' expects argument of type 'long unsigned int', but argument 3 has type 'uint64_t' {aka 'long long unsigned int'} [-Wformat=]
               "Timeout is %lu\n.",
               ^~~~~~~~~~~~~~~~~~~
               receiver->rekey_timeout.abs_value_us);
               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
gnunet-communicator-udp.c:2706:17: warning: format '%lu' expects argument of type 'long unsigned int', but argument 3 has type 'uint64_t' {aka 'long long unsigned int'} [-Wformat=]
                 "Relative time is %lu and timeout is %lu\n.",
                 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                 rt.rel_value_us,
                 ~~~~~~~~~~~~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
gnunet-communicator-udp.c:2706:17: warning: format '%lu' expects argument of type 'long unsigned int', but argument 4 has type 'uint64_t' {aka 'long long unsigned int'} [-Wformat=]
                 "Relative time is %lu and timeout is %lu\n.",
                 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
gnunet-communicator-udp.c:2708:17:
                 receiver->rekey_timeout.abs_value_us);
                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
gnunet-communicator-udp.c:2714:19: warning: format '%lu' expects argument of type 'long unsigned int', but argument 3 has type 'uint64_t' {aka 'long long unsigned int'} [-Wformat=]
                   "Bytes send %lu greater than %llu max bytes\n.",
                   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                   receiver->rekey_send_bytes,
                   ~~~~~~~~~~~~~~~~~~~~~~~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
gnunet-communicator-udp.c:2718:19: warning: format '%lu' expects argument of type 'long unsigned int', but argument 3 has type 'uint64_t' {aka 'long long unsigned int'} [-Wformat=]
                   "Relative time is %lu and timeout is %lu\n.",
                   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                   rt.rel_value_us,
                   ~~~~~~~~~~~~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
gnunet-communicator-udp.c:2718:19: warning: format '%lu' expects argument of type 'long unsigned int', but argument 4 has type 'uint64_t' {aka 'long long unsigned int'} [-Wformat=]
                   "Relative time is %lu and timeout is %lu\n.",
                   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
gnunet-communicator-udp.c:2720:19:
                   receiver->rekey_timeout.abs_value_us);
                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
gnunet-communicator-udp.c: In function 'mq_send_d':
gnunet-communicator-udp.c:2879:17: warning: format '%lu' expects argument of type 'long unsigned int', but argument 4 has type 'size_t' {aka 'unsigned int'} [-Wformat=]
                 "msize: %u, mtu: %lu, acks: %u\n",
                 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
gnunet-communicator-udp.c:2881:17:
                 receiver->d_mtu,
                 ~~~~~~~~~~~~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
  CC       gnunet-communicator-tcp.o
In file included from ../../src/include/gnunet_crypto_lib.h:60,
                 from ../../src/include/gnunet_util_lib.h:64,
                 from gnunet-service-tng.c:76:
gnunet-service-tng.c: In function 'handle_send_message_ack':
gnunet-service-tng.c:9072:19: warning: format '%lu' expects argument of type 'long unsigned int', but argument 3 has type 'uint64_t' {aka 'long long unsigned int'} [-Wformat=]
                   "QueueEntry MID: %lu, Ack MID: %lu\n",
                   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                   qep->mid, sma->mid);
                   ~~~~~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
gnunet-service-tng.c:9072:19: warning: format '%lu' expects argument of type 'long unsigned int', but argument 4 has type 'uint64_t' {aka 'const long long unsigned int'} [-Wformat=]
                   "QueueEntry MID: %lu, Ack MID: %lu\n",
                   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                   qep->mid, sma->mid);
                             ~~~~~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
  CC       gnunet-transport-profiler.o
In file included from ../../src/include/gnunet_crypto_lib.h:60,
                 from ../../src/include/gnunet_util_lib.h:64,
                 from gnunet-communicator-tcp.c:31:
gnunet-communicator-tcp.c: In function 'queue_write':
gnunet-communicator-tcp.c:1580:17: warning: format '%lu' expects argument of type 'long unsigned int', but argument 3 has type 'ssize_t' {aka 'int'} [-Wformat=]
                 "Sent %lu bytes to TCP queue\n", sent);
                 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  ~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
gnunet-communicator-tcp.c:1604:17: warning: format '%lu' expects argument of type 'long unsigned int', but argument 3 has type 'size_t' {aka 'unsigned int'} [-Wformat=]
                 "Encrypting %lu bytes\n", queue->pwrite_off);
                 ^~~~~~~~~~~~~~~~~~~~~~~~  ~~~~~~~~~~~~~~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
gnunet-communicator-tcp.c: In function 'try_handle_plaintext':
gnunet-communicator-tcp.c:1689:17: warning: format '%lu' expects argument of type 'long unsigned int', but argument 3 has type 'size_t' {aka 'unsigned int'} [-Wformat=]
                 "Already received data of size %lu bigger than KX size %lu!\n",
                 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                 unverified_size,
                 ~~~~~~~~~~~~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
gnunet-communicator-tcp.c:1689:17: warning: format '%lu' expects argument of type 'long unsigned int', but argument 4 has type 'unsigned int' [-Wformat=]
                 "Already received data of size %lu bigger than KX size %lu!\n",
                 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
gnunet-communicator-tcp.c: In function 'queue_read':
gnunet-communicator-tcp.c:1902:15: warning: format '%lu' expects argument of type 'long unsigned int', but argument 3 has type 'ssize_t' {aka 'int'} [-Wformat=]
               "Received %lu bytes from TCP queue\n", rcvd);
               ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  ~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
gnunet-communicator-tcp.c: In function 'mq_send':
gnunet-communicator-tcp.c:2330:15: warning: format '%lu' expects argument of type 'long unsigned int', but argument 3 has type 'size_t' {aka 'unsigned int'} [-Wformat=]
               "%lu bytes of plaintext to send\n", queue->pwrite_off);
               ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  ~~~~~~~~~~~~~~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
gnunet-communicator-tcp.c: In function 'proto_read_kx':
gnunet-communicator-tcp.c:2706:15: warning: format '%lu' expects argument of type 'long unsigned int', but argument 3 has type 'ssize_t' {aka 'int'} [-Wformat=]
               "Received %lu bytes for KX\n", rcvd);
               ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~  ~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
gnunet-communicator-tcp.c: In function 'queue_read_kx':
gnunet-communicator-tcp.c:2854:15: warning: format '%lu' expects argument of type 'long unsigned int', but argument 3 has type 'ssize_t' {aka 'int'} [-Wformat=]
               "Received %lu bytes for KX\n",
               ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
               rcvd);
               ~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
gnunet-communicator-tcp.c:2911:15: warning: format '%lu' expects argument of type 'long unsigned int', but argument 3 has type 'size_t' {aka 'unsigned int'} [-Wformat=]
               "cread_off is %lu bytes before adjusting\n",
               ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
               queue->cread_off);
               ~~~~~~~~~~~~~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
gnunet-communicator-tcp.c:2915:15: warning: format '%lu' expects argument of type 'long unsigned int', but argument 3 has type 'size_t' {aka 'unsigned int'} [-Wformat=]
               "cread_off set to %lu bytes\n",
               ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
               queue->cread_off);
               ~~~~~~~~~~~~~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
  CC       gnunet-transport-wlan-sender.o
  CC       gnunet-transport-wlan-receiver.o
sed -e 's,[@]pkgdatadir[@],/usr/share/gnunet,g' < ./gnunet-transport-certificate-creation.in > gnunet-transport-certificate-creation
chmod +x gnunet-transport-certificate-creation
  CCLD     libgnunettransport.la
  CCLD     libgnunettransportapplication.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunettransportcore.la
  CCLD     libgnunettransportcommunicator.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunettransportmonitor.la
  CCLD     libgnunettransporttesting.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunettransporttesting2.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_transport_template.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CCLD     libgnunet_plugin_transport_tcp.la
  CCLD     libgnunet_plugin_transport_unix.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_transport_http_client.la
  CCLD     libgnunet_plugin_transport_https_client.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_transport_http_server.la
  CCLD     libgnunet_plugin_transport_https_server.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_transport_wlan.la
  CCLD     libgnunet_plugin_transport_bluetooth.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_transport_udp.la
  CCLD     gnunet-transport
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-helper-transport-wlan
  CCLD     gnunet-helper-transport-wlan-dummy
  CCLD     gnunet-helper-transport-bluetooth
  CCLD     gnunet-service-transport
  CCLD     gnunet-service-tng
  CCLD     gnunet-communicator-unix
  CCLD     gnunet-communicator-udp
  CCLD     gnunet-communicator-tcp
  CCLD     gnunet-transport-profiler
  CCLD     gnunet-transport-wlan-sender
  CCLD     gnunet-transport-wlan-receiver
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/transport'
Making all in ats-tool
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats-tool'
  CC       gnunet-ats.o
  CCLD     gnunet-ats
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats-tool'
Making all in core
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/core'
  CC       core_api.lo
  CC       core_api_monitor_peers.lo
  CC       gnunet-core.o
  CC       gnunet-service-core.o
  CC       gnunet-service-core_kx.o
  CC       gnunet-service-core_sessions.o
  CC       gnunet-service-core_typemap.o
  CCLD     libgnunetcore.la
  CCLD     gnunet-service-core
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-core
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/core'
Making all in testbed-logger
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/testbed-logger'
  CC       testbed_logger_api.lo
  CC       gnunet-service-testbed-logger.o
  CCLD     gnunet-service-testbed-logger
  CCLD     libgnunettestbedlogger.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/testbed-logger'
Making all in testbed
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/testbed'
  CC       testbed_api.lo
  CC       testbed_api_hosts.lo
  CC       testbed_api_cmd_controller.lo
  CC       testbed_api_cmd_peer.lo
  CC       testbed_api_cmd_service.lo
  CC       testbed_api_operations.lo
testbed_api_cmd_service.c:47:1: warning: 'do_abort' defined but not used [-Wunused-function]
 do_abort (void *cls)
 ^~~~~~~~
  CC       testbed_api_peers.lo
  CC       testbed_api_services.lo
  CC       testbed_api_statistics.lo
  CC       testbed_api_testbed.lo
  CC       testbed_api_test.lo
  CC       testbed_api_topology.lo
  CC       testbed_api_sd.lo
  CC       testbed_api_barriers.lo
  CC       gnunet-testbed-profiler.o
  CC       gnunet-service-testbed.o
  CC       gnunet-service-testbed_links.o
  CC       gnunet-service-testbed_peers.o
  CC       gnunet-service-testbed_cache.o
  CC       gnunet-service-testbed_oc.o
  CC       gnunet-service-testbed_cpustatus.o
  CC       gnunet-service-testbed_meminfo.o
  CC       gnunet-service-testbed_barriers.o
  CC       gnunet-service-testbed_connectionpool.o
  CC       gnunet-helper-testbed.o
  CC       gnunet-daemon-testbed-blacklist.o
  CC       gnunet-daemon-testbed-underlay.o
  CC       gnunet-daemon-latency-logger.o
  CC       generate-underlay-topology.o
  CCLD     libgnunettestbed.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-daemon-testbed-blacklist
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-daemon-testbed-underlay
  CCLD     gnunet-daemon-latency-logger
  CCLD     generate-underlay-topology
  CCLD     gnunet-testbed-profiler
  CCLD     gnunet-service-testbed
  CCLD     gnunet-helper-testbed
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/testbed'
Making all in ats-tests
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats-tests'
  CC       ats-testing.lo
  CC       ats-testing-log.lo
  CC       ats-testing-traffic.lo
  CC       ats-testing-experiment.lo
  CC       ats-testing-preferences.lo
  CC       gnunet-ats-sim.o
  CC       gnunet-solver-eval.o
  CCLD     libgnunetatstesting.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-solver-eval
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-ats-sim
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats-tests'
Making all in nse
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nse'
  CC       nse_api.lo
  CC       gnunet-nse.o
  CC       gnunet-service-nse.o
  CC       gnunet-nse-profiler.o
  CCLD     libgnunetnse.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-nse
  CCLD     gnunet-service-nse
  CCLD     gnunet-nse-profiler
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nse'
Making all in dht
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/dht'
  CC       dht_test_lib.o
  CC       dht_api.lo
  CC       plugin_block_dht.lo
  CC       gnunet-dht-monitor.o
  CC       gnunet-dht-get.o
  CC       gnunet-dht-put.o
  CC       gnunet-service-dht.o
  CC       gnunet-service-dht_datacache.o
  CC       gnunet-service-dht_hello.o
  CC       gnunet-service-dht_nse.o
  CC       gnunet-service-dht_neighbours.o
  CC       gnunet-service-dht_routing.o
  CC       gnunet_dht_profiler.o
  CCLD     libgnunetdht.la
  CCLD     libgnunet_plugin_block_dht.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-service-dht
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-dht-profiler
  AR       libgnunetdhttest.a
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CCLD     gnunet-dht-monitor
  CCLD     gnunet-dht-get
  CCLD     gnunet-dht-put
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/dht'
Making all in hostlist
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hostlist'
  CC       gnunet_daemon_hostlist-gnunet-daemon-hostlist.o
  CC       gnunet_daemon_hostlist-gnunet-daemon-hostlist_client.o
  CC       gnunet_daemon_hostlist-gnunet-daemon-hostlist_server.o
  CCLD     gnunet-daemon-hostlist
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hostlist'
Making all in topology
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/topology'
  CC       friends.lo
  CC       gnunet-daemon-topology.o
  CCLD     libgnunetfriends.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-daemon-topology
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/topology'
Making all in regex
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/regex'
  CC       regex_internal.o
  CC       regex_internal_dht.o
In file included from ../../src/include/gnunet_crypto_lib.h:60,
                 from ../../src/include/gnunet_util_lib.h:64,
                 from regex_internal_lib.h:29,
                 from regex_internal_dht.c:27:
regex_internal_dht.c: In function 'regex_result_iterator':
regex_internal_dht.c:536:8: warning: format '%lu' expects argument of type 'long unsigned int', but argument 5 has type 'size_t' {aka 'unsigned int'} [-Wformat=]
        "* %lu, %lu, [%u]\n",
        ^~~~~~~~~~~~~~~~~~~~
regex_internal_dht.c:538:8:
        strlen (ctx->info->description),
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
../../src/include/gnunet_common.h:521:50: note: in definition of macro 'GNUNET_log_from'
           GNUNET_log_from_nocheck ((kind), comp, __VA_ARGS__);            \
                                                  ^~~~~~~~~~~
regex_internal_dht.c:535:3: note: in expansion of macro 'LOG'
   LOG (GNUNET_ERROR_TYPE_DEBUG,
   ^~~
  CC       regex_block_lib.lo
  CC       regex_test_lib.o
regex_test_lib.c:102:1: warning: 'space' defined but not used [-Wunused-function]
 space (int n)
 ^~~~~
  CC       regex_test_graph.o
  CC       regex_test_random.o
  CC       regex_api_announce.lo
  CC       regex_api_search.lo
  CC       plugin_block_regex.lo
  CC       gnunet-service-regex.o
  CC       gnunet-daemon-regexprofiler.o
  CC       perf-regex.o
  CC       gnunet-regex-profiler.o
  CCLD     libgnunetregexblock.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunetregex.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_block_regex.la
  AR       libgnunetregex_internal.a
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  AR       libgnunetregextest.a
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CCLD     gnunet-service-regex
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-daemon-regexprofiler
  CCLD     perf-regex
  CCLD     gnunet-regex-profiler
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/regex'
Making all in dns
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/dns'
  CC       dns_api.lo
  CC       plugin_block_dns.lo
  CC       gnunet-service-dns.o
  CC       gnunet-helper-dns.o
  CC       gnunet-dns-monitor.o
  CC       gnunet-dns-redirector.o
  CC       gnunet-zonewalk.o
  CCLD     libgnunetdns.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_block_dns.la
  CCLD     gnunet-service-dns
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-helper-dns
  CCLD     gnunet-dns-monitor
  CCLD     gnunet-dns-redirector
  CCLD     gnunet-zonewalk
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/dns'
Making all in identity
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/identity'
  CC       identity_api.lo
  CC       identity_api_lookup.lo
  CC       identity_api_suffix_lookup.lo
  CC       libgnunet_plugin_rest_identity_la-plugin_rest_identity.lo
  CC       gnunet-identity.o
  CC       gnunet-service-identity.o
  CCLD     libgnunetidentity.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_rest_identity.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-identity
  CCLD     gnunet-service-identity
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/identity'
Making all in gnsrecord
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gnsrecord'
  CC       gnsrecord.lo
  CC       gnsrecord_serialization.lo
  CC       gnsrecord_crypto.lo
  CC       gnsrecord_misc.lo
In file included from ../../src/include/gnunet_crypto_lib.h:60,
                 from ../../src/include/gnunet_util_lib.h:64,
                 from gnsrecord_misc.c:29:
gnsrecord_misc.c: In function 'GNUNET_GNSRECORD_records_cmp':
gnsrecord_misc.c:126:10: warning: format '%lu' expects argument of type 'long unsigned int', but argument 4 has type 'size_t' {aka 'const unsigned int'} [-Wformat=]
          "Data size %lu != %lu\n",
          ^~~~~~~~~~~~~~~~~~~~~~~~
          a->data_size,
          ~~~~~~~~~~~~
../../src/include/gnunet_common.h:521:50: note: in definition of macro 'GNUNET_log_from'
           GNUNET_log_from_nocheck ((kind), comp, __VA_ARGS__);            \
                                                  ^~~~~~~~~~~
gnsrecord_misc.c:125:5: note: in expansion of macro 'LOG'
     LOG (GNUNET_ERROR_TYPE_DEBUG,
     ^~~
gnsrecord_misc.c:126:10: warning: format '%lu' expects argument of type 'long unsigned int', but argument 5 has type 'size_t' {aka 'const unsigned int'} [-Wformat=]
          "Data size %lu != %lu\n",
          ^~~~~~~~~~~~~~~~~~~~~~~~
gnsrecord_misc.c:128:10:
          b->data_size);
          ~~~~~~~~~~~~
../../src/include/gnunet_common.h:521:50: note: in definition of macro 'GNUNET_log_from'
           GNUNET_log_from_nocheck ((kind), comp, __VA_ARGS__);            \
                                                  ^~~~~~~~~~~
gnsrecord_misc.c:125:5: note: in expansion of macro 'LOG'
     LOG (GNUNET_ERROR_TYPE_DEBUG,
     ^~~
  CC       json_gnsrecord.lo
  CC       plugin_gnsrecord_dns.lo
  CC       gnunet-gnsrecord-tvg.o
  CCLD     libgnunetgnsrecord.la
  CCLD     libgnunet_plugin_gnsrecord_dns.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunetgnsrecordjson.la
  CCLD     gnunet-gnsrecord-tvg
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gnsrecord'
Making all in namecache
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/namecache'
  CC       namecache_api.lo
  CC       plugin_namecache_sqlite.lo
  CC       plugin_namecache_flat.lo
  CC       plugin_namecache_postgres.lo
  CC       gnunet-namecache.o
  CC       gnunet-service-namecache.o
  CCLD     libgnunetnamecache.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_namecache_sqlite.la
  CCLD     libgnunet_plugin_namecache_flat.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_namecache_postgres.la
  CCLD     gnunet-namecache
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-service-namecache
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/namecache'
Making all in namestore
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/namestore'
  CC       namestore_api.lo
  CC       namestore_api_monitor.lo
  CC       plugin_namestore_sqlite.lo
  CC       plugin_namestore_postgres.lo
  CC       plugin_namestore_flat.lo
  CC       libgnunet_plugin_rest_namestore_la-plugin_rest_namestore.lo
  CC       gnunet-namestore.o
  CC       gnunet-zoneimport.o
  CC       gnunet-service-namestore.o
  CC       gnunet_namestore_fcfsd-gnunet-namestore-fcfsd.o
  CCLD     libgnunetnamestore.la
  CCLD     libgnunet_plugin_namestore_sqlite.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_namestore_postgres.la
  CCLD     libgnunet_plugin_namestore_flat.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_rest_namestore.la
  CCLD     gnunet-namestore
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-zoneimport
  CCLD     gnunet-service-namestore
  CCLD     gnunet-namestore-fcfsd
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/namestore'
Making all in peerinfo-tool
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/peerinfo-tool'
  CC       libgnunet_plugin_rest_peerinfo_la-plugin_rest_peerinfo.lo
  CC       gnunet-peerinfo.o
  CC       gnunet-peerinfo_plugins.o
  CCLD     libgnunet_plugin_rest_peerinfo.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-peerinfo
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/peerinfo-tool'
Making all in cadet
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/cadet'
  CC       cadet_api.lo
  CC       cadet_api_drop_message.lo
  CC       cadet_api_get_channel.lo
  CC       cadet_api_get_path.lo
  CC       cadet_api_list_peers.lo
  CC       cadet_api_list_tunnels.lo
  CC       cadet_api_helper.lo
  CC       cadet_test_lib.lo
  CC       gnunet-cadet.o
  CC       gnunet-service-cadet.o
  CC       gnunet-service-cadet_channel.o
  CC       gnunet-service-cadet_connection.o
  CC       gnunet-service-cadet_core.o
  CC       gnunet-service-cadet_dht.o
  CC       gnunet-service-cadet_hello.o
  CC       gnunet-service-cadet_tunnels.o
  CC       gnunet-service-cadet_paths.o
  CC       gnunet-service-cadet_peer.o
  CCLD     libgnunetcadet.la
  CCLD     gnunet-service-cadet
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunetcadettest.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CCLD     gnunet-cadet
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/cadet'
Making all in set
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/set'
  CC       set_api.lo
  CC       plugin_block_set_test.lo
  CC       gnunet-set-profiler.o
  CC       gnunet-service-set.o
  CC       gnunet-service-set_union.o
  CC       gnunet-service-set_intersection.o
  CC       ibf.o
  CC       gnunet-service-set_union_strata_estimator.o
  CC       gnunet-set-ibf-profiler.o
  CCLD     libgnunetset.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_block_set_test.la
  CCLD     gnunet-set-ibf-profiler
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-set-profiler
  CCLD     gnunet-service-set
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/set'
Making all in seti
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/seti'
  CC       seti_api.lo
  CC       plugin_block_seti_test.lo
  CC       gnunet-seti-profiler.o
  CC       gnunet-service-seti.o
  CCLD     libgnunetseti.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_block_seti_test.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-seti-profiler
  CCLD     gnunet-service-seti
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/seti'
Making all in setu
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/setu'
  CC       setu_api.lo
  CC       plugin_block_setu_test.lo
  CC       gnunet-setu-profiler.o
  CC       gnunet-service-setu.o
  CC       ibf.o
  CC       gnunet-service-setu_strata_estimator.o
  CC       gnunet-setu-ibf-profiler.o
  CCLD     libgnunetsetu.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_block_setu_test.la
  CCLD     gnunet-setu-ibf-profiler
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-setu-profiler
  CCLD     gnunet-service-setu
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/setu'
Making all in consensus
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/consensus'
  CC       consensus_api.lo
  CC       plugin_block_consensus.lo
  CC       gnunet-consensus-profiler.o
  CC       gnunet-service-consensus.o
  CC       gnunet_service_evil_consensus-gnunet-service-consensus.o
gawk -v bdir="/usr/bin" -v py="/openwrt/staging_dir/hostpkg/bin/python3" -v awkay="/openwrt/staging_dir/host/bin/awk" -v pfx="/usr" -v prl="/openwrt/staging_dir/host/bin/perl" -v sysconfdirectory="/etc" -v pkgdatadirectory="/usr/share/gnunet" -f ../../bin/dosubst.awk < consensus-simulation.py.in > consensus-simulation.py
chmod +x consensus-simulation.py
  CCLD     libgnunetconsensus.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_block_consensus.la
  CCLD     gnunet-consensus-profiler
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-service-consensus
  CCLD     gnunet-service-evil-consensus
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/consensus'
Making all in revocation
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/revocation'
  CC       revocation_api.lo
  CC       plugin_block_revocation.lo
  CC       gnunet-revocation.o
  CC       gnunet-revocation-tvg.o
  CC       gnunet-service-revocation.o
  CCLD     libgnunetrevocation.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_block_revocation.la
  CCLD     gnunet-revocation
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-revocation-tvg
  CCLD     gnunet-service-revocation
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/revocation'
Making all in vpn
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/vpn'
  CC       vpn_api.lo
  CC       gnunet-vpn.o
  CC       gnunet-helper-vpn.o
  CC       gnunet_service_vpn-gnunet-service-vpn.o
  CCLD     libgnunetvpn.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-helper-vpn
  CCLD     gnunet-vpn
cc1: note: someone does not honour COPTS correctly, passed 2 times
  CCLD     gnunet-service-vpn
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/vpn'
Making all in gns
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gns'
Making all in .
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gns'
  CC       gns_api.lo
  CC       gns_tld_api.lo
  CC       plugin_block_gns.lo
  CC       plugin_gnsrecord_gns.lo
  CC       libgnunet_plugin_rest_gns_la-plugin_rest_gns.lo
  CC       gnunet-gns.o
  CC       gnunet_bcd-gnunet-bcd.o
  CC       gnunet-service-gns.o
  CC       gnunet-service-gns_resolver.o
  CC       gnunet-service-gns_interceptor.o
  CC       gnunet-dns2gns.o
  CC       gnunet-gns-benchmark.o
In file included from ../../src/include/gnunet_crypto_lib.h:60,
                 from ../../src/include/gnunet_util_lib.h:64,
                 from gnunet-service-gns_resolver.c:41:
gnunet-service-gns_resolver.c: In function 'handle_dht_response':
gnunet-service-gns_resolver.c:2501:15: warning: format '%lu' expects argument of type 'long unsigned int', but argument 3 has type 'size_t' {aka 'unsigned int'} [-Wformat=]
               "Decrypting DHT block of size %lu for `%s', expires %s\n",
               ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
               GNUNET_GNSRECORD_block_get_size (block),
               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
gawk -v bdir="/usr/bin" -v py="/openwrt/staging_dir/hostpkg/bin/python3" -v awkay="/openwrt/staging_dir/host/bin/awk" -v pfx="/usr" -v prl="/openwrt/staging_dir/host/bin/perl" -v sysconfdirectory="/etc" -v pkgdatadirectory="/usr/share/gnunet" -f ../../bin/dosubst.awk < ./gnunet-gns-proxy-setup-ca.in > gnunet-gns-proxy-setup-ca
  CCLD     libgnunetgns.la
  CCLD     libgnunet_plugin_block_gns.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_gnsrecord_gns.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_rest_gns.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-gns
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-bcd
  CCLD     gnunet-service-gns
  CCLD     gnunet-dns2gns
  CCLD     gnunet-gns-benchmark
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gns'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gns'
Making all in zonemaster
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/zonemaster'
  CC       gnunet-service-zonemaster.o
  CC       gnunet-service-zonemaster-monitor.o
  CCLD     gnunet-service-zonemaster-monitor
  CCLD     gnunet-service-zonemaster
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/zonemaster'
Making all in conversation
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/conversation'
Making all in .
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/conversation'
  CC       microphone.lo
  CC       speaker.lo
  CC       conversation_api.lo
  CC       conversation_api_call.lo
  CC       plugin_gnsrecord_conversation.lo
  CC       gnunet-conversation-test.o
  CC       gnunet-conversation.o
  CC       gnunet-service-conversation.o
  CC       gnunet_helper_audio_record-gnunet-helper-audio-record-gst.o
  CC       gnunet_helper_audio_playback-gnunet-helper-audio-playback-gst.o
  CCLD     libgnunetmicrophone.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
gnunet-helper-audio-playback-gst.c: In function 'feed_buffer_to_gst':
gnunet-helper-audio-playback-gst.c:183:3: warning: 'g_memdup' is deprecated: Use 'g_memdup2' instead [-Wdeprecated-declarations]
   bufspace = g_memdup (audio, b_len);
   ^~~~~~~~
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/glib-2.0/glib.h:82,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/gstreamer-1.0/gst/gst.h:27,
                 from gnunet-helper-audio-playback-gst.c:32:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/glib-2.0/glib/gstrfuncs.h:257:23: note: declared here
 gpointer              g_memdup         (gconstpointer mem,
                       ^~~~~~~~
  CCLD     libgnunetspeaker.la
  CCLD     libgnunetconversation.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_gnsrecord_conversation.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-conversation-test
  CCLD     gnunet-helper-audio-record
  CCLD     gnunet-helper-audio-playback
  CCLD     gnunet-conversation
  CCLD     gnunet-service-conversation
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/conversation'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/conversation'
Making all in fs
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/fs'
  CC       fs_test_lib.o
  CC       fs_api.lo
  CC       fs_directory.lo
  CC       fs_dirmetascan.lo
  CC       fs_download.lo
  CC       fs_file_information.lo
  CC       fs_getopt.lo
  CC       fs_list_indexed.lo
In file included from ../../src/include/platform.h:180,
                 from fs_download.c:25:
fs_download.c: In function 'process_result_with_request':
../../src/include/gettext.h:46:53: warning: format '%lu' expects argument of type 'long unsigned int', but argument 3 has type 'size_t' {aka 'unsigned int'} [-Wformat=]
 #define dgettext(Domainname, Msgid) ((const char *) (Msgid))
                                                     ^
../../src/include/platform.h:184:19: note: in expansion of macro 'dgettext'
 #define _(String) dgettext (PACKAGE, String)
                   ^~~~~~~~
fs_download.c:1052:7: note: in expansion of macro '_'
       _ (
       ^
../../src/include/gettext.h:46:53: warning: format '%lu' expects argument of type 'long unsigned int', but argument 7 has type 'size_t' {aka 'unsigned int'} [-Wformat=]
 #define dgettext(Domainname, Msgid) ((const char *) (Msgid))
                                                     ^
../../src/include/platform.h:184:19: note: in expansion of macro 'dgettext'
 #define _(String) dgettext (PACKAGE, String)
                   ^~~~~~~~
fs_download.c:1052:7: note: in expansion of macro '_'
       _ (
       ^
  CC       fs_publish.lo
  CC       fs_publish_ksk.lo
  CC       fs_publish_ublock.lo
  CC       fs_misc.lo
  CC       fs_namespace.lo
  CC       fs_search.lo
  CC       fs_sharetree.lo
  CC       fs_tree.lo
  CC       fs_unindex.lo
  CC       fs_uri.lo
  CC       plugin_block_fs.lo
  CC       gnunet-auto-share.o
  CC       gnunet-directory.o
  CC       gnunet-download.o
  CC       gnunet-publish.o
  CC       gnunet-search.o
  CC       gnunet-fs.o
  CC       gnunet-unindex.o
  CC       gnunet-helper-fs-publish.o
  CC       gnunet-service-fs.o
  CC       gnunet-service-fs_cp.o
  CC       gnunet-service-fs_indexing.o
  CC       gnunet-service-fs_pe.o
  CC       gnunet-service-fs_pr.o
  CC       gnunet-service-fs_push.o
  CC       gnunet-service-fs_put.o
  CC       gnunet-service-fs_cadet_client.o
  CC       gnunet-service-fs_cadet_server.o
  CC       gnunet-fs-profiler.o
  CC       gnunet-daemon-fsprofiler.o
  AR       libgnunetfstest.a
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CCLD     libgnunetfs.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-auto-share
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-helper-fs-publish
  CCLD     gnunet-service-fs
  CCLD     gnunet-fs-profiler
  CCLD     gnunet-daemon-fsprofiler
  CCLD     libgnunet_plugin_block_fs.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-directory
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-download
  CCLD     gnunet-publish
  CCLD     gnunet-search
  CCLD     gnunet-fs
  CCLD     gnunet-unindex
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/fs'
Making all in exit
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/exit'
  CC       gnunet-daemon-exit.o
  CC       gnunet-helper-exit.o
  CCLD     gnunet-helper-exit
  CCLD     gnunet-daemon-exit
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/exit'
Making all in pt
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/pt'
  CC       gnunet-daemon-pt.o
  CCLD     gnunet-daemon-pt
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/pt'
Making all in secretsharing
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/secretsharing'
  CC       secretsharing_api.lo
  CC       secretsharing_common.lo
  CC       gnunet-secretsharing-profiler.o
  CC       gnunet_service_secretsharing-gnunet-service-secretsharing.o
  CC       gnunet_service_secretsharing-secretsharing_common.o
  CCLD     libgnunetsecretsharing.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-secretsharing-profiler
  CCLD     gnunet-service-secretsharing
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/secretsharing'
Making all in reclaim
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/reclaim'
  CC       reclaim_api.lo
  CC       reclaim_attribute.lo
  CC       reclaim_credential.lo
  CC       plugin_gnsrecord_reclaim.lo
  CC       plugin_reclaim_attribute_basic.lo
  CC       plugin_reclaim_credential_jwt.lo
  CC       libgnunet_plugin_rest_openid_connect_la-plugin_rest_openid_connect.lo
  CC       libgnunet_plugin_rest_openid_connect_la-oidc_helper.lo
In file included from ../../src/include/gnunet_crypto_lib.h:60,
                 from ../../src/include/gnunet_util_lib.h:64,
                 from oidc_helper.c:29:
oidc_helper.c: In function 'OIDC_build_authz_code':
oidc_helper.c:535:17: warning: format '%lu' expects argument of type 'long unsigned int', but argument 3 has type 'size_t' {aka 'unsigned int'} [-Wformat=]
                 "Length of serialized attributes: %lu\n",
                 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                 attr_list_len);
                 ~~~~~~~~~~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
oidc_helper.c:550:17: warning: format '%lu' expects argument of type 'long unsigned int', but argument 3 has type 'size_t' {aka 'unsigned int'} [-Wformat=]
                 "Length of serialized presentations: %lu\n",
                 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                 pres_list_len);
                 ~~~~~~~~~~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
oidc_helper.c:584:15: warning: format '%lu' expects argument of type 'long unsigned int', but argument 3 has type 'size_t' {aka 'unsigned int'} [-Wformat=]
               "Length of data to encode: %lu\n",
               ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
               code_payload_len);
               ~~~~~~~~~~~~~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
  CC       libgnunet_plugin_rest_reclaim_la-plugin_rest_reclaim.lo
  CC       libgnunet_plugin_rest_reclaim_la-json_reclaim.lo
  CC       gnunet-reclaim.o
  CC       gnunet-service-reclaim.o
  CC       gnunet-service-reclaim_tickets.o
  CCLD     libgnunetreclaim.la
  CCLD     libgnunet_plugin_gnsrecord_reclaim.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_reclaim_attribute_basic.la
  CCLD     libgnunet_plugin_reclaim_credential_jwt.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_rest_openid_connect.la
  CCLD     libgnunet_plugin_rest_reclaim.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-reclaim
  CCLD     gnunet-service-reclaim
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/reclaim'
Making all in rps
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/rps'
  CC       libgnunetrps_la-gnunet-service-rps_sampler_elem.lo
  CC       libgnunetrps_la-rps-test_util.lo
  CC       libgnunetrps_la-rps-sampler_common.lo
  CC       libgnunetrps_la-rps-sampler_client.lo
  CC       libgnunetrps_la-rps_api.lo
  CC       gnunet-rps.o
gnunet-rps.c: In function 'run':
gnunet-rps.c:210:35: warning: format '%lu' expects argument of type 'long unsigned int *', but argument 3 has type 'uint64_t *' {aka 'long long unsigned int *'} [-Wformat=]
         (0 == sscanf (args[0], "%lu", &num_peers)) )
                                 ~~^   ~~~~~~~~~~
                                 %llu
gnunet-rps.c:224:35: warning: format '%lu' expects argument of type 'long unsigned int *', but argument 3 has type 'uint64_t *' {aka 'long long unsigned int *'} [-Wformat=]
         (0 == sscanf (args[0], "%lu", &num_view_updates)) )
                                 ~~^   ~~~~~~~~~~~~~~~~~
                                 %llu
  CC       gnunet-service-rps_sampler_elem.o
  CC       rps-sampler_common.o
  CC       gnunet-service-rps_sampler.o
  CC       gnunet-service-rps_custommap.o
  CC       gnunet-service-rps_view.o
  CC       gnunet-service-rps.o
  CC       rps-test_util.o
  CC       gnunet-rps-profiler.o
In file included from ../../src/include/gnunet_crypto_lib.h:60,
                 from ../../src/include/gnunet_util_lib.h:64,
                 from gnunet-service-rps.c:28:
gnunet-service-rps.c: In function 's2i_full':
gnunet-service-rps.c:1546:10: warning: format '%lu' expects argument of type 'long unsigned int', but argument 4 has type 'size_t' {aka 'unsigned int'} [-Wformat=]
          "Not able to convert string representation of PeerID to PeerID\n"
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
gnunet-service-rps.c:1549:10:
          len);
          ~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
gnunet-service-rps.c:1545:5: note: in expansion of macro 'LOG'
     LOG (GNUNET_ERROR_TYPE_WARNING,
     ^~~
gnunet-service-rps.c:1547:43: note: format string is defined here
          "Sting representation: %s (len %lu) - too short\n",
                                         ~~^
                                         %u
In file included from ../../src/include/gnunet_crypto_lib.h:60,
                 from ../../src/include/gnunet_util_lib.h:64,
                 from gnunet-service-rps.c:28:
gnunet-service-rps.c: In function 'check_client_seed':
gnunet-service-rps.c:3309:10: warning: format '%lu' expects argument of type 'long unsigned int', but argument 4 has type 'unsigned int' [-Wformat=]
          "message says it sends %" PRIu32 " peers, have space for %lu peers\n",
          ^~~~~~~~~~~~~~~~~~~~~~~~~
gnunet-service-rps.c:3311:10:
          (msize / sizeof(struct GNUNET_PeerIdentity)));
          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
gnunet-service-rps.c:3308:5: note: in expansion of macro 'LOG'
     LOG (GNUNET_ERROR_TYPE_ERROR,
     ^~~
gnunet-service-rps.c:3309:69: note: format string is defined here
          "message says it sends %" PRIu32 " peers, have space for %lu peers\n",
                                                                   ~~^
                                                                   %u
In file included from ../../src/include/gnunet_crypto_lib.h:60,
                 from ../../src/include/gnunet_util_lib.h:64,
                 from gnunet-service-rps.c:28:
gnunet-service-rps.c: In function 'check_peer_pull_reply':
gnunet-service-rps.c:3712:10: warning: format '%lu' expects argument of type 'long unsigned int', but argument 4 has type 'unsigned int' [-Wformat=]
          "message says it sends %" PRIu32 " peers, have space for %lu peers\n",
          ^~~~~~~~~~~~~~~~~~~~~~~~~
gnunet-service-rps.c:3714:10:
          (ntohs (msg->header.size) - sizeof(struct
          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                             GNUNET_RPS_P2P_PullReplyMessage))
                                             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
          / sizeof(struct GNUNET_PeerIdentity));
          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
gnunet-service-rps.c:3711:5: note: in expansion of macro 'LOG'
     LOG (GNUNET_ERROR_TYPE_ERROR,
     ^~~
gnunet-service-rps.c:3712:69: note: format string is defined here
          "message says it sends %" PRIu32 " peers, have space for %lu peers\n",
                                                                   ~~^
                                                                   %u
  CCLD     libgnunetrps.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-rps
In file included from ../../src/include/gnunet_crypto_lib.h:60,
                 from ../../src/include/gnunet_util_lib.h:64,
                 from gnunet-rps-profiler.c:29:
gnunet-rps-profiler.c: In function 'tofile_':
gnunet-rps-profiler.c:900:17: warning: format '%lu' expects argument of type 'long unsigned int', but argument 3 has type 'size_t' {aka 'unsigned int'} [-Wformat=]
                 "Unable to write to file! (Size: %lu, size2: %lu)\n",
                 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                 size,
                 ~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
gnunet-rps-profiler.c:900:17: warning: format '%lu' expects argument of type 'long unsigned int', but argument 4 has type 'size_t' {aka 'unsigned int'} [-Wformat=]
                 "Unable to write to file! (Size: %lu, size2: %lu)\n",
                 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
gnunet-rps-profiler.c:902:17:
                 size2);
                 ~~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
gnunet-rps-profiler.c: In function 'test_run':
gnunet-rps-profiler.c:2974:40: warning: format '%lu' expects argument of type 'long unsigned int', but argument 3 has type 'uint64_t' {aka 'long long unsigned int'} [-Wformat=]
   GNUNET_log (GNUNET_ERROR_TYPE_DEBUG, "timeout for shutdown is %lu\n",
                                        ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
               timeout.rel_value_us / 1000000);
               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
gnunet-rps-profiler.c: In function 'run':
gnunet-rps-profiler.c:3088:15: warning: format '%lu' expects argument of type 'long unsigned int', but argument 3 has type 'uint64_t' {aka 'long long unsigned int'} [-Wformat=]
               "duration is %lus\n",
               ^~~~~~~~~~~~~~~~~~~~
               duration.rel_value_us / 1000000);
               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
gnunet-rps-profiler.c:3091:15: warning: format '%lu' expects argument of type 'long unsigned int', but argument 3 has type 'uint64_t' {aka 'long long unsigned int'} [-Wformat=]
               "timeout is %lus\n",
               ^~~~~~~~~~~~~~~~~~~
               timeout.rel_value_us / 1000000);
               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
../../src/include/gnunet_common.h:547:39: note: in definition of macro 'GNUNET_log'
           GNUNET_log_nocheck ((kind), __VA_ARGS__);                       \
                                       ^~~~~~~~~~~
  CCLD     gnunet-service-rps
  CCLD     gnunet-rps-profiler
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/rps'
Making all in messenger
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/messenger'
  CC       messenger_api.lo
  CC       messenger_api_contact.lo
  CC       messenger_api_contact_store.lo
  CC       messenger_api_message.lo
  CC       messenger_api_list_tunnels.lo
  CC       messenger_api_util.lo
  CC       messenger_api_handle.lo
  CC       messenger_api_room.lo
  CC       gnunet-messenger.o
messenger_api_room.c: In function 'handle_leave_message':
messenger_api_room.c:142:41: warning: unused variable 'store' [-Wunused-variable]
   struct GNUNET_MESSENGER_ContactStore *store = get_handle_contact_store(room->handle);
                                         ^~~~~
  CC       gnunet-service-messenger.o
  CC       gnunet-service-messenger_service.o
  CC       gnunet-service-messenger_list_handles.o
  CC       gnunet-service-messenger_list_messages.o
  CC       gnunet-service-messenger_member_session.o
  CC       gnunet-service-messenger_member.o
  CC       gnunet-service-messenger_member_store.o
  CC       gnunet-service-messenger_message_handle.o
  CC       gnunet-service-messenger_message_kind.o
  CC       gnunet-service-messenger_message_recv.o
  CC       gnunet-service-messenger_message_send.o
  CC       gnunet-service-messenger_message_state.o
  CC       gnunet-service-messenger_message_store.o
gnunet-service-messenger_message_state.c: In function 'save_message_state':
gnunet-service-messenger_message_state.c:105:22: warning: passing argument 1 of 'save_list_messages' discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
   save_list_messages(&(state->last_messages), last_messages_file);
                      ^~~~~~~~~~~~~~~~~~~~~~~
In file included from gnunet-service-messenger_message_state.h:33,
                 from gnunet-service-messenger_message_state.c:26:
gnunet-service-messenger_list_messages.h:107:59: note: expected 'struct GNUNET_MESSENGER_ListMessages *' but argument is of type 'const struct GNUNET_MESSENGER_ListMessages *'
 save_list_messages (struct GNUNET_MESSENGER_ListMessages *messages, const char *path);
                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~
  CC       gnunet-service-messenger_operation_store.o
  CC       gnunet-service-messenger_operation.o
  CC       gnunet-service-messenger_basement.o
  CC       gnunet-service-messenger_ego_store.o
  CC       gnunet-service-messenger_handle.o
  CC       gnunet-service-messenger_room.o
  CC       gnunet-service-messenger_tunnel.o
  CCLD     libgnunetmessenger.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-messenger
  CCLD     gnunet-service-messenger
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/messenger'
Making all in abe
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/abe'
  CC       abe.lo
  CCLD     libgnunetabe.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/abe'
Making all in auction
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/auction'
  CC       gnunet-auction-create.o
  CC       gnunet-auction-info.o
  CC       gnunet-auction-join.o
  CC       gnunet-service-auction.o
  CCLD     gnunet-auction-create
  CCLD     gnunet-auction-info
  CCLD     gnunet-auction-join
  CCLD     gnunet-service-auction
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/auction'
Making all in integration-tests
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/integration-tests'
gawk -v bdir="/usr/bin" -v py="/openwrt/staging_dir/hostpkg/bin/python3" -v awkay="/openwrt/staging_dir/host/bin/awk" -v pfx="/usr" -v prl="/openwrt/staging_dir/host/bin/perl" -v sysconfdirectory="/etc" -v pkgdatadirectory="/usr/share/gnunet" -f ../../bin/dosubst.awk < ./gnunet_testing.py.in > gnunet_testing.py
gawk -v bdir="/usr/bin" -v py="/openwrt/staging_dir/hostpkg/bin/python3" -v awkay="/openwrt/staging_dir/host/bin/awk" -v pfx="/usr" -v prl="/openwrt/staging_dir/host/bin/perl" -v sysconfdirectory="/etc" -v pkgdatadirectory="/usr/share/gnunet" -f ../../bin/dosubst.awk < ./gnunet_pyexpect.py.in > gnunet_pyexpect.py
chmod +x gnunet_testing.py
chmod +x gnunet_pyexpect.py
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/integration-tests'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src'
make[7]: Nothing to be done for 'all-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src'
Making all in po
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/po'
make[6]: Nothing to be done for 'all'.
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/po'
Making all in pkgconfig
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/pkgconfig'
make[6]: Nothing to be done for 'all'.
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/pkgconfig'
Making all in doc
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/doc'
Making all in doxygen
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/doc/doxygen'
Generate documentation:
 	make full - full documentation with dependency graphs (slow)
 	make fast - fast mode without dependency graphs
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/doc/doxygen'
Making all in man
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/doc/man'
gawk -v bdir="/usr/bin" -v py="/openwrt/staging_dir/hostpkg/bin/python3" -v awkay="/openwrt/staging_dir/host/bin/awk" -v pfx="/usr" -v prl="/openwrt/staging_dir/host/bin/perl" -v sysconfdirectory="/etc" -v pkgdatadirectory="/usr/share/gnunet" -f ../../bin/dosubst.awk < ./gnunet.conf.5.in > ./gnunet.conf.5
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/doc/man'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/doc'
make[7]: Nothing to be done for 'all-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/doc'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/doc'
Making all in contrib
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib'
Making all in scripts
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/scripts'
Making all in gnunet-logread
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/scripts/gnunet-logread'
make[8]: Nothing to be done for 'all'.
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/scripts/gnunet-logread'
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/scripts'
gawk -v awkay="/openwrt/staging_dir/host/bin/awk" -f ../../bin/dosubst.awk < ./check-texinfo.awk.in > check-texinfo.awk
chmod +x check-texinfo.awk
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/scripts'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/scripts'
Making all in hellos
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/hellos'
make[7]: Nothing to be done for 'all'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/hellos'
Making all in services
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/services'
Making all in openrc
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/services/openrc'
make[8]: Nothing to be done for 'all'.
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/services/openrc'
Making all in systemd
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/services/systemd'
make[8]: Nothing to be done for 'all'.
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/services/systemd'
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/services'
make[8]: Nothing to be done for 'all-am'.
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/services'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/services'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib'
make[7]: Nothing to be done for 'all-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib'
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1'
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1'
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1'
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1'
Making install in m4
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/m4'
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/m4'
make[6]: Nothing to be done for 'install-exec-am'.
make[6]: Nothing to be done for 'install-data-am'.
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/m4'
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/m4'
Making install in bin
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/bin'
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/bin'
make[6]: Nothing to be done for 'install-exec-am'.
make[6]: Nothing to be done for 'install-data-am'.
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/bin'
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/bin'
Making install in src
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src'
Making install in include
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/include'
Making install in .
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/include'
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/include'
make[8]: Nothing to be done for 'install-exec-am'.
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/include/gnunet'
 /openwrt/staging_dir/host/bin/install -c -m 644 platform.h gettext.h compat.h gnunet_abd_service.h gnunet_applications.h gnunet_arm_service.h gnunet_ats_service.h gnunet_ats_application_service.h gnunet_ats_transport_service.h gnunet_ats_plugin.h gnunet_bandwidth_lib.h gnunet_bio_lib.h gnunet_block_lib.h gnunet_block_group_lib.h gnunet_block_plugin.h gnunet_buffer_lib.h gnunet_client_lib.h gnunet_common.h gnunet_constants.h gnunet_configuration_lib.h gnunet_consensus_service.h gnunet_container_lib.h gnunet_conversation_service.h gnunet_core_service.h gnunet_crypto_lib.h gnunet_curl_lib.h gnunet_datacache_lib.h gnunet_datacache_plugin.h gnunet_datastore_service.h gnunet_datastore_plugin.h gnunet_db_lib.h gnunet_dht_service.h gnunet_disk_lib.h gnunet_dnsparser_lib.h gnunet_dnsstub_lib.h gnunet_dns_service.h gnunet_fragmentation_lib.h gnunet_friends_lib.h gnunet_fs_service.h gnunet_getopt_lib.h '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/include/gnunet'
 /openwrt/staging_dir/host/bin/install -c -m 644 gnunet_gns_service.h gnunet_gnsrecord_lib.h gnunet_gnsrecord_json_lib.h gnunet_gnsrecord_plugin.h gnu_name_system_record_types.h gnunet_hello_lib.h gnunet_helper_lib.h gnunet_identity_service.h gnunet_abe_lib.h gnunet_reclaim_lib.h gnunet_reclaim_plugin.h gnunet_reclaim_service.h gnunet_json_lib.h gnunet_load_lib.h gnunet_cadet_service.h gnunet_messenger_service.h gnunet_mhd_compat.h gnunet_microphone_lib.h gnunet_mst_lib.h gnunet_mq_lib.h gnunet_my_lib.h gnunet_mysql_lib.h gnunet_namecache_plugin.h gnunet_namecache_service.h gnunet_namestore_plugin.h gnunet_namestore_service.h gnunet_nat_auto_service.h gnunet_nat_service.h gnunet_nc_lib.h gnunet_network_lib.h gnunet_nse_service.h gnunet_nt_lib.h gnunet_op_lib.h gnunet_os_lib.h gnunet_peer_lib.h gnunet_peerinfo_service.h gnunet_peerstore_plugin.h gnunet_peerstore_service.h gnunet_plugin_lib.h gnunet_pq_lib.h '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/include/gnunet'
 /openwrt/staging_dir/host/bin/install -c -m 644 gnunet_program_lib.h gnunet_protocols.h gnunet_resolver_service.h gnunet_regex_service.h gnunet_rest_lib.h gnunet_rest_plugin.h gnunet_rps_service.h gnunet_revocation_service.h gnunet_scalarproduct_service.h gnunet_scheduler_lib.h gnunet_secretsharing_service.h gnunet_service_lib.h gnunet_set_service.h gnunet_seti_service.h gnunet_setu_service.h gnunet_signal_lib.h gnunet_signatures.h gnunet_socks.h gnunet_speaker_lib.h gnunet_sq_lib.h gnunet_statistics_service.h gnunet_strings_lib.h gnunet_testbed_service.h gnunet_testbed_logger_service.h gnunet_testbed_ng_service.h gnunet_testing_lib.h gnunet_testing_ng_lib.h gnunet_time_lib.h gnunet_transport_service.h gnunet_transport_application_service.h gnunet_transport_communication_service.h gnunet_transport_core_service.h gnunet_transport_hello_service.h gnunet_transport_manipulation_service.h gnunet_transport_monitor_service.h gnunet_transport_plugin.h gnunet_tun_lib.h gnunet_uri_lib.h gnunet_util_lib.h gnunet_vpn_service.h '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/include/gnunet'
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/include'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/include'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/include'
Making install in util
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetutil.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetutil.so.14.0.0 /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetutil.so.14.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetutil.so.14.0.0 libgnunetutil.so.14 || { rm -f libgnunetutil.so.14 && ln -s libgnunetutil.so.14.0.0 libgnunetutil.so.14; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetutil.so.14.0.0 libgnunetutil.so || { rm -f libgnunetutil.so && ln -s libgnunetutil.so.14.0.0 libgnunetutil.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetutil.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetutil.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-base32 gnunet-config gnunet-crypto-tvg gnunet-resolver gnunet-ecc gnunet-scrypt gnunet-uri '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-base32 /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-base32
OpenWrt-libtool: install: warning: `libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-config /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-config
OpenWrt-libtool: install: warning: `libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-crypto-tvg /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-crypto-tvg
OpenWrt-libtool: install: warning: `libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-resolver /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-resolver
OpenWrt-libtool: install: warning: `libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-ecc /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-ecc
OpenWrt-libtool: install: warning: `libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-scrypt /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-scrypt
OpenWrt-libtool: install: warning: `libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-uri /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-uri
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-resolver gnunet-timeout '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-resolver /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-resolver
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c gnunet-timeout /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-timeout
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 util.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 resolver.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunet_plugin_test.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_test.so /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_test.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_test.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_test.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/gnunet'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util'
Making install in nt
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nt'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nt'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetnt.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetnt.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nt; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 0:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetnt.la -rpath /usr/lib nt.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetnt.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetnt.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetnt.so.0.0.0 libgnunetnt.so.0 || { rm -f libgnunetnt.so.0 && ln -s libgnunetnt.so.0.0.0 libgnunetnt.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetnt.so.0.0.0 libgnunetnt.so || { rm -f libgnunetnt.so && ln -s libgnunetnt.so.0.0.0 libgnunetnt.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetnt.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetnt.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nt'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nt'
Making install in hello
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hello'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hello'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunethello.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunethello.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hello; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 1:0:1 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunethello.la -rpath /usr/lib hello.lo address.lo hello-ng.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunethello.so.0.1.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunethello.so.0.1.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunethello.so.0.1.0 libgnunethello.so.0 || { rm -f libgnunethello.so.0 && ln -s libgnunethello.so.0.1.0 libgnunethello.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunethello.so.0.1.0 libgnunethello.so || { rm -f libgnunethello.so && ln -s libgnunethello.so.0.1.0 libgnunethello.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunethello.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunethello.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hello'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hello'
Making install in block
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/block'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/block'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetblock.la libgnunetblockgroup.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetblock.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/block; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 0:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetblock.la -rpath /usr/lib block.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetblock.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetblock.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetblock.so.0.0.0 libgnunetblock.so.0 || { rm -f libgnunetblock.so.0 && ln -s libgnunetblock.so.0.0.0 libgnunetblock.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetblock.so.0.0.0 libgnunetblock.so || { rm -f libgnunetblock.so && ln -s libgnunetblock.so.0.0.0 libgnunetblock.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetblock.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetblock.la
OpenWrt-libtool: install: warning: relinking `libgnunetblockgroup.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/block; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 0:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetblockgroup.la -rpath /usr/lib bg_bf.lo libgnunetblock.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetblockgroup.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetblockgroup.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetblockgroup.so.0.0.0 libgnunetblockgroup.so.0 || { rm -f libgnunetblockgroup.so.0 && ln -s libgnunetblockgroup.so.0.0.0 libgnunetblockgroup.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetblockgroup.so.0.0.0 libgnunetblockgroup.so || { rm -f libgnunetblockgroup.so && ln -s libgnunetblockgroup.so.0.0.0 libgnunetblockgroup.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetblockgroup.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetblockgroup.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunet_plugin_block_test.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_block_test.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/block; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_block_test.la -rpath /usr/lib/gnunet plugin_block_test.lo libgnunetblockgroup.la libgnunetblock.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_block_test.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_block_test.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_block_test.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_block_test.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/gnunet'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/block'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/block'
Making install in statistics
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetstatistics.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetstatistics.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 2:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetstatistics.la -rpath /usr/lib statistics_api.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetstatistics.so.2.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetstatistics.so.2.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetstatistics.so.2.0.0 libgnunetstatistics.so.2 || { rm -f libgnunetstatistics.so.2 && ln -s libgnunetstatistics.so.2.0.0 libgnunetstatistics.so.2; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetstatistics.so.2.0.0 libgnunetstatistics.so || { rm -f libgnunetstatistics.so && ln -s libgnunetstatistics.so.2.0.0 libgnunetstatistics.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetstatistics.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetstatistics.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-statistics '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-statistics /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-statistics
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-statistics '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-statistics /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-statistics
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 statistics.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics'
Making install in arm
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/arm'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/arm'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetarm.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetarm.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/arm; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 2:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetarm.la -rpath /usr/lib arm_api.lo arm_monitor_api.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetarm.so.2.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetarm.so.2.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetarm.so.2.0.0 libgnunetarm.so.2 || { rm -f libgnunetarm.so.2 && ln -s libgnunetarm.so.2.0.0 libgnunetarm.so.2; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetarm.so.2.0.0 libgnunetarm.so || { rm -f libgnunetarm.so && ln -s libgnunetarm.so.2.0.0 libgnunetarm.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetarm.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetarm.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-arm '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `libgnunetarm.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-arm /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-arm
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-arm '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-arm /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-arm
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 arm.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/arm'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/arm'
Making install in testing
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/testing'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/testing'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunettesting.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunettesting.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/testing; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 2:0:1 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunettesting.la -rpath /usr/lib testing.lo testing_api_cmd_batch.lo testing_api_cmd_hello_world.lo testing_api_cmd_hello_world_birth.lo testing_api_loop.lo testing_api_trait_cmd.lo testing_api_trait_process.lo testing_api_traits.lo ../../src/arm/libgnunetarm.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunettesting.so.1.1.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunettesting.so.1.1.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunettesting.so.1.1.0 libgnunettesting.so.1 || { rm -f libgnunettesting.so.1 && ln -s libgnunettesting.so.1.1.0 libgnunettesting.so.1; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunettesting.so.1.1.0 libgnunettesting.so || { rm -f libgnunettesting.so && ln -s libgnunettesting.so.1.1.0 libgnunettesting.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunettesting.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunettesting.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-testing '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `libgnunettesting.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/arm/libgnunetarm.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-testing /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-testing
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 testing.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/testing'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/testing'
Making install in json
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/json'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/json'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetjson.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetjson.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/json; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -version-info 0:0:0 -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetjson.la -rpath /usr/lib libgnunetjson_la-json.lo libgnunetjson_la-json_mhd.lo libgnunetjson_la-json_generator.lo libgnunetjson_la-json_helper.lo ../../src/util/libgnunetutil.la -ljansson -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lmicrohttpd -lz -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetjson.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetjson.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetjson.so.0.0.0 libgnunetjson.so.0 || { rm -f libgnunetjson.so.0 && ln -s libgnunetjson.so.0.0.0 libgnunetjson.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetjson.so.0.0.0 libgnunetjson.so || { rm -f libgnunetjson.so && ln -s libgnunetjson.so.0.0.0 libgnunetjson.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetjson.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetjson.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/json'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/json'
Making install in curl
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/curl'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/curl'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetcurl.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetcurl.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/curl; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -version-info 0:0:0 -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetcurl.la -rpath /usr/lib libgnunetcurl_la-curl.lo libgnunetcurl_la-curl_reschedule.lo ../../src/util/libgnunetutil.la -ljansson -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lgnurl -lidn2 -lz -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetcurl.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetcurl.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetcurl.so.0.0.0 libgnunetcurl.so.0 || { rm -f libgnunetcurl.so.0 && ln -s libgnunetcurl.so.0.0.0 libgnunetcurl.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetcurl.so.0.0.0 libgnunetcurl.so || { rm -f libgnunetcurl.so && ln -s libgnunetcurl.so.0.0.0 libgnunetcurl.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetcurl.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetcurl.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/curl'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/curl'
Making install in rest
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/rest'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/rest'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetrest.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetrest.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/rest; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 0:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetrest.la -rpath /usr/lib libgnunetrest_la-rest.lo ../../src/util/libgnunetutil.la -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lmicrohttpd -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetrest.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetrest.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetrest.so.0.0.0 libgnunetrest.so.0 || { rm -f libgnunetrest.so.0 && ln -s libgnunetrest.so.0.0.0 libgnunetrest.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetrest.so.0.0.0 libgnunetrest.so || { rm -f libgnunetrest.so && ln -s libgnunetrest.so.0.0.0 libgnunetrest.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetrest.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetrest.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-rest-server '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-rest-server /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-rest-server
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 rest.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunet_plugin_rest_copying.la libgnunet_plugin_rest_config.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_rest_copying.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/rest; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_rest_copying.la -rpath /usr/lib/gnunet libgnunet_plugin_rest_copying_la-plugin_rest_copying.lo libgnunetrest.la ../../src/util/libgnunetutil.la -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lmicrohttpd -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_rest_copying.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_rest_copying.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_rest_copying.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_rest_copying.la
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_rest_config.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/rest; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_rest_config.la -rpath /usr/lib/gnunet libgnunet_plugin_rest_config_la-plugin_rest_config.lo libgnunetrest.la ../../src/util/libgnunetutil.la -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lmicrohttpd -ljansson -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_rest_config.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_rest_config.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_rest_config.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_rest_config.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/gnunet'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/rest'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/rest'
Making install in peerinfo
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/peerinfo'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/peerinfo'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetpeerinfo.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetpeerinfo.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/peerinfo; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 0:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetpeerinfo.la -rpath /usr/lib peerinfo_api.lo peerinfo_api_notify.lo ../../src/hello/libgnunethello.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetpeerinfo.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetpeerinfo.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetpeerinfo.so.0.0.0 libgnunetpeerinfo.so.0 || { rm -f libgnunetpeerinfo.so.0 && ln -s libgnunetpeerinfo.so.0.0.0 libgnunetpeerinfo.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetpeerinfo.so.0.0.0 libgnunetpeerinfo.so || { rm -f libgnunetpeerinfo.so && ln -s libgnunetpeerinfo.so.0.0.0 libgnunetpeerinfo.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetpeerinfo.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetpeerinfo.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-peerinfo '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `../../src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-peerinfo /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-peerinfo
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 peerinfo.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/peerinfo'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/peerinfo'
Making install in sq
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/sq'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/sq'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetsq.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetsq.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/sq; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 0:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetsq.la -rpath /usr/lib sq.lo sq_exec.lo sq_prepare.lo sq_query_helper.lo sq_result_helper.lo -lsqlite3 ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetsq.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetsq.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetsq.so.0.0.0 libgnunetsq.so.0 || { rm -f libgnunetsq.so.0 && ln -s libgnunetsq.so.0.0.0 libgnunetsq.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetsq.so.0.0.0 libgnunetsq.so || { rm -f libgnunetsq.so && ln -s libgnunetsq.so.0.0.0 libgnunetsq.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetsq.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetsq.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/sq'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/sq'
Making install in pq
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/pq'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/pq'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetpq.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetpq.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/pq; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -export-dynamic -no-undefined -version-info 1:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetpq.la -rpath /usr/lib pq.lo pq_connect.lo pq_eval.lo pq_exec.lo pq_prepare.lo pq_query_helper.lo pq_result_helper.lo -lpq ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetpq.so.1.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetpq.so.1.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetpq.so.1.0.0 libgnunetpq.so.1 || { rm -f libgnunetpq.so.1 && ln -s libgnunetpq.so.1.0.0 libgnunetpq.so.1; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetpq.so.1.0.0 libgnunetpq.so || { rm -f libgnunetpq.so && ln -s libgnunetpq.so.1.0.0 libgnunetpq.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetpq.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetpq.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/pq'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/pq'
Making install in datacache
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/datacache'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/datacache'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetdatacache.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetdatacache.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/datacache; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 0:1:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetdatacache.la -rpath /usr/lib datacache.lo ../../src/statistics/libgnunetstatistics.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetdatacache.so.0.0.1T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetdatacache.so.0.0.1
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetdatacache.so.0.0.1 libgnunetdatacache.so.0 || { rm -f libgnunetdatacache.so.0 && ln -s libgnunetdatacache.so.0.0.1 libgnunetdatacache.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetdatacache.so.0.0.1 libgnunetdatacache.so || { rm -f libgnunetdatacache.so && ln -s libgnunetdatacache.so.0.0.1 libgnunetdatacache.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetdatacache.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetdatacache.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 datacache.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunet_plugin_datacache_sqlite.la libgnunet_plugin_datacache_postgres.la libgnunet_plugin_datacache_heap.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_datacache_sqlite.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/datacache; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_datacache_sqlite.la -rpath /usr/lib/gnunet plugin_datacache_sqlite.lo ../../src/statistics/libgnunetstatistics.la ../../src/sq/libgnunetsq.la ../../src/util/libgnunetutil.la -lsqlite3 -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_datacache_sqlite.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_datacache_sqlite.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_datacache_sqlite.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_datacache_sqlite.la
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_datacache_postgres.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/datacache; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_datacache_postgres.la -rpath /usr/lib/gnunet libgnunet_plugin_datacache_postgres_la-plugin_datacache_postgres.lo ../../src/pq/libgnunetpq.la ../../src/statistics/libgnunetstatistics.la ../../src/util/libgnunetutil.la -export-dynamic -avoid-version -module -no-undefined -lpq -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_datacache_postgres.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_datacache_postgres.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_datacache_postgres.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_datacache_postgres.la
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_datacache_heap.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/datacache; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_datacache_heap.la -rpath /usr/lib/gnunet plugin_datacache_heap.lo ../../src/statistics/libgnunetstatistics.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_datacache_heap.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_datacache_heap.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_datacache_heap.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_datacache_heap.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/gnunet'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/datacache'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/datacache'
Making install in datastore
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/datastore'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/datastore'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetdatastore.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetdatastore.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/datastore; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 1:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetdatastore.la -rpath /usr/lib datastore_api.lo ../../src/statistics/libgnunetstatistics.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetdatastore.so.1.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetdatastore.so.1.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetdatastore.so.1.0.0 libgnunetdatastore.so.1 || { rm -f libgnunetdatastore.so.1 && ln -s libgnunetdatastore.so.1.0.0 libgnunetdatastore.so.1; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetdatastore.so.1.0.0 libgnunetdatastore.so || { rm -f libgnunetdatastore.so && ln -s libgnunetdatastore.so.1.0.0 libgnunetdatastore.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetdatastore.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetdatastore.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-datastore '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `libgnunetdatastore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-datastore /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-datastore
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-datastore '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-datastore /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-datastore
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 datastore.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunet_plugin_datastore_sqlite.la libgnunet_plugin_datastore_postgres.la libgnunet_plugin_datastore_heap.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_datastore_sqlite.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/datastore; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_datastore_sqlite.la -rpath /usr/lib/gnunet plugin_datastore_sqlite.lo ../../src/sq/libgnunetsq.la ../../src/statistics/libgnunetstatistics.la ../../src/util/libgnunetutil.la -lsqlite3 -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_datastore_sqlite.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_datastore_sqlite.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_datastore_sqlite.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_datastore_sqlite.la
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_datastore_postgres.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/datastore; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_datastore_postgres.la -rpath /usr/lib/gnunet libgnunet_plugin_datastore_postgres_la-plugin_datastore_postgres.lo ../../src/statistics/libgnunetstatistics.la ../../src/pq/libgnunetpq.la ../../src/util/libgnunetutil.la -lpq -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_datastore_postgres.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_datastore_postgres.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_datastore_postgres.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_datastore_postgres.la
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_datastore_heap.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/datastore; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_datastore_heap.la -rpath /usr/lib/gnunet plugin_datastore_heap.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_datastore_heap.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_datastore_heap.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_datastore_heap.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_datastore_heap.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/gnunet'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/datastore'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/datastore'
Making install in template
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/template'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/template'
make[7]: Nothing to be done for 'install-exec-am'.
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 template.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/template'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/template'
Making install in peerstore
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/peerstore'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/peerstore'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetpeerstore.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetpeerstore.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/peerstore; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetpeerstore.la -rpath /usr/lib peerstore_api.lo peerstore_common.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetpeerstore.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetpeerstore.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetpeerstore.so.0.0.0 libgnunetpeerstore.so.0 || { rm -f libgnunetpeerstore.so.0 && ln -s libgnunetpeerstore.so.0.0.0 libgnunetpeerstore.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetpeerstore.so.0.0.0 libgnunetpeerstore.so || { rm -f libgnunetpeerstore.so && ln -s libgnunetpeerstore.so.0.0.0 libgnunetpeerstore.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetpeerstore.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetpeerstore.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-peerstore '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `libgnunetpeerstore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-peerstore /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-peerstore
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-peerstore '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-peerstore /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-peerstore
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 peerstore.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunet_plugin_peerstore_sqlite.la libgnunet_plugin_peerstore_flat.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_peerstore_sqlite.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/peerstore; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_peerstore_sqlite.la -rpath /usr/lib/gnunet plugin_peerstore_sqlite.lo libgnunetpeerstore.la ../../src/sq/libgnunetsq.la ../../src/util/libgnunetutil.la -lsqlite3 -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_peerstore_sqlite.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_peerstore_sqlite.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_peerstore_sqlite.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_peerstore_sqlite.la
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_peerstore_flat.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/peerstore; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_peerstore_flat.la -rpath /usr/lib/gnunet plugin_peerstore_flat.lo libgnunetpeerstore.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_peerstore_flat.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_peerstore_flat.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_peerstore_flat.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_peerstore_flat.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/gnunet'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/peerstore'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/peerstore'
Making install in ats
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetats.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetats.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 4:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetats.la -rpath /usr/lib ats_api_connectivity.lo ats_api_scheduling.lo ats_api_scanner.lo ats_api_performance.lo ../../src/hello/libgnunethello.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetats.so.4.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetats.so.4.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetats.so.4.0.0 libgnunetats.so.4 || { rm -f libgnunetats.so.4 && ln -s libgnunetats.so.4.0.0 libgnunetats.so.4; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetats.so.4.0.0 libgnunetats.so || { rm -f libgnunetats.so && ln -s libgnunetats.so.4.0.0 libgnunetats.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetats.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetats.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-ats '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `../../src/nt/libgnunetnt.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `libgnunetats.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-ats /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-ats
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 ats.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunet_plugin_ats_proportional.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_ats_proportional.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_ats_proportional.la -rpath /usr/lib/gnunet plugin_ats_proportional.lo libgnunetats.la ../../src/statistics/libgnunetstatistics.la ../../src/util/libgnunetutil.la ../../src/nt/libgnunetnt.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_ats_proportional.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_ats_proportional.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_ats_proportional.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_ats_proportional.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/gnunet'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats'
Making install in nat
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nat'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nat'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetnatnew.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetnatnew.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nat; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 2:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetnatnew.la -rpath /usr/lib nat_api.lo nat_api_stun.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetnatnew.so.2.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetnatnew.so.2.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetnatnew.so.2.0.0 libgnunetnatnew.so.2 || { rm -f libgnunetnatnew.so.2 && ln -s libgnunetnatnew.so.2.0.0 libgnunetnatnew.so.2; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetnatnew.so.2.0.0 libgnunetnatnew.so || { rm -f libgnunetnatnew.so && ln -s libgnunetnatnew.so.2.0.0 libgnunetnatnew.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetnatnew.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetnatnew.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-nat '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `libgnunetnatnew.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-nat /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-nat
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-helper-nat-server gnunet-helper-nat-client gnunet-service-nat '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c gnunet-helper-nat-server /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-helper-nat-server
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c gnunet-helper-nat-client /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-helper-nat-client
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-nat /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-nat
make  install-exec-hook
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nat'
make[8]: Nothing to be done for 'install-exec-hook'.
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nat'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 nat.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nat'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nat'
Making install in nat-auto
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nat-auto'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nat-auto'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetnatauto.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetnatauto.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nat-auto; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 0:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetnatauto.la -rpath /usr/lib nat_auto_api.lo nat_auto_api_test.lo ../../src/nat/libgnunetnatnew.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetnatauto.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetnatauto.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetnatauto.so.0.0.0 libgnunetnatauto.so.0 || { rm -f libgnunetnatauto.so.0 && ln -s libgnunetnatauto.so.0.0.0 libgnunetnatauto.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetnatauto.so.0.0.0 libgnunetnatauto.so || { rm -f libgnunetnatauto.so && ln -s libgnunetnatauto.so.0.0.0 libgnunetnatauto.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetnatauto.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetnatauto.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-nat-auto gnunet-nat-server '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `libgnunetnatauto.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nat/libgnunetnatnew.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-nat-auto /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-nat-auto
OpenWrt-libtool: install: warning: `../../src/nat/libgnunetnatnew.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-nat-server /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-nat-server
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-nat-auto '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/nat/libgnunetnatnew.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-nat-auto /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-nat-auto
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 nat-auto.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nat-auto'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nat-auto'
Making install in fragmentation
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/fragmentation'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/fragmentation'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetfragmentation.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetfragmentation.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/fragmentation; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 2:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetfragmentation.la -rpath /usr/lib fragmentation.lo defragmentation.lo -lm ../../src/statistics/libgnunetstatistics.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetfragmentation.so.2.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetfragmentation.so.2.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetfragmentation.so.2.0.0 libgnunetfragmentation.so.2 || { rm -f libgnunetfragmentation.so.2 && ln -s libgnunetfragmentation.so.2.0.0 libgnunetfragmentation.so.2; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetfragmentation.so.2.0.0 libgnunetfragmentation.so || { rm -f libgnunetfragmentation.so && ln -s libgnunetfragmentation.so.2.0.0 libgnunetfragmentation.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetfragmentation.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetfragmentation.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/fragmentation'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/fragmentation'
Making install in transport
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/transport'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/transport'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunettransport.la libgnunettransportapplication.la libgnunettransportcore.la libgnunettransportcommunicator.la libgnunettransportmonitor.la libgnunettransporttesting.la libgnunettransporttesting2.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunettransport.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/transport; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 4:0:2 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunettransport.la -rpath /usr/lib transport_api_address_to_string.lo transport_api_blacklist.lo transport_api_core.lo transport_api_hello_get.lo transport_api_manipulation.lo transport_api_monitor_peers.lo transport_api_monitor_plugins.lo transport_api_offer_hello.lo ../../src/hello/libgnunethello.la ../../src/ats/libgnunetats.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunettransport.so.2.2.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunettransport.so.2.2.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunettransport.so.2.2.0 libgnunettransport.so.2 || { rm -f libgnunettransport.so.2 && ln -s libgnunettransport.so.2.2.0 libgnunettransport.so.2; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunettransport.so.2.2.0 libgnunettransport.so || { rm -f libgnunettransport.so && ln -s libgnunettransport.so.2.2.0 libgnunettransport.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunettransport.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunettransport.la
OpenWrt-libtool: install: warning: relinking `libgnunettransportapplication.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/transport; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 0:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunettransportapplication.la -rpath /usr/lib transport_api2_application.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunettransportapplication.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunettransportapplication.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunettransportapplication.so.0.0.0 libgnunettransportapplication.so.0 || { rm -f libgnunettransportapplication.so.0 && ln -s libgnunettransportapplication.so.0.0.0 libgnunettransportapplication.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunettransportapplication.so.0.0.0 libgnunettransportapplication.so || { rm -f libgnunettransportapplication.so && ln -s libgnunettransportapplication.so.0.0.0 libgnunettransportapplication.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunettransportapplication.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunettransportapplication.la
OpenWrt-libtool: install: warning: relinking `libgnunettransportcore.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/transport; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 0:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunettransportcore.la -rpath /usr/lib transport_api2_core.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunettransportcore.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunettransportcore.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunettransportcore.so.0.0.0 libgnunettransportcore.so.0 || { rm -f libgnunettransportcore.so.0 && ln -s libgnunettransportcore.so.0.0.0 libgnunettransportcore.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunettransportcore.so.0.0.0 libgnunettransportcore.so || { rm -f libgnunettransportcore.so && ln -s libgnunettransportcore.so.0.0.0 libgnunettransportcore.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunettransportcore.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunettransportcore.la
OpenWrt-libtool: install: warning: relinking `libgnunettransportcommunicator.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/transport; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 0:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunettransportcommunicator.la -rpath /usr/lib transport_api2_communication.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunettransportcommunicator.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunettransportcommunicator.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunettransportcommunicator.so.0.0.0 libgnunettransportcommunicator.so.0 || { rm -f libgnunettransportcommunicator.so.0 && ln -s libgnunettransportcommunicator.so.0.0.0 libgnunettransportcommunicator.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunettransportcommunicator.so.0.0.0 libgnunettransportcommunicator.so || { rm -f libgnunettransportcommunicator.so && ln -s libgnunettransportcommunicator.so.0.0.0 libgnunettransportcommunicator.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunettransportcommunicator.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunettransportcommunicator.la
OpenWrt-libtool: install: warning: relinking `libgnunettransportmonitor.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/transport; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 0:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunettransportmonitor.la -rpath /usr/lib transport_api2_monitor.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunettransportmonitor.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunettransportmonitor.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunettransportmonitor.so.0.0.0 libgnunettransportmonitor.so.0 || { rm -f libgnunettransportmonitor.so.0 && ln -s libgnunettransportmonitor.so.0.0.0 libgnunettransportmonitor.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunettransportmonitor.so.0.0.0 libgnunettransportmonitor.so || { rm -f libgnunettransportmonitor.so && ln -s libgnunettransportmonitor.so.0.0.0 libgnunettransportmonitor.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunettransportmonitor.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunettransportmonitor.la
OpenWrt-libtool: install: warning: relinking `libgnunettransporttesting.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/transport; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunettransporttesting.la -rpath /usr/lib transport-testing.lo transport-testing-filenames.lo transport-testing-loggers.lo transport-testing-main.lo transport-testing-send.lo libgnunettransport.la ../../src/hello/libgnunethello.la ../../src/ats/libgnunetats.la ../../src/util/libgnunetutil.la ../../src/testing/libgnunettesting.la ../../src/arm/libgnunetarm.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunettransporttesting.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunettransporttesting.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunettransporttesting.so.0.0.0 libgnunettransporttesting.so.0 || { rm -f libgnunettransporttesting.so.0 && ln -s libgnunettransporttesting.so.0.0.0 libgnunettransporttesting.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunettransporttesting.so.0.0.0 libgnunettransporttesting.so || { rm -f libgnunettransporttesting.so && ln -s libgnunettransporttesting.so.0.0.0 libgnunettransporttesting.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunettransporttesting.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunettransporttesting.la
OpenWrt-libtool: install: warning: relinking `libgnunettransporttesting2.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/transport; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunettransporttesting2.la -rpath /usr/lib transport-testing2.lo transport-testing-filenames2.lo transport-testing-loggers2.lo transport-testing-main2.lo transport-testing-send2.lo transport-testing-communicator.lo libgnunettransportapplication.la libgnunettransportcore.la ../../src/arm/libgnunetarm.la ../../src/testing/libgnunettesting.la ../../src/ats/libgnunetats.la ../../src/hello/libgnunethello.la ../../src/peerstore/libgnunetpeerstore.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunettransporttesting2.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunettransporttesting2.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunettransporttesting2.so.0.0.0 libgnunettransporttesting2.so.0 || { rm -f libgnunettransporttesting2.so.0 && ln -s libgnunettransporttesting2.so.0.0.0 libgnunettransporttesting2.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunettransporttesting2.so.0.0.0 libgnunettransporttesting2.so || { rm -f libgnunettransporttesting2.so && ln -s libgnunettransporttesting2.so.0.0.0 libgnunettransporttesting2.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunettransporttesting2.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunettransporttesting2.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-transport '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `libgnunettransport.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats/libgnunetats.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-transport /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-transport
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
 /openwrt/staging_dir/host/bin/install -c gnunet-transport-certificate-creation '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-helper-transport-wlan gnunet-helper-transport-wlan-dummy gnunet-helper-transport-bluetooth gnunet-service-transport gnunet-service-tng gnunet-communicator-unix gnunet-communicator-udp gnunet-communicator-tcp '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c gnunet-helper-transport-wlan /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-helper-transport-wlan
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-helper-transport-wlan-dummy /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-helper-transport-wlan-dummy
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c gnunet-helper-transport-bluetooth /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-helper-transport-bluetooth
OpenWrt-libtool: install: warning: `libgnunettransport.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats/libgnunetats.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/ats/libgnunetats.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/nt/libgnunetnt.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/peerinfo/libgnunetpeerinfo.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-transport /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-transport
OpenWrt-libtool: install: warning: `../../src/peerstore/libgnunetpeerstore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-tng /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-tng
OpenWrt-libtool: install: warning: `libgnunettransportcommunicator.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-communicator-unix /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-communicator-unix
OpenWrt-libtool: install: warning: `libgnunettransportapplication.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `libgnunettransportcommunicator.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/nat/libgnunetnatnew.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/nt/libgnunetnt.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-communicator-udp /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-communicator-udp
OpenWrt-libtool: install: warning: `libgnunettransportcommunicator.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/peerstore/libgnunetpeerstore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/nat/libgnunetnatnew.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/nt/libgnunetnt.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-communicator-tcp /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-communicator-tcp
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 transport.conf communicator-unix.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunet_plugin_transport_tcp.la libgnunet_plugin_transport_unix.la libgnunet_plugin_transport_http_client.la libgnunet_plugin_transport_https_client.la libgnunet_plugin_transport_http_server.la libgnunet_plugin_transport_https_server.la libgnunet_plugin_transport_wlan.la libgnunet_plugin_transport_bluetooth.la libgnunet_plugin_transport_udp.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_transport_tcp.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/transport; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_transport_tcp.la -rpath /usr/lib/gnunet plugin_transport_tcp.lo ../../src/hello/libgnunethello.la ../../src/statistics/libgnunetstatistics.la ../../src/peerinfo/libgnunetpeerinfo.la ../../src/nat/libgnunetnatnew.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_transport_tcp.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_transport_tcp.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_transport_tcp.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_transport_tcp.la
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_transport_unix.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/transport; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_transport_unix.la -rpath /usr/lib/gnunet plugin_transport_unix.lo ../../src/hello/libgnunethello.la ../../src/statistics/libgnunetstatistics.la ../../src/peerinfo/libgnunetpeerinfo.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_transport_unix.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_transport_unix.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_transport_unix.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_transport_unix.la
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_transport_http_client.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/transport; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_transport_http_client.la -rpath /usr/lib/gnunet libgnunet_plugin_transport_http_client_la-plugin_transport_http_client.lo libgnunet_plugin_transport_http_client_la-plugin_transport_http_common.lo ../../src/hello/libgnunethello.la ../../src/statistics/libgnunetstatistics.la ../../src/peerinfo/libgnunetpeerinfo.la -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lgnurl -lidn2 -lz ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_transport_http_client.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_transport_http_client.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_transport_http_client.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_transport_http_client.la
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_transport_https_client.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/transport; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -DBUILD_HTTPS -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_transport_https_client.la -rpath /usr/lib/gnunet libgnunet_plugin_transport_https_client_la-plugin_transport_http_client.lo libgnunet_plugin_transport_https_client_la-plugin_transport_http_common.lo ../../src/hello/libgnunethello.la ../../src/statistics/libgnunetstatistics.la ../../src/peerinfo/libgnunetpeerinfo.la -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lgnurl -lidn2 -lz ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_transport_https_client.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_transport_https_client.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_transport_https_client.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_transport_https_client.la
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_transport_http_server.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/transport; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_transport_http_server.la -rpath /usr/lib/gnunet libgnunet_plugin_transport_http_server_la-plugin_transport_http_server.lo libgnunet_plugin_transport_http_server_la-plugin_transport_http_common.lo -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lmicrohttpd ../../src/hello/libgnunethello.la ../../src/statistics/libgnunetstatistics.la ../../src/peerinfo/libgnunetpeerinfo.la ../../src/nat/libgnunetnatnew.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_transport_http_server.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_transport_http_server.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_transport_http_server.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_transport_http_server.la
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_transport_https_server.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/transport; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -DBUILD_HTTPS -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_transport_https_server.la -rpath /usr/lib/gnunet libgnunet_plugin_transport_https_server_la-plugin_transport_http_server.lo libgnunet_plugin_transport_https_server_la-plugin_transport_http_common.lo -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lmicrohttpd ../../src/hello/libgnunethello.la ../../src/statistics/libgnunetstatistics.la ../../src/peerinfo/libgnunetpeerinfo.la ../../src/nat/libgnunetnatnew.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_transport_https_server.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_transport_https_server.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_transport_https_server.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_transport_https_server.la
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_transport_wlan.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/transport; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -DBUILD_WLAN -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_transport_wlan.la -rpath /usr/lib/gnunet libgnunet_plugin_transport_wlan_la-plugin_transport_wlan.lo ../../src/hello/libgnunethello.la ../../src/statistics/libgnunetstatistics.la ../../src/peerinfo/libgnunetpeerinfo.la ../../src/fragmentation/libgnunetfragmentation.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_transport_wlan.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_transport_wlan.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_transport_wlan.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_transport_wlan.la
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_transport_bluetooth.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/transport; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -DBUILD_BLUETOOTH -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_transport_bluetooth.la -rpath /usr/lib/gnunet libgnunet_plugin_transport_bluetooth_la-plugin_transport_wlan.lo ../../src/hello/libgnunethello.la ../../src/statistics/libgnunetstatistics.la ../../src/peerinfo/libgnunetpeerinfo.la ../../src/fragmentation/libgnunetfragmentation.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_transport_bluetooth.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_transport_bluetooth.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_transport_bluetooth.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_transport_bluetooth.la
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_transport_udp.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/transport; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_transport_udp.la -rpath /usr/lib/gnunet plugin_transport_udp.lo plugin_transport_udp_broadcasting.lo ../../src/hello/libgnunethello.la ../../src/fragmentation/libgnunetfragmentation.la ../../src/statistics/libgnunetstatistics.la ../../src/peerinfo/libgnunetpeerinfo.la ../../src/nat/libgnunetnatnew.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_transport_udp.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_transport_udp.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_transport_udp.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_transport_udp.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/gnunet'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/transport'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/transport'
Making install in ats-tool
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats-tool'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats-tool'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-ats '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/ats/libgnunetats.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/nt/libgnunetnt.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/transport/libgnunettransport.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats/libgnunetats.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-ats /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-ats
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats-tool'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats-tool'
Making install in core
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/core'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/core'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetcore.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetcore.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/core; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 0:1:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetcore.la -rpath /usr/lib core_api.lo core_api_monitor_peers.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetcore.so.0.0.1T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetcore.so.0.0.1
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetcore.so.0.0.1 libgnunetcore.so.0 || { rm -f libgnunetcore.so.0 && ln -s libgnunetcore.so.0.0.1 libgnunetcore.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetcore.so.0.0.1 libgnunetcore.so || { rm -f libgnunetcore.so && ln -s libgnunetcore.so.0.0.1 libgnunetcore.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetcore.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetcore.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-core '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `libgnunetcore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-core /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-core
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-core '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/transport/libgnunettransport.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats/libgnunetats.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-core /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-core
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 core.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/core'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/core'
Making install in testbed-logger
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/testbed-logger'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/testbed-logger'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunettestbedlogger.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunettestbedlogger.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/testbed-logger; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 0:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunettestbedlogger.la -rpath /usr/lib testbed_logger_api.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunettestbedlogger.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunettestbedlogger.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunettestbedlogger.so.0.0.0 libgnunettestbedlogger.so.0 || { rm -f libgnunettestbedlogger.so.0 && ln -s libgnunettestbedlogger.so.0.0.0 libgnunettestbedlogger.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunettestbedlogger.so.0.0.0 libgnunettestbedlogger.so || { rm -f libgnunettestbedlogger.so && ln -s libgnunettestbedlogger.so.0.0.0 libgnunettestbedlogger.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunettestbedlogger.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunettestbedlogger.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-testbed-logger '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-testbed-logger /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-testbed-logger
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 testbed-logger.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/testbed-logger'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/testbed-logger'
Making install in testbed
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/testbed'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/testbed'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunettestbed.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunettestbed.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/testbed; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 0:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunettestbed.la -rpath /usr/lib testbed_api.lo testbed_api_hosts.lo testbed_api_cmd_controller.lo testbed_api_cmd_peer.lo testbed_api_cmd_service.lo testbed_api_operations.lo testbed_api_peers.lo testbed_api_services.lo testbed_api_statistics.lo testbed_api_testbed.lo testbed_api_test.lo testbed_api_topology.lo testbed_api_sd.lo testbed_api_barriers.lo ../../src/statistics/libgnunetstatistics.la ../../src/transport/libgnunettransport.la ../../src/hello/libgnunethello.la -lm -lz ../../src/util/libgnunetutil.la ../../src/testing/libgnunettesting.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunettestbed.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunettestbed.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunettestbed.so.0.0.0 libgnunettestbed.so.0 || { rm -f libgnunettestbed.so.0 && ln -s libgnunettestbed.so.0.0.0 libgnunettestbed.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunettestbed.so.0.0.0 libgnunettestbed.so || { rm -f libgnunettestbed.so && ln -s libgnunettestbed.so.0.0.0 libgnunettestbed.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunettestbed.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunettestbed.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-testbed-profiler '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `libgnunettestbed.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/transport/libgnunettransport.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats/libgnunetats.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/testing/libgnunettesting.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/arm/libgnunetarm.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-testbed-profiler /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-testbed-profiler
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-testbed gnunet-helper-testbed gnunet-daemon-testbed-blacklist gnunet-daemon-testbed-underlay gnunet-daemon-latency-logger '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/core/libgnunetcore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/transport/libgnunettransport.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/ats/libgnunetats.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/testing/libgnunettesting.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `libgnunettestbed.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/transport/libgnunettransport.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats/libgnunetats.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/testing/libgnunettesting.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/arm/libgnunetarm.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/arm/libgnunetarm.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-testbed /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-testbed
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/testing/libgnunettesting.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `libgnunettestbed.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/transport/libgnunettransport.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats/libgnunetats.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/testing/libgnunettesting.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/arm/libgnunetarm.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-helper-testbed /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-helper-testbed
OpenWrt-libtool: install: warning: `../../src/transport/libgnunettransport.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats/libgnunetats.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-daemon-testbed-blacklist /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-daemon-testbed-blacklist
OpenWrt-libtool: install: warning: `../../src/transport/libgnunettransport.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats/libgnunetats.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-daemon-testbed-underlay /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-daemon-testbed-underlay
OpenWrt-libtool: install: warning: `../../src/ats/libgnunetats.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-daemon-latency-logger /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-daemon-latency-logger
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 testbed.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/testbed'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/testbed'
Making install in ats-tests
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats-tests'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats-tests'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetatstesting.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetatstesting.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats-tests; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetatstesting.la -rpath /usr/lib ats-testing.lo ats-testing-log.lo ats-testing-traffic.lo ats-testing-experiment.lo ats-testing-preferences.lo ../../src/testbed/libgnunettestbed.la ../../src/statistics/libgnunetstatistics.la ../../src/core/libgnunetcore.la ../../src/transport/libgnunettransport.la ../../src/hello/libgnunethello.la ../../src/ats/libgnunetats.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetatstesting.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetatstesting.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetatstesting.so.0.0.0 libgnunetatstesting.so.0 || { rm -f libgnunetatstesting.so.0 && ln -s libgnunetatstesting.so.0.0.0 libgnunetatstesting.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetatstesting.so.0.0.0 libgnunetatstesting.so || { rm -f libgnunetatstesting.so && ln -s libgnunetatstesting.so.0.0.0 libgnunetatstesting.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetatstesting.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetatstesting.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats-tests'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats-tests'
Making install in nse
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nse'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nse'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetnse.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetnse.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nse; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 0:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetnse.la -rpath /usr/lib nse_api.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetnse.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetnse.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetnse.so.0.0.0 libgnunetnse.so.0 || { rm -f libgnunetnse.so.0 && ln -s libgnunetnse.so.0.0.0 libgnunetnse.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetnse.so.0.0.0 libgnunetnse.so || { rm -f libgnunetnse.so && ln -s libgnunetnse.so.0.0.0 libgnunetnse.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetnse.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetnse.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-nse '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `libgnunetnse.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-nse /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-nse
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-nse '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `libgnunetnse.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/core/libgnunetcore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-nse /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-nse
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 nse.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nse'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nse'
Making install in dht
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/dht'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/dht'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetdht.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetdht.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/dht; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 3:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetdht.la -rpath /usr/lib dht_api.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetdht.so.3.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetdht.so.3.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetdht.so.3.0.0 libgnunetdht.so.3 || { rm -f libgnunetdht.so.3 && ln -s libgnunetdht.so.3.0.0 libgnunetdht.so.3; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetdht.so.3.0.0 libgnunetdht.so || { rm -f libgnunetdht.so && ln -s libgnunetdht.so.3.0.0 libgnunetdht.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetdht.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetdht.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-dht-monitor gnunet-dht-get gnunet-dht-put '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `libgnunetdht.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/core/libgnunetcore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-dht-monitor /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-dht-monitor
OpenWrt-libtool: install: warning: `libgnunetdht.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/core/libgnunetcore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-dht-get /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-dht-get
OpenWrt-libtool: install: warning: `libgnunetdht.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/core/libgnunetcore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-dht-put /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-dht-put
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-dht '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/core/libgnunetcore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/nse/libgnunetnse.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/ats/libgnunetats.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/transport/libgnunettransport.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats/libgnunetats.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/peerinfo/libgnunetpeerinfo.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/block/libgnunetblock.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/datacache/libgnunetdatacache.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-dht /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-dht
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 dht.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunet_plugin_block_dht.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_block_dht.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/dht; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_block_dht.la -rpath /usr/lib/gnunet plugin_block_dht.lo ../../src/hello/libgnunethello.la ../../src/block/libgnunetblock.la ../../src/block/libgnunetblockgroup.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_block_dht.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_block_dht.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_block_dht.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_block_dht.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/gnunet'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/dht'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/dht'
Making install in hostlist
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hostlist'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hostlist'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-daemon-hostlist '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `../../src/core/libgnunetcore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/peerinfo/libgnunetpeerinfo.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/transport/libgnunettransport.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats/libgnunetats.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-daemon-hostlist /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-daemon-hostlist
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 hostlist.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hostlist'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hostlist'
Making install in topology
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/topology'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/topology'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetfriends.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetfriends.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/topology; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 0:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetfriends.la -rpath /usr/lib friends.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetfriends.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetfriends.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetfriends.so.0.0.0 libgnunetfriends.so.0 || { rm -f libgnunetfriends.so.0 && ln -s libgnunetfriends.so.0.0.0 libgnunetfriends.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetfriends.so.0.0.0 libgnunetfriends.so || { rm -f libgnunetfriends.so && ln -s libgnunetfriends.so.0.0.0 libgnunetfriends.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetfriends.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetfriends.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-daemon-topology '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `libgnunetfriends.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/core/libgnunetcore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/peerinfo/libgnunetpeerinfo.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/transport/libgnunettransport.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats/libgnunetats.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/ats/libgnunetats.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-daemon-topology /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-daemon-topology
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 topology.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/topology'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/topology'
Making install in regex
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/regex'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/regex'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetregexblock.la libgnunetregex.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetregexblock.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/regex; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 1:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetregexblock.la -rpath /usr/lib regex_block_lib.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetregexblock.so.1.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetregexblock.so.1.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetregexblock.so.1.0.0 libgnunetregexblock.so.1 || { rm -f libgnunetregexblock.so.1 && ln -s libgnunetregexblock.so.1.0.0 libgnunetregexblock.so.1; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetregexblock.so.1.0.0 libgnunetregexblock.so || { rm -f libgnunetregexblock.so && ln -s libgnunetregexblock.so.1.0.0 libgnunetregexblock.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetregexblock.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetregexblock.la
OpenWrt-libtool: install: warning: relinking `libgnunetregex.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/regex; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 3:1:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetregex.la -rpath /usr/lib regex_api_announce.lo regex_api_search.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetregex.so.3.0.1T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetregex.so.3.0.1
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetregex.so.3.0.1 libgnunetregex.so.3 || { rm -f libgnunetregex.so.3 && ln -s libgnunetregex.so.3.0.1 libgnunetregex.so.3; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetregex.so.3.0.1 libgnunetregex.so || { rm -f libgnunetregex.so && ln -s libgnunetregex.so.3.0.1 libgnunetregex.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetregex.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetregex.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-regex gnunet-daemon-regexprofiler '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `libgnunetregexblock.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/dht/libgnunetdht.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-regex /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-regex
OpenWrt-libtool: install: warning: `../../src/dht/libgnunetdht.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `libgnunetregexblock.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-daemon-regexprofiler /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-daemon-regexprofiler
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 regex.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunet_plugin_block_regex.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_block_regex.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/regex; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_block_regex.la -rpath /usr/lib/gnunet plugin_block_regex.lo libgnunetregexblock.la ../../src/block/libgnunetblock.la ../../src/block/libgnunetblockgroup.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_block_regex.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_block_regex.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_block_regex.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_block_regex.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/gnunet'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/regex'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/regex'
Making install in dns
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/dns'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/dns'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetdns.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetdns.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/dns; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 0:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetdns.la -rpath /usr/lib dns_api.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetdns.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetdns.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetdns.so.0.0.0 libgnunetdns.so.0 || { rm -f libgnunetdns.so.0 && ln -s libgnunetdns.so.0.0.0 libgnunetdns.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetdns.so.0.0.0 libgnunetdns.so || { rm -f libgnunetdns.so && ln -s libgnunetdns.so.0.0.0 libgnunetdns.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetdns.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetdns.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-dns gnunet-helper-dns '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-dns /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-dns
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c gnunet-helper-dns /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-helper-dns
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 dns.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunet_plugin_block_dns.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_block_dns.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/dns; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include ../../src/block/-export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_block_dns.la -rpath /usr/lib/gnunet plugin_block_dns.lo ../../src/block/libgnunetblockgroup.la ../../src/block/libgnunetblock.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_block_dns.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_block_dns.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_block_dns.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_block_dns.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/gnunet'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/dns'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/dns'
Making install in identity
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/identity'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/identity'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetidentity.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetidentity.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/identity; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 1:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetidentity.la -rpath /usr/lib identity_api.lo identity_api_lookup.lo identity_api_suffix_lookup.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetidentity.so.1.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetidentity.so.1.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetidentity.so.1.0.0 libgnunetidentity.so.1 || { rm -f libgnunetidentity.so.1 && ln -s libgnunetidentity.so.1.0.0 libgnunetidentity.so.1; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetidentity.so.1.0.0 libgnunetidentity.so || { rm -f libgnunetidentity.so && ln -s libgnunetidentity.so.1.0.0 libgnunetidentity.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetidentity.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetidentity.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-identity '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-identity /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-identity
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-identity '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-identity /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-identity
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 identity.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunet_plugin_rest_identity.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_rest_identity.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/identity; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_rest_identity.la -rpath /usr/lib/gnunet libgnunet_plugin_rest_identity_la-plugin_rest_identity.lo libgnunetidentity.la ../../src/rest/libgnunetrest.la ../../src/util/libgnunetutil.la -ljansson -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lmicrohttpd -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_rest_identity.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_rest_identity.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_rest_identity.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_rest_identity.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/gnunet'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/identity'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/identity'
Making install in gnsrecord
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gnsrecord'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gnsrecord'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetgnsrecord.la libgnunetgnsrecordjson.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetgnsrecord.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gnsrecord; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 0:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetgnsrecord.la -rpath /usr/lib gnsrecord.lo gnsrecord_serialization.lo gnsrecord_crypto.lo gnsrecord_misc.lo ../../src/util/libgnunetutil.la ../../src/identity/libgnunetidentity.la -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lgcrypt -lgpg-error -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetgnsrecord.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetgnsrecord.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetgnsrecord.so.0.0.0 libgnunetgnsrecord.so.0 || { rm -f libgnunetgnsrecord.so.0 && ln -s libgnunetgnsrecord.so.0.0.0 libgnunetgnsrecord.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetgnsrecord.so.0.0.0 libgnunetgnsrecord.so || { rm -f libgnunetgnsrecord.so && ln -s libgnunetgnsrecord.so.0.0.0 libgnunetgnsrecord.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetgnsrecord.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetgnsrecord.la
OpenWrt-libtool: install: warning: relinking `libgnunetgnsrecordjson.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gnsrecord; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 0:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetgnsrecordjson.la -rpath /usr/lib json_gnsrecord.lo ../../src/util/libgnunetutil.la ../../src/identity/libgnunetidentity.la libgnunetgnsrecord.la -ljansson -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetgnsrecordjson.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetgnsrecordjson.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetgnsrecordjson.so.0.0.0 libgnunetgnsrecordjson.so.0 || { rm -f libgnunetgnsrecordjson.so.0 && ln -s libgnunetgnsrecordjson.so.0.0.0 libgnunetgnsrecordjson.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetgnsrecordjson.so.0.0.0 libgnunetgnsrecordjson.so || { rm -f libgnunetgnsrecordjson.so && ln -s libgnunetgnsrecordjson.so.0.0.0 libgnunetgnsrecordjson.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetgnsrecordjson.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetgnsrecordjson.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-gnsrecord-tvg '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `libgnunetgnsrecord.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-gnsrecord-tvg /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-gnsrecord-tvg
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunet_plugin_gnsrecord_dns.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_gnsrecord_dns.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gnsrecord; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_gnsrecord_dns.la -rpath /usr/lib/gnunet plugin_gnsrecord_dns.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_gnsrecord_dns.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_gnsrecord_dns.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_gnsrecord_dns.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_gnsrecord_dns.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/gnunet'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gnsrecord'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gnsrecord'
Making install in namecache
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/namecache'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/namecache'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetnamecache.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetnamecache.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/namecache; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 0:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetnamecache.la -rpath /usr/lib namecache_api.lo ../../src/gnsrecord/libgnunetgnsrecord.la ../../src/identity/libgnunetidentity.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetnamecache.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetnamecache.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetnamecache.so.0.0.0 libgnunetnamecache.so.0 || { rm -f libgnunetnamecache.so.0 && ln -s libgnunetnamecache.so.0.0.0 libgnunetnamecache.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetnamecache.so.0.0.0 libgnunetnamecache.so || { rm -f libgnunetnamecache.so && ln -s libgnunetnamecache.so.0.0.0 libgnunetnamecache.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetnamecache.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetnamecache.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-namecache '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `../../src/gnsrecord/libgnunetgnsrecord.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `libgnunetnamecache.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gnsrecord/libgnunetgnsrecord.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-namecache /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-namecache
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-namecache '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `../../src/gnsrecord/libgnunetgnsrecord.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `libgnunetnamecache.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gnsrecord/libgnunetgnsrecord.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-namecache /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-namecache
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 namecache.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunet_plugin_namecache_sqlite.la libgnunet_plugin_namecache_flat.la libgnunet_plugin_namecache_postgres.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_namecache_sqlite.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/namecache; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_namecache_sqlite.la -rpath /usr/lib/gnunet plugin_namecache_sqlite.lo libgnunetnamecache.la ../../src/sq/libgnunetsq.la ../../src/statistics/libgnunetstatistics.la ../../src/gnsrecord/libgnunetgnsrecord.la ../../src/identity/libgnunetidentity.la ../../src/util/libgnunetutil.la -lsqlite3 -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_namecache_sqlite.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_namecache_sqlite.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_namecache_sqlite.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_namecache_sqlite.la
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_namecache_flat.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/namecache; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_namecache_flat.la -rpath /usr/lib/gnunet plugin_namecache_flat.lo libgnunetnamecache.la ../../src/statistics/libgnunetstatistics.la ../../src/gnsrecord/libgnunetgnsrecord.la ../../src/identity/libgnunetidentity.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_namecache_flat.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_namecache_flat.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_namecache_flat.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_namecache_flat.la
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_namecache_postgres.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/namecache; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_namecache_postgres.la -rpath /usr/lib/gnunet plugin_namecache_postgres.lo libgnunetnamecache.la ../../src/pq/libgnunetpq.la ../../src/statistics/libgnunetstatistics.la ../../src/gnsrecord/libgnunetgnsrecord.la ../../src/identity/libgnunetidentity.la ../../src/util/libgnunetutil.la -lpq -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_namecache_postgres.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_namecache_postgres.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_namecache_postgres.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_namecache_postgres.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/gnunet'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/namecache'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/namecache'
Making install in namestore
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/namestore'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/namestore'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetnamestore.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetnamestore.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/namestore; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 0:1:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetnamestore.la -rpath /usr/lib namestore_api.lo namestore_api_monitor.lo ../../src/gnsrecord/libgnunetgnsrecord.la ../../src/identity/libgnunetidentity.la ../../src/statistics/libgnunetstatistics.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetnamestore.so.0.0.1T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetnamestore.so.0.0.1
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetnamestore.so.0.0.1 libgnunetnamestore.so.0 || { rm -f libgnunetnamestore.so.0 && ln -s libgnunetnamestore.so.0.0.1 libgnunetnamestore.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetnamestore.so.0.0.1 libgnunetnamestore.so || { rm -f libgnunetnamestore.so && ln -s libgnunetnamestore.so.0.0.1 libgnunetnamestore.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetnamestore.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetnamestore.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-namestore gnunet-zoneimport '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `../../src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/gnsrecord/libgnunetgnsrecord.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `libgnunetnamestore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gnsrecord/libgnunetgnsrecord.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-namestore /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-namestore
OpenWrt-libtool: install: warning: `libgnunetnamestore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gnsrecord/libgnunetgnsrecord.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/gnsrecord/libgnunetgnsrecord.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-zoneimport /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-zoneimport
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-namestore gnunet-namestore-fcfsd '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `../../src/namecache/libgnunetnamecache.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/gnsrecord/libgnunetgnsrecord.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `libgnunetnamestore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gnsrecord/libgnunetgnsrecord.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-namestore /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-namestore
OpenWrt-libtool: install: warning: `../../src/gnsrecord/libgnunetgnsrecord.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `libgnunetnamestore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gnsrecord/libgnunetgnsrecord.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-namestore-fcfsd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-namestore-fcfsd
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 namestore.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunet_plugin_namestore_sqlite.la libgnunet_plugin_namestore_postgres.la libgnunet_plugin_namestore_flat.la libgnunet_plugin_rest_namestore.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_namestore_sqlite.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/namestore; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_namestore_sqlite.la -rpath /usr/lib/gnunet plugin_namestore_sqlite.lo ../../src/gnsrecord/libgnunetgnsrecord.la ../../src/identity/libgnunetidentity.la ../../src/sq/libgnunetsq.la ../../src/statistics/libgnunetstatistics.la ../../src/util/libgnunetutil.la -lsqlite3 -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_namestore_sqlite.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_namestore_sqlite.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_namestore_sqlite.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_namestore_sqlite.la
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_namestore_postgres.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/namestore; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_namestore_postgres.la -rpath /usr/lib/gnunet plugin_namestore_postgres.lo ../../src/gnsrecord/libgnunetgnsrecord.la ../../src/identity/libgnunetidentity.la ../../src/pq/libgnunetpq.la ../../src/statistics/libgnunetstatistics.la ../../src/util/libgnunetutil.la -lpq -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_namestore_postgres.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_namestore_postgres.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_namestore_postgres.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_namestore_postgres.la
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_namestore_flat.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/namestore; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_namestore_flat.la -rpath /usr/lib/gnunet plugin_namestore_flat.lo ../../src/gnsrecord/libgnunetgnsrecord.la ../../src/identity/libgnunetidentity.la ../../src/statistics/libgnunetstatistics.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_namestore_flat.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_namestore_flat.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_namestore_flat.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_namestore_flat.la
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_rest_namestore.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/namestore; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_rest_namestore.la -rpath /usr/lib/gnunet libgnunet_plugin_rest_namestore_la-plugin_rest_namestore.lo libgnunetnamestore.la ../../src/rest/libgnunetrest.la ../../src/identity/libgnunetidentity.la ../../src/json/libgnunetjson.la ../../src/gnsrecord/libgnunetgnsrecord.la ../../src/gnsrecord/libgnunetgnsrecordjson.la ../../src/util/libgnunetutil.la -ljansson -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lmicrohttpd -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_rest_namestore.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_rest_namestore.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_rest_namestore.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_rest_namestore.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/gnunet'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/namestore'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/namestore'
Making install in peerinfo-tool
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/peerinfo-tool'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/peerinfo-tool'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-peerinfo '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `../../src/peerinfo/libgnunetpeerinfo.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/transport/libgnunettransport.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats/libgnunetats.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-peerinfo /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-peerinfo
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunet_plugin_rest_peerinfo.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_rest_peerinfo.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/peerinfo-tool; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_rest_peerinfo.la -rpath /usr/lib/gnunet libgnunet_plugin_rest_peerinfo_la-plugin_rest_peerinfo.lo ../../src/hello/libgnunethello.la ../../src/peerinfo/libgnunetpeerinfo.la ../../src/transport/libgnunettransport.la ../../src/ats/libgnunetats.la ../../src/rest/libgnunetrest.la ../../src/json/libgnunetjson.la ../../src/util/libgnunetutil.la -ljansson -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lmicrohttpd -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_rest_peerinfo.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_rest_peerinfo.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_rest_peerinfo.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_rest_peerinfo.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/gnunet'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/peerinfo-tool'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/peerinfo-tool'
Making install in cadet
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/cadet'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/cadet'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetcadet.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetcadet.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/cadet; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 7:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetcadet.la -rpath /usr/lib cadet_api.lo cadet_api_drop_message.lo cadet_api_get_channel.lo cadet_api_get_path.lo cadet_api_list_peers.lo cadet_api_list_tunnels.lo cadet_api_helper.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetcadet.so.7.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetcadet.so.7.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetcadet.so.7.0.0 libgnunetcadet.so.7 || { rm -f libgnunetcadet.so.7 && ln -s libgnunetcadet.so.7.0.0 libgnunetcadet.so.7; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetcadet.so.7.0.0 libgnunetcadet.so || { rm -f libgnunetcadet.so && ln -s libgnunetcadet.so.7.0.0 libgnunetcadet.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetcadet.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetcadet.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-cadet '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `libgnunetcadet.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-cadet /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-cadet
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-cadet '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/ats/libgnunetats.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/core/libgnunetcore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/dht/libgnunetdht.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/transport/libgnunettransport.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats/libgnunetats.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/peerinfo/libgnunetpeerinfo.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/block/libgnunetblock.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-cadet /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-cadet
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 cadet.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/cadet'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/cadet'
Making install in set
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/set'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/set'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetset.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetset.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/set; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetset.la -rpath /usr/lib set_api.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetset.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetset.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetset.so.0.0.0 libgnunetset.so.0 || { rm -f libgnunetset.so.0 && ln -s libgnunetset.so.0.0.0 libgnunetset.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetset.so.0.0.0 libgnunetset.so || { rm -f libgnunetset.so && ln -s libgnunetset.so.0.0.0 libgnunetset.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetset.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetset.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-set-profiler '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `libgnunetset.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/testing/libgnunettesting.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/arm/libgnunetarm.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-set-profiler /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-set-profiler
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-set '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/core/libgnunetcore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/cadet/libgnunetcadet.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/block/libgnunetblock.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `libgnunetset.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-set /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-set
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 set.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunet_plugin_block_set_test.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_block_set_test.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/set; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_block_set_test.la -rpath /usr/lib/gnunet plugin_block_set_test.lo ../../src/block/libgnunetblock.la ../../src/block/libgnunetblockgroup.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_block_set_test.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_block_set_test.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_block_set_test.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_block_set_test.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/gnunet'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/set'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/set'
Making install in seti
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/seti'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/seti'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetseti.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetseti.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/seti; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetseti.la -rpath /usr/lib seti_api.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetseti.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetseti.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetseti.so.0.0.0 libgnunetseti.so.0 || { rm -f libgnunetseti.so.0 && ln -s libgnunetseti.so.0.0.0 libgnunetseti.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetseti.so.0.0.0 libgnunetseti.so || { rm -f libgnunetseti.so && ln -s libgnunetseti.so.0.0.0 libgnunetseti.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetseti.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetseti.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-seti-profiler '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `libgnunetseti.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/testing/libgnunettesting.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/arm/libgnunetarm.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-seti-profiler /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-seti-profiler
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-seti '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/core/libgnunetcore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/cadet/libgnunetcadet.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/block/libgnunetblock.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `libgnunetseti.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-seti /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-seti
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 seti.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunet_plugin_block_seti_test.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_block_seti_test.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/seti; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_block_seti_test.la -rpath /usr/lib/gnunet plugin_block_seti_test.lo ../../src/block/libgnunetblock.la ../../src/block/libgnunetblockgroup.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_block_seti_test.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_block_seti_test.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_block_seti_test.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_block_seti_test.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/gnunet'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/seti'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/seti'
Making install in setu
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/setu'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/setu'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetsetu.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetsetu.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/setu; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetsetu.la -rpath /usr/lib setu_api.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetsetu.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetsetu.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetsetu.so.0.0.0 libgnunetsetu.so.0 || { rm -f libgnunetsetu.so.0 && ln -s libgnunetsetu.so.0.0.0 libgnunetsetu.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetsetu.so.0.0.0 libgnunetsetu.so || { rm -f libgnunetsetu.so && ln -s libgnunetsetu.so.0.0.0 libgnunetsetu.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetsetu.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetsetu.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-setu-profiler '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `libgnunetsetu.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/testing/libgnunettesting.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/arm/libgnunetarm.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-setu-profiler /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-setu-profiler
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-setu '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/core/libgnunetcore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/cadet/libgnunetcadet.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/block/libgnunetblock.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `libgnunetsetu.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-setu /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-setu
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 setu.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunet_plugin_block_setu_test.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_block_setu_test.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/setu; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_block_setu_test.la -rpath /usr/lib/gnunet plugin_block_setu_test.lo ../../src/block/libgnunetblock.la ../../src/block/libgnunetblockgroup.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_block_setu_test.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_block_setu_test.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_block_setu_test.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_block_setu_test.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/gnunet'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/setu'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/setu'
Making install in consensus
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/consensus'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/consensus'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetconsensus.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetconsensus.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/consensus; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetconsensus.la -rpath /usr/lib consensus_api.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetconsensus.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetconsensus.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetconsensus.so.0.0.0 libgnunetconsensus.so.0 || { rm -f libgnunetconsensus.so.0 && ln -s libgnunetconsensus.so.0.0.0 libgnunetconsensus.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetconsensus.so.0.0.0 libgnunetconsensus.so || { rm -f libgnunetconsensus.so && ln -s libgnunetconsensus.so.0.0.0 libgnunetconsensus.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetconsensus.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetconsensus.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-consensus-profiler '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `libgnunetconsensus.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/testbed/libgnunettestbed.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/transport/libgnunettransport.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats/libgnunetats.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/testing/libgnunettesting.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/arm/libgnunetarm.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-consensus-profiler /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-consensus-profiler
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-consensus gnunet-service-evil-consensus '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/core/libgnunetcore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/set/libgnunetset.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-consensus /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-consensus
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/core/libgnunetcore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/set/libgnunetset.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-evil-consensus /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-evil-consensus
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 consensus.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunet_plugin_block_consensus.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_block_consensus.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/consensus; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_block_consensus.la -rpath /usr/lib/gnunet plugin_block_consensus.lo ../../src/block/libgnunetblock.la ../../src/block/libgnunetblockgroup.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_block_consensus.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_block_consensus.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_block_consensus.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_block_consensus.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/gnunet'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/consensus'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/consensus'
Making install in revocation
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/revocation'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/revocation'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetrevocation.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetrevocation.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/revocation; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 0:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetrevocation.la -rpath /usr/lib revocation_api.lo ../../src/util/libgnunetutil.la ../../src/identity/libgnunetidentity.la -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lgcrypt -lgpg-error -lgcrypt -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetrevocation.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetrevocation.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetrevocation.so.0.0.0 libgnunetrevocation.so.0 || { rm -f libgnunetrevocation.so.0 && ln -s libgnunetrevocation.so.0.0.0 libgnunetrevocation.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetrevocation.so.0.0.0 libgnunetrevocation.so || { rm -f libgnunetrevocation.so && ln -s libgnunetrevocation.so.0.0.0 libgnunetrevocation.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetrevocation.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetrevocation.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-revocation gnunet-revocation-tvg '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `libgnunetrevocation.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-revocation /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-revocation
OpenWrt-libtool: install: warning: `libgnunetrevocation.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-revocation-tvg /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-revocation-tvg
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-revocation '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `libgnunetrevocation.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/core/libgnunetcore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/setu/libgnunetsetu.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-revocation /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-revocation
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 revocation.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunet_plugin_block_revocation.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_block_revocation.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/revocation; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_block_revocation.la -rpath /usr/lib/gnunet plugin_block_revocation.lo libgnunetrevocation.la ../../src/block/libgnunetblockgroup.la ../../src/block/libgnunetblock.la ../../src/util/libgnunetutil.la ../../src/identity/libgnunetidentity.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_block_revocation.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_block_revocation.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_block_revocation.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_block_revocation.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/gnunet'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/revocation'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/revocation'
Making install in vpn
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/vpn'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/vpn'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetvpn.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetvpn.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/vpn; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetvpn.la -rpath /usr/lib vpn_api.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetvpn.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetvpn.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetvpn.so.0.0.0 libgnunetvpn.so.0 || { rm -f libgnunetvpn.so.0 && ln -s libgnunetvpn.so.0.0.0 libgnunetvpn.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetvpn.so.0.0.0 libgnunetvpn.so || { rm -f libgnunetvpn.so && ln -s libgnunetvpn.so.0.0.0 libgnunetvpn.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetvpn.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetvpn.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-vpn '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `libgnunetvpn.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-vpn /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-vpn
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-helper-vpn gnunet-service-vpn '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c gnunet-helper-vpn /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-helper-vpn
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/cadet/libgnunetcadet.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/regex/libgnunetregex.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-vpn /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-vpn
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 vpn.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/vpn'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/vpn'
Making install in gns
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gns'
Making install in .
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gns'
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gns'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetgns.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetgns.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gns; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetgns.la -rpath /usr/lib gns_api.lo gns_tld_api.lo ../../src/util/libgnunetutil.la ../../src/identity/libgnunetidentity.la ../../src/gnsrecord/libgnunetgnsrecord.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetgns.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetgns.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetgns.so.0.0.0 libgnunetgns.so.0 || { rm -f libgnunetgns.so.0 && ln -s libgnunetgns.so.0.0.0 libgnunetgns.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetgns.so.0.0.0 libgnunetgns.so || { rm -f libgnunetgns.so && ln -s libgnunetgns.so.0.0.0 libgnunetgns.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetgns.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetgns.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-gns gnunet-bcd '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `libgnunetgns.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gnsrecord/libgnunetgnsrecord.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/gnsrecord/libgnunetgnsrecord.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-gns /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-gns
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-bcd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-bcd
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
 /openwrt/staging_dir/host/bin/install -c gnunet-gns-proxy-setup-ca '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-gns gnunet-dns2gns '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `../../src/gnsrecord/libgnunetgnsrecord.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/revocation/libgnunetrevocation.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/dns/libgnunetdns.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/dht/libgnunetdht.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/namecache/libgnunetnamecache.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gnsrecord/libgnunetgnsrecord.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/vpn/libgnunetvpn.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-gns /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-gns
OpenWrt-libtool: install: warning: `../../src/gnsrecord/libgnunetgnsrecord.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `libgnunetgns.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gnsrecord/libgnunetgnsrecord.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-dns2gns /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-dns2gns
make  install-exec-hook
make[9]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gns'
setcap 'cap_net_bind_service=+ep' /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec//gnunet-dns2gns || true
/bin/bash: setcap: command not found
make[9]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gns'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 gns.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet'
 /openwrt/staging_dir/host/bin/install -c -m 644 gnunet-gns-proxy-ca.template '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunet_plugin_block_gns.la libgnunet_plugin_gnsrecord_gns.la libgnunet_plugin_rest_gns.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_block_gns.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gns; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_block_gns.la -rpath /usr/lib/gnunet plugin_block_gns.lo ../../src/util/libgnunetutil.la ../../src/block/libgnunetblock.la ../../src/block/libgnunetblockgroup.la ../../src/identity/libgnunetidentity.la ../../src/gnsrecord/libgnunetgnsrecord.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_block_gns.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_block_gns.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_block_gns.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_block_gns.la
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_gnsrecord_gns.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gns; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_gnsrecord_gns.la -rpath /usr/lib/gnunet plugin_gnsrecord_gns.lo ../../src/gnsrecord/libgnunetgnsrecord.la ../../src/identity/libgnunetidentity.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_gnsrecord_gns.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_gnsrecord_gns.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_gnsrecord_gns.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_gnsrecord_gns.la
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_rest_gns.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gns; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_rest_gns.la -rpath /usr/lib/gnunet libgnunet_plugin_rest_gns_la-plugin_rest_gns.lo ../../src/gnsrecord/libgnunetgnsrecord.la ../../src/gnsrecord/libgnunetgnsrecordjson.la libgnunetgns.la ../../src/rest/libgnunetrest.la ../../src/identity/libgnunetidentity.la ../../src/json/libgnunetjson.la ../../src/util/libgnunetutil.la -ljansson -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lmicrohttpd -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_rest_gns.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_rest_gns.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_rest_gns.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_rest_gns.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/gnunet'
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gns'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gns'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gns'
Making install in zonemaster
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/zonemaster'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/zonemaster'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-zonemaster gnunet-service-zonemaster-monitor '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `../../src/dht/libgnunetdht.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/gnsrecord/libgnunetgnsrecord.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/namestore/libgnunetnamestore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gnsrecord/libgnunetgnsrecord.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-zonemaster /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-zonemaster
OpenWrt-libtool: install: warning: `../../src/dht/libgnunetdht.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/gnsrecord/libgnunetgnsrecord.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/namestore/libgnunetnamestore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gnsrecord/libgnunetgnsrecord.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-zonemaster-monitor /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-zonemaster-monitor
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 zonemaster.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/zonemaster'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/zonemaster'
Making install in conversation
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/conversation'
Making install in .
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/conversation'
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/conversation'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetmicrophone.la libgnunetspeaker.la libgnunetconversation.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetmicrophone.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/conversation; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 0:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetmicrophone.la -rpath /usr/lib microphone.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetmicrophone.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetmicrophone.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetmicrophone.so.0.0.0 libgnunetmicrophone.so.0 || { rm -f libgnunetmicrophone.so.0 && ln -s libgnunetmicrophone.so.0.0.0 libgnunetmicrophone.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetmicrophone.so.0.0.0 libgnunetmicrophone.so || { rm -f libgnunetmicrophone.so && ln -s libgnunetmicrophone.so.0.0.0 libgnunetmicrophone.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetmicrophone.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetmicrophone.la
OpenWrt-libtool: install: warning: relinking `libgnunetspeaker.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/conversation; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 0:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetspeaker.la -rpath /usr/lib speaker.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetspeaker.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetspeaker.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetspeaker.so.0.0.0 libgnunetspeaker.so.0 || { rm -f libgnunetspeaker.so.0 && ln -s libgnunetspeaker.so.0.0.0 libgnunetspeaker.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetspeaker.so.0.0.0 libgnunetspeaker.so || { rm -f libgnunetspeaker.so && ln -s libgnunetspeaker.so.0.0.0 libgnunetspeaker.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetspeaker.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetspeaker.la
OpenWrt-libtool: install: warning: relinking `libgnunetconversation.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/conversation; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 0:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetconversation.la -rpath /usr/lib conversation_api.lo conversation_api_call.lo ../../src/gns/libgnunetgns.la ../../src/gnsrecord/libgnunetgnsrecord.la ../../src/namestore/libgnunetnamestore.la ../../src/identity/libgnunetidentity.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetconversation.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetconversation.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetconversation.so.0.0.0 libgnunetconversation.so.0 || { rm -f libgnunetconversation.so.0 && ln -s libgnunetconversation.so.0.0.0 libgnunetconversation.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetconversation.so.0.0.0 libgnunetconversation.so || { rm -f libgnunetconversation.so && ln -s libgnunetconversation.so.0.0.0 libgnunetconversation.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetconversation.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetconversation.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-conversation-test gnunet-conversation '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `libgnunetmicrophone.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `libgnunetspeaker.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-conversation-test /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-conversation-test
OpenWrt-libtool: install: warning: `libgnunetmicrophone.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `libgnunetspeaker.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `libgnunetconversation.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gns/libgnunetgns.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/namestore/libgnunetnamestore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/gns/libgnunetgns.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/gnsrecord/libgnunetgnsrecord.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/namestore/libgnunetnamestore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gnsrecord/libgnunetgnsrecord.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-conversation /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-conversation
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-conversation gnunet-helper-audio-record gnunet-helper-audio-playback '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `libgnunetconversation.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gns/libgnunetgns.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/namestore/libgnunetnamestore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gnsrecord/libgnunetgnsrecord.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `libgnunetspeaker.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `libgnunetmicrophone.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/cadet/libgnunetcadet.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-conversation /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-conversation
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-helper-audio-record /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-helper-audio-record
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-helper-audio-playback /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-helper-audio-playback
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 conversation.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunet_plugin_gnsrecord_conversation.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_gnsrecord_conversation.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/conversation; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_gnsrecord_conversation.la -rpath /usr/lib/gnunet plugin_gnsrecord_conversation.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_gnsrecord_conversation.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_gnsrecord_conversation.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_gnsrecord_conversation.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_gnsrecord_conversation.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/gnunet'
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/conversation'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/conversation'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/conversation'
Making install in fs
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/fs'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/fs'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetfs.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetfs.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/fs; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 3:1:1 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetfs.la -rpath /usr/lib fs_api.lo fs_directory.lo fs_dirmetascan.lo fs_download.lo fs_file_information.lo fs_getopt.lo fs_list_indexed.lo fs_publish.lo fs_publish_ksk.lo fs_publish_ublock.lo fs_misc.lo fs_namespace.lo fs_search.lo fs_sharetree.lo fs_tree.lo fs_unindex.lo fs_uri.lo ../../src/datastore/libgnunetdatastore.la ../../src/statistics/libgnunetstatistics.la ../../src/util/libgnunetutil.la -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lgcrypt -lgpg-error -lunistring -lextractor -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetfs.so.2.1.1T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetfs.so.2.1.1
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetfs.so.2.1.1 libgnunetfs.so.2 || { rm -f libgnunetfs.so.2 && ln -s libgnunetfs.so.2.1.1 libgnunetfs.so.2; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetfs.so.2.1.1 libgnunetfs.so || { rm -f libgnunetfs.so && ln -s libgnunetfs.so.2.1.1 libgnunetfs.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetfs.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetfs.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-auto-share gnunet-directory gnunet-download gnunet-publish gnunet-search gnunet-fs gnunet-unindex '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-auto-share /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-auto-share
OpenWrt-libtool: install: warning: `libgnunetfs.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/datastore/libgnunetdatastore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-directory /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-directory
OpenWrt-libtool: install: warning: `libgnunetfs.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/datastore/libgnunetdatastore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-download /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-download
OpenWrt-libtool: install: warning: `../../src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `libgnunetfs.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/datastore/libgnunetdatastore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-publish /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-publish
OpenWrt-libtool: install: warning: `libgnunetfs.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/datastore/libgnunetdatastore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-search /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-search
OpenWrt-libtool: install: warning: `libgnunetfs.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/datastore/libgnunetdatastore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-fs /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-fs
OpenWrt-libtool: install: warning: `libgnunetfs.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/datastore/libgnunetdatastore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-unindex /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-unindex
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-helper-fs-publish gnunet-service-fs '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-helper-fs-publish /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-helper-fs-publish
OpenWrt-libtool: install: warning: `libgnunetfs.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/datastore/libgnunetdatastore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/dht/libgnunetdht.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/block/libgnunetblock.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/datastore/libgnunetdatastore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/cadet/libgnunetcadet.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/ats/libgnunetats.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/core/libgnunetcore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/peerstore/libgnunetpeerstore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-fs /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-fs
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 fs.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunet_plugin_block_fs.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_block_fs.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/fs; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_block_fs.la -rpath /usr/lib/gnunet plugin_block_fs.lo ../../src/block/libgnunetblockgroup.la ../../src/block/libgnunetblock.la libgnunetfs.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_block_fs.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_block_fs.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_block_fs.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_block_fs.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/gnunet'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/fs'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/fs'
Making install in exit
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/exit'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/exit'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-daemon-exit gnunet-helper-exit '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `../../src/dht/libgnunetdht.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/cadet/libgnunetcadet.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/regex/libgnunetregex.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-daemon-exit /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-daemon-exit
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c gnunet-helper-exit /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-helper-exit
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 exit.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/exit'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/exit'
Making install in pt
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/pt'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/pt'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-daemon-pt '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `../../src/vpn/libgnunetvpn.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/cadet/libgnunetcadet.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/dht/libgnunetdht.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/dns/libgnunetdns.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-daemon-pt /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-daemon-pt
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 pt.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/pt'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/pt'
Making install in secretsharing
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/secretsharing'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/secretsharing'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetsecretsharing.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetsecretsharing.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/secretsharing; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetsecretsharing.la -rpath /usr/lib secretsharing_api.lo secretsharing_common.lo ../../src/util/libgnunetutil.la -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lgcrypt -lgpg-error -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetsecretsharing.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetsecretsharing.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetsecretsharing.so.0.0.0 libgnunetsecretsharing.so.0 || { rm -f libgnunetsecretsharing.so.0 && ln -s libgnunetsecretsharing.so.0.0.0 libgnunetsecretsharing.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetsecretsharing.so.0.0.0 libgnunetsecretsharing.so || { rm -f libgnunetsecretsharing.so && ln -s libgnunetsecretsharing.so.0.0.0 libgnunetsecretsharing.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetsecretsharing.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetsecretsharing.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-secretsharing-profiler '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `libgnunetsecretsharing.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/testbed/libgnunettestbed.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/transport/libgnunettransport.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/ats/libgnunetats.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/testing/libgnunettesting.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/arm/libgnunetarm.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-secretsharing-profiler /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-secretsharing-profiler
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-secretsharing '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/consensus/libgnunetconsensus.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-secretsharing /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-secretsharing
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 secretsharing.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/secretsharing'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/secretsharing'
Making install in reclaim
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/reclaim'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/reclaim'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetreclaim.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetreclaim.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/reclaim; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 0:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetreclaim.la -rpath /usr/lib reclaim_api.lo reclaim_attribute.lo reclaim_credential.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetreclaim.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetreclaim.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetreclaim.so.0.0.0 libgnunetreclaim.so.0 || { rm -f libgnunetreclaim.so.0 && ln -s libgnunetreclaim.so.0.0.0 libgnunetreclaim.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetreclaim.so.0.0.0 libgnunetreclaim.so || { rm -f libgnunetreclaim.so && ln -s libgnunetreclaim.so.0.0.0 libgnunetreclaim.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetreclaim.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetreclaim.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-reclaim '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/namestore/libgnunetnamestore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gnsrecord/libgnunetgnsrecord.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `libgnunetreclaim.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-reclaim /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-reclaim
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-reclaim '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `../../src/gnsrecord/libgnunetgnsrecord.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/namestore/libgnunetnamestore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `libgnunetreclaim.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/gns/libgnunetgns.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/gnsrecord/libgnunetgnsrecord.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-reclaim /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-reclaim
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 reclaim.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunet_plugin_gnsrecord_reclaim.la libgnunet_plugin_reclaim_attribute_basic.la libgnunet_plugin_reclaim_credential_jwt.la libgnunet_plugin_rest_openid_connect.la libgnunet_plugin_rest_reclaim.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet'
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_gnsrecord_reclaim.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/reclaim; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_gnsrecord_reclaim.la -rpath /usr/lib/gnunet plugin_gnsrecord_reclaim.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_gnsrecord_reclaim.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_gnsrecord_reclaim.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_gnsrecord_reclaim.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_gnsrecord_reclaim.la
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_reclaim_attribute_basic.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/reclaim; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_reclaim_attribute_basic.la -rpath /usr/lib/gnunet plugin_reclaim_attribute_basic.lo ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_reclaim_attribute_basic.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_reclaim_attribute_basic.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_reclaim_attribute_basic.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_reclaim_attribute_basic.la
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_reclaim_credential_jwt.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/reclaim; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_reclaim_credential_jwt.la -rpath /usr/lib/gnunet plugin_reclaim_credential_jwt.lo ../../src/util/libgnunetutil.la libgnunetreclaim.la -ljansson -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_reclaim_credential_jwt.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_reclaim_credential_jwt.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_reclaim_credential_jwt.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_reclaim_credential_jwt.la
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_rest_openid_connect.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/reclaim; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_rest_openid_connect.la -rpath /usr/lib/gnunet libgnunet_plugin_rest_openid_connect_la-plugin_rest_openid_connect.lo libgnunet_plugin_rest_openid_connect_la-oidc_helper.lo ../../src/identity/libgnunetidentity.la libgnunetreclaim.la ../../src/rest/libgnunetrest.la ../../src/namestore/libgnunetnamestore.la ../../src/gns/libgnunetgns.la ../../src/gnsrecord/libgnunetgnsrecord.la ../../src/util/libgnunetutil.la -ljansson -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lmicrohttpd -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lgcrypt -lgpg-error -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_rest_openid_connect.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_rest_openid_connect.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_rest_openid_connect.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_rest_openid_connect.la
OpenWrt-libtool: install: warning: relinking `libgnunet_plugin_rest_reclaim.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/reclaim; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -avoid-version -module -no-undefined -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunet_plugin_rest_reclaim.la -rpath /usr/lib/gnunet libgnunet_plugin_rest_reclaim_la-plugin_rest_reclaim.lo libgnunet_plugin_rest_reclaim_la-json_reclaim.lo ../../src/identity/libgnunetidentity.la libgnunetreclaim.la ../../src/json/libgnunetjson.la ../../src/gnsrecord/libgnunetgnsrecord.la ../../src/rest/libgnunetrest.la ../../src/namestore/libgnunetnamestore.la ../../src/util/libgnunetutil.la -ljansson -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lmicrohttpd -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_rest_reclaim.soT /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_rest_reclaim.so
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunet_plugin_rest_reclaim.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libgnunet_plugin_rest_reclaim.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib/gnunet'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/reclaim'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/reclaim'
Making install in rps
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/rps'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/rps'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetrps.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetrps.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/rps; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 0:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetrps.la -rpath /usr/lib libgnunetrps_la-gnunet-service-rps_sampler_elem.lo libgnunetrps_la-rps-test_util.lo libgnunetrps_la-rps-sampler_common.lo libgnunetrps_la-rps-sampler_client.lo libgnunetrps_la-rps_api.lo ../../src/nse/libgnunetnse.la ../../src/util/libgnunetutil.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetrps.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetrps.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetrps.so.0.0.0 libgnunetrps.so.0 || { rm -f libgnunetrps.so.0 && ln -s libgnunetrps.so.0.0.0 libgnunetrps.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetrps.so.0.0.0 libgnunetrps.so || { rm -f libgnunetrps.so && ln -s libgnunetrps.so.0.0.0 libgnunetrps.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetrps.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetrps.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-rps '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `libgnunetrps.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nse/libgnunetnse.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-rps /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-rps
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-rps '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `libgnunetrps.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/nse/libgnunetnse.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/cadet/libgnunetcadet.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/peerinfo/libgnunetpeerinfo.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/hello/libgnunethello.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/nse/libgnunetnse.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/statistics/libgnunetstatistics.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/core/libgnunetcore.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-rps /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-rps
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 rps.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/rps'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/rps'
Making install in messenger
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/messenger'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/messenger'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetmessenger.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetmessenger.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/messenger; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 0:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetmessenger.la -rpath /usr/lib messenger_api.lo messenger_api_contact.lo messenger_api_contact_store.lo messenger_api_message.lo messenger_api_list_tunnels.lo messenger_api_util.lo messenger_api_handle.lo messenger_api_room.lo ../../src/util/libgnunetutil.la ../../src/cadet/libgnunetcadet.la ../../src/identity/libgnunetidentity.la -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetmessenger.so.0.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetmessenger.so.0.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetmessenger.so.0.0.0 libgnunetmessenger.so.0 || { rm -f libgnunetmessenger.so.0 && ln -s libgnunetmessenger.so.0.0.0 libgnunetmessenger.so.0; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetmessenger.so.0.0.0 libgnunetmessenger.so || { rm -f libgnunetmessenger.so && ln -s libgnunetmessenger.so.0.0.0 libgnunetmessenger.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetmessenger.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetmessenger.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-messenger '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `libgnunetmessenger.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/cadet/libgnunetcadet.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-messenger /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-messenger
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-messenger '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `libgnunetmessenger.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/cadet/libgnunetcadet.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/cadet/libgnunetcadet.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `../../src/identity/libgnunetidentity.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: warning: `/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-messenger /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-messenger
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 messenger.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/messenger'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/messenger'
Making install in abe
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/abe'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/abe'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
 /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c   libgnunetabe.la '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib'
OpenWrt-libtool: install: warning: relinking `libgnunetabe.la'
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/abe; /bin/bash /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/libtool  --silent --tag CC --mode=relink ccache_cc -fno-strict-aliasing -Wall -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1=gnunet-0.14.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -export-dynamic -no-undefined -version-info 1:0:0 -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/pulseaudio -Wl,--unresolved-symbols=report-all -o libgnunetabe.la -rpath /usr/lib abe.lo -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lgcrypt -lgpg-error -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -liconv ../../src/util/libgnunetutil.la -lgmp -lgabe -lpbc -lglib-2.0 -lltdl -lz -lunistring -lm -inst-prefix-dir /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install)
OpenWrt-libtool: relink: warning: `/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetabe.so.1.0.0T /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetabe.so.1.0.0
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetabe.so.1.0.0 libgnunetabe.so.1 || { rm -f libgnunetabe.so.1 && ln -s libgnunetabe.so.1.0.0 libgnunetabe.so.1; }; })
OpenWrt-libtool: install: (cd /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib && { ln -s -f libgnunetabe.so.1.0.0 libgnunetabe.so || { rm -f libgnunetabe.so && ln -s libgnunetabe.so.1.0.0 libgnunetabe.so; }; })
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/libgnunetabe.lai /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetabe.la
OpenWrt-libtool: install: warning: remember to run `libtool --finish /usr/lib'
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/abe'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/abe'
Making install in auction
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/auction'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/auction'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-auction-create gnunet-auction-info gnunet-auction-join '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-auction-create /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-auction-create
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-auction-info /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-auction-info
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-auction-join /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-auction-join
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
  /bin/bash ../../libtool   --mode=install /openwrt/staging_dir/host/bin/install -c gnunet-service-auction '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/'
OpenWrt-libtool: install: warning: `../../src/util/libgnunetutil.la' has not been installed in `/usr/lib'
OpenWrt-libtool: install: /openwrt/staging_dir/host/bin/install -c .libs/gnunet-service-auction /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-auction
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
 /openwrt/staging_dir/host/bin/install -c -m 644 auction.conf '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/auction'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/auction'
Making install in integration-tests
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/integration-tests'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/integration-tests'
make[7]: Nothing to be done for 'install-exec-am'.
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/integration-tests'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src/integration-tests'
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src'
make[7]: Nothing to be done for 'install-exec-am'.
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src'
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/src'
Making install in po
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/po'
if test "gnunet" = "gettext-tools"; then \
  /usr/bin/mkdir -p /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gettext/po; \
  for file in Makefile.in.in remove-potcdate.sin quot.sed boldquot.sed en@quot.header en@boldquot.header insert-header.sin Rules-quot   Makevars.template; do \
    /openwrt/staging_dir/host/bin/install -c -m 644 ./$file \
		    /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gettext/po/$file; \
  done; \
  for file in Makevars; do \
    rm -f /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gettext/po/$file; \
  done; \
else \
  : ; \
fi
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/po'
Making install in pkgconfig
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/pkgconfig'
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/pkgconfig'
make[6]: Nothing to be done for 'install-exec-am'.
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/pkgconfig'
 /openwrt/staging_dir/host/bin/install -c -m 644 gnunetarm.pc gnunetats.pc gnunetblock.pc gnunetconsensus.pc gnunetconversation.pc gnunetcore.pc gnunetdatacache.pc gnunetdatastore.pc gnunetdht.pc gnunetdns.pc gnunetenv.pc gnunetfragmentation.pc gnunetfs.pc gnunetgns.pc gnunethello.pc gnunetidentity.pc gnunetcadet.pc gnunetmicrophone.pc gnunetmysql.pc gnunetnamestore.pc gnunetnat.pc gnunetnse.pc gnunetpeerinfo.pc gnunetregex.pc gnunetrevocation.pc gnunetrps.pc gnunetscalarproduct.pc gnunetset.pc gnunetspeaker.pc gnunetstatistics.pc gnunettestbed.pc gnunettesting.pc gnunettransport.pc gnunetutil.pc gnunetvpn.pc '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/pkgconfig'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/pkgconfig'
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/pkgconfig'
Making install in doc
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/doc'
Making install in doxygen
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/doc/doxygen'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/doc/doxygen'
make[7]: Nothing to be done for 'install-exec-am'.
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/doc/doxygen'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/doc/doxygen'
Making install in man
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/doc/man'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/doc/man'
make[7]: Nothing to be done for 'install-exec-am'.
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/man/man1'
 /openwrt/staging_dir/host/bin/install -c -m 644 gnunet-arm.1 gnunet-ats.1 gnunet-auto-share.1 gnunet-base32.1 gnunet-bcd.1 gnunet-bugreport.1 gnunet-config.1 gnunet-core.1 gnunet-conversation.1 gnunet-conversation-test.1 gnunet-directory.1 gnunet-dns2gns.1 gnunet-datastore.1 gnunet-download.1 gnunet-ecc.1 gnunet-fs.1 gnunet-gns.1 gnunet-gns-proxy.1 gnunet-gns-proxy-setup-ca.1 gnunet-identity.1 gnunet-cadet.1 gnunet-namecache.1 gnunet-namestore.1 gnunet-namestore-fcfsd.1 gnunet-nat.1 gnunet-nat-auto.1 gnunet-nat-server.1 gnunet-nse.1 gnunet-peerinfo.1 gnunet-publish.1 gnunet-qr.1 gnunet-reclaim.1 gnunet-resolver.1 gnunet-revocation.1 gnunet-scalarproduct.1 gnunet-scrypt.1 gnunet-search.1 gnunet-statistics.1 gnunet-testbed-profiler.1 gnunet-testing-run-service.1 '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/man/man1'
 /openwrt/staging_dir/host/bin/install -c -m 644 gnunet-timeout.1 gnunet-transport.1 gnunet-transport-certificate-creation.1 gnunet-unindex.1 gnunet-uri.1 gnunet-vpn.1 gnunet-zoneimport.1 '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/man/man1'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/man/man5'
 /openwrt/staging_dir/host/bin/install -c -m 644 gnunet.conf.5 '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/man/man5'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/man/man7'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/doc/man'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/doc/man'
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/doc'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/doc'
make[7]: Nothing to be done for 'install-exec-am'.
make[7]: Nothing to be done for 'install-data-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/doc'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/doc'
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/doc'
Making install in contrib
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib'
Making install in scripts
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/scripts'
Making install in gnunet-logread
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/scripts/gnunet-logread'
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/scripts/gnunet-logread'
make[8]: Nothing to be done for 'install-data-am'.
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/scripts/gnunet-logread'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/scripts/gnunet-logread'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/scripts'
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/scripts'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
 /openwrt/staging_dir/host/bin/install -c gnunet-bugreport gnunet-suidfix '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin'
make[8]: Nothing to be done for 'install-data-am'.
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/scripts'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/scripts'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/scripts'
Making install in hellos
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/hellos'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/hellos'
make[7]: Nothing to be done for 'install-exec-am'.
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/hellos'
 /openwrt/staging_dir/host/bin/install -c -m 644 Y924NSHMMZ1N1SQCE5TXF93ED6S6JY311K0QT86G9WJC68F6XVZ0 '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/hellos'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/hellos'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/hellos'
Making install in services
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/services'
Making install in openrc
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/services/openrc'
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/services/openrc'
make[8]: Nothing to be done for 'install-exec-am'.
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/services/openrc'
 /openwrt/staging_dir/host/bin/install -c -m 644 gnunet.initd '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/services/openrc'
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/services/openrc'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/services/openrc'
Making install in systemd
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/services/systemd'
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/services/systemd'
make[8]: Nothing to be done for 'install-exec-am'.
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/services/systemd'
 /openwrt/staging_dir/host/bin/install -c -m 644 gnunet.service '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/services/systemd'
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/services/systemd'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/services/systemd'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/services'
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/services'
make[8]: Nothing to be done for 'install-exec-am'.
make[8]: Nothing to be done for 'install-data-am'.
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/services'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/services'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib/services'
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib'
make[7]: Nothing to be done for 'install-exec-am'.
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet'
 /openwrt/staging_dir/host/bin/install -c -m 644 gns/gns-bcd.html gns/gns-bcd.tex gns/def.tex gns/gns-form-fields.xml gns/gns-form.xslt branding/logo/gnunet-logo.pdf branding/logo/gnunet-logo.png branding/logo/gnunet-logo-color.png testing_hostkeys.ecc build-common/sh/bin.sh/python.sh build-common/sh/lib.sh/existence.sh build-common/sh/lib.sh/existence_python.sh build-common/sh/lib.sh/msg.sh build-common/sh/lib.sh/progname.sh build-common/sh/lib.sh/version_gnunet.sh build-common/LICENSE '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib'
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/contrib'
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1'
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1'
make[6]: Nothing to be done for 'install-exec-am'.
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/doc/gnunet/'
 /openwrt/staging_dir/host/bin/install -c -m 644 COPYING README '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/doc/gnunet/'
 /usr/bin/mkdir -p '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/include/gnunet'
 /openwrt/staging_dir/host/bin/install -c -m 644 gnunet_config.h '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/include/gnunet'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1'
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1'
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1'
install: cannot stat '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-scalarproduct': No such file or directory
cp: cannot stat '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetscalarproduct.so*': No such file or directory
install: cannot stat '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-ats-new': No such file or directory
install: cannot stat '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-scalarproduct-alice': No such file or directory
install: cannot stat '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-scalarproduct-bob': No such file or directory
install: cannot stat '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-scalarproduct-ecc-alice': No such file or directory
install: cannot stat '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-scalarproduct-ecc-bob': No such file or directory
install: cannot stat '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/scalarproduct.conf': No such file or directory
install: cannot stat '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-scalarproduct': No such file or directory
cp: cannot stat '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetscalarproduct.so*': No such file or directory
install: cannot stat '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-ats-new': No such file or directory
install: cannot stat '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-scalarproduct-alice': No such file or directory
install: cannot stat '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-scalarproduct-bob': No such file or directory
install: cannot stat '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-scalarproduct-ecc-alice': No such file or directory
install: cannot stat '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-service-scalarproduct-ecc-bob': No such file or directory
install: cannot stat '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/share/gnunet/config.d/scalarproduct.conf': No such file or directory
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-uri: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-uri: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-arm: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-arm: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-config: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-config: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-transport: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-transport: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-nat-auto: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-nat-auto: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-core: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-core: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-nat-server: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-nat-server: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-identity: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-identity: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-nse: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-nse: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-statistics: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-statistics: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-ats: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-ats: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-cadet: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-cadet: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-revocation: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-revocation: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-peerstore: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-peerstore: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-peerinfo: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-peerinfo: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-ecc: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-ecc: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-scrypt: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-scrypt: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-nat: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/bin/gnunet-nat: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetset.so.0.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetset.so.0.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetdht.so.3.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetdht.so.3.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunettransportcore.so.0.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunettransportcore.so.0.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetarm.so.2.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetarm.so.2.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetcore.so.0.0.1: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetcore.so.0.0.1: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetregex.so.3.0.1: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetregex.so.3.0.1: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetats.so.4.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetats.so.4.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetfragmentation.so.2.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetfragmentation.so.2.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetblockgroup.so.0.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetblockgroup.so.0.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libgnunet_plugin_transport_unix.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libgnunet_plugin_transport_unix.so: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-set: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-set: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-nat: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-nat: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-peerinfo: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-peerinfo: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-arm: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-arm: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-identity: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-identity: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-daemon-topology: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-daemon-topology: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-helper-nat-client: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-peerstore: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-peerstore: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-helper-nat-server: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-transport: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-transport: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-ats: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-ats: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-timeout: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-regex: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-regex: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-statistics: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-statistics: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-cadet: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-cadet: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-nat-auto: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-nat-auto: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-core: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-core: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-setu: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-setu: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-revocation: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-revocation: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-seti: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-seti: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-dht: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-dht: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-nse: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libexec/gnunet-service-nse: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libgnunet_plugin_block_regex.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libgnunet_plugin_block_regex.so: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libgnunet_plugin_ats_proportional.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libgnunet_plugin_ats_proportional.so: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libgnunet_plugin_block_revocation.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libgnunet_plugin_block_revocation.so: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libgnunet_plugin_block_dht.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/gnunet/libgnunet_plugin_block_dht.so: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunethello.so.0.1.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunethello.so.0.1.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetcadet.so.7.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetcadet.so.7.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetdatacache.so.0.0.1: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetdatacache.so.0.0.1: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetstatistics.so.2.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetstatistics.so.2.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetseti.so.0.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetseti.so.0.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetrevocation.so.0.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetrevocation.so.0.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetidentity.so.1.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetidentity.so.1.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunettransport.so.2.2.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunettransport.so.2.2.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetregexblock.so.1.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetregexblock.so.1.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetnatauto.so.0.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetnatauto.so.0.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetnatnew.so.2.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetnatnew.so.2.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetblock.so.0.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetblock.so.0.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetfriends.so.0.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetfriends.so.0.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunettransportmonitor.so.0.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunettransportmonitor.so.0.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetdns.so.0.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetdns.so.0.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetsetu.so.0.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetsetu.so.0.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetnse.so.0.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetnse.so.0.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetutil.so.14.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetutil.so.14.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetpeerstore.so.0.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetpeerstore.so.0.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunettransportapplication.so.0.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunettransportapplication.so.0.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetnt.so.0.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetnt.so.0.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetpeerinfo.so.0.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet/usr/lib/libgnunetpeerinfo.so.0.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet into /openwrt/bin/packages/mips_24kc/packages/gnunet_0.14.1-1_mips_24kc.ipk
cp: cannot stat '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetdnsstub.so*': No such file or directory
cp: cannot stat '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunettun.so*': No such file or directory
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-vpn/usr/bin/gnunet-vpn: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-vpn/usr/bin/gnunet-vpn: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-vpn/usr/lib/gnunet/libexec/gnunet-helper-exit: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-vpn/usr/lib/gnunet/libexec/gnunet-daemon-exit: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-vpn/usr/lib/gnunet/libexec/gnunet-daemon-exit: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-vpn/usr/lib/gnunet/libexec/gnunet-helper-vpn: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-vpn/usr/lib/gnunet/libexec/gnunet-service-vpn: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-vpn/usr/lib/gnunet/libexec/gnunet-service-vpn: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-vpn/usr/lib/gnunet/libexec/gnunet-daemon-pt: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-vpn/usr/lib/gnunet/libexec/gnunet-daemon-pt: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-vpn/usr/lib/libgnunetvpn.so.0.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-vpn/usr/lib/libgnunetvpn.so.0.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-vpn into /openwrt/bin/packages/mips_24kc/packages/gnunet-vpn_0.14.1-1_mips_24kc.ipk
install: cannot stat '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-gns-import.sh': No such file or directory
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/bin/gnunet-namecache: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/bin/gnunet-namecache: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/bin/gnunet-gns: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/bin/gnunet-gns: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/bin/gnunet-resolver: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/bin/gnunet-resolver: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/bin/gnunet-zoneimport: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/bin/gnunet-zoneimport: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/bin/gnunet-namestore: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/bin/gnunet-namestore: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/libgnunetnamecache.so.0.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/libgnunetnamecache.so.0.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/libgnunetgnsrecord.so.0.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/libgnunetgnsrecord.so.0.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/gnunet/libgnunet_plugin_gnsrecord_dns.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/gnunet/libgnunet_plugin_gnsrecord_dns.so: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/gnunet/libgnunet_plugin_block_dns.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/gnunet/libgnunet_plugin_block_dns.so: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/gnunet/libexec/gnunet-service-resolver: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/gnunet/libexec/gnunet-service-resolver: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/gnunet/libexec/gnunet-dns2gns: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/gnunet/libexec/gnunet-dns2gns: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/gnunet/libexec/gnunet-service-gns: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/gnunet/libexec/gnunet-service-gns: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/gnunet/libexec/gnunet-service-dns: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/gnunet/libexec/gnunet-service-dns: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/gnunet/libexec/gnunet-service-namecache: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/gnunet/libexec/gnunet-service-namecache: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/gnunet/libexec/gnunet-service-zonemaster: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/gnunet/libexec/gnunet-service-zonemaster: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/gnunet/libexec/gnunet-service-namestore: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/gnunet/libexec/gnunet-service-namestore: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/gnunet/libexec/gnunet-helper-dns: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/gnunet/libgnunet_plugin_gnsrecord_gns.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/gnunet/libgnunet_plugin_gnsrecord_gns.so: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/gnunet/libgnunet_plugin_block_gns.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/gnunet/libgnunet_plugin_block_gns.so: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/gnunet/libgnunet_plugin_gnsrecord_conversation.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/gnunet/libgnunet_plugin_gnsrecord_conversation.so: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/libgnunetnamestore.so.0.0.1: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/libgnunetnamestore.so.0.0.1: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/libgnunetgns.so.0.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns/usr/lib/libgnunetgns.so.0.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-gns into /openwrt/bin/packages/mips_24kc/packages/gnunet-gns_0.14.1-1_mips_24kc.ipk
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-sqlite/usr/lib/libgnunetsq.so.0.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-sqlite/usr/lib/libgnunetsq.so.0.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-sqlite into /openwrt/bin/packages/mips_24kc/packages/gnunet-sqlite_0.14.1-1_mips_24kc.ipk
cp: cannot stat '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/libgnunetreclaimattribute.so*': No such file or directory
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-reclaim/usr/bin/gnunet-reclaim: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-reclaim/usr/bin/gnunet-reclaim: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-reclaim/usr/lib/libgnunetabe.so.1.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-reclaim/usr/lib/libgnunetabe.so.1.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-reclaim/usr/lib/gnunet/libgnunet_plugin_reclaim_credential_jwt.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-reclaim/usr/lib/gnunet/libgnunet_plugin_reclaim_credential_jwt.so: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-reclaim/usr/lib/gnunet/libgnunet_plugin_block_consensus.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-reclaim/usr/lib/gnunet/libgnunet_plugin_block_consensus.so: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-reclaim/usr/lib/gnunet/libgnunet_plugin_reclaim_attribute_basic.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-reclaim/usr/lib/gnunet/libgnunet_plugin_reclaim_attribute_basic.so: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-reclaim/usr/lib/gnunet/libexec/gnunet-service-secretsharing: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-reclaim/usr/lib/gnunet/libexec/gnunet-service-secretsharing: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-reclaim/usr/lib/gnunet/libexec/gnunet-service-consensus: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-reclaim/usr/lib/gnunet/libexec/gnunet-service-consensus: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-reclaim/usr/lib/gnunet/libexec/gnunet-service-reclaim: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-reclaim/usr/lib/gnunet/libexec/gnunet-service-reclaim: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-reclaim/usr/lib/gnunet/libgnunet_plugin_gnsrecord_reclaim.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-reclaim/usr/lib/gnunet/libgnunet_plugin_gnsrecord_reclaim.so: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-reclaim/usr/lib/libgnunetreclaim.so.0.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-reclaim/usr/lib/libgnunetreclaim.so.0.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-reclaim/usr/lib/libgnunetconsensus.so.0.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-reclaim/usr/lib/libgnunetconsensus.so.0.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-reclaim/usr/lib/libgnunetsecretsharing.so.0.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-reclaim/usr/lib/libgnunetsecretsharing.so.0.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-reclaim into /openwrt/bin/packages/mips_24kc/packages/gnunet-reclaim_0.14.1-1_mips_24kc.ipk
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-auction/usr/bin/gnunet-auction-join: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-auction/usr/bin/gnunet-auction-join: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-auction/usr/bin/gnunet-auction-info: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-auction/usr/bin/gnunet-auction-info: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-auction/usr/bin/gnunet-auction-create: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-auction/usr/bin/gnunet-auction-create: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-auction/usr/lib/gnunet/libexec/gnunet-service-auction: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-auction/usr/lib/gnunet/libexec/gnunet-service-auction: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-auction into /openwrt/bin/packages/mips_24kc/packages/gnunet-auction_0.14.1-1_mips_24kc.ipk
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-conversation/usr/bin/gnunet-conversation-test: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-conversation/usr/bin/gnunet-conversation-test: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-conversation/usr/bin/gnunet-conversation: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-conversation/usr/bin/gnunet-conversation: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-conversation/usr/lib/libgnunetconversation.so.0.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-conversation/usr/lib/libgnunetconversation.so.0.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-conversation/usr/lib/gnunet/libexec/gnunet-service-conversation: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-conversation/usr/lib/gnunet/libexec/gnunet-service-conversation: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-conversation/usr/lib/gnunet/libexec/gnunet-helper-audio-playback: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-conversation/usr/lib/gnunet/libexec/gnunet-helper-audio-playback: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-conversation/usr/lib/gnunet/libexec/gnunet-helper-audio-record: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-conversation/usr/lib/gnunet/libexec/gnunet-helper-audio-record: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-conversation/usr/lib/gnunet/libgnunet_plugin_gnsrecord_conversation.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-conversation/usr/lib/gnunet/libgnunet_plugin_gnsrecord_conversation.so: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-conversation/usr/lib/libgnunetmicrophone.so.0.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-conversation/usr/lib/libgnunetmicrophone.so.0.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-conversation/usr/lib/libgnunetspeaker.so.0.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-conversation/usr/lib/libgnunetspeaker.so.0.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-conversation into /openwrt/bin/packages/mips_24kc/packages/gnunet-conversation_0.14.1-1_mips_24kc.ipk
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-curl/usr/lib/libgnunetcurl.so.0.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-curl/usr/lib/libgnunetcurl.so.0.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-curl into /openwrt/bin/packages/mips_24kc/packages/gnunet-curl_0.14.1-1_mips_24kc.ipk
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-datastore/usr/bin/gnunet-datastore: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-datastore/usr/bin/gnunet-datastore: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-datastore/usr/lib/gnunet/libexec/gnunet-service-datastore: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-datastore/usr/lib/gnunet/libexec/gnunet-service-datastore: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-datastore/usr/lib/libgnunetdatastore.so.1.0.0: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-datastore/usr/lib/libgnunetdatastore.so.1.0.0: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-datastore into /openwrt/bin/packages/mips_24kc/packages/gnunet-datastore_0.14.1-1_mips_24kc.ipk
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-dht-cli/usr/bin/gnunet-dht-put: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-dht-cli/usr/bin/gnunet-dht-put: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-dht-cli/usr/bin/gnunet-dht-get: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-dht-cli/usr/bin/gnunet-dht-get: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-dht-cli/usr/bin/gnunet-dht-monitor: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-dht-cli/usr/bin/gnunet-dht-monitor: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-dht-cli/usr/lib/gnunet/libgnunet_plugin_block_test.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-dht-cli/usr/lib/gnunet/libgnunet_plugin_block_test.so: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-dht-cli into /openwrt/bin/packages/mips_24kc/packages/gnunet-dht-cli_0.14.1-1_mips_24kc.ipk
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-fs/usr/bin/gnunet-fs: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-fs/usr/bin/gnunet-fs: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-fs/usr/bin/gnunet-auto-share: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-fs/usr/bin/gnunet-auto-share: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-fs/usr/bin/gnunet-search: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-fs/usr/bin/gnunet-search: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-fs/usr/bin/gnunet-download: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-fs/usr/bin/gnunet-download: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-fs/usr/bin/gnunet-publish: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-fs/usr/bin/gnunet-publish: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-fs/usr/bin/gnunet-unindex: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-fs/usr/bin/gnunet-unindex: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-fs/usr/bin/gnunet-directory: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-fs/usr/bin/gnunet-directory: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-fs/usr/lib/libgnunetfs.so.2.1.1: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-fs/usr/lib/libgnunetfs.so.2.1.1: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-fs/usr/lib/gnunet/libexec/gnunet-helper-fs-publish: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-fs/usr/lib/gnunet/libexec/gnunet-helper-fs-publish: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-fs/usr/lib/gnunet/libexec/gnunet-service-fs: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-fs/usr/lib/gnunet/libexec/gnunet-service-fs: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-fs/usr/lib/gnunet/libgnunet_plugin_block_fs.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-fs/usr/lib/gnunet/libgnunet_plugin_block_fs.so: removing rpath /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-mips_24kc/gnunet-fs into /openwrt/bin/packages/mips_24kc/packages/gnunet-fs_0.14.1-1_mips_24kc.ipk
install: cannot stat '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/bin/gnunet-gns-import.sh': No such file or directory
install: cannot stat '/openwrt/build_dir/target-mips_24kc_musl/gnunet-0.14.1/ipkg-install/usr/lib/gnunet/libexec/gnunet-gns-proxy': No such file or directory
make[3]: *** [Makefile:419: /openwrt/bin/packages/mips_24kc/packages/gnunet-gns-proxy_0.14.1-1_mips_24kc.ipk] Error 1
```
