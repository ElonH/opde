---
title: "compile.40"
date: 2021-06-22 10:50:06.152361
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
make package/feeds/packages/prosody/compile -j$(nproc) || make package/feeds/packages/prosody/compile V=s
```

#### Compile.txt

``` bash
Lua version detected: 5.1
Lua interpreter found: /openwrt/staging_dir/hostpkg/bin/lua...
Checking Lua includes... lua.h found in /openwrt/staging_dir/target-mips_24kc_musl/usr/include/lua.h
Checking if Lua header version matches that of the interpreter... yes
Writing configuration...

Installation prefix: /usr
Prosody configuration directory: /etc/prosody
Using Lua from: /openwrt/staging_dir/hostpkg

Done. You can now run 'make' to build.

make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/prosody-0.11.7'
sed "1s| lua$| lua|; \
	s|^CFG_SOURCEDIR=.*;$|CFG_SOURCEDIR='/usr/lib/prosody';|; \
	s|^CFG_CONFIGDIR=.*;$|CFG_CONFIGDIR='/etc/prosody';|; \
	s|^CFG_DATADIR=.*;$|CFG_DATADIR='/etc/prosody/data';|; \
	s|^CFG_PLUGINDIR=.*;$|CFG_PLUGINDIR='/usr/lib/prosody/modules/';|;" < prosody > prosody.install
sed "1s| lua$| lua|; \
	s|^CFG_SOURCEDIR=.*;$|CFG_SOURCEDIR='/usr/lib/prosody';|; \
	s|^CFG_CONFIGDIR=.*;$|CFG_CONFIGDIR='/etc/prosody';|; \
	s|^CFG_DATADIR=.*;$|CFG_DATADIR='/etc/prosody/data';|; \
	s|^CFG_PLUGINDIR=.*;$|CFG_PLUGINDIR='/usr/lib/prosody/modules/';|;" < prosodyctl > prosodyctl.install
sed 's|certs/|/etc/prosody/certs/|' prosody.cfg.lua.dist > prosody.cfg.lua.install
cp prosody.release prosody.version
make -C util-src install
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/prosody-0.11.7/util-src'
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/prosody-0.11.7=prosody-0.11.7 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -c -o encodings.o encodings.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/prosody-0.11.7=prosody-0.11.7 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -c -o hashes.o hashes.c
hashes.c:26:10: fatal error: openssl/sha.h: No such file or directory
 #include <openssl/sha.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
make[5]: *** [<builtin>: hashes.o] Error 1
rm encodings.o
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/prosody-0.11.7/util-src'
make[4]: *** [GNUmakefile:28: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/prosody-0.11.7'
make[3]: *** [Makefile:132: /openwrt/build_dir/target-mips_24kc_musl/prosody-0.11.7/.built] Error 2
```
