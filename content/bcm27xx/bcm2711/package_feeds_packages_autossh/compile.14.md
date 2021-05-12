---
title: "compile.14"
date: 2021-05-12 23:09:15.520710
hidden: false
draft: false
weight: -14
---

build number: `14`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/autossh/compile -j$(nproc) || make package/feeds/packages/autossh/compile V=s
```

#### Compile.txt

``` bash
configure: loading site script /openwrt/include/site/aarch64
checking for aarch64-openwrt-linux-gcc... ccache_cc
checking for C compiler default output file name... a.out
checking whether the C compiler works... yes
checking whether we are cross compiling... yes
checking for suffix of executables... 
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ANSI C... none needed
checking for ssh... no
configure: error: ssh program not found! Modify PATH, or use --with-ssh.
make[3]: *** [Makefile:56: /openwrt/build_dir/target-aarch64_cortex-a72_musl/autossh-1.4g/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
