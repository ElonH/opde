---
title: "compile.45"
date: 2021-09-01 09:20:50.673241
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
-- Found OpenSSL: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libcrypto.so (found version "1.1.1l")  
-- Found WolfSSL: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libwolfssl.so (found version "4.7.0") 
-- Found MbedTLS: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libmbedtls.so (found version "2.16.11") 
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


-- Build files have been written to: /openwrt/build_dir/target-x86_64_musl/rtty-mbedtls/rtty-7.4.1
ninja: Entering directory `/openwrt/build_dir/target-x86_64_musl/rtty-mbedtls/rtty-7.4.1'
[1/13] Building C object src/CMakeFiles/rtty.dir/command.c.o
[2/13] Building C object src/CMakeFiles/rtty.dir/file.c.o
[3/13] Building C object src/CMakeFiles/rtty.dir/filectl.c.o
[4/13] Building C object src/CMakeFiles/rtty.dir/main.c.o
[5/13] Building C object src/CMakeFiles/rtty.dir/net.c.o
[6/13] Building C object src/CMakeFiles/rtty.dir/rtty.c.o
[7/13] Building C object src/CMakeFiles/rtty.dir/utils.c.o
[8/13] Building C object src/CMakeFiles/rtty.dir/web.c.o
[9/13] Building C object src/CMakeFiles/rtty.dir/log/log.c.o
[10/13] Building C object src/CMakeFiles/rtty.dir/buffer/buffer.c.o
[11/13] Building C object src/ssl/CMakeFiles/xssl.dir/mbedtls.c.o
[12/13] Linking C static library src/ssl/libxssl.a
[13/13] Linking C executable src/rtty
FAILED: src/rtty 
: && /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/bin/x86_64-openwrt-linux-musl-gcc -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/rtty-mbedtls/rtty-7.4.1=rtty-7.4.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DNDEBUG -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro   -rdynamic src/CMakeFiles/rtty.dir/command.c.o src/CMakeFiles/rtty.dir/file.c.o src/CMakeFiles/rtty.dir/filectl.c.o src/CMakeFiles/rtty.dir/main.c.o src/CMakeFiles/rtty.dir/net.c.o src/CMakeFiles/rtty.dir/rtty.c.o src/CMakeFiles/rtty.dir/utils.c.o src/CMakeFiles/rtty.dir/web.c.o src/CMakeFiles/rtty.dir/log/log.c.o src/CMakeFiles/rtty.dir/buffer/buffer.c.o -o src/rtty  -lev  -lutil  -lcrypt  -lm  src/ssl/libxssl.a  -lmbedtls  -lmbedx509  -lmbedcrypto  -lz && :
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/ssl/libxssl.a(mbedtls.c.o): in function `ssl_update_own_cert':
mbedtls.c:(.text+0x43): undefined reference to `mbedtls_ssl_conf_own_cert'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/ssl/libxssl.a(mbedtls.c.o): in function `ssl_context_new':
mbedtls.c:(.text+0xcf): undefined reference to `mbedtls_ssl_cache_init'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: mbedtls.c:(.text+0xdd): undefined reference to `mbedtls_ssl_cache_set_timeout'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: mbedtls.c:(.text+0xeb): undefined reference to `mbedtls_ssl_cache_set_max_entries'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: mbedtls.c:(.text+0xf7): undefined reference to `mbedtls_ssl_config_init'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: mbedtls.c:(.text+0x10e): undefined reference to `mbedtls_ssl_config_defaults'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: mbedtls.c:(.text+0x123): undefined reference to `mbedtls_ssl_conf_rng'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: mbedtls.c:(.text+0x13a): undefined reference to `mbedtls_ssl_conf_authmode'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: mbedtls.c:(.text+0x14a): undefined reference to `mbedtls_ssl_conf_ciphersuites'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: mbedtls.c:(.text+0x15d): undefined reference to `mbedtls_ssl_conf_min_version'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: mbedtls.c:(.text+0x164): undefined reference to `mbedtls_ssl_cache_set'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: mbedtls.c:(.text+0x16b): undefined reference to `mbedtls_ssl_cache_get'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: mbedtls.c:(.text+0x177): undefined reference to `mbedtls_ssl_conf_session_cache'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: mbedtls.c:(.text+0x1be): undefined reference to `mbedtls_ssl_conf_authmode'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: mbedtls.c:(.text+0x1ce): undefined reference to `mbedtls_ssl_conf_ciphersuites'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/ssl/libxssl.a(mbedtls.c.o): in function `ssl_context_free':
mbedtls.c:(.text+0x1e6): undefined reference to `mbedtls_ssl_cache_free'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: mbedtls.c:(.text+0x216): undefined reference to `mbedtls_ssl_config_free'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/ssl/libxssl.a(mbedtls.c.o): in function `ssl_load_ca_crt_file':
mbedtls.c:(.text+0x25d): undefined reference to `mbedtls_ssl_conf_ca_chain'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: mbedtls.c:(.text+0x26b): undefined reference to `mbedtls_ssl_conf_authmode'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/ssl/libxssl.a(mbedtls.c.o): in function `ssl_set_ciphers':
mbedtls.c:(.text+0x335): undefined reference to `mbedtls_ssl_get_ciphersuite_id'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: mbedtls.c:(.text+0x3cc): undefined reference to `mbedtls_ssl_conf_ciphersuites'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/ssl/libxssl.a(mbedtls.c.o): in function `ssl_set_require_validation':
mbedtls.c:(.text+0x416): undefined reference to `mbedtls_ssl_conf_authmode'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/ssl/libxssl.a(mbedtls.c.o): in function `ssl_session_new':
mbedtls.c:(.text+0x44b): undefined reference to `mbedtls_ssl_init'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: mbedtls.c:(.text+0x457): undefined reference to `mbedtls_ssl_setup'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: mbedtls.c:(.text+0x476): undefined reference to `mbedtls_net_recv'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: mbedtls.c:(.text+0x47d): undefined reference to `mbedtls_net_send'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: mbedtls.c:(.text+0x486): undefined reference to `mbedtls_ssl_set_bio'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/ssl/libxssl.a(mbedtls.c.o): in function `ssl_session_free':
mbedtls.c:(.text+0x4ad): undefined reference to `mbedtls_ssl_free'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/ssl/libxssl.a(mbedtls.c.o): in function `ssl_set_server_name':
mbedtls.c:(.text+0x4c3): undefined reference to `mbedtls_ssl_set_hostname'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/ssl/libxssl.a(mbedtls.c.o): in function `ssl_connect':
mbedtls.c:(.text+0x4ee): undefined reference to `mbedtls_ssl_handshake'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: mbedtls.c:(.text+0x526): undefined reference to `mbedtls_ssl_get_verify_result'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/ssl/libxssl.a(mbedtls.c.o): in function `ssl_write':
mbedtls.c:(.text+0x5b3): undefined reference to `mbedtls_ssl_write'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: src/ssl/libxssl.a(mbedtls.c.o): in function `ssl_read':
mbedtls.c:(.text+0x5f9): undefined reference to `mbedtls_ssl_read'
collect2: error: ld returned 1 exit status
ninja: build stopped: subcommand failed.
make[3]: *** [Makefile:69: /openwrt/build_dir/target-x86_64_musl/rtty-mbedtls/rtty-7.4.1/.built] Error 1
```
