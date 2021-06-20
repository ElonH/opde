---
title: "compile.37"
date: 2021-06-20 22:36:26.330939
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
make package/feeds/packages/radsecproxy/compile -j$(nproc) || make package/feeds/packages/radsecproxy/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/200-logdest-on-foreground.patch using plaintext: 
patching file radsecproxy.c

Applying ./patches/300-gcc10.patch using plaintext: 
patching file radsecproxy.c
patching file radsecproxy.h
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force 
autoreconf: configure.ac: tracing
autoreconf: configure.ac: not using Libtool
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: configure.ac: not using Autoheader
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
autoreconf: Leaving directory `.'
configure: WARNING: unrecognized options: --disable-nls
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
checking for style of include used by make... GNU
checking dependency style of ccache_cc... gcc3
checking for mips-openwrt-linux-ranlib... mips-openwrt-linux-musl-gcc-ranlib
checking for mallopt... no
checking for nettle_sha256_init in -lnettle... yes
UDP transport enabled
TCP transport enabled
TLS (RadSec) transport enabled
DTLS transport enabled
checking for OpenSSL... yes
OpenSSL found in /usr
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating radsecproxy.1
config.status: creating radsecproxy.conf.5
config.status: creating Makefile
config.status: creating tests/Makefile
config.status: executing depfiles commands
configure: WARNING: unrecognized options: --disable-nls
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/radsecproxy-1.8.1'
Making all in tests
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/radsecproxy-1.8.1/tests'
make[5]: Nothing to be done for 'all'.
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/radsecproxy-1.8.1/tests'
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/radsecproxy-1.8.1'
ccache_cc -DPACKAGE_NAME=\"radsecproxy\" -DPACKAGE_TARNAME=\"radsecproxy\" -DPACKAGE_VERSION=\"1.8.1\" -DPACKAGE_STRING=\"radsecproxy\ 1.8.1\" -DPACKAGE_BUGREPORT=\"https://radsecproxy.github.io\" -DPACKAGE_URL=\"\" -DPACKAGE=\"radsecproxy\" -DVERSION=\"1.8.1\" -DHAVE_LIBNETTLE=1 -DUSE_OPENSSL=1 -I.  -DSYSCONFDIR=\"/etc\" -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -g -Wall -Werror -fno-strict-aliasing -I/usr/include -I/usr/include/openssl -Wall -pedantic -Wno-long-long -pthread -DRADPROT_UDP -DRADPROT_TCP -DRADPROT_TLS -DRADPROT_DTLS -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/radsecproxy-1.8.1=radsecproxy-1.8.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -MT debug.o -MD -MP -MF .deps/debug.Tpo -c -o debug.o debug.c
In file included from debug.c:10:
../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/unistd.h:43:29: error: redefinition of 'confstr'
 _FORTIFY_FN(confstr) size_t confstr(int __n, char *__s, size_t __l)
                             ^~~~~~~
In file included from /usr/include/features.h:461,
                 from /usr/include/bits/libc-header-start.h:33,
                 from /usr/include/stdint.h:26,
                 from debug.c:6:
/usr/include/bits/unistd.h:240:8: note: previous definition of 'confstr' was here
 __NTH (confstr (int __name, char *__buf, size_t __len))
        ^~~~~~~
/usr/include/sys/cdefs.h:57:59: note: in definition of macro '__NTH'
 #  define __NTH(fct) __attribute__ ((__nothrow__ __LEAF)) fct
                                                           ^~~
In file included from debug.c:10:
../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/unistd.h:53:27: error: redefinition of 'getcwd'
 _FORTIFY_FN(getcwd) char *getcwd(char *__s, size_t __l)
                           ^~~~~~
In file included from /usr/include/features.h:461,
                 from /usr/include/bits/libc-header-start.h:33,
                 from /usr/include/stdint.h:26,
                 from debug.c:6:
/usr/include/bits/unistd.h:200:8: note: previous definition of 'getcwd' was here
 __NTH (getcwd (char *__buf, size_t __size))
        ^~~~~~
/usr/include/sys/cdefs.h:57:59: note: in definition of macro '__NTH'
 #  define __NTH(fct) __attribute__ ((__nothrow__ __LEAF)) fct
                                                           ^~~
In file included from debug.c:10:
../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/unistd.h:74:28: error: redefinition of 'getgroups'
 _FORTIFY_FN(getgroups) int getgroups(int __l, gid_t *__s)
                            ^~~~~~~~~
In file included from /usr/include/features.h:461,
                 from /usr/include/bits/libc-header-start.h:33,
                 from /usr/include/stdint.h:26,
                 from debug.c:6:
/usr/include/bits/unistd.h:265:8: note: previous definition of 'getgroups' was here
 __NTH (getgroups (int __size, __gid_t __list[]))
        ^~~~~~~~~
/usr/include/sys/cdefs.h:57:59: note: in definition of macro '__NTH'
 #  define __NTH(fct) __attribute__ ((__nothrow__ __LEAF)) fct
                                                           ^~~
In file included from debug.c:10:
../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/unistd.h:83:30: error: redefinition of 'gethostname'
 _FORTIFY_FN(gethostname) int gethostname(char *__s, size_t __l)
                              ^~~~~~~~~~~
In file included from /usr/include/features.h:461,
                 from /usr/include/bits/libc-header-start.h:33,
                 from /usr/include/stdint.h:26,
                 from debug.c:6:
/usr/include/bits/unistd.h:344:8: note: previous definition of 'gethostname' was here
 __NTH (gethostname (char *__buf, size_t __buflen))
        ^~~~~~~~~~~
/usr/include/sys/cdefs.h:57:59: note: in definition of macro '__NTH'
 #  define __NTH(fct) __attribute__ ((__nothrow__ __LEAF)) fct
                                                           ^~~
In file included from debug.c:10:
../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/unistd.h:92:29: error: redefinition of 'getlogin_r'
 _FORTIFY_FN(getlogin_r) int getlogin_r(char *__s, size_t __l)
                             ^~~~~~~~~~
In file included from /usr/include/unistd.h:1166,
                 from ../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/unistd.h:22,
                 from debug.c:10:
/usr/include/bits/unistd.h:317:1: note: previous definition of 'getlogin_r' was here
 getlogin_r (char *__buf, size_t __buflen)
 ^~~~~~~~~~
In file included from debug.c:10:
../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/unistd.h:110:27: error: redefinition of 'read'
 _FORTIFY_FN(read) ssize_t read(int __f, void *__s, size_t __n)
                           ^~~~
In file included from /usr/include/unistd.h:1166,
                 from ../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/unistd.h:22,
                 from debug.c:10:
/usr/include/bits/unistd.h:34:1: note: previous definition of 'read' was here
 read (int __fd, void *__buf, size_t __nbytes)
 ^~~~
In file included from debug.c:10:
../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/unistd.h:119:31: error: redefinition of 'readlink'
 _FORTIFY_FN(readlink) ssize_t readlink(const char *__p, char *__s, size_t __n)
                               ^~~~~~~~
In file included from /usr/include/features.h:461,
                 from /usr/include/bits/libc-header-start.h:33,
                 from /usr/include/stdint.h:26,
                 from debug.c:6:
/usr/include/bits/unistd.h:139:8: note: previous definition of 'readlink' was here
 __NTH (readlink (const char *__restrict __path, char *__restrict __buf,
        ^~~~~~~~
/usr/include/sys/cdefs.h:57:59: note: in definition of macro '__NTH'
 #  define __NTH(fct) __attribute__ ((__nothrow__ __LEAF)) fct
                                                           ^~~
In file included from debug.c:10:
../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/unistd.h:128:33: error: redefinition of 'readlinkat'
 _FORTIFY_FN(readlinkat) ssize_t readlinkat(int __f, const char *__p, char *__s, size_t __n)
                                 ^~~~~~~~~~
In file included from /usr/include/features.h:461,
                 from /usr/include/bits/libc-header-start.h:33,
                 from /usr/include/stdint.h:26,
                 from debug.c:6:
/usr/include/bits/unistd.h:173:8: note: previous definition of 'readlinkat' was here
 __NTH (readlinkat (int __fd, const char *__restrict __path,
        ^~~~~~~~~~
/usr/include/sys/cdefs.h:57:59: note: in definition of macro '__NTH'
 #  define __NTH(fct) __attribute__ ((__nothrow__ __LEAF)) fct
                                                           ^~~
In file included from debug.c:10:
../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/unistd.h:137:28: error: redefinition of 'ttyname_r'
 _FORTIFY_FN(ttyname_r) int ttyname_r(int __f, char *__s, size_t __n)
                            ^~~~~~~~~
In file included from /usr/include/features.h:461,
                 from /usr/include/bits/libc-header-start.h:33,
                 from /usr/include/stdint.h:26,
                 from debug.c:6:
/usr/include/bits/unistd.h:291:8: note: previous definition of 'ttyname_r' was here
 __NTH (ttyname_r (int __fd, char *__buf, size_t __buflen))
        ^~~~~~~~~
/usr/include/sys/cdefs.h:57:59: note: in definition of macro '__NTH'
 #  define __NTH(fct) __attribute__ ((__nothrow__ __LEAF)) fct
                                                           ^~~
In file included from ../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:22,
                 from debug.c:12:
/usr/include/stdio.h:52:9: error: unknown type name '__gnuc_va_list'
 typedef __gnuc_va_list va_list;
         ^~~~~~~~~~~~~~
/usr/include/stdio.h:52:24: error: conflicting types for 'va_list'
 typedef __gnuc_va_list va_list;
                        ^~~~~~~
In file included from /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/stdarg.h:10,
                 from /usr/include/stdio.h:36,
                 from ../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:22,
                 from debug.c:12:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/bits/alltypes.h:6:27: note: previous declaration of 'va_list' was here
 typedef __builtin_va_list va_list;
                           ^~~~~~~
In file included from ../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:22,
                 from debug.c:12:
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
                 from /usr/include/stdint.h:26,
                 from debug.c:6:
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
                 from ../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:22,
                 from debug.c:12:
/usr/include/bits/stdio2.h:30:7: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
       __gnuc_va_list __ap) __THROW;
       ^~~~~~~~~~~~~~
       va_list
In file included from /usr/include/features.h:461,
                 from /usr/include/bits/libc-header-start.h:33,
                 from /usr/include/stdint.h:26,
                 from debug.c:6:
/usr/include/bits/stdio2.h:47:4: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
    __gnuc_va_list __ap))
    ^~~~~~~~~~~~~~
/usr/include/sys/cdefs.h:57:59: note: in definition of macro '__NTH'
 #  define __NTH(fct) __attribute__ ((__nothrow__ __LEAF)) fct
                                                           ^~~
In file included from /usr/include/stdio.h:867,
                 from ../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:22,
                 from debug.c:12:
/usr/include/bits/stdio2.h:60:8: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
        __gnuc_va_list __ap) __THROW;
        ^~~~~~~~~~~~~~
        va_list
In file included from /usr/include/features.h:461,
                 from /usr/include/bits/libc-header-start.h:33,
                 from /usr/include/stdint.h:26,
                 from debug.c:6:
/usr/include/bits/stdio2.h:78:35: error: unknown type name '__gnuc_va_list'; did you mean 'va_list'?
     const char *__restrict __fmt, __gnuc_va_list __ap))
                                   ^~~~~~~~~~~~~~
/usr/include/sys/cdefs.h:57:59: note: in definition of macro '__NTH'
 #  define __NTH(fct) __attribute__ ((__nothrow__ __LEAF)) fct
                                                           ^~~
In file included from debug.c:12:
../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:39:26: error: redefinition of 'fgets'
 _FORTIFY_FN(fgets) char *fgets(char *__s, int __n, FILE *__f)
                          ^~~~~
In file included from /usr/include/stdio.h:867,
                 from ../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:22,
                 from debug.c:12:
/usr/include/bits/stdio2.h:255:1: note: previous definition of 'fgets' was here
 fgets (char *__restrict __s, int __n, FILE *__restrict __stream)
 ^~~~~
In file included from debug.c:12:
../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:48:27: error: redefinition of 'fread'
 _FORTIFY_FN(fread) size_t fread(void *__d, size_t __n, size_t __m, FILE *__f)
                           ^~~~~
In file included from /usr/include/stdio.h:867,
                 from ../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:22,
                 from debug.c:12:
/usr/include/bits/stdio2.h:284:1: note: previous definition of 'fread' was here
 fread (void *__restrict __ptr, size_t __size, size_t __n,
 ^~~~~
In file included from ../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/unistd.h:25,
                 from debug.c:10:
../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:70:13: error: 'vsnprintf' undeclared here (not in a function); did you mean 'snprintf'?
 _FORTIFY_FN(vsnprintf) int vsnprintf(char *__s, size_t __n, const char *__f,
             ^~~~~~~~~
../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/fortify-headers.h:20:40: note: in definition of macro '_FORTIFY_ORIG'
 #define _FORTIFY_ORIG(p,fn) __typeof__(fn) __orig_##fn __asm__(_FORTIFY_STR(p) #fn)
                                        ^~
../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:70:1: note: in expansion of macro '_FORTIFY_FN'
 _FORTIFY_FN(vsnprintf) int vsnprintf(char *__s, size_t __n, const char *__f,
 ^~~~~~~~~~~
../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:72: confused by earlier errors, bailing out
make[5]: *** [Makefile:623: debug.o] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/radsecproxy-1.8.1'
make[4]: *** [Makefile:729: all-recursive] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/radsecproxy-1.8.1'
make[3]: *** [Makefile:60: /openwrt/build_dir/target-mips_24kc_musl/radsecproxy-1.8.1/.built] Error 2
```
