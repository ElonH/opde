---
title: "compile.42"
date: 2021-06-29 09:26:41.846193
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
make package/feeds/packages/knot-resolver/compile -j$(nproc) || make package/feeds/packages/knot-resolver/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-fix-lmdb.patch using plaintext: 
patching file meson.build

Applying ./patches/030-fix-policy-hack.patch using plaintext: 
patching file modules/policy/policy.lua
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/knot-resolver-5.3.2
Build dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/knot-resolver-5.3.2/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: knot-resolver
Project version: 5.3.2
C compiler for the host machine: ccache_cc (gcc 8.4.0 "aarch64-openwrt-linux-musl-gcc (OpenWrt GCC 8.4.0 r0-af265d3) 8.4.0")
C linker for the host machine: ccache_cc ld.bfd 2.34
C++ compiler for the host machine: ccache_cxx (gcc 8.4.0 "aarch64-openwrt-linux-musl-g++ (OpenWrt GCC 8.4.0 r0-af265d3) 8.4.0")
C++ linker for the host machine: ccache_cxx ld.bfd 2.34
C compiler for the build machine: ccache gcc (gcc 9.3.0 "gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0")
C linker for the build machine: gcc ld.bfd 2.34
C++ compiler for the build machine: ccache g++ (gcc 9.3.0 "g++ (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0")
C++ linker for the build machine: g++ ld.bfd 2.34
Build machine cpu family: x86_64
Build machine cpu: x86_64
Host machine cpu family: aarch64
Host machine cpu: generic
Target machine cpu family: aarch64
Target machine cpu: generic
Message: --- required dependencies ---
Found pkg-config: /openwrt/staging_dir/host/bin/pkg-config (1.7.3)
Run-time dependency libknot found: YES 3.0.7
Run-time dependency libdnssec found: YES 3.0.7
Run-time dependency libzscanner found: YES 3.0.7
Run-time dependency libuv found: YES 1.41.0
Library lmdb found: YES
Run-time dependency gnutls found: YES 3.7.2
Run-time dependency luajit found: YES 2.1.0-beta3
Message: ------------------------------
Message: --- optional dependencies ---
Run-time dependency libnghttp2 found: YES 1.43.0
Run-time dependency openssl found: YES 1.1.1k
Checking for function "asprintf" : YES 
Checking for function "sendmmsg" : YES 
Has header "libknot/xdp/xdp.h" : NO 
Found CMake: NO
Run-time dependency libsystemd found: NO (tried pkgconfig and cmake)
Message: ---------------------------
Configuring kresconfig.h using configuration
Configuring trust_anchors.lua using configuration
Configuring sandbox.lua using configuration
Configuring distro-preconfig.lua using configuration
Program ./kres-gen.sh found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/knot-resolver-5.3.2/daemon/lua/./kres-gen.sh)
Configuring http.lua using configuration
Configuring upgrade-4-to-5.lua using configuration
Configuring kresd.8 using configuration
Program ../scripts/make-doc.sh found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/knot-resolver-5.3.2/doc/../scripts/make-doc.sh)
Message: --- lint dependencies ---
Program clang-tidy found: NO
Program luacheck found: NO
Program flake8 found: NO
Program scripts/run-pylint.sh found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/knot-resolver-5.3.2/scripts/run-pylint.sh)
Message: -------------------------
Message: 

======================= SUMMARY =======================

  paths
    prefix:             /usr
    lib_dir:            /usr/lib/knot-resolver
    sbin_dir:           /usr/sbin
    etc_dir:            /etc/knot-resolver
    root.hints:         /etc/knot-resolver/root.hints

  trust_anchors
    keyfile_default:    /etc/knot-resolver/root.keys
    managed_ta:         enabled
    install_root_keys:  disabled

  systemd:
    files:              disabled
    work_dir:           /var/lib/knot-resolver
    cache_dir:          /var/cache/knot-resolver

  optional components
    client:             disabled
    utils:              disabled
    dnstap:             disabled
    unit_tests:         disabled
    config_tests:       disabled
    extra_tests:        disabled

  additional
    user:               knot-resolver
    group:              knot-resolver
    install_kresd_conf: disabled
    sendmmsg:           enabled
    XDP (in libknot):   disabled
    openssl debug:      present
    capng:              disabled
    doh2:               enabled

=======================================================


Build targets in project: 15


ERROR: Could not detect Ninja v1.8.2 or newer

A full log can be found at /openwrt/build_dir/target-aarch64_cortex-a72_musl/knot-resolver-5.3.2/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:97: /openwrt/build_dir/target-aarch64_cortex-a72_musl/knot-resolver-5.3.2/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
