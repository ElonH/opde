---
title: "compile.41"
date: 2021-06-23 23:17:45.602106
hidden: false
draft: false
weight: -41
---

build number: `41`

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
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/restund-0.4.12'
  CC [M]  build-x86_64/modules/binding/binding.o
  CC [M]  build-x86_64/modules/auth/auth.o
  CC [M]  build-x86_64/modules/turn/alloc.o
  CC [M]  build-x86_64/modules/turn/chan.o
  CC [M]  build-x86_64/modules/turn/perm.o
  CC [M]  build-x86_64/modules/turn/turn.o
  CC [M]  build-x86_64/modules/stat/stat.o
  CC [M]  build-x86_64/modules/status/status.o
  CC [M]  build-x86_64/modules/status/httpd.o
  CC [M]  build-x86_64/modules/filedb/filedb.o
  CC [M]  build-x86_64/modules/restauth/restauth.o
  CC [M]  build-x86_64/modules/syslog/syslog.o
  CC [M]  build-x86_64/modules/mysql_ser/mysql_ser.o
modules/mysql_ser/mysql_ser.c:9:10: fatal error: mysql/mysql.h: No such file or directory
 #include <mysql/mysql.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
make[4]: *** [mk/mod.mk:30: build-x86_64/modules/mysql_ser/mysql_ser.o] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/restund-0.4.12'
make[3]: *** [Makefile:124: /openwrt/build_dir/target-x86_64_musl/restund-0.4.12/.built] Error 2
```
