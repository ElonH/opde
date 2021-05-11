---
title: "compile.13"
date: 2021-05-11 22:17:22.811737
hidden: false
draft: false
weight: -13
---

build number: `13`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/base/gpio-nct5104d/compile -j$(nproc) || make package/feeds/base/gpio-nct5104d/compile V=s
```

#### Compile.txt

``` bash
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/linux-5.4.115'
scripts/kconfig/conf  --syncconfig Kconfig
can't find file Kconfig
make[6]: *** [scripts/kconfig/Makefile:73: syncconfig] Error 1
make[5]: *** [Makefile:590: syncconfig] Error 2
make[4]: *** [Makefile:696: include/config/auto.conf.cmd] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/linux-5.4.115'
make[3]: *** [Makefile:54: /openwrt/build_dir/target-x86_64_musl/linux-x86_64/gpio-nct5104d/.built] Error 2
```
