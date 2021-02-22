---
title: "compile.48"
date: 2021-02-22 14:41:05.900659
hidden: false
draft: false
weight: -48
---

build number: `48`

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
autopoint: *** Missing version: please specify in configure.ac through a line 'AM_GNU_GETTEXT_VERSION(x.yy.zz)' the gettext version the package is using
autopoint: *** Stop.
autoreconf: Entering directory `.'
autoreconf: running: true --force
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
/openwrt/staging_dir/target-x86_64_musl/../host/share/automake-1.15/am/texinfos.am: warning: AM_MAKEINFOHTMLFLAGS was already defined in condition !ACTIVATE_TEXINFO4, which is included in condition TRUE ...
doc/handbook/Makefile.am:23: ... 'AM_MAKEINFOHTMLFLAGS' previously defined here
/openwrt/staging_dir/target-x86_64_musl/../host/share/automake-1.15/am/texinfos.am: warning: AM_MAKEINFOHTMLFLAGS was already defined in condition !ACTIVATE_TEXINFO4, which is included in condition TRUE ...
doc/tutorial/Makefile.am:21: ... 'AM_MAKEINFOHTMLFLAGS' previously defined here
autoreconf: Leaving directory `.'
configure: loading site script /openwrt/include/site/x86_64
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-openwrt-linux-gnu
checking target system type... x86_64-openwrt-linux-gnu
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for x86_64-openwrt-linux-strip... x86_64-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether make supports nested variables... (cached) yes
checking for gawk... (cached) gawk
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
checking for ccache_cc option to accept ISO C99... none needed
checking for x86_64-openwrt-linux-gcc... x86_64-openwrt-linux-gcc
checking whether we are using the GNU Objective C compiler... no
checking whether x86_64-openwrt-linux-gcc accepts -g... no
checking dependency style of x86_64-openwrt-linux-gcc... gcc3
checking whether ln -s works... yes
checking whether make sets $(MAKE)... (cached) yes
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache_cc... x86_64-openwrt-linux-musl-ld
checking if the linker (x86_64-openwrt-linux-musl-ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... x86_64-openwrt-linux-musl-gcc-nm
checking the name lister (x86_64-openwrt-linux-musl-gcc-nm) interface... BSD nm
checking the maximum length of command line arguments... 1572864
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
checking for x86_64-openwrt-linux-ar... x86_64-openwrt-linux-musl-gcc-ar
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
checking for SSH key... ./configure: line 11917: ssh: command not found
checking for a Python interpreter with version >= 3.4... python3
checking for python3... /openwrt/staging_dir/hostpkg/bin/python3
checking for python3 version... 3.9
checking for python3 platform... linux
checking for python3 script directory... ${prefix}/lib/python3.9/site-packages
checking for python3 extension module directory... ${exec_prefix}/lib/python3.9/site-packages
checking for perl... /openwrt/staging_dir/host/bin/perl
checking for awk... /openwrt/staging_dir/host/bin/awk
checking whether to install gnunet-logread... no
checking for x86_64-openwrt-linux-iptables... no
configure: WARNING: warning: 'iptables' not found.
checking for x86_64-openwrt-linux-ip6tables... no
configure: WARNING: warning: 'ip6tables' not found.
checking for x86_64-openwrt-linux-ip... no
configure: WARNING: warning: 'ip' not found.
checking for x86_64-openwrt-linux-ifconfig... no
checking for ifconfig... false
configure: WARNING: 'ifconfig' not found.
checking for adduser... /usr/sbin/adduser
checking for x86_64-openwrt-linux-sysctl... no
checking for sysctl... false
checking for x86_64-openwrt-linux-upnpc... no
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
checking for libgcrypt-config... /openwrt/staging_dir/target-x86_64_musl/host/bin/libgcrypt-config
checking for LIBGCRYPT - version >= 1.6.0... yes (1.8.7)
checking LIBGCRYPT API version... okay
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
checking for libbluetooth... /openwrt/staging_dir/target-x86_64_musl/usr
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
checking for libpulse... /openwrt/staging_dir/target-x86_64_musl/usr
checking pulse/simple.h usability... yes
checking pulse/simple.h presence... yes
checking for pulse/simple.h... yes
checking whether pa_stream_peek is declared... yes
checking for libopus... /openwrt/staging_dir/target-x86_64_musl/usr
checking opus/opus.h usability... yes
checking opus/opus.h presence... yes
checking for opus/opus.h... yes
checking whether OPUS_SET_GAIN is declared... yes
checking for libogg... /openwrt/staging_dir/target-x86_64_musl/usr
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
checking for gnurl-config... /openwrt/staging_dir/target-x86_64_musl/usr/bin/gnurl-config
checking for the version of libgnurl... 7.72.0
checking for libgnurl >= version 7.34.0... yes
checking whether libgnurl is usable... yes
checking for curl_free... yes
checking for gawk... (cached) gawk
checking for curl-config... /openwrt/staging_dir/target-x86_64_musl/host/bin/curl-config
checking for the version of libcurl... 7.74.0
checking for libcurl >= version 7.34.0... yes
checking whether libcurl is usable... yes
checking for curl_free... (cached) yes
checking curl/curl.h usability... yes
checking curl/curl.h presence... yes
checking for curl/curl.h... yes
checking whether CURLINFO_TLS_SESSION is declared... yes
checking for curl_easy_getinfo in -lcurl-gnutls... no
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
checking for libextractor... /openwrt/staging_dir/target-x86_64_musl/usr
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
checking for ld... x86_64-openwrt-linux-musl-ld -m elf_x86_64
checking if the linker (x86_64-openwrt-linux-musl-ld -m elf_x86_64) is GNU ld... yes
checking for shared library run path origin... done
checking 32-bit host C ABI... no
checking for ELF binary format... yes
checking for the common suffixes of directories in the library search path... lib,lib,lib64
checking for iconv... yes
checking for working iconv... guessing yes
checking how to link with libiconv... /openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib/libiconv.a
checking for iconv declaration... 
         extern size_t iconv (iconv_t cd, char * *inbuf, size_t *inbytesleft, char * *outbuf, size_t *outbytesleft);
checking for libunistring... yes
checking how to link with libunistring... /openwrt/staging_dir/target-x86_64_musl/usr/lib/libunistring.so -Wl,-rpath -Wl,/openwrt/staging_dir/target-x86_64_musl/usr/lib
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
checking for SQLite... "/openwrt/staging_dir/target-x86_64_musl/usr"
checking sqlite3.h usability... yes
checking sqlite3.h presence... yes
checking for sqlite3.h... yes
checking pkg-config is at least version 0.9.0... yes
checking for the PostgreSQL libraries CPPFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include 
checking for the PostgreSQL libraries LDFLAGS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib 
checking for the PostgreSQL libraries LIBS... -lpq 
checking for the PostgreSQL version... 13.1
checking libpq-fe.h usability... yes
checking libpq-fe.h presence... yes
checking for libpq-fe.h... yes
checking for the PostgreSQL library linking is working... yes
checking for libpq-fe.h... (cached) yes
checking for sigset_t... yes
checking for off_t... yes
checking for size_t... yes
checking for mysql... /openwrt/staging_dir/target-x86_64_musl/usr
checking mysql/mysql.h usability... yes
checking mysql/mysql.h presence... yes
checking for mysql/mysql.h... yes
checking for mysql_init in -lmysqlclient... yes
checking mysql version... configure: success, will keep false
ok
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
checking for sudo... no
checking for doas... checking for doas... no
checking for gnunetdns group name... gnunetdns
checking for gnutls... /openwrt/staging_dir/target-x86_64_musl/usr
checking gnutls/abstract.h usability... yes
checking gnutls/abstract.h presence... yes
checking for gnutls/abstract.h... yes
checking for gnutls_priority_set in -lgnutls... yes
checking gnutls/dane.h usability... yes
checking gnutls/dane.h presence... yes
checking for gnutls/dane.h... yes
checking for dane_verify_crt_raw in -lgnutls-dane... yes
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
config.status: creating src/abd/Makefile
config.status: creating src/abd/abd.conf
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
configure: WARNING: libcurl TLS backend is not gnutls. The GNS Proxy will likely not function properly.
configure:
Detected system
===============

GNUnet version:                 0.13.3

Host setup:                     x86_64-openwrt-linux-gnu
Install prefix:                 /usr
Compiler:                       ccache_cc
CFLAGS:                         -fno-strict-aliasing -Wall -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3=gnunet-0.13.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include 
CPPFLAGS:                       -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include 
LDFLAGS:                        -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/pulseaudio  -Wl,--unresolved-symbols=report-all
LIBS:                           -lm 
Build Target:                   linux

Default Interface:              eth0

MySQL:                          yes
PostgreSQL:                     yes
sqlite3:                        yes
http client:                    curl-openssl
bluetooth:                      yes
iptables:                       no (optional, DNS query interception will not work)
ifconfig:                       no (optional, some features will not work)
upnpc:                          no (optional, NAT traversal using UPnPc will not work)
gnutls:                         yes (with DANE support)
libzbar:                        no (gnunet-qr will not be built)
java:                           
libidn:                         libidn2
libopus:                        yes
gstreamer:                      yes
libpulse:                       yes
libextractor:                   yes
texi2mdoc:                      yes
mandoc:                         yes

GNUnet configuration:
=====================
transports:                     tcp udp unix http wlan bluetooth
conversation:                   yes (xpulse)
database backends:              mysql postgres sqlite 
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
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3'
make  all-recursive
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3'
Making all in m4
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/m4'
make[6]: Nothing to be done for 'all'.
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/m4'
Making all in bin
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/bin'
make[6]: Nothing to be done for 'all'.
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/bin'
Making all in src
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src'
Making all in include
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/include'
Making all in .
make[8]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/include'
make[8]: Nothing to be done for 'all-am'.
make[8]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/include'
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/include'
Making all in util
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/util'
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
  CC       crypto_ecc_dlog.lo
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
  CC       gnunet-resolver.o
  CC       gnunet-config.o
  CC       gnunet-crypto-tvg.o
  CC       gnunet-ecc.o
  CC       gnunet-scrypt.o
  CC       gnunet-uri.o
  CC       gnunet-service-resolver.o
  CC       gnunet-timeout.o
  CC       gnunet-config-diff.o
  CC       test_common_logging_dummy.o
  CCLD     libgnunetutil.la
  CCLD     libgnunet_plugin_test.la
  CCLD     gnunet-resolver
  CCLD     gnunet-config
  CCLD     gnunet-crypto-tvg
  CCLD     gnunet-ecc
  CCLD     gnunet-scrypt
  CCLD     gnunet-uri
  CCLD     gnunet-service-resolver
  CCLD     gnunet-timeout
  CCLD     gnunet-config-diff
  CCLD     test_common_logging_dummy
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/util'
Making all in nt
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/nt'
  CC       nt.lo
  CCLD     libgnunetnt.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/nt'
Making all in gnsrecord
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/gnsrecord'
  CC       gnsrecord.lo
  CC       gnsrecord_serialization.lo
  CC       gnsrecord_crypto.lo
  CC       gnsrecord_misc.lo
  CC       plugin_gnsrecord_dns.lo
  CC       gnunet-gnsrecord-tvg.o
  CCLD     libgnunetgnsrecord.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_gnsrecord_dns.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-gnsrecord-tvg
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/gnsrecord'
Making all in hello
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/hello'
  CC       hello.lo
  CC       address.lo
  CC       hello-ng.lo
  CC       gnunet-hello.o
  CCLD     libgnunethello.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-hello
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/hello'
Making all in block
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/block'
  CC       block.lo
  CC       bg_bf.lo
  CC       plugin_block_template.lo
  CC       plugin_block_test.lo
  CCLD     libgnunetblock.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunetblockgroup.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_block_template.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CCLD     libgnunet_plugin_block_test.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/block'
Making all in statistics
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/statistics'
  CC       statistics_api.lo
  CC       gnunet-statistics.o
  CC       gnunet-service-statistics.o
  CCLD     libgnunetstatistics.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-statistics
  CCLD     gnunet-service-statistics
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/statistics'
Making all in arm
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/arm'
  CC       arm_api.lo
  CC       arm_monitor_api.lo
  CC       gnunet-arm.o
  CC       gnunet-service-arm.o
  CC       mockup-service.o
  CCLD     libgnunetarm.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-service-arm
  CCLD     mockup-service
  CCLD     gnunet-arm
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/arm'
Making all in testing
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/testing'
  CC       testing.lo
  CC       gnunet-testing.o
  CC       list-keys.o
  CCLD     libgnunettesting.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     list-keys
  CCLD     gnunet-testing
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/testing'
Making all in json
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/json'
  CC       libgnunetjson_la-json.lo
  CC       libgnunetjson_la-json_mhd.lo
  CC       libgnunetjson_la-json_generator.lo
  CC       libgnunetjson_la-json_helper.lo
  CC       libgnunetjson_la-json_gnsrecord.lo
  CCLD     libgnunetjson.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/json'
Making all in curl
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/curl'
  CC       libgnunetcurl_la-curl.lo
  CC       libgnunetcurl_la-curl_reschedule.lo
  CCLD     libgnunetcurl.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/curl'
Making all in rest
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/rest'
  CC       libgnunetrest_la-rest.lo
  CC       libgnunet_plugin_rest_copying_la-plugin_rest_copying.lo
  CC       libgnunet_plugin_rest_config_la-plugin_rest_config.lo
  CC       gnunet_rest_server-gnunet-rest-server.o
  CCLD     libgnunetrest.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-rest-server
  CCLD     libgnunet_plugin_rest_copying.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_rest_config.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/rest'
Making all in peerinfo
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/peerinfo'
  CC       peerinfo_api.lo
  CC       peerinfo_api_notify.lo
  CC       gnunet-service-peerinfo.o
  CCLD     libgnunetpeerinfo.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-service-peerinfo
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/peerinfo'
Making all in sq
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/sq'
  CC       sq.lo
  CC       sq_exec.lo
  CC       sq_prepare.lo
  CC       sq_query_helper.lo
  CC       sq_result_helper.lo
  CCLD     libgnunetsq.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/sq'
Making all in mysql
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/mysql'
  CC       mysql.lo
  CCLD     libgnunetmysql.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/mysql'
Making all in my
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/my'
  CC       my.lo
  CC       my_query_helper.lo
my_query_helper.c: In function 'my_conv_rsa_public_key':
my_query_helper.c:289:51: warning: passing argument 2 of 'GNUNET_CRYPTO_rsa_public_key_encode' from incompatible pointer type [-Wincompatible-pointer-types]
                                                   &buf);
                                                   ^~~~
In file included from ../../src/include/gnunet_util_lib.h:64,
                 from ../../src/include/gnunet_my_lib.h:34,
                 from my_query_helper.c:28:
../../src/include/gnunet_crypto_lib.h:2151:10: note: expected 'void **' but argument is of type 'char **'
   void **buffer);
   ~~~~~~~^~~~~~
my_query_helper.c: In function 'my_conv_rsa_signature':
my_query_helper.c:341:50: warning: passing argument 2 of 'GNUNET_CRYPTO_rsa_signature_encode' from incompatible pointer type [-Wincompatible-pointer-types]
                                                  &buf);
                                                  ^~~~
In file included from ../../src/include/gnunet_util_lib.h:64,
                 from ../../src/include/gnunet_my_lib.h:34,
                 from my_query_helper.c:28:
../../src/include/gnunet_crypto_lib.h:2275:10: note: expected 'void **' but argument is of type 'char **'
   void **buffer);
   ~~~~~~~^~~~~~
  CC       my_result_helper.lo
my_result_helper.c: In function 'pre_extract_varsize_blob':
my_result_helper.c:53:22: warning: assignment to 'my_bool *' {aka 'char *'} from incompatible pointer type 'MYSQL_BOOL *' {aka '_Bool *'} [-Wincompatible-pointer-types]
   results[0].is_null = &rs->is_null;
                      ^
my_result_helper.c: In function 'pre_extract_fixed_blob':
my_result_helper.c:179:22: warning: assignment to 'my_bool *' {aka 'char *'} from incompatible pointer type 'MYSQL_BOOL *' {aka '_Bool *'} [-Wincompatible-pointer-types]
   results[0].is_null = &rs->is_null;
                      ^
my_result_helper.c: In function 'pre_extract_rsa_public_key':
my_result_helper.c:262:22: warning: assignment to 'my_bool *' {aka 'char *'} from incompatible pointer type 'MYSQL_BOOL *' {aka '_Bool *'} [-Wincompatible-pointer-types]
   results[0].is_null = &rs->is_null;
                      ^
my_result_helper.c: In function 'pre_extract_rsa_signature':
my_result_helper.c:396:22: warning: assignment to 'my_bool *' {aka 'char *'} from incompatible pointer type 'MYSQL_BOOL *' {aka '_Bool *'} [-Wincompatible-pointer-types]
   results[0].is_null = &rs->is_null;
                      ^
my_result_helper.c: In function 'pre_extract_string':
my_result_helper.c:526:22: warning: assignment to 'my_bool *' {aka 'char *'} from incompatible pointer type 'MYSQL_BOOL *' {aka '_Bool *'} [-Wincompatible-pointer-types]
   results[0].is_null = &rs->is_null;
                      ^
my_result_helper.c: In function 'pre_extract_uint16':
my_result_helper.c:658:22: warning: assignment to 'my_bool *' {aka 'char *'} from incompatible pointer type 'MYSQL_BOOL *' {aka '_Bool *'} [-Wincompatible-pointer-types]
   results[0].is_null = &rs->is_null;
                      ^
my_result_helper.c: In function 'pre_extract_uint32':
my_result_helper.c:738:22: warning: assignment to 'my_bool *' {aka 'char *'} from incompatible pointer type 'MYSQL_BOOL *' {aka '_Bool *'} [-Wincompatible-pointer-types]
   results[0].is_null = &rs->is_null;
                      ^
my_result_helper.c: In function 'pre_extract_uint64':
my_result_helper.c:820:22: warning: assignment to 'my_bool *' {aka 'char *'} from incompatible pointer type 'MYSQL_BOOL *' {aka '_Bool *'} [-Wincompatible-pointer-types]
   results[0].is_null = &rs->is_null;
                      ^
  CCLD     libgnunetmy.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/my'
Making all in pq
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/pq'
  CC       pq.lo
  CC       pq_connect.lo
  CC       pq_eval.lo
  CC       pq_exec.lo
  CC       pq_prepare.lo
  CC       pq_query_helper.lo
  CC       pq_result_helper.lo
  CCLD     libgnunetpq.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/pq'
Making all in datacache
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/datacache'
  CC       datacache.lo
  CC       plugin_datacache_template.lo
  CC       plugin_datacache_sqlite.lo
  CC       libgnunet_plugin_datacache_postgres_la-plugin_datacache_postgres.lo
  CC       plugin_datacache_heap.lo
  CCLD     libgnunetdatacache.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_datacache_template.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CCLD     libgnunet_plugin_datacache_sqlite.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_datacache_postgres.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_datacache_heap.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/datacache'
Making all in datastore
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/datastore'
  CC       datastore_api.lo
  CC       plugin_datastore_template.lo
  CC       plugin_datastore_sqlite.lo
  CC       libgnunet_plugin_datastore_mysql_la-plugin_datastore_mysql.lo
  CC       libgnunet_plugin_datastore_postgres_la-plugin_datastore_postgres.lo
  CC       plugin_datastore_heap.lo
  CC       gnunet-datastore.o
  CC       gnunet-service-datastore.o
  CCLD     libgnunetdatastore.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_datastore_template.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CCLD     libgnunet_plugin_datastore_sqlite.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_datastore_mysql.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_datastore_postgres.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_datastore_heap.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-datastore
  CCLD     gnunet-service-datastore
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/datastore'
Making all in template
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/template'
  CC       gnunet-template.o
  CC       gnunet-service-template.o
  CCLD     gnunet-template
  CCLD     gnunet-service-template
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/template'
Making all in peerstore
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/peerstore'
  CC       peerstore_api.lo
  CC       peerstore_common.lo
  CC       plugin_peerstore_sqlite.lo
  CC       plugin_peerstore_flat.lo
  CC       gnunet-peerstore.o
  CC       gnunet_service_peerstore-gnunet-service-peerstore.o
  CC       gnunet_service_peerstore-peerstore_common.o
  CCLD     libgnunetpeerstore.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-service-peerstore
  CCLD     libgnunet_plugin_peerstore_sqlite.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_peerstore_flat.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-peerstore
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/peerstore'
Making all in ats
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/ats'
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
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_ats_proportional.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-service-ats
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/ats'
Making all in nat
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/nat'
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
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-helper-nat-server
  CCLD     gnunet-helper-nat-client
  CCLD     gnunet-service-nat
  CCLD     gnunet-nat
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/nat'
Making all in nat-auto
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/nat-auto'
  CC       nat_auto_api.lo
  CC       nat_auto_api_test.lo
  CC       gnunet-nat-auto.o
  CC       gnunet-nat-server.o
  CC       gnunet-service-nat-auto.o
  CCLD     libgnunetnatauto.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-nat-server
  CCLD     gnunet-service-nat-auto
  CCLD     gnunet-nat-auto
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/nat-auto'
Making all in fragmentation
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/fragmentation'
  CC       fragmentation.lo
  CC       defragmentation.lo
  CCLD     libgnunetfragmentation.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/fragmentation'
Making all in transport
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/transport'
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
plugin_transport_udp.c: In function 'udp_select_send':
plugin_transport_udp.c:3134:5: warning: 'session' may be used uninitialized in this function [-Wmaybe-uninitialized]
     notify_session_monitor (session->plugin,
     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                             session,
                             ~~~~~~~~
                             GNUNET_TRANSPORT_SS_UPDATE);
                             ~~~~~~~~~~~~~~~~~~~~~~~~~~~
plugin_transport_udp.c:3071:30: note: 'session' was declared here
   struct GNUNET_ATS_Session *session;
                              ^~~~~~~
  CC       plugin_transport_udp_broadcasting.lo
  CC       gnunet-transport.o
  CC       gnunet-helper-transport-wlan.o
  CC       gnunet-helper-transport-wlan-dummy.o
  CC       gnunet-helper-transport-bluetooth.o
  CC       gnunet_service_transport-gnunet-service-transport.o
  CC       gnunet_service_transport-gnunet-service-transport_ats.o
  CC       gnunet_service_transport-gnunet-service-transport_hello.o
  CC       gnunet_service_transport-gnunet-service-transport_neighbours.o
  CC       gnunet_service_transport-gnunet-service-transport_plugins.o
  CC       gnunet_service_transport-gnunet-service-transport_validation.o
  CC       gnunet_service_transport-gnunet-service-transport_manipulation.o
  CC       gnunet-communicator-unix.o
  CC       gnunet-communicator-udp.o
  CC       gnunet-communicator-tcp.o
  CC       gnunet-transport-profiler.o
  CC       gnunet-service-tng.o
  CC       gnunet-transport-wlan-sender.o
  CC       gnunet-transport-wlan-receiver.o
sed -e 's,[@]pkgdatadir[@],/usr/share/gnunet,g' < ./gnunet-transport-certificate-creation.in > gnunet-transport-certificate-creation
chmod +x gnunet-transport-certificate-creation
  CCLD     libgnunettransport.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunettransportapplication.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunettransportcore.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunettransportcommunicator.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunettransportmonitor.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunettransporttesting.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunettransporttesting2.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_transport_template.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CCLD     libgnunet_plugin_transport_tcp.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_transport_unix.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_transport_http_client.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_transport_https_client.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_transport_http_server.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_transport_https_server.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_transport_wlan.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_transport_bluetooth.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_transport_udp.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-transport
  CCLD     gnunet-helper-transport-wlan
  CCLD     gnunet-helper-transport-wlan-dummy
  CCLD     gnunet-helper-transport-bluetooth
  CCLD     gnunet-service-transport
  CCLD     gnunet-communicator-unix
  CCLD     gnunet-communicator-udp
  CCLD     gnunet-communicator-tcp
  CCLD     gnunet-transport-profiler
  CCLD     gnunet-service-tng
  CCLD     gnunet-transport-wlan-sender
  CCLD     gnunet-transport-wlan-receiver
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/transport'
Making all in ats-tool
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/ats-tool'
  CC       gnunet-ats.o
  CCLD     gnunet-ats
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/ats-tool'
Making all in peerinfo-tool
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/peerinfo-tool'
  CC       libgnunet_plugin_rest_peerinfo_la-plugin_rest_peerinfo.lo
  CC       gnunet-peerinfo.o
  CC       gnunet-peerinfo_plugins.o
  CCLD     libgnunet_plugin_rest_peerinfo.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-peerinfo
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/peerinfo-tool'
Making all in core
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/core'
  CC       core_api.lo
  CC       core_api_monitor_peers.lo
  CC       gnunet-core.o
  CC       gnunet-service-core.o
  CC       gnunet-service-core_kx.o
  CC       gnunet-service-core_sessions.o
  CC       gnunet-service-core_typemap.o
  CCLD     libgnunetcore.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-service-core
  CCLD     gnunet-core
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/core'
Making all in testbed-logger
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/testbed-logger'
  CC       testbed_logger_api.lo
  CC       gnunet-service-testbed-logger.o
  CCLD     libgnunettestbedlogger.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-service-testbed-logger
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/testbed-logger'
Making all in testbed
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/testbed'
  CC       testbed_api.lo
  CC       testbed_api_hosts.lo
  CC       testbed_api_operations.lo
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
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-daemon-testbed-blacklist
  CCLD     gnunet-daemon-testbed-underlay
  CCLD     gnunet-daemon-latency-logger
  CCLD     generate-underlay-topology
  CCLD     gnunet-testbed-profiler
  CCLD     gnunet-service-testbed
  CCLD     gnunet-helper-testbed
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/testbed'
Making all in ats-tests
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/ats-tests'
  CC       ats-testing.lo
  CC       ats-testing-log.lo
  CC       ats-testing-traffic.lo
  CC       ats-testing-experiment.lo
  CC       ats-testing-preferences.lo
  CC       gnunet-ats-sim.o
  CC       gnunet-solver-eval.o
  CCLD     libgnunetatstesting.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-solver-eval
  CCLD     gnunet-ats-sim
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/ats-tests'
Making all in nse
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/nse'
  CC       nse_api.lo
  CC       gnunet-nse.o
  CC       gnunet-service-nse.o
  CC       gnunet-nse-profiler.o
  CCLD     libgnunetnse.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-nse
  CCLD     gnunet-service-nse
  CCLD     gnunet-nse-profiler
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/nse'
Making all in dht
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/dht'
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
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_block_dht.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-dht-monitor
  CCLD     gnunet-dht-get
  CCLD     gnunet-dht-put
  CCLD     gnunet-service-dht
  CCLD     gnunet-dht-profiler
  AR       libgnunetdhttest.a
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/dht'
Making all in hostlist
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/hostlist'
  CC       gnunet_daemon_hostlist-gnunet-daemon-hostlist.o
  CC       gnunet_daemon_hostlist-gnunet-daemon-hostlist_client.o
  CC       gnunet_daemon_hostlist-gnunet-daemon-hostlist_server.o
  CCLD     gnunet-daemon-hostlist
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/hostlist'
Making all in topology
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/topology'
  CC       friends.lo
  CC       gnunet-daemon-topology.o
  CCLD     libgnunetfriends.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-daemon-topology
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/topology'
Making all in regex
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/regex'
  CC       regex_internal.o
  CC       regex_internal_dht.o
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
  CC       gnunet-regex-simulation-profiler.o
  CC       perf-regex.o
  CC       gnunet-regex-profiler.o
  CCLD     libgnunetregexblock.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunetregex.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_block_regex.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  AR       libgnunetregex_internal.a
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  AR       libgnunetregextest.a
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CCLD     gnunet-service-regex
  CCLD     gnunet-daemon-regexprofiler
  CCLD     gnunet-regex-simulation-profiler
  CCLD     perf-regex
  CCLD     gnunet-regex-profiler
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/regex'
Making all in dns
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/dns'
  CC       dns_api.lo
  CC       plugin_block_dns.lo
  CC       gnunet-service-dns.o
  CC       gnunet-helper-dns.o
  CC       gnunet-dns-monitor.o
  CC       gnunet-dns-redirector.o
  CC       gnunet-zonewalk.o
  CCLD     libgnunetdns.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_block_dns.la
  CCLD     gnunet-service-dns
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-helper-dns
  CCLD     gnunet-dns-monitor
  CCLD     gnunet-dns-redirector
  CCLD     gnunet-zonewalk
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/dns'
Making all in identity
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/identity'
  CC       identity_api.lo
  CC       identity_api_lookup.lo
  CC       identity_api_suffix_lookup.lo
  CC       libgnunet_plugin_rest_identity_la-plugin_rest_identity.lo
  CC       gnunet-identity.o
  CC       gnunet-service-identity.o
  CCLD     libgnunetidentity.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_rest_identity.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-identity
  CCLD     gnunet-service-identity
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/identity'
Making all in namecache
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/namecache'
  CC       namecache_api.lo
  CC       plugin_namecache_sqlite.lo
  CC       plugin_namecache_flat.lo
  CC       plugin_namecache_postgres.lo
  CC       gnunet-namecache.o
  CC       gnunet-service-namecache.o
  CCLD     libgnunetnamecache.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_namecache_sqlite.la
  CCLD     libgnunet_plugin_namecache_flat.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_namecache_postgres.la
  CCLD     gnunet-namecache
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-service-namecache
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/namecache'
Making all in namestore
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/namestore'
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
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_namestore_postgres.la
  CCLD     libgnunet_plugin_namestore_flat.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_rest_namestore.la
  CCLD     gnunet-namestore
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-zoneimport
  CCLD     gnunet-service-namestore
  CCLD     gnunet-namestore-fcfsd
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/namestore'
Making all in cadet
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/cadet'
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
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunetcadettest.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CCLD     gnunet-cadet
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/cadet'
Making all in set
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/set'
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
  CCLD     libgnunet_plugin_block_set_test.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-set-ibf-profiler
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-set-profiler
  CCLD     gnunet-service-set
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/set'
Making all in seti
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/seti'
  CC       seti_api.lo
  CC       plugin_block_seti_test.lo
  CC       gnunet-seti-profiler.o
  CC       gnunet-service-seti.o
  CCLD     libgnunetseti.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_block_seti_test.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-seti-profiler
  CCLD     gnunet-service-seti
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/seti'
Making all in setu
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/setu'
  CC       setu_api.lo
  CC       plugin_block_setu_test.lo
  CC       gnunet-setu-profiler.o
  CC       gnunet-service-setu.o
  CC       ibf.o
  CC       gnunet-service-setu_strata_estimator.o
  CC       gnunet-setu-ibf-profiler.o
  CCLD     libgnunetsetu.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_block_setu_test.la
  CCLD     gnunet-setu-profiler
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-service-setu
  CCLD     gnunet-setu-ibf-profiler
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/setu'
Making all in consensus
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/consensus'
  CC       consensus_api.lo
  CC       plugin_block_consensus.lo
  CC       gnunet-consensus-profiler.o
  CC       gnunet-service-consensus.o
  CC       gnunet_service_evil_consensus-gnunet-service-consensus.o
gawk -v bdir="/usr/bin" -v py="/openwrt/staging_dir/hostpkg/bin/python3" -v awkay="/openwrt/staging_dir/host/bin/awk" -v pfx="/usr" -v prl="/openwrt/staging_dir/host/bin/perl" -v sysconfdirectory="/etc" -v pkgdatadirectory="/usr/share/gnunet" -f ../../bin/dosubst.awk < consensus-simulation.py.in > consensus-simulation.py
chmod +x consensus-simulation.py
  CCLD     libgnunetconsensus.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_block_consensus.la
  CCLD     gnunet-consensus-profiler
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-service-consensus
  CCLD     gnunet-service-evil-consensus
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/consensus'
Making all in scalarproduct
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/scalarproduct'
  CC       scalarproduct_api.lo
  CC       gnunet-scalarproduct.o
  CC       gnunet-service-scalarproduct_alice.o
  CC       gnunet-service-scalarproduct_bob.o
  CC       gnunet-service-scalarproduct-ecc_alice.o
  CC       gnunet-service-scalarproduct-ecc_bob.o
  CCLD     libgnunetscalarproduct.la
  CCLD     gnunet-service-scalarproduct-alice
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-service-scalarproduct-bob
  CCLD     gnunet-service-scalarproduct-ecc-alice
  CCLD     gnunet-service-scalarproduct-ecc-bob
  CCLD     gnunet-scalarproduct
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/scalarproduct'
Making all in revocation
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/revocation'
  CC       revocation_api.lo
  CC       plugin_block_revocation.lo
  CC       gnunet-revocation.o
  CC       gnunet-revocation-tvg.o
  CC       gnunet-service-revocation.o
  CCLD     libgnunetrevocation.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_block_revocation.la
  CCLD     gnunet-revocation
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-revocation-tvg
  CCLD     gnunet-service-revocation
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/revocation'
Making all in vpn
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/vpn'
  CC       vpn_api.lo
  CC       gnunet-vpn.o
  CC       gnunet-helper-vpn.o
  CC       gnunet_service_vpn-gnunet-service-vpn.o
  CCLD     libgnunetvpn.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-helper-vpn
  CCLD     gnunet-vpn
cc1: note: someone does not honour COPTS correctly, passed 2 times
  CCLD     gnunet-service-vpn
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/vpn'
Making all in gns
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/gns'
Making all in .
make[8]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/gns'
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
  CC       gnunet_gns_proxy-gnunet-gns-proxy.o
  CC       gnunet-gns-benchmark.o
gawk -v bdir="/usr/bin" -v py="/openwrt/staging_dir/hostpkg/bin/python3" -v awkay="/openwrt/staging_dir/host/bin/awk" -v pfx="/usr" -v prl="/openwrt/staging_dir/host/bin/perl" -v sysconfdirectory="/etc" -v pkgdatadirectory="/usr/share/gnunet" -f ../../bin/dosubst.awk < ./gnunet-gns-proxy-setup-ca.in > gnunet-gns-proxy-setup-ca
  CCLD     libgnunetgns.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_block_gns.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_gnsrecord_gns.la
  CCLD     libgnunet_plugin_rest_gns.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-gns
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-bcd
  CCLD     gnunet-service-gns
  CCLD     gnunet-dns2gns
  CCLD     gnunet-gns-proxy
  CCLD     gnunet-gns-benchmark
make[8]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/gns'
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/gns'
Making all in zonemaster
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/zonemaster'
  CC       gnunet-service-zonemaster.o
  CC       gnunet-service-zonemaster-monitor.o
  CCLD     gnunet-service-zonemaster-monitor
  CCLD     gnunet-service-zonemaster
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/zonemaster'
Making all in conversation
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/conversation'
Making all in .
make[8]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/conversation'
  CC       microphone.lo
  CC       speaker.lo
  CC       conversation_api.lo
  CC       conversation_api_call.lo
  CC       plugin_gnsrecord_conversation.lo
  CC       gnunet-conversation-test.o
  CC       gnunet-conversation.o
  CC       gnunet-service-conversation.o
  CC       gnunet_helper_audio_record-gnunet-helper-audio-record.o
  CC       gnunet_helper_audio_playback-gnunet-helper-audio-playback.o
  CCLD     libgnunetmicrophone.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunetspeaker.la
  CCLD     libgnunetconversation.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_gnsrecord_conversation.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-conversation-test
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-helper-audio-record
  CCLD     gnunet-helper-audio-playback
  CCLD     gnunet-conversation
  CCLD     gnunet-service-conversation
make[8]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/conversation'
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/conversation'
Making all in fs
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/fs'
  CC       fs_test_lib.o
  CC       fs_api.lo
  CC       fs_directory.lo
  CC       fs_dirmetascan.lo
  CC       fs_download.lo
  CC       fs_file_information.lo
  CC       fs_getopt.lo
  CC       fs_list_indexed.lo
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
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CCLD     libgnunetfs.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-auto-share
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-helper-fs-publish
  CCLD     gnunet-service-fs
  CCLD     gnunet-fs-profiler
  CCLD     gnunet-daemon-fsprofiler
  CCLD     libgnunet_plugin_block_fs.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-directory
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-download
  CCLD     gnunet-publish
  CCLD     gnunet-search
  CCLD     gnunet-fs
  CCLD     gnunet-unindex
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/fs'
Making all in exit
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/exit'
  CC       gnunet-daemon-exit.o
  CC       gnunet-helper-exit.o
  CCLD     gnunet-helper-exit
  CCLD     gnunet-daemon-exit
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/exit'
Making all in pt
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/pt'
  CC       gnunet-daemon-pt.o
  CCLD     gnunet-daemon-pt
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/pt'
Making all in secretsharing
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/secretsharing'
  CC       secretsharing_api.lo
  CC       secretsharing_common.lo
  CC       gnunet-secretsharing-profiler.o
  CC       gnunet_service_secretsharing-gnunet-service-secretsharing.o
  CC       gnunet_service_secretsharing-secretsharing_common.o
  CCLD     libgnunetsecretsharing.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-secretsharing-profiler
  CCLD     gnunet-service-secretsharing
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/secretsharing'
Making all in reclaim
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/reclaim'
  CC       reclaim_api.lo
  CC       reclaim_attribute.lo
  CC       reclaim_credential.lo
  CC       plugin_gnsrecord_reclaim.lo
  CC       plugin_reclaim_attribute_basic.lo
  CC       plugin_reclaim_credential_jwt.lo
  CC       libgnunet_plugin_rest_openid_connect_la-plugin_rest_openid_connect.lo
  CC       libgnunet_plugin_rest_openid_connect_la-oidc_helper.lo
  CC       libgnunet_plugin_rest_reclaim_la-plugin_rest_reclaim.lo
  CC       libgnunet_plugin_rest_reclaim_la-json_reclaim.lo
  CC       gnunet-reclaim.o
  CC       gnunet-service-reclaim.o
  CC       gnunet-service-reclaim_tickets.o
  CCLD     libgnunetreclaim.la
  CCLD     libgnunet_plugin_gnsrecord_reclaim.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_reclaim_attribute_basic.la
  CCLD     libgnunet_plugin_reclaim_credential_jwt.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_rest_openid_connect.la
  CCLD     libgnunet_plugin_rest_reclaim.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-reclaim
  CCLD     gnunet-service-reclaim
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/reclaim'
Making all in rps
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/rps'
  CC       libgnunetrps_la-gnunet-service-rps_sampler_elem.lo
  CC       libgnunetrps_la-rps-test_util.lo
  CC       libgnunetrps_la-rps-sampler_common.lo
  CC       libgnunetrps_la-rps-sampler_client.lo
rps-sampler_client.c:277:1: warning: 'prob_observed_n_peers' defined but not used [-Wunused-function]
 prob_observed_n_peers (uint32_t num_peers_estim,
 ^~~~~~~~~~~~~~~~~~~~~
rps-sampler_client.c: In function 'sampler_mod_get_rand_peer':
rps-sampler_client.c:433:3: warning: 'prob_observed_n' may be used uninitialized in this function [-Wmaybe-uninitialized]
   gpc->cont (gpc->cont_cls, gpc->id, prob_observed_n, num_observed);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  CC       libgnunetrps_la-rps_api.lo
  CC       gnunet-rps.o
  CC       gnunet-service-rps_sampler_elem.o
  CC       rps-sampler_common.o
  CC       gnunet-service-rps_sampler.o
  CC       gnunet-service-rps_custommap.o
  CC       gnunet-service-rps_view.o
  CC       gnunet-service-rps.o
  CC       rps-test_util.o
  CC       gnunet-rps-profiler.o
gnunet-service-rps.c: In function 'write_histogram_to_file':
gnunet-service-rps.c:3001:44: warning: passing argument 1 of 'store_prefix_file_name' makes integer from pointer without a cast [-Wint-conversion]
   file_name_full = store_prefix_file_name (&own_identity,
                                            ^~~~~~~~~~~~~
In file included from gnunet-service-rps.c:35:
rps-test_util.h:111:1: note: expected 'unsigned int' but argument is of type 'struct GNUNET_PeerIdentity *'
 store_prefix_file_name (const unsigned int index,
 ^~~~~~~~~~~~~~~~~~~~~~
gnunet-service-rps.c: At top level:
gnunet-service-rps.c:600:1: warning: 'do_mal_round' declared 'static' but never defined [-Wunused-function]
 do_mal_round (void *cls);
 ^~~~~~~~~~~~
gnunet-service-rps.c:2475:1: warning: 'add_peer_array_to_set' defined but not used [-Wunused-function]
 add_peer_array_to_set (const struct GNUNET_PeerIdentity *peer_array,
 ^~~~~~~~~~~~~~~~~~~~~
  CCLD     libgnunetrps.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-rps
gnunet-rps-profiler.c: In function 'mal_cb':
gnunet-rps-profiler.c:1686:12: warning: unused variable 'num_mal_peers' [-Wunused-variable]
   uint32_t num_mal_peers;
            ^~~~~~~~~~~~~
gnunet-rps-profiler.c: In function 'profiler_reply_handle_info':
gnunet-rps-profiler.c:2083:16: warning: unused variable 'i' [-Wunused-variable]
   unsigned int i;
                ^
gnunet-rps-profiler.c: In function 'post_profiler':
gnunet-rps-profiler.c:2904:41: warning: passing argument 1 of 'store_prefix_file_name' makes integer from pointer without a cast [-Wint-conversion]
         store_prefix_file_name (rps_peer->peer_id, "stats");
                                 ~~~~~~~~^~~~~~~~~
In file included from gnunet-rps-profiler.c:33:
rps-test_util.h:111:1: note: expected 'unsigned int' but argument is of type 'struct GNUNET_PeerIdentity *'
 store_prefix_file_name (const unsigned int index,
 ^~~~~~~~~~~~~~~~~~~~~~
At top level:
gnunet-rps-profiler.c:1729:1: warning: 'churn_test_cb' defined but not used [-Wunused-function]
 churn_test_cb (struct RPSPeer *rps_peer)
 ^~~~~~~~~~~~~
gnunet-rps-profiler.c:1684:1: warning: 'mal_cb' defined but not used [-Wunused-function]
 mal_cb (struct RPSPeer *rps_peer)
 ^~~~~~
gnunet-rps-profiler.c:1658:1: warning: 'mal_pre' defined but not used [-Wunused-function]
 mal_pre (struct RPSPeer *rps_peer, struct GNUNET_RPS_Handle *h)
 ^~~~~~~
gnunet-rps-profiler.c:1642:1: warning: 'mal_init_peer' defined but not used [-Wunused-function]
 mal_init_peer (struct RPSPeer *rps_peer)
 ^~~~~~~~~~~~~
gnunet-rps-profiler.c:1235:1: warning: 'seed_peers' defined but not used [-Wunused-function]
 seed_peers (void *cls)
 ^~~~~~~~~~
  CCLD     gnunet-service-rps
  CCLD     gnunet-rps-profiler
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/rps'
Making all in abd
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/abd'
  CC       abd_api.lo
  CC       abd_serialization.lo
  CC       delegate_misc.lo
  CC       plugin_gnsrecord_abd.lo
  CC       gnunet-abd.o
  CC       gnunet-service-abd.o
  CCLD     libgnunetabd.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_gnsrecord_abd.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-abd
  CCLD     gnunet-service-abd
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/abd'
Making all in abe
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/abe'
  CC       abe.lo
  CCLD     libgnunetabe.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/abe'
Making all in auction
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/auction'
  CC       gnunet-auction-create.o
  CC       gnunet-auction-info.o
  CC       gnunet-auction-join.o
  CC       gnunet-service-auction.o
  CCLD     gnunet-auction-create
gnunet-service-auction.c: In function 'handle_create':
gnunet-service-auction.c:59:12: warning: variable 'size' set but not used [-Wunused-but-set-variable]
   uint16_t size;
            ^~~~
  CCLD     gnunet-auction-info
  CCLD     gnunet-auction-join
  CCLD     gnunet-service-auction
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/auction'
Making all in integration-tests
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/integration-tests'
gawk -v bdir="/usr/bin" -v py="/openwrt/staging_dir/hostpkg/bin/python3" -v awkay="/openwrt/staging_dir/host/bin/awk" -v pfx="/usr" -v prl="/openwrt/staging_dir/host/bin/perl" -v sysconfdirectory="/etc" -v pkgdatadirectory="/usr/share/gnunet" -f ../../bin/dosubst.awk < ./gnunet_testing.py.in > gnunet_testing.py
gawk -v bdir="/usr/bin" -v py="/openwrt/staging_dir/hostpkg/bin/python3" -v awkay="/openwrt/staging_dir/host/bin/awk" -v pfx="/usr" -v prl="/openwrt/staging_dir/host/bin/perl" -v sysconfdirectory="/etc" -v pkgdatadirectory="/usr/share/gnunet" -f ../../bin/dosubst.awk < ./gnunet_pyexpect.py.in > gnunet_pyexpect.py
chmod +x gnunet_pyexpect.py
chmod +x gnunet_testing.py
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/integration-tests'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src'
make[7]: Nothing to be done for 'all-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src'
Making all in po
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/po'
*** error: gettext infrastructure mismatch: using a Makefile.in.in from gettext version 0.18 but the autoconf macros are from gettext version 0.20
make[6]: *** [Makefile:674: check-macro-version] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/po'
make[5]: *** [Makefile:630: all-recursive] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3'
make[4]: *** [Makefile:520: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3'
make[3]: *** [Makefile:404: /openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/.built] Error 2
```
