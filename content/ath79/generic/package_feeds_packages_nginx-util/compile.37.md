---
title: "compile.37"
date: 2021-06-20 22:39:07.396279
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
make package/feeds/packages/nginx-util/compile -j$(nproc) || make package/feeds/packages/nginx-util/compile V=s
```

#### Compile.txt

``` bash
CMake Deprecation Warning at CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 2.8.12 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- The CXX compiler identification is GNU 8.4.0
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-g++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Configuring done
-- Generating done
CMake Warning:
  Manually-specified variables were not used by the project:

    CMAKE_ASM_COMPILER
    CMAKE_ASM_COMPILER_LAUNCHER
    CMAKE_C_FLAGS_RELEASE
    CMAKE_EXPORT_NO_PACKAGE_REGISTRY
    CMAKE_EXPORT_PACKAGE_REGISTRY
    CMAKE_FIND_PACKAGE_NO_PACKAGE_REGISTRY
    CMAKE_FIND_PACKAGE_NO_SYSTEM_PACKAGE_REGISTRY
    CMAKE_FIND_USE_PACKAGE_REGISTRY
    CMAKE_FIND_USE_SYSTEM_PACKAGE_REGISTRY
    CMAKE_MODULE_LINKER_FLAGS
    CMAKE_SHARED_LINKER_FLAGS
    DL_LIBRARY


-- Build files have been written to: /openwrt/build_dir/target-mips_24kc_musl/nginx-util-1.6
ninja: Entering directory `/openwrt/build_dir/target-mips_24kc_musl/nginx-util-1.6'
[1/4] Building CXX object CMakeFiles/nginx-ssl-util-nopcre.dir/nginx-util.cpp.o
FAILED: CMakeFiles/nginx-ssl-util-nopcre.dir/nginx-util.cpp.o 
/openwrt/staging_dir/host/bin/ccache /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-g++ -DNO_PCRE -DVERSION=1.6  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/nginx-util-1.6=nginx-util-1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DNDEBUG   -Os -Wall -Werror -Wextra -g3 -Wno-unused-parameter -Wmissing-declarations -Wshadow -std=gnu++17 -MD -MT CMakeFiles/nginx-ssl-util-nopcre.dir/nginx-util.cpp.o -MF CMakeFiles/nginx-ssl-util-nopcre.dir/nginx-util.cpp.o.d -o CMakeFiles/nginx-ssl-util-nopcre.dir/nginx-util.cpp.o -c nginx-util.cpp
In file included from nginx-ssl-util.hpp:12,
                 from nginx-util.cpp:4:
px5g-openssl.hpp:6:10: fatal error: openssl/bn.h: No such file or directory
 #include <openssl/bn.h>
          ^~~~~~~~~~~~~~
compilation terminated.
ninja: build stopped: subcommand failed.
make[3]: *** [Makefile:121: /openwrt/build_dir/target-mips_24kc_musl/nginx-util-1.6/.built] Error 1
```
