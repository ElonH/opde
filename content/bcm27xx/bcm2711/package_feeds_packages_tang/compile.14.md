---
title: "compile.14"
date: 2021-05-12 23:07:35.002742
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
make package/feeds/packages/tang/compile -j$(nproc) || make package/feeds/packages/tang/compile V=s
```

#### Compile.txt

``` bash
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/tang-8
Build dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/tang-8/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: tang
Project version: 8
C compiler for the host machine: ccache_cc (gcc 8.4.0 "aarch64-openwrt-linux-musl-gcc (OpenWrt GCC 8.4.0 r0-93440ea) 8.4.0")
C linker for the host machine: ccache_cc ld.bfd 2.34
C compiler for the build machine: ccache gcc (gcc 9.3.0 "gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0")
C linker for the build machine: gcc ld.bfd 2.34
Build machine cpu family: x86_64
Build machine cpu: x86_64
Host machine cpu family: aarch64
Host machine cpu: generic
Target machine cpu family: aarch64
Target machine cpu: generic
Found pkg-config: /openwrt/staging_dir/host/bin/pkg-config (1.7.3)
Run-time dependency jose found: YES 10
Program a2x found: YES (/usr/bin/a2x)
Has header "http_parser.h" : YES 
Library http_parser found: YES
Configuring tangd@.service using configuration
Configuring test-keys.c using configuration
Program systemd-socket-activate systemd-activate found: NO
Build targets in project: 4

Found ninja-1.10.2 at /openwrt/staging_dir/hostpkg/bin/ninja
ninja: Entering directory `/openwrt/build_dir/target-aarch64_cortex-a72_musl/tang-8/openwrt-build'
[1/9] Compiling C object src/tangd.p/http.c.o
[2/9] Compiling C object src/tangd.p/tangd.c.o
[3/9] Compiling C object src/tangd.p/keys.c.o
[4/9] Linking target src/tangd
[5/9] Compiling C object tests/test-keys.p/test-util.c.o
[6/9] Compiling C object tests/test-keys.p/meson-generated_.._test-keys.c.o
[7/9] Linking target tests/test-keys
[8/9] Generating tang-show-keys.1 with a custom command
FAILED: tang-show-keys.1 
/usr/bin/a2x -f manpage -D /openwrt/build_dir/target-aarch64_cortex-a72_musl/tang-8/openwrt-build /openwrt/build_dir/target-aarch64_cortex-a72_musl/tang-8/doc/tang-show-keys.1.adoc
a2x: ERROR: "xmllint" --nonet --noout --valid "/openwrt/build_dir/target-aarch64_cortex-a72_musl/tang-8/openwrt-build/tang-show-keys.1.xml" returned non-zero exit status 4

[9/9] Generating tang.8 with a custom command
FAILED: tang.8 
/usr/bin/a2x -f manpage -D /openwrt/build_dir/target-aarch64_cortex-a72_musl/tang-8/openwrt-build /openwrt/build_dir/target-aarch64_cortex-a72_musl/tang-8/doc/tang.8.adoc
a2x: ERROR: "xmllint" --nonet --noout --valid "/openwrt/build_dir/target-aarch64_cortex-a72_musl/tang-8/openwrt-build/tang.8.xml" returned non-zero exit status 4

ninja: build stopped: subcommand failed.
make[3]: *** [Makefile:73: /openwrt/build_dir/target-aarch64_cortex-a72_musl/tang-8/.built] Error 1
```
