---
title: "compile.48"
date: 2021-02-22 14:41:15.179054
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
make package/feeds/packages/cshark/compile -j$(nproc) || make package/feeds/packages/cshark/compile V=s
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
-- Found PkgConfig: /openwrt/staging_dir/host/bin/pkg-config (found version "1.7.3") 
-- Found LIBUBOX: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libubox.so  
CMake Error at /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindPackageHandleStandardArgs.cmake:218 (message):
  Could NOT find LIBUCLIENT (missing: LIBUCLIENT_LIBRARY
  LIBUCLIENT_INCLUDE_DIR)
Call Stack (most recent call first):
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindPackageHandleStandardArgs.cmake:577 (_FPHSA_FAILURE_MESSAGE)
  build/modules/FindLIBUCLIENT.cmake:19 (find_package_handle_standard_args)
  CMakeLists.txt:31 (find_package)


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-x86_64_musl/cshark-2018-08-20-7a7cf7f3/CMakeFiles/CMakeOutput.log".
make[3]: *** [Makefile:65: /openwrt/build_dir/target-x86_64_musl/cshark-2018-08-20-7a7cf7f3/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
