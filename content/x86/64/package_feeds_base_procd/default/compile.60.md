---
title: "compile.60"
date: 2021-02-18 15:10:27.229857
hidden: false
draft: false
weight: -60
---

build number: `60`

path: `package/feeds/base/procd/compile`


``` bash
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948'
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948'
[  3%] Built target setlbf
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948'
[  5%] Built target syscall-names-h
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948'
[  7%] Linking C shared library libpreload-seccomp.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948'
[ 10%] Built target preload-seccomp
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948'
[ 12%] Linking C executable ujail-console
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948'
[ 14%] Built target ujail-console
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948'
[ 18%] Built target udevtrigger
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948'
[ 21%] Built target preload-trace
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948'
[ 23%] Linking C executable procd
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948'
[ 54%] Built target procd
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948'
[ 56%] Built target capabilities-names-h
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948'
[ 58%] Building C object CMakeFiles/ujail.dir/jail/jail.c.o
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
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948'
make[5]: *** [CMakeFiles/Makefile2:354: CMakeFiles/ujail.dir/all] Error 2
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948'
make[4]: *** [Makefile:149: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948'
make[3]: *** [Makefile:177: /openwrt/build_dir/target-x86_64_musl/procd-default/procd-2020-11-06-b0de8948/.built] Error 2
```
