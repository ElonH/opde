---
title: "compile.40"
date: 2021-06-22 10:42:16.502845
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
make package/feeds/packages/python-yarl/compile -j$(nproc) || make package/feeds/packages/python-yarl/compile V=s
```

#### Compile.txt

``` bash
**********************
* Accellerated build *
**********************
running install
running build
running build_py
creating build
creating build/lib.-3.9
creating build/lib.-3.9/yarl
copying yarl/_quoting_py.py -> build/lib.-3.9/yarl
copying yarl/__init__.py -> build/lib.-3.9/yarl
copying yarl/_quoting.py -> build/lib.-3.9/yarl
copying yarl/_url.py -> build/lib.-3.9/yarl
running egg_info
writing yarl.egg-info/PKG-INFO
writing dependency_links to yarl.egg-info/dependency_links.txt
writing requirements to yarl.egg-info/requires.txt
writing top-level names to yarl.egg-info/top_level.txt
warning: the 'license_file' option is deprecated, use 'license_files' instead
adding license file 'LICENSE' (matched pattern 'LICENSE')
reading manifest file 'yarl.egg-info/SOURCES.txt'
reading manifest template 'MANIFEST.in'
warning: no previously-included files matching '*.pyc' found anywhere in distribution
warning: no previously-included files matching '*.cache' found anywhere in distribution
warning: no previously-included files found matching 'yarl/*.html'
warning: no previously-included files found matching 'yarl/*.so'
warning: no previously-included files found matching 'yarl/*.pyd'
no previously-included directories found matching 'docs/_build'
writing manifest file 'yarl.egg-info/SOURCES.txt'
copying yarl/__init__.pyi -> build/lib.-3.9/yarl
copying yarl/_quoting_c.c -> build/lib.-3.9/yarl
copying yarl/_quoting_c.pyi -> build/lib.-3.9/yarl
copying yarl/_quoting_c.pyx -> build/lib.-3.9/yarl
copying yarl/py.typed -> build/lib.-3.9/yarl
warning: build_py: byte-compiling is disabled, skipping.

running build_ext
building 'yarl._quoting_c' extension
creating build/temp.-3.9
creating build/temp.-3.9/yarl
ccache_cc -Wno-unused-result -Wsign-compare -DNDEBUG -g -O3 -Wall -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/pypi/yarl-1.6.2=yarl-1.6.2 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -fPIC -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -c yarl/_quoting_c.c -o build/temp.-3.9/yarl/_quoting_c.o
yarl/_quoting_c.c:4:10: fatal error: Python.h: No such file or directory
 #include "Python.h"
          ^~~~~~~~~~
compilation terminated.
error: command '/openwrt/staging_dir/host/bin/ccache_cc' failed with exit code 1
make[3]: *** [Makefile:48: /openwrt/build_dir/target-mips_24kc_musl/pypi/yarl-1.6.2/.built] Error 1
```
