---
title: "compile.41"
date: 2021-06-23 23:22:46.140442
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
make package/feeds/packages/libmariadb/compile -j$(nproc) || make package/feeds/packages/libmariadb/compile V=s
```

#### Compile.txt

``` bash
CMake Deprecation Warning at CMakeLists.txt:5 (CMAKE_MINIMUM_REQUIRED):
  Compatibility with CMake < 2.8.12 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- The C compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/bin/x86_64-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Found CURL: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libcurl.so (found version "7.77.0")  
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
-- Found Git: /openwrt/staging_dir/host/bin/git (found version "2.25.1") 
-- MariaDB Connector C: INSTALL_BINDIR=bin
-- MariaDB Connector C: INSTALL_LIBDIR=lib
-- MariaDB Connector C: INSTALL_PCDIR=lib/pkgconfig
-- MariaDB Connector C: INSTALL_INCLUDEDIR=include/mysql
-- MariaDB Connector C: INSTALL_DOCSDIR=
-- MariaDB Connector C: INSTALL_PLUGINDIR=lib/mariadb/plugin
-- MariaDB Connector C: LIBMARIADB_STATIC_NAME mariadbclient
-- Found ZLIB: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libz.so (found version "1.2.11") 
-- Looking for include file alloca.h
-- Looking for include file alloca.h - found
-- Looking for include file arpa/inet.h
-- Looking for include file arpa/inet.h - found
-- Looking for include file dlfcn.h
-- Looking for include file dlfcn.h - found
-- Looking for include file fcntl.h
-- Looking for include file fcntl.h - found
-- Looking for include file float.h
-- Looking for include file float.h - found
-- Looking for include file limits.h
-- Looking for include file limits.h - found
-- Looking for include file linux/limits.h
-- Looking for include file linux/limits.h - found
-- Looking for include file pwd.h
-- Looking for include file pwd.h - found
-- Looking for include file sched.h
-- Looking for include file sched.h - found
-- Looking for include file select.h
-- Looking for include file select.h - not found
-- Looking for include file signal.h
-- Looking for include file signal.h - found
-- Looking for include file stddef.h
-- Looking for include file stddef.h - found
-- Looking for include file stdint.h
-- Looking for include file stdint.h - found
-- Looking for include file stdlib.h
-- Looking for include file stdlib.h - found
-- Looking for include file string.h
-- Looking for include file string.h - found
-- Looking for include file strings.h
-- Looking for include file strings.h - found
-- Looking for include file sys/ioctl.h
-- Looking for include file sys/ioctl.h - found
-- Looking for include file sys/select.h
-- Looking for include file sys/select.h - found
-- Looking for include file sys/socket.h
-- Looking for include file sys/socket.h - found
-- Looking for include file sys/types.h
-- Looking for include file sys/types.h - found
-- Looking for include file sys/stat.h
-- Looking for include file sys/stat.h - found
-- Looking for include file sys/un.h
-- Looking for include file sys/un.h - found
-- Looking for include file unistd.h
-- Looking for include file unistd.h - found
-- Looking for include file utime.h
-- Looking for include file utime.h - found
-- Looking for include file ucontext.h
-- Looking for include file ucontext.h - found
-- Looking for alloca
-- Looking for alloca - not found
-- Looking for dlerror
-- Looking for dlerror - found
-- Looking for dlopen
-- Looking for dlopen - found
-- Looking for fcntl
-- Looking for fcntl - found
-- Looking for memcpy
-- Looking for memcpy - found
-- Looking for nl_langinfo
-- Looking for nl_langinfo - found
-- Looking for setlocale
-- Looking for setlocale - found
-- Looking for poll
-- Looking for poll - found
-- Looking for getpwuid
-- Looking for getpwuid - found
-- Looking for makecontext
-- Looking for makecontext - not found
-- Looking for cuserid
-- Looking for cuserid - found
-- Check size of char *
-- Check size of char * - done
-- Check size of int
-- Check size of int - done
-- Check size of long
-- Check size of long - done
-- Check size of long long
-- Check size of long long - done
-- Check size of size_t
-- Check size of size_t - done
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
-- Check size of socklen_t
-- Check size of socklen_t - failed
-- Performing Test SOCKET_SIZE_FOUND_socklen_t
-- Performing Test SOCKET_SIZE_FOUND_socklen_t - Success
-- Looking for floor
-- Looking for floor - found
-- Looking for pthread_getspecific
-- Looking for pthread_getspecific - found
-- Looking for gethostbyname_r
-- Looking for gethostbyname_r - found
-- Looking for setsockopt
-- Looking for setsockopt - found
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
-- Found OpenSSL: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libcrypto.so (found version "1.1.1k")  
-- TLS library/version: OpenSSL 1.1.1k
-- SYSTEM_LIBS /openwrt/staging_dir/target-x86_64_musl/usr/lib/libz.so;dl;dl;/openwrt/staging_dir/target-x86_64_musl/usr/lib/libssl.so;/openwrt/staging_dir/target-x86_64_musl/usr/lib/libcrypto.so
-- Found GSSAPI: -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro -lgssapi_krb5 -lkrb5 -lk5crypto -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lcom_err
-- Dynamic column API support: ON
-- SYSTEM processor: x86_64
CMake Error at cmake/ConnectorName.cmake:30 (ENDMACRO):
  Flow control statements are not properly nested.
Call Stack (most recent call first):
  CMakeLists.txt:423 (INCLUDE)


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-x86_64_musl/mariadb-connector-c-3.1.12-src/CMakeFiles/CMakeOutput.log".
See also "/openwrt/build_dir/target-x86_64_musl/mariadb-connector-c-3.1.12-src/CMakeFiles/CMakeError.log".
make[3]: *** [Makefile:185: /openwrt/build_dir/target-x86_64_musl/mariadb-connector-c-3.1.12-src/.configured_41dbb0eecaaedfbdf68b832f245272a3] Error 1
```
