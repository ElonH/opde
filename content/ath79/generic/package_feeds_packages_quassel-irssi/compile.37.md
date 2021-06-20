---
title: "compile.37"
date: 2021-06-20 22:26:36.901263
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
make package/feeds/packages/quassel-irssi/compile -j$(nproc) || make package/feeds/packages/quassel-irssi/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-respect-cflags.patch using plaintext: 
patching file core/Makefile

Applying ./patches/002-use-cc-var.patch using plaintext: 
patching file core/Makefile

Applying ./patches/003-use-pkgconfig-ldflags-quasselc.patch using plaintext: 
patching file core/Makefile

Applying ./patches/010-Get-compatible-with-potential-irssi-abi-8-and-drop-p.patch using plaintext: 
patching file core/Makefile
patching file core/quassel-net.c
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/quassel-irssi-079be662dde374a383646256108a4974c2bc7796/core'
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/quassel-irssi-079be662dde374a383646256108a4974c2bc7796=quassel-irssi-079be662dde374a383646256108a4974c2bc7796 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -std=gnu11 -Wall -Wextra -g -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/quassel-irssi-079be662dde374a383646256108a4974c2bc7796=quassel-irssi-079be662dde374a383646256108a4974c2bc7796 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/irssi/src/ -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/irssi/src/core/ -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/irssi/src/fe-common/ -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/irssi/src/fe-common/core/ -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/irssi/src/fe-text/ -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -DUOFF_T_LONG -fPIC -DHAVE_OPENSSL -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/quasselc  -Wmissing-prototypes -Wmissing-declarations    -c -o quasselc-connector.o quasselc-connector.c
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
cc1: note: someone does not honour COPTS correctly, passed 2 times
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/quassel-irssi-079be662dde374a383646256108a4974c2bc7796=quassel-irssi-079be662dde374a383646256108a4974c2bc7796 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -std=gnu11 -Wall -Wextra -g -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/quassel-irssi-079be662dde374a383646256108a4974c2bc7796=quassel-irssi-079be662dde374a383646256108a4974c2bc7796 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/irssi/src/ -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/irssi/src/core/ -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/irssi/src/fe-common/ -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/irssi/src/fe-common/core/ -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/irssi/src/fe-text/ -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -DUOFF_T_LONG -fPIC -DHAVE_OPENSSL -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/quasselc  -Wmissing-prototypes -Wmissing-declarations    -c -o quassel-core.o quassel-core.c
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
cc1: note: someone does not honour COPTS correctly, passed 2 times
quassel-core.c:20:10: fatal error: module.h: No such file or directory
 #include <module.h>
          ^~~~~~~~~~
compilation terminated.
make[4]: *** [<builtin>: quassel-core.o] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/quassel-irssi-079be662dde374a383646256108a4974c2bc7796/core'
make[3]: *** [Makefile:54: /openwrt/build_dir/target-mips_24kc_musl/quassel-irssi-079be662dde374a383646256108a4974c2bc7796/.built] Error 2
```
