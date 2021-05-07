---
title: "compile.10"
date: 2021-05-07 12:47:46.907701
hidden: false
draft: false
weight: -10
---

build number: `10`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/base/shortcut-fe/compile -j$(nproc) || make package/feeds/base/shortcut-fe/compile V=s
```

#### Compile.txt

``` bash
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/linux-5.4.115'
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/shortcut-fe/sfe_ipv4.o
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/shortcut-fe/sfe_ipv4.c: In function 'sfe_ipv4_recv_udp':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/shortcut-fe/sfe_ipv4.c:1478:5: error: 'struct sk_buff' has no member named 'fast_forwarded'
  skb->fast_forwarded = 1;
     ^~
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/shortcut-fe/sfe_ipv4.c: In function 'sfe_ipv4_recv_tcp':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/shortcut-fe/sfe_ipv4.c:2052:5: error: 'struct sk_buff' has no member named 'fast_forwarded'
  skb->fast_forwarded = 1;
     ^~
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/shortcut-fe/sfe_ipv4.c: In function 'sfe_ipv4_periodic_sync':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/shortcut-fe/sfe_ipv4.c:2868:46: error: 'struct timer_list' has no member named 'cust_data'
  struct sfe_ipv4 *si = (struct sfe_ipv4 *)arg->cust_data;
                                              ^~
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/shortcut-fe/sfe_ipv4.c: In function 'sfe_ipv4_init':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/shortcut-fe/sfe_ipv4.c:3552:11: error: 'struct timer_list' has no member named 'cust_data'
  si->timer.cust_data = (unsigned long)si;
           ^
make[5]: *** [scripts/Makefile.build:262: /openwrt/build_dir/target-x86_64_musl/linux-x86_64/shortcut-fe/sfe_ipv4.o] Error 1
make[4]: *** [Makefile:1734: /openwrt/build_dir/target-x86_64_musl/linux-x86_64/shortcut-fe] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/linux-5.4.115'
make[3]: *** [Makefile:84: /openwrt/build_dir/target-x86_64_musl/linux-x86_64/shortcut-fe/.built] Error 2
```
