---
title: "compile.40"
date: 2021-06-22 10:46:12.816646
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
make package/feeds/packages/stubby/compile -j$(nproc) || make package/feeds/packages/stubby/compile V=s
```

#### Compile.txt

``` bash
-- The C compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Could NOT find Libsystemd (missing: LIBSYSTEMD_LIBRARIES LIBSYSTEMD_INCLUDE_DIR) 
-- Found Libyaml: /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libyaml.so  
-- Looking for os/log.h
-- Looking for os/log.h - not found
-- Looking for inttypes.h
-- Looking for inttypes.h - found
-- Looking for sys/types.h
-- Looking for sys/types.h - found
-- Looking for getopt
-- Looking for getopt - found
CMake Error at /openwrt/staging_dir/host/share/cmake-3.20/Modules/FindPackageHandleStandardArgs.cmake:230 (message):
  Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the
  system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY
  OPENSSL_INCLUDE_DIR) (Required is at least version "1.0.2")
Call Stack (most recent call first):
  /openwrt/staging_dir/host/share/cmake-3.20/Modules/FindPackageHandleStandardArgs.cmake:594 (_FPHSA_FAILURE_MESSAGE)
  /openwrt/staging_dir/host/share/cmake-3.20/Modules/FindOpenSSL.cmake:570 (find_package_handle_standard_args)
  cmake/modules/FindGetdns.cmake:61 (find_package)
  CMakeLists.txt:181 (find_package)


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-mips_24kc_musl/stubby-0.4.0/CMakeFiles/CMakeOutput.log".
See also "/openwrt/build_dir/target-mips_24kc_musl/stubby-0.4.0/CMakeFiles/CMakeError.log".
make[3]: *** [Makefile:70: /openwrt/build_dir/target-mips_24kc_musl/stubby-0.4.0/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
