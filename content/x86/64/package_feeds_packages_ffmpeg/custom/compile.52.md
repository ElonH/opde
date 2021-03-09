---
title: "compile.52"
date: 2021-03-09 13:47:09.083709
hidden: false
draft: false
weight: -52
---

build number: `52`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/ffmpeg/compile -j$(nproc) || make package/feeds/packages/ffmpeg/compile V=s
```

#### Compile.txt

``` bash
cp: cannot stat '/openwrt/build_dir/target-x86_64_musl/ffmpeg-custom/ffmpeg-4.3.2/ipkg-install/usr/bin/ffmpeg': No such file or directory
make[3]: *** [Makefile:753: /openwrt/bin/packages/x86_64/packages/ffmpeg-custom_4.3.2-1_x86_64.ipk] Error 1
```
