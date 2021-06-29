---
title: "compile.42"
date: 2021-06-29 09:40:48.062924
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
make package/feeds/packages/libgd/compile -j$(nproc) || make package/feeds/packages/libgd/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-webp.patch using plaintext: 
patching file CMakeLists.txt

Applying ./patches/100-no-cxx.patch using plaintext: 
patching file src/CMakeLists.txt
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
-- gd version 2.3.2
-- gd shared lib version 3 (3.0.10)
-- Looking for include file dirent.h
-- Looking for include file dirent.h - found
-- Looking for include file inttypes.h
-- Looking for include file inttypes.h - found
-- Looking for include file stdint.h
-- Looking for include file stdint.h - found
-- Looking for include file strings.h
-- Looking for include file strings.h - found
-- Looking for include file unistd.h
-- Looking for include file unistd.h - found
-- Looking for include file sys/stat.h
-- Looking for include file sys/stat.h - found
-- Looking for include file sys/types.h
-- Looking for include file sys/types.h - found
-- Found ZLIB: /openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libz.so  
-- Found PNG: /openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libpng.so (found version "1.6.37") 
-- Found JPEG: /openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libjpeg.so (found version "62") 
-- Found TIFF: /openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libtiff.so (found version "4.3.0")  
CMake Error at /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindPackageHandleStandardArgs.cmake:218 (message):
  Could NOT find Freetype (missing: FREETYPE_LIBRARY)
Call Stack (most recent call first):
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindPackageHandleStandardArgs.cmake:577 (_FPHSA_FAILURE_MESSAGE)
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindFreetype.cmake:157 (find_package_handle_standard_args)
  CMakeLists.txt:152 (FIND_PACKAGE)


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-aarch64_cortex-a72_musl/libgd-full/libgd-2.3.2/CMakeFiles/CMakeOutput.log".
make[3]: *** [Makefile:128: /openwrt/build_dir/target-aarch64_cortex-a72_musl/libgd-full/libgd-2.3.2/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
