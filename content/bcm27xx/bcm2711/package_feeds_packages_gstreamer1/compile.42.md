---
title: "compile.42"
date: 2021-06-29 09:40:48.069580
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
make package/feeds/packages/gstreamer1/compile -j$(nproc) || make package/feeds/packages/gstreamer1/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-gstplugin-use-lazy-symbol-binding.patch using plaintext: 
patching file gst/gstplugin.c

Applying ./patches/020-distutils.patch using plaintext: 
patching file meson.build
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/gstreamer-1.18.4
Build dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/gstreamer-1.18.4/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: gstreamer
Project version: 1.18.4
C compiler for the host machine: ccache_cc (gcc 8.4.0 "aarch64-openwrt-linux-musl-gcc (OpenWrt GCC 8.4.0 r0-af265d3) 8.4.0")
C linker for the host machine: ccache_cc ld.bfd 2.34
C compiler for the build machine: ccache gcc (gcc 9.3.0 "gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0")
C linker for the build machine: gcc ld.bfd 2.34
Build machine cpu family: x86_64
Build machine cpu: x86_64
Host machine cpu family: aarch64
Host machine cpu: generic
Target machine cpu family: aarch64
Target machine cpu: generic
Compiler for C supports link arguments -Wl,-Bsymbolic-functions: YES 
Compiler for C supports arguments -fvisibility=hidden: YES 
Compiler for C supports arguments -fno-strict-aliasing: YES 
Message: Disabling GLib cast checks
Message: Disabling GLib asserts
Has header "dlfcn.h" : YES 
Has header "inttypes.h" : YES 
Has header "memory.h" : YES 
Has header "poll.h" : YES 
Has header "stdint.h" : YES 
Has header "stdio_ext.h" : YES 
Has header "strings.h" : YES 
Has header "string.h" : YES 
Has header "sys/param.h" : YES 
Has header "sys/poll.h" : YES 
Has header "sys/prctl.h" : YES 
Has header "sys/socket.h" : YES 
Has header "sys/stat.h" : YES 
Has header "sys/times.h" : YES 
Has header "sys/time.h" : YES 
Has header "sys/types.h" : YES 
Has header "sys/utsname.h" : YES 
Has header "sys/wait.h" : YES 
Has header "ucontext.h" : YES 
Has header "unistd.h" : YES 
Has header "valgrind/valgrind.h" : NO 
Has header "sys/resource.h" : YES 
Has header "sys/uio.h" : YES 
Checking whether type "struct tm" has member "tm_gmtoff" : YES 
Checking for function "gmtime_r" : YES 
Checking for function "sigaction" : YES 
Checking for function "getrusage" : YES 
Checking for function "fseeko" : YES 
Checking for function "ftello" : YES 
Checking for function "poll" : YES 
Checking for function "ppoll" : YES 
Checking for function "pselect" : YES 
Checking for function "getpagesize" : YES 
Checking for function "clock_gettime" : YES 
Checking for function "strnlen" : YES 
Checking for function "getline" : YES 
Checking for function "mkstemp" : YES 
Checking for function "alarm" : YES 
Checking for function "gettimeofday" : YES 
Checking for function "localtime_r" : YES 
Checking if "pthread_setname_np(const char*)" links: YES 
Header <pthread.h> has symbol "pthread_condattr_setclock" : YES 
Header <pthread.h> has symbol "pthread_cond_timedwait_relative_np" : NO 
Checking if "futex(2) system call" links: YES 
Checking if "posix timers from time.h" compiles: YES 
Checking if "monotonic clock from time.h" compiles: YES 
Checking if "__uint128_t available" compiles: YES 
Checking for function "getpid" : YES 
Checking for function "strdup" : YES 
Checking for function "strsignal" : YES 
Checking for type "clockid_t" : YES 
Checking for type "timer_t" : YES 
Checking whether type "struct timespec" has members "tv_sec", "tv_nsec" : YES 
Checking whether type "struct itimerspec" has members "it_interval", "it_value" : YES 
Dependency libunwind skipped: feature libunwind disabled
Dependency libdw skipped: feature libdw disabled
WARNING: Project targeting '>= 0.48' but tried to use feature introduced in '0.50.0': required arg in compiler.has_header.
Has header "dbghelp.h" skipped: feature dbghelp disabled
Checking for function "backtrace" : NO 
Message: NO support for stack traces.
Has header "execinfo.h" : NO 
Compiler for C supports arguments -Wmissing-declarations: YES 
Compiler for C supports arguments -Wmissing-prototypes: YES 
Compiler for C supports arguments -Wredundant-decls: YES 
Compiler for C supports arguments -Wundef: YES 
Compiler for C supports arguments -Wwrite-strings: YES 
Compiler for C supports arguments -Wformat: YES 
Compiler for C supports arguments -Wformat-nonliteral: YES 
Compiler for C supports arguments -Wformat-security: YES 
Compiler for C supports arguments -Wold-style-definition: YES 
Compiler for C supports arguments -Winit-self: YES 
Compiler for C supports arguments -Wmissing-include-dirs: YES 
Compiler for C supports arguments -Waddress: YES 
Compiler for C supports arguments -Waggregate-return: YES 
Compiler for C supports arguments -Wno-multichar: YES 
Compiler for C supports arguments -Wdeclaration-after-statement: YES 
Compiler for C supports arguments -Wvla: YES 
Compiler for C supports arguments -Wpointer-arith: YES 
Library gmp found: YES
Library gsl found: NO
Library gslcblas found: NO
Library dl found: YES
Checking for function "dladdr" with dependency -ldl: YES 
Found pkg-config: /openwrt/staging_dir/host/bin/pkg-config (1.7.3)
Found CMake: NO
Run-time dependency glib-2.0 found: NO (tried pkgconfig and cmake)
Looking for a fallback subproject for the dependency glib-2.0

../../../../build_dir/target-aarch64_cortex-a72_musl/gstreamer-1.18.4/meson.build:482:0: ERROR: Neither a subproject directory nor a glib.wrap file was found.

A full log can be found at /openwrt/build_dir/target-aarch64_cortex-a72_musl/gstreamer-1.18.4/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:244: /openwrt/build_dir/target-aarch64_cortex-a72_musl/gstreamer-1.18.4/.configured_a17fb5ef857664f03cd0ce37cc5ea591] Error 1
```
