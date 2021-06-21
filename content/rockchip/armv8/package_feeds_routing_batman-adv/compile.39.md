---
title: "compile.39"
date: 2021-06-21 19:18:00.094722
hidden: false
draft: false
weight: -39
---

build number: `39`

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

Applying ./patches/0003-batman-adv-Fix-build-of-multicast-code-against-Linux.patch using plaintext: 
patching file net/batman-adv/multicast.c

Applying ./patches/0004-batman-adv-Always-send-iface-index-name-in-genlmsg.patch using plaintext: 
patching file net/batman-adv/bat_iv_ogm.c
patching file net/batman-adv/bat_v.c
patching file net/batman-adv/netlink.c
make[3]: *** No rule to make target '/openwrt/staging_dir/target-aarch64_generic_musl/usr/include/mac80211-backport/backport/autoconf.h', needed by '/openwrt/build_dir/target-aarch64_generic_musl/linux-rockchip_armv8/batman-adv-2021.1/.configured_68b329da9893e34099c7d8ad5cb9c940'.  Stop.
```
