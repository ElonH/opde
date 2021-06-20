---
title: "compile.37"
date: 2021-06-20 22:36:26.358322
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
make package/feeds/packages/mwol/compile -j$(nproc) || make package/feeds/packages/mwol/compile V=s
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
    CMAKE_FIND_ROOT_PATH_MODE_LIBRARY
    CMAKE_FIND_USE_PACKAGE_REGISTRY
    CMAKE_FIND_USE_SYSTEM_PACKAGE_REGISTRY
    CMAKE_MODULE_LINKER_FLAGS
    CMAKE_SHARED_LINKER_FLAGS
    DL_LIBRARY


-- Build files have been written to: /openwrt/build_dir/target-mips_24kc_musl/mwol-1.0.0
ninja: Entering directory `/openwrt/build_dir/target-mips_24kc_musl/mwol-1.0.0'
[1/8] Building C object src/CMakeFiles/mwol.dir/main.c.o
[2/8] Building C object src/CMakeFiles/mwol.dir/common.c.o
[3/8] Building C object src/CMakeFiles/mwol.dir/config.c.o
[4/8] Building C object src/CMakeFiles/mwol.dir/json.c.o
src/json.c: In function 'json_arp_list':
src/json.c:281:2: warning: 'strncpy' output truncated before terminating nul copying as many bytes from a string as its length [-Wstringop-truncation]
  strncpy(*msg, out, strlen(out));
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
src/json.c: In function 'json_wol_response':
src/json.c:320:2: warning: 'strncpy' output truncated before terminating nul copying as many bytes from a string as its length [-Wstringop-truncation]
  strncpy(*msg, out, strlen(out));
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[5/8] Building C object src/CMakeFiles/mwol.dir/mqtt_client.c.o
[6/8] Building C object src/CMakeFiles/mwol.dir/wake.c.o
src/wake.c: In function 'wake_on_lan':
src/wake.c:217:3: warning: 'strncpy' specified bound 16 equals destination size [-Wstringop-truncation]
   strncpy(ifr.ifr_name, ifname, sizeof(ifr.ifr_name));
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[7/8] Building C object src/CMakeFiles/mwol.dir/cJSON.c.o
[8/8] Linking C executable src/mwol
ninja: Entering directory `/openwrt/build_dir/target-mips_24kc_musl/mwol-1.0.0'
[0/1] Install the project...
-- Install configuration: "Release"
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mwol-1.0.0/ipkg-install/usr/bin/mwol
Package mwol is missing dependencies for the following libraries:
libmosquitto.so.1
make[3]: *** [Makefile:77: /openwrt/bin/packages/mips_24kc/packages/mwol_1.0.0-2_mips_24kc.ipk] Error 1
```
