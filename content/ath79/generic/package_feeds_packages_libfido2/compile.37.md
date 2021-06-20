---
title: "compile.37"
date: 2021-06-20 22:39:07.421506
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
make package/feeds/packages/libfido2/compile -j$(nproc) || make package/feeds/packages/libfido2/compile V=s
```

#### Compile.txt

``` bash
-- The C compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Performing Test CMAKE_C_LINK_PIE_SUPPORTED
-- Performing Test CMAKE_C_LINK_PIE_SUPPORTED - Success
-- Performing Test CMAKE_C_LINK_NO_PIE_SUPPORTED
-- Performing Test CMAKE_C_LINK_NO_PIE_SUPPORTED - Success
-- Found PkgConfig: /openwrt/staging_dir/host/bin/pkg-config (found version "1.7.3") 
-- Checking for one of the modules 'libcbor'
-- Checking for one of the modules 'libcrypto'
-- Looking for include file openssl/opensslv.h
-- Looking for include file openssl/opensslv.h - not found
CMake Error at CMakeLists.txt:106 (message):
  could not find crypto header files


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-mips_24kc_musl/libfido2-1.6.0/CMakeFiles/CMakeOutput.log".
See also "/openwrt/build_dir/target-mips_24kc_musl/libfido2-1.6.0/CMakeFiles/CMakeError.log".
make[3]: *** [Makefile:65: /openwrt/build_dir/target-mips_24kc_musl/libfido2-1.6.0/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
