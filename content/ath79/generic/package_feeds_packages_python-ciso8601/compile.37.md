---
title: "compile.37"
date: 2021-06-20 22:36:26.360412
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
make package/feeds/packages/python-ciso8601/compile -j$(nproc) || make package/feeds/packages/python-ciso8601/compile V=s
```

#### Compile.txt

``` bash
running install
running build
running build_py
package init file 'ciso8601/__init__.py' not found (or not a regular file)
creating build
creating build/lib.-3.9
creating build/lib.-3.9/ciso8601
copying ciso8601/__init__.pyi -> build/lib.-3.9/ciso8601
copying ciso8601/py.typed -> build/lib.-3.9/ciso8601
warning: build_py: byte-compiling is disabled, skipping.

running build_ext
building 'ciso8601' extension
creating build/temp.-3.9
ccache_cc -Wno-unused-result -Wsign-compare -DNDEBUG -g -O3 -Wall -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/pypi/ciso8601-2.1.3=ciso8601-2.1.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -fPIC -DCISO8601_VERSION=2.1.3 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -c module.c -o build/temp.-3.9/module.o
module.c:1:10: fatal error: Python.h: No such file or directory
 #include <Python.h>
          ^~~~~~~~~~
compilation terminated.
error: command '/openwrt/staging_dir/host/bin/ccache_cc' failed with exit code 1
make[3]: *** [Makefile:44: /openwrt/build_dir/target-mips_24kc_musl/pypi/ciso8601-2.1.3/.built] Error 1
```
