---
title: "compile.30"
date: 2021-06-09 21:58:55.427343
hidden: false
draft: false
weight: -30
---

build number: `30`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/base/fullconenat/compile -j$(nproc) || make package/feeds/base/fullconenat/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/000-printk.patch using plaintext: 
patching file xt_FULLCONENAT.c
Hunk #1 succeeded at 702 (offset 5 lines).
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/linux-5.4.124'
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/fullconenat-2019-10-21-0cf3b48f/xt_FULLCONENAT.o
  Building modules, stage 2.
  MODPOST 1 modules
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/fullconenat-2019-10-21-0cf3b48f/xt_FULLCONENAT.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/fullconenat-2019-10-21-0cf3b48f/xt_FULLCONENAT.ko
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/linux-5.4.124'
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fullconenat-2019-10-21-0cf3b48f'
ccache_cc -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fullconenat-2019-10-21-0cf3b48f=fullconenat-2019-10-21-0cf3b48f -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include  -fPIC -D_INIT=libipt_FULLCONENAT_init -c -o libipt_FULLCONENAT.o libipt_FULLCONENAT.c;
ccache_cc -shared -lxtables -o libipt_FULLCONENAT.so libipt_FULLCONENAT.o;
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fullconenat-2019-10-21-0cf3b48f'
Package kmod-ipt-fullconenat is missing dependencies for the following libraries:
nf_conntrack.ko
nf_nat.ko
x_tables.ko
make[3]: *** [Makefile:76: /openwrt/bin/targets/x86/64/packages/kmod-ipt-fullconenat_5.4.124+2019-10-21-0cf3b48f-1_x86_64.ipk] Error 1
```
