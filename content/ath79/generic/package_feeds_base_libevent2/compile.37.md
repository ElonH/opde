---
title: "compile.37"
date: 2021-06-20 22:39:07.383506
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
make package/feeds/base/libevent2/compile -j$(nproc) || make package/feeds/base/libevent2/compile V=s
```

#### Compile.txt

``` bash
-- The C compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Found Git: /openwrt/staging_dir/host/bin/git (found version "2.25.1") 
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
-- Performing Test check_c_compiler_flag__fdiagnostics_color_always
-- Performing Test check_c_compiler_flag__fdiagnostics_color_always - Success
-- Performing Test check_c_compiler_flag__Wall
-- Performing Test check_c_compiler_flag__Wall - Success
-- Performing Test check_c_compiler_flag__Wextra
-- Performing Test check_c_compiler_flag__Wextra - Success
-- Performing Test check_c_compiler_flag__Wno_unused_parameter
-- Performing Test check_c_compiler_flag__Wno_unused_parameter - Success
-- Performing Test check_c_compiler_flag__Wstrict_aliasing
-- Performing Test check_c_compiler_flag__Wstrict_aliasing - Success
-- Performing Test check_c_compiler_flag__Wstrict_prototypes
-- Performing Test check_c_compiler_flag__Wstrict_prototypes - Success
-- Performing Test check_c_compiler_flag__fno_strict_aliasing
-- Performing Test check_c_compiler_flag__fno_strict_aliasing - Success
-- Performing Test check_c_compiler_flag__Wmissing_prototypes
-- Performing Test check_c_compiler_flag__Wmissing_prototypes - Success
-- Performing Test check_c_compiler_flag__Winit_self
-- Performing Test check_c_compiler_flag__Winit_self - Success
-- Performing Test check_c_compiler_flag__Wmissing_field_initializers
-- Performing Test check_c_compiler_flag__Wmissing_field_initializers - Success
-- Performing Test check_c_compiler_flag__Wdeclaration_after_statement
-- Performing Test check_c_compiler_flag__Wdeclaration_after_statement - Success
-- Performing Test check_c_compiler_flag__Waddress
-- Performing Test check_c_compiler_flag__Waddress - Success
-- Performing Test check_c_compiler_flag__Wnormalized_id
-- Performing Test check_c_compiler_flag__Wnormalized_id - Success
-- Performing Test check_c_compiler_flag__Woverride_init
-- Performing Test check_c_compiler_flag__Woverride_init - Success
-- Performing Test check_c_compiler_flag__Wlogical_op
-- Performing Test check_c_compiler_flag__Wlogical_op - Success
-- Performing Test check_c_compiler_flag__Wwrite_strings
-- Performing Test check_c_compiler_flag__Wwrite_strings - Success
-- Looking for __GNU_LIBRARY__
-- Looking for __GNU_LIBRARY__ - not found
-- Looking for _GNU_SOURCE
-- Looking for _GNU_SOURCE - not found
-- Looking for include file fcntl.h
-- Looking for include file fcntl.h - found
-- Looking for include files fcntl.h, inttypes.h
-- Looking for include files fcntl.h, inttypes.h - found
-- Looking for 3 include files fcntl.h, ..., memory.h
-- Looking for 3 include files fcntl.h, ..., memory.h - found
-- Looking for 4 include files fcntl.h, ..., signal.h
-- Looking for 4 include files fcntl.h, ..., signal.h - found
-- Looking for 5 include files fcntl.h, ..., stdarg.h
-- Looking for 5 include files fcntl.h, ..., stdarg.h - found
-- Looking for 6 include files fcntl.h, ..., stddef.h
-- Looking for 6 include files fcntl.h, ..., stddef.h - found
-- Looking for 7 include files fcntl.h, ..., stdint.h
-- Looking for 7 include files fcntl.h, ..., stdint.h - found
-- Looking for 8 include files fcntl.h, ..., stdlib.h
-- Looking for 8 include files fcntl.h, ..., stdlib.h - found
-- Looking for 9 include files fcntl.h, ..., string.h
-- Looking for 9 include files fcntl.h, ..., string.h - found
-- Looking for 10 include files fcntl.h, ..., errno.h
-- Looking for 10 include files fcntl.h, ..., errno.h - found
-- Looking for 11 include files fcntl.h, ..., unistd.h
-- Looking for 11 include files fcntl.h, ..., unistd.h - found
-- Looking for 12 include files fcntl.h, ..., time.h
-- Looking for 12 include files fcntl.h, ..., time.h - found
-- Looking for 13 include files fcntl.h, ..., sys/types.h
-- Looking for 13 include files fcntl.h, ..., sys/types.h - found
-- Looking for 14 include files fcntl.h, ..., sys/stat.h
-- Looking for 14 include files fcntl.h, ..., sys/stat.h - found
-- Looking for 15 include files fcntl.h, ..., sys/time.h
-- Looking for 15 include files fcntl.h, ..., sys/time.h - found
-- Looking for 16 include files fcntl.h, ..., sys/param.h
-- Looking for 16 include files fcntl.h, ..., sys/param.h - found
-- Looking for 17 include files fcntl.h, ..., netdb.h
-- Looking for 17 include files fcntl.h, ..., netdb.h - found
-- Looking for 18 include files fcntl.h, ..., dlfcn.h
-- Looking for 18 include files fcntl.h, ..., dlfcn.h - found
-- Looking for 19 include files fcntl.h, ..., arpa/inet.h
-- Looking for 19 include files fcntl.h, ..., arpa/inet.h - found
-- Looking for 20 include files fcntl.h, ..., poll.h
-- Looking for 20 include files fcntl.h, ..., poll.h - found
-- Looking for 21 include files fcntl.h, ..., port.h
-- Looking for 21 include files fcntl.h, ..., port.h - not found
-- Looking for 21 include files fcntl.h, ..., sys/socket.h
-- Looking for 21 include files fcntl.h, ..., sys/socket.h - found
-- Looking for 22 include files fcntl.h, ..., sys/random.h
-- Looking for 22 include files fcntl.h, ..., sys/random.h - found
-- Looking for 23 include files fcntl.h, ..., sys/un.h
-- Looking for 23 include files fcntl.h, ..., sys/un.h - found
-- Looking for 24 include files fcntl.h, ..., sys/devpoll.h
-- Looking for 24 include files fcntl.h, ..., sys/devpoll.h - not found
-- Looking for 24 include files fcntl.h, ..., sys/epoll.h
-- Looking for 24 include files fcntl.h, ..., sys/epoll.h - found
-- Looking for 25 include files fcntl.h, ..., sys/eventfd.h
-- Looking for 25 include files fcntl.h, ..., sys/eventfd.h - found
-- Looking for 26 include files fcntl.h, ..., sys/event.h
-- Looking for 26 include files fcntl.h, ..., sys/event.h - not found
-- Looking for 26 include files fcntl.h, ..., sys/ioctl.h
-- Looking for 26 include files fcntl.h, ..., sys/ioctl.h - found
-- Looking for 27 include files fcntl.h, ..., sys/mman.h
-- Looking for 27 include files fcntl.h, ..., sys/mman.h - found
-- Looking for 28 include files fcntl.h, ..., sys/queue.h
-- Looking for 28 include files fcntl.h, ..., sys/queue.h - found
-- Looking for 29 include files fcntl.h, ..., sys/select.h
-- Looking for 29 include files fcntl.h, ..., sys/select.h - found
-- Looking for 30 include files fcntl.h, ..., sys/sendfile.h
-- Looking for 30 include files fcntl.h, ..., sys/sendfile.h - found
-- Looking for 31 include files fcntl.h, ..., sys/uio.h
-- Looking for 31 include files fcntl.h, ..., sys/uio.h - found
-- Looking for 32 include files fcntl.h, ..., sys/wait.h
-- Looking for 32 include files fcntl.h, ..., sys/wait.h - found
-- Looking for 33 include files fcntl.h, ..., sys/resource.h
-- Looking for 33 include files fcntl.h, ..., sys/resource.h - found
-- Looking for 34 include files fcntl.h, ..., sys/timerfd.h
-- Looking for 34 include files fcntl.h, ..., sys/timerfd.h - found
-- Looking for 35 include files fcntl.h, ..., netinet/in.h
-- Looking for 35 include files fcntl.h, ..., netinet/in.h - found
-- Looking for 36 include files fcntl.h, ..., netinet/in6.h
-- Looking for 36 include files fcntl.h, ..., netinet/in6.h - not found
-- Looking for 36 include files fcntl.h, ..., netinet/tcp.h
-- Looking for 36 include files fcntl.h, ..., netinet/tcp.h - found
-- Looking for 37 include files fcntl.h, ..., ifaddrs.h
-- Looking for 37 include files fcntl.h, ..., ifaddrs.h - found
-- Looking for getaddrinfo
-- Looking for getaddrinfo - found
-- Looking for getnameinfo
-- Looking for getnameinfo - found
-- Looking for getprotobynumber
-- Looking for getprotobynumber - found
-- Looking for getservbyname
-- Looking for getservbyname - found
-- Looking for gethostbyname
-- Looking for gethostbyname - found
-- Looking for inet_ntop
-- Looking for inet_ntop - found
-- Looking for inet_pton
-- Looking for inet_pton - found
-- Looking for gettimeofday
-- Looking for gettimeofday - found
-- Looking for signal
-- Looking for signal - found
-- Looking for strtoll
-- Looking for strtoll - found
-- Looking for splice
-- Looking for splice - not found
-- Looking for strlcpy
-- Looking for strlcpy - found
-- Looking for strsep
-- Looking for strsep - found
-- Looking for strtok_r
-- Looking for strtok_r - found
-- Looking for vasprintf
-- Looking for vasprintf - found
-- Looking for timerclear
-- Looking for timerclear - found
-- Looking for timercmp
-- Looking for timercmp - found
-- Looking for timerisset
-- Looking for timerisset - found
-- Looking for timeradd
-- Looking for timeradd - found
-- Looking for nanosleep
-- Looking for nanosleep - found
-- Looking for putenv
-- Looking for putenv - found
-- Looking for umask
-- Looking for umask - found
-- Looking for clock_gettime
-- Looking for clock_gettime - found
-- Looking for getifaddrs
-- Looking for getifaddrs - found
-- Looking for select
-- Looking for select - found
-- Looking for epoll_create
-- Looking for epoll_create - found
-- Looking for epoll_create1
-- Looking for epoll_create1 - found
-- Looking for epoll_ctl
-- Looking for epoll_ctl - found
-- Looking for eventfd
-- Looking for eventfd - found
-- Looking for poll
-- Looking for poll - found
-- Looking for port_create
-- Looking for port_create - not found
-- Looking for kqueue
-- Looking for kqueue - not found
-- Looking for fcntl
-- Looking for fcntl - found
-- Looking for mmap
-- Looking for mmap - found
-- Looking for pipe
-- Looking for pipe - found
-- Looking for pipe2
-- Looking for pipe2 - found
-- Looking for sendfile
-- Looking for sendfile - found
-- Looking for sigaction
-- Looking for sigaction - found
-- Looking for strsignal
-- Looking for strsignal - found
-- Looking for sysctl
-- Looking for sysctl - not found
-- Looking for accept4
-- Looking for accept4 - found
-- Looking for arc4random
-- Looking for arc4random - not found
-- Looking for arc4random_buf
-- Looking for arc4random_buf - not found
-- Looking for arc4random_addrandom
-- Looking for arc4random_addrandom - not found
-- Looking for getrandom
-- Looking for getrandom - found
-- Looking for getegid
-- Looking for getegid - found
-- Looking for geteuid
-- Looking for geteuid - found
-- Looking for issetugid
-- Looking for issetugid - found
-- Looking for usleep
-- Looking for usleep - found
-- Looking for timerfd_create
-- Looking for timerfd_create - found
-- Looking for setenv
-- Looking for setenv - found
-- Looking for unsetenv
-- Looking for unsetenv - found
-- Looking for setrlimit
-- Looking for setrlimit - found
-- Looking for gethostbyname_r
-- Looking for gethostbyname_r - found
-- Checking prototype gethostbyname_r for EVENT__HAVE_GETHOSTBYNAME_R_3_ARG - False
-- Checking prototype gethostbyname_r for EVENT__HAVE_GETHOSTBYNAME_R_5_ARG - False
-- Checking prototype gethostbyname_r for EVENT__HAVE_GETHOSTBYNAME_R_6_ARG - True
-- Looking for sys/types.h
-- Looking for sys/types.h - found
-- Looking for stdint.h
-- Looking for stdint.h - found
-- Looking for stddef.h
-- Looking for stddef.h - found
-- Check size of struct sockaddr_un
-- Check size of struct sockaddr_un - done
-- Check size of uint8_t
-- Check size of uint8_t - done
-- Check size of uint16_t
-- Check size of uint16_t - done
-- Check size of uint32_t
-- Check size of uint32_t - done
-- Check size of uint64_t
-- Check size of uint64_t - done
-- Check size of short
-- Check size of short - done
-- Check size of int
-- Check size of int - done
-- Check size of unsigned
-- Check size of unsigned - done
-- Check size of unsigned int
-- Check size of unsigned int - done
-- Check size of long
-- Check size of long - done
-- Check size of long long
-- Check size of long long - done
-- Performing Test HAVE_INLINE
-- Performing Test HAVE_INLINE - Success
-- Looking for __func__
-- Looking for __func__ - found
-- Looking for __FUNCTION__
-- Looking for __FUNCTION__ - found
-- Looking for TAILQ_FOREACH
-- Looking for TAILQ_FOREACH - found
-- Performing Test EVENT__HAVE_DECL_CTL_KERN
-- Performing Test EVENT__HAVE_DECL_CTL_KERN - Failed
-- Looking for CTL_KERN - not found
-- Performing Test EVENT__HAVE_DECL_KERN_ARND
-- Performing Test EVENT__HAVE_DECL_KERN_ARND - Failed
-- Looking for KERN_ARND - not found
-- Looking for F_SETFD
-- Looking for F_SETFD - found
-- Check size of fd_mask
-- Check size of fd_mask - done
-- Check size of size_t
-- Check size of size_t - done
-- Check size of off_t
-- Check size of off_t - done
-- Check size of ssize_t
-- Check size of ssize_t - done
-- Check size of SSIZE_T
-- Check size of SSIZE_T - failed
-- Check size of socklen_t
-- Check size of socklen_t - done
-- Check size of pid_t
-- Check size of pid_t - done
-- Check size of pthread_t
-- Check size of pthread_t - done
-- Check size of uintptr_t
-- Check size of uintptr_t - done
-- Check size of void *
-- Check size of void * - done
-- Check size of time_t
-- Check size of time_t - done
-- Check size of struct addrinfo
-- Check size of struct addrinfo - done
-- Check size of struct in6_addr
-- Check size of struct in6_addr - done
-- Performing Test EVENT__HAVE_STRUCT_IN6_ADDR_S6_ADDR16
-- Performing Test EVENT__HAVE_STRUCT_IN6_ADDR_S6_ADDR16 - Success
-- Performing Test EVENT__HAVE_STRUCT_IN6_ADDR_S6_ADDR32
-- Performing Test EVENT__HAVE_STRUCT_IN6_ADDR_S6_ADDR32 - Success
-- Check size of sa_family_t
-- Check size of sa_family_t - done
-- Check size of struct sockaddr_in6
-- Check size of struct sockaddr_in6 - done
-- Performing Test EVENT__HAVE_STRUCT_SOCKADDR_IN6_SIN6_LEN
-- Performing Test EVENT__HAVE_STRUCT_SOCKADDR_IN6_SIN6_LEN - Failed
-- Performing Test EVENT__HAVE_STRUCT_SOCKADDR_IN_SIN_LEN
-- Performing Test EVENT__HAVE_STRUCT_SOCKADDR_IN_SIN_LEN - Failed
-- Check size of struct sockaddr_storage
-- Check size of struct sockaddr_storage - done
-- Performing Test EVENT__HAVE_STRUCT_SOCKADDR_STORAGE_SS_FAMILY
-- Performing Test EVENT__HAVE_STRUCT_SOCKADDR_STORAGE_SS_FAMILY - Success
-- Performing Test EVENT__HAVE_STRUCT_SOCKADDR_STORAGE___SS_FAMILY
-- Performing Test EVENT__HAVE_STRUCT_SOCKADDR_STORAGE___SS_FAMILY - Failed
-- Check size of struct linger
-- Check size of struct linger - done
CMake Error at /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindPackageHandleStandardArgs.cmake:218 (message):
  Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the
  system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY
  OPENSSL_INCLUDE_DIR)
Call Stack (most recent call first):
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindPackageHandleStandardArgs.cmake:577 (_FPHSA_FAILURE_MESSAGE)
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindOpenSSL.cmake:536 (find_package_handle_standard_args)
  CMakeLists.txt:844 (find_package)


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-mips_24kc_musl/libevent-2.1.12-stable/CMakeFiles/CMakeOutput.log".
See also "/openwrt/build_dir/target-mips_24kc_musl/libevent-2.1.12-stable/CMakeFiles/CMakeError.log".
make[3]: *** [Makefile:164: /openwrt/build_dir/target-mips_24kc_musl/libevent-2.1.12-stable/.configured_69f72ac61b7835edf6e93563707463bd] Error 1
```
