---
title: "compile.48"
date: 2021-02-22 14:40:59.076988
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
make package/feeds/base/openwrt-dnsforwarder/compile -j$(nproc) || make package/feeds/base/openwrt-dnsforwarder/compile V=s
```

#### Compile.txt

``` bash
openwrt-dnsforwarder-6.tar.xz: Download from https://github.com/holmium/dnsforwarder.git failed
openwrt-dnsforwarder-6.tar.xz: Requires sha256sum for verification
Checking out files from the git repository...
Cloning into 'openwrt-dnsforwarder-6'...
remote: Repository not found.
fatal: Authentication failed for 'https://github.com/holmium/dnsforwarder.git/'
make[3]: *** [Makefile:37: /openwrt/dl/openwrt-dnsforwarder-6.tar.xz] Error 128
```
