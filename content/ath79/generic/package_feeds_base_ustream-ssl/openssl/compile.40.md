---
title: "compile.40"
date: 2021-06-22 10:50:06.150299
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
-- Check for working C compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc - skipped
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


-- Build files have been written to: /openwrt/build_dir/target-mips_24kc_musl/ustream-ssl-openssl/ustream-ssl-2020-12-10-68d09243
ninja: Entering directory `/openwrt/build_dir/target-mips_24kc_musl/ustream-ssl-openssl/ustream-ssl-2020-12-10-68d09243'
[1/8] Building C object CMakeFiles/ustream-example-client.dir/ustream-example-client.c.o
[2/8] Building C object CMakeFiles/ustream-example-server.dir/ustream-example-server.c.o
[3/8] Building C object CMakeFiles/ustream-ssl.dir/ustream-ssl.c.o
FAILED: CMakeFiles/ustream-ssl.dir/ustream-ssl.c.o 
/openwrt/staging_dir/host/bin/ccache /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc -Dustream_ssl_EXPORTS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/ustream-ssl-openssl/ustream-ssl-2020-12-10-68d09243=ustream-ssl-2020-12-10-68d09243 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DNDEBUG -fPIC   -Os -Wall -Werror --std=gnu99 -g3 -Wextra -Werror=implicit-function-declaration -Wformat -Werror=format-security -Werror=format-nonliteral -Wno-unused-parameter -Wmissing-declarations -MD -MT CMakeFiles/ustream-ssl.dir/ustream-ssl.c.o -MF CMakeFiles/ustream-ssl.dir/ustream-ssl.c.o.d -o CMakeFiles/ustream-ssl.dir/ustream-ssl.c.o -c ustream-ssl.c
In file included from ustream-internal.h:27,
                 from ustream-ssl.c:25:
ustream-openssl.h:26:10: fatal error: openssl/ssl.h: No such file or directory
 #include <openssl/ssl.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
ninja: build stopped: subcommand failed.
make[3]: *** [Makefile:73: /openwrt/build_dir/target-mips_24kc_musl/ustream-ssl-openssl/ustream-ssl-2020-12-10-68d09243/.built] Error 1
```
