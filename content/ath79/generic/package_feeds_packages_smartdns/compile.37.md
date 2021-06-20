---
title: "compile.37"
date: 2021-06-20 22:36:26.353831
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
make package/feeds/packages/smartdns/compile -j$(nproc) || make package/feeds/packages/smartdns/compile V=s
```

#### Compile.txt

``` bash
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/smartdns-1.2021.24/src'
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/smartdns-1.2021.24=smartdns-1.2021.24 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -Iinclude -DBASE_FILE_NAME=\"smartdns.c\" -DSMARTDNS_VERION=\"1.2021.24\"   -c -o smartdns.o smartdns.c
smartdns.c:34:10: fatal error: openssl/err.h: No such file or directory
 #include <openssl/err.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
make[4]: *** [<builtin>: smartdns.o] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/smartdns-1.2021.24/src'
make[3]: *** [Makefile:72: /openwrt/build_dir/target-mips_24kc_musl/smartdns-1.2021.24/.built] Error 2
```
