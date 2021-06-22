---
title: "compile.40"
date: 2021-06-22 10:50:44.055902
hidden: false
draft: false
weight: -40
---

build number: `40`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/python-evdev/compile -j$(nproc) || make package/feeds/packages/python-evdev/compile V=s
```

#### Compile.txt

``` bash
running build
running build_py
creating build
creating build/lib.-3.9
creating build/lib.-3.9/evdev
copying evdev/ecodes.py -> build/lib.-3.9/evdev
copying evdev/device.py -> build/lib.-3.9/evdev
copying evdev/events.py -> build/lib.-3.9/evdev
copying evdev/__init__.py -> build/lib.-3.9/evdev
copying evdev/uinput.py -> build/lib.-3.9/evdev
copying evdev/genecodes.py -> build/lib.-3.9/evdev
copying evdev/evtest.py -> build/lib.-3.9/evdev
copying evdev/util.py -> build/lib.-3.9/evdev
copying evdev/ff.py -> build/lib.-3.9/evdev
copying evdev/eventio.py -> build/lib.-3.9/evdev
copying evdev/eventio_async.py -> build/lib.-3.9/evdev
warning: build_py: byte-compiling is disabled, skipping.

running build_ext
running build_ecodes
writing ecodes.c (using /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/uapi/linux/input.h /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124/include/uapi/linux/input-event-codes.h)
building 'evdev._input' extension
creating build/temp.-3.9
creating build/temp.-3.9/evdev
ccache_cc -Wno-unused-result -Wsign-compare -DNDEBUG -g -O3 -Wall -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/pypi/evdev-1.4.0=evdev-1.4.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -fPIC -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -c evdev/input.c -o build/temp.-3.9/evdev/input.o -std=c99 -Wno-error=declaration-after-statement
evdev/input.c:10:10: fatal error: Python.h: No such file or directory
 #include <Python.h>
          ^~~~~~~~~~
compilation terminated.
error: command '/openwrt/staging_dir/host/bin/ccache_cc' failed with exit code 1
make[3]: *** [Makefile:53: /openwrt/build_dir/target-mips_24kc_musl/pypi/evdev-1.4.0/.built] Error 1
```
