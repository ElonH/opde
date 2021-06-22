---
title: "compile.40"
date: 2021-06-22 10:49:10.771964
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
make package/feeds/packages/apfree-wifidog/compile -j$(nproc) || make package/feeds/packages/apfree-wifidog/compile V=s
```

#### Compile.txt

``` bash
CMake Deprecation Warning at CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 2.8.12 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- The C compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- libevent NOT found.
CMake Error at CMakeLists.txt:9 (message):
  libevent2 not found!


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-mips_24kc_musl/apfree-wifidog-4.08.1771/CMakeFiles/CMakeOutput.log".
make[3]: *** [Makefile:71: /openwrt/build_dir/target-mips_24kc_musl/apfree-wifidog-4.08.1771/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
