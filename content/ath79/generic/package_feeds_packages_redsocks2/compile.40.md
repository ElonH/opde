---
title: "compile.40"
date: 2021-06-22 10:37:31.198553
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
make package/feeds/packages/redsocks2/compile -j$(nproc) || make package/feeds/packages/redsocks2/compile V=s
```

#### Compile.txt

``` bash
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/redsocks2-0.67'
Compile with OpenSSL by default. To compile with PolarSSL, run 'make USE_CRYPTO_POLARSSL=true' instead.
mkdir -p gen
touch gen/.build
rm -f -f gen/version.c.tmp
echo '/* this file is auto-generated during build */' > gen/version.c.tmp
echo '#include "../version.h"' >> gen/version.c.tmp
echo 'const char* redsocks_version = ' >> gen/version.c.tmp
if [ -d .git ]; then \
	echo '"redsocks.git/'`git describe --tags`' OpenSSL"'; \
	if [ `git status --porcelain | grep -v -c '^??'` != 0 ]; then \
		echo '"-unclean"'; \
	fi; \
	echo '"\\n"'; \
	echo '"Features: DISABLE_SHADOWSOCKS"'; \
else \
	echo '"redsocks/0.68 OpenSSL"'; \
	echo '"\\n"'; \
	echo '"Features: DISABLE_SHADOWSOCKS"'; \
fi >> gen/version.c.tmp
echo ';' >> gen/version.c.tmp
mv -f gen/version.c.tmp gen/version.c
ccache_cc -MM -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/redsocks2-0.67=redsocks2-0.67 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC -O3 -DDISABLE_SHADOWSOCKS -D_BSD_SOURCE -D_DEFAULT_SOURCE -Wall -std=c99 -D_XOPEN_SOURCE=600 -DUSE_CRYPTO_OPENSSL parser.c main.c redsocks.c log.c direct.c ipcache.c autoproxy.c http-connect.c socks4.c socks5.c http-relay.c base.c base64.c md5.c http-auth.c utils.c redudp.c socks5-udp.c tcpdns.c gen/version.c 2>/dev/null >.depend || \
( \
	for I in redsocks.h list.h encrypt.h md5.h tcpdns.h shadowsocks.h socks5.h log.h base.h libc-compat.h http-auth.h parser.h version.h main.h base64.h redudp.h ipcache.h utils.h; do \
		export ${I//[-.]/_}_DEPS="`sed '/^\#[ \t]*include \?"\(.*\)".*/!d;s//\1/' $I`"; \
	done; \
	echo -n >.depend; \
	for SRC in parser.c main.c redsocks.c log.c direct.c ipcache.c autoproxy.c http-connect.c socks4.c socks5.c http-relay.c base.c base64.c md5.c http-auth.c utils.c redudp.c socks5-udp.c tcpdns.c gen/version.c; do \
		echo -n "${SRC%.c}.o: " >>.depend; \
		export SRC_DEPS="`sed '/\#[ \t]*include \?"\(.*\)".*/!d;s//\1/' $SRC | sort`"; \
		while true; do \
			export SRC_DEPS_OLD="$SRC_DEPS"; \
			export SRC_DEEP_DEPS=""; \
			for HDR in $SRC_DEPS; do \
				eval export SRC_DEEP_DEPS="\"$SRC_DEEP_DEPS \$${HDR//[-.]/_}_DEPS\""; \
			done; \
			export SRC_DEPS="`echo $SRC_DEPS $SRC_DEEP_DEPS | sed 's/  */\n/g' | sort -u`"; \
			test "$SRC_DEPS" = "$SRC_DEPS_OLD" && break; \
		done; \
		echo $SRC $SRC_DEPS >>.depend; \
	done; \
)
Compile with OpenSSL by default. To compile with PolarSSL, run 'make USE_CRYPTO_POLARSSL=true' instead.
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/redsocks2-0.67=redsocks2-0.67 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -fPIC -O3 -DDISABLE_SHADOWSOCKS -D_BSD_SOURCE -D_DEFAULT_SOURCE -Wall -std=c99 -D_XOPEN_SOURCE=600 -DUSE_CRYPTO_OPENSSL   -c -o parser.o parser.c
In file included from parser.c:29:
utils.h:7:10: fatal error: event2/event.h: No such file or directory
 #include <event2/event.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
make[4]: *** [<builtin>: parser.o] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/redsocks2-0.67'
make[3]: *** [Makefile:56: /openwrt/build_dir/target-mips_24kc_musl/redsocks2-0.67/.built] Error 2
```
