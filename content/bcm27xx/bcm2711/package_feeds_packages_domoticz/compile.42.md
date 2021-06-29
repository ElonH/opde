---
title: "compile.42"
date: 2021-06-29 09:40:48.073335
hidden: false
draft: false
weight: -42
---

build number: `42`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/domoticz/compile -j$(nproc) || make package/feeds/packages/domoticz/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/012-minizip-overflow.patch using plaintext: 
patching file main/unzip_stream.h
-- The C compiler identification is GNU 8.4.0
-- The CXX compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/bin/aarch64-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/bin/aarch64-openwrt-linux-musl-g++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
fatal: not a git repository: './.git'
-- Failed to get ProjectRevision from git
-- Read ProjectRevision from History.txt
-- LUA library found at: /openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/liblua5.3.so
-- Found PythonInterp: /openwrt/staging_dir/hostpkg/bin/python3 (found suitable version "3.9.5", minimum required is "3.4") 
-- Found PythonLibs: /openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libpython3.9.so (found suitable version "3.9.5", minimum required is "3.4") 
-- Python3 includes found at: /openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include/python3.9
-- Looking for execinfo.h
-- Looking for execinfo.h - not found
-- Looking for 3 include files sys/types.h, ..., linux/i2c.h
-- Looking for 3 include files sys/types.h, ..., linux/i2c.h - found
-- Building with I2C support
-- Looking for include files sys/types.h, linux/spi/spidev.h
-- Looking for include files sys/types.h, linux/spi/spidev.h - found
-- Building with SPI support
-- ###########################
-- Compiling Revision #1
-- ###########################
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
-- Check if the system is big endian - little endian
-- Found PkgConfig: /openwrt/staging_dir/host/bin/pkg-config (found version "1.7.3") 
-- Checking for module 'jsoncpp'
--   Package 'jsoncpp', required by 'virtual:world', not found
CMake Error at /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindPkgConfig.cmake:553 (message):
  A required package was not found
Call Stack (most recent call first):
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindPkgConfig.cmake:741 (_pkg_check_modules_internal)
  CMakeLists.txt:517 (pkg_check_modules)


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-aarch64_cortex-a72_musl/domoticz-2021.1/CMakeFiles/CMakeOutput.log".
See also "/openwrt/build_dir/target-aarch64_cortex-a72_musl/domoticz-2021.1/CMakeFiles/CMakeError.log".
make[3]: *** [Makefile:134: /openwrt/build_dir/target-aarch64_cortex-a72_musl/domoticz-2021.1/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
