---
title: "compile.8"
date: 2021-05-06 05:08:41.865866
hidden: false
draft: false
weight: -8
---

build number: `8`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/base/ustream-ssl/compile -j$(nproc) || make package/feeds/base/ustream-ssl/compile V=s
```

#### Compile.txt

``` bash
CMake Deprecation Warning at CMakeLists.txt:1 (cmake_minimum_required):
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
    CMAKE_FIND_USE_PACKAGE_REGISTRY
    CMAKE_FIND_USE_SYSTEM_PACKAGE_REGISTRY
    CMAKE_MODULE_LINKER_FLAGS
    DL_LIBRARY


-- Build files have been written to: /openwrt/build_dir/target-x86_64_musl/ustream-ssl-mbedtls/ustream-ssl-2020-12-10-68d09243
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ustream-ssl-mbedtls/ustream-ssl-2020-12-10-68d09243'
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ustream-ssl-mbedtls/ustream-ssl-2020-12-10-68d09243'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ustream-ssl-mbedtls/ustream-ssl-2020-12-10-68d09243'
Scanning dependencies of target ustream-ssl
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ustream-ssl-mbedtls/ustream-ssl-2020-12-10-68d09243'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ustream-ssl-mbedtls/ustream-ssl-2020-12-10-68d09243'
[ 14%] Building C object CMakeFiles/ustream-ssl.dir/ustream-ssl.c.o
[ 28%] Building C object CMakeFiles/ustream-ssl.dir/ustream-mbedtls.c.o
[ 42%] Linking C shared library libustream-ssl.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ustream-ssl-mbedtls/ustream-ssl-2020-12-10-68d09243'
[ 42%] Built target ustream-ssl
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ustream-ssl-mbedtls/ustream-ssl-2020-12-10-68d09243'
Scanning dependencies of target ustream-example-client
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ustream-ssl-mbedtls/ustream-ssl-2020-12-10-68d09243'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ustream-ssl-mbedtls/ustream-ssl-2020-12-10-68d09243'
[ 57%] Building C object CMakeFiles/ustream-example-client.dir/ustream-example-client.c.o
[ 71%] Linking C executable ustream-example-client
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: libustream-ssl.so: undefined reference to `mbedtls_ssl_init'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: libustream-ssl.so: undefined reference to `mbedtls_ssl_conf_min_version'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: libustream-ssl.so: undefined reference to `mbedtls_ssl_config_defaults'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: libustream-ssl.so: undefined reference to `mbedtls_ssl_config_init'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: libustream-ssl.so: undefined reference to `mbedtls_ssl_cache_get'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: libustream-ssl.so: undefined reference to `mbedtls_ssl_free'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: libustream-ssl.so: undefined reference to `mbedtls_ssl_config_free'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: libustream-ssl.so: undefined reference to `mbedtls_ssl_setup'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: libustream-ssl.so: undefined reference to `mbedtls_ssl_cache_set'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: libustream-ssl.so: undefined reference to `mbedtls_ssl_cache_set_max_entries'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: libustream-ssl.so: undefined reference to `mbedtls_ssl_cache_free'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: libustream-ssl.so: undefined reference to `mbedtls_ssl_handshake'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: libustream-ssl.so: undefined reference to `mbedtls_ssl_cache_set_timeout'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: libustream-ssl.so: undefined reference to `mbedtls_ssl_get_ciphersuite_id'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: libustream-ssl.so: undefined reference to `mbedtls_ssl_conf_authmode'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: libustream-ssl.so: undefined reference to `mbedtls_ssl_set_bio'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: libustream-ssl.so: undefined reference to `mbedtls_ssl_get_verify_result'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: libustream-ssl.so: undefined reference to `mbedtls_ssl_read'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: libustream-ssl.so: undefined reference to `mbedtls_ssl_conf_ciphersuites'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: libustream-ssl.so: undefined reference to `mbedtls_ssl_conf_rng'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: libustream-ssl.so: undefined reference to `mbedtls_ssl_conf_session_cache'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: libustream-ssl.so: undefined reference to `mbedtls_ssl_cache_init'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: libustream-ssl.so: undefined reference to `mbedtls_ssl_set_hostname'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: libustream-ssl.so: undefined reference to `mbedtls_ssl_write'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: libustream-ssl.so: undefined reference to `mbedtls_ssl_conf_own_cert'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: libustream-ssl.so: undefined reference to `mbedtls_ssl_conf_ca_chain'
collect2: error: ld returned 1 exit status
make[6]: *** [CMakeFiles/ustream-example-client.dir/build.make:108: ustream-example-client] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ustream-ssl-mbedtls/ustream-ssl-2020-12-10-68d09243'
make[5]: *** [CMakeFiles/Makefile2:99: CMakeFiles/ustream-example-client.dir/all] Error 2
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ustream-ssl-mbedtls/ustream-ssl-2020-12-10-68d09243'
make[4]: *** [Makefile:149: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ustream-ssl-mbedtls/ustream-ssl-2020-12-10-68d09243'
make[3]: *** [Makefile:71: /openwrt/build_dir/target-x86_64_musl/ustream-ssl-mbedtls/ustream-ssl-2020-12-10-68d09243/.built] Error 2
```
