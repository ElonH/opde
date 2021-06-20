---
title: "compile.37"
date: 2021-06-20 22:38:00.055934
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
make package/feeds/packages/taskwarrior/compile -j$(nproc) || make package/feeds/packages/taskwarrior/compile V=s
```

#### Compile.txt

``` bash
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
-- Configuring C++17
-- System: Linux
-- Performing Test _HAS_CXX17
-- Performing Test _HAS_CXX17 - Success
-- Looking for libshared
-- Found libshared
-- Looking for SHA1 references
-- Looking for GnuTLS
-- Could NOT find GnuTLS (missing: GNUTLS_LIBRARY GNUTLS_INCLUDE_DIR) 
CMake Error at CMakeLists.txt:79 (message):
  Cannot find GnuTLS.  Use -DENABLE_SYNC=OFF to build Taskwarrior without
  sync support.  See INSTALL for more information.


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-mips_24kc_musl/task-2.5.3/CMakeFiles/CMakeOutput.log".
make[3]: *** [Makefile:48: /openwrt/build_dir/target-mips_24kc_musl/task-2.5.3/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
