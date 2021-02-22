---
title: "compile.48"
date: 2021-02-22 14:41:15.180927
hidden: false
draft: false
weight: -48
---

build number: `48`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/umurmur/compile -j$(nproc) || make package/feeds/packages/umurmur/compile V=s
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
-- Looking for clock_gettime in rt
-- Looking for clock_gettime in rt - found
-- Looking for MBEDTLS_ZLIB_SUPPORT
-- Looking for MBEDTLS_ZLIB_SUPPORT - not found
-- Found mbedTLS: /openwrt/staging_dir/target-x86_64_musl/usr/include/mbedtls  
-- Found Libconfig: /openwrt/staging_dir/target-x86_64_musl/usr/include  
-- Found ProtobufC: /openwrt/staging_dir/target-x86_64_musl/usr/include  
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
    CMAKE_FIND_ROOT_PATH_MODE_LIBRARY
    CMAKE_MODULE_LINKER_FLAGS
    CMAKE_SHARED_LINKER_FLAGS
    DL_LIBRARY


-- Build files have been written to: /openwrt/build_dir/target-x86_64_musl/umurmur-mbedtls/umurmur-0.2.19
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/umurmur-mbedtls/umurmur-0.2.19'
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/umurmur-mbedtls/umurmur-0.2.19'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/umurmur-mbedtls/umurmur-0.2.19'
Scanning dependencies of target umurmurd
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/umurmur-mbedtls/umurmur-0.2.19'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/umurmur-mbedtls/umurmur-0.2.19'
[  5%] Building C object src/CMakeFiles/umurmurd.dir/Mumble.pb-c.c.o
[ 11%] Building C object src/CMakeFiles/umurmurd.dir/ban.c.o
[ 16%] Building C object src/CMakeFiles/umurmurd.dir/channel.c.o
[ 22%] Building C object src/CMakeFiles/umurmurd.dir/client.c.o
[ 27%] Building C object src/CMakeFiles/umurmurd.dir/conf.c.o
[ 33%] Building C object src/CMakeFiles/umurmurd.dir/crypt.c.o
[ 38%] Building C object src/CMakeFiles/umurmurd.dir/log.c.o
[ 44%] Building C object src/CMakeFiles/umurmurd.dir/main.c.o
[ 50%] Building C object src/CMakeFiles/umurmurd.dir/messagehandler.c.o
[ 55%] Building C object src/CMakeFiles/umurmurd.dir/messages.c.o
[ 61%] Building C object src/CMakeFiles/umurmurd.dir/pds.c.o
[ 66%] Building C object src/CMakeFiles/umurmurd.dir/server.c.o
[ 72%] Building C object src/CMakeFiles/umurmurd.dir/timer.c.o
[ 77%] Building C object src/CMakeFiles/umurmurd.dir/util.c.o
[ 83%] Building C object src/CMakeFiles/umurmurd.dir/voicetarget.c.o
[ 88%] Building C object src/CMakeFiles/umurmurd.dir/memory.c.o
[ 94%] Building C object src/CMakeFiles/umurmurd.dir/ssli_mbedtls.c.o
[100%] Linking C executable ../bin/umurmurd
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: CMakeFiles/umurmurd.dir/ssli_mbedtls.c.o: in function `SSLi_init':
ssli_mbedtls.c:(.text+0x18c): undefined reference to `mbedtls_ssl_config_init'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ssli_mbedtls.c:(.text+0x1a2): undefined reference to `mbedtls_ssl_config_defaults'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ssli_mbedtls.c:(.text+0x1c4): undefined reference to `mbedtls_ssl_conf_authmode'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ssli_mbedtls.c:(.text+0x1d8): undefined reference to `mbedtls_ssl_conf_rng'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ssli_mbedtls.c:(.text+0x1ec): undefined reference to `mbedtls_ssl_conf_dbg'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ssli_mbedtls.c:(.text+0x203): undefined reference to `mbedtls_ssl_conf_min_version'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ssli_mbedtls.c:(.text+0x215): undefined reference to `mbedtls_ssl_conf_ciphersuites'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ssli_mbedtls.c:(.text+0x229): undefined reference to `mbedtls_ssl_conf_ca_chain'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ssli_mbedtls.c:(.text+0x240): undefined reference to `mbedtls_ssl_conf_own_cert'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: CMakeFiles/umurmurd.dir/ssli_mbedtls.c.o: in function `SSLi_deinit':
ssli_mbedtls.c:(.text+0x295): undefined reference to `mbedtls_ssl_config_free'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: CMakeFiles/umurmurd.dir/ssli_mbedtls.c.o: in function `SSLi_getSHA1Hash':
ssli_mbedtls.c:(.text+0x2cf): undefined reference to `mbedtls_ssl_get_peer_cert'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: CMakeFiles/umurmurd.dir/ssli_mbedtls.c.o: in function `SSLi_newconnection':
ssli_mbedtls.c:(.text+0x33b): undefined reference to `mbedtls_ssl_init'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ssli_mbedtls.c:(.text+0x34b): undefined reference to `mbedtls_net_recv'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ssli_mbedtls.c:(.text+0x352): undefined reference to `mbedtls_net_send'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ssli_mbedtls.c:(.text+0x358): undefined reference to `mbedtls_ssl_set_bio'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ssli_mbedtls.c:(.text+0x364): undefined reference to `mbedtls_ssl_set_session'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: ssli_mbedtls.c:(.text+0x374): undefined reference to `mbedtls_ssl_setup'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: CMakeFiles/umurmurd.dir/ssli_mbedtls.c.o: in function `SSLi_nonblockaccept':
ssli_mbedtls.c:(.text+0x399): undefined reference to `mbedtls_ssl_handshake'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: CMakeFiles/umurmurd.dir/ssli_mbedtls.c.o: in function `SSLi_read':
ssli_mbedtls.c:(.text+0x3d8): undefined reference to `mbedtls_ssl_read'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: CMakeFiles/umurmurd.dir/ssli_mbedtls.c.o: in function `SSLi_write':
ssli_mbedtls.c:(.text+0x3f0): undefined reference to `mbedtls_ssl_write'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: CMakeFiles/umurmurd.dir/ssli_mbedtls.c.o: in function `SSLi_data_pending':
ssli_mbedtls.c:(.text+0x408): undefined reference to `mbedtls_ssl_get_bytes_avail'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: CMakeFiles/umurmurd.dir/ssli_mbedtls.c.o: in function `SSLi_shutdown':
ssli_mbedtls.c:(.text+0x416): undefined reference to `mbedtls_ssl_close_notify'
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: CMakeFiles/umurmurd.dir/ssli_mbedtls.c.o: in function `SSLi_free':
ssli_mbedtls.c:(.text+0x420): undefined reference to `mbedtls_ssl_free'
collect2: error: ld returned 1 exit status
make[6]: *** [src/CMakeFiles/umurmurd.dir/build.make:343: bin/umurmurd] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/umurmur-mbedtls/umurmur-0.2.19'
make[5]: *** [CMakeFiles/Makefile2:113: src/CMakeFiles/umurmurd.dir/all] Error 2
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/umurmur-mbedtls/umurmur-0.2.19'
make[4]: *** [Makefile:149: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/umurmur-mbedtls/umurmur-0.2.19'
make[3]: *** [Makefile:99: /openwrt/build_dir/target-x86_64_musl/umurmur-mbedtls/umurmur-0.2.19/.built] Error 2
```
