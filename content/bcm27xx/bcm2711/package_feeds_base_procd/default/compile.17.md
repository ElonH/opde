---
title: "compile.17"
date: 2021-05-14 00:38:50.653729
hidden: false
draft: false
weight: -17
---

build number: `17`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/base/procd/compile -j$(nproc) || make package/feeds/base/procd/compile V=s
```

#### Compile.txt

``` bash
bash: md5: command not found
CMake Deprecation Warning at CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 2.8.12 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- The C compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/bin/aarch64-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
CMake Deprecation Warning at upgraded/CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 2.8.12 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- Configuring done
-- Generating done
CMake Warning:
  Manually-specified variables were not used by the project:

    CMAKE_ASM_COMPILER
    CMAKE_ASM_COMPILER_LAUNCHER
    CMAKE_CXX_COMPILER
    CMAKE_CXX_FLAGS_RELEASE
    CMAKE_EXPORT_NO_PACKAGE_REGISTRY
    CMAKE_EXPORT_PACKAGE_REGISTRY
    CMAKE_FIND_PACKAGE_NO_PACKAGE_REGISTRY
    CMAKE_FIND_PACKAGE_NO_SYSTEM_PACKAGE_REGISTRY
    CMAKE_FIND_USE_PACKAGE_REGISTRY
    CMAKE_FIND_USE_SYSTEM_PACKAGE_REGISTRY
    CMAKE_MODULE_LINKER_FLAGS
    DL_LIBRARY


-- Build files have been written to: /openwrt/build_dir/target-aarch64_cortex-a72_musl/procd-default/procd-2020-11-06-b0de8948
make[4]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/procd-default/procd-2020-11-06-b0de8948'
make[5]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/procd-default/procd-2020-11-06-b0de8948'
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/procd-default/procd-2020-11-06-b0de8948'
Scanning dependencies of target ujail-console
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/procd-default/procd-2020-11-06-b0de8948'
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/procd-default/procd-2020-11-06-b0de8948'
[  2%] Building C object CMakeFiles/ujail-console.dir/jail/console.c.o
[  4%] Linking C executable ujail-console
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/procd-default/procd-2020-11-06-b0de8948'
[  4%] Built target ujail-console
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/procd-default/procd-2020-11-06-b0de8948'
Scanning dependencies of target udevtrigger
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/procd-default/procd-2020-11-06-b0de8948'
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/procd-default/procd-2020-11-06-b0de8948'
[  6%] Building C object CMakeFiles/udevtrigger.dir/plug/udevtrigger.c.o
[  8%] Linking C executable udevtrigger
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/procd-default/procd-2020-11-06-b0de8948'
[  8%] Built target udevtrigger
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/procd-default/procd-2020-11-06-b0de8948'
Scanning dependencies of target procd
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/procd-default/procd-2020-11-06-b0de8948'
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/procd-default/procd-2020-11-06-b0de8948'
[ 10%] Building C object CMakeFiles/procd.dir/procd.c.o
[ 13%] Building C object CMakeFiles/procd.dir/signal.c.o
[ 15%] Building C object CMakeFiles/procd.dir/state.c.o
[ 17%] Building C object CMakeFiles/procd.dir/inittab.c.o
[ 19%] Building C object CMakeFiles/procd.dir/rcS.c.o
[ 21%] Building C object CMakeFiles/procd.dir/ubus.c.o
[ 23%] Building C object CMakeFiles/procd.dir/system.c.o
[ 26%] Building C object CMakeFiles/procd.dir/sysupgrade.c.o
[ 28%] Building C object CMakeFiles/procd.dir/service/service.c.o
[ 30%] Building C object CMakeFiles/procd.dir/service/instance.c.o
[ 32%] Building C object CMakeFiles/procd.dir/service/validate.c.o
[ 34%] Building C object CMakeFiles/procd.dir/service/trigger.c.o
[ 36%] Building C object CMakeFiles/procd.dir/service/watch.c.o
[ 39%] Building C object CMakeFiles/procd.dir/utils/utils.c.o
[ 41%] Building C object CMakeFiles/procd.dir/watchdog.c.o
[ 43%] Building C object CMakeFiles/procd.dir/plug/coldplug.c.o
[ 45%] Building C object CMakeFiles/procd.dir/plug/hotplug.c.o
[ 47%] Linking C executable procd
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/procd-default/procd-2020-11-06-b0de8948'
[ 47%] Built target procd
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/procd-default/procd-2020-11-06-b0de8948'
Scanning dependencies of target capabilities-names-h
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/procd-default/procd-2020-11-06-b0de8948'
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/procd-default/procd-2020-11-06-b0de8948'
[ 50%] Generating capabilities-names.h
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/procd-default/procd-2020-11-06-b0de8948'
[ 50%] Built target capabilities-names-h
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/procd-default/procd-2020-11-06-b0de8948'
Scanning dependencies of target ujail
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/procd-default/procd-2020-11-06-b0de8948'
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/procd-default/procd-2020-11-06-b0de8948'
[ 52%] Building C object CMakeFiles/ujail.dir/jail/jail.c.o
jail/jail.c:1585:40: error: 'BLOBMSG_CAST_INT64' undeclared here (not in a function); did you mean 'BLOBMSG_TYPE_INT64'?
  [OCI_PROCESS_RLIMIT_SOFT] = { "soft", BLOBMSG_CAST_INT64 },
                                        ^~~~~~~~~~~~~~~~~~
                                        BLOBMSG_TYPE_INT64
jail/jail.c: In function 'parseOCIrlimit':
jail/jail.c:1644:21: error: implicit declaration of function 'blobmsg_cast_u64'; did you mean 'blobmsg_get_u64'? [-Werror=implicit-function-declaration]
  curlim->rlim_cur = blobmsg_cast_u64(tb[OCI_PROCESS_RLIMIT_SOFT]);
                     ^~~~~~~~~~~~~~~~
                     blobmsg_get_u64
cc1: all warnings being treated as errors
make[6]: *** [CMakeFiles/ujail.dir/build.make:82: CMakeFiles/ujail.dir/jail/jail.c.o] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/procd-default/procd-2020-11-06-b0de8948'
make[5]: *** [CMakeFiles/Makefile2:266: CMakeFiles/ujail.dir/all] Error 2
make[5]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/procd-default/procd-2020-11-06-b0de8948'
make[4]: *** [Makefile:149: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/procd-default/procd-2020-11-06-b0de8948'
make[3]: *** [Makefile:177: /openwrt/build_dir/target-aarch64_cortex-a72_musl/procd-default/procd-2020-11-06-b0de8948/.built] Error 2
```
