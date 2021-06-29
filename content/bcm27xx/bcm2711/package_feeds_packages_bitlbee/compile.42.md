---
title: "compile.42"
date: 2021-06-29 09:38:24.623455
hidden: false
draft: false
weight: -42
---

build number: `42`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/bitlbee/compile -j$(nproc) || make package/feeds/packages/bitlbee/compile V=s
```

#### Compile.txt

``` bash
BitlBee configure

Cannot find glib2 development libraries, aborting. (Install libglib2-dev?)
make[3]: *** [Makefile:73: /openwrt/build_dir/target-aarch64_cortex-a72_musl/bitlbee-3.6/.configured_a17fb5ef857664f03cd0ce37cc5ea591] Error 1
```
