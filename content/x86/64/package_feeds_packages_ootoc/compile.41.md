---
title: "compile.41"
date: 2021-06-23 23:18:49.913696
hidden: false
draft: false
weight: -41
---

build number: `41`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/ootoc/compile -j$(nproc) || make package/feeds/packages/ootoc/compile V=s
```

#### Compile.txt

``` bash
-- The C compiler identification is GNU 8.4.0
-- The CXX compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/bin/x86_64-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/bin/x86_64-openwrt-linux-musl-g++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
Looking for libtar.h found in /openwrt/staging_dir/target-x86_64_musl/usr/include
Looking for libtar found in /openwrt/staging_dir/target-x86_64_musl/usr/lib/libtar.so
-- Found CURL: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libcurl.so (found version "7.77.0")  
-- Could NOT find Doxygen (missing: DOXYGEN_EXECUTABLE) 
-- Doxygen not found, building docs has been disabled
CMake Error at lib/CMakeLists.txt:55 (find_package):
  By not providing "Findspdlog.cmake" in CMAKE_MODULE_PATH this project has
  asked CMake to find a package configuration file provided by "spdlog", but
  CMake did not find one.

  Could not find a package configuration file provided by "spdlog" with any
  of the following names:

    spdlogConfig.cmake
    spdlog-config.cmake

  Add the installation prefix of "spdlog" to CMAKE_PREFIX_PATH or set
  "spdlog_DIR" to a directory containing one of the above files.  If "spdlog"
  provides a separate development package or SDK, be sure it has been
  installed.


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-x86_64_musl/ootoc-2.2.3/CMakeFiles/CMakeOutput.log".
make[3]: *** [Makefile:58: /openwrt/build_dir/target-x86_64_musl/ootoc-2.2.3/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
