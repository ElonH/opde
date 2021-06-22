---
title: "compile.40"
date: 2021-06-22 10:45:15.529031
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
make package/feeds/packages/h2o/compile -j$(nproc) || make package/feeds/packages/h2o/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/100-socket_disable_npn.patch using plaintext: 
patching file include/h2o/socket.h

Applying ./patches/200-libh2o-evloop_wslay-link.patch using plaintext: 
patching file CMakeLists.txt

Applying ./patches/300-picotls-chacha-detect.patch using plaintext: 
patching file deps/picotls/include/picotls/openssl.h

Applying ./patches/400-backtrace-detection.patch using plaintext: 
patching file CMakeLists.txt
patching file src/main.c

Applying ./patches/500-openssl.patch using plaintext: 
patching file deps/neverbleed/neverbleed.c
patching file deps/picotls/lib/openssl.c
patching file src/main.c
patching file src/ssl.c

Applying ./patches/600-engine.patch using plaintext: 
patching file deps/neverbleed/neverbleed.c
CMake Deprecation Warning at CMakeLists.txt:22 (CMAKE_MINIMUM_REQUIRED):
  Compatibility with CMake < 2.8.12 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


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
-- Found PkgConfig: /openwrt/staging_dir/host/bin/pkg-config (found version "1.7.3") 
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
-- Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY OPENSSL_INCLUDE_DIR) 
-- Found ZLIB: /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libz.so (found version "1.2.11") 
-- Performing Test ARCH_SUPPORTS_64BIT_ATOMICS
-- Performing Test ARCH_SUPPORTS_64BIT_ATOMICS - Failed
-- Performing Test LIBC_HAS_BACKTRACE
-- Performing Test LIBC_HAS_BACKTRACE - Failed
-- Checking for module 'libuv>=1.0.0'
--   Found libuv, version 1.41.0
-- Checking for module 'libwslay'
--   Package 'libwslay', required by 'virtual:world', not found
CMake Warning (dev) at /openwrt/staging_dir/host/share/cmake-3.20/Modules/FindPackageHandleStandardArgs.cmake:438 (message):
  The package name passed to `find_package_handle_standard_args` (WSLAY) does
  not match the name of the calling package (Wslay).  This can lead to
  problems in calling code that expects `find_package` result variables
  (e.g., `_FOUND`) to follow a certain pattern.
Call Stack (most recent call first):
  cmake/FindWslay.cmake:5 (FIND_PACKAGE_HANDLE_STANDARD_ARGS)
  CMakeLists.txt:164 (FIND_PACKAGE)
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Found WSLAY: /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libwslay.a  
-- Configuring done
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
    DL_LIBRARY


-- Build files have been written to: /openwrt/build_dir/target-mips_24kc_musl/h2o-2.2.6
ninja: Entering directory `/openwrt/build_dir/target-mips_24kc_musl/h2o-2.2.6'
ninja: error: 'libressl-build/lib/libssl.a', needed by 'h2o', missing and no known rule to make it
make[3]: *** [Makefile:61: /openwrt/build_dir/target-mips_24kc_musl/h2o-2.2.6/.built] Error 1
```
