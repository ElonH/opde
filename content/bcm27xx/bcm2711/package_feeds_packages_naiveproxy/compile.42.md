---
title: "compile.42"
date: 2021-06-29 09:38:57.203149
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
make package/feeds/packages/naiveproxy/compile -j$(nproc) || make package/feeds/packages/naiveproxy/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-Remove-concurrency-limit.patch using plaintext: 
patching file src/net/tools/naive/naive_proxy.cc
patching file src/net/tools/naive/naive_proxy_bin.cc
Hunk #1 succeeded at 296 (offset -3 lines).
Archive:  /openwrt/dl/gn-git_revision-dba01723a441c358d843a575cb7720d54ddcdf92.zip
  inflating: gn/out/gn               
  inflating: gn/out/.cipdpkg/manifest.json  
Done. Made 366 targets from 133 files in 548ms
bash: C: command not found
install: cannot stat '/openwrt/build_dir/target-aarch64_cortex-a72_musl/naiveproxy-91.0.4472.77-1/src/out/Release/naive': No such file or directory
make[3]: *** [Makefile:134: /openwrt/build_dir/target-aarch64_cortex-a72_musl/naiveproxy-91.0.4472.77-1/.pkgdir/naiveproxy.installed] Error 1
```
