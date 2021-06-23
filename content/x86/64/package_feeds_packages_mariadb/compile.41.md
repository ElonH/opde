---
title: "compile.41"
date: 2021-06-23 23:13:13.735552
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
make package/feeds/packages/mariadb/compile -j$(nproc) || make package/feeds/packages/mariadb/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/100-fix_hostname.patch using plaintext: 
patching file scripts/mysql_install_db.sh

Applying ./patches/110-pcre.cmake.patch using plaintext: 
patching file cmake/pcre.cmake

Applying ./patches/130-c11_atomics.patch using plaintext: 
patching file configure.cmake
patching file mysys/CMakeLists.txt
patching file sql/CMakeLists.txt

Applying ./patches/140-mips-connect-unaligned.patch using plaintext: 
patching file storage/connect/valblk.cpp
patching file storage/connect/valblk.h

Applying ./patches/160-mips-machine.patch using plaintext: 
patching file cmake/package_name.cmake

Applying ./patches/170-ppc-remove-glibc-dep.patch using plaintext: 
patching file include/my_cpu.h
patching file storage/tokudb/PerconaFT/portability/toku_time.h

Applying ./patches/180-relax-mysql_install-db-wrt-pam-tool.patch using plaintext: 
patching file scripts/mysql_install_db.sh

Applying ./patches/190-replace-hostname-in-mysqld_safe.patch using plaintext: 
patching file scripts/mysqld_safe.sh

Applying ./patches/200-no-selinux.patch using plaintext: 
patching file support-files/CMakeLists.txt
CMake Deprecation Warning at CMakeLists.txt:17 (CMAKE_MINIMUM_REQUIRED):
  Compatibility with CMake < 2.8.12 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- Running cmake version 3.20.3
-- The C compiler identification is GNU 8.4.0
-- The CXX compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/bin/x86_64-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/bin/x86_64-openwrt-linux-musl-g++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Looking for SHM_HUGETLB
-- Looking for SHM_HUGETLB - found
-- Found Git: /openwrt/staging_dir/host/bin/git (found version "2.25.1") 
-- MariaDB 10.4.18
-- Looking for sys/types.h
-- Looking for sys/types.h - found
-- Looking for stdint.h
-- Looking for stdint.h - found
-- Looking for stddef.h
-- Looking for stddef.h - found
-- Check size of void *
-- Check size of void * - done
-- Packaging as: mariadb-10.4.18-Linux-x86_64
-- Performing Test HAVE_VISIBILITY_HIDDEN
-- Performing Test HAVE_VISIBILITY_HIDDEN - Success
CMake Deprecation Warning at wsrep-lib/CMakeLists.txt:5 (cmake_minimum_required):
  Compatibility with CMake < 2.8.12 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- Wsrep-lib version: 1.0.0
-- Performing Test HAVE_SUGGEST_OVERRIDE
-- Performing Test HAVE_SUGGEST_OVERRIDE - Success
-- Looking for dlopen in dl
-- Looking for dlopen in dl - found
-- Performing Test have_C__ggdb3
-- Performing Test have_C__ggdb3 - Success
-- Performing Test have_CXX__ggdb3
-- Performing Test have_CXX__ggdb3 - Success
-- Looking for floor
-- Looking for floor - found
-- Looking for __infinity
-- Looking for __infinity - not found
-- Looking for __infinity in m
-- Looking for __infinity in m - not found
-- Looking for gethostbyname_r
-- Looking for gethostbyname_r - found
-- Looking for bind
-- Looking for bind - found
-- Looking for crypt
-- Looking for crypt - found
-- Looking for setsockopt
-- Looking for setsockopt - found
-- Looking for sched_yield
-- Looking for sched_yield - found
-- Looking for clock_gettime
-- Looking for clock_gettime - found
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
-- Looking for 4 include files stdlib.h, ..., float.h
-- Looking for 4 include files stdlib.h, ..., float.h - found
-- Looking for include file alloca.h
-- Looking for include file alloca.h - found
-- Looking for include file arpa/inet.h
-- Looking for include file arpa/inet.h - found
-- Looking for include file crypt.h
-- Looking for include file crypt.h - found
-- Looking for include file dirent.h
-- Looking for include file dirent.h - found
-- Looking for include file dlfcn.h
-- Looking for include file dlfcn.h - found
-- Looking for include file execinfo.h
-- Looking for include file execinfo.h - not found
-- Looking for include file fcntl.h
-- Looking for include file fcntl.h - found
-- Looking for include file fenv.h
-- Looking for include file fenv.h - found
-- Looking for include file float.h
-- Looking for include file float.h - found
-- Looking for include file fpu_control.h
-- Looking for include file fpu_control.h - not found
-- Looking for include file grp.h
-- Looking for include file grp.h - found
-- Looking for include file ieeefp.h
-- Looking for include file ieeefp.h - not found
-- Looking for include file inttypes.h
-- Looking for include file inttypes.h - found
-- Looking for include file langinfo.h
-- Looking for include file langinfo.h - found
-- Looking for include file link.h
-- Looking for include file link.h - found
-- Looking for include file linux/unistd.h
-- Looking for include file linux/unistd.h - found
-- Looking for include file limits.h
-- Looking for include file limits.h - found
-- Looking for include file locale.h
-- Looking for include file locale.h - found
-- Looking for include file malloc.h
-- Looking for include file malloc.h - found
-- Looking for include file memory.h
-- Looking for include file memory.h - found
-- Looking for include file ndir.h
-- Looking for include file ndir.h - not found
-- Looking for include file netinet/in.h
-- Looking for include file netinet/in.h - found
-- Looking for include file paths.h
-- Looking for include file paths.h - found
-- Looking for include file poll.h
-- Looking for include file poll.h - found
-- Looking for include file sys/poll.h
-- Looking for include file sys/poll.h - found
-- Looking for include file pwd.h
-- Looking for include file pwd.h - found
-- Looking for include file sched.h
-- Looking for include file sched.h - found
-- Looking for include file select.h
-- Looking for include file select.h - not found
-- Looking for include files sys/types.h, sys/dir.h
-- Looking for include files sys/types.h, sys/dir.h - found
-- Looking for include files sys/types.h, sys/event.h
-- Looking for include files sys/types.h, sys/event.h - not found
-- Looking for include file sys/ndir.h
-- Looking for include file sys/ndir.h - not found
-- Looking for include file sys/pte.h
-- Looking for include file sys/pte.h - not found
-- Looking for include file stdlib.h
-- Looking for include file stdlib.h - found
-- Looking for include file strings.h
-- Looking for include file strings.h - found
-- Looking for include file string.h
-- Looking for include file string.h - found
-- Looking for include file synch.h
-- Looking for include file synch.h - not found
-- Looking for include file sysent.h
-- Looking for include file sysent.h - not found
-- Looking for include file sys/file.h
-- Looking for include file sys/file.h - found
-- Looking for include file sys/fpu.h
-- Looking for include file sys/fpu.h - not found
-- Looking for include file sys/ioctl.h
-- Looking for include file sys/ioctl.h - found
-- Looking for include files sys/types.h, sys/ipc.h
-- Looking for include files sys/types.h, sys/ipc.h - found
-- Looking for include files sys/types.h, sys/malloc.h
-- Looking for include files sys/types.h, sys/malloc.h - not found
-- Looking for include file sys/mman.h
-- Looking for include file sys/mman.h - found
-- Looking for include file sys/prctl.h
-- Looking for include file sys/prctl.h - found
-- Looking for include file sys/resource.h
-- Looking for include file sys/resource.h - found
-- Looking for include file sys/select.h
-- Looking for include file sys/select.h - found
-- Looking for include files sys/types.h, sys/shm.h
-- Looking for include files sys/types.h, sys/shm.h - found
-- Looking for include file sys/socket.h
-- Looking for include file sys/socket.h - found
-- Looking for include file sys/stat.h
-- Looking for include file sys/stat.h - found
-- Looking for include file sys/stream.h
-- Looking for include file sys/stream.h - not found
-- Looking for include file sys/syscall.h
-- Looking for include file sys/syscall.h - found
-- Looking for include file asm/termbits.h
-- Looking for include file asm/termbits.h - found
-- Looking for include file termbits.h
-- Looking for include file termbits.h - not found
-- Looking for include file termios.h
-- Looking for include file termios.h - found
-- Looking for include file termio.h
-- Looking for include file termio.h - not found
-- Looking for include file termcap.h
-- Looking for include file termcap.h - found
-- Looking for include file unistd.h
-- Looking for include file unistd.h - found
-- Looking for include file utime.h
-- Looking for include file utime.h - found
-- Looking for include file varargs.h
-- Looking for include file varargs.h - not found
-- Looking for include file sys/time.h
-- Looking for include file sys/time.h - found
-- Looking for include file sys/utime.h
-- Looking for include file sys/utime.h - not found
-- Looking for include file sys/wait.h
-- Looking for include file sys/wait.h - found
-- Looking for include file sys/param.h
-- Looking for include file sys/param.h - found
-- Looking for include file sys/vadvise.h
-- Looking for include file sys/vadvise.h - not found
-- Looking for include file fnmatch.h
-- Looking for include file fnmatch.h - found
-- Looking for include file stdarg.h
-- Looking for include file stdarg.h - found
-- Looking for include files stdlib.h, sys/un.h
-- Looking for include files stdlib.h, sys/un.h - found
-- Looking for include file wchar.h
-- Looking for include file wchar.h - found
-- Looking for include file wctype.h
-- Looking for include file wctype.h - found
-- Looking for include file sys/sockio.h
-- Looking for include file sys/sockio.h - not found
-- Looking for include file sys/utsname.h
-- Looking for include file sys/utsname.h - found
-- Looking for include file sys/statvfs.h
-- Looking for include file sys/statvfs.h - found
-- Looking for include file bfd.h
-- Looking for include file bfd.h - found
-- Looking for include file sys/ptem.h
-- Looking for include file sys/ptem.h - not found
-- Performing Test have_C__Werror
-- Performing Test have_C__Werror - Success
-- Performing Test HAVE_PTHREAD_ONCE_INIT
-- Performing Test HAVE_PTHREAD_ONCE_INIT - Success
-- Looking for accept4
-- Looking for accept4 - found
-- Looking for access
-- Looking for access - found
-- Looking for alarm
-- Looking for alarm - found
-- Looking for backtrace
-- Looking for backtrace - not found
-- Looking for backtrace_symbols
-- Looking for backtrace_symbols - not found
-- Looking for backtrace_symbols_fd
-- Looking for backtrace_symbols_fd - not found
-- Looking for printstack
-- Looking for printstack - not found
-- Looking for bfill
-- Looking for bfill - not found
-- Looking for index
-- Looking for index - found
-- Looking for clock_gettime
-- Looking for clock_gettime - found
-- Looking for cuserid
-- Looking for cuserid - found
-- Looking for ftruncate
-- Looking for ftruncate - found
-- Looking for compress
-- Looking for compress - not found
-- Looking for crypt
-- Looking for crypt - found
-- Looking for dladdr
-- Looking for dladdr - found
-- Looking for dlerror
-- Looking for dlerror - found
-- Looking for dlopen
-- Looking for dlopen - found
-- Looking for fchmod
-- Looking for fchmod - found
-- Looking for fcntl
-- Looking for fcntl - found
-- Looking for fdatasync
-- Looking for fdatasync - found
-- Looking for fdatasync
-- Looking for fdatasync - found
-- Looking for fesetround
-- Looking for fesetround - found
-- Looking for fedisableexcept
-- Looking for fedisableexcept - not found
-- Looking for fseeko
-- Looking for fseeko - found
-- Looking for fsync
-- Looking for fsync - found
-- Looking for getcwd
-- Looking for getcwd - found
-- Looking for gethostbyaddr_r
-- Looking for gethostbyaddr_r - found
-- Looking for gethrtime
-- Looking for gethrtime - not found
-- Looking for getpass
-- Looking for getpass - found
-- Looking for getpassphrase
-- Looking for getpassphrase - not found
-- Looking for getpwnam
-- Looking for getpwnam - found
-- Looking for getpwuid
-- Looking for getpwuid - found
-- Looking for getrlimit
-- Looking for getrlimit - found
-- Looking for getifaddrs
-- Looking for getifaddrs - found
-- Looking for getrusage
-- Looking for getrusage - found
-- Looking for getwd
-- Looking for getwd - not found
-- Looking for gmtime_r
-- Looking for gmtime_r - found
-- Looking for initgroups
-- Looking for initgroups - found
-- Looking for ldiv
-- Looking for ldiv - found
-- Looking for localtime_r
-- Looking for localtime_r - found
-- Looking for lstat
-- Looking for lstat - found
-- Looking for madvise
-- Looking for madvise - found
-- Looking for mallinfo
-- Looking for mallinfo - not found
-- Looking for memcpy
-- Looking for memcpy - found
-- Looking for memmove
-- Looking for memmove - found
-- Looking for mkstemp
-- Looking for mkstemp - found
-- Looking for mkostemp
-- Looking for mkostemp - found
-- Looking for mlock
-- Looking for mlock - found
-- Looking for mlockall
-- Looking for mlockall - found
-- Looking for mmap
-- Looking for mmap - found
-- Looking for mmap64
-- Looking for mmap64 - found
-- Looking for perror
-- Looking for perror - found
-- Looking for poll
-- Looking for poll - found
-- Looking for posix_fallocate
-- Looking for posix_fallocate - found
-- Looking for pread
-- Looking for pread - found
-- Looking for pthread_attr_create
-- Looking for pthread_attr_create - not found
-- Looking for pthread_attr_getstacksize
-- Looking for pthread_attr_getstacksize - found
-- Looking for pthread_attr_setscope
-- Looking for pthread_attr_setscope - found
-- Looking for pthread_attr_getguardsize
-- Looking for pthread_attr_getguardsize - found
-- Looking for pthread_attr_setstacksize
-- Looking for pthread_attr_setstacksize - found
-- Looking for pthread_condattr_create
-- Looking for pthread_condattr_create - not found
-- Looking for pthread_getaffinity_np
-- Looking for pthread_getaffinity_np - found
-- Looking for pthread_key_delete
-- Looking for pthread_key_delete - found
-- Looking for pthread_rwlock_rdlock
-- Looking for pthread_rwlock_rdlock - found
-- Looking for pthread_sigmask
-- Looking for pthread_sigmask - found
-- Looking for pthread_yield_np
-- Looking for pthread_yield_np - not found
-- Looking for putenv
-- Looking for putenv - found
-- Looking for readlink
-- Looking for readlink - found
-- Looking for realpath
-- Looking for realpath - found
-- Looking for rename
-- Looking for rename - found
-- Looking for rwlock_init
-- Looking for rwlock_init - not found
-- Looking for sched_yield
-- Looking for sched_yield - found
-- Looking for setenv
-- Looking for setenv - found
-- Looking for setlocale
-- Looking for setlocale - found
-- Looking for sigaction
-- Looking for sigaction - found
-- Looking for sigthreadmask
-- Looking for sigthreadmask - not found
-- Looking for sigwait
-- Looking for sigwait - found
-- Looking for sigwaitinfo
-- Looking for sigwaitinfo - found
-- Looking for sigset
-- Looking for sigset - found
-- Looking for sleep
-- Looking for sleep - found
-- Looking for snprintf
-- Looking for snprintf - found
-- Looking for stpcpy
-- Looking for stpcpy - found
-- Looking for strcoll
-- Looking for strcoll - found
-- Looking for strerror
-- Looking for strerror - found
-- Looking for strnlen
-- Looking for strnlen - found
-- Looking for strpbrk
-- Looking for strpbrk - found
-- Looking for strtok_r
-- Looking for strtok_r - found
-- Looking for strtoll
-- Looking for strtoll - found
-- Looking for strtoul
-- Looking for strtoul - found
-- Looking for strtoull
-- Looking for strtoull - found
-- Looking for strcasecmp
-- Looking for strcasecmp - found
-- Looking for tell
-- Looking for tell - not found
-- Looking for thr_setconcurrency
-- Looking for thr_setconcurrency - not found
-- Looking for thr_yield
-- Looking for thr_yield - not found
-- Looking for vasprintf
-- Looking for vasprintf - found
-- Looking for vsnprintf
-- Looking for vsnprintf - found
-- Looking for memalign
-- Looking for memalign - found
-- Looking for nl_langinfo
-- Looking for nl_langinfo - found
-- Performing Test HAVE_READDIR_R
-- Performing Test HAVE_READDIR_R - Success
-- Looking for include file time.h
-- Looking for include file time.h - found
-- Looking for include file sys/times.h
-- Looking for include file sys/times.h - found
-- Looking for include file ia64intrin.h
-- Looking for include file ia64intrin.h - not found
-- Looking for times
-- Looking for times - found
-- Looking for gettimeofday
-- Looking for gettimeofday - found
-- Looking for read_real_time
-- Looking for read_real_time - not found
-- Looking for ftime
-- Looking for ftime - found
-- Looking for time
-- Looking for time - found
-- Looking for madvise
-- Looking for madvise - found
-- Looking for tzname
-- Looking for tzname - found
-- Looking for lrand48
-- Looking for lrand48 - found
-- Looking for getpagesize
-- Looking for getpagesize - found
-- Looking for TIOCGWINSZ
-- Looking for TIOCGWINSZ - found
-- Looking for FIONREAD
-- Looking for FIONREAD - found
-- Looking for TIOCSTAT
-- Looking for TIOCSTAT - not found
-- Looking for FIONREAD
-- Looking for FIONREAD - not found
-- Check size of sigset_t
-- Check size of sigset_t - done
-- Check size of mode_t
-- Check size of mode_t - done
-- Check size of sighandler_t
-- Check size of sighandler_t - done
-- Check size of in_addr_t
-- Check size of in_addr_t - done
-- Check size of char *
-- Check size of char * - done
-- Check size of long
-- Check size of long - done
-- Check size of size_t
-- Check size of size_t - done
-- Check size of short
-- Check size of short - done
-- Check size of int
-- Check size of int - done
-- Check size of long long
-- Check size of long long - done
-- Check size of off_t
-- Check size of off_t - done
-- Check size of uchar
-- Check size of uchar - failed
-- Check size of uint
-- Check size of uint - done
-- Check size of ulong
-- Check size of ulong - done
-- Check size of int8
-- Check size of int8 - failed
-- Check size of uint8
-- Check size of uint8 - failed
-- Check size of int16
-- Check size of int16 - failed
-- Check size of uint16
-- Check size of uint16 - failed
-- Check size of int32
-- Check size of int32 - failed
-- Check size of uint32
-- Check size of uint32 - failed
-- Check size of int64
-- Check size of int64 - failed
-- Check size of uint64
-- Check size of uint64 - failed
-- Check size of time_t
-- Check size of time_t - done
-- Performing Test TIME_T_UNSIGNED
-- Performing Test TIME_T_UNSIGNED - Failed
-- Performing Test HAVE_SELECT
-- Performing Test HAVE_SELECT - Success
-- Performing Test HAVE_TIMESPEC_TS_SEC
-- Performing Test HAVE_TIMESPEC_TS_SEC - Failed
-- Performing Test QSORT_TYPE_IS_VOID
-- Performing Test QSORT_TYPE_IS_VOID - Success
-- Performing Test HAVE_SOCKET_SIZE_T_AS_socklen_t
-- Performing Test HAVE_SOCKET_SIZE_T_AS_socklen_t - Success
-- Performing Test HAVE_PTHREAD_YIELD_ZERO_ARG
-- Performing Test HAVE_PTHREAD_YIELD_ZERO_ARG - Failed
-- Performing Test SIGNAL_RETURN_TYPE_IS_VOID
-- Performing Test SIGNAL_RETURN_TYPE_IS_VOID - Success
-- Looking for include files time.h, sys/time.h
-- Looking for include files time.h, sys/time.h - found
-- Looking for O_NONBLOCK
-- Looking for O_NONBLOCK - found
-- Performing Test C_HAS_inline
-- Performing Test C_HAS_inline - Success
-- Looking for tcgetattr
-- Looking for tcgetattr - found
-- Performing Test HAVE_POSIX_SIGNALS
-- Performing Test HAVE_POSIX_SIGNALS - Success
-- Performing Test HAVE_ABI_CXA_DEMANGLE
-- Performing Test HAVE_ABI_CXA_DEMANGLE - Success
-- Performing Test HAVE_WEAK_SYMBOL
-- Performing Test HAVE_WEAK_SYMBOL - Success
-- Performing Test HAVE_ATTRIBUTE_CLEANUP
-- Performing Test HAVE_ATTRIBUTE_CLEANUP - Success
-- Performing Test HAVE_CXX_NEW
-- Performing Test HAVE_CXX_NEW - Success
-- Performing Test HAVE_SOLARIS_STYLE_GETHOST
-- Performing Test HAVE_SOLARIS_STYLE_GETHOST - Failed
-- Performing Test HAVE_GCC_C11_ATOMICS_WITHOUT_LIBATOMIC
-- Performing Test HAVE_GCC_C11_ATOMICS_WITHOUT_LIBATOMIC - Success
-- Looking for include files valgrind/memcheck.h, valgrind/valgrind.h
-- Looking for include files valgrind/memcheck.h, valgrind/valgrind.h - not found
-- Looking for netinet/in6.h
-- Looking for netinet/in6.h - not found
-- Check size of struct sockaddr_in6
-- Check size of struct sockaddr_in6 - done
-- Check size of struct in6_addr
-- Check size of struct in6_addr - done
-- Performing Test HAVE_SOCKADDR_STORAGE_SS_FAMILY
-- Performing Test HAVE_SOCKADDR_STORAGE_SS_FAMILY - Success
-- Performing Test HAVE_SOCKADDR_IN_SIN_LEN
-- Performing Test HAVE_SOCKADDR_IN_SIN_LEN - Failed
-- Performing Test HAVE_SOCKADDR_IN6_SIN6_LEN
-- Performing Test HAVE_SOCKADDR_IN6_SIN6_LEN - Failed
-- Performing Test STRUCT_DIRENT_HAS_D_INO
-- Performing Test STRUCT_DIRENT_HAS_D_INO - Success
-- Performing Test STRUCT_DIRENT_HAS_D_NAMLEN
-- Performing Test STRUCT_DIRENT_HAS_D_NAMLEN - Failed
-- Looking for ucontext.h
-- Looking for ucontext.h - found
-- Looking for makecontext
-- Looking for makecontext - not found
-- Performing Test STRUCT_TIMESPEC_HAS_TV_SEC
-- Performing Test STRUCT_TIMESPEC_HAS_TV_SEC - Success
-- Performing Test STRUCT_TIMESPEC_HAS_TV_NSEC
-- Performing Test STRUCT_TIMESPEC_HAS_TV_NSEC - Success
-- Performing Test HAVE_FALLOC_PUNCH_HOLE_AND_KEEP_SIZE
-- Performing Test HAVE_FALLOC_PUNCH_HOLE_AND_KEEP_SIZE - Success
-- Found ZLIB: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libz.so (found version "1.2.11") 
-- Looking for crc32
-- Looking for crc32 - found
-- Looking for compressBound
-- Looking for compressBound - found
-- Looking for deflateBound
-- Looking for deflateBound - found
-- Found OpenSSL: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libcrypto.so (found version "1.1.1k")  
-- OPENSSL_INCLUDE_DIR = /openwrt/staging_dir/target-x86_64_musl/usr/include
-- OPENSSL_SSL_LIBRARY = /openwrt/staging_dir/target-x86_64_musl/usr/lib/libssl.so
-- OPENSSL_CRYPTO_LIBRARY = /openwrt/staging_dir/target-x86_64_musl/usr/lib/libcrypto.so
-- OPENSSL_VERSION = 1.1.1k
-- SSL_LIBRARIES = /openwrt/staging_dir/target-x86_64_musl/usr/lib/libssl.so;/openwrt/staging_dir/target-x86_64_musl/usr/lib/libcrypto.so;dl
-- Looking for ERR_remove_thread_state
-- Looking for ERR_remove_thread_state - found
-- Looking for EVP_aes_128_ctr
-- Looking for EVP_aes_128_ctr - found
-- Looking for EVP_aes_128_gcm
-- Looking for EVP_aes_128_gcm - found
-- Looking for X509_check_host
-- Looking for X509_check_host - found
-- Check size of mbstate_t
-- Check size of mbstate_t - done
-- Looking for mbrlen
-- Looking for mbrlen - found
-- Looking for mbsrtowcs
-- Looking for mbsrtowcs - found
-- Looking for mbrtowc
-- Looking for mbrtowc - found
-- Looking for wcwidth
-- Looking for wcwidth - found
-- Looking for iswlower
-- Looking for iswlower - found
-- Looking for iswupper
-- Looking for iswupper - found
-- Looking for towlower
-- Looking for towlower - found
-- Looking for towupper
-- Looking for towupper - found
-- Looking for iswctype
-- Looking for iswctype - found
-- Check size of wchar_t
-- Check size of wchar_t - done
-- Check size of wctype_t
-- Check size of wctype_t - done
-- Check size of wint_t
-- Check size of wint_t - done
-- Looking for cbreak in /openwrt/staging_dir/target-x86_64_musl/usr/lib/libncurses.so
-- Looking for cbreak in /openwrt/staging_dir/target-x86_64_musl/usr/lib/libncurses.so - found
-- Looking for nodelay in /openwrt/staging_dir/target-x86_64_musl/usr/lib/libncurses.so
-- Looking for nodelay in /openwrt/staging_dir/target-x86_64_musl/usr/lib/libncurses.so - found
-- Found Curses: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libncurses.so  
-- Looking for tputs in /openwrt/staging_dir/target-x86_64_musl/usr/lib/libncurses.so
-- Looking for tputs in /openwrt/staging_dir/target-x86_64_musl/usr/lib/libncurses.so - found
-- Looking for setupterm in /openwrt/staging_dir/target-x86_64_musl/usr/lib/libncurses.so
-- Looking for setupterm in /openwrt/staging_dir/target-x86_64_musl/usr/lib/libncurses.so - found
-- Looking for vidattr in /openwrt/staging_dir/target-x86_64_musl/usr/lib/libncurses.so
-- Looking for vidattr in /openwrt/staging_dir/target-x86_64_musl/usr/lib/libncurses.so - found
-- Performing Test NEW_READLINE_INTERFACE
-- Performing Test NEW_READLINE_INTERFACE - Success
-- Performing Test READLINE_V5
-- Performing Test READLINE_V5 - Failed
-- Performing Test LIBEDIT_HAVE_COMPLETION_INT
-- Performing Test LIBEDIT_HAVE_COMPLETION_INT - Failed
-- Performing Test LIBEDIT_HAVE_COMPLETION_CHAR
-- Performing Test LIBEDIT_HAVE_COMPLETION_CHAR - Success
-- Performing Test HAVE_HIST_ENTRY
-- Performing Test HAVE_HIST_ENTRY - Success
-- Looking for include files curses.h, term.h
-- Looking for include files curses.h, term.h - found
-- Looking for pcre_stack_guard in pcre
-- Looking for pcre_stack_guard in pcre - found
-- Found PkgConfig: /openwrt/staging_dir/host/bin/pkg-config (found version "1.7.3") 
CMake Error at CMakeLists.txt:381 (INCLUDE):
  INCLUDE could not find requested file:

    /openwrt/staging_dir/hostpkg/share/mariadb/import_executables.cmake


-- Performing Test have_C__Wall
-- Performing Test have_C__Wall - Success
-- Performing Test have_CXX__Wall
-- Performing Test have_CXX__Wall - Success
-- Performing Test have_C__Wdeclaration_after_statement
-- Performing Test have_C__Wdeclaration_after_statement - Success
-- Performing Test have_CXX__Wdeclaration_after_statement
-- Performing Test have_CXX__Wdeclaration_after_statement - Failed
-- Performing Test have_C__Wextra
-- Performing Test have_C__Wextra - Success
-- Performing Test have_CXX__Wextra
-- Performing Test have_CXX__Wextra - Success
-- Performing Test have_C__Wformat_security
-- Performing Test have_C__Wformat_security - Success
-- Performing Test have_CXX__Wformat_security
-- Performing Test have_CXX__Wformat_security - Success
-- Performing Test have_C__Wformat_truncation
-- Performing Test have_C__Wformat_truncation - Success
-- Performing Test have_CXX__Wformat_truncation
-- Performing Test have_CXX__Wformat_truncation - Success
-- Performing Test have_C__Winit_self
-- Performing Test have_C__Winit_self - Success
-- Performing Test have_CXX__Winit_self
-- Performing Test have_CXX__Winit_self - Success
-- Performing Test have_C__Wnonnull_compare
-- Performing Test have_C__Wnonnull_compare - Success
-- Performing Test have_CXX__Wnonnull_compare
-- Performing Test have_CXX__Wnonnull_compare - Success
-- Performing Test have_C__Wnull_conversion
-- Performing Test have_C__Wnull_conversion - Failed
-- Performing Test have_CXX__Wnull_conversion
-- Performing Test have_CXX__Wnull_conversion - Failed
-- Performing Test have_C__Wunused_parameter
-- Performing Test have_C__Wunused_parameter - Success
-- Performing Test have_CXX__Wunused_parameter
-- Performing Test have_CXX__Wunused_parameter - Success
-- Performing Test have_C__Wunused_private_field
-- Performing Test have_C__Wunused_private_field - Failed
-- Performing Test have_CXX__Wunused_private_field
-- Performing Test have_CXX__Wunused_private_field - Failed
-- Performing Test have_C__Woverloaded_virtual
-- Performing Test have_C__Woverloaded_virtual - Failed
-- Performing Test have_CXX__Woverloaded_virtual
-- Performing Test have_CXX__Woverloaded_virtual - Success
-- Performing Test have_C__Wnon_virtual_dtor
-- Performing Test have_C__Wnon_virtual_dtor - Failed
-- Performing Test have_CXX__Wnon_virtual_dtor
-- Performing Test have_CXX__Wnon_virtual_dtor - Success
-- Performing Test have_C__Wvla
-- Performing Test have_C__Wvla - Success
-- Performing Test have_CXX__Wvla
-- Performing Test have_CXX__Wvla - Success
-- Performing Test have_C__Wwrite_strings
-- Performing Test have_C__Wwrite_strings - Success
-- Performing Test have_CXX__Wwrite_strings
-- Performing Test have_CXX__Wwrite_strings - Success
-- Performing Test have_CXX__Werror
-- Performing Test have_CXX__Werror - Success
== Configuring MariaDB Connector/C
CMake Deprecation Warning at libmariadb/CMakeLists.txt:5 (CMAKE_MINIMUM_REQUIRED):
  Compatibility with CMake < 2.8.12 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- Could NOT find CURL (missing: CURL_LIBRARY CURL_INCLUDE_DIR) 
-- Performing Test HAS_-Wunused_FLAG
-- Performing Test HAS_-Wunused_FLAG - Success
-- Performing Test HAS_-Wlogical-op_FLAG
-- Performing Test HAS_-Wlogical-op_FLAG - Success
-- Performing Test HAS_-Wno-uninitialized_FLAG
-- Performing Test HAS_-Wno-uninitialized_FLAG - Success
-- Performing Test HAS_-Wall_FLAG
-- Performing Test HAS_-Wall_FLAG - Success
-- Performing Test HAS_-Wextra_FLAG
-- Performing Test HAS_-Wextra_FLAG - Success
-- Performing Test HAS_-Wformat-security_FLAG
-- Performing Test HAS_-Wformat-security_FLAG - Success
-- Performing Test HAS_-Wno-init-self_FLAG
-- Performing Test HAS_-Wno-init-self_FLAG - Success
-- Performing Test HAS_-Wwrite-strings_FLAG
-- Performing Test HAS_-Wwrite-strings_FLAG - Success
-- Performing Test HAS_-Wshift-count-overflow_FLAG
-- Performing Test HAS_-Wshift-count-overflow_FLAG - Success
-- Performing Test HAS_-Wdeclaration-after-statement_FLAG
-- Performing Test HAS_-Wdeclaration-after-statement_FLAG - Success
-- Performing Test HAS_-Wno-undef_FLAG
-- Performing Test HAS_-Wno-undef_FLAG - Success
-- Performing Test HAS_-Wno-unknown-pragmas_FLAG
-- Performing Test HAS_-Wno-unknown-pragmas_FLAG - Success
-- MariaDB Connector C: INSTALL_BINDIR=bin
-- MariaDB Connector C: INSTALL_LIBDIR=lib
-- MariaDB Connector C: INSTALL_PCDIR=lib/pkgconfig
-- MariaDB Connector C: INSTALL_INCLUDEDIR=include/mysql
-- MariaDB Connector C: INSTALL_DOCSDIR=
-- MariaDB Connector C: INSTALL_PLUGINDIR=lib/mariadb/plugin
-- MariaDB Connector C: LIBMARIADB_STATIC_NAME mariadbclient
-- Looking for include file linux/limits.h
-- Looking for include file linux/limits.h - found
-- Looking for include file signal.h
-- Looking for include file signal.h - found
-- Check size of socklen_t
-- Check size of socklen_t - failed
-- Looking for floor
-- Looking for floor - found
-- Looking for pthread_getspecific
-- Looking for pthread_getspecific - found
-- Looking for gethostbyname_r
-- Looking for gethostbyname_r - found
-- Looking for setsockopt
-- Looking for setsockopt - found
-- TLS library/version: OpenSSL 1.1.1k
-- SYSTEM_LIBS dl;dl;/openwrt/staging_dir/target-x86_64_musl/usr/lib/libssl.so;/openwrt/staging_dir/target-x86_64_musl/usr/lib/libcrypto.so
-- Found GSSAPI: -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro -lgssapi_krb5 -lkrb5 -lk5crypto -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lcom_err
-- SYSTEM processor: x86_64
CMake Error at libmariadb/cmake/ConnectorName.cmake:30 (ENDMACRO):
  Flow control statements are not properly nested.
Call Stack (most recent call first):
  libmariadb/CMakeLists.txt:423 (INCLUDE)


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-x86_64_musl/mariadb-10.4.18/CMakeFiles/CMakeOutput.log".
See also "/openwrt/build_dir/target-x86_64_musl/mariadb-10.4.18/CMakeFiles/CMakeError.log".
make[3]: *** [Makefile:579: /openwrt/build_dir/target-x86_64_musl/mariadb-10.4.18/.configured_bed93ddeaf8a5aadb5e8c392a97cdb2c] Error 1
```
