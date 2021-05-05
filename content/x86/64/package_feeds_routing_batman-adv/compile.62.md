---
title: "compile.62"
date: 2021-05-05 13:47:41.259336
hidden: false
draft: false
weight: -62
---

build number: `62`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/routing/batman-adv/compile -j$(nproc) || make package/feeds/routing/batman-adv/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/0001-Revert-batman-adv-genetlink-move-to-smaller-ops-wher.patch using plaintext: 
patching file compat-include/net/genetlink.h
patching file net/batman-adv/netlink.c

Applying ./patches/0002-Revert-batman-adv-Add-new-include-for-min-max-helper.patch using plaintext: 
patching file compat-include/linux/minmax.h
patching file net/batman-adv/bat_v.c
patching file net/batman-adv/bat_v_elp.c
patching file net/batman-adv/bat_v_ogm.c
patching file net/batman-adv/fragmentation.c
patching file net/batman-adv/hard-interface.c
patching file net/batman-adv/main.c
patching file net/batman-adv/netlink.c
patching file net/batman-adv/tp_meter.c
make[3]: *** No rule to make target '/openwrt/staging_dir/target-x86_64_musl/usr/include/mac80211-backport/backport/autoconf.h', needed by '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/batman-adv-2021.0/.configured_68b329da9893e34099c7d8ad5cb9c940'.  Stop.
```
