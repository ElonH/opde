---
title: "compile.60"
date: 2021-02-18 15:10:27.229496
hidden: false
draft: false
weight: -60
---

build number: `60`

path: `package/feeds/base/tinyfecvpn/compile`


``` bash
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/tinyfecVPN-20210116.0'
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
echo "const char * const gitversion = \"\";" > git_version.h
ccache_cxx   -o tinyvpn_cross    -I. `ls UDPspeeder/*.cpp UDPspeeder/lib/*.cpp|grep -v main.cpp|grep -v tunnel.cpp` main.cpp tun_dev.cpp tun_dev_client.cpp tun_dev_server.cpp -std=c++11   -Wall -Wextra -Wno-unused-variable -Wno-unused-parameter -Wno-missing-field-initializers -ggdb -I. -IUDPspeeder -isystem UDPspeeder/libev   -lrt -O3
ls: cannot access 'UDPspeeder/*.cpp': No such file or directory
ls: cannot access 'UDPspeeder/lib/*.cpp': No such file or directory
main.cpp:8:10: fatal error: common.h: No such file or directory
 #include "common.h"
          ^~~~~~~~~~
compilation terminated.
In file included from tun_dev.cpp:9:
tun_dev.h:12:10: fatal error: common.h: No such file or directory
 #include "common.h"
          ^~~~~~~~~~
compilation terminated.
In file included from tun_dev_client.cpp:1:
tun_dev.h:12:10: fatal error: common.h: No such file or directory
 #include "common.h"
          ^~~~~~~~~~
compilation terminated.
In file included from tun_dev_server.cpp:1:
tun_dev.h:12:10: fatal error: common.h: No such file or directory
 #include "common.h"
          ^~~~~~~~~~
compilation terminated.
make[4]: *** [makefile:60: cross] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/tinyfecVPN-20210116.0'
make[3]: *** [Makefile:55: /openwrt/build_dir/target-x86_64_musl/tinyfecVPN-20210116.0/.built] Error 2
```
