---
title: "compile.40"
date: 2021-06-22 10:50:44.064698
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
make package/feeds/telephony/libks/compile -j$(nproc) || make package/feeds/telephony/libks/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/01-find-libm.patch using plaintext: 
patching file cmake/FindLibM.cmake

Applying ./patches/02-correct-signal_h-include.patch using plaintext: 
patching file src/include/libks/ks_platform.h

Applying ./patches/03-fix-flags.patch using plaintext: 
patching file CMakeLists.txt

Applying ./patches/04-don_t-override-optimization.patch using plaintext: 
patching file cmake/ksutil.cmake
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
LibKS Version 1.7
Platform is linux
Build type: Release CXX Flags: 
Install prefix: /usr
-- Found Git: /openwrt/staging_dir/host/bin/git (found version "2.25.1") 
-- Looking for clock_gettime in rt
-- Looking for clock_gettime in rt - found
-- Looking for clock_getres in rt
-- Looking for clock_getres in rt - found
-- Looking for clock_nanosleep in rt
-- Looking for clock_nanosleep in rt - found
-- Looking for strftime in rt
-- Looking for strftime in rt - found
-- Looking for sched_setscheduler in c
-- Looking for sched_setscheduler in c - found
-- Looking for malloc in c
-- Looking for malloc in c - found
-- Looking for usleep in c
-- Looking for usleep in c - found
-- Looking for pthread_setschedparam
-- Looking for pthread_setschedparam - found
-- Looking for memmem
-- Looking for memmem - found
-- Looking for stdlib.h
-- Looking for stdlib.h - found
-- Looking for sys/types.h
-- Looking for sys/types.h - found
-- Looking for sys/stat.h
-- Looking for sys/stat.h - found
-- Looking for string.h
-- Looking for string.h - found
-- Looking for unistd.h
-- Looking for unistd.h - found
-- Looking for memory.h
-- Looking for memory.h - found
-- Looking for strings.h
-- Looking for strings.h - found
-- Looking for inttypes.h
-- Looking for inttypes.h - found
-- Looking for stdint.h
-- Looking for stdint.h - found
-- Looking for dlfcn.h
-- Looking for dlfcn.h - found
-- Looking for sched.h
-- Looking for sched.h - found
-- Looking for byteswap.h
-- Looking for byteswap.h - found
-- Looking for dirent.h
-- Looking for dirent.h - found
-- Found LibM: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libm.a  
-- Found PkgConfig: /openwrt/staging_dir/host/bin/pkg-config (found version "1.7.3") 
-- Checking for module 'uuid'
--   Found uuid, version 2.36.1
Found UUID setup target at imported location: /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libuuid.so
-- Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY OPENSSL_INCLUDE_DIR) 
CMake Error at /openwrt/staging_dir/host/share/cmake-3.20/Modules/FindPackageHandleStandardArgs.cmake:230 (message):
  Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the
  system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY
  OPENSSL_INCLUDE_DIR Crypto SSL)
Call Stack (most recent call first):
  /openwrt/staging_dir/host/share/cmake-3.20/Modules/FindPackageHandleStandardArgs.cmake:594 (_FPHSA_FAILURE_MESSAGE)
  /openwrt/staging_dir/host/share/cmake-3.20/Modules/FindOpenSSL.cmake:570 (find_package_handle_standard_args)
  CMakeLists.txt:420 (find_package)


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-mips_24kc_musl/libks-1.7.0/CMakeFiles/CMakeOutput.log".
make[3]: *** [Makefile:71: /openwrt/build_dir/target-mips_24kc_musl/libks-1.7.0/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
