---
title: "compile.40"
date: 2021-06-22 10:50:06.153436
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
make package/feeds/packages/luasec/compile -j$(nproc) || make package/feeds/packages/luasec/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/100-fix-compilation.patch using plaintext: 
patching file src/Makefile
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/luasec-0.9'
---------------------
** Build for Linux **
---------------------
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/luasec-0.9/src'
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/luasec-0.9/src'
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/luasec-0.9/src/luasocket'
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/luasec-0.9=luasec-0.9 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include   -I.  -DWITH_LUASOCKET -I.  -DWITH_LUASOCKET -DLUASOCKET_DEBUG   -c -o io.o io.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/luasec-0.9=luasec-0.9 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include   -I.  -DWITH_LUASOCKET -I.  -DWITH_LUASOCKET -DLUASOCKET_DEBUG   -c -o buffer.o buffer.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/luasec-0.9=luasec-0.9 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include   -I.  -DWITH_LUASOCKET -I.  -DWITH_LUASOCKET -DLUASOCKET_DEBUG   -c -o timeout.o timeout.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/luasec-0.9=luasec-0.9 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include   -I.  -DWITH_LUASOCKET -I.  -DWITH_LUASOCKET -DLUASOCKET_DEBUG   -c -o usocket.o usocket.c
In file included from usocket.h:35,
                 from socket.h:20,
                 from usocket.c:12:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/poll.h:1:2: warning: #warning redirecting incorrect #include <sys/poll.h> to <poll.h> [-Wcpp]
 #warning redirecting incorrect #include <sys/poll.h> to <poll.h>
  ^~~~~~~
mips-openwrt-linux-musl-gcc-ar rcu libluasocket.a io.o buffer.o timeout.o usocket.o
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
mips-openwrt-linux-musl-gcc-ranlib libluasocket.a
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/luasec-0.9/src/luasocket'
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/luasec-0.9=luasec-0.9 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include   -I.  -DWITH_LUASOCKET   -c -o options.o options.c
options.c:8:10: fatal error: openssl/ssl.h: No such file or directory
 #include <openssl/ssl.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
make[6]: *** [<builtin>: options.o] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/luasec-0.9/src'
make[5]: *** [Makefile:43: linux] Error 2
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/luasec-0.9/src'
make[4]: *** [Makefile:41: linux] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/luasec-0.9'
make[3]: *** [Makefile:68: /openwrt/build_dir/target-mips_24kc_musl/luasec-0.9/.built] Error 2
```
