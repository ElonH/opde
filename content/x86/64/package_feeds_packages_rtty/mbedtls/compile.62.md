---
title: "compile.62"
date: 2021-05-05 13:47:21.923339
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
-- Found MbedTLS: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libmbedtls.so (found version "2.16.10") 
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
ninja: Entering directory `/openwrt/build_dir/target-x86_64_musl/rtty-mbedtls/rtty-7.4.0/'
[1/12] Building C object src/CMakeFiles/rtty.dir/utils.c.o
[2/12] Building C object src/CMakeFiles/rtty.dir/buffer/buffer.c.o
[3/12] Building C object src/CMakeFiles/rtty.dir/main.c.o
[4/12] Building C object src/CMakeFiles/rtty.dir/log.c.o
[5/12] Building C object src/CMakeFiles/rtty.dir/net.c.o
[6/12] Building C object src/CMakeFiles/rtty.dir/file.c.o
[7/12] Building C object src/CMakeFiles/rtty.dir/command.c.o
[8/12] Building C object src/CMakeFiles/rtty.dir/rtty.c.o
[9/12] Building C object src/CMakeFiles/rtty.dir/filectl.c.o
[10/12] Building C object src/CMakeFiles/rtty.dir/web.c.o
[11/12] Building C object src/CMakeFiles/rtty.dir/ssl.c.o
[12/12] Linking C executable src/rtty
FAILED: src/rtty 
: && /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/bin/x86_64-openwrt-linux-musl-gcc -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/rtty-mbedtls/rtty-7.4.0=rtty-7.4.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DNDEBUG -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro   -rdynamic src/CMakeFiles/rtty.dir/main.c.o src/CMakeFiles/rtty.dir/utils.c.o src/CMakeFiles/rtty.dir/buffer/buffer.c.o src/CMakeFiles/rtty.dir/log.c.o src/CMakeFiles/rtty.dir/net.c.o src/CMakeFiles/rtty.dir/rtty.c.o src/CMakeFiles/rtty.dir/command.c.o src/CMakeFiles/rtty.dir/file.c.o src/CMakeFiles/rtty.dir/filectl.c.o src/CMakeFiles/rtty.dir/ssl.c.o src/CMakeFiles/rtty.dir/web.c.o -o src/rtty  -lev  -lutil  -lcrypt  -lm  -lmbedtls  -lmbedx509  -lmbedcrypto  -lz && :
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/CMakeFiles/rtty.dir/ssl.c.o: in function `rtty_ssl_init':
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
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/CMakeFiles/rtty.dir/ssl.c.o: in function `rtty_ssl_free':
ssl.c:(.text+0x262): undefined reference to `mbedtls_ssl_free'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ssl.c:(.text+0x26f): undefined reference to `mbedtls_ssl_config_free'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/CMakeFiles/rtty.dir/ssl.c.o: in function `rtty_ssl_read':
ssl.c:(.text+0x292): undefined reference to `mbedtls_ssl_read'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/CMakeFiles/rtty.dir/ssl.c.o: in function `rtty_ssl_write':
ssl.c:(.text+0x2da): undefined reference to `mbedtls_ssl_handshake'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ssl.c:(.text+0x33b): undefined reference to `mbedtls_ssl_write'
collect2: error: ld returned 1 exit status
ninja: build stopped: subcommand failed.
make[3]: *** [Makefile:69: /openwrt/build_dir/target-x86_64_musl/rtty-mbedtls/rtty-7.4.0/.built] Error 1
```
