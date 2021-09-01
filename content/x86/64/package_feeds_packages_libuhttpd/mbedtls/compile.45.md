---
title: "compile.45"
date: 2021-09-01 09:20:50.676013
hidden: false
draft: false
weight: -45
---

build number: `45`

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
-- Found OpenSSL: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libcrypto.so (found version "1.1.1l")  
-- Found WolfSSL: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libwolfssl.so (found version "4.7.0") 
-- Found MbedTLS: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libmbedtls.so (found version "2.16.11") 
-- Found ZLIB: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libz.so (found version "1.2.11") 
-- Select MbedTLS(PolarSSL) as the SSL backend
-- Looking for dlopen in dl
-- Looking for dlopen in dl - found
-- UHTTPD_VERSION: 3.12.1
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


-- Build files have been written to: /openwrt/build_dir/target-x86_64_musl/libuhttpd-mbedtls/libuhttpd-3.12.1
ninja: Entering directory `/openwrt/build_dir/target-x86_64_musl/libuhttpd-mbedtls/libuhttpd-3.12.1'
[1/23] Building C object src/ssl/CMakeFiles/xssl.dir/mbedtls.c.o
[2/23] Linking C static library src/ssl/libxssl.a
[3/23] Building C object src/CMakeFiles/uhttpd.dir/connection.c.o
[4/23] Building C object src/CMakeFiles/uhttpd.dir/file.c.o
[5/23] Building C object src/CMakeFiles/uhttpd.dir/mimetypes.c.o
[6/23] Building C object src/CMakeFiles/uhttpd.dir/uhttpd.c.o
[7/23] Building C object src/CMakeFiles/uhttpd.dir/utils.c.o
[8/23] Building C object src/CMakeFiles/uhttpd.dir/log/log.c.o
[9/23] Building C object src/CMakeFiles/uhttpd.dir/buffer/buffer.c.o
[10/23] Building C object src/CMakeFiles/uhttpd.dir/http-parser/http_parser.c.o
[11/23] Linking C shared library src/libuhttpd.so.3.12.1
[12/23] Creating library symlink src/libuhttpd.so
[13/23] Building C object example/CMakeFiles/multi_process_server.dir/multi_process_server.c.o
[14/23] Building C object example/CMakeFiles/multi_process_server.dir/handler.c.o
[15/23] Linking C executable example/multi_process_server
FAILED: example/multi_process_server 
: && /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/bin/x86_64-openwrt-linux-musl-gcc -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/libuhttpd-mbedtls/libuhttpd-3.12.1=libuhttpd-3.12.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DNDEBUG -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro   -rdynamic example/CMakeFiles/multi_process_server.dir/multi_process_server.c.o example/CMakeFiles/multi_process_server.dir/handler.c.o -o example/multi_process_server  -lev  src/libuhttpd.so.3.12.1  -lmbedtls  -lmbedx509  -lmbedcrypto  -lz && :
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.12.1: undefined reference to `mbedtls_ssl_init'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.12.1: undefined reference to `mbedtls_ssl_conf_min_version'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.12.1: undefined reference to `mbedtls_ssl_config_defaults'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.12.1: undefined reference to `mbedtls_ssl_config_init'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.12.1: undefined reference to `mbedtls_ssl_cache_get'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.12.1: undefined reference to `mbedtls_ssl_free'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.12.1: undefined reference to `mbedtls_ssl_config_free'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.12.1: undefined reference to `mbedtls_ssl_setup'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.12.1: undefined reference to `mbedtls_ssl_cache_set'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.12.1: undefined reference to `mbedtls_ssl_cache_set_max_entries'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.12.1: undefined reference to `mbedtls_ssl_cache_free'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.12.1: undefined reference to `mbedtls_ssl_handshake'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.12.1: undefined reference to `mbedtls_ssl_cache_set_timeout'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.12.1: undefined reference to `mbedtls_ssl_get_ciphersuite_id'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.12.1: undefined reference to `mbedtls_ssl_conf_authmode'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.12.1: undefined reference to `mbedtls_ssl_set_bio'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.12.1: undefined reference to `mbedtls_ssl_get_verify_result'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.12.1: undefined reference to `mbedtls_ssl_read'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.12.1: undefined reference to `mbedtls_ssl_conf_ciphersuites'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.12.1: undefined reference to `mbedtls_ssl_conf_rng'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.12.1: undefined reference to `mbedtls_ssl_conf_session_cache'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.12.1: undefined reference to `mbedtls_ssl_cache_init'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.12.1: undefined reference to `mbedtls_ssl_set_hostname'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.12.1: undefined reference to `mbedtls_ssl_write'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.12.1: undefined reference to `mbedtls_net_recv'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.12.1: undefined reference to `mbedtls_ssl_conf_own_cert'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.12.1: undefined reference to `mbedtls_ssl_conf_ca_chain'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuhttpd.so.3.12.1: undefined reference to `mbedtls_net_send'
collect2: error: ld returned 1 exit status
ninja: build stopped: subcommand failed.
make[3]: *** [Makefile:61: /openwrt/build_dir/target-x86_64_musl/libuhttpd-mbedtls/libuhttpd-3.12.1/.built] Error 1
```
