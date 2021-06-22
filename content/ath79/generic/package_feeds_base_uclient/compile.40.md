---
title: "compile.40"
date: 2021-06-22 10:50:06.147869
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
make package/feeds/base/uclient/compile -j$(nproc) || make package/feeds/base/uclient/compile V=s
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
CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
ubox_include_dir
   used as include directory in directory /openwrt/build_dir/target-mips_24kc_musl/uclient-2021-05-14-6a6011df
   used as include directory in directory /openwrt/build_dir/target-mips_24kc_musl/uclient-2021-05-14-6a6011df
   used as include directory in directory /openwrt/build_dir/target-mips_24kc_musl/uclient-2021-05-14-6a6011df
   used as include directory in directory /openwrt/build_dir/target-mips_24kc_musl/uclient-2021-05-14-6a6011df
   used as include directory in directory /openwrt/build_dir/target-mips_24kc_musl/uclient-2021-05-14-6a6011df
   used as include directory in directory /openwrt/build_dir/target-mips_24kc_musl/uclient-2021-05-14-6a6011df
   used as include directory in directory /openwrt/build_dir/target-mips_24kc_musl/uclient-2021-05-14-6a6011df
   used as include directory in directory /openwrt/build_dir/target-mips_24kc_musl/uclient-2021-05-14-6a6011df

CMake Warning (dev) in CMakeLists.txt:
  Policy CMP0021 is not set: Fatal error on relative paths in
  INCLUDE_DIRECTORIES target property.  Run "cmake --help-policy CMP0021" for
  policy details.  Use the cmake_policy command to set the policy and
  suppress this warning.

  Found relative path while evaluating include directories of
  "uclient-fetch":

    "ubox_include_dir-NOTFOUND"

This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) in CMakeLists.txt:
  Policy CMP0021 is not set: Fatal error on relative paths in
  INCLUDE_DIRECTORIES target property.  Run "cmake --help-policy CMP0021" for
  policy details.  Use the cmake_policy command to set the policy and
  suppress this warning.

  Found relative path while evaluating include directories of "uclient":

    "ubox_include_dir-NOTFOUND"

This warning is for project developers.  Use -Wno-dev to suppress it.

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


CMake Generate step failed.  Build files cannot be regenerated correctly.
make[3]: *** [Makefile:55: /openwrt/build_dir/target-mips_24kc_musl/uclient-2021-05-14-6a6011df/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
