---
title: "compile.37"
date: 2021-06-20 22:38:00.062996
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
make package/feeds/packages/trojan-plus/compile -j$(nproc) || make package/feeds/packages/trojan-plus/compile V=s
```

#### Compile.txt

``` bash
-- The CXX compiler identification is GNU 8.4.0
-- The C compiler identification is GNU 8.4.0
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-g++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
-- Using and shipping https://github.com/Microsoft/GSL version 
Cloning into '/openwrt/build_dir/target-mips_24kc_musl/trojan-plus-10.0.3/external/GSL'...
Note: switching to '0f6dbc9'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 0f6dbc9 Merge pull request #892 from JordanMaples/dev/jomaples/gsl3.1.0
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
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1637 ] location of version.hpp: /openwrt/staging_dir/target-mips_24kc_musl/usr/include/boost/version.hpp
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1677 ] Boost_VERSION = "107600"
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1678 ] Boost_VERSION_STRING = "1.76.0"
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1679 ] Boost_VERSION_MACRO = "107600"
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1680 ] Boost_VERSION_MAJOR = "1"
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1681 ] Boost_VERSION_MINOR = "76"
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1682 ] Boost_VERSION_PATCH = "0"
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1683 ] Boost_VERSION_COUNT = "3"
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1707 ] Boost_LIB_PREFIX = ""
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1708 ] Boost_NAMESPACE = "boost"
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:818 ] _boost_COMPILER = "-gcc8" (guessed)
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1744 ] _boost_MULTITHREADED = "-mt"
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1821 ] _boost_ARCHITECTURE_TAG = "" (detected)
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1825 ] _boost_RELEASE_ABI_TAG = "-"
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1826 ] _boost_DEBUG_ABI_TAG = "-d"
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1886 ] _boost_LIBRARY_SEARCH_DIRS_RELEASE = "/openwrt/staging_dir/target-mips_24kc_musl/usr/include/lib;/openwrt/staging_dir/target-mips_24kc_musl/usr/include/../lib;/openwrt/staging_dir/target-mips_24kc_musl/usr/include/stage/lib;PATHS;C:/boost/lib;C:/boost;/sw/local/lib"
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1887 ] _boost_LIBRARY_SEARCH_DIRS_DEBUG = "/openwrt/staging_dir/target-mips_24kc_musl/usr/include/lib;/openwrt/staging_dir/target-mips_24kc_musl/usr/include/../lib;/openwrt/staging_dir/target-mips_24kc_musl/usr/include/stage/lib;PATHS;C:/boost/lib;C:/boost;/sw/local/lib"
CMake Warning at /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1204 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1326 (_Boost_COMPONENT_DEPENDENCIES)
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1935 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:199 (find_package)


CMake Warning at /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1204 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1326 (_Boost_COMPONENT_DEPENDENCIES)
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1935 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:199 (find_package)


-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:2072 ] Searching for SYSTEM_LIBRARY_RELEASE: boost_system-gcc8-mt-1_76;boost_system-gcc8-mt;boost_system-gcc8-mt;boost_system-mt-1_76;boost_system-mt;boost_system-mt;boost_system-mt;boost_system
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:673 ] Boost_LIBRARY_DIR_RELEASE = "/openwrt/staging_dir/target-mips_24kc_musl/usr/lib"
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:675 ] _boost_LIBRARY_SEARCH_DIRS_RELEASE = "/openwrt/staging_dir/target-mips_24kc_musl/usr/lib;NO_DEFAULT_PATH;NO_CMAKE_FIND_ROOT_PATH"
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:2127 ] Searching for SYSTEM_LIBRARY_DEBUG: boost_system-gcc8-mt-d-1_76;boost_system-gcc8-mt-d;boost_system-gcc8-mt-d;boost_system-mt-d-1_76;boost_system-mt-d;boost_system-mt-d;boost_system-mt;boost_system
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:673 ] Boost_LIBRARY_DIR_DEBUG = "/openwrt/staging_dir/target-mips_24kc_musl/usr/lib"
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:675 ] _boost_LIBRARY_SEARCH_DIRS_DEBUG = "/openwrt/staging_dir/target-mips_24kc_musl/usr/lib;NO_DEFAULT_PATH;NO_CMAKE_FIND_ROOT_PATH"
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:2072 ] Searching for PROGRAM_OPTIONS_LIBRARY_RELEASE: boost_program_options-gcc8-mt-1_76;boost_program_options-gcc8-mt;boost_program_options-gcc8-mt;boost_program_options-mt-1_76;boost_program_options-mt;boost_program_options-mt;boost_program_options-mt;boost_program_options
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:673 ] Boost_LIBRARY_DIR_RELEASE = "/openwrt/staging_dir/target-mips_24kc_musl/usr/lib"
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:675 ] _boost_LIBRARY_SEARCH_DIRS_RELEASE = "/openwrt/staging_dir/target-mips_24kc_musl/usr/lib;NO_DEFAULT_PATH;NO_CMAKE_FIND_ROOT_PATH"
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:2127 ] Searching for PROGRAM_OPTIONS_LIBRARY_DEBUG: boost_program_options-gcc8-mt-d-1_76;boost_program_options-gcc8-mt-d;boost_program_options-gcc8-mt-d;boost_program_options-mt-d-1_76;boost_program_options-mt-d;boost_program_options-mt-d;boost_program_options-mt;boost_program_options
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:673 ] Boost_LIBRARY_DIR_DEBUG = "/openwrt/staging_dir/target-mips_24kc_musl/usr/lib"
-- [ /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:675 ] _boost_LIBRARY_SEARCH_DIRS_DEBUG = "/openwrt/staging_dir/target-mips_24kc_musl/usr/lib;NO_DEFAULT_PATH;NO_CMAKE_FIND_ROOT_PATH"
-- Found Boost: /openwrt/staging_dir/target-mips_24kc_musl/usr/include (found suitable version "1.76.0", minimum required is "1.66.0") found components: system program_options 
CMake Error at /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindPackageHandleStandardArgs.cmake:218 (message):
  Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the
  system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY
  OPENSSL_INCLUDE_DIR) (Required is at least version "1.1.0")
Call Stack (most recent call first):
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindPackageHandleStandardArgs.cmake:577 (_FPHSA_FAILURE_MESSAGE)
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindOpenSSL.cmake:536 (find_package_handle_standard_args)
  CMakeLists.txt:206 (find_package)


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-mips_24kc_musl/trojan-plus-10.0.3/CMakeFiles/CMakeOutput.log".
make[3]: *** [Makefile:75: /openwrt/build_dir/target-mips_24kc_musl/trojan-plus-10.0.3/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
