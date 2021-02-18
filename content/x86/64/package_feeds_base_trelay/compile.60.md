---
title: "compile.60"
date: 2021-02-18 15:10:27.231572
hidden: false
draft: false
weight: -60
---

build number: `60`

path: `package/feeds/base/trelay/compile`


``` bash
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/linux-5.4.98'
scripts/Makefile.build:42: arch/x86/entry/syscalls/Makefile: No such file or directory
make[5]: *** No rule to make target 'arch/x86/entry/syscalls/Makefile'.  Stop.
make[4]: *** [arch/x86/Makefile:241: archheaders] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/linux-5.4.98'
make[3]: *** [Makefile:51: /openwrt/build_dir/target-x86_64_musl/linux-x86_64/trelay/.built] Error 2
```
