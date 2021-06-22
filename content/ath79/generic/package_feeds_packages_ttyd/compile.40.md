---
title: "compile.40"
date: 2021-06-22 10:46:12.814451
hidden: false
draft: false
weight: -40
---

build number: `40`

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
-- Could NOT find Libwebsockets (missing: LIBWEBSOCKETS_LIBRARY LIBWEBSOCKETS_INCLUDE_DIR) 
-- Looking for LWS_OPENSSL_SUPPORT
-- Looking for LWS_OPENSSL_SUPPORT - not found
-- Looking for LWS_WITH_MBEDTLS
-- Looking for LWS_WITH_MBEDTLS - not found
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
FAILED: CMakeFiles/ttyd.dir/src/server.c.o 
/openwrt/staging_dir/host/bin/ccache /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc -DTTYD_VERSION=\"1.6.3\" -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-c -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/ttyd-1.6.3=ttyd-1.6.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -D_GNU_SOURCE -DNDEBUG -std=gnu99 -MD -MT CMakeFiles/ttyd.dir/src/server.c.o -MF CMakeFiles/ttyd.dir/src/server.c.o.d -o CMakeFiles/ttyd.dir/src/server.c.o -c src/server.c
src/server.c:6:10: fatal error: libwebsockets.h: No such file or directory
 #include <libwebsockets.h>
          ^~~~~~~~~~~~~~~~~
compilation terminated.
ninja: build stopped: subcommand failed.
make[3]: *** [Makefile:54: /openwrt/build_dir/target-mips_24kc_musl/ttyd-1.6.3/.built] Error 1
```
