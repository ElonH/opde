---
title: "compile.37"
date: 2021-06-20 22:36:26.383211
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
make package/feeds/telephony/restund/compile -j$(nproc) || make package/feeds/telephony/restund/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/100-reproducible-builds.patch using plaintext: 
patching file modules/status/status.c
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/restund-0.4.12'
  CC [M]  build-mips/modules/binding/binding.o
  CC [M]  build-mips/modules/auth/auth.o
  CC [M]  build-mips/modules/turn/alloc.o
  CC [M]  build-mips/modules/turn/chan.o
  CC [M]  build-mips/modules/turn/perm.o
  CC [M]  build-mips/modules/turn/turn.o
  CC [M]  build-mips/modules/stat/stat.o
  CC [M]  build-mips/modules/status/status.o
  CC [M]  build-mips/modules/status/httpd.o
  CC [M]  build-mips/modules/filedb/filedb.o
  CC [M]  build-mips/modules/restauth/restauth.o
  CC [M]  build-mips/modules/syslog/syslog.o
  CC [M]  build-mips/modules/mysql_ser/mysql_ser.o
modules/mysql_ser/mysql_ser.c:9:10: fatal error: mysql/mysql.h: No such file or directory
 #include <mysql/mysql.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
make[4]: *** [mk/mod.mk:30: build-mips/modules/mysql_ser/mysql_ser.o] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/restund-0.4.12'
make[3]: *** [Makefile:124: /openwrt/build_dir/target-mips_24kc_musl/restund-0.4.12/.built] Error 2
```
