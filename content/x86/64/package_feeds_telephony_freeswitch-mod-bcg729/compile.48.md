---
title: "compile.48"
date: 2021-02-22 14:41:04.521718
hidden: false
draft: false
weight: -48
---

build number: `48`

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
make[3]: *** [Makefile:84: /openwrt/build_dir/target-x86_64_musl/freeswitch-mod-bcg729-20170629/.built] Error 1
```
