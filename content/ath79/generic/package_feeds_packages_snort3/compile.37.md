---
title: "compile.37"
date: 2021-06-20 22:23:59.889511
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
make package/feeds/packages/snort3/compile -j$(nproc) || make package/feeds/packages/snort3/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-update-openssl.patch using plaintext: 
patching file src/network_inspectors/appid/appid_inspector.cc
patching file src/utils/util.cc
-- The CXX compiler identification is GNU 8.4.0
-- The C compiler identification is GNU 8.4.0
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-g++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
-- Found PkgConfig: /openwrt/staging_dir/host/bin/pkg-config (found version "1.7.3") 
-- Checking for module 'libdaq>=3.0.2'
--   Package 'libdaq', required by 'virtual:world', not found
-- Found DAQ: /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/daq3/libdaq.so  
-- Found DNET: /openwrt/staging_dir/target-mips_24kc_musl/usr/include  
-- Found FLEX: /openwrt/staging_dir/host/bin/flex (found suitable version "2.6.4", minimum required is "2.6.0") 
-- Checking for module 'hwloc'
--   Found hwloc, version 2.3.0
-- Found HWLOC: /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libhwloc.so  
-- Checking for module 'luajit'
--   Found luajit, version 2.1.0-beta3
-- Found LuaJIT: /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libluajit-5.1.so (found version "2.1.0-beta3") 
CMake Error at /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindPackageHandleStandardArgs.cmake:218 (message):
  Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the
  system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY
  OPENSSL_INCLUDE_DIR)
Call Stack (most recent call first):
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindPackageHandleStandardArgs.cmake:577 (_FPHSA_FAILURE_MESSAGE)
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindOpenSSL.cmake:536 (find_package_handle_standard_args)
  cmake/include_libraries.cmake:9 (find_package)
  CMakeLists.txt:27 (include)


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-mips_24kc_musl/snort3-3.1.4.0/CMakeFiles/CMakeOutput.log".
make[3]: *** [Makefile:106: /openwrt/build_dir/target-mips_24kc_musl/snort3-3.1.4.0/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
