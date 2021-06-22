---
title: "compile.40"
date: 2021-06-22 10:37:31.195174
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
make package/feeds/packages/redsocks/compile -j$(nproc) || make package/feeds/packages/redsocks/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/0006-fix_default_config_location.patch using plaintext: 
patching file main.c
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/redsocks-release-0.5'
mkdir -p gen
touch gen/.build
rm -f gen/version.c.tmp
echo '/* this file is auto-generated during build */' > gen/version.c.tmp
echo '#include "../version.h"' >> gen/version.c.tmp
echo 'const char* redsocks_version = ' >> gen/version.c.tmp
if [ -d .git ]; then \
	echo '"redsocks.git/'`git describe --tags`'"'; \
	if [ `git status --porcelain | grep -v -c '^??'` != 0 ]; then \
		echo '"'"-unclean-$(date --rfc-3339=seconds | tr ' ' 'T')-${USER}@$(uname -n)"'"'; \
	fi \
else \
	echo '"redsocks/0.5"'; \
fi >> gen/version.c.tmp
echo ';' >> gen/version.c.tmp
mv -f gen/version.c.tmp gen/version.c
gcc -MM parser.c main.c redsocks.c log.c http-connect.c socks4.c socks5.c http-relay.c base.c base64.c md5.c http-auth.c utils.c redudp.c dnstc.c gen/version.c 2>/dev/null >.depend || \
( \
	for I in http-auth.h log.h libc-compat.h list.h redsocks.h parser.h version.h main.h md5.h libevent-compat.h base64.h redudp.h dnstc.h socks5.h utils.h base.h; do \
		export ${I//[-.]/_}_DEPS="`sed '/^\#[ \t]*include \?"\(.*\)".*/!d;s//\1/' $I`"; \
	done; \
	echo -n >.depend; \
	for SRC in parser.c main.c redsocks.c log.c http-connect.c socks4.c socks5.c http-relay.c base.c base64.c md5.c http-auth.c utils.c redudp.c dnstc.c gen/version.c; do \
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
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/redsocks-release-0.5=redsocks-release-0.5 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  -g -O2 -std=c99 -D_XOPEN_SOURCE=600 -D_DEFAULT_SOURCE -D_GNU_SOURCE -Wall   -c -o parser.o parser.c
In file included from parser.c:29:
utils.h:6:10: fatal error: event.h: No such file or directory
 #include <event.h>
          ^~~~~~~~~
compilation terminated.
make[4]: *** [<builtin>: parser.o] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/redsocks-release-0.5'
make[3]: *** [Makefile:60: /openwrt/build_dir/target-mips_24kc_musl/redsocks-release-0.5/.built] Error 2
```
