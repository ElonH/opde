---
title: "compile.42"
date: 2021-06-29 09:27:20.670629
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
make package/feeds/packages/p11-kit/compile -j$(nproc) || make package/feeds/packages/p11-kit/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-stdint.patch using plaintext: 
patching file p11-kit/lists.c
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/p11-kit-0.23.22
Build dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/p11-kit-0.23.22/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: p11-kit
Project version: 0.23.22
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
Checking for size of "unsigned long" : 8
Run-time dependency threads found: YES
Checking for function "pthread_create" with dependency threads: YES 
Checking for function "nanosleep" : YES 
Checking for function "dlopen" : YES 
Library nsl found: NO
Has header "locale.h" : YES 
Checking for type "locale_t" : YES 
Checking for function "newlocale" : YES 
Checking for function "strerror_l" : YES 
Has header "sys/resource.h" : YES 
Has header "ucred.h" : NO 
Checking for function "fdwalk" : NO 
Checking for function "getauxval" : YES 
Checking for function "getexecname" : NO 
Checking for function "getpeereid" : NO 
Checking for function "getpeerucred" : NO 
Checking for function "getprogname" : NO 
Checking for function "getresuid" : YES 
Checking for function "issetugid" : YES 
Checking for function "mkdtemp" : YES 
Checking for function "mkstemp" : YES 
Checking for function "secure_getenv" : YES 
Checking for function "strndup" : YES 
Checking whether type "struct dirent" has member "d_type" : YES 
Checking if "thread-local storage class" compiles: YES 
Checking for function "gmtime_r" : YES 
Checking if "program_invocation_short_name_test_code" links: YES 
Checking if "__libc_enable_secure" links: NO 
Checking if "vsock_test" compiles: YES 
Checking for type "sighandler_t" : NO 
Checking for type "sig_t" : NO 
Checking for type "__sighandler_t" : NO 
Checking for type "sighandler_t" : NO 
Checking for type "sig_t" : YES 
Checking for type "__sighandler_t" : NO 
Has header "stdbool.h" : YES 
Checking for function "asprintf" : YES 
Checking for function "basename" : YES 
Checking for function "memdup" : NO 
Checking for function "reallocarray" : NO 
Checking for function "secure_getenv" : YES (cached)
Checking for function "setenv" : YES 
Checking for function "strerror_r" : YES 
Checking for function "strnstr" : NO 
Checking for function "vasprintf" : YES 
Header <errno.h> has symbol "program_invocation_short_name" : YES 
Header <stdio.h> has symbol "asprintf" : YES 
Header <stdio.h> has symbol "vasprintf" : YES 
Header <stdlib.h> has symbol "reallocarray" : NO 
Dependency libffi skipped: feature libffi disabled
Dependency libtasn1 skipped: feature trust_module disabled
Dependency libsystemd skipped: feature systemd disabled
Dependency systemd skipped: feature systemd disabled
Configuring config.h using configuration
Compiler for C supports link arguments -Wl,--version-script,/openwrt/build_dir/target-aarch64_cortex-a72_musl/p11-kit-0.23.22/p11-kit/libp11-kit.map: YES 
Program meson_post_install.sh found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/p11-kit-0.23.22/p11-kit/meson_post_install.sh)
Compiler for C supports link arguments -Wl,--version-script,/openwrt/build_dir/target-aarch64_cortex-a72_musl/p11-kit-0.23.22/p11-kit/p11-module.map: YES 
Program gen-pkcs11-gnu.sh found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/p11-kit-0.23.22/p11-kit/gen-pkcs11-gnu.sh)
Program test-messages.sh found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/p11-kit-0.23.22/p11-kit/test-messages.sh)
Program test-server.sh found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/p11-kit-0.23.22/p11-kit/test-server.sh)
Configuring pkcs11.conf.example using configuration
Found pkg-config: /openwrt/staging_dir/host/bin/pkg-config (1.7.3)
Found CMake: NO
Run-time dependency bash-completion found: NO (tried pkgconfig and cmake)
../../../../build_dir/target-aarch64_cortex-a72_musl/p11-kit-0.23.22/bash-completion/meson.build:7: WARNING: Will not install bash completion due to missing dependencies!
Build targets in project: 67


ERROR: Could not detect Ninja v1.8.2 or newer

A full log can be found at /openwrt/build_dir/target-aarch64_cortex-a72_musl/p11-kit-0.23.22/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:77: /openwrt/build_dir/target-aarch64_cortex-a72_musl/p11-kit-0.23.22/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
