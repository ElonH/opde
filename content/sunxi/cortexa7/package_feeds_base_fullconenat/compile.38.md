---
title: "compile.38"
date: 2021-06-21 06:15:36.327017
hidden: false
draft: false
weight: -38
---

build number: `38`

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
make[4]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/linux-5.4.124'
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/fullconenat-2019-10-21-0cf3b48f/xt_FULLCONENAT.o
  Building modules, stage 2.
  MODPOST 1 modules
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/fullconenat-2019-10-21-0cf3b48f/xt_FULLCONENAT.mod.o
  LD [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/fullconenat-2019-10-21-0cf3b48f/xt_FULLCONENAT.ko
make[4]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/linux-5.4.124'
make[4]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/fullconenat-2019-10-21-0cf3b48f'
ccache_cc -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -mfloat-abi=hard -fmacro-prefix-map=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/fullconenat-2019-10-21-0cf3b48f=fullconenat-2019-10-21-0cf3b48f -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/usr/include -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include/fortify -I/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/include  -fPIC -D_INIT=libipt_FULLCONENAT_init -c -o libipt_FULLCONENAT.o libipt_FULLCONENAT.c;
ccache_cc -shared -lxtables -o libipt_FULLCONENAT.so libipt_FULLCONENAT.o;
make[4]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/fullconenat-2019-10-21-0cf3b48f'
Package kmod-ipt-fullconenat is missing dependencies for the following libraries:
nf_conntrack.ko
nf_nat.ko
x_tables.ko
make[3]: *** [Makefile:76: /openwrt/bin/targets/sunxi/cortexa7/packages/kmod-ipt-fullconenat_5.4.124+2019-10-21-0cf3b48f-1_arm_cortex-a7_neon-vfpv4.ipk] Error 1
```
