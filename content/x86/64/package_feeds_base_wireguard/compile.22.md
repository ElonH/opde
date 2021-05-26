---
title: "compile.22"
date: 2021-05-26 12:45:38.532812
hidden: false
draft: false
weight: -22
---

build number: `22`

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
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/linux-5.4.121'
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/wireguard-linux-compat-1.0.20210424/src/main.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/wireguard-linux-compat-1.0.20210424/src/noise.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/wireguard-linux-compat-1.0.20210424/src/device.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/wireguard-linux-compat-1.0.20210424/src/peer.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/wireguard-linux-compat-1.0.20210424/src/timers.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/wireguard-linux-compat-1.0.20210424/src/queueing.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/wireguard-linux-compat-1.0.20210424/src/send.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/wireguard-linux-compat-1.0.20210424/src/receive.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/wireguard-linux-compat-1.0.20210424/src/socket.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/wireguard-linux-compat-1.0.20210424/src/peerlookup.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/wireguard-linux-compat-1.0.20210424/src/allowedips.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/wireguard-linux-compat-1.0.20210424/src/ratelimiter.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/wireguard-linux-compat-1.0.20210424/src/cookie.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/wireguard-linux-compat-1.0.20210424/src/netlink.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/wireguard-linux-compat-1.0.20210424/src/crypto/zinc/chacha20/chacha20.o
  PERLASM /openwrt/build_dir/target-x86_64_musl/linux-x86_64/wireguard-linux-compat-1.0.20210424/src/crypto/zinc/chacha20/chacha20-x86_64.S
  AS [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/wireguard-linux-compat-1.0.20210424/src/crypto/zinc/chacha20/chacha20-x86_64.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/wireguard-linux-compat-1.0.20210424/src/crypto/zinc/poly1305/poly1305.o
  PERLASM /openwrt/build_dir/target-x86_64_musl/linux-x86_64/wireguard-linux-compat-1.0.20210424/src/crypto/zinc/poly1305/poly1305-x86_64.S
  AS [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/wireguard-linux-compat-1.0.20210424/src/crypto/zinc/poly1305/poly1305-x86_64.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/wireguard-linux-compat-1.0.20210424/src/crypto/zinc/chacha20poly1305.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/wireguard-linux-compat-1.0.20210424/src/crypto/zinc/blake2s/blake2s.o
  AS [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/wireguard-linux-compat-1.0.20210424/src/crypto/zinc/blake2s/blake2s-x86_64.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/wireguard-linux-compat-1.0.20210424/src/crypto/zinc/curve25519/curve25519.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/wireguard-linux-compat-1.0.20210424/src/wireguard.o
  Building modules, stage 2.
  MODPOST 1 modules
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/wireguard-linux-compat-1.0.20210424/src/wireguard.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/wireguard-linux-compat-1.0.20210424/src/wireguard.ko
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/linux-5.4.121'
Package kmod-wireguard is missing dependencies for the following libraries:
ip6_udp_tunnel.ko
udp_tunnel.ko
make[3]: *** [Makefile:98: /openwrt/bin/targets/x86/64/packages/kmod-wireguard_5.4.121+1.0.20210424-1_x86_64.ipk] Error 1
```
