---
title: "compile.50"
date: 2021-02-25 14:20:49.081329
hidden: false
draft: false
weight: -50
---

build number: `50`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/libuhttpd/compile -j$(nproc) || make package/feeds/packages/libuhttpd/compile V=s
```

#### Compile.txt

``` bash
-- The C compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/bin/x86_64-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Found Libev: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libev.so (found version "4.31") 
-- Looking for dlopen in dl
-- Looking for dlopen in dl - found
CMake Warning (dev) at /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindPackageHandleStandardArgs.cmake:424 (message):
  The package name passed to `find_package_handle_standard_args` (WOLFSSL)
  does not match the name of the calling package (WolfSSL).  This can lead to
  problems in calling code that expects `find_package` result variables
  (e.g., `_FOUND`) to follow a certain pattern.
Call Stack (most recent call first):
  cmake/Modules/FindWolfSSL.cmake:49 (find_package_handle_standard_args)
  src/CMakeLists.txt:58 (find_package)
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Found WOLFSSL: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libwolfssl.so (found version "4.7.0") 
-- Found MbedTLS: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libmbedtls.so (found version "2.16.9") 
-- Found ZLIB: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libz.so (found version "1.2.11") 
-- Select MbedTLS(PolarSSL) as the SSL backend
-- UHTTPD_VERSION: 3.9.0
-- UHTTPD_SSL_SUPPORT: MbedTLS(PolarSSL)
-- Configuring done
-- Generating done
CMake Warning:
  Manually-specified variables were not used by the project:

    CMAKE_ASM_COMPILER
    CMAKE_ASM_COMPILER_LAUNCHER
    CMAKE_CXX_COMPILER
    CMAKE_CXX_FLAGS_RELEASE
    CMAKE_EXPORT_NO_PACKAGE_REGISTRY
    CMAKE_EXPORT_PACKAGE_REGISTRY
    CMAKE_FIND_PACKAGE_NO_PACKAGE_REGISTRY
    CMAKE_FIND_PACKAGE_NO_SYSTEM_PACKAGE_REGISTRY
    DL_LIBRARY


-- Build files have been written to: /openwrt/build_dir/target-x86_64_musl/libuhttpd-mbedtls/libuhttpd-3.9.0
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/libuhttpd-mbedtls/libuhttpd-3.9.0'
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/libuhttpd-mbedtls/libuhttpd-3.9.0'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/libuhttpd-mbedtls/libuhttpd-3.9.0'
Scanning dependencies of target uhttpd_s
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/libuhttpd-mbedtls/libuhttpd-3.9.0'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/libuhttpd-mbedtls/libuhttpd-3.9.0'
[  3%] Building C object src/CMakeFiles/uhttpd_s.dir/uhttpd.c.o
[  6%] Building C object src/CMakeFiles/uhttpd_s.dir/log.c.o
[  9%] Building C object src/CMakeFiles/uhttpd_s.dir/connection.c.o
[ 12%] Building C object src/CMakeFiles/uhttpd_s.dir/buffer/buffer.c.o
[ 16%] Building C object src/CMakeFiles/uhttpd_s.dir/http-parser/http_parser.c.o
[ 19%] Building C object src/CMakeFiles/uhttpd_s.dir/ssl.c.o
[ 22%] Building C object src/CMakeFiles/uhttpd_s.dir/file.c.o
[ 25%] Building C object src/CMakeFiles/uhttpd_s.dir/mimetypes.c.o
[ 29%] Building C object src/CMakeFiles/uhttpd_s.dir/utils.c.o
[ 32%] Linking C static library libuhttpd.a
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/libuhttpd-mbedtls/libuhttpd-3.9.0'
[ 32%] Built target uhttpd_s
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/libuhttpd-mbedtls/libuhttpd-3.9.0'
Scanning dependencies of target uhttpd
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/libuhttpd-mbedtls/libuhttpd-3.9.0'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/libuhttpd-mbedtls/libuhttpd-3.9.0'
[ 35%] Building C object src/CMakeFiles/uhttpd.dir/uhttpd.c.o
[ 38%] Building C object src/CMakeFiles/uhttpd.dir/log.c.o
[ 41%] Building C object src/CMakeFiles/uhttpd.dir/connection.c.o
[ 45%] Building C object src/CMakeFiles/uhttpd.dir/buffer/buffer.c.o
[ 48%] Building C object src/CMakeFiles/uhttpd.dir/http-parser/http_parser.c.o
[ 51%] Building C object src/CMakeFiles/uhttpd.dir/ssl.c.o
[ 54%] Building C object src/CMakeFiles/uhttpd.dir/file.c.o
[ 58%] Building C object src/CMakeFiles/uhttpd.dir/mimetypes.c.o
[ 61%] Building C object src/CMakeFiles/uhttpd.dir/utils.c.o
[ 64%] Linking C shared library libuhttpd.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/libuhttpd-mbedtls/libuhttpd-3.9.0'
[ 64%] Built target uhttpd
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/libuhttpd-mbedtls/libuhttpd-3.9.0'
Scanning dependencies of target multi_process_server
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/libuhttpd-mbedtls/libuhttpd-3.9.0'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/libuhttpd-mbedtls/libuhttpd-3.9.0'
[ 67%] Building C object example/CMakeFiles/multi_process_server.dir/multi_process_server.c.o
[ 70%] Building C object example/CMakeFiles/multi_process_server.dir/handler.c.o
[ 74%] Linking C executable multi_process_server
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuhttpd.so.3.9.0: undefined reference to `mbedtls_ssl_config_defaults'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuhttpd.so.3.9.0: undefined reference to `mbedtls_ssl_cache_get'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuhttpd.so.3.9.0: undefined reference to `mbedtls_ssl_free'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuhttpd.so.3.9.0: undefined reference to `mbedtls_ssl_config_free'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuhttpd.so.3.9.0: undefined reference to `mbedtls_ssl_setup'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuhttpd.so.3.9.0: undefined reference to `mbedtls_ssl_cache_set'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuhttpd.so.3.9.0: undefined reference to `mbedtls_ssl_cache_free'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuhttpd.so.3.9.0: undefined reference to `mbedtls_ssl_handshake'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuhttpd.so.3.9.0: undefined reference to `mbedtls_ssl_set_bio'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuhttpd.so.3.9.0: undefined reference to `mbedtls_ssl_read'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuhttpd.so.3.9.0: undefined reference to `mbedtls_ssl_conf_rng'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuhttpd.so.3.9.0: undefined reference to `mbedtls_ssl_conf_session_cache'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuhttpd.so.3.9.0: undefined reference to `mbedtls_ssl_cache_init'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuhttpd.so.3.9.0: undefined reference to `mbedtls_ssl_write'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuhttpd.so.3.9.0: undefined reference to `mbedtls_ssl_conf_own_cert'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuhttpd.so.3.9.0: undefined reference to `mbedtls_ssl_conf_ca_chain'
collect2: error: ld returned 1 exit status
make[6]: *** [example/CMakeFiles/multi_process_server.dir/build.make:125: example/multi_process_server] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/libuhttpd-mbedtls/libuhttpd-3.9.0'
make[5]: *** [CMakeFiles/Makefile2:196: example/CMakeFiles/multi_process_server.dir/all] Error 2
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/libuhttpd-mbedtls/libuhttpd-3.9.0'
make[4]: *** [Makefile:149: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/libuhttpd-mbedtls/libuhttpd-3.9.0'
make[3]: *** [Makefile:62: /openwrt/build_dir/target-x86_64_musl/libuhttpd-mbedtls/libuhttpd-3.9.0/.built] Error 2
```
