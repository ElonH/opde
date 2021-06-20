---
title: "compile.37"
date: 2021-06-20 22:39:07.399665
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
make package/feeds/packages/znc/compile -j$(nproc) || make package/feeds/packages/znc/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/101-Reduce_rebuild_time.patch using plaintext: 
patching file Makefile.in
patching file modules/Makefile.in

Applying ./patches/104-disable-empty-modules-check.patch using plaintext: 
patching file src/main.cpp

Applying ./patches/110-add-playback-module.patch using plaintext: 
patching file modules/playback.cpp

Applying ./patches/120-openssl-deprecated.patch using plaintext: 
patching file third_party/Csocket/Csocket.cc
-- The CXX compiler identification is GNU 8.4.0
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-g++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Checking for C++11 support
-- Checking for C++11 support - supported
-- Looking for C++ include pthread.h
-- Looking for C++ include pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
-- Checking for 64-bit off_t
-- Checking for 64-bit off_t - present
-- Checking for fseeko/ftello
-- Checking for fseeko/ftello - present
-- Found PkgConfig: /openwrt/staging_dir/host/bin/pkg-config (found version "1.7.3") 
CMake Error at /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindPackageHandleStandardArgs.cmake:218 (message):
  Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the
  system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY
  OPENSSL_INCLUDE_DIR)
Call Stack (most recent call first):
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindPackageHandleStandardArgs.cmake:577 (_FPHSA_FAILURE_MESSAGE)
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindOpenSSL.cmake:536 (find_package_handle_standard_args)
  CMakeLists.txt:84 (find_package)


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-mips_24kc_musl/znc-1.8.2/CMakeFiles/CMakeOutput.log".
make[3]: *** [Makefile:294: /openwrt/build_dir/target-mips_24kc_musl/znc-1.8.2/.configured_7d392e48e0a0f5461a23892c5be6bd83] Error 1
```
