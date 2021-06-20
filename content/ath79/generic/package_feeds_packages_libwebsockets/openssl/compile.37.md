---
title: "compile.37"
date: 2021-06-20 22:38:00.058560
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
make package/feeds/packages/libwebsockets/compile -j$(nproc) || make package/feeds/packages/libwebsockets/compile V=s
```

#### Compile.txt

``` bash
-- The C compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Compiled with LWS_WITH_DIR and LWS_WITH_LEJP_CONF
-- Found Git: /openwrt/staging_dir/host/bin/git (found version "2.25.1") 
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
Git commit hash: 
-- Performing Test LWS_HAVE_inline
-- Performing Test LWS_HAVE_inline - Success
-- Performing Test LWS_HAVE___inline__
-- Performing Test LWS_HAVE___inline__ - Success
-- Performing Test LWS_HAVE___inline
-- Performing Test LWS_HAVE___inline - Success
-- Performing Test LWS_HAVE_MALLOC_TRIM
-- Performing Test LWS_HAVE_MALLOC_TRIM - Failed
-- Performing Test LWS_HAVE_MALLOC_USABLE_SIZE
-- Performing Test LWS_HAVE_MALLOC_USABLE_SIZE - Success
-- Looking for fork
-- Looking for fork - found
-- Looking for getenv
-- Looking for getenv - found
-- Looking for malloc
-- Looking for malloc - found
-- Looking for memset
-- Looking for memset - found
-- Looking for realloc
-- Looking for realloc - found
-- Looking for socket
-- Looking for socket - found
-- Looking for strerror
-- Looking for strerror - found
-- Looking for vfork
-- Looking for vfork - found
-- Looking for execvpe
-- Looking for execvpe - found
-- Looking for getifaddrs
-- Looking for getifaddrs - found
-- Looking for snprintf
-- Looking for snprintf - found
-- Looking for _snprintf
-- Looking for _snprintf - not found
-- Looking for _vsnprintf
-- Looking for _vsnprintf - not found
-- Looking for getloadavg
-- Looking for getloadavg - found
-- Looking for atoll
-- Looking for atoll - found
-- Looking for _atoi64
-- Looking for _atoi64 - not found
-- Looking for _stat32i64
-- Looking for _stat32i64 - not found
-- Looking for clock_gettime
-- Looking for clock_gettime - found
-- Looking for in6addr.h
-- Looking for in6addr.h - not found
-- Looking for memory.h
-- Looking for memory.h - found
-- Looking for netinet/in.h
-- Looking for netinet/in.h - found
-- Looking for stdint.h
-- Looking for stdint.h - found
-- Looking for stdlib.h
-- Looking for stdlib.h - found
-- Looking for strings.h
-- Looking for strings.h - found
-- Looking for string.h
-- Looking for string.h - found
-- Looking for sys/prctl.h
-- Looking for sys/prctl.h - found
-- Looking for sys/socket.h
-- Looking for sys/socket.h - found
-- Looking for sys/sockio.h
-- Looking for sys/sockio.h - not found
-- Looking for sys/stat.h
-- Looking for sys/stat.h - found
-- Looking for sys/types.h
-- Looking for sys/types.h - found
-- Looking for unistd.h
-- Looking for unistd.h - found
-- Looking for vfork.h
-- Looking for vfork.h - not found
-- Looking for sys/capability.h
-- Looking for sys/capability.h - found
-- Looking for malloc.h
-- Looking for malloc.h - found
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for inttypes.h
-- Looking for inttypes.h - found
-- Looking for sys/resource.h
-- Looking for sys/resource.h - found
-- Looking for cap_set_flag in cap
-- Looking for cap_set_flag in cap - found
-- Looking for 3 include files stdlib.h, ..., string.h
-- Looking for 3 include files stdlib.h, ..., string.h - found
-- Performing Test LWS_HAS_INTPTR_T
-- Performing Test LWS_HAS_INTPTR_T - Success
-- Performing Test LWS_HAS_PTHREAD_SETNAME_NP
-- Performing Test LWS_HAS_PTHREAD_SETNAME_NP - Success
-- Performing Test LWS_HAS_GETOPT_LONG
-- Performing Test LWS_HAS_GETOPT_LONG - Success
-- Performing Test LWS_HAVE_VISIBILITY
-- Performing Test LWS_HAVE_VISIBILITY - Success
-- Performing Test LWS_GCC_HAS_IGNORED_QUALIFIERS
-- Performing Test LWS_GCC_HAS_IGNORED_QUALIFIERS - Success
-- Performing Test LWS_GCC_HAS_TYPE_LIMITS
-- Performing Test LWS_GCC_HAS_TYPE_LIMITS - Success
-- Looking for eventfd_read
-- Looking for eventfd_read - found
-- Performing Test LWS_HAVE_PIPE2
-- Performing Test LWS_HAVE_PIPE2 - Success
-- Performing Test LWS_HAVE_TCP_USER_TIMEOUT
-- Performing Test LWS_HAVE_TCP_USER_TIMEOUT - Success
Compiling with SSL support
CMake Error at /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindPackageHandleStandardArgs.cmake:218 (message):
  Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the
  system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY
  OPENSSL_INCLUDE_DIR)
Call Stack (most recent call first):
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindPackageHandleStandardArgs.cmake:577 (_FPHSA_FAILURE_MESSAGE)
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindOpenSSL.cmake:536 (find_package_handle_standard_args)
  lib/tls/CMakeLists.txt:238 (find_package)


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-mips_24kc_musl/libwebsockets-openssl/libwebsockets-4.1.6/CMakeFiles/CMakeOutput.log".
See also "/openwrt/build_dir/target-mips_24kc_musl/libwebsockets-openssl/libwebsockets-4.1.6/CMakeFiles/CMakeError.log".
make[3]: *** [Makefile:109: /openwrt/build_dir/target-mips_24kc_musl/libwebsockets-openssl/libwebsockets-4.1.6/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
