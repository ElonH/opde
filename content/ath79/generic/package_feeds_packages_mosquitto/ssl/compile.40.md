---
title: "compile.40"
date: 2021-06-22 10:47:21.974228
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
make package/feeds/packages/mosquitto/compile -j$(nproc) || make package/feeds/packages/mosquitto/compile V=s
```

#### Compile.txt

``` bash
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/mosquitto-ssl/mosquitto-2.0.11'
set -e; for d in lib apps client plugins src; do make -C ${d}; done
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/mosquitto-ssl/mosquitto-2.0.11/lib'
ccache_cc  -I. -I.. -I../include -I../../include -DWITH_TLS -DWITH_TLS_PSK -DWITH_THREADING -DWITH_SOCKS -DWITH_UNIX_SOCKETS -I../deps -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/mosquitto-ssl/mosquitto-2.0.11=mosquitto-2.0.11 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC -c mosquitto.c -o mosquitto.o
In file included from mosquitto.c:19:
../config.h:61:12: fatal error: openssl/opensslconf.h: No such file or directory
 #  include <openssl/opensslconf.h>
            ^~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
make[5]: *** [Makefile:102: mosquitto.o] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/mosquitto-ssl/mosquitto-2.0.11/lib'
make[4]: *** [Makefile:66: mosquitto] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/mosquitto-ssl/mosquitto-2.0.11'
make[3]: *** [Makefile:248: /openwrt/build_dir/target-mips_24kc_musl/mosquitto-ssl/mosquitto-2.0.11/.built] Error 2
```
