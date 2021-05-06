---
title: "compile.7"
date: 2021-05-06 04:58:13.022491
hidden: false
draft: false
weight: -7
---

build number: `7`

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
-- Found MbedTLS: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libmbedtls.so (found version "2.16.10") 
-- Found ZLIB: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libz.so (found version "1.2.11") 
-- Select MbedTLS(PolarSSL) as the SSL backend
-- UHTTPD_VERSION: 3.11.0
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


-- Build files have been written to: /openwrt/build_dir/target-x86_64_musl/libuhttpd-mbedtls/libuhttpd-3.11.0
ninja: Entering directory `/openwrt/build_dir/target-x86_64_musl/libuhttpd-mbedtls/libuhttpd-3.11.0/'
[1/32] Building C object src/CMakeFiles/uhttpd_s.dir/log.c.o
[2/32] Building C object src/CMakeFiles/uhttpd_s.dir/buffer/buffer.c.o
[3/32] Building C object src/CMakeFiles/uhttpd_s.dir/http-parser/http_parser.c.o
[4/32] Building C object src/CMakeFiles/uhttpd_s.dir/uhttpd.c.o
[5/32] Building C object src/CMakeFiles/uhttpd_s.dir/file.c.o
[6/32] Building C object src/CMakeFiles/uhttpd_s.dir/mimetypes.c.o
[7/32] Building C object src/CMakeFiles/uhttpd_s.dir/ssl.c.o
[8/32] Building C object src/CMakeFiles/uhttpd_s.dir/connection.c.o
[9/32] Building C object src/CMakeFiles/uhttpd_s.dir/utils.c.o
[10/32] Building C object src/CMakeFiles/uhttpd.dir/log.c.o
[11/32] Linking C static library src/libuhttpd.a
[12/32] Building C object src/CMakeFiles/uhttpd.dir/buffer/buffer.c.o
[13/32] Building C object src/CMakeFiles/uhttpd.dir/uhttpd.c.o
[14/32] Building C object src/CMakeFiles/uhttpd.dir/http-parser/http_parser.c.o
[15/32] Building C object src/CMakeFiles/uhttpd.dir/file.c.o
[16/32] Building C object src/CMakeFiles/uhttpd.dir/ssl.c.o
[17/32] Building C object src/CMakeFiles/uhttpd.dir/utils.c.o
[18/32] Building C object src/CMakeFiles/uhttpd.dir/mimetypes.c.o
[19/32] Building C object src/CMakeFiles/uhttpd.dir/connection.c.o
[20/32] Building C object example/CMakeFiles/multi_process_server.dir/multi_process_server.c.o
[21/32] Linking C shared library src/libuhttpd.so.3.11.0
[22/32] Building C object example/CMakeFiles/multi_process_server.dir/handler.c.o
[23/32] Building C object example/CMakeFiles/test_plugin.dir/test_plugin.c.o
[24/32] Creating library symlink src/libuhttpd.so
[25/32] Linking C executable example/multi_process_server
FAILED: example/multi_process_server 
: && /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/bin/x86_64-openwrt-linux-musl-gcc -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/libuhttpd-mbedtls/libuhttpd-3.11.0=libuhttpd-3.11.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DNDEBUG -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro    -rdynamic example/CMakeFiles/multi_process_server.dir/multi_process_server.c.o example/CMakeFiles/multi_process_server.dir/handler.c.o -o example/multi_process_server  -lev  src/libuhttpd.so.3.11.0  -lev  -lm  -ldl  -lmbedtls  -lmbedx509  -lmbedcrypto  -lz && :
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.11.0: undefined reference to `mbedtls_ssl_config_defaults'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.11.0: undefined reference to `mbedtls_ssl_cache_get'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.11.0: undefined reference to `mbedtls_ssl_free'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.11.0: undefined reference to `mbedtls_ssl_config_free'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.11.0: undefined reference to `mbedtls_ssl_setup'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.11.0: undefined reference to `mbedtls_ssl_cache_set'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.11.0: undefined reference to `mbedtls_ssl_cache_free'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.11.0: undefined reference to `mbedtls_ssl_handshake'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.11.0: undefined reference to `mbedtls_ssl_set_bio'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.11.0: undefined reference to `mbedtls_ssl_read'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.11.0: undefined reference to `mbedtls_ssl_conf_rng'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.11.0: undefined reference to `mbedtls_ssl_conf_session_cache'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.11.0: undefined reference to `mbedtls_ssl_cache_init'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.11.0: undefined reference to `mbedtls_ssl_write'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.11.0: undefined reference to `mbedtls_ssl_conf_own_cert'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.11.0: undefined reference to `mbedtls_ssl_conf_ca_chain'
collect2: error: ld returned 1 exit status
[26/32] Linking C shared module example/test_plugin.so
[27/32] Building C object example/CMakeFiles/multi_process_server_reuseport.dir/multi_process_server_reuseport.c.o
ninja: build stopped: subcommand failed.
make[3]: *** [Makefile:61: /openwrt/build_dir/target-x86_64_musl/libuhttpd-mbedtls/libuhttpd-3.11.0/.built] Error 1
```
