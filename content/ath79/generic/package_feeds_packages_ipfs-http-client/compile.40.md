---
title: "compile.40"
date: 2021-06-22 10:51:10.649892
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
make package/feeds/packages/ipfs-http-client/compile -j$(nproc) || make package/feeds/packages/ipfs-http-client/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-add-srv-addr.patch using plaintext: 
patching file test/test_block.cc
patching file test/test_config.cc
patching file test/test_dht.cc
patching file test/test_error.cc
patching file test/test_files.cc
patching file test/test_generic.cc
patching file test/test_key.cc
patching file test/test_name.cc
patching file test/test_object.cc
patching file test/test_pin.cc
patching file test/test_swarm.cc
-- The CXX compiler identification is GNU 8.4.0
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-g++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
CMake Error at /openwrt/staging_dir/host/share/cmake-3.20/Modules/FindPackageHandleStandardArgs.cmake:230 (message):
  Could NOT find CURL (missing: CURL_LIBRARY CURL_INCLUDE_DIR)
Call Stack (most recent call first):
  /openwrt/staging_dir/host/share/cmake-3.20/Modules/FindPackageHandleStandardArgs.cmake:594 (_FPHSA_FAILURE_MESSAGE)
  /openwrt/staging_dir/host/share/cmake-3.20/Modules/FindCURL.cmake:181 (find_package_handle_standard_args)
  CMakeLists.txt:26 (find_package)


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-mips_24kc_musl/ipfs-http-client-2021-03-01-27f64393/CMakeFiles/CMakeOutput.log".
make[3]: *** [Makefile:85: /openwrt/build_dir/target-mips_24kc_musl/ipfs-http-client-2021-03-01-27f64393/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
