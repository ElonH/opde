---
title: "compile.37"
date: 2021-06-20 22:36:26.355520
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
make package/feeds/packages/bfdd/compile -j$(nproc) || make package/feeds/packages/bfdd/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/002-ipv6_musl_fix.patch using plaintext: 
patching file bfd_packet.c

Applying ./patches/020-gcc10.patch using plaintext: 
patching file bfd.h
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/bfdd-c54534beb524afc3972039f57b56ec65332b43f7'
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/bfdd-c54534beb524afc3972039f57b56ec65332b43f7=bfdd-c54534beb524afc3972039f57b56ec65332b43f7 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -Wall -Wextra -Og -ggdb -Wstrict-prototypes -Wmissing-prototypes -Wmissing-declarations -Wshadow -Wpointer-arith -Wsign-compare -Wno-implicit-fallthrough bfdd.c -c -o bfdd.o
In file included from bfdd.c:30:
bfd.h:30:10: fatal error: event.h: No such file or directory
 #include <event.h>
          ^~~~~~~~~
compilation terminated.
make[4]: *** [Makefile:25: bfdd.o] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/bfdd-c54534beb524afc3972039f57b56ec65332b43f7'
make[3]: *** [Makefile:62: /openwrt/build_dir/target-mips_24kc_musl/bfdd-c54534beb524afc3972039f57b56ec65332b43f7/.built] Error 2
```
