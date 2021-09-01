---
title: "compile.45"
date: 2021-09-01 09:25:00.624508
hidden: false
draft: false
weight: -45
---

build number: `45`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/glib2/compile -j$(nproc) || make package/feeds/packages/glib2/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/003-valgrind.h-mips16-fix.patch using plaintext: 
patching file glib/valgrind.h

Applying ./patches/004-no-distutils.patch using plaintext: 
patching file meson.build

Applying ./patches/005-uclibc.patch using plaintext: 
patching file meson.build

Applying ./patches/006-c99.patch using plaintext: 
patching file meson.build
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-x86_64_musl/glib-2.68.4
Build dir: /openwrt/build_dir/target-x86_64_musl/glib-2.68.4/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: glib
Project version: 2.68.4
C compiler for the host machine: ccache_cc (gcc 8.4.0 "x86_64-openwrt-linux-musl-gcc (OpenWrt GCC 8.4.0 r0-009c172) 8.4.0")
C linker for the host machine: ccache_cc ld.bfd 2.36.1
C++ compiler for the host machine: ccache_cxx (gcc 8.4.0 "x86_64-openwrt-linux-musl-g++ (OpenWrt GCC 8.4.0 r0-009c172) 8.4.0")
C++ linker for the host machine: ccache_cxx ld.bfd 2.36.1
C compiler for the build machine: ccache gcc (gcc 9.3.0 "gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0")
C linker for the build machine: gcc ld.bfd 2.34
C++ compiler for the build machine: ccache g++ (gcc 9.3.0 "g++ (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0")
C++ linker for the build machine: g++ ld.bfd 2.34
Build machine cpu family: x86_64
Build machine cpu: x86_64
Host machine cpu family: x86_64
Host machine cpu: generic
Target machine cpu family: x86_64
Target machine cpu: generic
Compiler for C supports arguments -fno-strict-aliasing: YES 
Checking if "GNU C visibility attributes test" compiles: YES 
Compiler for C supports arguments -fvisibility=hidden: YES 
Message: Disabling GLib asserts
Message: Disabling GLib checks
Has header "alloca.h" : YES 
Has header "crt_externs.h" : NO 
Has header "dirent.h" : YES 
Has header "float.h" : YES 
Has header "fstab.h" : NO 
Has header "grp.h" : YES 
Has header "inttypes.h" : YES 
Has header "limits.h" : YES 
Has header "linux/magic.h" : YES 
Has header "locale.h" : YES 
Has header "mach/mach_time.h" : NO 
Has header "memory.h" : YES 
Has header "mntent.h" : YES 
Has header "poll.h" : YES 
Has header "pwd.h" : YES 
Has header "sched.h" : YES 
Has header "spawn.h" : YES 
Has header "stdatomic.h" : YES 
Has header "stdint.h" : YES 
Has header "stdlib.h" : YES 
Has header "string.h" : YES 
Has header "strings.h" : YES 
Has header "sys/auxv.h" : YES 
Has header "sys/event.h" : NO 
Has header "sys/filio.h" : NO 
Has header "sys/inotify.h" : YES 
Has header "sys/mkdev.h" : NO 
Has header "sys/mntctl.h" : NO 
Has header "sys/mnttab.h" : NO 
Has header "sys/mount.h" : YES 
Has header "sys/param.h" : YES 
Has header "sys/resource.h" : YES 
Has header "sys/select.h" : YES 
Has header "sys/statfs.h" : YES 
Has header "sys/stat.h" : YES 
Has header "sys/statvfs.h" : YES 
Has header "sys/sysctl.h" : NO 
Has header "sys/time.h" : YES 
Has header "sys/times.h" : YES 
Has header "sys/types.h" : YES 
Has header "sys/uio.h" : YES 
Has header "sys/vfs.h" : YES 
Has header "sys/vfstab.h" : NO 
Has header "sys/vmount.h" : NO 
Has header "sys/wait.h" : YES 
Has header "termios.h" : YES 
Has header "unistd.h" : YES 
Has header "values.h" : YES 
Has header "wchar.h" : YES 
Has header "xlocale.h" : NO 
Checking if "malloc.h" compiles: YES 
Has header "linux/netlink.h" : YES 
Checking if "statx() test" compiles: NO 
Header <locale.h> has symbol "LC_MESSAGES" : YES 
Checking whether type "struct stat" has member "st_mtimensec" : NO 
Checking whether type "struct stat" has member "st_mtim.tv_nsec" : YES 
Checking whether type "struct stat" has member "st_atimensec" : NO 
Checking whether type "struct stat" has member "st_atim.tv_nsec" : YES 
Checking whether type "struct stat" has member "st_ctimensec" : NO 
Checking whether type "struct stat" has member "st_ctim.tv_nsec" : YES 
Checking whether type "struct stat" has member "st_birthtime" : NO 
Checking whether type "struct stat" has member "st_birthtimensec" : NO 
Checking whether type "struct stat" has member "st_birthtim" : NO 
Checking whether type "struct stat" has member "st_birthtim.tv_nsec" : NO 
Checking whether type "struct stat" has member "st_blksize" : YES 
Checking whether type "struct stat" has member "st_blocks" : YES 
Checking whether type "struct statfs" has member "f_fstypename" : NO 
Checking whether type "struct statfs" has member "f_bavail" : YES 
Checking whether type "struct dirent" has member "d_type" : YES 
Checking whether type "struct statvfs" has member "f_basetype" : NO 
Checking whether type "struct statvfs" has member "f_fstypename" : NO 
Checking whether type "struct tm" has member "tm_gmtoff" : YES 
Checking whether type "struct tm" has member "__tm_gmtoff" : YES 
Compiler for C supports arguments -Wduplicated-branches: YES 
Compiler for C supports arguments -Wimplicit-fallthrough: YES 
Compiler for C supports arguments -Wmisleading-indentation: YES 
Compiler for C supports arguments -Wstrict-prototypes: YES 
Compiler for C supports arguments -Wunused: YES 
Compiler for C supports arguments -Wno-unused-parameter: YES 
Compiler for C supports arguments -Wno-bad-function-cast: YES 
Compiler for C supports arguments -Wno-cast-function-type: YES 
Compiler for C supports arguments -Wno-pedantic: YES 
Compiler for C supports arguments -Wno-format-zero-length: YES 
Compiler for C supports arguments -Werror=declaration-after-statement: YES 
Compiler for C supports arguments -Werror=format=2: YES 
Compiler for C supports arguments -Werror=implicit-function-declaration: YES 
Compiler for C supports arguments -Werror=init-self: YES 
Compiler for C supports arguments -Werror=missing-include-dirs: YES 
Compiler for C supports arguments -Werror=missing-prototypes: YES 
Compiler for C supports arguments -Werror=pointer-arith: YES 
Compiler for C supports link arguments -Wl,-z,nodelete: YES 
Compiler for C supports link arguments -Wl,-Bsymbolic-functions: YES 
Checking for function "close_range" : NO 
Checking for function "endmntent" : YES 
Checking for function "endservent" : YES 
Checking for function "epoll_create" : YES 
Checking for function "fallocate" : YES 
Checking for function "fchmod" : YES 
Checking for function "fchown" : YES 
Checking for function "fdwalk" : NO 
Checking for function "fsync" : YES 
Checking for function "getauxval" : YES 
Checking for function "getc_unlocked" : YES 
Checking for function "getfsstat" : NO 
Checking for function "getgrgid_r" : YES 
Checking for function "getmntent_r" : YES 
Checking for function "getpwuid_r" : YES 
Checking for function "getresuid" : YES 
Checking for function "getvfsstat" : NO 
Checking for function "gmtime_r" : YES 
Checking for function "hasmntopt" : YES 
Checking for function "inotify_init1" : YES 
Checking for function "issetugid" : YES 
Checking for function "kevent" : NO 
Checking for function "kqueue" : NO 
Checking for function "lchmod" : YES 
Checking for function "lchown" : YES 
Checking for function "link" : YES 
Checking for function "localtime_r" : YES 
Checking for function "lstat" : YES 
Checking for function "mbrtowc" : YES 
Checking for function "memalign" : YES 
Checking for function "mmap" : YES 
Checking for function "newlocale" : YES 
Checking for function "pipe2" : YES 
Checking for function "poll" : YES 
Checking for function "prlimit" : YES 
Checking for function "readlink" : YES 
Checking for function "recvmmsg" : YES 
Checking for function "sendmmsg" : YES 
Checking for function "setenv" : YES 
Checking for function "setmntent" : YES 
Checking for function "strerror_r" : YES 
Checking for function "strnlen" : YES 
Checking for function "strsignal" : YES 
Checking for function "strtod_l" : YES 
Checking for function "strtoll_l" : NO 
Checking for function "strtoull_l" : NO 
Checking for function "symlink" : YES 
Checking for function "timegm" : YES 
Checking for function "unsetenv" : YES 
Checking for function "uselocale" : YES 
Checking for function "utimes" : YES 
Checking for function "valloc" : YES 
Checking for function "vasprintf" : YES 
Checking for function "vsnprintf" : YES 
Checking for function "wcrtomb" : YES 
Checking for function "wcslen" : YES 
Checking for function "wcsnlen" : YES 
Checking for function "sysctlbyname" : NO 
Checking for function "statvfs" : YES 
Checking for function "statfs" : YES 
Checking for function "if_indextoname" : YES 
Checking for function "if_nametoindex" : YES 
Checking for function "splice" : YES 
Checking for function "stpcpy" : YES 
Checking for function "posix_memalign" : YES 
Checking for function "posix_spawn" : YES 
Checking if "strerror_r() returns char *" compiles: NO 
Checking for function "snprintf" : YES 
Checking for function "strcasecmp" : YES 
Checking for function "strncasecmp" : YES 
Header <sys/sysmacros.h> has symbol "major" : YES 
Header <dlfcn.h> has symbol "RTLD_LAZY" : YES 
Header <dlfcn.h> has symbol "RTLD_NOW" : YES 
Header <dlfcn.h> has symbol "RTLD_GLOBAL" : YES 
Header <dlfcn.h> has symbol "RTLD_NEXT" : YES 
Message: Checking whether to use statfs or statvfs .. statfs
Checking for function "mkostemp" : YES 
Checking if "futex(2) system call" links: YES 
Checking if "eventfd(2) system call" links: YES 
Checking if "__uint128_t available" compiles: YES 
Checking if "clock_gettime" links: YES 
Checking if "dlopen() and dlsym() in system libraries" links: YES 
Checking if "number of arguments to statfs() (n=2)" compiles: YES 
Checking if "open() option O_DIRECTORY" compiles: YES 
Checking if "fcntl() option F_FULLFSYNC" compiles: NO 
Checking if "nl_langinfo and CODESET" links: YES 
Checking if "nl_langinfo (PM_STR)" links: YES 
Checking if "nl_langinfo (_NL_CTYPE_OUTDIGITn_MB)" links: NO 
Checking if "nl_langinfo (ALTMON_n)" links: NO 
Checking if "nl_langinfo (_NL_ABALTMON_n)" links: NO 
Checking if "signed" compiles: YES 
Header <stddef.h> has symbol "ptrdiff_t" : YES 
Checking if "sig_atomic_t" links: YES 
Checking if "long long" compiles: YES 
Checking if "long double" compiles: YES 
Header <stddef.h> has symbol "wchar_t" : YES 
Header <wchar.h> has symbol "wint_t" : YES 
Checking if "uintmax_t in inttypes.h" compiles: YES 
Checking if "uintmax_t in stdint.h" compiles: YES 
Checking for size of "char" : 1
Checking for size of "short" : 2
Checking for size of "int" : 4
Checking for size of "void*" : 8
Checking for size of "long" : 8
Checking for size of "long long" : 8
Checking for size of "size_t" : 8
Checking for size of "ssize_t" : 8
Checking if "int64_t is long" compiles: YES 
Checking for alignment of "char" : 1
Checking for alignment of "short" : 2
Checking for alignment of "int" : 4
Checking for alignment of "void*" : 8
Checking for alignment of "long" : 8
Checking for alignment of "long long" : 8
Checking for alignment of "size_t" : 8
Checking for size of "wchar_t" : 4
Checking if "GCC size_t typedef is long" compiles: YES 
Checking if "GCC size_t typedef is long long" compiles: NO 
Checking if "__va_copy check" compiles: YES 
Checking if "va_copy check" compiles: YES 
Checking if "ISO C99 varargs macros in C" compiles: YES 
Checking if "ISO C99 varargs macros in C++" compiles: YES 
Checking if "GNUC varargs macros" compiles: YES 
Has header "alloca.h" : YES (cached)
Has header "sys/poll.h" : YES 
Has header "sys/types.h" : YES (cached)
Has header "winsock2.h" : NO 
Computing int of "POLLIN" : 1
Computing int of "POLLOUT" : 4
Computing int of "POLLPRI" : 2
Computing int of "POLLERR" : 8
Computing int of "POLLHUP" : 16
Computing int of "POLLNVAL" : 32
Computing int of "AF_UNIX" : 1
Computing int of "AF_INET" : 2
Computing int of "AF_INET6" : 10
Computing int of "MSG_OOB" : 1
Computing int of "MSG_PEEK" : 2
Computing int of "MSG_DONTROUTE" : 4
Checking for type "struct in6_addr" : YES 
Checking if "atomic ops" links: YES 
Checking if "atomic ops define" compiles: YES 
Run-time dependency threads found: YES
Header <pthread.h> has symbol "pthread_attr_setstacksize" : YES 
Header <pthread.h> has symbol "pthread_attr_setinheritsched" : YES 
Header <pthread.h> has symbol "pthread_condattr_setclock" : YES 
Header <pthread.h> has symbol "pthread_cond_timedwait_relative_np" : NO 
Header <pthread.h> has symbol "pthread_getname_np" : NO 
Header <sys/syscall.h> has symbol "SYS_sched_getattr" : YES 
Checking if "pthread_setname_np(const char*)" with dependency threads links: NO 
Checking if "pthread_setname_np(pthread_t, const char*)" with dependency threads links: YES 
Header <iconv.h> has symbol "iconv_open" : YES 
Library iconv found: YES
Library m found: YES
Found pkg-config: /openwrt/staging_dir/host/bin/pkg-config (1.7.3)
Run-time dependency libffi found: YES 3.4.2
Run-time dependency zlib found: YES 1.2.11
Checking for function "bind_textdomain_codeset" : YES 
Dependency mount skipped: feature libmount disabled
Dependency libselinux skipped: feature selinux disabled
Checking for function "getxattr" : YES 
Has header "sys/xattr.h" : YES 
Checking if "XATTR_NOFOLLOW" compiles: NO 
Checking for function "strlcpy" : YES 
Program bash found: YES (/openwrt/staging_dir/host/bin/bash)
Found CMake: NO
Run-time dependency bash-completion found: NO (tried pkgconfig and cmake)
Program sh found: YES (/usr/bin/sh)
Program env found: YES (/usr/bin/env)
Configuring glibconfig.h using configuration
Dependency sysprof-capture-4 skipped: feature sysprof disabled
Configuring gtester-report using configuration
Configuring libglib-2.0.so.0.6800.4-gdb.py using configuration
Configuring glib-genmarshal using configuration
Program glib-genmarshal found: YES (/openwrt/build_dir/target-x86_64_musl/glib-2.68.4/openwrt-build/gobject/glib-genmarshal)
Configuring glib-mkenums using configuration
Program glib-mkenums found: YES (/openwrt/build_dir/target-x86_64_musl/glib-2.68.4/openwrt-build/gobject/glib-mkenums)
Configuring libgobject-2.0.so.0.6800.4-gdb.py using configuration
Message: Cross-compiling: assuming that symbols aren't prefixed with underscore
Checking for function "dlerror" : YES 
Configuring gmoduleconf.h using configuration
Checking if "C_IN in public headers (no arpa/nameser_compat.h needed)" compiles: YES 
Checking if "res_query()" links: YES 
Checking if "socket()" links: YES 
Checking if "res_init()" links: YES 
Checking if "res_nclose()" links: NO 
Checking if "res_ndestroy()" links: NO 
Checking if "res_ninit()" links: NO 
Checking if "res_nquery()" links: NO 
Checking for type "struct ip_mreqn" : YES 
Checking if "ioctl with request SIOCGIFADDR" compiles: YES 
Configuring gnetworking.h using configuration
Configuring gdbus-codegen using configuration
Program gdbus-codegen found: YES (/openwrt/build_dir/target-x86_64_musl/glib-2.68.4/openwrt-build/gio/gdbus-2.0/codegen/gdbus-codegen)
Configuring config.py using configuration
Message: Found bash-completion but the .pc file did not set 'completionsdir', fallback to a predefined path
Dependency libelf skipped: feature libelf disabled
Library elf skipped: feature libelf disabled
Compiler for C supports arguments -Werror=unused-function: YES 
Library FuzzingEngine skipped: feature oss_fuzz disabled
Program xgettext skipped: feature nls disabled
Configuring glib-gettextize using configuration
Configuring config.h using configuration
Build targets in project: 46

Option buildtype is: plain [default: debugoptimized]
Found ninja-1.10.2 at /openwrt/staging_dir/host/bin/ninja
ninja: Entering directory `/openwrt/build_dir/target-x86_64_musl/glib-2.68.4/openwrt-build'
[1/474] Compiling C object glib/libcharset/libcharset.a.p/localcharset.c.o
[2/474] Linking static target glib/libcharset/libcharset.a
[3/474] Compiling C object glib/pcre/libpcre.a.p/pcre_byte_order.c.o
[4/474] Compiling C object glib/pcre/libpcre.a.p/pcre_chartables.c.o
[5/474] Compiling C object glib/pcre/libpcre.a.p/pcre_compile.c.o
../glib/pcre/pcre_compile.c: In function 'compile_branch':
../glib/pcre/pcre_compile.c:6038:17: warning: this statement may fall through [-Wimplicit-fallthrough=]
         else if (*ptr != CHAR_LESS_THAN_SIGN)  /* Test for Python-style defn */
                 ^
../glib/pcre/pcre_compile.c:6047:9: note: here
         DEFINE_NAME:    /* Come here from (?< handling */
         ^~~~~~~~~~~
../glib/pcre/pcre_compile.c: In function 'check_escape':
../glib/pcre/pcre_compile.c:1003:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if ((c = *ptr) >= CHAR_8)
        ^
../glib/pcre/pcre_compile.c:1016:5: note: here
     case CHAR_0:
     ^~~~
../glib/pcre/pcre_compile.c: In function 'find_fixedlength':
../glib/pcre/pcre_compile.c:1898:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     cc += GET(cc, 1) - PRIV(OP_lengths)[OP_CLASS];
     ~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
../glib/pcre/pcre_compile.c:1902:5: note: here
     case OP_CLASS:
     ^~~~
[6/474] Compiling C object glib/pcre/libpcre.a.p/pcre_config.c.o
[7/474] Compiling C object glib/pcre/libpcre.a.p/pcre_dfa_exec.c.o
../glib/pcre/pcre_dfa_exec.c: In function 'internal_dfa_exec':
../glib/pcre/pcre_dfa_exec.c:2145:12: warning: this statement may fall through [-Wimplicit-fallthrough=]
         if ((md->moptions & PCRE_BSR_ANYCRLF) != 0) break;
            ^
../glib/pcre/pcre_dfa_exec.c:2147:9: note: here
         case 0x000a:
         ^~~~
[8/474] Compiling C object glib/pcre/libpcre.a.p/pcre_exec.c.o
../glib/pcre/pcre_exec.c: In function 'match':
../glib/pcre/pcre_exec.c:937:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (offset < md->offset_max)
        ^
../glib/pcre/pcre_exec.c:1025:5: note: here
     case OP_ONCE:
     ^~~~
../glib/pcre/pcre_exec.c:1106:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (offset < md->offset_max)
        ^
../glib/pcre/pcre_exec.c:1193:5: note: here
     case OP_BRAPOS:
     ^~~~
../glib/pcre/pcre_exec.c:2032:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (md->notbol && eptr == md->start_subject) RRETURN(MATCH_NOMATCH);
        ^
../glib/pcre/pcre_exec.c:2036:5: note: here
     case OP_SOD:
     ^~~~
../glib/pcre/pcre_exec.c:2098:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (!md->endonly) goto ASSERT_NL_OR_EOS;
        ^
../glib/pcre/pcre_exec.c:2104:5: note: here
     case OP_EOD:
     ^~~~
[9/474] Compiling C object glib/pcre/libpcre.a.p/pcre_fullinfo.c.o
[10/474] Compiling C object glib/pcre/libpcre.a.p/pcre_get.c.o
[11/474] Compiling C object glib/pcre/libpcre.a.p/pcre_globals.c.o
[12/474] Compiling C object glib/pcre/libpcre.a.p/pcre_jit_compile.c.o
[13/474] Compiling C object glib/pcre/libpcre.a.p/pcre_newline.c.o
[14/474] Compiling C object glib/pcre/libpcre.a.p/pcre_ord2utf8.c.o
[15/474] Compiling C object glib/pcre/libpcre.a.p/pcre_string_utils.c.o
[16/474] Compiling C object glib/pcre/libpcre.a.p/pcre_study.c.o
../glib/pcre/pcre_study.c: In function 'set_start_bits':
../glib/pcre/pcre_study.c:1240:33: warning: '<<' in boolean context, did you mean '<' ? [-Wint-in-bool-context]
             if ((map[c/8] && (1 << (c&7))) != 0)
                              ~~~^~~~~~~~~
../glib/pcre/pcre_study.c: In function 'find_minlength':
../glib/pcre/pcre_study.c:111:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     if (*cs != OP_ALT)
        ^
../glib/pcre/pcre_study.c:120:5: note: here
     case OP_CBRA:
     ^~~~
../glib/pcre/pcre_study.c:326:8: warning: this statement may fall through [-Wimplicit-fallthrough=]
     cc += GET(cc, 1) - PRIV(OP_lengths)[OP_CLASS];
     ~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
../glib/pcre/pcre_study.c:330:5: note: here
     case OP_CLASS:
     ^~~~
[17/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/deprecated_gcache.c.o
[18/474] Compiling C object glib/pcre/libpcre.a.p/pcre_tables.c.o
[19/474] Compiling C object glib/pcre/libpcre.a.p/pcre_valid_utf8.c.o
[20/474] Compiling C object glib/pcre/libpcre.a.p/pcre_version.c.o
[21/474] Compiling C object glib/pcre/libpcre.a.p/pcre_xclass.c.o
[22/474] Linking static target glib/pcre/libpcre.a
[23/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/deprecated_gallocator.c.o
[24/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/deprecated_gcompletion.c.o
[25/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/deprecated_grel.c.o
[26/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/deprecated_gthread-deprecated.c.o
[27/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/garcbox.c.o
[28/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/garray.c.o
[29/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gasyncqueue.c.o
[30/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gatomic.c.o
[31/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gbacktrace.c.o
[32/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gbase64.c.o
In file included from ../glib/gbase64.c:30:
../glib/glibintl.h:17: warning: "_" redefined
 #define _(String) glib_gettext(String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gbase64.c:30:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:41: note: this is the location of the previous definition
 #define _(String) (String)
 
In file included from ../glib/gbase64.c:30:
../glib/glibintl.h:25: warning: "N_" redefined
 #define N_(String) (String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gbase64.c:30:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:42: note: this is the location of the previous definition
 #define N_(String) String
 
[33/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gbitlock.c.o
[34/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gbookmarkfile.c.o
In file included from ../glib/gbookmarkfile.c:38:
../glib/glibintl.h:17: warning: "_" redefined
 #define _(String) glib_gettext(String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gbookmarkfile.c:38:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:41: note: this is the location of the previous definition
 #define _(String) (String)
 
In file included from ../glib/gbookmarkfile.c:38:
../glib/glibintl.h:25: warning: "N_" redefined
 #define N_(String) (String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gbookmarkfile.c:38:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:42: note: this is the location of the previous definition
 #define N_(String) String
 
[35/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gbytes.c.o
[36/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gcharset.c.o
[37/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gchecksum.c.o
In file included from ../glib/gchecksum.c:30:
../glib/glibintl.h:17: warning: "_" redefined
 #define _(String) glib_gettext(String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gchecksum.c:30:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:41: note: this is the location of the previous definition
 #define _(String) (String)
 
In file included from ../glib/gchecksum.c:30:
../glib/glibintl.h:25: warning: "N_" redefined
 #define N_(String) (String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gchecksum.c:30:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:42: note: this is the location of the previous definition
 #define N_(String) String
 
[38/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gconvert.c.o
In file included from ../glib/gconvert.c:54:
../glib/glibintl.h:17: warning: "_" redefined
 #define _(String) glib_gettext(String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gconvert.c:54:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:41: note: this is the location of the previous definition
 #define _(String) (String)
 
In file included from ../glib/gconvert.c:54:
../glib/glibintl.h:25: warning: "N_" redefined
 #define N_(String) (String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gconvert.c:54:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:42: note: this is the location of the previous definition
 #define N_(String) String
 
[39/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gdataset.c.o
[40/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gdate.c.o
[41/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gdatetime.c.o
In file included from ../glib/gdatetime.c:78:
../glib/glibintl.h:17: warning: "_" redefined
 #define _(String) glib_gettext(String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gdatetime.c:78:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:41: note: this is the location of the previous definition
 #define _(String) (String)
 
In file included from ../glib/gdatetime.c:78:
../glib/glibintl.h:25: warning: "N_" redefined
 #define N_(String) (String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gdatetime.c:78:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:42: note: this is the location of the previous definition
 #define N_(String) String
 
[42/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gdir.c.o
In file included from ../glib/gdir.c:41:
../glib/glibintl.h:17: warning: "_" redefined
 #define _(String) glib_gettext(String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gdir.c:41:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:41: note: this is the location of the previous definition
 #define _(String) (String)
 
In file included from ../glib/gdir.c:41:
../glib/glibintl.h:25: warning: "N_" redefined
 #define N_(String) (String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gdir.c:41:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:42: note: this is the location of the previous definition
 #define N_(String) String
 
[43/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/genviron.c.o
[44/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gerror.c.o
[45/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gfileutils.c.o
In file included from ../glib/gfileutils.c:57:
../glib/glibintl.h:17: warning: "_" redefined
 #define _(String) glib_gettext(String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gfileutils.c:57:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:41: note: this is the location of the previous definition
 #define _(String) (String)
 
In file included from ../glib/gfileutils.c:57:
../glib/glibintl.h:25: warning: "N_" redefined
 #define N_(String) (String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gfileutils.c:57:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:42: note: this is the location of the previous definition
 #define N_(String) String
 
[46/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/ggettext.c.o
In file included from ../glib/ggettext.c:28:
../glib/glibintl.h:17: warning: "_" redefined
 #define _(String) glib_gettext(String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/ggettext.c:28:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:41: note: this is the location of the previous definition
 #define _(String) (String)
 
In file included from ../glib/ggettext.c:28:
../glib/glibintl.h:25: warning: "N_" redefined
 #define N_(String) (String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/ggettext.c:28:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:42: note: this is the location of the previous definition
 #define N_(String) String
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/ggettext.c:28:
../glib/ggettext.c: In function 'ensure_gettext_initialized':
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:49:43: warning: statement with no effect [-Wunused-value]
 #define bindtextdomain(Domain, Directory) (Domain)
                                           ^
../glib/ggettext.c:107:7: note: in expansion of macro 'bindtextdomain'
       bindtextdomain (GETTEXT_PACKAGE, GLIB_LOCALE_DIR);
       ^~~~~~~~~~~~~~
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:50:50: warning: statement with no effect [-Wunused-value]
 #define bind_textdomain_codeset(Domain, Codeset) (Codeset)
                                                  ^
../glib/ggettext.c:110:7: note: in expansion of macro 'bind_textdomain_codeset'
       bind_textdomain_codeset (GETTEXT_PACKAGE, "UTF-8");
       ^~~~~~~~~~~~~~~~~~~~~~~
[47/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/ghash.c.o
[48/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/ghmac.c.o
In file included from ../glib/ghmac.c:34:
../glib/glibintl.h:17: warning: "_" redefined
 #define _(String) glib_gettext(String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/ghmac.c:34:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:41: note: this is the location of the previous definition
 #define _(String) (String)
 
In file included from ../glib/ghmac.c:34:
../glib/glibintl.h:25: warning: "N_" redefined
 #define N_(String) (String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/ghmac.c:34:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:42: note: this is the location of the previous definition
 #define N_(String) String
 
[49/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/ghook.c.o
[50/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/ghostutils.c.o
In file included from ../glib/ghostutils.c:35:
../glib/glibintl.h:17: warning: "_" redefined
 #define _(String) glib_gettext(String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/ghostutils.c:35:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:41: note: this is the location of the previous definition
 #define _(String) (String)
 
In file included from ../glib/ghostutils.c:35:
../glib/glibintl.h:25: warning: "N_" redefined
 #define N_(String) (String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/ghostutils.c:35:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:42: note: this is the location of the previous definition
 #define N_(String) String
 
[51/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/giochannel.c.o
In file included from ../glib/giochannel.c:41:
../glib/glibintl.h:17: warning: "_" redefined
 #define _(String) glib_gettext(String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/giochannel.c:41:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:41: note: this is the location of the previous definition
 #define _(String) (String)
 
In file included from ../glib/giochannel.c:41:
../glib/glibintl.h:25: warning: "N_" redefined
 #define N_(String) (String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/giochannel.c:41:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:42: note: this is the location of the previous definition
 #define N_(String) String
 
[52/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gkeyfile.c.o
In file included from ../glib/gkeyfile.c:59:
../glib/glibintl.h:17: warning: "_" redefined
 #define _(String) glib_gettext(String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gkeyfile.c:59:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:41: note: this is the location of the previous definition
 #define _(String) (String)
 
In file included from ../glib/gkeyfile.c:59:
../glib/glibintl.h:25: warning: "N_" redefined
 #define N_(String) (String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gkeyfile.c:59:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:42: note: this is the location of the previous definition
 #define N_(String) String
 
[53/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/glib-init.c.o
[54/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/glib-private.c.o
[55/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/glist.c.o
[56/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gmain.c.o
../glib/gmain.c: In function 'g_main_context_push_thread_default':
../glib/gmain.c:819:12: warning: variable 'acquired_context' set but not used [-Wunused-but-set-variable]
   gboolean acquired_context;
            ^~~~~~~~~~~~~~~~
[57/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gmappedfile.c.o
In file included from ../glib/gmappedfile.c:61:
../glib/glibintl.h:17: warning: "_" redefined
 #define _(String) glib_gettext(String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gmappedfile.c:61:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:41: note: this is the location of the previous definition
 #define _(String) (String)
 
In file included from ../glib/gmappedfile.c:61:
../glib/glibintl.h:25: warning: "N_" redefined
 #define N_(String) (String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gmappedfile.c:61:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:42: note: this is the location of the previous definition
 #define N_(String) String
 
[58/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gmarkup.c.o
In file included from ../glib/gmarkup.c:36:
../glib/glibintl.h:17: warning: "_" redefined
 #define _(String) glib_gettext(String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gmarkup.c:36:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:41: note: this is the location of the previous definition
 #define _(String) (String)
 
In file included from ../glib/gmarkup.c:36:
../glib/glibintl.h:25: warning: "N_" redefined
 #define N_(String) (String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gmarkup.c:36:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:42: note: this is the location of the previous definition
 #define N_(String) String
 
[59/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gmem.c.o
[60/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gmessages.c.o
[61/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gnode.c.o
[62/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/goption.c.o
In file included from ../glib/goption.c:195:
../glib/glibintl.h:17: warning: "_" redefined
 #define _(String) glib_gettext(String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/goption.c:195:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:41: note: this is the location of the previous definition
 #define _(String) (String)
 
In file included from ../glib/goption.c:195:
../glib/glibintl.h:25: warning: "N_" redefined
 #define N_(String) (String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/goption.c:195:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:42: note: this is the location of the previous definition
 #define N_(String) String
 
[63/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gpattern.c.o
[64/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gpoll.c.o
[65/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gprimes.c.o
[66/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gqsort.c.o
[67/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gquark.c.o
[68/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gqueue.c.o
[69/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/grand.c.o
[70/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/grcbox.c.o
[71/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/grefcount.c.o
[72/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/grefstring.c.o
[73/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gregex.c.o
In file included from ../glib/gregex.c:33:
../glib/glibintl.h:17: warning: "_" redefined
 #define _(String) glib_gettext(String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gregex.c:33:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:41: note: this is the location of the previous definition
 #define _(String) (String)
 
In file included from ../glib/gregex.c:33:
../glib/glibintl.h:25: warning: "N_" redefined
 #define N_(String) (String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gregex.c:33:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:42: note: this is the location of the previous definition
 #define N_(String) String
 
[74/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gscanner.c.o
[75/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gsequence.c.o
../glib/gsequence.c: In function 'g_sequence_remove_range':
../glib/gsequence.c:578:26: warning: variable 'seq_end' set but not used [-Wunused-but-set-variable]
   GSequence *seq_begin, *seq_end;
                          ^~~~~~~
../glib/gsequence.c:578:14: warning: variable 'seq_begin' set but not used [-Wunused-but-set-variable]
   GSequence *seq_begin, *seq_end;
              ^~~~~~~~~
At top level:
../glib/gsequence.c:188:1: warning: 'seq_is_end' defined but not used [-Wunused-function]
 seq_is_end (GSequence     *seq,
 ^~~~~~~~~~
[76/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gshell.c.o
In file included from ../glib/gshell.c:31:
../glib/glibintl.h:17: warning: "_" redefined
 #define _(String) glib_gettext(String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gshell.c:31:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:41: note: this is the location of the previous definition
 #define _(String) (String)
 
In file included from ../glib/gshell.c:31:
../glib/glibintl.h:25: warning: "N_" redefined
 #define N_(String) (String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gshell.c:31:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:42: note: this is the location of the previous definition
 #define N_(String) String
 
[77/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gslice.c.o
[78/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gslist.c.o
[79/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gstdio.c.o
[80/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gstrfuncs.c.o
In file included from ../glib/gstrfuncs.c:56:
../glib/glibintl.h:17: warning: "_" redefined
 #define _(String) glib_gettext(String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gstrfuncs.c:56:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:41: note: this is the location of the previous definition
 #define _(String) (String)
 
In file included from ../glib/gstrfuncs.c:56:
../glib/glibintl.h:25: warning: "N_" redefined
 #define N_(String) (String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gstrfuncs.c:56:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:42: note: this is the location of the previous definition
 #define N_(String) String
 
[81/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gstring.c.o
[82/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gstringchunk.c.o
[83/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gstrvbuilder.c.o
[84/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gtestutils.c.o
[85/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gthread.c.o
[86/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gthreadpool.c.o
[87/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gtimer.c.o
[88/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gtimezone.c.o
../glib/gtimezone.c:2071:1: warning: 'interval_valid' defined but not used [-Wunused-function]
 interval_valid (GTimeZone *tz,
 ^~~~~~~~~~~~~~
[89/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gtrace.c.o
[90/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gtranslit.c.o
[91/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gtrashstack.c.o
[92/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gtree.c.o
[93/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/guniprop.c.o
[94/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gutf8.c.o
In file included from ../glib/gutf8.c:41:
../glib/glibintl.h:17: warning: "_" redefined
 #define _(String) glib_gettext(String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gutf8.c:41:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:41: note: this is the location of the previous definition
 #define _(String) (String)
 
In file included from ../glib/gutf8.c:41:
../glib/glibintl.h:25: warning: "N_" redefined
 #define N_(String) (String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gutf8.c:41:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:42: note: this is the location of the previous definition
 #define N_(String) String
 
[95/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gunibreak.c.o
[96/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gunicollate.c.o
[97/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gunidecomp.c.o
[98/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/guri.c.o
In file included from ../glib/guri.c:25:
../glib/glibintl.h:17: warning: "_" redefined
 #define _(String) glib_gettext(String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/guri.c:25:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:41: note: this is the location of the previous definition
 #define _(String) (String)
 
In file included from ../glib/guri.c:25:
../glib/glibintl.h:25: warning: "N_" redefined
 #define N_(String) (String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/guri.c:25:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:42: note: this is the location of the previous definition
 #define N_(String) String
 
[99/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gutils.c.o
In file included from ../glib/gutils.c:70:
../glib/glibintl.h:17: warning: "_" redefined
 #define _(String) glib_gettext(String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gutils.c:70:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:41: note: this is the location of the previous definition
 #define _(String) (String)
 
In file included from ../glib/gutils.c:70:
../glib/glibintl.h:25: warning: "N_" redefined
 #define N_(String) (String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gutils.c:70:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:42: note: this is the location of the previous definition
 #define N_(String) String
 
[100/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/guuid.c.o
In file included from ../glib/guuid.c:26:
../glib/gi18n.h:26: warning: "_" redefined
 #define  _(String) gettext (String)
 
In file included from ../glib/gi18n.h:23,
                 from ../glib/guuid.c:26:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:41: note: this is the location of the previous definition
 #define _(String) (String)
 
In file included from ../glib/guuid.c:26:
../glib/gi18n.h:28: warning: "N_" redefined
 #define N_(String) (String)
 
In file included from ../glib/gi18n.h:23,
                 from ../glib/guuid.c:26:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:42: note: this is the location of the previous definition
 #define N_(String) String
 
[101/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gvariant.c.o
../glib/gvariant.c:4562:1: warning: 'valid_format_string' defined but not used [-Wunused-function]
 valid_format_string (const gchar *format_string,
 ^~~~~~~~~~~~~~~~~~~
../glib/gvariant.c:3859:1: warning: 'ensure_valid_dict' defined but not used [-Wunused-function]
 ensure_valid_dict (GVariantDict *dict)
 ^~~~~~~~~~~~~~~~~
../glib/gvariant.c:3202:1: warning: 'ensure_valid_builder' defined but not used [-Wunused-function]
 ensure_valid_builder (GVariantBuilder *builder)
 ^~~~~~~~~~~~~~~~~~~~
[102/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gvariant-core.c.o
[103/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gvariant-parser.c.o
[104/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gvariant-serialiser.c.o
[105/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gvarianttypeinfo.c.o
[106/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gvarianttype.c.o
../glib/gvarianttype.c:189:1: warning: 'g_variant_type_check' defined but not used [-Wunused-function]
 g_variant_type_check (const GVariantType *type)
 ^~~~~~~~~~~~~~~~~~~~
[107/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gversion.c.o
[108/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gwakeup.c.o
[109/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gprintf.c.o
[110/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/glib-unix.c.o
[111/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gspawn.c.o
In file included from ../glib/gspawn.c:67:
../glib/glibintl.h:17: warning: "_" redefined
 #define _(String) glib_gettext(String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gspawn.c:67:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:41: note: this is the location of the previous definition
 #define _(String) (String)
 
In file included from ../glib/gspawn.c:67:
../glib/glibintl.h:25: warning: "N_" redefined
 #define N_(String) (String)
 
In file included from ../glib/glibintl.h:16,
                 from ../glib/gspawn.c:67:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:42: note: this is the location of the previous definition
 #define N_(String) String
 
[112/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/giounix.c.o
[113/474] Compiling C object glib/libglib-2.0.so.0.6800.4.p/gthread-posix.c.o
[114/474] Generating glib_enumtypes_h with a custom command (wrapped by meson to capture output)
[115/474] Compiling C object gobject/libgobject-2.0.so.0.6800.4.p/gsourceclosure.c.o
[116/474] Compiling C object gobject/libgobject-2.0.so.0.6800.4.p/gatomicarray.c.o
[117/474] Compiling C object glib/gtester.p/gtester.c.o
[118/474] Generating glib_enumtypes_c with a custom command (wrapped by meson to capture output)
[119/474] Compiling C object gobject/libgobject-2.0.so.0.6800.4.p/meson-generated_.._glib-enumtypes.c.o
[120/474] Linking target glib/libglib-2.0.so.0.6800.4
[121/474] Generating symbol file glib/libglib-2.0.so.0.6800.4.p/libglib-2.0.so.0.6800.4.symbols
[122/474] Linking target glib/gtester
[123/474] Linking static target glib/libglib-2.0.a
[124/474] Compiling C object gobject/libgobject-2.0.so.0.6800.4.p/gparamspecs.c.o
[125/474] Compiling C object gobject/libgobject-2.0.so.0.6800.4.p/gparam.c.o
[126/474] Compiling C object gobject/libgobject-2.0.so.0.6800.4.p/gclosure.c.o
[127/474] Compiling C object gobject/libgobject-2.0.so.0.6800.4.p/gbinding.c.o
In file included from ../gobject/gbinding.c:117:
../glib/glibintl.h:17: warning: "_" redefined
 #define _(String) glib_gettext(String)
 
In file included from ../glib/glibintl.h:16,
                 from ../gobject/gbinding.c:117:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:41: note: this is the location of the previous definition
 #define _(String) (String)
 
In file included from ../gobject/gbinding.c:117:
../glib/glibintl.h:25: warning: "N_" redefined
 #define N_(String) (String)
 
In file included from ../glib/glibintl.h:16,
                 from ../gobject/gbinding.c:117:
../../../../staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include/libintl.h:42: note: this is the location of the previous definition
 #define N_(String) String
 
../gobject/gbinding.c:702:1: warning: 'is_valid_property_name' defined but not used [-Wunused-function]
 is_valid_property_name (const gchar *key)
 ^~~~~~~~~~~~~~~~~~~~~~
[128/474] Compiling C object gobject/libgobject-2.0.so.0.6800.4.p/gboxed.c.o
[129/474] Compiling C object gobject/libgobject-2.0.so.0.6800.4.p/genums.c.o
../gobject/genums.c: In function '_g_enum_types_init':
../gobject/genums.c:90:19: warning: variable 'initialized' set but not used [-Wunused-but-set-variable]
   static gboolean initialized = FALSE;
                   ^~~~~~~~~~~
[130/474] Compiling C object gobject/libgobject-2.0.so.0.6800.4.p/gmarshal.c.o
[131/474] Compiling C object gobject/libgobject-2.0.so.0.6800.4.p/gobject.c.o
../gobject/gobject.c: In function '_g_object_type_init':
../gobject/gobject.c:404:19: warning: variable 'initialized' set but not used [-Wunused-but-set-variable]
   static gboolean initialized = FALSE;
                   ^~~~~~~~~~~
../gobject/gobject.c: In function 'g_object_ref':
../gobject/gobject.c:3387:12: warning: variable 'object_already_finalized' set but not used [-Wunused-but-set-variable]
   gboolean object_already_finalized;
            ^~~~~~~~~~~~~~~~~~~~~~~~
[132/474] Compiling C object gobject/libgobject-2.0.so.0.6800.4.p/gsignal.c.o
[133/474] Compiling C object gobject/gobject-query.p/gobject-query.c.o
[134/474] Compiling C object gthread/libgthread-2.0.so.0.6800.4.p/gthread-impl.c.o
[135/474] Compiling C object gobject/libgobject-2.0.so.0.6800.4.p/gtype.c.o
[136/474] Compiling C object gobject/libgobject-2.0.so.0.6800.4.p/gtypemodule.c.o
[137/474] Compiling C object gobject/libgobject-2.0.so.0.6800.4.p/gtypeplugin.c.o
[138/474] Compiling C object gobject/libgobject-2.0.so.0.6800.4.p/gvalue.c.o
[139/474] Compiling C object gobject/libgobject-2.0.so.0.6800.4.p/gvaluearray.c.o
[140/474] Compiling C object gobject/libgobject-2.0.so.0.6800.4.p/gvaluetransform.c.o
[141/474] Compiling C object gobject/libgobject-2.0.so.0.6800.4.p/gvaluetypes.c.o
[142/474] Linking target gobject/libgobject-2.0.so.0.6800.4
[143/474] Generating symbol file gobject/libgobject-2.0.so.0.6800.4.p/libgobject-2.0.so.0.6800.4.symbols
[144/474] Linking static target gobject/libgobject-2.0.a
[145/474] Linking target gobject/gobject-query
[146/474] Linking target gthread/libgthread-2.0.so.0.6800.4
[147/474] Linking static target gthread/libgthread-2.0.a
[148/474] Compiling C object gmodule/libgmodule-2.0.so.0.6800.4.p/gmodule.c.o
[149/474] Linking target gmodule/libgmodule-2.0.so.0.6800.4
[150/474] Generating symbol file gmodule/libgmodule-2.0.so.0.6800.4.p/libgmodule-2.0.so.0.6800.4.symbols
[151/474] Linking static target gmodule/libgmodule-2.0.a
[152/474] Compiling C object gio/xdgmime/libxdgmime.a.p/xdgmime.c.o
[153/474] Generating xdp-dbus with a custom command
FAILED: gio/xdp-dbus.h gio/xdp-dbus.c 
python3 gio/gdbus-2.0/codegen/gdbus-codegen --interface-prefix org.freedesktop.portal. --output-directory gio --generate-c-code xdp-dbus --c-namespace GXdp ../gio/org.freedesktop.portal.Documents.xml ../gio/org.freedesktop.portal.OpenURI.xml ../gio/org.freedesktop.portal.ProxyResolver.xml ../gio/org.freedesktop.portal.Trash.xml
Python path configuration:
  PYTHONHOME = (not set)
  PYTHONPATH = (not set)
  program name = 'python3'
  isolated = 0
  environment = 1
  user site = 1
  import site = 1
  sys._base_executable = '/openwrt/staging_dir/hostpkg/bin/python3'
  sys.base_prefix = '/openwrt/staging_dir/hostpkg'
  sys.base_exec_prefix = '/openwrt/staging_dir/hostpkg'
  sys.platlibdir = 'lib'
  sys.executable = '/openwrt/staging_dir/hostpkg/bin/python3'
  sys.prefix = '/openwrt/staging_dir/hostpkg'
  sys.exec_prefix = '/openwrt/staging_dir/hostpkg'
  sys.path = [
    '/openwrt/staging_dir/hostpkg/lib/python39.zip',
    '/openwrt/staging_dir/hostpkg/lib/python3.9',
    '/openwrt/staging_dir/hostpkg/lib/python3.9/lib-dynload',
  ]
Fatal Python error: init_fs_encoding: failed to get the Python codec of the filesystem encoding
Python runtime state: core initialized
LookupError: no codec search functions registered: can't find encoding

Current thread 0x00007f703ad1d740 (most recent call first):
<no Python frame>
ninja: build stopped: subcommand failed.
make[3]: *** [Makefile:134: /openwrt/build_dir/target-x86_64_musl/glib-2.68.4/.built] Error 1
```
