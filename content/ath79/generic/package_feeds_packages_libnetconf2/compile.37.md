---
title: "compile.37"
date: 2021-06-20 22:32:33.817819
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
make package/feeds/packages/libnetconf2/compile -j$(nproc) || make package/feeds/packages/libnetconf2/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-cmake_not_updated.patch using plaintext: 
patching file CMakeLists.txt
-- The C compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Looking for vdprintf
-- Looking for vdprintf - found
-- Looking for asprintf
-- Looking for asprintf - found
-- Looking for vasprintf
-- Looking for vasprintf - found
-- Looking for get_current_dir_name
-- Looking for get_current_dir_name - found
-- Looking for strndup
-- Looking for strndup - found
-- Looking for getline
-- Looking for getline - found
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
-- Check if the system is big endian - big endian
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
-- Looking for stdatomic.h
-- Looking for stdatomic.h - found
-- Looking for pthread_mutex_timedlock
-- Looking for pthread_mutex_timedlock - found
-- Looking for pthread_rwlockattr_setkind_np
-- Looking for pthread_rwlockattr_setkind_np - not found
CMake Error at /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindPackageHandleStandardArgs.cmake:218 (message):
  Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the
  system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY
  OPENSSL_INCLUDE_DIR)
Call Stack (most recent call first):
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindPackageHandleStandardArgs.cmake:577 (_FPHSA_FAILURE_MESSAGE)
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindOpenSSL.cmake:536 (find_package_handle_standard_args)
  CMakeLists.txt:170 (find_package)


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-mips_24kc_musl/libnetconf2-1.1.43/CMakeFiles/CMakeOutput.log".
See also "/openwrt/build_dir/target-mips_24kc_musl/libnetconf2-1.1.43/CMakeFiles/CMakeError.log".
make[3]: *** [Makefile:52: /openwrt/build_dir/target-mips_24kc_musl/libnetconf2-1.1.43/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
