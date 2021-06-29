---
title: "compile.42"
date: 2021-06-29 09:35:35.000645
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
make package/feeds/packages/spice-protocol/compile -j$(nproc) || make package/feeds/packages/spice-protocol/compile V=s
```

#### Compile.txt

``` bash
+ curl -f --connect-timeout 20 --retry 5 --location --insecure https://www.spice-space.org/download/releases/spice-protocol-0.14.3.tar.xz
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100 22224  100 22224    0     0   116k      0 --:--:-- --:--:-- --:--:--  116k
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/spice-protocol-0.14.3
Build dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/spice-protocol-0.14.3/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: spice-protocol
Project version: 0.14.3
Build machine cpu family: x86_64
Build machine cpu: x86_64
Host machine cpu family: aarch64
Host machine cpu: generic
Target machine cpu family: aarch64
Target machine cpu: generic
Build targets in project: 0


ERROR: Could not detect Ninja v1.8.2 or newer

A full log can be found at /openwrt/build_dir/target-aarch64_cortex-a72_musl/spice-protocol-0.14.3/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:48: /openwrt/build_dir/target-aarch64_cortex-a72_musl/spice-protocol-0.14.3/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
