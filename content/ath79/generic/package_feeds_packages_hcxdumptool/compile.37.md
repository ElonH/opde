---
title: "compile.37"
date: 2021-06-20 22:36:26.337665
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
make package/feeds/packages/hcxdumptool/compile -j$(nproc) || make package/feeds/packages/hcxdumptool/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-openssl.patch using plaintext: 
patching file hcxdumptool.c

Applying ./patches/020-stdout.patch using plaintext: 
patching file hcxdumptool.c
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/hcxdumptool-6.1.6'
mkdir -p .deps
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/hcxdumptool-6.1.6=hcxdumptool-6.1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro   -MMD -MF .deps/hcxdumptool.d -o hcxdumptool hcxdumptool.c   -DVERSION_TAG=\"6.1.6\" -DVERSION_YEAR=\"2021\"
hcxdumptool.c:42:10: fatal error: openssl/conf.h: No such file or directory
 #include <openssl/conf.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
make[4]: *** [Makefile:73: hcxdumptool] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/hcxdumptool-6.1.6'
make[3]: *** [Makefile:55: /openwrt/build_dir/target-mips_24kc_musl/hcxdumptool-6.1.6/.built] Error 2
```
