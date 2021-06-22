---
title: "compile.40"
date: 2021-06-22 10:51:50.607796
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
make package/feeds/packages/i2pd/compile -j$(nproc) || make package/feeds/packages/i2pd/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-config.patch using plaintext: 
patching file contrib/i2pd.conf
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/i2pd-2.38.0'
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/i2pd-2.38.0'
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/i2pd-2.38.0'
ccache_cxx -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/i2pd-2.38.0=i2pd-2.38.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -std=c++17 -fPIC -MMD -MP -Ilibi2pd -Ilibi2pd_client  -c -o obj/libi2pd/TunnelGateway.o libi2pd/TunnelGateway.cpp
In file included from libi2pd/TunnelGateway.cpp:10:
libi2pd/Crypto.h:15:10: fatal error: openssl/bn.h: No such file or directory
 #include <openssl/bn.h>
          ^~~~~~~~~~~~~~
compilation terminated.
make[4]: *** [Makefile:80: obj/libi2pd/TunnelGateway.o] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/i2pd-2.38.0'
make[3]: *** [Makefile:83: /openwrt/build_dir/target-mips_24kc_musl/i2pd-2.38.0/.built] Error 2
```
