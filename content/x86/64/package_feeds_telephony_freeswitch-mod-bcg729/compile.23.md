---
title: "compile.23"
date: 2021-05-27 00:00:11.286166
hidden: false
draft: false
weight: -23
---

build number: `23`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/telephony/freeswitch-mod-bcg729/compile -j$(nproc) || make package/feeds/telephony/freeswitch-mod-bcg729/compile V=s
```

#### Compile.txt

``` bash
mod_bcg729.c:30:10: fatal error: switch.h: No such file or directory
 #include "switch.h"
          ^~~~~~~~~~
compilation terminated.
make[3]: *** [Makefile:82: /openwrt/build_dir/target-x86_64_musl/freeswitch-mod-bcg729-2017-06-29-686eb06d/.built] Error 1
```
