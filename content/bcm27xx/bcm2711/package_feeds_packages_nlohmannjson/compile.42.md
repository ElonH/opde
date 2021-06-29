---
title: "compile.42"
date: 2021-06-29 09:38:24.611874
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
make package/feeds/packages/nlohmannjson/compile -j$(nproc) || make package/feeds/packages/nlohmannjson/compile V=s
```

#### Compile.txt

``` bash
+ curl -f --connect-timeout 20 --retry 5 --location --insecure https://codeload.github.com/nlohmann/json/zip/v3.9.1?/nlohmannjson-3.9.1.zip
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100 7032k    0 7032k    0     0  13.2M      0 --:--:-- --:--:-- --:--:-- 13.2M
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/json-3.9.1
Build dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/json-3.9.1/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: nlohmann_json
Project version: 3.9.1
C++ compiler for the host machine: ccache_cxx (gcc 8.4.0 "aarch64-openwrt-linux-musl-g++ (OpenWrt GCC 8.4.0 r0-af265d3) 8.4.0")
C++ linker for the host machine: ccache_cxx ld.bfd 2.34
C++ compiler for the build machine: ccache g++ (gcc 9.3.0 "g++ (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0")
C++ linker for the build machine: g++ ld.bfd 2.34
Build machine cpu family: x86_64
Build machine cpu: x86_64
Host machine cpu family: aarch64
Host machine cpu: generic
Target machine cpu family: aarch64
Target machine cpu: generic
Build targets in project: 0


ERROR: Could not detect Ninja v1.8.2 or newer

A full log can be found at /openwrt/build_dir/target-aarch64_cortex-a72_musl/json-3.9.1/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:51: /openwrt/build_dir/target-aarch64_cortex-a72_musl/json-3.9.1/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
