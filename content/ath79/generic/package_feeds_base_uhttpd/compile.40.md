---
title: "compile.40"
date: 2021-06-22 10:50:06.146402
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
make package/feeds/base/uhttpd/compile -j$(nproc) || make package/feeds/base/uhttpd/compile V=s
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
-- Looking for getspnam
-- Looking for getspnam - found
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
    CMAKE_SHARED_LINKER_FLAGS
    DL_LIBRARY


-- Build files have been written to: /openwrt/build_dir/target-mips_24kc_musl/uhttpd-2021-03-21-15346de8
ninja: Entering directory `/openwrt/build_dir/target-mips_24kc_musl/uhttpd-2021-03-21-15346de8'
[1/17] Building C object CMakeFiles/uhttpd_lua.dir/lua.c.o
FAILED: CMakeFiles/uhttpd_lua.dir/lua.c.o 
/openwrt/staging_dir/host/bin/ccache /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc -DHAVE_LUA -DHAVE_SHADOW -DHAVE_TLS -DHAVE_UBUS -D_FILE_OFFSET_BITS=64 -Duhttpd_lua_EXPORTS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/uhttpd-2021-03-21-15346de8=uhttpd-2021-03-21-15346de8 -Wformat -Werror=format-security -DPIC -fpic -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DNDEBUG -fPIC   -Os -Wall -Werror -Wmissing-declarations --std=gnu99 -g3 -MD -MT CMakeFiles/uhttpd_lua.dir/lua.c.o -MF CMakeFiles/uhttpd_lua.dir/lua.c.o.d -o CMakeFiles/uhttpd_lua.dir/lua.c.o -c lua.c
In file included from lua.c:27:
uhttpd.h:37:10: fatal error: libubox/ustream-ssl.h: No such file or directory
 #include <libubox/ustream-ssl.h>
          ^~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
ninja: build stopped: subcommand failed.
make[3]: *** [Makefile:115: /openwrt/build_dir/target-mips_24kc_musl/uhttpd-2021-03-21-15346de8/.built] Error 1
```
