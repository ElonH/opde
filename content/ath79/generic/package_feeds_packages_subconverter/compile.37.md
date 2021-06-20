---
title: "compile.37"
date: 2021-06-20 22:32:33.810914
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
make package/feeds/packages/subconverter/compile -j$(nproc) || make package/feeds/packages/subconverter/compile V=s
```

#### Compile.txt

``` bash
-- The CXX compiler identification is GNU 8.4.0
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-g++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Performing Test HAVE_TO_STRING
-- Performing Test HAVE_TO_STRING - Failed
-- Found PkgConfig: /openwrt/staging_dir/host/bin/pkg-config (found version "1.7.3") 
-- Looking for C++ include pthread.h
-- Looking for C++ include pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
-- Checking for module 'libevent>=2.1.10'
--   Package 'libevent', required by 'virtual:world', not found
CMake Error at /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindPkgConfig.cmake:553 (message):
  A required package was not found
Call Stack (most recent call first):
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindPkgConfig.cmake:741 (_pkg_check_modules_internal)
  CMakeLists.txt:72 (PKG_CHECK_MODULES)


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-mips_24kc_musl/subconverter-0.6.4-2021-03-27-d6cb49fa/CMakeFiles/CMakeOutput.log".
See also "/openwrt/build_dir/target-mips_24kc_musl/subconverter-0.6.4-2021-03-27-d6cb49fa/CMakeFiles/CMakeError.log".
make[3]: *** [Makefile:61: /openwrt/build_dir/target-mips_24kc_musl/subconverter-0.6.4-2021-03-27-d6cb49fa/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
