---
title: "compile.37"
date: 2021-06-20 22:36:26.331748
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
make package/feeds/packages/uanytun/compile -j$(nproc) || make package/feeds/packages/uanytun/compile V=s
```

#### Compile.txt

``` bash
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/uanytun-sslcrypt/uanytun-0.3.7/src'
(re)building auth_algo.d
(re)building key_derivation.d
(re)building uanytun.d
(re)building cipher.d
(re)building seq_window.d
(re)building encrypted_packet.d
(re)building plain_packet.d
(re)building udp.d
(re)building tun.d
(re)building options.d
(re)building sysexec.d
(re)building sig_handler.d
(re)building string_list.d
(re)building log.d
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/uanytun-sslcrypt/uanytun-0.3.7=uanytun-0.3.7 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -DUSE_SSL_CRYPTO -DCRYPTO_LIB_NAME=\"OpenSSL\" -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -c log.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/uanytun-sslcrypt/uanytun-0.3.7=uanytun-0.3.7 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -DUSE_SSL_CRYPTO -DCRYPTO_LIB_NAME=\"OpenSSL\" -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -c string_list.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/uanytun-sslcrypt/uanytun-0.3.7=uanytun-0.3.7 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -DUSE_SSL_CRYPTO -DCRYPTO_LIB_NAME=\"OpenSSL\" -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -c sig_handler.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/uanytun-sslcrypt/uanytun-0.3.7=uanytun-0.3.7 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -DUSE_SSL_CRYPTO -DCRYPTO_LIB_NAME=\"OpenSSL\" -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -c sysexec.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/uanytun-sslcrypt/uanytun-0.3.7=uanytun-0.3.7 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -DUSE_SSL_CRYPTO -DCRYPTO_LIB_NAME=\"OpenSSL\" -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -c options.c
In file included from options.c:62:
auth_algo.h:53:10: fatal error: openssl/hmac.h: No such file or directory
 #include <openssl/hmac.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
make[4]: *** [Makefile:95: options.o] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/uanytun-sslcrypt/uanytun-0.3.7/src'
make[3]: *** [Makefile:173: /openwrt/build_dir/target-mips_24kc_musl/uanytun-sslcrypt/uanytun-0.3.7/.built] Error 2
```
