---
title: "compile.42"
date: 2021-06-29 09:31:48.748148
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
make package/feeds/packages/ffmpeg/compile -j$(nproc) || make package/feeds/packages/ffmpeg/compile V=s
```

#### Compile.txt

``` bash
cp: cannot stat '/openwrt/build_dir/target-aarch64_cortex-a72_musl/ffmpeg-custom/ffmpeg-4.3.2/ipkg-install/usr/bin/ffmpeg': No such file or directory
make[3]: *** [Makefile:755: /openwrt/bin/packages/aarch64_cortex-a72/packages/ffmpeg-custom_4.3.2-1_aarch64_cortex-a72.ipk] Error 1
```