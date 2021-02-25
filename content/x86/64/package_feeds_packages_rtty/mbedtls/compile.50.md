---
title: "compile.50"
date: 2021-02-25 14:20:49.082278
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
make package/feeds/packages/rtty/compile -j$(nproc) || make package/feeds/packages/rtty/compile V=s
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
CMake Warning (dev) at /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindPackageHandleStandardArgs.cmake:424 (message):
  The package name passed to `find_package_handle_standard_args` (WOLFSSL)
  does not match the name of the calling package (WolfSSL).  This can lead to
  problems in calling code that expects `find_package` result variables
  (e.g., `_FOUND`) to follow a certain pattern.
Call Stack (most recent call first):
  cmake/Modules/FindWolfSSL.cmake:49 (find_package_handle_standard_args)
  src/CMakeLists.txt:34 (find_package)
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Found WOLFSSL: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libwolfssl.so (found version "4.7.0") 
-- Found MbedTLS: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libmbedtls.so (found version "2.16.9") 
-- Found ZLIB: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libz.so (found version "1.2.11") 
-- Select MbedTLS(PolarSSL) as the SSL backend
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
    CMAKE_MODULE_LINKER_FLAGS
    CMAKE_SHARED_LINKER_FLAGS
    DL_LIBRARY


-- Build files have been written to: /openwrt/build_dir/target-x86_64_musl/rtty-mbedtls/rtty-7.4.0
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/rtty-mbedtls/rtty-7.4.0'
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/rtty-mbedtls/rtty-7.4.0'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/rtty-mbedtls/rtty-7.4.0'
Scanning dependencies of target rtty
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/rtty-mbedtls/rtty-7.4.0'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/rtty-mbedtls/rtty-7.4.0'
[  8%] Building C object src/CMakeFiles/rtty.dir/main.c.o
[ 16%] Building C object src/CMakeFiles/rtty.dir/utils.c.o
[ 25%] Building C object src/CMakeFiles/rtty.dir/buffer/buffer.c.o
[ 33%] Building C object src/CMakeFiles/rtty.dir/log.c.o
[ 41%] Building C object src/CMakeFiles/rtty.dir/net.c.o
[ 50%] Building C object src/CMakeFiles/rtty.dir/rtty.c.o
[ 58%] Building C object src/CMakeFiles/rtty.dir/command.c.o
[ 66%] Building C object src/CMakeFiles/rtty.dir/file.c.o
[ 75%] Building C object src/CMakeFiles/rtty.dir/filectl.c.o
[ 83%] Building C object src/CMakeFiles/rtty.dir/ssl.c.o
[ 91%] Building C object src/CMakeFiles/rtty.dir/web.c.o
[100%] Linking C executable rtty
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: CMakeFiles/rtty.dir/ssl.c.o: in function `rtty_ssl_init':
ssl.c:(.text+0x4f): undefined reference to `mbedtls_net_init'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ssl.c:(.text+0x5c): undefined reference to `mbedtls_ssl_init'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ssl.c:(.text+0x6c): undefined reference to `mbedtls_ssl_config_init'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ssl.c:(.text+0xd2): undefined reference to `mbedtls_ssl_config_defaults'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ssl.c:(.text+0xe0): undefined reference to `mbedtls_ssl_conf_authmode'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ssl.c:(.text+0xf1): undefined reference to `mbedtls_ssl_conf_ca_chain'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ssl.c:(.text+0x104): undefined reference to `mbedtls_ssl_conf_rng'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ssl.c:(.text+0x15e): undefined reference to `mbedtls_ssl_conf_own_cert'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ssl.c:(.text+0x173): undefined reference to `mbedtls_net_recv'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ssl.c:(.text+0x17a): undefined reference to `mbedtls_net_send'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ssl.c:(.text+0x188): undefined reference to `mbedtls_ssl_set_bio'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ssl.c:(.text+0x196): undefined reference to `mbedtls_ssl_set_hostname'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ssl.c:(.text+0x1a2): undefined reference to `mbedtls_ssl_setup'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: CMakeFiles/rtty.dir/ssl.c.o: in function `rtty_ssl_free':
ssl.c:(.text+0x262): undefined reference to `mbedtls_ssl_free'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ssl.c:(.text+0x26f): undefined reference to `mbedtls_ssl_config_free'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: CMakeFiles/rtty.dir/ssl.c.o: in function `rtty_ssl_read':
ssl.c:(.text+0x292): undefined reference to `mbedtls_ssl_read'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: CMakeFiles/rtty.dir/ssl.c.o: in function `rtty_ssl_write':
ssl.c:(.text+0x2da): undefined reference to `mbedtls_ssl_handshake'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ssl.c:(.text+0x33b): undefined reference to `mbedtls_ssl_write'
collect2: error: ld returned 1 exit status
make[6]: *** [src/CMakeFiles/rtty.dir/build.make:258: src/rtty] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/rtty-mbedtls/rtty-7.4.0'
make[5]: *** [CMakeFiles/Makefile2:113: src/CMakeFiles/rtty.dir/all] Error 2
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/rtty-mbedtls/rtty-7.4.0'
make[4]: *** [Makefile:149: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/rtty-mbedtls/rtty-7.4.0'
make[3]: *** [Makefile:71: /openwrt/build_dir/target-x86_64_musl/rtty-mbedtls/rtty-7.4.0/.built] Error 2
```
