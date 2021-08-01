---
title: "compile.44"
date: 2021-08-01 09:45:27.117654
hidden: false
draft: false
weight: -44
---

build number: `44`

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
Applying ./patches/0001-mt76-allow-VHT-rate-on-2.4GHz.patch using plaintext: 
patching file mac80211.c
Hunk #1 succeeded at 191 (offset 31 lines).
Hunk #2 succeeded at 254 (offset 31 lines).
Hunk #3 succeeded at 389 (offset 31 lines).
Hunk #4 succeeded at 499 (offset 45 lines).
make[3]: *** No rule to make target '/openwrt/staging_dir/target-x86_64_musl/usr/include/mac80211-backport/backport/autoconf.h', needed by '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/mt76-2021-07-15-bbebea7d/.configured_98efdcd916b181aef82ec860dfcf9dd8'.  Stop.
```
