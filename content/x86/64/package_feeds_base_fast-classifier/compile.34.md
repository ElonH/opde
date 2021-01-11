---
title: "compile.34"
date: 2021-01-11 00:12:33.000069
hidden: false
draft: false
weight: -34
---

build number: `34`

path: `package/feeds/base/fast-classifier/compile`


``` bash
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/linux-4.19.166'
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.o
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.c: In function 'fast_classifier_init':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.c:1888:1: warning: label 'exit4' defined but not used [-Wunused-label]
 exit4:
 ^~~~~
  Building modules, stage 2.
  MODPOST 1 modules
WARNING: "sfe_ipv6_register_sync_rule_callback" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
WARNING: "sfe_ipv4_register_sync_rule_callback" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
WARNING: "athrs_fast_nat_recv" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
WARNING: "sfe_ipv6_update_rule" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
WARNING: "nf_ct_tcp_no_window_check" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
WARNING: "sfe_ipv4_create_rule" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
WARNING: "sfe_ipv4_update_rule" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
WARNING: "sfe_ipv6_create_rule" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
WARNING: "sfe_ipv6_mark_rule" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
WARNING: "sfe_ipv6_destroy_rule" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
WARNING: "sfe_ipv4_mark_rule" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
WARNING: "sfe_ipv4_destroy_rule" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
WARNING: "sfe_ipv4_destroy_all_rules_for_dev" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
WARNING: "sfe_ipv6_destroy_all_rules_for_dev" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
WARNING: "sfe_ipv6_recv" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
WARNING: "sfe_ipv4_recv" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
  CC      /openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/linux-4.19.166'
Package kmod-fast-classifier is missing dependencies for the following libraries:
nf_conntrack.ko
make[3]: *** [Makefile:99: /openwrt/bin/targets/x86/64/packages/kmod-fast-classifier_4.19.166-1_x86_64.ipk] Error 1
```
