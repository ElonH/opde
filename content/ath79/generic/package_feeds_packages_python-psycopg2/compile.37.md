---
title: "compile.37"
date: 2021-06-20 22:26:36.881261
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
make package/feeds/packages/python-psycopg2/compile -j$(nproc) || make package/feeds/packages/python-psycopg2/compile V=s
```

#### Compile.txt

``` bash
running install
running build
running build_py
creating build
creating build/lib.-3.9
creating build/lib.-3.9/psycopg2
copying lib/_lru_cache.py -> build/lib.-3.9/psycopg2
copying lib/_range.py -> build/lib.-3.9/psycopg2
copying lib/extras.py -> build/lib.-3.9/psycopg2
copying lib/sql.py -> build/lib.-3.9/psycopg2
copying lib/__init__.py -> build/lib.-3.9/psycopg2
copying lib/_ipaddress.py -> build/lib.-3.9/psycopg2
copying lib/extensions.py -> build/lib.-3.9/psycopg2
copying lib/_json.py -> build/lib.-3.9/psycopg2
copying lib/pool.py -> build/lib.-3.9/psycopg2
copying lib/errors.py -> build/lib.-3.9/psycopg2
copying lib/tz.py -> build/lib.-3.9/psycopg2
copying lib/errorcodes.py -> build/lib.-3.9/psycopg2
copying lib/compat.py -> build/lib.-3.9/psycopg2
warning: build_py: byte-compiling is disabled, skipping.

running build_ext
building 'psycopg2._psycopg' extension
creating build/temp.-3.9
creating build/temp.-3.9/psycopg
ccache_cc -Wno-unused-result -Wsign-compare -DNDEBUG -g -O3 -Wall -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/pypi/psycopg2-2.8.6=psycopg2-2.8.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -fPIC -DPSYCOPG_VERSION=2.8.6 (dt dec pq3 ext lo64) -DPG_VERSION_NUM=130002 -DHAVE_LO64=1 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -I. -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/postgresql/server -c psycopg/adapter_asis.c -o build/temp.-3.9/psycopg/adapter_asis.o -Wdeclaration-after-statement
In file included from psycopg/adapter_asis.c:28:
./psycopg/psycopg.h:35:10: fatal error: Python.h: No such file or directory
 #include <Python.h>
          ^~~~~~~~~~
compilation terminated.

It appears you are missing some prerequisite to build the package from source.

You may install a binary package by installing 'psycopg2-binary' from PyPI.
If you want to install psycopg2 from source, please install the packages
required for the build and try again.

For further information please check the 'doc/src/install.rst' file (also at
<https://www.psycopg.org/docs/install.html>).

error: command '/openwrt/staging_dir/host/bin/ccache_cc' failed with exit code 1
make[3]: *** [Makefile:44: /openwrt/build_dir/target-mips_24kc_musl/pypi/psycopg2-2.8.6/.built] Error 1
```
