---
title: "compile.37"
date: 2021-06-20 22:32:33.808030
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
make package/feeds/packages/netopeer2/compile -j$(nproc) || make package/feeds/packages/netopeer2/compile V=s
```

#### Compile.txt

``` bash
-- The C compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Found PkgConfig: /openwrt/staging_dir/host/bin/pkg-config (found version "1.7.3") 
-- Unable to learn libnetconf2 thread support, check skipped
-- Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY OPENSSL_INCLUDE_DIR) 
-- Could NOT find LibSSH (missing: LIBSSH_INCLUDE_DIRS LIBSSH_LIBRARIES) (Required is at least version "0.7.1")
CMake Error at /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindPackageHandleStandardArgs.cmake:218 (message):
  Could NOT find LibNETCONF2 (missing: LIBNETCONF2_LIBRARY
  LIBNETCONF2_INCLUDE_DIR)
Call Stack (most recent call first):
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindPackageHandleStandardArgs.cmake:577 (_FPHSA_FAILURE_MESSAGE)
  CMakeModules/FindLibNETCONF2.cmake:77 (find_package_handle_standard_args)
  CMakeLists.txt:127 (find_package)


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-mips_24kc_musl/netopeer2-1.1.70/CMakeFiles/CMakeOutput.log".
make[3]: *** [Makefile:85: /openwrt/build_dir/target-mips_24kc_musl/netopeer2-1.1.70/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
