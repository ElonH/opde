---
title: "compile.41"
date: 2021-06-23 23:20:13.557458
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
make package/feeds/packages/strongswan/compile -j$(nproc) || make package/feeds/packages/strongswan/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/101-musl-fixes.patch using plaintext: 
patching file src/libstrongswan/library.h
patching file src/libstrongswan/musl.h
patching file src/libcharon/plugins/kernel_netlink/kernel_netlink_ipsec.c
patching file src/libcharon/plugins/kernel_netlink/kernel_netlink_net.c
patching file src/libcharon/plugins/kernel_netlink/kernel_netlink_shared.c
patching file src/libstrongswan/plugins/bliss/bliss_huffman.c

Applying ./patches/203-uci.patch using plaintext: 
patching file src/libcharon/plugins/uci/uci_parser.c

Applying ./patches/210-sleep.patch using plaintext: 
patching file src/ipsec/_ipsec.in

Applying ./patches/300-include-ipsec-hotplug.patch using plaintext: 
patching file src/_updown/_updown.in

Applying ./patches/305-minimal_dh_plugin.patch using plaintext: 
patching file configure.ac
patching file src/libstrongswan/Makefile.am
patching file src/libstrongswan/plugins/gmpdh/Makefile.am
patching file src/libstrongswan/plugins/gmpdh/gmpdh_plugin.c
patching file src/libstrongswan/plugins/gmpdh/gmpdh_plugin.h
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-x86_64_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal -I m4 -I . --force -I m4/config
autoreconf: configure.ac: tracing
autoreconf: running: /openwrt/staging_dir/host/bin/libtoolize --install --force
OpenWrt-libtoolize: putting auxiliary files in `.'.
OpenWrt-libtoolize: linking file `./config.guess'
OpenWrt-libtoolize: linking file `./config.sub'
OpenWrt-libtoolize: linking file `./install-sh'
OpenWrt-libtoolize: linking file `./ltmain.sh'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `m4/config'.
OpenWrt-libtoolize: linking file `m4/config/libtool.m4'
OpenWrt-libtoolize: linking file `m4/config/ltoptions.m4'
OpenWrt-libtoolize: linking file `m4/config/ltsugar.m4'
OpenWrt-libtoolize: linking file `m4/config/ltversion.m4'
OpenWrt-libtoolize: linking file `m4/config/lt~obsolete.m4'
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
checking whether UID '1000' is supported by ustar format... yes
checking whether GID '1000' is supported by ustar format... yes
checking how to create a ustar tar archive... gnutar
checking whether make supports nested variables... (cached) yes
checking pkg-config is at least version 0.9.0... yes
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking configured UDP ports (500, 4500)... ok
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
checking for style of include used by make... GNU
checking dependency style of ccache_cc... gcc3
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-openwrt-linux-gnu
checking 32-bit host C ABI... no
checking how to run the C preprocessor... ccache_cc -E
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for ELF binary format... yes
checking for the common suffixes of directories in the library search path... lib,lib,lib64
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
checking whether byte ordering is bigendian... (cached) no
checking how to print strings... printf
checking for a sed that does not truncate output... (cached) /openwrt/staging_dir/host/bin/sed
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
checking whether to build static libraries... no
checking for egrep... (cached) /openwrt/staging_dir/host/bin/grep -E
checking for gawk... (cached) gawk
checking for flex... flex
checking lex output file root... lex.yy
checking lex library... none needed
checking whether yytext is a pointer... no
checking for bison... bison -y
checking for python... /openwrt/staging_dir/host/bin/python
checking for python version... 3.8
checking for python platform... linux
checking for python script directory... ${prefix}/lib/python3.8/site-packages
checking for python extension module directory... ${exec_prefix}/lib/python3.8/site-packages
checking for perl... /openwrt/staging_dir/host/bin/perl
checking for gperf... /openwrt/staging_dir/hostpkg/bin/gperf
checking gperf len type... size_t
checking for stdbool.h that conforms to C99... yes
checking for _Bool... yes
checking for size_t... yes
checking for working alloca.h... yes
checking for alloca... yes
checking whether strerror_r is declared... yes
checking for strerror_r... yes
checking whether strerror_r returns char *... no
checking for library containing dlopen... none required
checking for library containing backtrace... no
checking for backtrace... no
checking for library containing socket... none required
checking for library containing pthread_create... none required
checking for library containing __atomic_and_fetch... none required
checking for dladdr... yes
checking for pthread_condattr_setclock(CLOCK_MONOTONIC)... unknown
checking for pthread_condattr_setclock... yes
checking for pthread_condattr_init... yes
checking for pthread_cond_timedwait_monotonic... no
checking for pthread_cancel... yes
checking for pthread_rwlock_init... yes
checking for pthread_spin_init... yes
checking for sem_timedwait... yes
checking for gettid... no
checking for SYS_gettid... yes
checking for qsort_r... no
checking for prctl... yes
checking for mallinfo... no
checking for getpass... yes
checking for closefrom... no
checking for getpwnam_r... yes
checking for getgrnam_r... yes
checking for getpwuid_r... (cached) yes
checking for chown... yes
checking for fmemopen... yes
checking for funopen... no
checking for mmap... yes
checking for memrchr... yes
checking for setlinebuf... yes
checking for strptime... yes
checking for dirfd... yes
checking for sigwaitinfo... yes
checking for explicit_bzero... yes
checking for syslog... yes
checking sys/sockio.h usability... no
checking sys/sockio.h presence... no
checking for sys/sockio.h... no
checking sys/syscall.h usability... yes
checking sys/syscall.h presence... yes
checking for sys/syscall.h... yes
checking sys/param.h usability... yes
checking sys/param.h presence... yes
checking for sys/param.h... yes
checking glob.h usability... yes
checking glob.h presence... yes
checking for glob.h... yes
checking net/if_tun.h usability... no
checking net/if_tun.h presence... no
checking for net/if_tun.h... no
checking net/pfkeyv2.h usability... no
checking net/pfkeyv2.h presence... no
checking for net/pfkeyv2.h... no
checking netipsec/ipsec.h usability... no
checking netipsec/ipsec.h presence... no
checking for netipsec/ipsec.h... no
checking netinet6/ipsec.h usability... no
checking netinet6/ipsec.h presence... no
checking for netinet6/ipsec.h... no
checking linux/udp.h usability... yes
checking linux/udp.h presence... yes
checking for linux/udp.h... yes
checking for netinet/ip6.h... yes
checking for linux/fib_rules.h... yes
checking for struct sockaddr.sa_len... no
checking for struct sadb_x_policy.sadb_x_policy_priority... yes
checking for in6addr_any... yes
checking for in6_pktinfo... yes
checking for RTM_IFANNOUNCE... no
checking for IPSEC_MODE_BEET... yes
checking for IPSEC_DIR_FWD... yes
checking for RTA_TABLE... yes
checking for __int128... yes
checking for GCC __sync operations... no
checking for register_printf_specifier... no
checking for register_printf_function... no
configure: printf(3) does not support custom format specifiers!
checking for Windows target... no
checking for library containing clock_gettime... none required
checking for clock_gettime... yes
checking for working __attribute__((packed))... yes
checking clang... no
checking x86/x64 target... yes
checking for __gmpz_init in -lgmp... yes
checking mpz_powm_sec... yes
checking gmp.h version >= 4.1.4... yes
checking for ldap_init in -lldap... yes
checking for ber_free in -llber... yes
checking ldap.h usability... yes
checking ldap.h presence... yes
checking for ldap.h... yes
checking for curl_global_init in -lcurl... yes
checking curl/curl.h usability... yes
checking curl/curl.h presence... yes
checking for curl/curl.h... yes
checking for xml... yes
checking for mysql_config... no
configure: error: mysql_config not found!
make[3]: *** [Makefile:661: /openwrt/build_dir/target-x86_64_musl/strongswan-5.9.2/.configured_e9413f68e7121db5cabc93d63fdfb1e8] Error 1
```
