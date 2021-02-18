---
title: "compile.60"
date: 2021-02-18 15:10:27.221006
hidden: false
draft: false
weight: -60
---

build number: `60`

path: `package/feeds/packages/mc/compile`


``` bash
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/mc-4.8.25'
make  all-recursive
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/mc-4.8.25'
Making all in po
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/mc-4.8.25/po'
*** error: gettext infrastructure mismatch: using a Makefile.in.in from gettext version 0.18 but the autoconf macros are from gettext version 0.20
make[6]: *** [Makefile:249: check-macro-version] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/mc-4.8.25/po'
make[5]: *** [Makefile:578: all-recursive] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/mc-4.8.25'
make[4]: *** [Makefile:508: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/mc-4.8.25'
make[3]: *** [Makefile:131: /openwrt/build_dir/target-x86_64_musl/mc-4.8.25/.built] Error 2
```
