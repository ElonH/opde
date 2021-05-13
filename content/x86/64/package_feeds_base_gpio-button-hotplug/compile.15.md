---
title: "compile.15"
date: 2021-05-13 06:20:15.130569
hidden: false
draft: false
weight: -15
---

build number: `15`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/base/gpio-button-hotplug/compile -j$(nproc) || make package/feeds/base/gpio-button-hotplug/compile V=s
```

#### Compile.txt

``` bash
make[4]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/linux-5.4.117'
  HOSTCC  scripts/basic/fixdep
  HOSTCC  scripts/kconfig/conf.o
  HOSTCC  scripts/kconfig/confdata.o
  HOSTCC  scripts/kconfig/expr.o
  HOSTCC  scripts/kconfig/lexer.lex.o
  HOSTCC  scripts/kconfig/parser.tab.o
  HOSTCC  scripts/kconfig/preprocess.o
  HOSTCC  scripts/kconfig/symbol.o
  HOSTLD  scripts/kconfig/conf
scripts/kconfig/conf  --syncconfig Kconfig
can't find file Kconfig
make[6]: *** [scripts/kconfig/Makefile:73: syncconfig] Error 1
make[5]: *** [Makefile:590: syncconfig] Error 2
make[4]: *** [Makefile:696: include/config/auto.conf.cmd] Error 2
make[4]: *** [include/config/auto.conf.cmd] Deleting file 'include/config/tristate.conf'
make[4]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/linux-5.4.117'
make[3]: *** [Makefile:48: /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/gpio-button-hotplug/.built] Error 2
```
