---
title: "compile.62"
date: 2021-05-05 14:26:33.259920
hidden: false
draft: false
weight: -62
---

build number: `62`

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
  src/CMakeLists.txt:44 (find_package)
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Found WOLFSSL: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libwolfssl.so (found version "4.7.0") 
-- Found MbedTLS: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libmbedtls.so (found version "2.16.10") 
-- Select MbedTLS(PolarSSL) as the SSL backend
-- Found Lua: /openwrt/staging_dir/target-x86_64_musl/usr/lib/liblua.so  
-- UWSC_VERSION: 3.3.5
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


-- Build files have been written to: /openwrt/build_dir/target-x86_64_musl/libuwsc-mbedtls/libuwsc-3.3.5
ninja: Entering directory `/openwrt/build_dir/target-x86_64_musl/libuwsc-mbedtls/libuwsc-3.3.5/'
[1/19] Building C object src/CMakeFiles/uwsc_s.dir/log.c.o
[2/19] Building C object src/CMakeFiles/uwsc_s.dir/uwsc.c.o
[3/19] Building C object src/CMakeFiles/uwsc_s.dir/utils.c.o
[4/19] Building C object src/CMakeFiles/uwsc_s.dir/buffer/buffer.c.o
[5/19] Building C object src/CMakeFiles/uwsc_s.dir/sha1.c.o
[6/19] Building C object src/CMakeFiles/uwsc.dir/uwsc.c.o
[7/19] Building C object src/CMakeFiles/uwsc.dir/log.c.o
[8/19] Building C object src/CMakeFiles/uwsc.dir/utils.c.o
[9/19] Building C object src/CMakeFiles/uwsc.dir/sha1.c.o
[10/19] Building C object src/CMakeFiles/uwsc.dir/buffer/buffer.c.o
[11/19] Building C object src/CMakeFiles/uwsc_s.dir/ssl.c.o
[12/19] Linking C static library src/libuwsc.a
[13/19] Building C object src/lua/CMakeFiles/uwsc-lua.dir/uwsc_lua.c.o
[14/19] Building C object src/CMakeFiles/uwsc.dir/ssl.c.o
[15/19] Building C object example/CMakeFiles/example.dir/example.c.o
[16/19] Linking C shared library src/libuwsc.so.3.3.5
[17/19] Creating library symlink src/libuwsc.so
[18/19] Linking C executable example/example
FAILED: example/example 
: && /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/bin/x86_64-openwrt-linux-musl-gcc -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/libuwsc-mbedtls/libuwsc-3.3.5=libuwsc-3.3.5 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DNDEBUG -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro    -rdynamic example/CMakeFiles/example.dir/example.c.o -o example/example  src/libuwsc.so.3.3.5  -lev  -ldl  -lmbedtls  -lmbedx509  -lmbedcrypto && :
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuwsc.so.3.3.5: undefined reference to `mbedtls_ssl_init'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuwsc.so.3.3.5: undefined reference to `mbedtls_ssl_config_defaults'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuwsc.so.3.3.5: undefined reference to `mbedtls_ssl_config_init'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuwsc.so.3.3.5: undefined reference to `mbedtls_ssl_free'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuwsc.so.3.3.5: undefined reference to `mbedtls_ssl_config_free'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuwsc.so.3.3.5: undefined reference to `mbedtls_ssl_setup'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuwsc.so.3.3.5: undefined reference to `mbedtls_ssl_handshake'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuwsc.so.3.3.5: undefined reference to `mbedtls_ssl_conf_authmode'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuwsc.so.3.3.5: undefined reference to `mbedtls_ssl_set_bio'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuwsc.so.3.3.5: undefined reference to `mbedtls_ssl_read'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuwsc.so.3.3.5: undefined reference to `mbedtls_ssl_conf_rng'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuwsc.so.3.3.5: undefined reference to `mbedtls_net_init'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuwsc.so.3.3.5: undefined reference to `mbedtls_ssl_set_hostname'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuwsc.so.3.3.5: undefined reference to `mbedtls_ssl_write'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuwsc.so.3.3.5: undefined reference to `mbedtls_net_recv'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuwsc.so.3.3.5: undefined reference to `mbedtls_ssl_conf_ca_chain'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/libuwsc.so.3.3.5: undefined reference to `mbedtls_net_send'
collect2: error: ld returned 1 exit status
[19/19] Linking C shared module src/lua/uwsc.so
ninja: build stopped: subcommand failed.
make[3]: *** [Makefile:91: /openwrt/build_dir/target-x86_64_musl/libuwsc-mbedtls/libuwsc-3.3.5/.built] Error 1
```
