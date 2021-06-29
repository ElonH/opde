---
title: "compile.42"
date: 2021-06-29 09:38:24.626592
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
make package/feeds/packages/gkrellmd/compile -j$(nproc) || make package/feeds/packages/gkrellmd/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/100-conf.patch using plaintext: 
patching file server/gkrellmd.conf
make[4]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gkrellm-2.3.11/server'
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package 'gmodule-2.0', required by 'virtual:world', not found
Package 'gthread-2.0', required by 'virtual:world', not found
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package 'gmodule-2.0', required by 'virtual:world', not found
Package 'gthread-2.0', required by 'virtual:world', not found
/openwrt/staging_dir/host/bin/pkg-config --atleast-version=2.32 glib-2.0
make[4]: *** [Makefile:216: check_env] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/gkrellm-2.3.11/server'
make[3]: *** [Makefile:64: /openwrt/build_dir/target-aarch64_cortex-a72_musl/gkrellm-2.3.11/.built] Error 2
```
