---
title: "compile.40"
date: 2021-06-22 10:50:44.052629
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
make package/feeds/packages/hcxtools/compile -j$(nproc) || make package/feeds/packages/hcxtools/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-openssl.patch using plaintext: 
patching file hcxhashtool.c
patching file hcxpcapngtool.c
patching file hcxpmktool.c
patching file hcxpsktool.c
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/hcxtools-6.1.6'
mkdir -p .deps
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/hcxtools-6.1.6=hcxtools-6.1.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -MMD -MF .deps/hcxpcapngtool.d -o hcxpcapngtool hcxpcapngtool.c  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lz   -DVERSION_TAG=\"6.1.6\" -DVERSION_YEAR=\"2021\"
hcxpcapngtool.c:20:10: fatal error: openssl/conf.h: No such file or directory
 #include <openssl/conf.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
make[4]: *** [Makefile:116: hcxpcapngtool] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/hcxtools-6.1.6'
make[3]: *** [Makefile:64: /openwrt/build_dir/target-mips_24kc_musl/hcxtools-6.1.6/.built] Error 2
```
