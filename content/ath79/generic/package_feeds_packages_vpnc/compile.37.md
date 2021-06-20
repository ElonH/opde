---
title: "compile.37"
date: 2021-06-20 22:36:26.332395
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
make package/feeds/packages/vpnc/compile -j$(nproc) || make package/feeds/packages/vpnc/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/110-openssl-deprecated.patch using plaintext: 
patching file src/crypto-openssl.c
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/vpnc-2021-01-31-43780cec'
cd src && LC_ALL=C perl -w ./enum2debug.pl isakmp.h >vpnc-debug.c 2>vpnc-debug.h
Package gnutls was not found in the pkg-config search path.
Perhaps you should add the directory containing `gnutls.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gnutls', required by 'virtual:world', not found
Package gnutls was not found in the pkg-config search path.
Perhaps you should add the directory containing `gnutls.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gnutls', required by 'virtual:world', not found
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/vpnc-2021-01-31-43780cec=vpnc-2021-01-31-43780cec -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -W -Wall -Wmissing-declarations -Wwrite-strings -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DCRYPTO_GNUTLS -DVERSION=\"2021-01-31-43780cec\" -DSCRIPT_PATH=\"/etc/vpnc/vpnc-script\"  -c -o src/sysdep.o src/sysdep.c
Package gnutls was not found in the pkg-config search path.
Perhaps you should add the directory containing `gnutls.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gnutls', required by 'virtual:world', not found
Package gnutls was not found in the pkg-config search path.
Perhaps you should add the directory containing `gnutls.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gnutls', required by 'virtual:world', not found
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/vpnc-2021-01-31-43780cec=vpnc-2021-01-31-43780cec -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -W -Wall -Wmissing-declarations -Wwrite-strings -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DCRYPTO_GNUTLS -DVERSION=\"2021-01-31-43780cec\" -DSCRIPT_PATH=\"/etc/vpnc/vpnc-script\"  -c -o src/vpnc-debug.o src/vpnc-debug.c
Package gnutls was not found in the pkg-config search path.
Perhaps you should add the directory containing `gnutls.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gnutls', required by 'virtual:world', not found
Package gnutls was not found in the pkg-config search path.
Perhaps you should add the directory containing `gnutls.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gnutls', required by 'virtual:world', not found
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/vpnc-2021-01-31-43780cec=vpnc-2021-01-31-43780cec -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -W -Wall -Wmissing-declarations -Wwrite-strings -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DCRYPTO_GNUTLS -DVERSION=\"2021-01-31-43780cec\" -DSCRIPT_PATH=\"/etc/vpnc/vpnc-script\"  -c -o src/isakmp-pkt.o src/isakmp-pkt.c
Package gnutls was not found in the pkg-config search path.
Perhaps you should add the directory containing `gnutls.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gnutls', required by 'virtual:world', not found
Package gnutls was not found in the pkg-config search path.
Perhaps you should add the directory containing `gnutls.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gnutls', required by 'virtual:world', not found
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/vpnc-2021-01-31-43780cec=vpnc-2021-01-31-43780cec -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -W -Wall -Wmissing-declarations -Wwrite-strings -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DCRYPTO_GNUTLS -DVERSION=\"2021-01-31-43780cec\" -DSCRIPT_PATH=\"/etc/vpnc/vpnc-script\"  -c -o src/tunip.o src/tunip.c
Package gnutls was not found in the pkg-config search path.
Perhaps you should add the directory containing `gnutls.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gnutls', required by 'virtual:world', not found
Package gnutls was not found in the pkg-config search path.
Perhaps you should add the directory containing `gnutls.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gnutls', required by 'virtual:world', not found
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/vpnc-2021-01-31-43780cec=vpnc-2021-01-31-43780cec -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -W -Wall -Wmissing-declarations -Wwrite-strings -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DCRYPTO_GNUTLS -DVERSION=\"2021-01-31-43780cec\" -DSCRIPT_PATH=\"/etc/vpnc/vpnc-script\"  -c -o src/config.o src/config.c
Package gnutls was not found in the pkg-config search path.
Perhaps you should add the directory containing `gnutls.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gnutls', required by 'virtual:world', not found
Package gnutls was not found in the pkg-config search path.
Perhaps you should add the directory containing `gnutls.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gnutls', required by 'virtual:world', not found
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/vpnc-2021-01-31-43780cec=vpnc-2021-01-31-43780cec -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -W -Wall -Wmissing-declarations -Wwrite-strings -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DCRYPTO_GNUTLS -DVERSION=\"2021-01-31-43780cec\" -DSCRIPT_PATH=\"/etc/vpnc/vpnc-script\"  -c -o src/dh.o src/dh.c
Package gnutls was not found in the pkg-config search path.
Perhaps you should add the directory containing `gnutls.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gnutls', required by 'virtual:world', not found
Package gnutls was not found in the pkg-config search path.
Perhaps you should add the directory containing `gnutls.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gnutls', required by 'virtual:world', not found
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/vpnc-2021-01-31-43780cec=vpnc-2021-01-31-43780cec -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -W -Wall -Wmissing-declarations -Wwrite-strings -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DCRYPTO_GNUTLS -DVERSION=\"2021-01-31-43780cec\" -DSCRIPT_PATH=\"/etc/vpnc/vpnc-script\"  -c -o src/math_group.o src/math_group.c
Package gnutls was not found in the pkg-config search path.
Perhaps you should add the directory containing `gnutls.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gnutls', required by 'virtual:world', not found
Package gnutls was not found in the pkg-config search path.
Perhaps you should add the directory containing `gnutls.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gnutls', required by 'virtual:world', not found
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/vpnc-2021-01-31-43780cec=vpnc-2021-01-31-43780cec -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -W -Wall -Wmissing-declarations -Wwrite-strings -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DCRYPTO_GNUTLS -DVERSION=\"2021-01-31-43780cec\" -DSCRIPT_PATH=\"/etc/vpnc/vpnc-script\"  -c -o src/supp.o src/supp.c
Package gnutls was not found in the pkg-config search path.
Perhaps you should add the directory containing `gnutls.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gnutls', required by 'virtual:world', not found
Package gnutls was not found in the pkg-config search path.
Perhaps you should add the directory containing `gnutls.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gnutls', required by 'virtual:world', not found
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/vpnc-2021-01-31-43780cec=vpnc-2021-01-31-43780cec -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -W -Wall -Wmissing-declarations -Wwrite-strings -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DCRYPTO_GNUTLS -DVERSION=\"2021-01-31-43780cec\" -DSCRIPT_PATH=\"/etc/vpnc/vpnc-script\"  -c -o src/decrypt-utils.o src/decrypt-utils.c
Package gnutls was not found in the pkg-config search path.
Perhaps you should add the directory containing `gnutls.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gnutls', required by 'virtual:world', not found
Package gnutls was not found in the pkg-config search path.
Perhaps you should add the directory containing `gnutls.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gnutls', required by 'virtual:world', not found
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/vpnc-2021-01-31-43780cec=vpnc-2021-01-31-43780cec -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -W -Wall -Wmissing-declarations -Wwrite-strings -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DCRYPTO_GNUTLS -DVERSION=\"2021-01-31-43780cec\" -DSCRIPT_PATH=\"/etc/vpnc/vpnc-script\"  -c -o src/crypto.o src/crypto.c
Package gnutls was not found in the pkg-config search path.
Perhaps you should add the directory containing `gnutls.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gnutls', required by 'virtual:world', not found
In file included from src/crypto.h:40,
                 from src/crypto.c:29:
src/crypto-gnutls.h:21:10: fatal error: gnutls/gnutls.h: No such file or directory
 #include <gnutls/gnutls.h>
          ^~~~~~~~~~~~~~~~~
compilation terminated.
make[4]: *** [<builtin>: src/crypto.o] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/vpnc-2021-01-31-43780cec'
make[3]: *** [Makefile:93: /openwrt/build_dir/target-mips_24kc_musl/vpnc-2021-01-31-43780cec/.built] Error 2
```
