---
title: "compile.8"
date: 2021-05-06 05:08:41.880183
hidden: false
draft: false
weight: -8
---

build number: `8`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/openvpn/compile -j$(nproc) || make package/feeds/packages/openvpn/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-reproducible-remove_DATE.patch using plaintext: 
patching file src/openvpn/options.c

Applying ./patches/100-mbedtls-disable-runtime-version-check.patch using plaintext: 
patching file src/openvpn/ssl_mbedtls.c

Applying ./patches/115-fix-mbedtls-without-renegotiation.patch using plaintext: 
patching file src/openvpn/ssl_mbedtls.c

Applying ./patches/210-build_always_use_internal_lz4.patch using plaintext: 
patching file configure.ac

Applying ./patches/220-disable_des.patch using plaintext: 
patching file src/openvpn/syshead.h
patching file src/openvpn/crypto_mbedtls.c
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-x86_64_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal -I m4 -I . --force -I m4
autoreconf: configure.ac: tracing
autoreconf: running: /openwrt/staging_dir/host/bin/libtoolize --install --force
OpenWrt-libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, `.'.
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
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-x86_64_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-x86_64_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
src/openvpnmsica/Makefile.am:48: warning: source file '$(top_srcdir)/src/tapctl/error.c' is in a subdirectory,
src/openvpnmsica/Makefile.am:48: but option 'subdir-objects' is disabled
automake: warning: possible forward-incompatibility.
automake: At least a source file is in a subdirectory, but the 'subdir-objects'
automake: automake option hasn't been enabled.  For now, the corresponding output
automake: object file(s) will be placed in the top-level directory.  However,
automake: this behaviour will change in future Automake versions: they will
automake: unconditionally cause object files to be placed in the same subdirectory
automake: of the corresponding sources.
automake: You are advised to start using 'subdir-objects' option throughout your
automake: project, to avoid future incompatibilities.
src/openvpnmsica/Makefile.am:48: warning: source file '$(top_srcdir)/src/tapctl/tap.c' is in a subdirectory,
src/openvpnmsica/Makefile.am:48: but option 'subdir-objects' is disabled
src/openvpnserv/Makefile.am:32: warning: source file '$(top_srcdir)/src/openvpn/block_dns.c' is in a subdirectory,
src/openvpnserv/Makefile.am:32: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:27: warning: source file '$(openvpn_srcdir)/platform.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:27: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:27: warning: source file '$(openvpn_srcdir)/buffer.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:27: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:27: warning: source file '$(openvpn_srcdir)/argv.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:27: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:104: warning: source file '$(openvpn_srcdir)/buffer.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:104: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:104: warning: source file '$(openvpn_srcdir)/crypto.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:104: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:104: warning: source file '$(openvpn_srcdir)/crypto_mbedtls.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:104: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:104: warning: source file '$(openvpn_srcdir)/crypto_openssl.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:104: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:104: warning: source file '$(openvpn_srcdir)/otime.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:104: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:104: warning: source file '$(openvpn_srcdir)/packet_id.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:104: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:104: warning: source file '$(openvpn_srcdir)/platform.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:104: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:104: warning: source file '$(openvpn_srcdir)/base64.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:104: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:35: warning: source file '$(openvpn_srcdir)/platform.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:35: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:42: warning: source file '$(openvpn_srcdir)/buffer.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:42: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:42: warning: source file '$(openvpn_srcdir)/crypto.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:42: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:42: warning: source file '$(openvpn_srcdir)/crypto_mbedtls.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:42: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:42: warning: source file '$(openvpn_srcdir)/crypto_openssl.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:42: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:42: warning: source file '$(openvpn_srcdir)/otime.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:42: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:42: warning: source file '$(openvpn_srcdir)/packet_id.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:42: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:42: warning: source file '$(openvpn_srcdir)/platform.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:42: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:121: warning: source file '$(openvpn_srcdir)/buffer.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:121: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:121: warning: source file '$(openvpn_srcdir)/crypto.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:121: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:121: warning: source file '$(openvpn_srcdir)/crypto_mbedtls.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:121: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:121: warning: source file '$(openvpn_srcdir)/crypto_openssl.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:121: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:121: warning: source file '$(openvpn_srcdir)/otime.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:121: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:121: warning: source file '$(openvpn_srcdir)/packet_id.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:121: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:121: warning: source file '$(openvpn_srcdir)/platform.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:121: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:87: warning: source file '$(openvpn_srcdir)/networking_sitnl.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:87: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:87: warning: source file '$(openvpn_srcdir)/buffer.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:87: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:87: warning: source file '$(openvpn_srcdir)/crypto.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:87: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:87: warning: source file '$(openvpn_srcdir)/crypto_mbedtls.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:87: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:87: warning: source file '$(openvpn_srcdir)/crypto_openssl.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:87: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:87: warning: source file '$(openvpn_srcdir)/otime.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:87: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:87: warning: source file '$(openvpn_srcdir)/packet_id.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:87: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:87: warning: source file '$(openvpn_srcdir)/platform.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:87: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:54: warning: source file '$(openvpn_srcdir)/buffer.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:54: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:54: warning: source file '$(openvpn_srcdir)/otime.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:54: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:54: warning: source file '$(openvpn_srcdir)/packet_id.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:54: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:54: warning: source file '$(openvpn_srcdir)/platform.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:54: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:68: warning: source file '$(openvpn_srcdir)/argv.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:68: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:68: warning: source file '$(openvpn_srcdir)/base64.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:68: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:68: warning: source file '$(openvpn_srcdir)/buffer.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:68: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:68: warning: source file '$(openvpn_srcdir)/crypto.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:68: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:68: warning: source file '$(openvpn_srcdir)/crypto_mbedtls.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:68: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:68: warning: source file '$(openvpn_srcdir)/crypto_openssl.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:68: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:68: warning: source file '$(openvpn_srcdir)/env_set.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:68: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:68: warning: source file '$(openvpn_srcdir)/otime.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:68: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:68: warning: source file '$(openvpn_srcdir)/packet_id.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:68: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:68: warning: source file '$(openvpn_srcdir)/platform.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:68: but option 'subdir-objects' is disabled
tests/unit_tests/openvpn/Makefile.am:68: warning: source file '$(openvpn_srcdir)/run_command.c' is in a subdirectory,
tests/unit_tests/openvpn/Makefile.am:68: but option 'subdir-objects' is disabled
tests/unit_tests/plugins/auth-pam/Makefile.am:10: warning: source file '$(sut_sourcedir)/utils.c' is in a subdirectory,
tests/unit_tests/plugins/auth-pam/Makefile.am:10: but option 'subdir-objects' is disabled
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
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-openwrt-linux-gnu
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
checking pkg-config is at least version 0.9.0... yes
checking how to run the C preprocessor... ccache_cc -E
checking whether ln -s works... yes
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking whether make sets $(MAKE)... (cached) yes
checking for ifconfig... no
checking for route... no
checking for ip... /sbin/ip
checking for systemd-ask-password... no
checking for netstat... /sbin/netstat
checking for git... git
checking for rst2man... no
checking for rst2html... no
checking how to print strings... printf
checking for a sed that does not truncate output... (cached) /openwrt/staging_dir/host/bin/sed
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
checking whether to build static libraries... yes
checking for x86_64-openwrt-linux-windres... no
checking for windres... no
checking for an ANSI C-conforming const... yes
checking for inline... inline
checking for working volatile... yes
checking for off_t... yes
checking for pid_t... yes
checking for size_t... yes
checking for uid_t in sys/types.h... yes
checking for int8_t... yes
checking for int16_t... yes
checking for int32_t... yes
checking for int64_t... yes
checking for uint8_t... yes
checking for uint16_t... yes
checking for uint32_t... yes
checking for uint64_t... yes
checking return type of signal handlers... void
checking for ISO C 1999 vararg macro support... yes
checking for GNU GCC vararg macro support... yes
checking for socklen_t... yes
checking for C compiler empty array size... 0
checking size of unsigned int... (cached) 4
checking size of unsigned long... (cached) 8
checking stdio.h usability... yes
checking stdio.h presence... yes
checking for stdio.h... yes
checking stdarg.h usability... yes
checking stdarg.h presence... yes
checking for stdarg.h... yes
checking limits.h usability... yes
checking limits.h presence... yes
checking for limits.h... yes
checking time.h usability... yes
checking time.h presence... yes
checking for time.h... yes
checking errno.h usability... yes
checking errno.h presence... yes
checking for errno.h... yes
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking io.h usability... no
checking io.h presence... no
checking for io.h... no
checking direct.h usability... no
checking direct.h presence... no
checking for direct.h... no
checking ctype.h usability... yes
checking ctype.h presence... yes
checking for ctype.h... yes
checking for sys/types.h... (cached) yes
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking signal.h usability... yes
checking signal.h presence... yes
checking for signal.h... yes
checking for unistd.h... (cached) yes
checking for dlfcn.h... (cached) yes
checking netinet/in.h usability... yes
checking netinet/in.h presence... yes
checking for netinet/in.h... yes
checking netinet/in_systm.h usability... yes
checking netinet/in_systm.h presence... yes
checking for netinet/in_systm.h... yes
checking netinet/tcp.h usability... yes
checking netinet/tcp.h presence... yes
checking for netinet/tcp.h... yes
checking arpa/inet.h usability... yes
checking arpa/inet.h presence... yes
checking for arpa/inet.h... yes
checking netdb.h usability... yes
checking netdb.h presence... yes
checking for netdb.h... yes
checking windows.h usability... no
checking windows.h presence... no
checking for windows.h... no
checking winsock2.h usability... no
checking winsock2.h presence... no
checking for winsock2.h... no
checking ws2tcpip.h usability... no
checking ws2tcpip.h presence... no
checking for ws2tcpip.h... no
checking versionhelpers.h usability... no
checking versionhelpers.h presence... no
checking for versionhelpers.h... no
checking sys/time.h usability... yes
checking sys/time.h presence... yes
checking for sys/time.h... yes
checking sys/ioctl.h usability... yes
checking sys/ioctl.h presence... yes
checking for sys/ioctl.h... yes
checking for sys/stat.h... (cached) yes
checking sys/mman.h usability... yes
checking sys/mman.h presence... yes
checking for sys/mman.h... yes
checking sys/file.h usability... yes
checking sys/file.h presence... yes
checking for sys/file.h... yes
checking sys/wait.h usability... yes
checking sys/wait.h presence... yes
checking for sys/wait.h... yes
checking for unistd.h... (cached) yes
checking for signal.h... (cached) yes
checking libgen.h usability... yes
checking libgen.h presence... yes
checking for libgen.h... yes
checking stropts.h usability... yes
checking stropts.h presence... yes
checking for stropts.h... yes
checking syslog.h usability... yes
checking syslog.h presence... yes
checking for syslog.h... yes
checking pwd.h usability... yes
checking pwd.h presence... yes
checking for pwd.h... yes
checking grp.h usability... yes
checking grp.h presence... yes
checking for grp.h... yes
checking sys/sockio.h usability... no
checking sys/sockio.h presence... no
checking for sys/sockio.h... no
checking sys/uio.h usability... yes
checking sys/uio.h presence... yes
checking for sys/uio.h... yes
checking linux/sockios.h usability... yes
checking linux/sockios.h presence... yes
checking for linux/sockios.h... yes
checking linux/types.h usability... yes
checking linux/types.h presence... yes
checking for linux/types.h... yes
checking poll.h usability... yes
checking poll.h presence... yes
checking for poll.h... yes
checking sys/epoll.h usability... yes
checking sys/epoll.h presence... yes
checking for sys/epoll.h... yes
checking err.h usability... yes
checking err.h presence... yes
checking for err.h... yes
checking for net/if.h... yes
checking for netinet/ip.h... yes
checking for resolv.h... yes
checking for sys/un.h... yes
checking for net/if_utun.h... no
checking for sys/kern_control.h... no
checking for in_addr_t... yes
checking for in_port_t... yes
checking for struct iphdr... yes
checking for struct sock_extended_err... no
checking for struct msghdr... yes
checking for struct cmsghdr... yes
checking for struct in_pktinfo... yes
checking for sa_family_t... yes
checking for struct in_pktinfo.ipi_spec_dst... yes
checking for struct sockaddr_in6... yes
checking whether SO_MARK is declared... yes
configure: checking anonymous union support...
yes
checking linker supports --wrap... yes
checking whether SIGHUP is declared... yes
checking whether SIGINT is declared... yes
checking whether SIGUSR1 is declared... yes
checking whether SIGUSR2 is declared... yes
checking whether SIGTERM is declared... yes
checking vfork.h usability... no
checking vfork.h presence... no
checking for vfork.h... no
checking for fork... yes
checking for vfork... yes
checking for working fork... cross
configure: WARNING: result yes guessed because of cross compilation
checking for working vfork... (cached) yes
checking for daemon... yes
checking for chroot... yes
checking for getpwnam... yes
checking for setuid... yes
checking for nice... yes
checking for system... yes
checking for getpid... yes
checking for dup... yes
checking for dup2... yes
checking for getpass... yes
checking for syslog... yes
checking for openlog... yes
checking for mlockall... yes
checking for getgrnam... yes
checking for setgid... yes
checking for setgroups... yes
checking for stat... yes
checking for flock... yes
checking for readv... yes
checking for writev... yes
checking for time... yes
checking for gettimeofday... (cached) yes
checking for ctime... yes
checking for memset... yes
checking for vsnprintf... (cached) yes
checking for strdup... yes
checking for setsid... yes
checking for chdir... yes
checking for putenv... yes
checking for getpeername... yes
checking for unlink... yes
checking for chsize... no
checking for ftruncate... yes
checking for execve... yes
checking for getpeereid... no
checking for umask... yes
checking for basename... yes
checking for dirname... yes
checking for access... yes
checking for epoll_create... yes
checking for strsep... yes
checking for dlopen in -ldl... yes
checking for inet_ntoa in -lnsl... no
checking for socket in -lsocket... no
checking for gethostbyname in -lresolv... yes
checking for sendmsg... yes
checking for recvmsg... yes
checking for inet_ntop... yes
checking for inet_pton... yes
checking for socket... yes
checking for recv... yes
checking for recvfrom... yes
checking for send... yes
checking for sendto... yes
checking for listen... yes
checking for accept... yes
checking for connect... yes
checking for bind... yes
checking for select... yes
checking for gethostbyname... yes
checking for inet_ntoa... yes
checking for setsockopt... yes
checking for getsockopt... yes
checking for getsockname... yes
checking for poll... yes
checking for library containing __res_init... no
checking for library containing res_9_init... no
checking for library containing res_init... none required
checking net/if_tun.h usability... no
checking net/if_tun.h presence... no
checking for net/if_tun.h... no
checking net/tun/if_tun.h usability... no
checking net/tun/if_tun.h presence... no
checking for net/tun/if_tun.h... no
checking linux/if_tun.h usability... yes
checking linux/if_tun.h presence... yes
checking for linux/if_tun.h... yes
checking tap-windows.h usability... no
checking tap-windows.h presence... no
checking for tap-windows.h... no
checking whether TUNSETPERSIST is declared... yes
checking for setcon in -lselinux... yes
checking for pam_start in -lpam... yes
checking for PKCS11_HELPER... no
checking for mbedtls_ssl_init in -lmbedtls... no
configure: error: Could not find mbed TLS.
make[3]: *** [Makefile:147: /openwrt/build_dir/target-x86_64_musl/openvpn-mbedtls/openvpn-2.5.2/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
