---
title: "compile.14"
date: 2021-05-12 23:06:11.752157
hidden: false
draft: false
weight: -14
---

build number: `14`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/base/wireguard/compile -j$(nproc) || make package/feeds/base/wireguard/compile V=s
```

#### Compile.txt

``` bash
make[4]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/linux-5.4.117'
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/wireguard-linux-compat-1.0.20210219/src/main.o
In file included from <command-line>:
./../wireguard-linux-compat-1.0.20210219/src/compat/compat.h:1059:22: error: static declaration of 'ip_tunnel_parse_protocol' follows non-static declaration
 static inline __be16 ip_tunnel_parse_protocol(const struct sk_buff *skb)
                      ^~~~~~~~~~~~~~~~~~~~~~~~
In file included from ./include/net/gre.h:6,
                 from ./include/linux/netfilter/nf_conntrack_proto_gre.h:5,
                 from ./include/net/netfilter/nf_conntrack.h:23,
                 from ./../wireguard-linux-compat-1.0.20210219/src/compat/compat.h:941,
                 from <command-line>:
./include/net/ip_tunnels.h:293:8: note: previous declaration of 'ip_tunnel_parse_protocol' was here
 __be16 ip_tunnel_parse_protocol(const struct sk_buff *skb);
        ^~~~~~~~~~~~~~~~~~~~~~~~
In file included from <command-line>:
./../wireguard-linux-compat-1.0.20210219/src/compat/compat.h:1072:32: error: static declaration of 'ip_tunnel_header_ops' follows non-static declaration
 static const struct header_ops ip_tunnel_header_ops = { .parse_protocol = ip_tunnel_parse_protocol };
                                ^~~~~~~~~~~~~~~~~~~~
In file included from ./include/net/gre.h:6,
                 from ./include/linux/netfilter/nf_conntrack_proto_gre.h:5,
                 from ./include/net/netfilter/nf_conntrack.h:23,
                 from ./../wireguard-linux-compat-1.0.20210219/src/compat/compat.h:941,
                 from <command-line>:
./include/net/ip_tunnels.h:292:32: note: previous declaration of 'ip_tunnel_header_ops' was here
 extern const struct header_ops ip_tunnel_header_ops;
                                ^~~~~~~~~~~~~~~~~~~~
make[5]: *** [scripts/Makefile.build:262: /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/wireguard-linux-compat-1.0.20210219/src/main.o] Error 1
make[4]: *** [Makefile:1737: /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/wireguard-linux-compat-1.0.20210219/src] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/linux-5.4.117'
make[3]: *** [Makefile:90: /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/wireguard-linux-compat-1.0.20210219/.built] Error 2
```
