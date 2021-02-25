---
title: "compile.50"
date: 2021-02-25 14:20:49.081638
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
make package/feeds/packages/libuwsc/compile -j$(nproc) || make package/feeds/packages/libuwsc/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-fix_find_lua.patch using plaintext: 
patching file cmake/Modules/FindLua.cmake
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
-- Found Libev: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libev.so (found version "4.31") 
CMake Warning (dev) at /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindPackageHandleStandardArgs.cmake:424 (message):
  The package name passed to `find_package_handle_standard_args` (WOLFSSL)
  does not match the name of the calling package (WolfSSL).  This can lead to
  problems in calling code that expects `find_package` result variables
  (e.g., `_FOUND`) to follow a certain pattern.
Call Stack (most recent call first):
  cmake/Modules/FindWolfSSL.cmake:49 (find_package_handle_standard_args)
  src/CMakeLists.txt:37 (find_package)
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Found WOLFSSL: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libwolfssl.so (found version "4.7.0") 
-- Found MbedTLS: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libmbedtls.so (found version "2.16.9") 
-- Select MbedTLS(PolarSSL) as the SSL backend
-- Found Lua: /openwrt/staging_dir/target-x86_64_musl/usr/lib/liblua.so  
-- UWSC_VERSION: 3.3.4
-- UWSC_SSL_SUPPORT: MbedTLS(PolarSSL)
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


-- Build files have been written to: /openwrt/build_dir/target-x86_64_musl/libuwsc-mbedtls/libuwsc-3.3.4
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/libuwsc-mbedtls/libuwsc-3.3.4'
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/libuwsc-mbedtls/libuwsc-3.3.4'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/libuwsc-mbedtls/libuwsc-3.3.4'
Scanning dependencies of target uwsc_s
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/libuwsc-mbedtls/libuwsc-3.3.4'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/libuwsc-mbedtls/libuwsc-3.3.4'
[  5%] Building C object src/CMakeFiles/uwsc_s.dir/uwsc.c.o
[ 11%] Building C object src/CMakeFiles/uwsc_s.dir/log.c.o
[ 16%] Building C object src/CMakeFiles/uwsc_s.dir/utils.c.o
[ 22%] Building C object src/CMakeFiles/uwsc_s.dir/buffer/buffer.c.o
[ 27%] Building C object src/CMakeFiles/uwsc_s.dir/sha1.c.o
[ 33%] Building C object src/CMakeFiles/uwsc_s.dir/ssl.c.o
[ 38%] Linking C static library libuwsc.a
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/libuwsc-mbedtls/libuwsc-3.3.4'
[ 38%] Built target uwsc_s
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/libuwsc-mbedtls/libuwsc-3.3.4'
Scanning dependencies of target uwsc
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/libuwsc-mbedtls/libuwsc-3.3.4'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/libuwsc-mbedtls/libuwsc-3.3.4'
[ 44%] Building C object src/CMakeFiles/uwsc.dir/uwsc.c.o
[ 50%] Building C object src/CMakeFiles/uwsc.dir/log.c.o
[ 55%] Building C object src/CMakeFiles/uwsc.dir/utils.c.o
[ 61%] Building C object src/CMakeFiles/uwsc.dir/buffer/buffer.c.o
[ 66%] Building C object src/CMakeFiles/uwsc.dir/sha1.c.o
[ 72%] Building C object src/CMakeFiles/uwsc.dir/ssl.c.o
[ 77%] Linking C shared library libuwsc.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/libuwsc-mbedtls/libuwsc-3.3.4'
[ 77%] Built target uwsc
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/libuwsc-mbedtls/libuwsc-3.3.4'
Scanning dependencies of target uwsc-lua
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/libuwsc-mbedtls/libuwsc-3.3.4'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/libuwsc-mbedtls/libuwsc-3.3.4'
[ 83%] Building C object src/lua/CMakeFiles/uwsc-lua.dir/uwsc_lua.c.o
[ 88%] Linking C shared module uwsc.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/libuwsc-mbedtls/libuwsc-3.3.4'
[ 88%] Built target uwsc-lua
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/libuwsc-mbedtls/libuwsc-3.3.4'
Scanning dependencies of target example
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/libuwsc-mbedtls/libuwsc-3.3.4'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/libuwsc-mbedtls/libuwsc-3.3.4'
[ 94%] Building C object example/CMakeFiles/example.dir/example.c.o
[100%] Linking C executable example
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuwsc.so.3.3.4: undefined reference to `mbedtls_ssl_init'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuwsc.so.3.3.4: undefined reference to `mbedtls_ssl_config_defaults'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuwsc.so.3.3.4: undefined reference to `mbedtls_ssl_config_init'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuwsc.so.3.3.4: undefined reference to `mbedtls_ssl_free'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuwsc.so.3.3.4: undefined reference to `mbedtls_ssl_config_free'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuwsc.so.3.3.4: undefined reference to `mbedtls_ssl_setup'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuwsc.so.3.3.4: undefined reference to `mbedtls_ssl_handshake'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuwsc.so.3.3.4: undefined reference to `mbedtls_ssl_conf_authmode'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuwsc.so.3.3.4: undefined reference to `mbedtls_ssl_set_bio'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuwsc.so.3.3.4: undefined reference to `mbedtls_ssl_read'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuwsc.so.3.3.4: undefined reference to `mbedtls_ssl_conf_rng'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuwsc.so.3.3.4: undefined reference to `mbedtls_net_init'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuwsc.so.3.3.4: undefined reference to `mbedtls_ssl_set_hostname'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuwsc.so.3.3.4: undefined reference to `mbedtls_ssl_write'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuwsc.so.3.3.4: undefined reference to `mbedtls_net_recv'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuwsc.so.3.3.4: undefined reference to `mbedtls_ssl_conf_ca_chain'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ../src/libuwsc.so.3.3.4: undefined reference to `mbedtls_net_send'
collect2: error: ld returned 1 exit status
make[6]: *** [example/CMakeFiles/example.dir/build.make:108: example/example] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/libuwsc-mbedtls/libuwsc-3.3.4'
make[5]: *** [CMakeFiles/Makefile2:237: example/CMakeFiles/example.dir/all] Error 2
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/libuwsc-mbedtls/libuwsc-3.3.4'
make[4]: *** [Makefile:149: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/libuwsc-mbedtls/libuwsc-3.3.4'
make[3]: *** [Makefile:92: /openwrt/build_dir/target-x86_64_musl/libuwsc-mbedtls/libuwsc-3.3.4/.built] Error 2
```
