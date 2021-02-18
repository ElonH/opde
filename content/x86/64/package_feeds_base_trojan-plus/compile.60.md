---
title: "compile.60"
date: 2021-02-18 15:10:27.224824
hidden: false
draft: false
weight: -60
---

build number: `60`

path: `package/feeds/base/trojan-plus/compile`


``` bash
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/trojan-plus-10.0.3'
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/trojan-plus-10.0.3'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/trojan-plus-10.0.3'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/trojan-plus-10.0.3'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/trojan-plus-10.0.3'
[  4%] Building CXX object CMakeFiles/trojan.dir/src/core/config.cpp.o
/openwrt/build_dir/target-x86_64_musl/trojan-plus-10.0.3/src/core/config.cpp:26:10: fatal error: gsl/gsl: No such file or directory
 #include <gsl/gsl>
          ^~~~~~~~~
compilation terminated.
make[6]: *** [CMakeFiles/trojan.dir/build.make:95: CMakeFiles/trojan.dir/src/core/config.cpp.o] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/trojan-plus-10.0.3'
make[5]: *** [CMakeFiles/Makefile2:95: CMakeFiles/trojan.dir/all] Error 2
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/trojan-plus-10.0.3'
make[4]: *** [Makefile:160: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/trojan-plus-10.0.3'
make[3]: *** [Makefile:72: /openwrt/build_dir/target-x86_64_musl/trojan-plus-10.0.3/.built] Error 2
```
