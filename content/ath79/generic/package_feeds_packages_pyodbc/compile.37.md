---
title: "compile.37"
date: 2021-06-20 22:33:34.435641
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
make package/feeds/packages/pyodbc/compile -j$(nproc) || make package/feeds/packages/pyodbc/compile V=s
```

#### Compile.txt

``` bash
/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/setuptools/dist.py:642: UserWarning: Usage of dash-separated 'library-dirs' will not be supported in future versions. Please use the underscore name 'library_dirs' instead
  warnings.warn(
/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/setuptools/dist.py:642: UserWarning: Usage of dash-separated 'library-dirs' will not be supported in future versions. Please use the underscore name 'library_dirs' instead
  warnings.warn(
running install
running build
running build_ext
building 'pyodbc' extension
creating build
creating build/temp.-3.9
creating build/temp.-3.9/src
ccache_cc -Wno-unused-result -Wsign-compare -DNDEBUG -g -O3 -Wall -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/pypi/pyodbc-4.0.30=pyodbc-4.0.30 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -fPIC -DPYODBC_VERSION=4.0.30 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -c src/buffer.cpp -o build/temp.-3.9/src/buffer.o -Wno-write-strings -DHAVE_UNISTD_H -DHAVE_PWD_H -DHAVE_SYS_TYPES_H -DHAVE_LONG_LONG -DSIZEOF_LONG_INT=4 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include
In file included from src/buffer.cpp:12:
src/pyodbc.h:45:10: fatal error: Python.h: No such file or directory
 #include <Python.h>
          ^~~~~~~~~~
compilation terminated.
error: command '/openwrt/staging_dir/host/bin/ccache_cc' failed with exit code 1
make[3]: *** [Makefile:46: /openwrt/build_dir/target-mips_24kc_musl/pypi/pyodbc-4.0.30/.built] Error 1
```
