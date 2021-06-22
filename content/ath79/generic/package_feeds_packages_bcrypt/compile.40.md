---
title: "compile.40"
date: 2021-06-22 10:50:44.052938
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
make package/feeds/packages/bcrypt/compile -j$(nproc) || make package/feeds/packages/bcrypt/compile V=s
```

#### Compile.txt

``` bash
Requirement already satisfied: cffi==1.14.5 in /openwrt/staging_dir/hostpkg/lib/python3.9/site-packages (from -r ../host-pip-requirements/cffi.txt (line 1)) (1.14.5)
Requirement already satisfied: pycparser==2.20 in /openwrt/staging_dir/hostpkg/lib/python3.9/site-packages (from -r ../host-pip-requirements/cffi.txt (line 2)) (2.20)
running install
running build
running build_py
creating build
creating build/lib.-3.9
creating build/lib.-3.9/bcrypt
copying src/bcrypt/__init__.py -> build/lib.-3.9/bcrypt
copying src/bcrypt/__about__.py -> build/lib.-3.9/bcrypt
warning: build_py: byte-compiling is disabled, skipping.

running build_ext
generating cffi module 'build/temp.-3.9/_bcrypt.c'
creating build/temp.-3.9
building '_bcrypt' extension
creating build/temp.-3.9/build
creating build/temp.-3.9/build/temp.-3.9
creating build/temp.-3.9/src
creating build/temp.-3.9/src/_csrc
ccache_cc -Wno-unused-result -Wsign-compare -DNDEBUG -g -O3 -Wall -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/pypi/bcrypt-3.1.7=bcrypt-3.1.7 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -fPIC -Isrc/_csrc -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -c build/temp.-3.9/_bcrypt.c -o build/temp.-3.9/build/temp.-3.9/_bcrypt.o
build/temp.-3.9/_bcrypt.c:50:14: fatal error: pyconfig.h: No such file or directory
 #    include <pyconfig.h>
              ^~~~~~~~~~~~
compilation terminated.
error: command '/openwrt/staging_dir/host/bin/ccache_cc' failed with exit code 1
make[3]: *** [Makefile:47: /openwrt/build_dir/target-mips_24kc_musl/pypi/bcrypt-3.1.7/.built] Error 1
```
