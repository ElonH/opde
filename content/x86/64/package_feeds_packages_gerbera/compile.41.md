---
title: "compile.41"
date: 2021-06-23 23:25:01.766679
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
make package/feeds/packages/gerbera/compile -j$(nproc) || make package/feeds/packages/gerbera/compile V=s
```

#### Compile.txt

``` bash
-- The CXX compiler identification is GNU 8.4.0
-- The C compiler identification is GNU 8.4.0
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/bin/x86_64-openwrt-linux-musl-g++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/bin/x86_64-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Gerbera Version: 1.8.2
-- Looking for C++ include optional
-- Looking for C++ include optional - found
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
-- Looking for __atomic_fetch_add_4 in atomic
-- Looking for __atomic_fetch_add_4 in atomic - found
-- Looking for C++ include filesystem
-- Looking for C++ include filesystem - found
-- Performing Test CXX_FILESYSTEM_NO_LINK_NEEDED
-- Performing Test CXX_FILESYSTEM_NO_LINK_NEEDED - Failed
-- Performing Test CXX_FILESYSTEM_STDCPPFS_NEEDED
-- Performing Test CXX_FILESYSTEM_STDCPPFS_NEEDED - Success
-- Found Iconv: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib/libiconv.a  
-- Looking for BSD native UUID
-- Looking for libuuid
-- Looking for libuuid - found
-- Found libuuid: TRUE  
-- Looking for native LFS support
-- Looking for native LFS support - found
-- Found LFS: TRUE  
CMake Error at /openwrt/staging_dir/host/share/cmake-3.20/Modules/FindPackageHandleStandardArgs.cmake:230 (message):
  Could NOT find spdlog (missing: spdlog_LIBRARY spdlog_INCLUDE_DIR)
Call Stack (most recent call first):
  /openwrt/staging_dir/host/share/cmake-3.20/Modules/FindPackageHandleStandardArgs.cmake:594 (_FPHSA_FAILURE_MESSAGE)
  cmake/Findspdlog.cmake:27 (find_package_handle_standard_args)
  CMakeLists.txt:400 (find_package)


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-x86_64_musl/gerbera-1.8.2/CMakeFiles/CMakeOutput.log".
See also "/openwrt/build_dir/target-x86_64_musl/gerbera-1.8.2/CMakeFiles/CMakeError.log".
make[3]: *** [Makefile:90: /openwrt/build_dir/target-x86_64_musl/gerbera-1.8.2/.configured_09f4147509b3be2b1b7c074f234880e3] Error 1
```
