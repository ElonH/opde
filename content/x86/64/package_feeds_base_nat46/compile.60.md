---
title: "compile.60"
date: 2021-02-18 15:10:27.224528
hidden: false
draft: false
weight: -60
---

build number: `60`

path: `package/feeds/base/nat46/compile`


``` bash
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/linux-5.4.98'
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/nat46-2020-08-17-362640b4/nat46/modules/nat46-netdev.o
../nat46-2020-08-17-362640b4/nat46/modules/nat46-netdev.c: In function 'nat46_remove':
../nat46-2020-08-17-362640b4/nat46/modules/nat46-netdev.c:257:2: warning: ISO C90 forbids variable length array 'config_remove' [-Wvla]
  char config_remove[buflen];
  ^~~~
../nat46-2020-08-17-362640b4/nat46/modules/nat46-netdev.c:277:3: warning: ISO C90 forbids variable length array 'config' [-Wvla]
   char config[buflen];
   ^~~~
/bin/sh: 1: scripts/basic/fixdep: not found
make[5]: *** [scripts/Makefile.build:262: /openwrt/build_dir/target-x86_64_musl/linux-x86_64/nat46-2020-08-17-362640b4/nat46/modules/nat46-netdev.o] Error 127
make[5]: *** Deleting file '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/nat46-2020-08-17-362640b4/nat46/modules/nat46-netdev.o'
make[4]: *** [Makefile:1726: /openwrt/build_dir/target-x86_64_musl/linux-x86_64/nat46-2020-08-17-362640b4/nat46/modules] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/linux-5.4.98'
make[3]: *** [Makefile:38: /openwrt/build_dir/target-x86_64_musl/linux-x86_64/nat46-2020-08-17-362640b4/.built] Error 2
```
