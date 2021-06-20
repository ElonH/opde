---
title: "compile.37"
date: 2021-06-20 22:36:26.334619
hidden: false
draft: false
weight: -37
---

build number: `37`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/ttyd/compile -j$(nproc) || make package/feeds/packages/ttyd/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/100-log-to-syslog.patch using plaintext: 
patching file src/server.c
CMake Deprecation Warning at CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 2.8.12 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- The C compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Found Git: /openwrt/staging_dir/host/bin/git (found version "2.25.1") 
-- Found LIBUV: /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libuv.so  
-- Found JSON-C: /openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-c  
-- Found ZLIB: /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libz.so (found version "1.2.11") 
-- Looking for LWS_OPENSSL_SUPPORT
-- Looking for LWS_OPENSSL_SUPPORT - found
-- Looking for LWS_WITH_MBEDTLS
-- Looking for LWS_WITH_MBEDTLS - found
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


-- Build files have been written to: /openwrt/build_dir/target-mips_24kc_musl/ttyd-1.6.3
ninja: Entering directory `/openwrt/build_dir/target-mips_24kc_musl/ttyd-1.6.3'
[1/6] Building C object CMakeFiles/ttyd.dir/src/server.c.o
[2/6] Building C object CMakeFiles/ttyd.dir/src/http.c.o
[3/6] Building C object CMakeFiles/ttyd.dir/src/protocol.c.o
[4/6] Building C object CMakeFiles/ttyd.dir/src/terminal.c.o
[5/6] Building C object CMakeFiles/ttyd.dir/src/utils.c.o
[6/6] Linking C executable ttyd
ninja: Entering directory `/openwrt/build_dir/target-mips_24kc_musl/ttyd-1.6.3'
[0/1] Install the project...
-- Install configuration: "Release"
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/ttyd-1.6.3/ipkg-install/usr/bin/ttyd
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/ttyd-1.6.3/ipkg-install/usr/share/man/man1/ttyd.1
Package ttyd is missing dependencies for the following libraries:
libcap.so.2
libmbedcrypto.so.3
libmbedtls.so.12
libmbedx509.so.0
libwebsockets.so.17
make[3]: *** [Makefile:64: /openwrt/bin/packages/mips_24kc/packages/ttyd_1.6.3-2_mips_24kc.ipk] Error 1
```
