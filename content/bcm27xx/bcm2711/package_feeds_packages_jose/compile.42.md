---
title: "compile.42"
date: 2021-06-29 09:38:24.592537
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
make package/feeds/packages/jose/compile -j$(nproc) || make package/feeds/packages/jose/compile V=s
```

#### Compile.txt

``` bash
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/jose-11
Build dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/jose-11/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: jose
Project version: 11
C compiler for the host machine: ccache_cc (gcc 8.4.0 "aarch64-openwrt-linux-musl-gcc (OpenWrt GCC 8.4.0 r0-af265d3) 8.4.0")
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
Run-time dependency zlib found: YES 1.2.11
Run-time dependency threads found: YES
Run-time dependency jansson found: YES 2.13.1
Run-time dependency libcrypto found: YES 1.1.1k
Program a2x found: YES (/usr/bin/a2x)
Configuring jose.h using configuration
Checking if "-Wl,--version-script=..." links: YES 
Program ./jose-alg found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/jose-11/tests/./jose-alg)
Program ./jose-fmt found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/jose-11/tests/./jose-fmt)
Program ./jose-b64-enc found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/jose-11/tests/./jose-b64-enc)
Program ./jose-b64-dec found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/jose-11/tests/./jose-b64-dec)
Program ./jose-jwk-eql found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/jose-11/tests/./jose-jwk-eql)
Program ./jose-jwk-exc found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/jose-11/tests/./jose-jwk-exc)
Program ./jose-jwk-gen found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/jose-11/tests/./jose-jwk-gen)
Program ./jose-jwk-pub found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/jose-11/tests/./jose-jwk-pub)
Program ./jose-jwk-use found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/jose-11/tests/./jose-jwk-use)
Program ./jose-jwk-thp found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/jose-11/tests/./jose-jwk-thp)
Program ./jose-jws-fmt found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/jose-11/tests/./jose-jws-fmt)
Program ./jose-jws-ver found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/jose-11/tests/./jose-jws-ver)
Program ./jose-jws-sig found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/jose-11/tests/./jose-jws-sig)
Program ./jose-jwe-fmt found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/jose-11/tests/./jose-jwe-fmt)
Program ./jose-jwe-dec found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/jose-11/tests/./jose-jwe-dec)
Program ./jose-jwe-enc found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/jose-11/tests/./jose-jwe-enc)
Run-time dependency openssl found: YES 1.1.1k
Build targets in project: 28


ERROR: Could not detect Ninja v1.8.2 or newer

A full log can be found at /openwrt/build_dir/target-aarch64_cortex-a72_musl/jose-11/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:79: /openwrt/build_dir/target-aarch64_cortex-a72_musl/jose-11/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
