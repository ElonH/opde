---
title: "compile.37"
date: 2021-06-20 22:36:26.343424
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
make package/feeds/packages/gost_engine/compile -j$(nproc) || make package/feeds/packages/gost_engine/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-openssl-deprecated.patch using plaintext: 
patching file gost_pmeth.c
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
-- Check if the system is big endian
-- Searching 16 bit integer
-- Looking for sys/types.h
-- Looking for sys/types.h - found
-- Looking for stdint.h
-- Looking for stdint.h - found
-- Looking for stddef.h
-- Looking for stddef.h - found
-- Check size of unsigned short
-- Check size of unsigned short - done
-- Searching 16 bit integer - Using unsigned short
-- Check if the system is big endian - big endian
-- BIG_ENDIAN
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
    CMAKE_FIND_USE_PACKAGE_REGISTRY
    CMAKE_FIND_USE_SYSTEM_PACKAGE_REGISTRY
    CMAKE_SHARED_LINKER_FLAGS
    DL_LIBRARY
    OPENSSL_ENGINES_DIR


-- Build files have been written to: /openwrt/build_dir/target-mips_24kc_musl/gost_engine-1.1.0.3
ninja: Entering directory `/openwrt/build_dir/target-mips_24kc_musl/gost_engine-1.1.0.3'
[1/28] Building C object CMakeFiles/gostsum.dir/gostsum.c.o
[2/28] Building C object CMakeFiles/gost12sum.dir/gost12sum.c.o
[3/28] Building C object CMakeFiles/gost_engine.dir/e_gost_err.c.o
FAILED: CMakeFiles/gost_engine.dir/e_gost_err.c.o 
/openwrt/staging_dir/host/bin/ccache /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc -Dgost_engine_EXPORTS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gost_engine-1.1.0.3=gost_engine-1.1.0.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -O2 -Werror -Wall -Wno-unused-parameter -Wno-unused-function -Wno-missing-braces -ggdb -DNDEBUG -fPIC -MD -MT CMakeFiles/gost_engine.dir/e_gost_err.c.o -MF CMakeFiles/gost_engine.dir/e_gost_err.c.o.d -o CMakeFiles/gost_engine.dir/e_gost_err.c.o -c e_gost_err.c
e_gost_err.c:63:10: fatal error: openssl/err.h: No such file or directory
 #include <openssl/err.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
ninja: build stopped: subcommand failed.
make[3]: *** [Makefile:81: /openwrt/build_dir/target-mips_24kc_musl/gost_engine-1.1.0.3/.built] Error 1
```
