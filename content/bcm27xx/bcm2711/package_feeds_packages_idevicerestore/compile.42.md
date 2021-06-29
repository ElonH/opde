---
title: "compile.42"
date: 2021-06-29 09:28:26.551148
hidden: false
draft: false
weight: -42
---

build number: `42`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/idevicerestore/compile -j$(nproc) || make package/feeds/packages/idevicerestore/compile V=s
```

#### Compile.txt

``` bash
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/aarch64
checking build system type... x86_64-pc-linux-gnu
checking host system type... aarch64-openwrt-linux-gnu
checking target system type... aarch64-openwrt-linux-gnu
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for aarch64-openwrt-linux-strip... aarch64-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether make supports nested variables... (cached) yes
checking for aarch64-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
checking whether ccache_cc understands -c and -o together... yes
checking whether make supports the include directive... yes (GNU style)
checking dependency style of ccache_cc... gcc3
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache_cc... aarch64-openwrt-linux-musl-ld
checking if the linker (aarch64-openwrt-linux-musl-ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... aarch64-openwrt-linux-musl-gcc-nm
checking the name lister (aarch64-openwrt-linux-musl-gcc-nm) interface... BSD nm
checking whether ln -s works... yes
checking the maximum length of command line arguments... 3145728
checking how to convert x86_64-pc-linux-gnu file names to aarch64-openwrt-linux-gnu format... func_convert_file_noop
checking how to convert x86_64-pc-linux-gnu file names to toolchain format... func_convert_file_noop
checking for aarch64-openwrt-linux-musl-ld option to reload object files... -r
checking for aarch64-openwrt-linux-objdump... aarch64-openwrt-linux-musl-objdump
checking how to recognize dependent libraries... pass_all
checking for aarch64-openwrt-linux-dlltool... no
checking for dlltool... no
checking how to associate runtime and link libraries... printf %s\n
checking for aarch64-openwrt-linux-ar... aarch64-openwrt-linux-musl-gcc-ar
checking for archiver @FILE support... @
checking for aarch64-openwrt-linux-strip... (cached) aarch64-openwrt-linux-musl-strip
checking for aarch64-openwrt-linux-ranlib... aarch64-openwrt-linux-musl-gcc-ranlib
checking command to parse aarch64-openwrt-linux-musl-gcc-nm output from ccache_cc object... ok
checking for sysroot... no
checking for a working dd... /usr/bin/dd
checking how to truncate binary pipes... /usr/bin/dd bs=4096 count=1
checking for aarch64-openwrt-linux-mt... no
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
checking whether the ccache_cc linker (aarch64-openwrt-linux-musl-ld) supports shared libraries... yes
checking whether -lc should be explicitly linked in... no
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... yes
checking pkg-config is at least version 0.9.0... yes
checking for libirecovery... yes
checking for libimobiledevice... yes
checking for libplist... yes
checking for libzip... yes
checking for libcurl... yes
checking for zlib... yes
checking for openssl... yes
checking whether we need platform-specific build settings... yes
checking whether ccache_cc is Clang... no
checking whether pthreads work with -pthread... yes
checking for joinable pthread attribute... PTHREAD_CREATE_JOINABLE
checking whether more special flags are required for pthreads... no
checking for PTHREAD_PRIO_INHERIT... yes
checking for strsep... yes
checking for strcspn... yes
checking for mkstemp... yes
checking for realpath... yes
checking for IDEVICE_E_TIMEOUT in enum idevice_error_t... yes
checking for RESTORE_E_RECEIVE_TIMEOUT in enum restored_error_t... yes
checking for enum idevice_connection_type... yes
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking whether make supports nested variables... (cached) yes
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating Makefile
config.status: creating src/Makefile
config.status: creating docs/Makefile
config.status: creating config.h
config.status: executing depfiles commands
config.status: executing libtool commands
configure: WARNING: unrecognized options: --disable-nls

Configuration for idevicerestore 1.0.0:
-------------------------------------------

  Install prefix: .........: /usr

  Now type 'make' to build idevicerestore 1.0.0,
  and then 'make install' for installation.

make[4]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/idevicerestore-1.0.0'
make  all-recursive
make[5]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/idevicerestore-1.0.0'
Making all in src
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/idevicerestore-1.0.0/src'
  CC       idevicerestore-idevicerestore.o
In file included from ../../../../staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify/stdio.h:22,
                 from idevicerestore.c:28:
/usr/include/stdio.h:52:9: error: unknown type name '__gnuc_va_list'
 typedef __gnuc_va_list va_list;
         ^~~~~~~~~~~~~~
/usr/include/stdio.h:52:24: error: conflicting types for 'va_list'
 typedef __gnuc_va_list va_list;
                        ^~~~~~~
In file included from /openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/stdarg.h:10,
                 from /usr/include/stdio.h:36,
                 from ../../../../staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify/stdio.h:22,
                 from idevicerestore.c:28:
/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/bits/alltypes.h:6:27: note: previous declaration of 'va_list' was here
 typedef __builtin_va_list va_list;
                           ^~~~~~~
In file included from ../../../../staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify/stdio.h:22,
                 from idevicerestore.c:28:
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
                 from /usr/include/stdio.h:27,
                 from ../../../../staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify/stdio.h:22,
                 from idevicerestore.c:28:
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
In file included from /usr/include/stdio.h:867,
                 from ../../../../staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify/stdio.h:22,
                 from idevicerestore.c:28:
/usr/include/bits/stdio2.h:30:7: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
       __gnuc_va_list __ap) __THROW;
       ^~~~~~~~~~~~~~
       va_list
In file included from /usr/include/features.h:461,
                 from /usr/include/bits/libc-header-start.h:33,
                 from /usr/include/stdio.h:27,
                 from ../../../../staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify/stdio.h:22,
                 from idevicerestore.c:28:
/usr/include/bits/stdio2.h:47:4: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
    __gnuc_va_list __ap))
    ^~~~~~~~~~~~~~
/usr/include/sys/cdefs.h:57:59: note: in definition of macro '__NTH'
 #  define __NTH(fct) __attribute__ ((__nothrow__ __LEAF)) fct
                                                           ^~~
In file included from /usr/include/stdio.h:867,
                 from ../../../../staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify/stdio.h:22,
                 from idevicerestore.c:28:
/usr/include/bits/stdio2.h:60:8: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
        __gnuc_va_list __ap) __THROW;
        ^~~~~~~~~~~~~~
        va_list
In file included from /usr/include/features.h:461,
                 from /usr/include/bits/libc-header-start.h:33,
                 from /usr/include/stdio.h:27,
                 from ../../../../staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify/stdio.h:22,
                 from idevicerestore.c:28:
/usr/include/bits/stdio2.h:78:35: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
     const char *__restrict __fmt, __gnuc_va_list __ap))
                                   ^~~~~~~~~~~~~~
/usr/include/sys/cdefs.h:57:59: note: in definition of macro '__NTH'
 #  define __NTH(fct) __attribute__ ((__nothrow__ __LEAF)) fct
                                                           ^~~
In file included from idevicerestore.c:28:
../../../../staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify/stdio.h:39:26: error: redefinition of 'fgets'
 _FORTIFY_FN(fgets) char *fgets(char *__s, int __n, FILE *__f)
                          ^~~~~
In file included from /usr/include/stdio.h:867,
                 from ../../../../staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify/stdio.h:22,
                 from idevicerestore.c:28:
/usr/include/bits/stdio2.h:255:1: note: previous definition of 'fgets' was here
 fgets (char *__restrict __s, int __n, FILE *__restrict __stream)
 ^~~~~
In file included from idevicerestore.c:28:
../../../../staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify/stdio.h:48:27: error: redefinition of 'fread'
 _FORTIFY_FN(fread) size_t fread(void *__d, size_t __n, size_t __m, FILE *__f)
                           ^~~~~
In file included from /usr/include/stdio.h:867,
                 from ../../../../staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify/stdio.h:22,
                 from idevicerestore.c:28:
/usr/include/bits/stdio2.h:284:1: note: previous definition of 'fread' was here
 fread (void *__restrict __ptr, size_t __size, size_t __n,
 ^~~~~
In file included from ../../../../staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify/stdio.h:25,
                 from idevicerestore.c:28:
../../../../staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify/stdio.h:70:13: error: 'vsnprintf' undeclared here (not in a function); did you mean 'snprintf'?
 _FORTIFY_FN(vsnprintf) int vsnprintf(char *__s, size_t __n, const char *__f,
             ^~~~~~~~~
../../../../staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify/fortify-headers.h:20:40: note: in definition of macro '_FORTIFY_ORIG'
 #define _FORTIFY_ORIG(p,fn) __typeof__(fn) __orig_##fn __asm__(_FORTIFY_STR(p) #fn)
                                        ^~
../../../../staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify/stdio.h:70:1: note: in expansion of macro '_FORTIFY_FN'
 _FORTIFY_FN(vsnprintf) int vsnprintf(char *__s, size_t __n, const char *__f,
 ^~~~~~~~~~~
../../../../staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify/stdio.h:72: confused by earlier errors, bailing out
make[6]: *** [Makefile:556: idevicerestore-idevicerestore.o] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/idevicerestore-1.0.0/src'
make[5]: *** [Makefile:434: all-recursive] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/idevicerestore-1.0.0'
make[4]: *** [Makefile:366: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/idevicerestore-1.0.0'
make[3]: *** [Makefile:50: /openwrt/build_dir/target-aarch64_cortex-a72_musl/idevicerestore-1.0.0/.built] Error 2
```
