---
title: "compile.45"
date: 2021-09-01 09:30:10.315795
hidden: false
draft: false
weight: -45
---

build number: `45`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/mdio-netlink/compile -j$(nproc) || make package/feeds/packages/mdio-netlink/compile V=s
```

#### Compile.txt

``` bash
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/linux-5.4.143'
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/mdio-netlink-2021-07-19-65f6898f/kernel/mdio-netlink.o
  Building modules, stage 2.
  MODPOST 1 modules
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/mdio-netlink-2021-07-19-65f6898f/kernel/mdio-netlink.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/mdio-netlink-2021-07-19-65f6898f/kernel/mdio-netlink.ko
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/linux-5.4.143'
grep: /openwrt/build_dir/target-x86_64_musl/linux-x86_64/mdio-netlink-2021-07-19-65f6898f/./Module.symvers: No such file or directory
Package kmod-mdio-netlink is missing dependencies for the following libraries:
libphy.ko
make[3]: *** [Makefile:49: /openwrt/bin/targets/x86/64/packages/kmod-mdio-netlink_5.4.143+2021-07-19-65f6898f-1_x86_64.ipk] Error 1
```
