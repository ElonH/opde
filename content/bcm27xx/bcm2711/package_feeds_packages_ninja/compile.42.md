---
title: "compile.42"
date: 2021-06-29 09:29:13.198322
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
make package/feeds/packages/ninja/compile -j$(nproc) || make package/feeds/packages/ninja/compile V=s
```

#### Compile.txt

``` bash
warning: A compatible version of re2c (>= 0.11.3) was not found; changes to src/*.in.cc will not affect your build.
wrote build.ninja.
bash: C: command not found
install: cannot stat '/openwrt/build_dir/target-aarch64_cortex-a72_musl/ninja-1.10.2/ninja': No such file or directory
make[3]: *** [Makefile:54: /openwrt/build_dir/target-aarch64_cortex-a72_musl/ninja-1.10.2/.pkgdir/ninja.installed] Error 1
```
