---
title: "compile.42"
date: 2021-06-29 09:35:34.997161
hidden: false
draft: false
weight: -42
---

build number: `42`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/bluelog/compile -j$(nproc) || make package/feeds/packages/bluelog/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/100-gen-oui-fix-tempfile-use-mirror.patch using plaintext: 
patching file gen_oui.sh
make[4]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/Bluelog-1.1.2'
ccache_cc -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/Bluelog-1.1.2=Bluelog-1.1.2 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DOPENWRT  -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include  -Wall -O2  bluelog.c -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro -lbluetooth -lm -o bluelog
bluelog.c:32:10: fatal error: bluetooth/bluetooth.h: No such file or directory
 #include <bluetooth/bluetooth.h>
          ^~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
make[4]: *** [Makefile:29: bluelog] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/Bluelog-1.1.2'
make[3]: *** [Makefile:112: /openwrt/build_dir/target-aarch64_cortex-a72_musl/Bluelog-1.1.2/.built] Error 2
```
