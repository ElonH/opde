---
title: "compile.40"
date: 2021-06-22 10:41:19.972525
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
make package/feeds/base/adb/compile -j$(nproc) || make package/feeds/base/adb/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-create_Makefile.patch using plaintext: 
patching file adb/Makefile

Applying ./patches/003-fix-musl-build.patch using plaintext: 
patching file adb/usb_linux.c

Applying ./patches/010-openssl-1.1.patch using plaintext: 
patching file adb/adb_auth_host.c

Applying ./patches/020-cherry-picked-superspeed-fix.patch using plaintext: 
patching file adb/usb_linux.c
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/adb-6fe92d1a3fb17545d82d020a3c995f32e6b71f9d/adb'
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/adb-6fe92d1a3fb17545d82d020a3c995f32e6b71f9d=adb-6fe92d1a3fb17545d82d020a3c995f32e6b71f9d -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_BIG_ENDIAN=1 -D_GNU_SOURCE -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -DADB_HOST=1 -DHAVE_FORKEXEC=1 -I. -I../include -D_FILE_OFFSET_BITS=64  -c -o adb.o adb.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/adb-6fe92d1a3fb17545d82d020a3c995f32e6b71f9d=adb-6fe92d1a3fb17545d82d020a3c995f32e6b71f9d -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DHAVE_BIG_ENDIAN=1 -D_GNU_SOURCE -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -DADB_HOST=1 -DHAVE_FORKEXEC=1 -I. -I../include -D_FILE_OFFSET_BITS=64  -c -o adb_auth_host.o adb_auth_host.c
adb_auth_host.c:42:10: fatal error: openssl/evp.h: No such file or directory
 #include <openssl/evp.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
make[4]: *** [<builtin>: adb_auth_host.o] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/adb-6fe92d1a3fb17545d82d020a3c995f32e6b71f9d/adb'
make[3]: *** [Makefile:56: /openwrt/build_dir/target-mips_24kc_musl/adb-6fe92d1a3fb17545d82d020a3c995f32e6b71f9d/.built] Error 2
```
