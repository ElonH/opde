---
title: "compile.41"
date: 2021-06-23 23:18:49.910464
hidden: false
draft: false
weight: -41
---

build number: `41`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/luasql/compile -j$(nproc) || make package/feeds/packages/luasql/compile V=s
```

#### Compile.txt

``` bash
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/luasql-mysql/luasql-2.4.0'
ccache_cc -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/luasql-mysql/luasql-2.4.0=luasql-2.4.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -std=gnu99 -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -DLUA_USE_LINUX -c src/luasql.c -o src/luasql.o
ccache_cc -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/luasql-mysql/luasql-2.4.0=luasql-2.4.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -std=gnu99 -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -DLUA_USE_LINUX src/ls_mysql.c -o src/mysql.so -shared src/luasql.o -I/openwrt/staging_dir/target-x86_64_musl/usr/include/mysql -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/mysql -lmysqlclient -lz
src/ls_mysql.c:19:10: fatal error: mysql.h: No such file or directory
 #include "mysql.h"
          ^~~~~~~~~
compilation terminated.
make[4]: *** [Makefile:24: src/mysql.so] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/luasql-mysql/luasql-2.4.0'
make[3]: *** [Makefile:112: /openwrt/build_dir/target-x86_64_musl/luasql-mysql/luasql-2.4.0/.built] Error 2
```
