---
title: "compile.40"
date: 2021-06-22 10:37:31.195854
hidden: false
draft: false
weight: -40
---

build number: `40`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/libevhtp/compile -j$(nproc) || make package/feeds/packages/libevhtp/compile V=s
```

#### Compile.txt

``` bash
+ curl -f --connect-timeout 20 --retry 5 --location --insecure https://codeload.github.com/criticalstack/libevhtp/tar.gz/1.2.18?/libevhtp-1.2.18.tar.gz
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100 86068    0 86068    0     0   306k      0 --:--:-- --:--:-- --:--:--  305k
100  203k    0  203k    0     0   585k      0 --:--:-- --:--:-- --:--:--  584k

Applying ./patches/010-openssl-thread.patch using plaintext: 
patching file evhtp.c
-- The C compiler identification is GNU 8.4.0
-- The CXX compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-g++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
CMake Warning (dev) at /openwrt/staging_dir/host/share/cmake-3.20/Modules/FindPackageHandleStandardArgs.cmake:438 (message):
  The package name passed to `find_package_handle_standard_args` (ONIGURUMA)
  does not match the name of the calling package (Oniguruma).  This can lead
  to problems in calling code that expects `find_package` result variables
  (e.g., `_FOUND`) to follow a certain pattern.
Call Stack (most recent call first):
  cmake/FindOniguruma.cmake:26 (FIND_PACKAGE_HANDLE_STANDARD_ARGS)
  cmake/options.cmake:8 (find_package)
  CMakeLists.txt:11 (include)
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Found ONIGURUMA: /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libonig.so  
-- Looking for strndup
-- Looking for strndup - found
-- Looking for strnlen
-- Looking for strnlen - found
-- Looking for include file stdlib.h
-- Looking for include file stdlib.h - found
-- Looking for include file string.h
-- Looking for include file string.h - found
-- Looking for include file stdint.h
-- Looking for include file stdint.h - found
-- Looking for include file errno.h
-- Looking for include file errno.h - found
-- Looking for include file signal.h
-- Looking for include file signal.h - found
-- Looking for include file strings.h
-- Looking for include file strings.h - found
-- Looking for include file inttypes.h
-- Looking for include file inttypes.h - found
-- Looking for include file stdbool.h
-- Looking for include file stdbool.h - found
-- Looking for include file limits.h
-- Looking for include file limits.h - found
-- Looking for include file stddef.h
-- Looking for include file stddef.h - found
-- Looking for include file ctype.h
-- Looking for include file ctype.h - found
-- Looking for include file unistd.h
-- Looking for include file unistd.h - found
-- Looking for include file stdarg.h
-- Looking for include file stdarg.h - found
-- Looking for include file sys/tree.h
-- Looking for include file sys/tree.h - not found
-- Looking for include file sys/queue.h
-- Looking for include file sys/queue.h - found
-- Looking for include file sys/un.h
-- Looking for include file sys/un.h - found
-- Looking for include file sys/types.h
-- Looking for include file sys/types.h - found
-- Check size of int
-- Check size of int - done
-- Check size of long
-- Check size of long - done
-- Check size of short
-- Check size of short - done
-- Check if the system is big endian
-- Searching 16 bit integer
-- Check size of unsigned short
-- Check size of unsigned short - done
-- Using unsigned short
-- Check if the system is big endian - big endian
-- Performing Test has_c99
-- Performing Test has_c99 - Success
-- Performing Test has_stack_protector
-- Performing Test has_stack_protector - Success
CMake Warning (dev) at /openwrt/staging_dir/host/share/cmake-3.20/Modules/FindPackageHandleStandardArgs.cmake:438 (message):
  The package name passed to `find_package_handle_standard_args` (LIBEVENT)
  does not match the name of the calling package (LibEvent).  This can lead
  to problems in calling code that expects `find_package` result variables
  (e.g., `_FOUND`) to follow a certain pattern.
Call Stack (most recent call first):
  cmake/FindLibEvent.cmake:33 (find_package_handle_standard_args)
  CMakeLists.txt:57 (find_package)
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Could NOT find LIBEVENT (missing: LIBEVENT_LIBRARIES LIBEVENT_INCLUDE_DIR) 
-- Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY OPENSSL_INCLUDE_DIR) 
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
CMake Warning (dev) at /openwrt/staging_dir/host/share/cmake-3.20/Modules/FindPackageHandleStandardArgs.cmake:438 (message):
  The package name passed to `find_package_handle_standard_args` (ONIGURUMA)
  does not match the name of the calling package (Oniguruma).  This can lead
  to problems in calling code that expects `find_package` result variables
  (e.g., `_FOUND`) to follow a certain pattern.
Call Stack (most recent call first):
  cmake/FindOniguruma.cmake:26 (FIND_PACKAGE_HANDLE_STANDARD_ARGS)
  CMakeLists.txt:88 (find_package)
This warning is for project developers.  Use -Wno-dev to suppress it.


-- [1;34mEVHTP_VERSION[m            : [1;32m 1.2.18[m
-- [1;34mEVHTP_DISABLE_SSL[m        : [1;32m OFF[m
-- [1;34mEVHTP_DISABLE_EVTHR[m      : [1;32m OFF[m
-- [1;34mEVHTP_DISABLE_REGEX[m      : [1;32m OFF[m
-- [1;34mEVHTP_BUILD_SHARED[m       : [1;32m [m
-- [1;34mEVHTP_USE_JEMALLOC[m       : [1;32m [m
-- [1;34mEVHTP_USE_TCMALLOC[m       : [1;32m [m

-- [34mCMAKE_BUILD_TYPE[m         : [1;31mRelease[m
-- [34mCMAKE_INSTALL_PREFIX[m     : [1;35m/usr[m
-- [34mCMAKE_BINARY_DIR[m         : /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18
-- [34mCMAKE_CURRENT_BINARY_DIR[m : /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18
-- [34mCMAKE_CURRENT_SOURCE_DIR[m : /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18
-- [34mPROJECT_BINARY_DIR[m       : /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18
-- [34mPROJECT_SOURCE_DIR[m       : /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18
-- [34mCMAKE_MODULE_PATH[m        : /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/cmake
-- [34mCMAKE_SYSTEM_NAME[m        : Linux
-- [34mCMAKE_SYSTEM_VERSION[m     : 1
-- [34mCMAKE_C_COMPILER[m         : /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc
-- [34mCMAKE_AR[m                 : /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc-ar
-- [34mCMAKE_RANLIB[m             : /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc-ranlib
-- [34mCFLAGS[m                   :   -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18=libevhtp-1.2.18 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro
                              -DNDEBUG

-- Configuring done
CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
/openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/LIBEVENT_INCLUDE_DIR
   used as include directory in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18
LIBEVENT_CORE
    linked by target "evhtp" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18
    linked by target "example_https_client" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_https_server" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_extensive" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_proxy" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_basic" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_vhost" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_client" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_query" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_perf" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_request_fini" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_chunked" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_pause" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_vhost" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_basic" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
LIBEVENT_EXTRA
    linked by target "evhtp" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18
    linked by target "evhtp" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18
    linked by target "example_https_client" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_https_client" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_https_server" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_https_server" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_extensive" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_extensive" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_proxy" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_proxy" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_basic" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_basic" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_vhost" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_vhost" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_client" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_client" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_query" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_query" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_perf" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_perf" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_request_fini" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_request_fini" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_chunked" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_chunked" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_pause" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_pause" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_vhost" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_vhost" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_basic" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_basic" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
LIBEVENT_LIBRARY
    linked by target "evhtp" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18
    linked by target "example_https_client" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_https_server" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_extensive" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_proxy" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_basic" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_vhost" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_client" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_query" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_perf" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_request_fini" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_chunked" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_pause" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_vhost" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_basic" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
LIBEVENT_SSL
    linked by target "evhtp" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18
    linked by target "example_https_client" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_https_server" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_extensive" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_proxy" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_basic" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_vhost" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_client" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_query" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_perf" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_request_fini" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_chunked" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_pause" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_vhost" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_basic" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
LIBEVENT_THREAD
    linked by target "evhtp" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18
    linked by target "example_https_client" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_https_server" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_extensive" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_proxy" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_basic" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_vhost" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_client" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_query" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "test_perf" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_request_fini" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_chunked" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_pause" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_vhost" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples
    linked by target "example_basic" in directory /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/examples

CMake Error in CMakeLists.txt:
  Target "evhtp" INTERFACE_INCLUDE_DIRECTORIES property contains path:

    "/openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/LIBEVENT_INCLUDE_DIR-NOTFOUND"

  which is prefixed in the build directory.


-- Generating done
CMake Warning:
  Manually-specified variables were not used by the project:

    CMAKE_ASM_COMPILER
    CMAKE_ASM_COMPILER_LAUNCHER
    CMAKE_EXPORT_NO_PACKAGE_REGISTRY
    CMAKE_EXPORT_PACKAGE_REGISTRY
    CMAKE_FIND_PACKAGE_NO_PACKAGE_REGISTRY
    CMAKE_FIND_PACKAGE_NO_SYSTEM_PACKAGE_REGISTRY
    CMAKE_MODULE_LINKER_FLAGS
    CMAKE_SHARED_LINKER_FLAGS
    DL_LIBRARY


CMake Generate step failed.  Build files cannot be regenerated correctly.
make[3]: *** [Makefile:72: /openwrt/build_dir/target-mips_24kc_musl/libevhtp-1.2.18/.configured_0ecca85f0443480392d844226a6c3a25] Error 1
```
