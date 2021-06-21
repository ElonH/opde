---
title: "compile.38"
date: 2021-06-21 06:07:20.316643
hidden: false
draft: false
weight: -38
---

build number: `38`

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
cp: cannot stat '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/ffmpeg-custom/ffmpeg-4.3.2/ipkg-install/usr/bin/ffmpeg': No such file or directory
make[3]: *** [Makefile:755: /openwrt/bin/packages/arm_cortex-a7_neon-vfpv4/packages/ffmpeg-custom_4.3.2-1_arm_cortex-a7_neon-vfpv4.ipk] Error 1
```
