---
title: "compile.37"
date: 2021-06-20 22:26:36.902269
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
make package/feeds/packages/softethervpn/compile -j$(nproc) || make package/feeds/packages/softethervpn/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/103-noeucjp.patch using plaintext: 
patching file src/Mayaqua/Internat.c

Applying ./patches/110-no-m64.patch using plaintext: 
patching file src/makefiles/linux_64bit.mak

Applying ./patches/120-openssl-deprecated.patch using plaintext: 
patching file src/Mayaqua/Encrypt.c
patching file src/Mayaqua/Encrypt.h
patching file src/Mayaqua/Network.c
patching file src/Mayaqua/Secure.c

Applying ./patches/130-iconv.patch using plaintext: 
patching file src/Mayaqua/Mayaqua.h
patching file src/makefiles/linux_32bit.mak
patching file src/makefiles/linux_64bit.mak
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/softethervpn/v4.34-9745'
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/softethervpn/v4.34-9745=v4.34-9745 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DSSL_OP_NO_SSLv3 -minterlink-mips16 -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -znow -zrelro -DNDEBUG -DVPN_SPEED -DUNIX -DUNIX_LINUX -D_REENTRANT -DREENTRANT -D_THREAD_SAFE -D_THREADSAFE -DTHREAD_SAFE -DTHREADSAFE -D_FILE_OFFSET_BITS=64 -I./src/ -I./src/Cedar/ -I./src/Mayaqua/ -O2 -fsigned-char -c src/Mayaqua/Cfg.c -o tmp/objs/Mayaqua/Cfg.o
In file included from ./src/Mayaqua/Mayaqua.h:265,
                 from src/Mayaqua/Cfg.c:116:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/poll.h:1:2: warning: #warning redirecting incorrect #include <sys/poll.h> to <poll.h> [-Wcpp]
 #warning redirecting incorrect #include <sys/poll.h> to <poll.h>
  ^~~~~~~
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/softethervpn/v4.34-9745=v4.34-9745 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DSSL_OP_NO_SSLv3 -minterlink-mips16 -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -znow -zrelro -DNDEBUG -DVPN_SPEED -DUNIX -DUNIX_LINUX -D_REENTRANT -DREENTRANT -D_THREAD_SAFE -D_THREADSAFE -DTHREAD_SAFE -DTHREADSAFE -D_FILE_OFFSET_BITS=64 -I./src/ -I./src/Cedar/ -I./src/Mayaqua/ -O2 -fsigned-char -c src/Mayaqua/Encrypt.c -o tmp/objs/Mayaqua/Encrypt.o
src/Mayaqua/Encrypt.c:118:10: fatal error: openssl/ssl.h: No such file or directory
 #include <openssl/ssl.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
make[4]: *** [src/makefiles/linux_32bit.mak:114: tmp/objs/Mayaqua/Encrypt.o] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/softethervpn/v4.34-9745'
make[3]: *** [Makefile:197: /openwrt/build_dir/target-mips_24kc_musl/softethervpn/v4.34-9745/.built] Error 2
```
