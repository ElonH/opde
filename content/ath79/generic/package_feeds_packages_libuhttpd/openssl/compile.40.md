---
title: "compile.40"
date: 2021-06-22 10:41:19.980517
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
make package/feeds/packages/libuhttpd/compile -j$(nproc) || make package/feeds/packages/libuhttpd/compile V=s
```

#### Compile.txt

``` bash
-- The C compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Found Libev: /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libev.so (found version "4.31") 
-- Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY OPENSSL_INCLUDE_DIR) 
-- Checking for module 'openssl'
--   Package 'openssl', required by 'virtual:world', not found
-- Found WolfSSL: /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libwolfssl.so (found version "4.7.0") 
-- Found MbedTLS: /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libmbedtls.so (found version "2.16.10") 
-- Found ZLIB: /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libz.so (found version "1.2.11") 
CMake Error at src/ssl/CMakeLists.txt:29 (message):
  Force select OpenSSL, but not found it


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-mips_24kc_musl/libuhttpd-openssl/libuhttpd-3.12.1/CMakeFiles/CMakeOutput.log".
make[3]: *** [Makefile:63: /openwrt/build_dir/target-mips_24kc_musl/libuhttpd-openssl/libuhttpd-3.12.1/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
