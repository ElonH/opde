---
title: "compile.52"
date: 2021-03-09 13:46:57.318002
hidden: false
draft: false
weight: -52
---

build number: `52`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/base/mt76/compile -j$(nproc) || make package/feeds/base/mt76/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-allow-vht-on-2g.patch using plaintext: 
patching file mac80211.c
make[3]: *** No rule to make target '/openwrt/staging_dir/target-x86_64_musl/usr/include/mac80211-backport/backport/autoconf.h', needed by '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/mt76-2020-03-10-08054d5a/.configured_90cfbe17226f457e38768d3d3063649a'.  Stop.
```
