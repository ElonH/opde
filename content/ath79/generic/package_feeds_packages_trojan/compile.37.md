---
title: "compile.37"
date: 2021-06-20 22:39:07.404968
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
make package/feeds/packages/trojan/compile -j$(nproc) || make package/feeds/packages/trojan/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-force-openssl-version.patch using plaintext: 
patching file CMakeLists.txt
-- The CXX compiler identification is GNU 8.4.0
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-g++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Looking for C++ include pthread.h
-- Looking for C++ include pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1507 ] _boost_TEST_VERSIONS = "1.74.0;1.74;1.73.0;1.73;1.72.0;1.72;1.71.0;1.71;1.70.0;1.70;1.69.0;1.69;1.68.0;1.68;1.67.0;1.67;1.66.0;1.66"
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1508 ] Boost_USE_MULTITHREADED = "TRUE"
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1509 ] Boost_USE_STATIC_LIBS = <unset>
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1510 ] Boost_USE_STATIC_RUNTIME = <unset>
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1511 ] Boost_ADDITIONAL_VERSIONS = <unset>
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1512 ] Boost_NO_SYSTEM_PATHS = <unset>
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1544 ] BOOST_ROOT = <unset>
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1545 ] ENV{BOOST_ROOT} = <unset>
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1546 ] BOOST_INCLUDEDIR = <unset>
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1547 ] ENV{BOOST_INCLUDEDIR} = <unset>
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1548 ] BOOST_LIBRARYDIR = <unset>
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1549 ] ENV{BOOST_LIBRARYDIR} = <unset>
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1621 ] _boost_INCLUDE_SEARCH_DIRS = "PATHS;C:/boost/include;C:/boost;/sw/local/include"
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1622 ] _boost_PATH_SUFFIXES = "boost-1_74_0;boost_1_74_0;boost/boost-1_74_0;boost/boost_1_74_0;boost-1_74;boost_1_74;boost/boost-1_74;boost/boost_1_74;boost-1_73_0;boost_1_73_0;boost/boost-1_73_0;boost/boost_1_73_0;boost-1_73;boost_1_73;boost/boost-1_73;boost/boost_1_73;boost-1_72_0;boost_1_72_0;boost/boost-1_72_0;boost/boost_1_72_0;boost-1_72;boost_1_72;boost/boost-1_72;boost/boost_1_72;boost-1_71_0;boost_1_71_0;boost/boost-1_71_0;boost/boost_1_71_0;boost-1_71;boost_1_71;boost/boost-1_71;boost/boost_1_71;boost-1_70_0;boost_1_70_0;boost/boost-1_70_0;boost/boost_1_70_0;boost-1_70;boost_1_70;boost/boost-1_70;boost/boost_1_70;boost-1_69_0;boost_1_69_0;boost/boost-1_69_0;boost/boost_1_69_0;boost-1_69;boost_1_69;boost/boost-1_69;boost/boost_1_69;boost-1_68_0;boost_1_68_0;boost/boost-1_68_0;boost/boost_1_68_0;boost-1_68;boost_1_68;boost/boost-1_68;boost/boost_1_68;boost-1_67_0;boost_1_67_0;boost/boost-1_67_0;boost/boost_1_67_0;boost-1_67;boost_1_67;boost/boost-1_67;boost/boost_1_67;boost-1_66_0;boost_1_66_0;boost/boost-1_66_0;boost/boost_1_66_0;boost-1_66;boost_1_66;boost/boost-1_66;boost/boost_1_66"
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1707 ] Boost_LIB_PREFIX = ""
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1708 ] Boost_NAMESPACE = "boost"
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:818 ] _boost_COMPILER = "-gcc" (guessed)
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1744 ] _boost_MULTITHREADED = "-mt"
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1821 ] _boost_ARCHITECTURE_TAG = "" (detected)
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1825 ] _boost_RELEASE_ABI_TAG = "-"
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1826 ] _boost_DEBUG_ABI_TAG = "-d"
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1886 ] _boost_LIBRARY_SEARCH_DIRS_RELEASE = "Boost_INCLUDE_DIR-NOTFOUND/lib;Boost_INCLUDE_DIR-NOTFOUND/../lib;Boost_INCLUDE_DIR-NOTFOUND/stage/lib;PATHS;C:/boost/lib;C:/boost;/sw/local/lib"
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1887 ] _boost_LIBRARY_SEARCH_DIRS_DEBUG = "Boost_INCLUDE_DIR-NOTFOUND/lib;Boost_INCLUDE_DIR-NOTFOUND/../lib;Boost_INCLUDE_DIR-NOTFOUND/stage/lib;PATHS;C:/boost/lib;C:/boost;/sw/local/lib"
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:2072 ] Searching for SYSTEM_LIBRARY_RELEASE: boost_system-gcc-mt-;boost_system-gcc-mt;boost_system-gcc-mt;boost_system-mt-;boost_system-mt;boost_system-mt;boost_system-mt;boost_system
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:2127 ] Searching for SYSTEM_LIBRARY_DEBUG: boost_system-gcc-mt-d-;boost_system-gcc-mt-d;boost_system-gcc-mt-d;boost_system-mt-d-;boost_system-mt-d;boost_system-mt-d;boost_system-mt;boost_system
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:2072 ] Searching for PROGRAM_OPTIONS_LIBRARY_RELEASE: boost_program_options-gcc-mt-;boost_program_options-gcc-mt;boost_program_options-gcc-mt;boost_program_options-mt-;boost_program_options-mt;boost_program_options-mt;boost_program_options-mt;boost_program_options
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:2127 ] Searching for PROGRAM_OPTIONS_LIBRARY_DEBUG: boost_program_options-gcc-mt-d-;boost_program_options-gcc-mt-d;boost_program_options-gcc-mt-d;boost_program_options-mt-d-;boost_program_options-mt-d;boost_program_options-mt-d;boost_program_options-mt;boost_program_options
CMake Error at /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindPackageHandleStandardArgs.cmake:218 (message):
  Could NOT find Boost (missing: Boost_INCLUDE_DIR system program_options)
  (Required is at least version "1.66.0")
Call Stack (most recent call first):
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindPackageHandleStandardArgs.cmake:577 (_FPHSA_FAILURE_MESSAGE)
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:2193 (find_package_handle_standard_args)
  CMakeLists.txt:39 (find_package)


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-mips_24kc_musl/trojan-1.16.0/CMakeFiles/CMakeOutput.log".
make[3]: *** [Makefile:73: /openwrt/build_dir/target-mips_24kc_musl/trojan-1.16.0/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
