---
title: "compile.42"
date: 2021-06-29 09:40:48.066033
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
Source dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/glib-2.68.1
Build dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/glib-2.68.1/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: glib
Project version: 2.68.1
C compiler for the host machine: ccache_cc (gcc 8.4.0 "aarch64-openwrt-linux-musl-gcc (OpenWrt GCC 8.4.0 r0-af265d3) 8.4.0")
C linker for the host machine: ccache_cc ld.bfd 2.34
C++ compiler for the host machine: ccache_cxx (gcc 8.4.0 "aarch64-openwrt-linux-musl-g++ (OpenWrt GCC 8.4.0 r0-af265d3) 8.4.0")
C++ linker for the host machine: ccache_cxx ld.bfd 2.34
C compiler for the build machine: ccache gcc (gcc 9.3.0 "gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0")
C linker for the build machine: gcc ld.bfd 2.34
C++ compiler for the build machine: ccache g++ (gcc 9.3.0 "g++ (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0")
C++ linker for the build machine: g++ ld.bfd 2.34
Build machine cpu family: x86_64
Build machine cpu: x86_64
Host machine cpu family: aarch64
Host machine cpu: generic
Target machine cpu family: aarch64
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
Run-time dependency libffi found: YES 3.3
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
Configuring libglib-2.0.so.0.6800.1-gdb.py using configuration
Configuring glib-genmarshal using configuration
Program glib-genmarshal found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/glib-2.68.1/openwrt-build/gobject/glib-genmarshal)
Configuring glib-mkenums using configuration
Program glib-mkenums found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/glib-2.68.1/openwrt-build/gobject/glib-mkenums)
Configuring libgobject-2.0.so.0.6800.1-gdb.py using configuration
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
Program gdbus-codegen found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/glib-2.68.1/openwrt-build/gio/gdbus-2.0/codegen/gdbus-codegen)
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

ERROR: Could not detect Ninja v1.8.2 or newer

A full log can be found at /openwrt/build_dir/target-aarch64_cortex-a72_musl/glib-2.68.1/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:137: /openwrt/build_dir/target-aarch64_cortex-a72_musl/glib-2.68.1/.configured_efb2d3cf01c707184fb77fd0fe149f94] Error 1
```
