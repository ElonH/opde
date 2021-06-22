---
title: "compile.40"
date: 2021-06-22 10:37:31.206168
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
make package/feeds/packages/libtorrent-rasterbar/compile -j$(nproc) || make package/feeds/packages/libtorrent-rasterbar/compile V=s
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
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
-- Performing Test HAVE_CXX_ATOMICS_WITHOUT_LIB
-- Performing Test HAVE_CXX_ATOMICS_WITHOUT_LIB - Success
-- Performing Test HAVE_CXX_ATOMICS64_WITHOUT_LIB
-- Performing Test HAVE_CXX_ATOMICS64_WITHOUT_LIB - Failed
-- Performing Test HAVE_CXX_ATOMICS_WITH_LIB
-- Performing Test HAVE_CXX_ATOMICS_WITH_LIB - Success
-- Performing Test HAVE_CXX_ATOMICS64_WITH_LIB
-- Performing Test HAVE_CXX_ATOMICS64_WITH_LIB - Success
-- Linking with libatomic for atomics support
-- Performing Test Iconv_IS_BUILT_IN
-- Performing Test Iconv_IS_BUILT_IN - Success
-- Found Iconv: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/libc.so  
-- Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY OPENSSL_INCLUDE_DIR) 
-- Found LibGcrypt: /openwrt/staging_dir/target-mips_24kc_musl/usr/include (found version "1.9.3") 
-- Warning: Property DESCRIPTION for package LibGcrypt already set to "General purpose crypto library based on the code used in GnuPG.", overriding it with "A general purpose cryptographic library"
-- Warning: Property URL already set to "http://directory.fsf.org/wiki/Libgcrypt", overriding it with "https://www.gnupg.org/software/libgcrypt/index.html"
-- Found Boost: /openwrt/staging_dir/hostpkg/lib/cmake/Boost-1.76.0/BoostConfig.cmake (found version "1.76.0")  
-- The following features have been enabled:

 * BUILD_SHARED_LIBS, build libtorrent as a shared library
 * dht, enable support for Mainline DHT
 * deprecated-functions, enable deprecated functions for backwards compatibility
 * encryption, Enables encryption in libtorrent
 * exceptions, build with exception support
 * extensions, Enables protocol extensions
 * i2p, build with I2P support
 * logging, build with logging
 * mutable-torrents, Enables mutable torrent support
 * streaming, Enables support for piece deadline

-- The following RECOMMENDED packages have been found:

 * Iconv, GNU encoding conversion library, <https://www.gnu.org/software/libiconv/>
   Convert strings between various encodings
 * LibGcrypt, A general purpose cryptographic library, <https://www.gnupg.org/software/libgcrypt/index.html>
   Use GCrypt instead of the built-in functions for RC4 and SHA1

-- The following REQUIRED packages have been found:

 * Threads
 * boost_headers (required version == 1.76.0)
 * Boost

-- The following features have been disabled:

 * static_runtime, build libtorrent with static runtime
 * build_tests, build tests
 * build_examples, build examples
 * build_tools, build tools
 * python-bindings, build python bindings
 * python-egg-info, generate python egg info
 * python-install-system-dir, Install python bindings to the system installation directory rather than the CMake installation prefix

-- The following RECOMMENDED packages have not been found:

 * OpenSSL, Full-strength general purpose cryptography library, <https://www.openssl.org/>
   Provides HTTPS support to libtorrent

-- Configuring done
CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/web_connection_base.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/alert.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/alert_manager.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/announce_entry.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/assert.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/bandwidth_limit.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/bandwidth_manager.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/bandwidth_queue_entry.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/bdecode.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/bitfield.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/block_cache.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/bloom_filter.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/chained_buffer.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/choker.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/close_reason.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/cpuid.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/crc32c.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/create_torrent.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/disk_buffer_holder.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/entry.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/error_code.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/file_storage.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/file_progress.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/generate_peer_id.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/lazy_bdecode.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/escape_string.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/string_util.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/file.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/path.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/fingerprint.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/gzip.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/hasher.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/sha1.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/hex.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/http_connection.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/http_stream.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/http_parser.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/i2p_stream.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/identify_client.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/ip_filter.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/ip_notifier.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/ip_voter.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/listen_socket_handle.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/performance_counters.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/peer_class.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/peer_class_set.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/peer_connection.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/bt_peer_connection.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/web_peer_connection.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/http_seed_connection.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/peer_connection_handle.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/instantiate_connection.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/merkle.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/natpmp.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/openssl.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/part_file.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/packet_buffer.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/piece_picker.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/platform_util.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/proxy_base.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/peer_list.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/puff.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/random.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/receive_buffer.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/read_resume_data.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/write_resume_data.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/request_blocks.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/resolve_links.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/resolver.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/session.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/session_call.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/session_handle.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/session_impl.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/session_settings.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/proxy_settings.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/session_stats.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/settings_pack.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/sha1_hash.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/socket_io.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/socket_type.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/socks5_stream.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/stat.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/stat_cache.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/storage.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/storage_piece_set.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/storage_utils.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/time.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/timestamp_history.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/torrent.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/torrent_handle.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/torrent_info.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/torrent_peer.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/torrent_peer_allocator.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/torrent_status.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/tracker_manager.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/http_tracker_connection.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/utf8.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/udp_tracker_connection.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/udp_socket.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/upnp.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/utp_socket_manager.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/utp_stream.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/file_pool.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/lsd.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/disk_io_job.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/disk_job_fence.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/disk_job_pool.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/disk_buffer_pool.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/disk_io_thread.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/disk_io_thread_pool.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/enum_net.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/broadcast_socket.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/magnet_uri.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/parse_url.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/xml_parse.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/version.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/ffs.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/add_torrent_params.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/peer_info.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/stack_allocator.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/ut_pex.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/ut_metadata.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/smart_ban.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/add_torrent_params.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/address.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/alert.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/alert_manager.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/alert_types.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/announce_entry.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/assert.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/bandwidth_limit.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/bandwidth_manager.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/bandwidth_queue_entry.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/bandwidth_socket.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/bdecode.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/bencode.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/bitfield.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/block_cache.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/bloom_filter.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/broadcast_socket.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/bt_peer_connection.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/buffer.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/chained_buffer.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/choker.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/close_reason.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/config.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/copy_ptr.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/crc32c.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/create_torrent.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/deadline_timer.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/debug.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/disk_buffer_holder.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/disk_buffer_pool.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/disk_interface.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/disk_io_job.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/disk_io_thread.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/disk_io_thread_pool.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/disk_job_pool.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/disk_observer.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/download_priority.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/ed25519.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/entry.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/enum_net.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/error.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/error_code.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/file.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/file_pool.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/file_storage.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/fingerprint.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/flags.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/fwd.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/gzip.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/hasher.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/hasher512.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/heterogeneous_queue.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/hex.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/http_connection.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/http_parser.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/http_seed_connection.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/http_stream.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/http_tracker_connection.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/i2p_stream.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/identify_client.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/index_range.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/invariant_check.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/io.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/io_service.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/io_service_fwd.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/ip_filter.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/ip_voter.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/lazy_entry.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/link.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/linked_list.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/lsd.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/magnet_uri.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/natpmp.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/netlink.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/operations.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/optional.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/packet_buffer.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/packet_pool.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/parse_url.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/part_file.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/pe_crypto.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/peer.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/peer_class.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/peer_class_set.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/peer_class_type_filter.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/peer_connection.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/peer_connection_handle.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/peer_connection_interface.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/peer_id.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/peer_info.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/peer_list.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/peer_request.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/performance_counters.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/pex_flags.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/piece_block.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/piece_block_progress.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/piece_picker.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/platform_util.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/portmap.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/proxy_base.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/puff.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/random.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/read_resume_data.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/receive_buffer.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/request_blocks.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/resolve_links.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/resolver.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/resolver_interface.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/session.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/session_handle.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/session_settings.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/session_stats.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/session_status.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/session_types.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/settings_pack.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/sha1.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/sha1_hash.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/sha512.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/sliding_average.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/socket.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/socket_io.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/socks5_stream.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/span.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/ssl_stream.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/stack_allocator.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/stat.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/stat_cache.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/storage.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/storage_defs.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/string_util.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/string_view.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/tailqueue.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/time.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/timestamp_history.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/torrent.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/torrent_flags.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/torrent_handle.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/torrent_info.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/torrent_peer.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/torrent_peer_allocator.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/torrent_status.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/tracker_manager.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/udp_socket.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/udp_tracker_connection.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/union_endpoint.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/units.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/upnp.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/utf8.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/utp_socket_manager.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/utp_stream.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/vector_utils.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/version.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/web_connection_base.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/web_peer_connection.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/write_resume_data.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/xml_parse.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/extensions/smart_ban.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/extensions/ut_metadata.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/extensions/ut_pex.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/aligned_storage.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/aligned_union.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/alloca.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/allocating_handler.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/array.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/bind_to_device.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/keepalive.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/block_cache_reference.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/byteswap.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/cppint_import_export.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/cpuid.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/deferred_handler.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/deprecated.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/deque.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/dev_random.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/disable_warnings_pop.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/disable_warnings_push.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/disk_job_fence.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/escape_string.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/export.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/ffs.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/file_progress.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/has_block.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/instantiate_connection.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/io.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/ip_notifier.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/listen_socket_handle.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/lsd.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/merkle.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/noexcept_movable.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/numeric_cast.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/openssl.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/path.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/pool.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/portmap.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/proxy_settings.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/range.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/route.h
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/scope_end.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/session_call.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/session_impl.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/session_interface.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/session_settings.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/session_udp_sockets.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/set_socket_buffer.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/socket_type.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/storage_piece_set.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/storage_utils.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/string_ptr.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/suggest_piece.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/throw.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/time.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/torrent_impl.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/unique_ptr.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/vector.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/win_crypto_provider.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/aux_/win_util.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/pe_crypto.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/kademlia/dht_state.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/kademlia/dht_storage.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/kademlia/dos_blocker.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/kademlia/dht_tracker.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/kademlia/msg.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/kademlia/node.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/kademlia/node_entry.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/kademlia/refresh.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/kademlia/rpc_manager.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/kademlia/find_data.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/kademlia/put_data.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/kademlia/node_id.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/kademlia/routing_table.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/kademlia/traversal_algorithm.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/kademlia/item.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/kademlia/get_peers.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/kademlia/get_item.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/kademlia/ed25519.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/kademlia/sample_infohashes.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/kademlia/dht_settings.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ed25519/src/add_scalar.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ed25519/src/fe.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ed25519/src/ge.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ed25519/src/key_exchange.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ed25519/src/keypair.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ed25519/src/sc.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ed25519/src/sign.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ed25519/src/verify.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/kademlia/announce_flags.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/kademlia/dht_observer.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/kademlia/dht_settings.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/kademlia/dht_state.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/kademlia/dht_storage.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/kademlia/dht_tracker.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/kademlia/direct_request.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/kademlia/dos_blocker.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/kademlia/ed25519.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/kademlia/find_data.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/kademlia/get_item.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/kademlia/get_peers.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/kademlia/io.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/kademlia/item.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/kademlia/msg.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/kademlia/node.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/kademlia/node_entry.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/kademlia/node_id.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/kademlia/observer.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/kademlia/put_data.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/kademlia/refresh.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/kademlia/routing_table.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/kademlia/rpc_manager.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/kademlia/sample_infohashes.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/kademlia/traversal_algorithm.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/include/libtorrent/kademlia/types.hpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/hasher512.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:506 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/src/sha512.cpp
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Generating done
CMake Warning:
  Manually-specified variables were not used by the project:

    CMAKE_ASM_COMPILER
    CMAKE_ASM_COMPILER_LAUNCHER
    CMAKE_EXPORT_NO_PACKAGE_REGISTRY
    CMAKE_EXPORT_PACKAGE_REGISTRY
    CMAKE_FIND_PACKAGE_NO_PACKAGE_REGISTRY
    CMAKE_FIND_PACKAGE_NO_SYSTEM_PACKAGE_REGISTRY
    CMAKE_MODULE_LINKER_FLAGS
    DL_LIBRARY


-- Build files have been written to: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12
ninja: Entering directory `/openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12'
[1/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/web_connection_base.cpp.o
[2/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/alert.cpp.o
[3/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/alert_manager.cpp.o
[4/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/announce_entry.cpp.o
[5/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/assert.cpp.o
[6/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/bandwidth_limit.cpp.o
[7/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/bandwidth_manager.cpp.o
[8/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/bandwidth_queue_entry.cpp.o
[9/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/bdecode.cpp.o
[10/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/bitfield.cpp.o
[11/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/block_cache.cpp.o
[12/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/bloom_filter.cpp.o
[13/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/chained_buffer.cpp.o
[14/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/choker.cpp.o
[15/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/close_reason.cpp.o
[16/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/cpuid.cpp.o
[17/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/crc32c.cpp.o
[18/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/create_torrent.cpp.o
[19/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/disk_buffer_holder.cpp.o
[20/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/entry.cpp.o
[21/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/error_code.cpp.o
[22/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/file_storage.cpp.o
[23/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/file_progress.cpp.o
[24/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/generate_peer_id.cpp.o
[25/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/lazy_bdecode.cpp.o
[26/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/escape_string.cpp.o
[27/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/string_util.cpp.o
[28/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/file.cpp.o
[29/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/path.cpp.o
[30/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/fingerprint.cpp.o
[31/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/gzip.cpp.o
[32/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/hasher.cpp.o
[33/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/sha1.cpp.o
[34/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/hex.cpp.o
[35/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/http_connection.cpp.o
[36/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/http_stream.cpp.o
[37/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/http_parser.cpp.o
[38/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/i2p_stream.cpp.o
[39/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/identify_client.cpp.o
[40/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/ip_filter.cpp.o
[41/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/ip_notifier.cpp.o
[42/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/ip_voter.cpp.o
[43/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/listen_socket_handle.cpp.o
[44/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/performance_counters.cpp.o
[45/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/peer_class.cpp.o
[46/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/peer_class_set.cpp.o
[47/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/peer_connection.cpp.o
[48/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/bt_peer_connection.cpp.o
[49/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/web_peer_connection.cpp.o
[50/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/http_seed_connection.cpp.o
[51/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/peer_connection_handle.cpp.o
[52/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/instantiate_connection.cpp.o
[53/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/merkle.cpp.o
[54/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/natpmp.cpp.o
[55/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/openssl.cpp.o
[56/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/part_file.cpp.o
[57/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/packet_buffer.cpp.o
[58/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/piece_picker.cpp.o
[59/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/platform_util.cpp.o
[60/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/proxy_base.cpp.o
[61/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/peer_list.cpp.o
[62/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/puff.cpp.o
[63/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/random.cpp.o
[64/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/receive_buffer.cpp.o
[65/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/read_resume_data.cpp.o
[66/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/write_resume_data.cpp.o
[67/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/request_blocks.cpp.o
[68/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/resolve_links.cpp.o
[69/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/resolver.cpp.o
[70/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/session.cpp.o
[71/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/session_call.cpp.o
[72/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/session_handle.cpp.o
[73/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/session_impl.cpp.o
[74/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/session_settings.cpp.o
[75/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/proxy_settings.cpp.o
[76/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/session_stats.cpp.o
[77/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/settings_pack.cpp.o
[78/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/sha1_hash.cpp.o
[79/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/socket_io.cpp.o
[80/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/socket_type.cpp.o
[81/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/socks5_stream.cpp.o
[82/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/stat.cpp.o
[83/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/stat_cache.cpp.o
[84/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/storage.cpp.o
[85/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/storage_piece_set.cpp.o
[86/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/storage_utils.cpp.o
[87/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/time.cpp.o
[88/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/timestamp_history.cpp.o
[89/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/torrent.cpp.o
[90/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/torrent_handle.cpp.o
[91/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/torrent_info.cpp.o
[92/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/torrent_peer.cpp.o
[93/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/torrent_peer_allocator.cpp.o
[94/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/torrent_status.cpp.o
[95/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/tracker_manager.cpp.o
[96/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/http_tracker_connection.cpp.o
[97/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/utf8.cpp.o
[98/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/udp_tracker_connection.cpp.o
[99/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/udp_socket.cpp.o
[100/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/upnp.cpp.o
[101/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/utp_socket_manager.cpp.o
[102/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/utp_stream.cpp.o
[103/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/file_pool.cpp.o
[104/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/lsd.cpp.o
[105/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/disk_io_job.cpp.o
[106/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/disk_job_fence.cpp.o
[107/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/disk_job_pool.cpp.o
[108/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/disk_buffer_pool.cpp.o
[109/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/disk_io_thread.cpp.o
[110/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/disk_io_thread_pool.cpp.o
[111/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/enum_net.cpp.o
[112/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/broadcast_socket.cpp.o
[113/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/magnet_uri.cpp.o
[114/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/parse_url.cpp.o
[115/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/xml_parse.cpp.o
[116/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/version.cpp.o
[117/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/ffs.cpp.o
[118/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/add_torrent_params.cpp.o
[119/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/peer_info.cpp.o
[120/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/stack_allocator.cpp.o
[121/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/ut_pex.cpp.o
[122/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/ut_metadata.cpp.o
[123/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/smart_ban.cpp.o
[124/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/pe_crypto.cpp.o
[125/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/kademlia/dht_state.cpp.o
[126/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/kademlia/dht_storage.cpp.o
[127/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/kademlia/dos_blocker.cpp.o
[128/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/kademlia/dht_tracker.cpp.o
[129/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/kademlia/msg.cpp.o
[130/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/kademlia/node.cpp.o
[131/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/kademlia/node_entry.cpp.o
[132/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/kademlia/refresh.cpp.o
[133/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/kademlia/rpc_manager.cpp.o
[134/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/kademlia/find_data.cpp.o
[135/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/kademlia/put_data.cpp.o
[136/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/kademlia/node_id.cpp.o
[137/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/kademlia/routing_table.cpp.o
[138/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/kademlia/traversal_algorithm.cpp.o
[139/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/kademlia/item.cpp.o
[140/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/kademlia/get_peers.cpp.o
[141/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/kademlia/get_item.cpp.o
[142/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/kademlia/ed25519.cpp.o
[143/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/kademlia/sample_infohashes.cpp.o
[144/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/kademlia/dht_settings.cpp.o
[145/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/ed25519/src/add_scalar.cpp.o
[146/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/ed25519/src/fe.cpp.o
[147/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/ed25519/src/ge.cpp.o
[148/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/ed25519/src/key_exchange.cpp.o
[149/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/ed25519/src/keypair.cpp.o
[150/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/ed25519/src/sc.cpp.o
[151/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/ed25519/src/sign.cpp.o
[152/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/ed25519/src/verify.cpp.o
[153/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/hasher512.cpp.o
[154/156] Building CXX object CMakeFiles/torrent-rasterbar.dir/src/sha512.cpp.o
[155/156] Linking CXX shared library libtorrent-rasterbar.so.1.2.12
[156/156] Creating library symlink libtorrent-rasterbar.so.10 libtorrent-rasterbar.so
ninja: Entering directory `/openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12'
[0/1] Install the project...
-- Install configuration: "Release"
CMake Warning (dev) at torrent-rasterbar-pkgconfig/compile-settings-expanded.cmake:3 (set):
  Policy CMP0053 is not set: Simplify variable reference and escape sequence
  evaluation.  Run "cmake --help-policy CMP0053" for policy details.  Use the
  cmake_policy command to set the policy and suppress this warning.

  For input:

    ';@CMAKE_INSTALL_PREFIX@/include;/openwrt/staging_dir/hostpkg/include'

  the old evaluation rules produce:

    ';/usr/include;/openwrt/staging_dir/hostpkg/include'

  but the new evaluation rules produce:

    ';@CMAKE_INSTALL_PREFIX@/include;/openwrt/staging_dir/hostpkg/include'

  Using the old result for compatibility since the policy is not set.
Call Stack (most recent call first):
  torrent-rasterbar-pkgconfig/generate-pkg-config.cmake:1 (include)
  cmake_install.cmake:46 (include)
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at torrent-rasterbar-pkgconfig/generate-pkg-config.cmake:29 (list):
  Policy CMP0007 is not set: list command no longer ignores empty elements.
  Run "cmake --help-policy CMP0007" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.  List has value =
  [/usr/lib;].
Call Stack (most recent call first):
  torrent-rasterbar-pkgconfig/generate-pkg-config.cmake:36 (split_library_dirs)
  cmake_install.cmake:46 (include)
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at torrent-rasterbar-pkgconfig/generate-pkg-config.cmake:5 (list):
  Policy CMP0007 is not set: list command no longer ignores empty elements.
  Run "cmake --help-policy CMP0007" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.  List has value =
  [TORRENT_LINKING_SHARED;;BOOST_ASIO_ENABLE_CANCELIO;TORRENT_USE_ICONV;TORRENT_USE_LIBGCRYPT].
Call Stack (most recent call first):
  torrent-rasterbar-pkgconfig/generate-pkg-config.cmake:46 (cmake_list_to_pkg_config)
  cmake_install.cmake:46 (include)
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at torrent-rasterbar-pkgconfig/generate-pkg-config.cmake:5 (list):
  Policy CMP0007 is not set: list command no longer ignores empty elements.
  Run "cmake --help-policy CMP0007" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.  List has value =
  [;/usr/include;/openwrt/staging_dir/hostpkg/include].
Call Stack (most recent call first):
  torrent-rasterbar-pkgconfig/generate-pkg-config.cmake:47 (cmake_list_to_pkg_config)
  cmake_install.cmake:46 (include)
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/lib/pkgconfig/libtorrent-rasterbar.pc
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/lib/libtorrent-rasterbar.so.1.2.12
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/lib/libtorrent-rasterbar.so.10
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/lib/libtorrent-rasterbar.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/error.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/extensions.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/session_types.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/lsd.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/peer_class.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/choker.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/utp_socket_manager.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/web_peer_connection.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/http_seed_connection.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/tracker_manager.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/invariant_check.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/vector_utils.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/disk_io_thread_pool.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/broadcast_socket.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/torrent_flags.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/torrent_status.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/disk_io_job.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/chained_buffer.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/torrent_info.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/platform_util.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/web_connection_base.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/parse_url.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/peer_list.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/entry.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/peer_class_type_filter.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/sha512.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/download_priority.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/bandwidth_limit.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/operations.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/socket.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/session_status.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/close_reason.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/time.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/debug.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/session.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/ip_filter.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/magnet_uri.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/peer_info.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/address.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/performance_counters.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/request_blocks.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/session_settings.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/extensions
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/extensions/ut_pex.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/extensions/smart_ban.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/extensions/ut_metadata.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/error_code.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/gzip.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/optional.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/lazy_entry.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/bdecode.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/deadline_timer.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/version.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/puff.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/torrent.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/link.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/torrent_handle.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/disk_job_pool.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/storage.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/session_stats.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/file.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/hasher512.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/pe_crypto.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/resolver.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/add_torrent_params.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/stat.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/file_pool.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/utp_stream.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/piece_picker.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/io_service_fwd.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/utf8.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/pex_flags.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/part_file.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/peer_id.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/http_tracker_connection.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/http_connection.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/io_service.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/ssl_stream.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/fwd.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/peer_class_set.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/timestamp_history.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/i2p_stream.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/disk_observer.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/piece_block.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/bloom_filter.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/sha1.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/heterogeneous_queue.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/buffer.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/bencode.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/sliding_average.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/config.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/peer_connection_handle.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/torrent_peer.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/identify_client.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/flags.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/fingerprint.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/netlink.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/bt_peer_connection.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/ip_voter.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/crc32c.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/stack_allocator.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/resolve_links.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/resolver_interface.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/stat_cache.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/bandwidth_socket.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/torrent_peer_allocator.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/socket_io.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/disk_buffer_pool.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/peer_request.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/assert.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/session_handle.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/disk_buffer_holder.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/random.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/index_range.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/alert.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/numeric_cast.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/lsd.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/aligned_union.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/file_progress.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/deferred_handler.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/proxy_settings.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/allocating_handler.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/vector.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/byteswap.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/keepalive.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/alloca.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/bind_to_device.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/time.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/cppint_import_export.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/instantiate_connection.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/noexcept_movable.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/session_settings.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/win_util.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/disable_warnings_pop.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/session_interface.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/generate_peer_id.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/deprecated.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/path.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/session_udp_sockets.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/range.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/dev_random.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/disable_warnings_push.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/merkle.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/scope_end.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/route.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/array.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/storage_utils.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/export.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/aligned_storage.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/set_socket_buffer.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/session_call.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/string_ptr.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/session_impl.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/listen_socket_handle.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/windows.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/openssl.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/throw.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/escape_string.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/has_block.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/cpuid.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/pool.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/portmap.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/deque.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/storage_piece_set.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/io.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/suggest_piece.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/torrent_impl.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/block_cache_reference.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/socket_type.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/container_wrapper.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/unique_ptr.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/win_crypto_provider.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/disk_job_fence.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/ip_notifier.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/aux_/ffs.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/create_torrent.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/kademlia
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/kademlia/dht_settings.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/kademlia/direct_request.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/kademlia/traversal_algorithm.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/kademlia/item.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/kademlia/dht_state.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/kademlia/get_peers.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/kademlia/sample_infohashes.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/kademlia/announce_flags.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/kademlia/observer.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/kademlia/put_data.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/kademlia/routing_table.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/kademlia/node_id.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/kademlia/dht_storage.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/kademlia/node.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/kademlia/types.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/kademlia/ed25519.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/kademlia/msg.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/kademlia/dht_observer.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/kademlia/rpc_manager.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/kademlia/find_data.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/kademlia/io.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/kademlia/dht_tracker.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/kademlia/get_item.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/kademlia/node_entry.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/kademlia/dos_blocker.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/kademlia/refresh.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/union_endpoint.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/copy_ptr.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/string_view.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/packet_pool.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/ed25519.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/linked_list.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/natpmp.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/sha1_hash.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/bandwidth_manager.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/bitfield.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/string_util.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/http_stream.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/span.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/units.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/http_parser.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/piece_block_progress.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/disk_io_thread.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/alert_types.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/packet_buffer.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/peer_connection_interface.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/xml_parse.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/write_resume_data.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/portmap.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/read_resume_data.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/file_storage.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/block_cache.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/enum_net.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/upnp.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/alert_manager.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/hasher.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/receive_buffer.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/io.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/proxy_base.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/peer.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/bandwidth_queue_entry.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/tailqueue.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/peer_connection.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/hex.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/socks5_stream.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/udp_tracker_connection.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/disk_interface.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/announce_entry.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/udp_socket.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/storage_defs.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/include/libtorrent/settings_pack.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/lib/cmake/LibtorrentRasterbar/LibtorrentRasterbarTargets.cmake
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/lib/cmake/LibtorrentRasterbar/LibtorrentRasterbarTargets-release.cmake
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/lib/cmake/LibtorrentRasterbar/LibtorrentRasterbarConfig.cmake
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/lib/cmake/LibtorrentRasterbar/LibtorrentRasterbarConfigVersion.cmake
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/libtorrent-rasterbar-1.2.12/ipkg-install/usr/share/cmake/Modules/FindLibtorrentRasterbar.cmake
Package libtorrent-rasterbar is missing dependencies for the following libraries:
libatomic.so.1
libgcrypt.so.20
make[3]: *** [Makefile:59: /openwrt/bin/packages/mips_24kc/packages/libtorrent-rasterbar_1.2.12-1_mips_24kc.ipk] Error 1
```
