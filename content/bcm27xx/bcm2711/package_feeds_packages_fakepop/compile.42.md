---
title: "compile.42"
date: 2021-06-29 09:38:24.598102
hidden: false
draft: false
weight: -42
---

build number: `42`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/fakepop/compile -j$(nproc) || make package/feeds/packages/fakepop/compile V=s
```

#### Compile.txt

``` bash
make[4]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/fakepop-10'
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
ccache_cc -D_GNU_SOURCE -Wall -O2    -c -o fakepop.o fakepop.c
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
cc1: note: someone does not honour COPTS correctly, passed 0 times
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
ccache_cc -D_GNU_SOURCE -Wall -O2    -c -o header.o header.c
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
cc1: note: someone does not honour COPTS correctly, passed 0 times
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
ccache_cc -D_GNU_SOURCE -Wall -O2    -c -o id.o id.c
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
cc1: note: someone does not honour COPTS correctly, passed 0 times
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
ccache_cc -D_GNU_SOURCE -Wall -O2    -c -o msg.o msg.c
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
cc1: note: someone does not honour COPTS correctly, passed 0 times
msg.c:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
make[4]: *** [<builtin>: msg.o] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/fakepop-10'
make[3]: *** [Makefile:45: /openwrt/build_dir/target-aarch64_cortex-a72_musl/fakepop-10/.built] Error 2
```
