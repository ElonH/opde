---
title: "compile.40"
date: 2021-06-22 10:50:44.065017
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
make package/feeds/telephony/signalwire-client-c/compile -j$(nproc) || make package/feeds/telephony/signalwire-client-c/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/01-set-libks-cmake-dir.patch using plaintext: 
patching file cmake/FindLibKS.cmake
-- cotire 1.7.10 loaded.
-- The C compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
SignalWire-Client-C 1.3
-- Found PkgConfig: /openwrt/staging_dir/host/bin/pkg-config (found version "1.7.3") 
-- Checking for module 'libks'
--   Package 'libks', required by 'virtual:world', not found
CMake Error at /openwrt/staging_dir/host/share/cmake-3.20/Modules/FindPkgConfig.cmake:556 (message):
  A required package was not found
Call Stack (most recent call first):
  /openwrt/staging_dir/host/share/cmake-3.20/Modules/FindPkgConfig.cmake:778 (_pkg_check_modules_internal)
  cmake/FindLibKS.cmake:14 (pkg_check_modules)
  CMakeLists.txt:28 (include)


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-mips_24kc_musl/signalwire-c-1.3.0/CMakeFiles/CMakeOutput.log".
make[3]: *** [Makefile:73: /openwrt/build_dir/target-mips_24kc_musl/signalwire-c-1.3.0/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
