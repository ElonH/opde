---
title: "compile.19"
date: 2021-05-15 01:43:57.279264
hidden: false
draft: false
weight: -19
---

build number: `19`

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
-- Check for working C compiler: /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/bin/x86_64-openwrt-linux-musl-gcc - skipped
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


-- Build files have been written to: /openwrt/build_dir/target-x86_64_musl/uhttpd-2020-11-23-f53a6399
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/uhttpd-2020-11-23-f53a6399'
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/uhttpd-2020-11-23-f53a6399'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/uhttpd-2020-11-23-f53a6399'
Scanning dependencies of target uhttpd_lua
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/uhttpd-2020-11-23-f53a6399'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/uhttpd-2020-11-23-f53a6399'
[  5%] Building C object CMakeFiles/uhttpd_lua.dir/lua.c.o
In file included from /openwrt/build_dir/target-x86_64_musl/uhttpd-2020-11-23-f53a6399/lua.c:27:
/openwrt/build_dir/target-x86_64_musl/uhttpd-2020-11-23-f53a6399/uhttpd.h:37:10: fatal error: libubox/ustream-ssl.h: No such file or directory
 #include <libubox/ustream-ssl.h>
          ^~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
make[6]: *** [CMakeFiles/uhttpd_lua.dir/build.make:82: CMakeFiles/uhttpd_lua.dir/lua.c.o] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/uhttpd-2020-11-23-f53a6399'
make[5]: *** [CMakeFiles/Makefile2:99: CMakeFiles/uhttpd_lua.dir/all] Error 2
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/uhttpd-2020-11-23-f53a6399'
make[4]: *** [Makefile:149: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/uhttpd-2020-11-23-f53a6399'
make[3]: *** [Makefile:115: /openwrt/build_dir/target-x86_64_musl/uhttpd-2020-11-23-f53a6399/.built] Error 2
```
