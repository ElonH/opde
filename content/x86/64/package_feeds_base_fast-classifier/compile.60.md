---
title: "compile.60"
date: 2021-02-18 15:10:27.228878
hidden: false
draft: false
weight: -60
---

build number: `60`

path: `package/feeds/base/fast-classifier/compile`


``` bash
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/linux-5.4.98'
  Building modules, stage 2.
  MODPOST 1 modules
ERROR: "sfe_ipv6_register_sync_rule_callback" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
ERROR: "sfe_ipv4_register_sync_rule_callback" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
ERROR: "athrs_fast_nat_recv" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
ERROR: "sfe_ipv6_update_rule" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
ERROR: "nf_ct_tcp_no_window_check" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
ERROR: "sfe_ipv4_create_rule" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
ERROR: "sfe_ipv4_update_rule" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
ERROR: "sfe_ipv6_create_rule" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
ERROR: "sfe_ipv6_mark_rule" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
ERROR: "sfe_ipv6_destroy_rule" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
ERROR: "sfe_ipv4_mark_rule" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
ERROR: "sfe_ipv4_destroy_rule" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
ERROR: "sfe_ipv4_destroy_all_rules_for_dev" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
ERROR: "sfe_ipv6_destroy_all_rules_for_dev" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
ERROR: "sfe_ipv6_recv" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
ERROR: "sfe_ipv4_recv" [/openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/fast-classifier.ko] undefined!
make[5]: *** [scripts/Makefile.modpost:94: __modpost] Error 1
make[4]: *** [Makefile:1639: modules] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/linux-5.4.98'
make[3]: *** [Makefile:72: /openwrt/build_dir/target-x86_64_musl/linux-x86_64/fast-classifier/.built] Error 2
```
