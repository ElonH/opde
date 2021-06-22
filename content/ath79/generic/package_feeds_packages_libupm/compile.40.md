---
title: "compile.40"
date: 2021-06-22 10:45:15.547296
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
make package/feeds/packages/libupm/compile -j$(nproc) || make package/feeds/packages/libupm/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-version.patch using plaintext: 
patching file CMakeLists.txt

Applying ./patches/002-at42qt1070-id.patch using plaintext: 
patching file src/at42qt1070/at42qt1070.cxx

Applying ./patches/003-link-atomic.patch using plaintext: 
patching file src/nmea_gps/CMakeLists.txt

Applying ./patches/004-uint8_t.patch using plaintext: 
patching file src/bma250e/bma250e.cxx
patching file src/bmg160/bmg160.cxx
patching file src/bmm150/bmm150.cxx

Applying ./patches/005-support_v12.patch using plaintext: 
patching file src/carrays_uint32_t.i
CMake Deprecation Warning at CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 2.8.12 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- The C compiler identification is GNU 8.4.0
-- The CXX compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-g++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Warnings as errors enabled (-Werror), disable with -DWERROR=off
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
-- Found PkgConfig: /openwrt/staging_dir/host/bin/pkg-config (found version "1.7.3") 
-- Checking for module 'mraa>=2.0.0'
--   Found mraa, version 2.2.0
-- Looking for mraa_iio_init in mraa
-- Looking for mraa_iio_init in mraa - found
-- Looking for mraa_firmata_init in mraa
-- Looking for mraa_firmata_init in mraa - found
-- Looking for mraa_uart_ow_init in mraa
-- Looking for mraa_uart_ow_init in mraa - found
-- Checking for module 'libbacnet'
--   Package 'libbacnet', required by 'virtual:world', not found
-- Checking for module 'libmodbus>=3.1.2'
--   Found libmodbus, version 3.1.6
-- Checking for module 'libopenzwave'
--   Found libopenzwave, version 1.6
-- Checking for module 'tinyb>=0.5.1'
--   Package 'tinyb', required by 'virtual:world', not found
-- Found JPEG: /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libjpeg.so (found version "62") 
-- Found SWIG: /openwrt/staging_dir/hostpkg/bin/swig (found suitable version "4.0.2", minimum required is "3.0.5")  
-- Found PythonInterp: /usr/bin/python2.7 (found suitable version "2.7.18", minimum required is "2.7") 
-- Could NOT find PythonLibs (missing: PYTHON_LIBRARIES PYTHON_INCLUDE_DIRS) (Required is at least version "2.7")
-- Found PythonInterp: /openwrt/staging_dir/hostpkg/bin/python3 (found suitable version "3.9.5", minimum required is "3") 
-- Could NOT find PythonLibs (missing: PYTHON_LIBRARIES PYTHON_INCLUDE_DIRS) (Required is at least version "3.9")
CMake Error at CMakeLists.txt:211 (message):
  At least one python lib is required


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-mips_24kc_musl/upm-2.0.0/build/CMakeFiles/CMakeOutput.log".
make[3]: *** [Makefile:367: /openwrt/build_dir/target-mips_24kc_musl/upm-2.0.0/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
