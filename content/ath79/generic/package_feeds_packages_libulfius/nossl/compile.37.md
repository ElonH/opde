---
title: "compile.37"
date: 2021-06-20 22:38:00.056712
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
make package/feeds/packages/libulfius/compile -j$(nproc) || make package/feeds/packages/libulfius/compile V=s
```

#### Compile.txt

``` bash
-- The C compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Looking for __GNU_LIBRARY__
-- Looking for __GNU_LIBRARY__ - not found
-- Looking for _GNU_SOURCE
-- Looking for _GNU_SOURCE - not found
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
-- Found MHD: /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libmicrohttpd.so (found version "0.9.73") 
-- Found MHD: /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libmicrohttpd.so (found suitable version "0.9.73", minimum required is "0.9.51") 
-- Could NOT find CURL (missing: CURL_LIBRARY CURL_INCLUDE_DIR) 
CMake Error at /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindPackageHandleStandardArgs.cmake:218 (message):
  Could NOT find CURL (missing: CURL_LIBRARY CURL_INCLUDE_DIR)
Call Stack (most recent call first):
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindPackageHandleStandardArgs.cmake:577 (_FPHSA_FAILURE_MESSAGE)
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindCURL.cmake:171 (find_package_handle_standard_args)
  CMakeLists.txt:172 (find_package)


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-mips_24kc_musl/libulfius-2.7.2-nossl/ulfius-2.7.2/CMakeFiles/CMakeOutput.log".
See also "/openwrt/build_dir/target-mips_24kc_musl/libulfius-2.7.2-nossl/ulfius-2.7.2/CMakeFiles/CMakeError.log".
make[3]: *** [Makefile:73: /openwrt/build_dir/target-mips_24kc_musl/libulfius-2.7.2-nossl/ulfius-2.7.2/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
