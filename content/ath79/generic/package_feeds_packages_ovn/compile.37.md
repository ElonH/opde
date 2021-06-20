---
title: "compile.37"
date: 2021-06-20 22:36:26.345920
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
make package/feeds/packages/ovn/compile -j$(nproc) || make package/feeds/packages/ovn/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/0001-build-skip-check-and-use-of-libunbound.patch using plaintext: 
patching file configure.ac

Applying ./patches/0002-build-skip-tests-and-docs.patch using plaintext: 
patching file Makefile.am
Hunk #1 succeeded at 479 (offset -4 lines).

Applying ./patches/0003-ovn-lib-fix-install_dir.patch using plaintext: 
patching file utilities/ovn-lib.in
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
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
configure.ac:25: installing 'build-aux/compile'
configure.ac:21: installing 'build-aux/missing'
Makefile.am: installing 'build-aux/depcomp'
autoreconf: Leaving directory `.'
configure: WARNING: unrecognized options: --disable-nls, --disable-libcapng
configure: loading site script /openwrt/include/site/mips
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking how to create a pax tar archive... gnutar
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
checking whether we are using the GNU C++ compiler... yes
checking whether ccache_cxx accepts -g... yes
checking dependency style of ccache_cxx... gcc3
checking how to run the C preprocessor... ccache_cc -E
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking pkg-config is at least version 0.9.0... yes
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
checking whether byte ordering is bigendian... (cached) yes
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
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
checking for mips-openwrt-linux-ar... mips-openwrt-linux-musl-gcc-ar
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
checking how to run the C++ preprocessor... ccache_cxx -E
checking for ld used by ccache_cxx... mips-openwrt-linux-musl-ld
checking if the linker (mips-openwrt-linux-musl-ld) is GNU ld... yes
checking whether the ccache_cxx linker (mips-openwrt-linux-musl-ld) supports shared libraries... yes
checking for ccache_cxx option to produce PIC... -fPIC -DPIC
checking if ccache_cxx PIC flag -fPIC -DPIC works... yes
checking if ccache_cxx static flag -static works... yes
checking if ccache_cxx supports -c -o file.o... yes
checking if ccache_cxx supports -c -o file.o... (cached) yes
checking whether the ccache_cxx linker (mips-openwrt-linux-musl-ld) supports shared libraries... yes
checking dynamic linker characteristics... (cached) GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking for library containing pow... none required
checking for library containing clock_gettime... none required
checking for library containing timer_create... none required
checking for library containing pthread_rwlock_tryrdlock... none required
checking for library containing pthread_rwlockattr_destroy... none required
checking whether strerror_r is declared... yes
checking for strerror_r... yes
checking whether strerror_r returns char *... no
checking for MSVC x64 compiler... no
checking windows.h usability... no
checking windows.h presence... no
checking for windows.h... no
checking for pkg-config... /openwrt/staging_dir/host/bin/pkg-config
checking for openssl/ssl.h in /usr/local/ssl... no
checking for openssl/ssl.h in /usr/lib/ssl... no
checking for openssl/ssl.h in /usr/ssl... no
checking for openssl/ssl.h in /usr/pkg... no
checking for openssl/ssl.h in /usr/local... no
checking for openssl/ssl.h in /usr... yes
checking whether compiling and linking against OpenSSL works... no
configure: WARNING: Cannot find openssl:



OpenFlow connections over SSL will not be supported.
(You may use --disable-ssl to suppress this warning.)
checking for Python 3 (version 3.4 or later)... (cached) /openwrt/staging_dir/hostpkg/bin/python3.9
checking for flake8... (cached) no
checking for sphinx... (cached) no
checking for dot... no
checking net/if_dl.h usability... no
checking net/if_dl.h presence... no
checking for net/if_dl.h... no
checking whether strtok_r macro segfaults on some inputs... yes
checking whether sys_siglist is declared... (cached) no
checking for struct stat.st_mtim.tv_nsec... yes
checking for struct stat.st_mtimensec... no
checking for struct ifreq.ifr_flagshigh... no
checking for struct mmsghdr.msg_len... yes
checking for struct sockaddr_in6.sin6_scope_id... yes
checking for strnlen... yes
checking for getloadavg... yes
checking for statvfs... yes
checking for getmntent_r... yes
checking for sendmmsg... yes
checking for clock_gettime... yes
checking mntent.h usability... yes
checking mntent.h presence... yes
checking for mntent.h... yes
checking sys/statvfs.h usability... yes
checking sys/statvfs.h presence... yes
checking for sys/statvfs.h... yes
checking linux/types.h usability... yes
checking linux/types.h presence... yes
checking for linux/types.h... yes
checking linux/if_ether.h usability... yes
checking linux/if_ether.h presence... yes
checking for linux/if_ether.h... yes
checking linux/net_namespace.h usability... yes
checking linux/net_namespace.h presence... yes
checking for linux/net_namespace.h... yes
checking stdatomic.h usability... yes
checking stdatomic.h presence... yes
checking for stdatomic.h... yes
checking bits/floatn-common.h usability... no
checking bits/floatn-common.h presence... no
checking for bits/floatn-common.h... no
checking for net/if_mib.h... no
checking for library containing backtrace... no
checking linux/perf_event.h usability... yes
checking linux/perf_event.h presence... yes
checking for linux/perf_event.h... yes
checking valgrind/valgrind.h usability... no
checking valgrind/valgrind.h presence... no
checking for valgrind/valgrind.h... no
checking for groff... no
checking whether ccache_cc has <threads.h> that supports thread_local... yes
checking for library containing __atomic_load_8... -latomic
checking whether ccache_cc supports GCC 4.0+ atomic built-ins... no
checking value of __atomic_always_lock_free(1)... unsupported
checking value of __atomic_always_lock_free(2)... unsupported
checking value of __atomic_always_lock_free(4)... unsupported
checking value of __atomic_always_lock_free(8)... unsupported
checking for library containing aio_write... none required
checking for pthread_set_name_np... no
checking for pthread_setname_np() variant... glibc
checking whether __linux__ is defined... true
checking linker output version information... libX-20.12.so.0.0.0)
checking whether ccache_cxx supports C++11 features by default... yes
checking for working posix_memalign... no
checking whether the preprocessor supports include_next... yes
checking whether system header files limit the line length... no
checking for stdio.h... yes
checking for string.h... (cached) yes
checking whether ccache_cc accepts -Werror... yes
checking whether ccache_cc accepts -Wall... yes
checking whether ccache_cc accepts -Wextra... yes
checking whether ccache_cc accepts -Wno-sign-compare... yes
checking whether ccache_cc accepts -Wpointer-arith... yes
checking whether ccache_cc accepts -Wformat -Wformat-security... yes
checking whether ccache_cc accepts -Wswitch-enum... yes
checking whether ccache_cc accepts -Wunused-parameter... yes
checking whether ccache_cc accepts -Wbad-function-cast... yes
checking whether ccache_cc accepts -Wcast-align... yes
checking whether ccache_cc accepts -Wstrict-prototypes... yes
checking whether ccache_cc accepts -Wold-style-definition... yes
checking whether ccache_cc accepts -Wmissing-prototypes... yes
checking whether ccache_cc accepts -Wmissing-field-initializers... yes
checking whether ccache_cc accepts -Wthread-safety... no
checking whether ccache_cc accepts -fno-strict-aliasing... yes
checking whether ccache_cc accepts -Wswitch-bool... yes
checking whether ccache_cc accepts -Wlogical-not-parentheses... yes
checking whether ccache_cc accepts -Wsizeof-array-argument... yes
checking whether ccache_cc accepts -Wbool-compare... yes
checking whether ccache_cc accepts -Wshift-negative-value... yes
checking whether ccache_cc accepts -Wduplicated-cond... yes
checking whether ccache_cc accepts -Qunused-arguments... no
checking whether ccache_cc accepts -Wshadow... yes
checking whether ccache_cc accepts -Wmultistatement-macros... yes
checking whether ccache_cc accepts -Wcast-align=strict... yes
checking whether ccache_cc accepts -Wno-null-pointer-arithmetic... no
checking whether ccache_cc accepts -Warray-bounds-pointer-arithmetic... no
checking whether ccache_cc accepts -Wno-unused... yes
checking whether ccache_cc accepts -Wno-unused-parameter... yes
checking target hint for cgcc... other
checking for OVS source directory... /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0
checking for OVS build directory... /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0
OVS version is 2.15.0
checking whether make supports nested variables... (cached) yes
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating lib/libovn.sym
config.status: creating Makefile
config.status: creating tests/atlocal
config.status: creating include/ovn/version.h
config.status: creating config.h
config.status: executing tests/atconfig commands
config.status: executing depfiles commands
config.status: executing libtool commands
config.status: executing include/openflow/openflow.h.stamp commands
config.status: executing utilities/bugtool/dummy commands
config.status: executing utilities/dummy commands
config.status: executing ipsec/dummy commands
configure: WARNING: unrecognized options: --disable-nls, --disable-libcapng
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/ovn-20.12.0'
 cd . && /bin/bash /openwrt/build_dir/target-mips_24kc_musl/ovn-20.12.0/build-aux/missing automake-1.15 --foreign Makefile
 cd . && /bin/bash ./config.status Makefile depfiles
config.status: creating Makefile
config.status: executing depfiles commands
PYTHONPATH=/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/python":"$PYTHONPATH PYTHONDONTWRITEBYTECODE=yes /openwrt/staging_dir/hostpkg/bin/python3.9 /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/ovsdb/ovsdb-idlc.in annotate ./ovn-sb.ovsschema ./lib/ovn-sb-idl.ann > lib/ovn-sb-idl.ovsidl.tmp && \
mv lib/ovn-sb-idl.ovsidl.tmp lib/ovn-sb-idl.ovsidl
PYTHONPATH=/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/python":"$PYTHONPATH PYTHONDONTWRITEBYTECODE=yes /openwrt/staging_dir/hostpkg/bin/python3.9 /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/ovsdb/ovsdb-idlc.in annotate ./ovn-nb.ovsschema ./lib/ovn-nb-idl.ann > lib/ovn-nb-idl.ovsidl.tmp && \
mv lib/ovn-nb-idl.ovsidl.tmp lib/ovn-nb-idl.ovsidl
PYTHONPATH=/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/python":"$PYTHONPATH PYTHONDONTWRITEBYTECODE=yes /openwrt/staging_dir/hostpkg/bin/python3.9 /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/ovsdb/ovsdb-idlc.in annotate ./ovn-ic-nb.ovsschema ./lib/ovn-ic-nb-idl.ann > lib/ovn-ic-nb-idl.ovsidl.tmp && \
mv lib/ovn-ic-nb-idl.ovsidl.tmp lib/ovn-ic-nb-idl.ovsidl
PYTHONPATH=/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/python":"$PYTHONPATH PYTHONDONTWRITEBYTECODE=yes /openwrt/staging_dir/hostpkg/bin/python3.9 /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/ovsdb/ovsdb-idlc.in annotate ./ovn-ic-sb.ovsschema ./lib/ovn-ic-sb-idl.ann > lib/ovn-ic-sb-idl.ovsidl.tmp && \
mv lib/ovn-ic-sb-idl.ovsidl.tmp lib/ovn-ic-sb-idl.ovsidl
PYTHONPATH=/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/python":"$PYTHONPATH PYTHONDONTWRITEBYTECODE=yes /openwrt/staging_dir/hostpkg/bin/python3.9 /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/ovsdb/ovsdb-idlc.in c-idl-source lib/ovn-sb-idl.ovsidl > lib/ovn-sb-idl.c.tmp && mv lib/ovn-sb-idl.c.tmp lib/ovn-sb-idl.c
PYTHONPATH=/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/python":"$PYTHONPATH PYTHONDONTWRITEBYTECODE=yes /openwrt/staging_dir/hostpkg/bin/python3.9 /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/ovsdb/ovsdb-idlc.in c-idl-header lib/ovn-sb-idl.ovsidl > lib/ovn-sb-idl.h.tmp && mv lib/ovn-sb-idl.h.tmp lib/ovn-sb-idl.h
PYTHONPATH=/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/python":"$PYTHONPATH PYTHONDONTWRITEBYTECODE=yes /openwrt/staging_dir/hostpkg/bin/python3.9 /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/ovsdb/ovsdb-idlc.in c-idl-source lib/ovn-nb-idl.ovsidl > lib/ovn-nb-idl.c.tmp && mv lib/ovn-nb-idl.c.tmp lib/ovn-nb-idl.c
PYTHONPATH=/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/python":"$PYTHONPATH PYTHONDONTWRITEBYTECODE=yes /openwrt/staging_dir/hostpkg/bin/python3.9 /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/ovsdb/ovsdb-idlc.in c-idl-header lib/ovn-nb-idl.ovsidl > lib/ovn-nb-idl.h.tmp && mv lib/ovn-nb-idl.h.tmp lib/ovn-nb-idl.h
PYTHONPATH=/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/python":"$PYTHONPATH PYTHONDONTWRITEBYTECODE=yes /openwrt/staging_dir/hostpkg/bin/python3.9 /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/ovsdb/ovsdb-idlc.in c-idl-source lib/ovn-ic-nb-idl.ovsidl > lib/ovn-ic-nb-idl.c.tmp && mv lib/ovn-ic-nb-idl.c.tmp lib/ovn-ic-nb-idl.c
PYTHONPATH=/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/python":"$PYTHONPATH PYTHONDONTWRITEBYTECODE=yes /openwrt/staging_dir/hostpkg/bin/python3.9 /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/ovsdb/ovsdb-idlc.in c-idl-header lib/ovn-ic-nb-idl.ovsidl > lib/ovn-ic-nb-idl.h.tmp && mv lib/ovn-ic-nb-idl.h.tmp lib/ovn-ic-nb-idl.h
PYTHONPATH=/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/python":"$PYTHONPATH PYTHONDONTWRITEBYTECODE=yes /openwrt/staging_dir/hostpkg/bin/python3.9 /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/ovsdb/ovsdb-idlc.in c-idl-source lib/ovn-ic-sb-idl.ovsidl > lib/ovn-ic-sb-idl.c.tmp && mv lib/ovn-ic-sb-idl.c.tmp lib/ovn-ic-sb-idl.c
PYTHONPATH=/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/python":"$PYTHONPATH PYTHONDONTWRITEBYTECODE=yes /openwrt/staging_dir/hostpkg/bin/python3.9 /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/ovsdb/ovsdb-idlc.in c-idl-header lib/ovn-ic-sb-idl.ovsidl > lib/ovn-ic-sb-idl.h.tmp && mv lib/ovn-ic-sb-idl.h.tmp lib/ovn-ic-sb-idl.h
make  all-am
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/ovn-20.12.0'
(echo '/* -*- mode: c; buffer-read-only: t -*- */' && sed < ./lib/ovn-dirs.c.in \
	-e 's,[@]srcdir[@],.,g' \
	-e 's,[@]LOGDIR[@],"/var/log/ovn",g' \
	-e 's,[@]OVN_RUNDIR[@],"/var/run/ovn",g' \
	-e 's,[@]DBDIR[@],"/etc/ovn",g' \
	-e 's,[@]bindir[@],"/usr/bin",g' \
	-e 's,[@]sysconfdir[@],"/etc",g' \
	-e 's,[@]pkgdatadir[@],"/usr/share/ovn",g') \
     > lib/ovn-dirs.c.tmp && \
mv lib/ovn-dirs.c.tmp lib/ovn-dirs.c
depbase=`echo lib/ovn-nb-idl.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/bash ./libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I.   -I ./include  -I ./include -I ./ovn -I ./include -I ./lib -I ./lib -I /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/include -I /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/include -I /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/lib -I /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/lib -I /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0 -I /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0 -I/usr/include -DNDEBUG -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -Wstrict-prototypes -Wall -Wextra -Wno-sign-compare -Wpointer-arith -Wformat -Wformat-security -Wswitch-enum -Wunused-parameter -Wbad-function-cast -Wcast-align -Wstrict-prototypes -Wold-style-definition -Wmissing-prototypes -Wmissing-field-initializers -fno-strict-aliasing -Wswitch-bool -Wlogical-not-parentheses -Wsizeof-array-argument -Wbool-compare -Wshift-negative-value -Wduplicated-cond -Wshadow -Wmultistatement-macros -Wcast-align=strict  -fomit-frame-pointer -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/ovn-20.12.0=ovn-20.12.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto -std=gnu99  -MT lib/ovn-nb-idl.lo -MD -MP -MF $depbase.Tpo -c -o lib/ovn-nb-idl.lo lib/ovn-nb-idl.c &&\
mv -f $depbase.Tpo $depbase.Plo
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I ./include -I ./include -I ./ovn -I ./include -I ./lib -I ./lib -I /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/include -I /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/include -I /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/lib -I /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0/lib -I /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0 -I /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/openvswitch-2.15.0 -I/usr/include -DNDEBUG -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -Wstrict-prototypes -Wall -Wextra -Wno-sign-compare -Wpointer-arith -Wformat -Wformat-security -Wswitch-enum -Wunused-parameter -Wbad-function-cast -Wcast-align -Wstrict-prototypes -Wold-style-definition -Wmissing-prototypes -Wmissing-field-initializers -fno-strict-aliasing -Wswitch-bool -Wlogical-not-parentheses -Wsizeof-array-argument -Wbool-compare -Wshift-negative-value -Wduplicated-cond -Wshadow -Wmultistatement-macros -Wcast-align=strict -fomit-frame-pointer -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/ovn-20.12.0=ovn-20.12.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto -std=gnu99 -MT lib/ovn-nb-idl.lo -MD -MP -MF lib/.deps/ovn-nb-idl.Tpo -c lib/ovn-nb-idl.c  -fPIC -DPIC -o lib/.libs/ovn-nb-idl.o
In file included from ../linux-ath79_generic/openvswitch-2.15.0/lib/ovsdb-data.h:19,
                 from ./lib/ovn-nb-idl.h:9,
                 from lib/ovn-nb-idl.c:4:
/usr/include/stdlib.h:152:8: error: '_Float128' is not supported on this target
 extern _Float128 strtof128 (const char *__restrict __nptr,
        ^~~~~~~~~
/usr/include/stdlib.h:164:8: error: '_Float64x' is not supported on this target
 extern _Float64x strtof64x (const char *__restrict __nptr,
        ^~~~~~~~~
/usr/include/stdlib.h:245:4: error: '_Float128' is not supported on this target
    _Float128 __f)
    ^~~~~~~~~
/usr/include/stdlib.h:257:4: error: '_Float64x' is not supported on this target
    _Float64x __f)
    ^~~~~~~~~
In file included from ../linux-ath79_generic/openvswitch-2.15.0/lib/ovsdb-data.h:19,
                 from ./lib/ovn-nb-idl.h:9,
                 from lib/ovn-nb-idl.c:4:
/usr/include/stdlib.h:330:8: error: '_Float128' is not supported on this target
 extern _Float128 strtof128_l (const char *__restrict __nptr,
        ^~~~~~~~~
/usr/include/stdlib.h:344:8: error: '_Float64x' is not supported on this target
 extern _Float64x strtof64x_l (const char *__restrict __nptr,
        ^~~~~~~~~
In file included from /usr/include/bits/local_lim.h:38,
                 from /usr/include/bits/posix1_lim.h:161,
                 from /usr/include/limits.h:183,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/usr/include/linux/limits.h:7: warning: "NGROUPS_MAX" redefined
 #define NGROUPS_MAX    65536 /* supplemental group IDs are available */
 
In file included from /usr/include/limits.h:124,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:46: note: this is the location of the previous definition
 #define NGROUPS_MAX 32
 
In file included from /usr/include/bits/posix1_lim.h:161,
                 from /usr/include/limits.h:183,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/usr/include/bits/local_lim.h:64: warning: "PTHREAD_KEYS_MAX" redefined
 #define PTHREAD_KEYS_MAX 1024
 
In file included from /usr/include/limits.h:124,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:58: note: this is the location of the previous definition
 #define PTHREAD_KEYS_MAX 128
 
In file included from /usr/include/bits/posix1_lim.h:161,
                 from /usr/include/limits.h:183,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/usr/include/bits/local_lim.h:69: warning: "PTHREAD_DESTRUCTOR_ITERATIONS" redefined
 #define PTHREAD_DESTRUCTOR_ITERATIONS _POSIX_THREAD_DESTRUCTOR_ITERATIONS
 
In file included from /usr/include/limits.h:124,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:60: note: this is the location of the previous definition
 #define PTHREAD_DESTRUCTOR_ITERATIONS 4
 
In file included from /usr/include/bits/posix1_lim.h:161,
                 from /usr/include/limits.h:183,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/usr/include/bits/local_lim.h:81: warning: "PTHREAD_STACK_MIN" redefined
 #define PTHREAD_STACK_MIN 16384
 
In file included from /usr/include/limits.h:124,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:59: note: this is the location of the previous definition
 #define PTHREAD_STACK_MIN 2048
 
In file included from /usr/include/bits/posix1_lim.h:161,
                 from /usr/include/limits.h:183,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/usr/include/bits/local_lim.h:84: warning: "DELAYTIMER_MAX" redefined
 #define DELAYTIMER_MAX 2147483647
 
In file included from /usr/include/limits.h:124,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:63: note: this is the location of the previous definition
 #define DELAYTIMER_MAX 0x7fffffff
 
In file included from /usr/include/bits/posix1_lim.h:161,
                 from /usr/include/limits.h:183,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/usr/include/bits/local_lim.h:93: warning: "HOST_NAME_MAX" redefined
 #define HOST_NAME_MAX  64
 
In file included from /usr/include/limits.h:124,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:54: note: this is the location of the previous definition
 #define HOST_NAME_MAX 255
 
In file included from /usr/include/bits/posix1_lim.h:161,
                 from /usr/include/limits.h:183,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/usr/include/bits/local_lim.h:99: warning: "SEM_VALUE_MAX" redefined
 #define SEM_VALUE_MAX   (2147483647)
 
In file included from /usr/include/limits.h:124,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:61: note: this is the location of the previous definition
 #define SEM_VALUE_MAX 0x7fffffff
 
In file included from /usr/include/limits.h:187,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/usr/include/bits/posix2_lim.h:88: warning: "RE_DUP_MAX" redefined
 #define RE_DUP_MAX (0x7fff)
 
In file included from /usr/include/limits.h:124,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:77: note: this is the location of the previous definition
 #define RE_DUP_MAX 255
 
In file included from /usr/include/limits.h:191,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/usr/include/bits/xopen_lim.h:62: warning: "_XOPEN_IOV_MAX" redefined
 #define _XOPEN_IOV_MAX _POSIX_UIO_MAXIOV
 
In file included from /usr/include/limits.h:124,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:154: note: this is the location of the previous definition
 #define _XOPEN_IOV_MAX          16
 
In file included from /usr/include/limits.h:191,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/usr/include/bits/xopen_lim.h:66: warning: "IOV_MAX" redefined
 # define IOV_MAX __IOV_MAX
 
In file included from /usr/include/limits.h:124,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:48: note: this is the location of the previous definition
 #define IOV_MAX 1024
 
In file included from /usr/include/limits.h:191,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/usr/include/bits/xopen_lim.h:73: warning: "NL_ARGMAX" redefined
 #define NL_ARGMAX _POSIX_ARG_MAX
 
In file included from /usr/include/limits.h:124,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:79: note: this is the location of the previous definition
 #define NL_ARGMAX 9
 
In file included from /usr/include/limits.h:191,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/usr/include/bits/xopen_lim.h:76: warning: "NL_LANGMAX" redefined
 #define NL_LANGMAX _POSIX2_LINE_MAX
 
In file included from /usr/include/limits.h:124,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:92: note: this is the location of the previous definition
 #define NL_LANGMAX 32
 
In file included from /usr/include/limits.h:191,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/usr/include/bits/xopen_lim.h:79: warning: "NL_MSGMAX" redefined
 #define NL_MSGMAX INT_MAX
 
In file included from /usr/include/limits.h:124,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:80: note: this is the location of the previous definition
 #define NL_MSGMAX 32767
 
In file included from /usr/include/limits.h:191,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/usr/include/bits/xopen_lim.h:84: warning: "NL_NMAX" redefined
 # define NL_NMAX INT_MAX
 
In file included from /usr/include/limits.h:124,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:99: note: this is the location of the previous definition
 #define NL_NMAX 16
 
In file included from /usr/include/limits.h:191,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/usr/include/bits/xopen_lim.h:88: warning: "NL_SETMAX" redefined
 #define NL_SETMAX INT_MAX
 
In file included from /usr/include/limits.h:124,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:81: note: this is the location of the previous definition
 #define NL_SETMAX 255
 
In file included from /usr/include/limits.h:191,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/usr/include/bits/xopen_lim.h:91: warning: "NL_TEXTMAX" redefined
 #define NL_TEXTMAX INT_MAX
 
In file included from /usr/include/limits.h:124,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:24,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/limits.h:82: note: this is the location of the previous definition
 #define NL_TEXTMAX 2048
 
In file included from ../linux-ath79_generic/openvswitch-2.15.0/lib/stdio.h:17,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:26,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/usr/include/stdio.h:52:9: error: unknown type name '__gnuc_va_list'
 typedef __gnuc_va_list va_list;
         ^~~~~~~~~~~~~~
/usr/include/stdio.h:52:24: error: conflicting types for 'va_list'
 typedef __gnuc_va_list va_list;
                        ^~~~~~~
In file included from /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/stdarg.h:10,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:25,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/bits/alltypes.h:6:27: note: previous declaration of 'va_list' was here
 typedef __builtin_va_list va_list;
                           ^~~~~~~
In file included from ../linux-ath79_generic/openvswitch-2.15.0/lib/stdio.h:17,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:26,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/usr/include/stdio.h:342:8: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
        __gnuc_va_list __arg);
        ^~~~~~~~~~~~~~
        va_list
/usr/include/stdio.h:347:54: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
 extern int vprintf (const char *__restrict __format, __gnuc_va_list __arg);
                                                      ^~~~~~~~~~~~~~
                                                      va_list
/usr/include/stdio.h:350:8: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
        __gnuc_va_list __arg) __THROWNL;
        ^~~~~~~~~~~~~~
        va_list
/usr/include/stdio.h:359:42: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
         const char *__restrict __format, __gnuc_va_list __arg)
                                          ^~~~~~~~~~~~~~
                                          va_list
/usr/include/stdio.h:367:9: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
         __gnuc_va_list __arg)
         ^~~~~~~~~~~~~~
         va_list
/usr/include/stdio.h:380:8: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
        __gnuc_va_list __arg)
        ^~~~~~~~~~~~~~
        va_list
/usr/include/stdio.h:433:7: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
       __gnuc_va_list __arg)
       ^~~~~~~~~~~~~~
       va_list
/usr/include/stdio.h:440:53: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
 extern int vscanf (const char *__restrict __format, __gnuc_va_list __arg)
                                                     ^~~~~~~~~~~~~~
                                                     va_list
/usr/include/stdio.h:445:40: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
       const char *__restrict __format, __gnuc_va_list __arg)
                                        ^~~~~~~~~~~~~~
                                        va_list
In file included from /usr/include/features.h:461,
                 from /usr/include/bits/libc-header-start.h:33,
                 from /usr/include/stdint.h:26,
                 from ./lib/ovn-nb-idl.h:8,
                 from lib/ovn-nb-idl.c:4:
/usr/include/stdio.h:453:37: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
    const char *__restrict __format, __gnuc_va_list __arg),
                                     ^~~~~~~~~~~~~~
/usr/include/sys/cdefs.h:174:46: note: in definition of macro '__REDIRECT'
 # define __REDIRECT(name, proto, alias) name proto __asm__ (__ASMNAME (#alias))
                                              ^~~~~
/usr/include/stdio.h:457:5: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
     __gnuc_va_list __arg), __isoc99_vscanf)
     ^~~~~~~~~~~~~~
/usr/include/sys/cdefs.h:174:46: note: in definition of macro '__REDIRECT'
 # define __REDIRECT(name, proto, alias) name proto __asm__ (__ASMNAME (#alias))
                                              ^~~~~
/usr/include/stdio.h:462:8: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
        __gnuc_va_list __arg), __isoc99_vsscanf)
        ^~~~~~~~~~~~~~
/usr/include/sys/cdefs.h:182:11: note: in definition of macro '__REDIRECT_NTH'
      name proto __asm__ (__ASMNAME (#alias)) __THROW
           ^~~~~
In file included from ../linux-ath79_generic/openvswitch-2.15.0/lib/stdio.h:17,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:26,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/usr/include/stdio.h:831:8: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
        __gnuc_va_list __args)
        ^~~~~~~~~~~~~~
        va_list
In file included from /usr/include/stdio.h:867,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/stdio.h:17,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:26,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/usr/include/bits/stdio2.h:30:7: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
       __gnuc_va_list __ap) __THROW;
       ^~~~~~~~~~~~~~
       va_list
In file included from /usr/include/features.h:461,
                 from /usr/include/bits/libc-header-start.h:33,
                 from /usr/include/stdint.h:26,
                 from ./lib/ovn-nb-idl.h:8,
                 from lib/ovn-nb-idl.c:4:
/usr/include/bits/stdio2.h:47:4: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
    __gnuc_va_list __ap))
    ^~~~~~~~~~~~~~
/usr/include/sys/cdefs.h:57:59: note: in definition of macro '__NTH'
 #  define __NTH(fct) __attribute__ ((__nothrow__ __LEAF)) fct
                                                           ^~~
In file included from /usr/include/stdio.h:867,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/stdio.h:17,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/util.h:26,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/hash.h:23,
                 from ../linux-ath79_generic/openvswitch-2.15.0/lib/smap.h:20,
                 from ./lib/ovn-nb-idl.h:11,
                 from lib/ovn-nb-idl.c:4:
/usr/include/bits/stdio2.h:60:8: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
        __gnuc_va_list __ap) __THROW;
        ^~~~~~~~~~~~~~
        va_list
In file included from /usr/include/features.h:461,
                 from /usr/include/bits/libc-header-start.h:33,
                 from /usr/include/stdint.h:26,
                 from ./lib/ovn-nb-idl.h:8,
                 from lib/ovn-nb-idl.c:4:
/usr/include/bits/stdio2.h:78:35: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
     const char *__restrict __fmt, __gnuc_va_list __ap))
                                   ^~~~~~~~~~~~~~
/usr/include/sys/cdefs.h:57:59: note: in definition of macro '__NTH'
 #  define __NTH(fct) __attribute__ ((__nothrow__ __LEAF)) fct
                                                           ^~~
In file included from ../linux-ath79_generic/openvswitch-2.15.0/lib/ovs-thread.h:20,
                 from lib/ovn-nb-idl.c:6:
/usr/include/pthread.h:657:6: warning: 'regparm' attribute directive ignored [-Wattributes]
      __cleanup_fct_attribute;
      ^~~~~~~~~~~~~~~~~~~~~~~
/usr/include/pthread.h:669:3: warning: 'regparm' attribute directive ignored [-Wattributes]
   __cleanup_fct_attribute;
   ^~~~~~~~~~~~~~~~~~~~~~~
/usr/include/pthread.h:692:6: warning: 'regparm' attribute directive ignored [-Wattributes]
      __cleanup_fct_attribute;
      ^~~~~~~~~~~~~~~~~~~~~~~
/usr/include/pthread.h:705:3: warning: 'regparm' attribute directive ignored [-Wattributes]
   __cleanup_fct_attribute;
   ^~~~~~~~~~~~~~~~~~~~~~~
/usr/include/pthread.h:714:6: warning: 'regparm' attribute directive ignored [-Wattributes]
      ;
      ^
make[5]: *** [Makefile:1711: lib/ovn-nb-idl.lo] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/ovn-20.12.0'
make[4]: *** [Makefile:1026: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/ovn-20.12.0'
make[3]: *** [Makefile:96: /openwrt/build_dir/target-mips_24kc_musl/ovn-20.12.0/.built] Error 2
```
