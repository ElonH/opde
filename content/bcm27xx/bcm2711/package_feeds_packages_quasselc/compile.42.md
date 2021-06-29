---
title: "compile.42"
date: 2021-06-29 09:35:35.003464
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
make package/feeds/packages/quasselc/compile -j$(nproc) || make package/feeds/packages/quasselc/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-respect-cflags-ldflags.patch using plaintext: 
patching file Makefile
make[4]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/QuasselC-a0a1e6bd87d3eac68b5369972d1c2035cfe47e94'
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
ccache_cc -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/QuasselC-a0a1e6bd87d3eac68b5369972d1c2035cfe47e94=QuasselC-a0a1e6bd87d3eac68b5369972d1c2035cfe47e94 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include  -Wall -g -Wextra  -Wswitch-enum -std=gnu11 -fPIC   -c -o bot.o bot.c
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
In file included from bot.c:27:
quasselc.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
make[4]: *** [<builtin>: bot.o] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/QuasselC-a0a1e6bd87d3eac68b5369972d1c2035cfe47e94'
make[3]: *** [Makefile:66: /openwrt/build_dir/target-aarch64_cortex-a72_musl/QuasselC-a0a1e6bd87d3eac68b5369972d1c2035cfe47e94/.built] Error 2
```
