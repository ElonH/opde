---
title: "compile.23"
date: 2021-05-26 23:59:14.964076
hidden: false
draft: false
weight: -23
---

build number: `23`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/base/mac80211/compile -j$(nproc) || make package/feeds/base/mac80211/compile V=s
```

#### Compile.txt

``` bash
broadcom.mk:398: warning: overriding recipe for target '/openwrt/dl/broadcom-wl-5.100.138.tar.bz2'
broadcom.mk:98: warning: ignoring old recipe for target '/openwrt/dl/broadcom-wl-5.100.138.tar.bz2'

Applying ./patches/build/000-fix_kconfig.patch using plaintext: 
patching file kconf/Makefile

Applying ./patches/build/001-fix_build.patch using plaintext: 
patching file Makefile
patching file Makefile.real

Applying ./patches/build/002-change_allconfig.patch using plaintext: 
patching file kconf/conf.c
patching file kconf/confdata.c

Applying ./patches/build/003-remove_bogus_modparams.patch using plaintext: 
patching file compat/main.c

Applying ./patches/build/004-kconfig_backport_fix.patch using plaintext: 
patching file backport-include/linux/kconfig.h

Applying ./patches/build/010-disable_rfkill.patch using plaintext: 
patching file backport-include/linux/rfkill.h

Applying ./patches/build/012-kernel_build_check.patch using plaintext: 
patching file Makefile

Applying ./patches/build/015-ipw200-mtu.patch using plaintext: 
patching file drivers/net/wireless/intel/ipw2x00/ipw2200.c

Applying ./patches/build/050-lib80211_option.patch using plaintext: 
patching file net/wireless/Kconfig

Applying ./patches/build/060-no_local_ssb_bcma.patch using plaintext: 
patching file local-symbols
patching file drivers/net/wireless/broadcom/b43/Kconfig
patching file drivers/net/wireless/broadcom/b43/main.c
patching file drivers/net/wireless/broadcom/b43legacy/Kconfig
patching file drivers/net/wireless/broadcom/b43legacy/main.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmsmac/led.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmsmac/Makefile
patching file drivers/net/wireless/broadcom/brcm80211/Kconfig
patching file Kconfig.local
patching file Kconfig.sources
patching file Makefile.kernel

Applying ./patches/subsys/100-remove-cryptoapi-dependencies.patch using plaintext: 
patching file net/mac80211/Makefile
patching file net/mac80211/aead_api.c
patching file net/mac80211/aead_api.h
patching file net/mac80211/aes_ccm.h
patching file net/mac80211/aes_gcm.c
patching file net/mac80211/aes_gcm.h
patching file net/mac80211/wpa.c
patching file net/mac80211/aes_ccm.c
patching file net/mac80211/Kconfig
patching file net/mac80211/aes_gmac.h
patching file net/mac80211/key.h

Applying ./patches/subsys/110-mac80211_keep_keys_on_stop_ap.patch using plaintext: 
patching file net/mac80211/cfg.c

Applying ./patches/subsys/120-cfg80211_allow_perm_addr_change.patch using plaintext: 
patching file net/wireless/sysfs.c

Applying ./patches/subsys/130-disable-fils.patch using plaintext: 
patching file net/mac80211/fils_aead.h
patching file net/mac80211/fils_aead.c
patching file net/mac80211/main.c

Applying ./patches/subsys/131-Revert-mac80211-aes-cmac-switch-to-shash-CMAC-driver.patch using plaintext: 
patching file net/mac80211/aes_cmac.c
patching file net/mac80211/aes_cmac.h
patching file net/mac80211/key.h

Applying ./patches/subsys/132-mac80211-remove-cmac-dependency.patch using plaintext: 
patching file net/mac80211/Kconfig

Applying ./patches/subsys/150-disable_addr_notifier.patch using plaintext: 
patching file net/mac80211/main.c

Applying ./patches/subsys/210-ap_scan.patch using plaintext: 
patching file net/mac80211/cfg.c

Applying ./patches/subsys/300-cfg80211-support-immediate-reconnect-request-hint.patch using plaintext: 
patching file include/net/cfg80211.h
patching file include/uapi/linux/nl80211.h
patching file net/mac80211/mlme.c
patching file net/wireless/mlme.c
patching file net/wireless/nl80211.c
patching file net/wireless/nl80211.h
patching file net/wireless/trace.h

Applying ./patches/subsys/301-mac80211-support-driver-based-disconnect-with-reconn.patch using plaintext: 
patching file include/net/mac80211.h
patching file net/mac80211/ieee80211_i.h
patching file net/mac80211/mlme.c
patching file net/mac80211/trace.h

Applying ./patches/subsys/304-mac80211-sta-randomize-BA-session-dialog-token-alloc.patch using plaintext: 
patching file net/mac80211/sta_info.c

Applying ./patches/subsys/310-net-fq_impl-bulk-free-packets-from-a-flow-on-overmem.patch using plaintext: 
patching file include/net/fq_impl.h

Applying ./patches/subsys/311-net-fq_impl-drop-get_default_func-move-default-flow-.patch using plaintext: 
patching file include/net/fq.h
patching file include/net/fq_impl.h
patching file net/mac80211/ieee80211_i.h
patching file net/mac80211/tx.c

Applying ./patches/subsys/312-net-fq_impl-do-not-maintain-a-backlog-sorted-list-of.patch using plaintext: 
patching file include/net/fq.h
patching file include/net/fq_impl.h
patching file net/mac80211/tx.c

Applying ./patches/subsys/315-mac80211-add-rx-decapsulation-offload-support.patch using plaintext: 
patching file include/net/mac80211.h
patching file net/mac80211/debugfs.c
patching file net/mac80211/debugfs_sta.c
patching file net/mac80211/driver-ops.h
patching file net/mac80211/iface.c
patching file net/mac80211/rx.c
patching file net/mac80211/sta_info.h
patching file net/mac80211/trace.h

Applying ./patches/subsys/337-mac80211-minstrel_ht-clean-up-CCK-code.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c
patching file net/mac80211/rc80211_minstrel_ht.h

Applying ./patches/subsys/338-mac80211-minstrel_ht-add-support-for-OFDM-rates-on-n.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel.h
patching file net/mac80211/rc80211_minstrel_ht.c
patching file net/mac80211/rc80211_minstrel_ht.h
patching file net/mac80211/rc80211_minstrel_ht_debugfs.c

Applying ./patches/subsys/339-mac80211-remove-legacy-minstrel-rate-control.patch using plaintext: 
patching file net/mac80211/Makefile
patching file net/mac80211/rc80211_minstrel.c
patching file net/mac80211/rc80211_minstrel.h
patching file net/mac80211/rc80211_minstrel_debugfs.c
patching file net/mac80211/rc80211_minstrel_ht.c
patching file net/mac80211/rc80211_minstrel_ht.h
patching file net/mac80211/rc80211_minstrel_ht_debugfs.c

Applying ./patches/subsys/340-mac80211-minstrel_ht-remove-old-ewma-based-rate-aver.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c
patching file net/mac80211/rc80211_minstrel_ht.h

Applying ./patches/subsys/341-mac80211-minstrel_ht-improve-ampdu-length-estimation.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c

Applying ./patches/subsys/342-mac80211-minstrel_ht-improve-sample-rate-selection.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c

Applying ./patches/subsys/343-mac80211-minstrel_ht-fix-max-probability-rate-select.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c

Applying ./patches/subsys/344-mac80211-minstrel_ht-increase-stats-update-interval.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c

Applying ./patches/subsys/345-mac80211-minstrel_ht-fix-rounding-error-in-throughpu.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c

Applying ./patches/subsys/346-mac80211-minstrel_ht-use-bitfields-to-encode-rate-in.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c
patching file net/mac80211/rc80211_minstrel_ht.h
patching file net/mac80211/rc80211_minstrel_ht_debugfs.c

Applying ./patches/subsys/347-mac80211-minstrel_ht-update-total-packets-counter-in.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c

Applying ./patches/subsys/348-mac80211-minstrel_ht-reduce-the-need-to-sample-slowe.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c
patching file net/mac80211/rc80211_minstrel_ht.h

Applying ./patches/subsys/349-mac80211-minstrel_ht-significantly-redesign-the-rate.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c
patching file net/mac80211/rc80211_minstrel_ht.h

Applying ./patches/subsys/350-mac80211-minstrel_ht-show-sampling-rates-in-debugfs.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht_debugfs.c

Applying ./patches/subsys/351-mac80211-minstrel_ht-remove-sample-rate-switching-co.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c
patching file net/mac80211/rc80211_minstrel_ht.h

Applying ./patches/subsys/352-mac80211-minstrel_ht-fix-regression-in-the-max_prob_.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c

Applying ./patches/subsys/353-mac80211-minstrel_ht-fix-MINSTREL_FRAC-macro.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.h

Applying ./patches/subsys/354-mac80211-minstrel_ht-reduce-fluctuations-in-rate-pro.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c

Applying ./patches/subsys/355-mac80211-minstrel_ht-rework-rate-downgrade-code-and-.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c

Applying ./patches/subsys/371-mac80211-don-t-apply-flow-control-on-management-fram.patch using plaintext: 
patching file net/mac80211/tx.c

Applying ./patches/subsys/372-mac80211-set-sk_pacing_shift-for-802.3-txpath.patch using plaintext: 
patching file net/mac80211/tx.c

Applying ./patches/subsys/373-mac80211-support-Rx-timestamp-calculation-for-all-pr.patch using plaintext: 
patching file net/mac80211/ieee80211_i.h
patching file net/mac80211/util.c

Applying ./patches/subsys/380-mac80211-assure-all-fragments-are-encrypted.patch using plaintext: 
patching file net/mac80211/rx.c

Applying ./patches/subsys/381-mac80211-prevent-mixed-key-and-fragment-cache-attack.patch using plaintext: 
patching file net/mac80211/ieee80211_i.h
patching file net/mac80211/key.c
patching file net/mac80211/key.h
patching file net/mac80211/rx.c

Applying ./patches/subsys/382-mac80211-properly-handle-A-MSDUs-that-start-with-an-.patch using plaintext: 
patching file include/net/cfg80211.h
patching file net/mac80211/rx.c
patching file net/wireless/util.c

Applying ./patches/subsys/383-cfg80211-mitigate-A-MSDU-aggregation-attacks.patch using plaintext: 
patching file net/wireless/util.c

Applying ./patches/subsys/384-mac80211-drop-A-MSDUs-on-old-ciphers.patch using plaintext: 
patching file net/mac80211/rx.c

Applying ./patches/subsys/385-mac80211-add-fragment-cache-to-sta_info.patch using plaintext: 
patching file net/mac80211/ieee80211_i.h
patching file net/mac80211/iface.c
patching file net/mac80211/rx.c
patching file net/mac80211/sta_info.c
patching file net/mac80211/sta_info.h

Applying ./patches/subsys/386-mac80211-check-defrag-PN-against-current-frame.patch using plaintext: 
patching file net/mac80211/ieee80211_i.h
patching file net/mac80211/rx.c
patching file net/mac80211/wpa.c

Applying ./patches/subsys/387-mac80211-prevent-attacks-on-TKIP-WEP-as-well.patch using plaintext: 
patching file net/mac80211/rx.c
patching file net/mac80211/sta_info.h

Applying ./patches/subsys/388-mac80211-do-not-accept-forward-invalid-EAPOL-frames.patch using plaintext: 
patching file net/mac80211/rx.c

Applying ./patches/subsys/389-mac80211-extend-protection-against-mixed-key-and-fra.patch using plaintext: 
patching file net/mac80211/rx.c

Applying ./patches/subsys/400-allow-ibss-mixed.patch using plaintext: 
patching file net/wireless/core.c

Applying ./patches/subsys/500-mac80211_configure_antenna_gain.patch using plaintext: 
patching file include/net/cfg80211.h
patching file include/net/mac80211.h
patching file include/uapi/linux/nl80211.h
patching file net/mac80211/cfg.c
patching file net/mac80211/ieee80211_i.h
patching file net/mac80211/main.c
patching file net/wireless/nl80211.c

Applying ./patches/subsys/600-mac80211-allow-vht-on-2g.patch using plaintext: 
patching file net/mac80211/vht.c
patching file net/mac80211/util.c
Hunk #1 succeeded at 1906 (offset 137 lines).
patching file net/mac80211/mlme.c
Hunk #1 succeeded at 5071 (offset 247 lines).

Applying ./patches/ath/070-ath_common_config.patch using plaintext: 
patching file drivers/net/wireless/ath/Kconfig

Applying ./patches/ath/080-ath10k_thermal_config.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/Kconfig
patching file drivers/net/wireless/ath/ath10k/Makefile
patching file drivers/net/wireless/ath/ath10k/thermal.h
patching file local-symbols
Hunk #1 succeeded at 142 (offset -1 lines).

Applying ./patches/ath/120-owl-loader-compat.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/ath9k_pci_owl_loader.c

Applying ./patches/ath/201-ath5k-WAR-for-AR71xx-PCI-bug.patch using plaintext: 
patching file drivers/net/wireless/ath/ath5k/initvals.c
patching file drivers/net/wireless/ath/ath5k/dma.c

Applying ./patches/ath/300-ath10k-add-CCMP-PN-replay-protection-for-fragmented-.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/htt.h
patching file drivers/net/wireless/ath/ath10k/htt_rx.c

Applying ./patches/ath/301-ath10k-drop-fragments-with-multicast-DA-for-PCIe.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/htt_rx.c

Applying ./patches/ath/302-ath10k-drop-fragments-with-multicast-DA-for-SDIO.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/htt_rx.c

Applying ./patches/ath/303-ath10k-drop-MPDU-which-has-discard-flag-set-by-firmw.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/htt_rx.c
patching file drivers/net/wireless/ath/ath10k/rx_desc.h

Applying ./patches/ath/304-ath10k-Fix-TKIP-Michael-MIC-verification-for-PCIe.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/htt_rx.c

Applying ./patches/ath/305-ath10k-Validate-first-subframe-of-A-MSDU-before-proc.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/htt_rx.c

Applying ./patches/ath/350-ath9k_hw-reset-AHB-WMAC-interface-on-AR91xx.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/hw.c

Applying ./patches/ath/351-ath9k_hw-issue-external-reset-for-QCA955x.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/hw.c

Applying ./patches/ath/354-ath9k-force-rx_clear-when-disabling-rx.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/mac.c

Applying ./patches/ath/356-Revert-ath9k-interpret-requested-txpower-in-EIRP-dom.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/hw.c

Applying ./patches/ath/365-ath9k-adjust-tx-power-reduction-for-US-regulatory-do.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/hw.c

Applying ./patches/ath/400-ath_move_debug_code.patch using plaintext: 
patching file drivers/net/wireless/ath/Makefile
patching file drivers/net/wireless/ath/ath.h

Applying ./patches/ath/401-ath9k_blink_default.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/init.c

Applying ./patches/ath/402-ath_regd_optional.patch using plaintext: 
patching file drivers/net/wireless/ath/regd.c
patching file drivers/net/wireless/ath/Kconfig
patching file local-symbols
Hunk #1 succeeded at 85 (offset -1 lines).

Applying ./patches/ath/403-world_regd_fixup.patch using plaintext: 
patching file drivers/net/wireless/ath/regd.c

Applying ./patches/ath/404-regd_no_assoc_hints.patch using plaintext: 
patching file net/wireless/reg.c

Applying ./patches/ath/405-ath_regd_us.patch using plaintext: 
patching file drivers/net/wireless/ath/regd_common.h

Applying ./patches/ath/406-ath_relax_default_regd.patch using plaintext: 
patching file drivers/net/wireless/ath/regd.c

Applying ./patches/ath/410-ath9k_allow_adhoc_and_ap.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/init.c

Applying ./patches/ath/411-ath5k_allow_adhoc_and_ap.patch using plaintext: 
patching file drivers/net/wireless/ath/ath5k/mac80211-ops.c
patching file drivers/net/wireless/ath/ath5k/base.c

Applying ./patches/ath/420-ath5k_disable_fast_cc.patch using plaintext: 
patching file drivers/net/wireless/ath/ath5k/reset.c

Applying ./patches/ath/430-add_ath5k_platform.patch using plaintext: 
patching file include/linux/ath5k_platform.h

Applying ./patches/ath/431-add_platform_eeprom_support_to_ath5k.patch using plaintext: 
patching file drivers/net/wireless/ath/ath5k/pci.c

Applying ./patches/ath/432-ath5k_add_pciids.patch using plaintext: 
patching file drivers/net/wireless/ath/ath5k/pci.c

Applying ./patches/ath/440-ath5k_channel_bw_debugfs.patch using plaintext: 
patching file drivers/net/wireless/ath/ath5k/debug.c
patching file drivers/net/wireless/ath/ath5k/ath5k.h
patching file drivers/net/wireless/ath/ath5k/base.c

Applying ./patches/ath/450-ath9k-enabled-MFP-capability-unconditionally.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/init.c

Applying ./patches/ath/500-ath9k_eeprom_debugfs.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/debug.c

Applying ./patches/ath/501-ath9k_ahb_init.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/init.c

Applying ./patches/ath/510-ath9k_intr_mitigation_tweak.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/hw.c

Applying ./patches/ath/511-ath9k_reduce_rxbuf.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/ath9k.h

Applying ./patches/ath/512-ath9k_channelbw_debugfs.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/debug.c
patching file drivers/net/wireless/ath/ath.h
patching file drivers/net/wireless/ath/ath9k/common.c

Applying ./patches/ath/513-ath9k_add_pci_ids.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/hw.c
patching file drivers/net/wireless/ath/ath9k/hw.h
patching file drivers/net/wireless/ath/ath9k/pci.c

Applying ./patches/ath/530-ath9k_extra_leds.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/ath9k.h
patching file drivers/net/wireless/ath/ath9k/gpio.c
patching file drivers/net/wireless/ath/ath9k/init.c
patching file drivers/net/wireless/ath/ath9k/debug.c

Applying ./patches/ath/531-ath9k_extra_platform_leds.patch using plaintext: 
patching file include/linux/ath9k_platform.h
patching file drivers/net/wireless/ath/ath9k/gpio.c

Applying ./patches/ath/540-ath9k_reduce_ani_interval.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/ani.h

Applying ./patches/ath/542-ath9k_debugfs_diag.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/debug.c
patching file drivers/net/wireless/ath/ath9k/hw.h
patching file drivers/net/wireless/ath/ath9k/hw.c
patching file drivers/net/wireless/ath/ath9k/main.c

Applying ./patches/ath/543-ath9k_entropy_from_adc.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/hw.h
patching file drivers/net/wireless/ath/ath9k/ar9003_phy.c
patching file drivers/net/wireless/ath/ath9k/init.c
patching file drivers/net/wireless/ath/ath9k/hw-ops.h
patching file drivers/net/wireless/ath/ath9k/ar5008_phy.c
patching file drivers/net/wireless/ath/ath9k/ar9002_phy.h

Applying ./patches/ath/544-ath9k-ar933x-usb-hang-workaround.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/hw.c
patching file drivers/net/wireless/ath/ath9k/phy.h

Applying ./patches/ath/545-ath9k_ani_ws_detect.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/ar5008_phy.c
patching file drivers/net/wireless/ath/ath9k/ar9003_phy.c

Applying ./patches/ath/547-ath9k_led_defstate_fix.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/gpio.c

Applying ./patches/ath/548-ath9k_enable_gpio_chip.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/ath9k.h
patching file drivers/net/wireless/ath/ath9k/gpio.c

Applying ./patches/ath/549-ath9k_enable_gpio_buttons.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/ath9k.h
patching file drivers/net/wireless/ath/ath9k/gpio.c
patching file include/linux/ath9k_platform.h

Applying ./patches/ath/550-ath9k-disable-bands-via-dt.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/init.c

Applying ./patches/ath/551-ath9k_ubnt_uap_plus_hsr.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/channel.c
patching file drivers/net/wireless/ath/ath9k/hsr.c
patching file drivers/net/wireless/ath/ath9k/hsr.h
patching file drivers/net/wireless/ath/ath9k/main.c
patching file drivers/net/wireless/ath/ath9k/Makefile
patching file local-symbols
Hunk #1 succeeded at 112 (offset -1 lines).
patching file drivers/net/wireless/ath/ath9k/Kconfig

Applying ./patches/ath/552-ahb_of.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/ahb.c
patching file drivers/net/wireless/ath/ath9k/ath9k.h

Applying ./patches/ath/553-ath9k_of_gpio_mask.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/init.c

Applying ./patches/ath/921-ath10k_init_devices_synchronously.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/core.c

Applying ./patches/ath/922-ath10k-increase-rx-buffer-size-to-2048.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/htt.h

Applying ./patches/ath/930-ath10k_add_tpt_led_trigger.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/mac.c

Applying ./patches/ath/974-ath10k_add-LED-and-GPIO-controlling-support-for-various-chipsets.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/Kconfig
patching file drivers/net/wireless/ath/ath10k/Makefile
patching file local-symbols
Hunk #1 succeeded at 145 (offset -1 lines).
patching file drivers/net/wireless/ath/ath10k/core.c
patching file drivers/net/wireless/ath/ath10k/core.h
patching file drivers/net/wireless/ath/ath10k/hw.h
patching file drivers/net/wireless/ath/ath10k/leds.c
patching file drivers/net/wireless/ath/ath10k/leds.h
patching file drivers/net/wireless/ath/ath10k/mac.c
patching file drivers/net/wireless/ath/ath10k/wmi-ops.h
patching file drivers/net/wireless/ath/ath10k/wmi-tlv.c
patching file drivers/net/wireless/ath/ath10k/wmi.c
patching file drivers/net/wireless/ath/ath10k/wmi.h

Applying ./patches/ath/975-ath10k-use-tpt-trigger-by-default.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/core.h
patching file drivers/net/wireless/ath/ath10k/leds.c
patching file drivers/net/wireless/ath/ath10k/mac.c

Applying ./patches/ath/980-ath10k-fix-max-antenna-gain-unit.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/mac.c

Applying ./patches/ath/981-ath10k-adjust-tx-power-reduction-for-US-regulatory-d.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/mac.c

Applying ./patches/ath/983-ath10k-allow-vht-on-2g.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/mac.c
Hunk #1 succeeded at 4834 (offset 116 lines).

Applying ./patches/rt2x00/002-rt2x00-define-RF5592-in-init_eeprom-routine.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c

Applying ./patches/rt2x00/100-rt2x00_options.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/Kconfig

Applying ./patches/rt2x00/501-rt2x00-allow-to-build-rt2800soc-module-for-RT3883.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/Kconfig

Applying ./patches/rt2x00/601-rt2x00-introduce-rt2x00_platform_h.patch using plaintext: 
patching file include/linux/rt2x00_platform.h
patching file drivers/net/wireless/ralink/rt2x00/rt2x00.h

Applying ./patches/rt2x00/602-rt2x00-introduce-rt2x00eeprom.patch using plaintext: 
patching file local-symbols
Hunk #1 succeeded at 332 (offset -1 lines).
patching file drivers/net/wireless/ralink/rt2x00/Kconfig
patching file drivers/net/wireless/ralink/rt2x00/Makefile
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.h
patching file drivers/net/wireless/ralink/rt2x00/rt2800soc.c
patching file drivers/net/wireless/ralink/rt2x00/rt2x00.h
patching file drivers/net/wireless/ralink/rt2x00/rt2x00dev.c
patching file drivers/net/wireless/ralink/rt2x00/rt2x00eeprom.c
patching file drivers/net/wireless/ralink/rt2x00/rt2x00lib.h
patching file drivers/net/wireless/ralink/rt2x00/rt2x00soc.c

Applying ./patches/rt2x00/603-rt2x00-of_load_eeprom_filename.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2x00eeprom.c

Applying ./patches/rt2x00/604-rt2x00-load-eeprom-on-SoC-from-a-mtd-device-defines-.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/Kconfig
patching file drivers/net/wireless/ralink/rt2x00/rt2x00eeprom.c

Applying ./patches/rt2x00/606-rt2x00-allow_disabling_bands_through_platform_data.patch using plaintext: 
patching file include/linux/rt2x00_platform.h
patching file drivers/net/wireless/ralink/rt2x00/rt2x00dev.c
patching file drivers/net/wireless/ralink/rt2x00/rt2x00.h

Applying ./patches/rt2x00/607-rt2x00-add_platform_data_mac_addr.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2x00dev.c
patching file include/linux/rt2x00_platform.h

Applying ./patches/rt2x00/608-rt2x00-allow_disabling_bands_through_dts.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2x00dev.c

Applying ./patches/rt2x00/609-rt2x00-make-wmac-loadable-via-OF-on-rt288x-305x-SoC.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800soc.c

Applying ./patches/rt2x00/610-rt2x00-change-led-polarity-from-OF.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c
patching file drivers/net/wireless/ralink/rt2x00/rt2x00leds.c

Applying ./patches/rt2x00/611-rt2x00-add-AP+STA-support.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2x00dev.c

Applying ./patches/rt2x00/612-rt2x00-led-tpt-trigger-support.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2x00dev.c

Applying ./patches/rt2x00/650-rt2x00-add-support-for-external-PA-on-MT7620.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800.h
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c

Applying ./patches/rt2x00/982-rt2x00-add-rf-self-txdc-calibration.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c

Applying ./patches/rt2x00/983-rt2x00-add-r-calibration.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c

Applying ./patches/rt2x00/984-rt2x00-add-rxdcoc-calibration.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c

Applying ./patches/rt2x00/985-rt2x00-add-rxiq-calibration.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c

Applying ./patches/rt2x00/986-rt2x00-add-TX-LOFT-calibration.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.h

Applying ./patches/rt2x00/990-rt2x00-mt7620-introduce-accessors-for-CHIP_VER-register.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.h
patching file drivers/net/wireless/ralink/rt2x00/rt2800pci.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800soc.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800usb.c

Applying ./patches/rt2x00/991-rt2x00-mt7620-differentiate-based-on-SoC-CHIP_VER.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800.h
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c

Applying ./patches/rt2x00/992-rt2x00-save-survey-for-every-channel-visited.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.h
patching file drivers/net/wireless/ralink/rt2x00/rt2800pci.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800soc.c
patching file drivers/net/wireless/ralink/rt2x00/rt2x00.h
patching file drivers/net/wireless/ralink/rt2x00/rt2x00dev.c
patching file drivers/net/wireless/ralink/rt2x00/rt2x00mac.c

Applying ./patches/mwl/700-mwl8k-missing-pci-id-for-WNR854T.patch using plaintext: 
patching file drivers/net/wireless/marvell/mwl8k.c

Applying ./patches/mwl/801-libertas-configure-sysfs-links.patch using plaintext: 
patching file drivers/net/wireless/marvell/libertas/cfg.c
patching file drivers/net/wireless/marvell/libertas/main.c

Applying ./patches/mwl/802-libertas-set-wireless-macaddr.patch using plaintext: 
patching file drivers/net/wireless/marvell/libertas/cfg.c

Applying ./patches/mwl/940-mwl8k_init_devices_synchronously.patch using plaintext: 
patching file drivers/net/wireless/marvell/mwl8k.c

Applying ./patches/brcm/040-brcmutil_option.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/Kconfig

Applying ./patches/brcm/810-b43-gpio-mask-module-option.patch using plaintext: 
patching file drivers/net/wireless/broadcom/b43/b43.h
patching file drivers/net/wireless/broadcom/b43/main.c

Applying ./patches/brcm/811-b43_no_pio.patch using plaintext: 
patching file drivers/net/wireless/broadcom/b43/Makefile
patching file drivers/net/wireless/broadcom/b43/main.c
patching file drivers/net/wireless/broadcom/b43/pio.h
patching file drivers/net/wireless/broadcom/b43/Kconfig

Applying ./patches/brcm/812-b43-add-antenna-control.patch using plaintext: 
patching file drivers/net/wireless/broadcom/b43/main.c
patching file drivers/net/wireless/broadcom/b43/b43.h

Applying ./patches/brcm/813-b43-reduce-number-of-RX-slots.patch using plaintext: 
patching file drivers/net/wireless/broadcom/b43/dma.h

Applying ./patches/brcm/814-b43-only-use-gpio-0-1-for-led.patch using plaintext: 
patching file drivers/net/wireless/broadcom/b43/main.c

Applying ./patches/brcm/815-b43-always-take-overlapping-devs.patch using plaintext: 
patching file drivers/net/wireless/broadcom/b43/main.c

Applying ./patches/brcm/850-brcmsmac-remove-extra-regulation-restriction.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmsmac/channel.c

Applying ./patches/brcm/860-brcmfmac-register-wiphy-s-during-module_init.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/core.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/firmware.c

Applying ./patches/brcm/861-brcmfmac-workaround-bug-with-some-inconsistent-BSSes.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/cfg80211.c

Applying ./patches/brcm/862-brcmfmac-Disable-power-management.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/cfg80211.c

Applying ./patches/brcm/863-brcmfmac-add-in-driver-tables-with-country-codes.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/of.c

Applying ./patches/brcm/864-brcmfmac-do-not-use-internal-roaming-engine-by-default.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/common.c

Applying ./patches/brcm/998-survey.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/cfg80211.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/core.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/core.h

Applying ./patches/rtl/001-v5.12-rtlwifi-8821ae-upgrade-PHY-and-RF-parameters.patch using plaintext: 
patching file drivers/net/wireless/realtek/rtlwifi/rtl8821ae/table.c

Applying ./patches/rtl/002-v5.13-rtlwifi-implement-set_tim-by-update-beacon-content.patch using plaintext: 
patching file drivers/net/wireless/realtek/rtlwifi/core.c
patching file drivers/net/wireless/realtek/rtlwifi/core.h
patching file drivers/net/wireless/realtek/rtlwifi/usb.c
patching file drivers/net/wireless/realtek/rtlwifi/wifi.h
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1'
Generating local configuration database from kernel ... done.
cc -Wall -Wmissing-prototypes -Wstrict-prototypes -O2 -fomit-frame-pointer -DKBUILD_NO_NLS   -c -o conf.o conf.c
conf.c: In function 'conf_askvalue':
conf.c:89:3: warning: format not a string literal and no format arguments [-Wformat-security]
   89 |   printf(_("(NEW) "));
      |   ^~~~~~
conf.c: In function 'conf_choice':
conf.c:285:5: warning: format not a string literal and no format arguments [-Wformat-security]
  285 |     printf(_(" (NEW)"));
      |     ^~~~~~
conf.c: In function 'check_conf':
conf.c:440:6: warning: format not a string literal and no format arguments [-Wformat-security]
  440 |      printf(_("*\n* Restart config...\n*\n"));
      |      ^~~~~~
conf.c: In function 'main':
conf.c:617:6: warning: format not a string literal and no format arguments [-Wformat-security]
  617 |      _("\n*** The configuration requires explicit update.\n\n"));
      |      ^
conf.c:669:4: warning: format not a string literal and no format arguments [-Wformat-security]
  669 |    fprintf(stderr, _("\n*** Error during writing of the configuration.\n\n"));
      |    ^~~~~~~
conf.c:673:4: warning: format not a string literal and no format arguments [-Wformat-security]
  673 |    fprintf(stderr, _("\n*** Error during update of the configuration.\n\n"));
      |    ^~~~~~~
conf.c:684:4: warning: format not a string literal and no format arguments [-Wformat-security]
  684 |    fprintf(stderr, _("\n*** Error during writing of the configuration.\n\n"));
      |    ^~~~~~~
lex -ozconf.lex.c -L zconf.l
yacc -ozconf.tab.c -t -l zconf.y
zconf.y:34.1-7: warning: POSIX Yacc does not support %expect [-Wyacc]
   34 | %expect 32
      | ^~~~~~~
zconf.y:97.1-11: warning: POSIX Yacc does not support %destructor [-Wyacc]
   97 | %destructor {
      | ^~~~~~~~~~~
cc -Wall -Wmissing-prototypes -Wstrict-prototypes -O2 -fomit-frame-pointer -DKBUILD_NO_NLS   -c -o zconf.tab.o zconf.tab.c
In file included from zconf.tab.c:2346:
confdata.c: In function 'conf_write':
confdata.c:773:22: warning: '%s' directive writing likely 7 or more bytes into a region of size between 1 and 4097 [-Wformat-overflow=]
  773 |  sprintf(newname, "%s%s", dirname, basename);
      |                      ^~
confdata.c:773:19: note: assuming directive output of 7 bytes
  773 |  sprintf(newname, "%s%s", dirname, basename);
      |                   ^~~~~~
In file included from /usr/include/stdio.h:867,
                 from zconf.tab.c:78:
/usr/include/x86_64-linux-gnu/bits/stdio2.h:36:10: note: '__builtin___sprintf_chk' output 1 or more bytes (assuming 4104) into a destination of size 4097
   36 |   return __builtin___sprintf_chk (__s, __USE_FORTIFY_LEVEL - 1,
      |          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   37 |       __bos (__s), __fmt, __va_arg_pack ());
      |       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from zconf.tab.c:2346:
confdata.c:776:23: warning: '.tmpconfig.' directive writing 11 bytes into a region of size between 1 and 4097 [-Wformat-overflow=]
  776 |   sprintf(tmpname, "%s.tmpconfig.%d", dirname, (int)getpid());
      |                       ^~~~~~~~~~~
In file included from /usr/include/stdio.h:867,
                 from zconf.tab.c:78:
/usr/include/x86_64-linux-gnu/bits/stdio2.h:36:10: note: '__builtin___sprintf_chk' output between 13 and 4119 bytes into a destination of size 4097
   36 |   return __builtin___sprintf_chk (__s, __USE_FORTIFY_LEVEL - 1,
      |          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   37 |       __bos (__s), __fmt, __va_arg_pack ());
      |       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
cc   conf.o zconf.tab.o   -o conf
.config:34:warning: override: reassigning to symbol LIBERTAS
.config:36:warning: override: reassigning to symbol LIBERTAS
.config:41:warning: override: reassigning to symbol MWIFIEX
boolean symbol CRYPTO_LIB_ARC4 tested for 'm'? test forced to 'n'
#
# configuration written to .config
#
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1'
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1'
make[5]: 'Kconfig.versions' is up to date.
make[7]: 'Kconfig.versions' is up to date.
make[8]: 'conf' is up to date.
boolean symbol CRYPTO_LIB_ARC4 tested for 'm'? test forced to 'n'
#
# configuration written to .config
#
Building backport-include/backport/autoconf.h ... done.
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/compat/main.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/compat/backport-5.5.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/compat/backport-5.10.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/compat/compat.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/admtek/adm8211.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ar5523/ar5523.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath10k/mac.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath10k/debug.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath10k/core.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath10k/htc.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath10k/htt.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath10k/htt_rx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath10k/htt_tx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath10k/txrx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath10k/wmi.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath10k/wmi-tlv.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath10k/bmi.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath10k/hw.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath10k/p2p.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath10k/swap.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath10k/thermal.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath10k/leds.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath10k/debugfs_sta.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath10k/wow.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath10k/coredump.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath10k/ce.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath10k/pci.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath10k/ath10k_core.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath10k/ath10k_pci.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath5k/caps.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath5k/initvals.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath5k/eeprom.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath5k/gpio.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath5k/desc.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath5k/dma.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath5k/qcu.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath5k/pcu.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath5k/phy.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath5k/reset.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath5k/attach.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath5k/base.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath5k/led.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath5k/rfkill.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath5k/ani.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath5k/sysfs.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath5k/mac80211-ops.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath5k/debug.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath5k/pci.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath5k/ath5k.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath6kl/debug.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath6kl/hif.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath6kl/htc_mbox.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath6kl/htc_pipe.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath6kl/bmi.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath6kl/cfg80211.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath6kl/init.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath6kl/main.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath6kl/txrx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath6kl/wmi.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath6kl/core.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath6kl/recovery.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath6kl/sdio.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath6kl/usb.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath6kl/ath6kl_core.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath6kl/ath6kl_sdio.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath6kl/ath6kl_usb.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/beacon.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/gpio.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/init.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/main.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/recv.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/xmit.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/link.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/antenna.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/channel.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/pci.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/dfs_debug.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/dfs.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/debug.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/ar9002_hw.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/ar9003_hw.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/hw.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/ar9003_phy.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/ar9002_phy.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/ar5008_phy.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/ar9002_calib.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/ar9003_calib.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/calib.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/eeprom.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/eeprom_def.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/eeprom_4k.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/eeprom_9287.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/ani.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/mac.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/ar9002_mac.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/ar9003_mac.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/ar9003_eeprom.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/ar9003_paprd.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/ar9003_rtt.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/common.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/common-init.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/common-beacon.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/common-debug.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/htc_hst.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/hif_usb.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/wmi.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/htc_drv_txrx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/htc_drv_main.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/htc_drv_beacon.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/htc_drv_init.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/htc_drv_gpio.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/htc_drv_debug.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/ath9k_pci_owl_loader.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/ath9k.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/ath9k_hw.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/ath9k_common.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/ath9k_htc.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/carl9170/main.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/carl9170/usb.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/carl9170/cmd.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/carl9170/mac.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/carl9170/phy.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/carl9170/led.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/carl9170/fw.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/carl9170/tx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/carl9170/rx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/carl9170/debug.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/carl9170/carl9170.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/wil6210/main.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/wil6210/netdev.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/wil6210/cfg80211.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/wil6210/pcie_bus.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/wil6210/debugfs.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/wil6210/wmi.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/wil6210/interrupt.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/wil6210/txrx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/wil6210/txrx_edma.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/wil6210/debug.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/wil6210/rx_reorder.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/wil6210/fw.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/wil6210/pm.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/wil6210/pmc.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/wil6210/wil_platform.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/wil6210/ethtool.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/wil6210/wil_crash_dump.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/wil6210/p2p.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/wil6210/wil6210.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/main.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/regd.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/hw.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/key.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/debug.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/dfs_pattern_detector.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/dfs_pri_detector.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43/main.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43/bus.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43/phy_g.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43/tables.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43/lo.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43/wa.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43/tables_nphy.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43/radio_2055.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43/radio_2056.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43/radio_2057.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43/phy_common.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43/phy_n.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43/phy_lp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43/tables_lpphy.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43/phy_ht.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43/tables_phy_ht.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43/radio_2059.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43/sysfs.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43/xmit.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43/dma.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43/rfkill.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43/ppr.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43/leds.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43/b43.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43legacy/main.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43legacy/ilt.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43legacy/phy.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43legacy/radio.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43legacy/sysfs.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43legacy/xmit.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43legacy/rfkill.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43legacy/leds.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43legacy/dma.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43legacy/b43legacy.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmfmac/cfg80211.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmfmac/chip.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmfmac/fwil.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmfmac/fweh.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmfmac/p2p.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmfmac/proto.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmfmac/common.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmfmac/core.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmfmac/firmware.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmfmac/feature.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmfmac/btcoex.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmfmac/vendor.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmfmac/pno.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmfmac/bcdc.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmfmac/fwsignal.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmfmac/commonring.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmfmac/flowring.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmfmac/msgbuf.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmfmac/usb.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmfmac/pcie.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmfmac/dmi.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmfmac/brcmfmac.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmsmac/mac80211_if.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmsmac/ucode_loader.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmsmac/ampdu.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmsmac/antsel.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmsmac/channel.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmsmac/main.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmsmac/phy_shim.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmsmac/pmu.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmsmac/rate.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmsmac/stf.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmsmac/aiutils.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmsmac/phy/phy_cmn.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmsmac/phy/phy_lcn.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmsmac/phy/phy_n.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmsmac/phy/phytbl_lcn.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmsmac/phy/phytbl_n.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmsmac/phy/phy_qmath.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmsmac/dma.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmsmac/brcms_trace_events.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmsmac/debug.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmsmac/brcmsmac.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmutil/utils.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmutil/d11.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmutil/brcmutil.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/ipw2x00/ipw2100.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/ipw2x00/ipw2200.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/ipw2x00/libipw_module.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/ipw2x00/libipw_tx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/ipw2x00/libipw_rx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/ipw2x00/libipw_wx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/ipw2x00/libipw_geo.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/ipw2x00/libipw.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlegacy/common.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlegacy/4965.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlegacy/4965-mac.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlegacy/4965-rs.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlegacy/4965-calib.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlegacy/3945-mac.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlegacy/3945.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlegacy/3945-rs.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlegacy/iwlegacy.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlegacy/iwl4965.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlegacy/iwl3945.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/dvm/main.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/dvm/rs.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/dvm/mac80211.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/dvm/ucode.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/dvm/tx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/dvm/lib.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/dvm/calib.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/dvm/tt.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/dvm/sta.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/dvm/rx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/dvm/power.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/dvm/scan.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/dvm/rxon.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/dvm/devices.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/dvm/led.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/dvm/iwldvm.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/mvm/fw.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/mvm/mac80211.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/mvm/nvm.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/mvm/ops.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/mvm/phy-ctxt.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/mvm/mac-ctxt.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/mvm/utils.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/mvm/rx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/mvm/rxmq.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/mvm/tx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/mvm/binding.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/mvm/quota.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/mvm/sta.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/mvm/sf.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/mvm/scan.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/mvm/time-event.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/mvm/rs.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/mvm/rs-fw.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/mvm/power.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/mvm/coex.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/mvm/tt.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/mvm/offloading.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/mvm/tdls.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/mvm/ftm-responder.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/mvm/ftm-initiator.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/mvm/led.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/mvm/d3.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/mvm/iwlmvm.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/iwl-io.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/iwl-drv.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/iwl-debug.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/iwl-eeprom-read.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/iwl-eeprom-parse.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/iwl-phy-db.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/iwl-nvm-parse.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/pcie/drv.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/pcie/rx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/pcie/tx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/pcie/trans.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/pcie/ctxt-info.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/pcie/ctxt-info-gen3.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/pcie/trans-gen2.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/pcie/tx-gen2.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/iwl-dbg-tlv.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/iwl-trans.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/queue/tx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/fw/img.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/fw/notif-wait.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/fw/dbg.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/fw/pnvm.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/cfg/1000.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/cfg/2000.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/cfg/5000.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/cfg/6000.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/cfg/7000.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/cfg/8000.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/cfg/9000.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/cfg/22000.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/fw/paging.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/fw/smem.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/fw/init.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/fw/acpi.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/iwlwifi.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/orinoco/main.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/orinoco/fw.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/orinoco/hw.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/orinoco/mic.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/orinoco/scan.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/orinoco/wext.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/orinoco/hermes_dld.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/orinoco/hermes.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/orinoco/cfg.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/orinoco/orinoco_cs.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/orinoco/orinoco_plx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/orinoco/orinoco_pci.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/orinoco/orinoco.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/p54/eeprom.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/p54/fwio.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/p54/txrx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/p54/main.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/p54/led.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/p54/p54usb.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/p54/p54pci.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/p54/p54common.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/libertas/cfg.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/libertas/cmd.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/libertas/cmdresp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/libertas/debugfs.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/libertas/ethtool.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/libertas/main.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/libertas/rx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/libertas/tx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/libertas/firmware.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/libertas/if_usb.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/libertas/if_sdio.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/libertas/if_spi.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/libertas/libertas.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/libertas/usb8xxx.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/libertas/libertas_sdio.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/libertas/libertas_spi.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/main.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/init.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/cfp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/cmdevt.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/util.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/txrx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/wmm.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/11n.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/11ac.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/11n_aggr.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/11n_rxreorder.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/scan.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/join.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/sta_ioctl.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/sta_cmd.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/uap_cmd.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/ie.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/sta_cmdresp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/sta_event.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/uap_event.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/sta_tx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/sta_rx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/uap_txrx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/cfg80211.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/ethtool.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/11h.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/tdls.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/debugfs.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/sdio.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/pcie.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/mwifiex.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/mwifiex_sdio.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/mwifiex_pcie.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwl8k.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/mediatek/mt7601u/usb.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/mediatek/mt7601u/init.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/mediatek/mt7601u/main.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/mediatek/mt7601u/mcu.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/mediatek/mt7601u/trace.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/mediatek/mt7601u/dma.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/mediatek/mt7601u/core.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/mediatek/mt7601u/eeprom.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/mediatek/mt7601u/phy.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/mediatek/mt7601u/mac.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/mediatek/mt7601u/util.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/mediatek/mt7601u/debugfs.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/mediatek/mt7601u/tx.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/mediatek/mt7601u/mt7601u.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2x00dev.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2x00mac.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2x00config.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2x00queue.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2x00link.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2x00crypto.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2x00firmware.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2x00leds.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2x00eeprom.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2x00mmio.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2x00pci.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2x00usb.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2800lib.o
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2800lib.c: In function 'rt2800_get_survey':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2800lib.c:12215:25: warning: unused variable 'conf' [-Wunused-variable]
  struct ieee80211_conf *conf = &hw->conf;
                         ^~~~
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2800mmio.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2400pci.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2500pci.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt61pci.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2800pci.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2500usb.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt73usb.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2800usb.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2x00lib.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/dev.o
In file included from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/dev.c:55:
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h: In function 'rtl818x_ioread8':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h:155:17: warning: passing argument 1 of 'ioread8' discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  return ioread8(addr);
                 ^~~~
In file included from ./arch/x86/include/asm/io.h:229,
                 from ./arch/x86/include/asm/realmode.h:15,
                 from ./arch/x86/include/asm/acpi.h:16,
                 from ./arch/x86/include/asm/fixmap.h:29,
                 from ./arch/x86/include/asm/apic.h:11,
                 from ./arch/x86/include/asm/smp.h:13,
                 from ./include/linux/smp.h:68,
                 from ./include/linux/percpu.h:7,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/percpu.h:6,
                 from ./include/linux/context_tracking_state.h:5,
                 from ./include/linux/vtime.h:5,
                 from ./include/linux/hardirq.h:8,
                 from ./include/linux/interrupt.h:11,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/interrupt.h:4,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/dev.c:46:
./include/asm-generic/iomap.h:29:29: note: expected 'void *' but argument is of type 'const u8 *' {aka 'const unsigned char *'}
 extern unsigned int ioread8(void __iomem *);
                             ^~~~~~~~~~~~~~
In file included from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/dev.c:55:
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h: In function 'rtl818x_ioread16':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h:160:18: warning: passing argument 1 of 'ioread16' discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  return ioread16(addr);
                  ^~~~
In file included from ./arch/x86/include/asm/io.h:229,
                 from ./arch/x86/include/asm/realmode.h:15,
                 from ./arch/x86/include/asm/acpi.h:16,
                 from ./arch/x86/include/asm/fixmap.h:29,
                 from ./arch/x86/include/asm/apic.h:11,
                 from ./arch/x86/include/asm/smp.h:13,
                 from ./include/linux/smp.h:68,
                 from ./include/linux/percpu.h:7,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/percpu.h:6,
                 from ./include/linux/context_tracking_state.h:5,
                 from ./include/linux/vtime.h:5,
                 from ./include/linux/hardirq.h:8,
                 from ./include/linux/interrupt.h:11,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/interrupt.h:4,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/dev.c:46:
./include/asm-generic/iomap.h:30:30: note: expected 'void *' but argument is of type 'const __le16 *' {aka 'const short unsigned int *'}
 extern unsigned int ioread16(void __iomem *);
                              ^~~~~~~~~~~~~~
In file included from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/dev.c:55:
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h: In function 'rtl818x_ioread32':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h:165:18: warning: passing argument 1 of 'ioread32' discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  return ioread32(addr);
                  ^~~~
In file included from ./arch/x86/include/asm/io.h:229,
                 from ./arch/x86/include/asm/realmode.h:15,
                 from ./arch/x86/include/asm/acpi.h:16,
                 from ./arch/x86/include/asm/fixmap.h:29,
                 from ./arch/x86/include/asm/apic.h:11,
                 from ./arch/x86/include/asm/smp.h:13,
                 from ./include/linux/smp.h:68,
                 from ./include/linux/percpu.h:7,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/percpu.h:6,
                 from ./include/linux/context_tracking_state.h:5,
                 from ./include/linux/vtime.h:5,
                 from ./include/linux/hardirq.h:8,
                 from ./include/linux/interrupt.h:11,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/interrupt.h:4,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/dev.c:46:
./include/asm-generic/iomap.h:32:30: note: expected 'void *' but argument is of type 'const __le32 *' {aka 'const unsigned int *'}
 extern unsigned int ioread32(void __iomem *);
                              ^~~~~~~~~~~~~~
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8225.o
In file included from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8225.c:19:
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h: In function 'rtl818x_ioread8':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h:155:17: warning: passing argument 1 of 'ioread8' discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  return ioread8(addr);
                 ^~~~
In file included from ./arch/x86/include/asm/io.h:229,
                 from ./arch/x86/include/asm/realmode.h:15,
                 from ./arch/x86/include/asm/acpi.h:16,
                 from ./arch/x86/include/asm/fixmap.h:29,
                 from ./arch/x86/include/asm/apic.h:11,
                 from ./arch/x86/include/asm/smp.h:13,
                 from ./include/linux/smp.h:68,
                 from ./include/linux/percpu.h:7,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/percpu.h:6,
                 from ./include/linux/arch_topology.h:9,
                 from ./include/linux/topology.h:30,
                 from ./include/linux/gfp.h:9,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/gfp.h:3,
                 from ./include/linux/xarray.h:14,
                 from ./include/linux/radix-tree.h:18,
                 from ./include/linux/idr.h:15,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/idr.h:5,
                 from ./include/linux/kernfs.h:13,
                 from ./include/linux/sysfs.h:16,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/sysfs.h:3,
                 from ./include/linux/kobject.h:20,
                 from ./include/linux/pci.h:35,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/pci.h:3,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8225.c:15:
./include/asm-generic/iomap.h:29:29: note: expected 'void *' but argument is of type 'const u8 *' {aka 'const unsigned char *'}
 extern unsigned int ioread8(void __iomem *);
                             ^~~~~~~~~~~~~~
In file included from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8225.c:19:
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h: In function 'rtl818x_ioread16':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h:160:18: warning: passing argument 1 of 'ioread16' discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  return ioread16(addr);
                  ^~~~
In file included from ./arch/x86/include/asm/io.h:229,
                 from ./arch/x86/include/asm/realmode.h:15,
                 from ./arch/x86/include/asm/acpi.h:16,
                 from ./arch/x86/include/asm/fixmap.h:29,
                 from ./arch/x86/include/asm/apic.h:11,
                 from ./arch/x86/include/asm/smp.h:13,
                 from ./include/linux/smp.h:68,
                 from ./include/linux/percpu.h:7,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/percpu.h:6,
                 from ./include/linux/arch_topology.h:9,
                 from ./include/linux/topology.h:30,
                 from ./include/linux/gfp.h:9,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/gfp.h:3,
                 from ./include/linux/xarray.h:14,
                 from ./include/linux/radix-tree.h:18,
                 from ./include/linux/idr.h:15,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/idr.h:5,
                 from ./include/linux/kernfs.h:13,
                 from ./include/linux/sysfs.h:16,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/sysfs.h:3,
                 from ./include/linux/kobject.h:20,
                 from ./include/linux/pci.h:35,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/pci.h:3,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8225.c:15:
./include/asm-generic/iomap.h:30:30: note: expected 'void *' but argument is of type 'const __le16 *' {aka 'const short unsigned int *'}
 extern unsigned int ioread16(void __iomem *);
                              ^~~~~~~~~~~~~~
In file included from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8225.c:19:
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h: In function 'rtl818x_ioread32':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h:165:18: warning: passing argument 1 of 'ioread32' discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  return ioread32(addr);
                  ^~~~
In file included from ./arch/x86/include/asm/io.h:229,
                 from ./arch/x86/include/asm/realmode.h:15,
                 from ./arch/x86/include/asm/acpi.h:16,
                 from ./arch/x86/include/asm/fixmap.h:29,
                 from ./arch/x86/include/asm/apic.h:11,
                 from ./arch/x86/include/asm/smp.h:13,
                 from ./include/linux/smp.h:68,
                 from ./include/linux/percpu.h:7,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/percpu.h:6,
                 from ./include/linux/arch_topology.h:9,
                 from ./include/linux/topology.h:30,
                 from ./include/linux/gfp.h:9,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/gfp.h:3,
                 from ./include/linux/xarray.h:14,
                 from ./include/linux/radix-tree.h:18,
                 from ./include/linux/idr.h:15,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/idr.h:5,
                 from ./include/linux/kernfs.h:13,
                 from ./include/linux/sysfs.h:16,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/sysfs.h:3,
                 from ./include/linux/kobject.h:20,
                 from ./include/linux/pci.h:35,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/pci.h:3,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8225.c:15:
./include/asm-generic/iomap.h:32:30: note: expected 'void *' but argument is of type 'const __le32 *' {aka 'const unsigned int *'}
 extern unsigned int ioread32(void __iomem *);
                              ^~~~~~~~~~~~~~
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/sa2400.o
In file included from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/sa2400.c:23:
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h: In function 'rtl818x_ioread8':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h:155:17: warning: passing argument 1 of 'ioread8' discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  return ioread8(addr);
                 ^~~~
In file included from ./arch/x86/include/asm/io.h:229,
                 from ./arch/x86/include/asm/realmode.h:15,
                 from ./arch/x86/include/asm/acpi.h:16,
                 from ./arch/x86/include/asm/fixmap.h:29,
                 from ./arch/x86/include/asm/apic.h:11,
                 from ./arch/x86/include/asm/smp.h:13,
                 from ./include/linux/smp.h:68,
                 from ./include/linux/percpu.h:7,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/percpu.h:6,
                 from ./include/linux/arch_topology.h:9,
                 from ./include/linux/topology.h:30,
                 from ./include/linux/gfp.h:9,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/gfp.h:3,
                 from ./include/linux/xarray.h:14,
                 from ./include/linux/radix-tree.h:18,
                 from ./include/linux/idr.h:15,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/idr.h:5,
                 from ./include/linux/kernfs.h:13,
                 from ./include/linux/sysfs.h:16,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/sysfs.h:3,
                 from ./include/linux/kobject.h:20,
                 from ./include/linux/pci.h:35,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/pci.h:3,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/sa2400.c:19:
./include/asm-generic/iomap.h:29:29: note: expected 'void *' but argument is of type 'const u8 *' {aka 'const unsigned char *'}
 extern unsigned int ioread8(void __iomem *);
                             ^~~~~~~~~~~~~~
In file included from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/sa2400.c:23:
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h: In function 'rtl818x_ioread16':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h:160:18: warning: passing argument 1 of 'ioread16' discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  return ioread16(addr);
                  ^~~~
In file included from ./arch/x86/include/asm/io.h:229,
                 from ./arch/x86/include/asm/realmode.h:15,
                 from ./arch/x86/include/asm/acpi.h:16,
                 from ./arch/x86/include/asm/fixmap.h:29,
                 from ./arch/x86/include/asm/apic.h:11,
                 from ./arch/x86/include/asm/smp.h:13,
                 from ./include/linux/smp.h:68,
                 from ./include/linux/percpu.h:7,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/percpu.h:6,
                 from ./include/linux/arch_topology.h:9,
                 from ./include/linux/topology.h:30,
                 from ./include/linux/gfp.h:9,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/gfp.h:3,
                 from ./include/linux/xarray.h:14,
                 from ./include/linux/radix-tree.h:18,
                 from ./include/linux/idr.h:15,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/idr.h:5,
                 from ./include/linux/kernfs.h:13,
                 from ./include/linux/sysfs.h:16,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/sysfs.h:3,
                 from ./include/linux/kobject.h:20,
                 from ./include/linux/pci.h:35,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/pci.h:3,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/sa2400.c:19:
./include/asm-generic/iomap.h:30:30: note: expected 'void *' but argument is of type 'const __le16 *' {aka 'const short unsigned int *'}
 extern unsigned int ioread16(void __iomem *);
                              ^~~~~~~~~~~~~~
In file included from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/sa2400.c:23:
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h: In function 'rtl818x_ioread32':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h:165:18: warning: passing argument 1 of 'ioread32' discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  return ioread32(addr);
                  ^~~~
In file included from ./arch/x86/include/asm/io.h:229,
                 from ./arch/x86/include/asm/realmode.h:15,
                 from ./arch/x86/include/asm/acpi.h:16,
                 from ./arch/x86/include/asm/fixmap.h:29,
                 from ./arch/x86/include/asm/apic.h:11,
                 from ./arch/x86/include/asm/smp.h:13,
                 from ./include/linux/smp.h:68,
                 from ./include/linux/percpu.h:7,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/percpu.h:6,
                 from ./include/linux/arch_topology.h:9,
                 from ./include/linux/topology.h:30,
                 from ./include/linux/gfp.h:9,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/gfp.h:3,
                 from ./include/linux/xarray.h:14,
                 from ./include/linux/radix-tree.h:18,
                 from ./include/linux/idr.h:15,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/idr.h:5,
                 from ./include/linux/kernfs.h:13,
                 from ./include/linux/sysfs.h:16,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/sysfs.h:3,
                 from ./include/linux/kobject.h:20,
                 from ./include/linux/pci.h:35,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/pci.h:3,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/sa2400.c:19:
./include/asm-generic/iomap.h:32:30: note: expected 'void *' but argument is of type 'const __le32 *' {aka 'const unsigned int *'}
 extern unsigned int ioread32(void __iomem *);
                              ^~~~~~~~~~~~~~
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/max2820.o
In file included from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/max2820.c:22:
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h: In function 'rtl818x_ioread8':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h:155:17: warning: passing argument 1 of 'ioread8' discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  return ioread8(addr);
                 ^~~~
In file included from ./arch/x86/include/asm/io.h:229,
                 from ./arch/x86/include/asm/realmode.h:15,
                 from ./arch/x86/include/asm/acpi.h:16,
                 from ./arch/x86/include/asm/fixmap.h:29,
                 from ./arch/x86/include/asm/apic.h:11,
                 from ./arch/x86/include/asm/smp.h:13,
                 from ./include/linux/smp.h:68,
                 from ./include/linux/percpu.h:7,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/percpu.h:6,
                 from ./include/linux/arch_topology.h:9,
                 from ./include/linux/topology.h:30,
                 from ./include/linux/gfp.h:9,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/gfp.h:3,
                 from ./include/linux/xarray.h:14,
                 from ./include/linux/radix-tree.h:18,
                 from ./include/linux/idr.h:15,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/idr.h:5,
                 from ./include/linux/kernfs.h:13,
                 from ./include/linux/sysfs.h:16,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/sysfs.h:3,
                 from ./include/linux/kobject.h:20,
                 from ./include/linux/pci.h:35,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/pci.h:3,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/max2820.c:18:
./include/asm-generic/iomap.h:29:29: note: expected 'void *' but argument is of type 'const u8 *' {aka 'const unsigned char *'}
 extern unsigned int ioread8(void __iomem *);
                             ^~~~~~~~~~~~~~
In file included from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/max2820.c:22:
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h: In function 'rtl818x_ioread16':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h:160:18: warning: passing argument 1 of 'ioread16' discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  return ioread16(addr);
                  ^~~~
In file included from ./arch/x86/include/asm/io.h:229,
                 from ./arch/x86/include/asm/realmode.h:15,
                 from ./arch/x86/include/asm/acpi.h:16,
                 from ./arch/x86/include/asm/fixmap.h:29,
                 from ./arch/x86/include/asm/apic.h:11,
                 from ./arch/x86/include/asm/smp.h:13,
                 from ./include/linux/smp.h:68,
                 from ./include/linux/percpu.h:7,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/percpu.h:6,
                 from ./include/linux/arch_topology.h:9,
                 from ./include/linux/topology.h:30,
                 from ./include/linux/gfp.h:9,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/gfp.h:3,
                 from ./include/linux/xarray.h:14,
                 from ./include/linux/radix-tree.h:18,
                 from ./include/linux/idr.h:15,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/idr.h:5,
                 from ./include/linux/kernfs.h:13,
                 from ./include/linux/sysfs.h:16,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/sysfs.h:3,
                 from ./include/linux/kobject.h:20,
                 from ./include/linux/pci.h:35,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/pci.h:3,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/max2820.c:18:
./include/asm-generic/iomap.h:30:30: note: expected 'void *' but argument is of type 'const __le16 *' {aka 'const short unsigned int *'}
 extern unsigned int ioread16(void __iomem *);
                              ^~~~~~~~~~~~~~
In file included from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/max2820.c:22:
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h: In function 'rtl818x_ioread32':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h:165:18: warning: passing argument 1 of 'ioread32' discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  return ioread32(addr);
                  ^~~~
In file included from ./arch/x86/include/asm/io.h:229,
                 from ./arch/x86/include/asm/realmode.h:15,
                 from ./arch/x86/include/asm/acpi.h:16,
                 from ./arch/x86/include/asm/fixmap.h:29,
                 from ./arch/x86/include/asm/apic.h:11,
                 from ./arch/x86/include/asm/smp.h:13,
                 from ./include/linux/smp.h:68,
                 from ./include/linux/percpu.h:7,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/percpu.h:6,
                 from ./include/linux/arch_topology.h:9,
                 from ./include/linux/topology.h:30,
                 from ./include/linux/gfp.h:9,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/gfp.h:3,
                 from ./include/linux/xarray.h:14,
                 from ./include/linux/radix-tree.h:18,
                 from ./include/linux/idr.h:15,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/idr.h:5,
                 from ./include/linux/kernfs.h:13,
                 from ./include/linux/sysfs.h:16,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/sysfs.h:3,
                 from ./include/linux/kobject.h:20,
                 from ./include/linux/pci.h:35,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/pci.h:3,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/max2820.c:18:
./include/asm-generic/iomap.h:32:30: note: expected 'void *' but argument is of type 'const __le32 *' {aka 'const unsigned int *'}
 extern unsigned int ioread32(void __iomem *);
                              ^~~~~~~~~~~~~~
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/grf5101.o
In file included from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/grf5101.c:23:
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h: In function 'rtl818x_ioread8':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h:155:17: warning: passing argument 1 of 'ioread8' discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  return ioread8(addr);
                 ^~~~
In file included from ./arch/x86/include/asm/io.h:229,
                 from ./arch/x86/include/asm/realmode.h:15,
                 from ./arch/x86/include/asm/acpi.h:16,
                 from ./arch/x86/include/asm/fixmap.h:29,
                 from ./arch/x86/include/asm/apic.h:11,
                 from ./arch/x86/include/asm/smp.h:13,
                 from ./include/linux/smp.h:68,
                 from ./include/linux/percpu.h:7,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/percpu.h:6,
                 from ./include/linux/arch_topology.h:9,
                 from ./include/linux/topology.h:30,
                 from ./include/linux/gfp.h:9,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/gfp.h:3,
                 from ./include/linux/xarray.h:14,
                 from ./include/linux/radix-tree.h:18,
                 from ./include/linux/idr.h:15,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/idr.h:5,
                 from ./include/linux/kernfs.h:13,
                 from ./include/linux/sysfs.h:16,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/sysfs.h:3,
                 from ./include/linux/kobject.h:20,
                 from ./include/linux/pci.h:35,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/pci.h:3,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/grf5101.c:19:
./include/asm-generic/iomap.h:29:29: note: expected 'void *' but argument is of type 'const u8 *' {aka 'const unsigned char *'}
 extern unsigned int ioread8(void __iomem *);
                             ^~~~~~~~~~~~~~
In file included from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/grf5101.c:23:
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h: In function 'rtl818x_ioread16':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h:160:18: warning: passing argument 1 of 'ioread16' discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  return ioread16(addr);
                  ^~~~
In file included from ./arch/x86/include/asm/io.h:229,
                 from ./arch/x86/include/asm/realmode.h:15,
                 from ./arch/x86/include/asm/acpi.h:16,
                 from ./arch/x86/include/asm/fixmap.h:29,
                 from ./arch/x86/include/asm/apic.h:11,
                 from ./arch/x86/include/asm/smp.h:13,
                 from ./include/linux/smp.h:68,
                 from ./include/linux/percpu.h:7,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/percpu.h:6,
                 from ./include/linux/arch_topology.h:9,
                 from ./include/linux/topology.h:30,
                 from ./include/linux/gfp.h:9,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/gfp.h:3,
                 from ./include/linux/xarray.h:14,
                 from ./include/linux/radix-tree.h:18,
                 from ./include/linux/idr.h:15,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/idr.h:5,
                 from ./include/linux/kernfs.h:13,
                 from ./include/linux/sysfs.h:16,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/sysfs.h:3,
                 from ./include/linux/kobject.h:20,
                 from ./include/linux/pci.h:35,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/pci.h:3,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/grf5101.c:19:
./include/asm-generic/iomap.h:30:30: note: expected 'void *' but argument is of type 'const __le16 *' {aka 'const short unsigned int *'}
 extern unsigned int ioread16(void __iomem *);
                              ^~~~~~~~~~~~~~
In file included from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/grf5101.c:23:
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h: In function 'rtl818x_ioread32':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h:165:18: warning: passing argument 1 of 'ioread32' discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  return ioread32(addr);
                  ^~~~
In file included from ./arch/x86/include/asm/io.h:229,
                 from ./arch/x86/include/asm/realmode.h:15,
                 from ./arch/x86/include/asm/acpi.h:16,
                 from ./arch/x86/include/asm/fixmap.h:29,
                 from ./arch/x86/include/asm/apic.h:11,
                 from ./arch/x86/include/asm/smp.h:13,
                 from ./include/linux/smp.h:68,
                 from ./include/linux/percpu.h:7,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/percpu.h:6,
                 from ./include/linux/arch_topology.h:9,
                 from ./include/linux/topology.h:30,
                 from ./include/linux/gfp.h:9,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/gfp.h:3,
                 from ./include/linux/xarray.h:14,
                 from ./include/linux/radix-tree.h:18,
                 from ./include/linux/idr.h:15,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/idr.h:5,
                 from ./include/linux/kernfs.h:13,
                 from ./include/linux/sysfs.h:16,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/sysfs.h:3,
                 from ./include/linux/kobject.h:20,
                 from ./include/linux/pci.h:35,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/pci.h:3,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/grf5101.c:19:
./include/asm-generic/iomap.h:32:30: note: expected 'void *' but argument is of type 'const __le32 *' {aka 'const unsigned int *'}
 extern unsigned int ioread32(void __iomem *);
                              ^~~~~~~~~~~~~~
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8225se.o
In file included from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8225se.c:18:
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h: In function 'rtl818x_ioread8':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h:155:17: warning: passing argument 1 of 'ioread8' discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  return ioread8(addr);
                 ^~~~
In file included from ./arch/x86/include/asm/io.h:229,
                 from ./arch/x86/include/asm/realmode.h:15,
                 from ./arch/x86/include/asm/acpi.h:16,
                 from ./arch/x86/include/asm/fixmap.h:29,
                 from ./arch/x86/include/asm/apic.h:11,
                 from ./arch/x86/include/asm/smp.h:13,
                 from ./include/linux/smp.h:68,
                 from ./include/linux/percpu.h:7,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/percpu.h:6,
                 from ./include/linux/arch_topology.h:9,
                 from ./include/linux/topology.h:30,
                 from ./include/linux/gfp.h:9,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/gfp.h:3,
                 from ./include/linux/mm.h:10,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/mm.h:3,
                 from ./include/linux/bvec.h:13,
                 from ./include/linux/skbuff.h:17,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/skbuff.h:3,
                 from ./include/linux/if_ether.h:19,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/if_ether.h:3,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/include/net/mac80211.h:18,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8225se.c:16:
./include/asm-generic/iomap.h:29:29: note: expected 'void *' but argument is of type 'const u8 *' {aka 'const unsigned char *'}
 extern unsigned int ioread8(void __iomem *);
                             ^~~~~~~~~~~~~~
In file included from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8225se.c:18:
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h: In function 'rtl818x_ioread16':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h:160:18: warning: passing argument 1 of 'ioread16' discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  return ioread16(addr);
                  ^~~~
In file included from ./arch/x86/include/asm/io.h:229,
                 from ./arch/x86/include/asm/realmode.h:15,
                 from ./arch/x86/include/asm/acpi.h:16,
                 from ./arch/x86/include/asm/fixmap.h:29,
                 from ./arch/x86/include/asm/apic.h:11,
                 from ./arch/x86/include/asm/smp.h:13,
                 from ./include/linux/smp.h:68,
                 from ./include/linux/percpu.h:7,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/percpu.h:6,
                 from ./include/linux/arch_topology.h:9,
                 from ./include/linux/topology.h:30,
                 from ./include/linux/gfp.h:9,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/gfp.h:3,
                 from ./include/linux/mm.h:10,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/mm.h:3,
                 from ./include/linux/bvec.h:13,
                 from ./include/linux/skbuff.h:17,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/skbuff.h:3,
                 from ./include/linux/if_ether.h:19,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/if_ether.h:3,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/include/net/mac80211.h:18,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8225se.c:16:
./include/asm-generic/iomap.h:30:30: note: expected 'void *' but argument is of type 'const __le16 *' {aka 'const short unsigned int *'}
 extern unsigned int ioread16(void __iomem *);
                              ^~~~~~~~~~~~~~
In file included from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8225se.c:18:
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h: In function 'rtl818x_ioread32':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8180.h:165:18: warning: passing argument 1 of 'ioread32' discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  return ioread32(addr);
                  ^~~~
In file included from ./arch/x86/include/asm/io.h:229,
                 from ./arch/x86/include/asm/realmode.h:15,
                 from ./arch/x86/include/asm/acpi.h:16,
                 from ./arch/x86/include/asm/fixmap.h:29,
                 from ./arch/x86/include/asm/apic.h:11,
                 from ./arch/x86/include/asm/smp.h:13,
                 from ./include/linux/smp.h:68,
                 from ./include/linux/percpu.h:7,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/percpu.h:6,
                 from ./include/linux/arch_topology.h:9,
                 from ./include/linux/topology.h:30,
                 from ./include/linux/gfp.h:9,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/gfp.h:3,
                 from ./include/linux/mm.h:10,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/mm.h:3,
                 from ./include/linux/bvec.h:13,
                 from ./include/linux/skbuff.h:17,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/skbuff.h:3,
                 from ./include/linux/if_ether.h:19,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/backport-include/linux/if_ether.h:3,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/include/net/mac80211.h:18,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl8225se.c:16:
./include/asm-generic/iomap.h:32:30: note: expected 'void *' but argument is of type 'const __le32 *' {aka 'const unsigned int *'}
 extern unsigned int ioread32(void __iomem *);
                              ^~~~~~~~~~~~~~
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl818x_pci.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8187/dev.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8187/rtl8225.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8187/leds.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8187/rfkill.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8187/rtl8187.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl8xxxu/rtl8xxxu_core.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl8xxxu/rtl8xxxu_8192e.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl8xxxu/rtl8xxxu_8723b.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl8xxxu/rtl8xxxu_8723a.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl8xxxu/rtl8xxxu_8192c.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl8xxxu/rtl8xxxu.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/btcoexist/halbtc8192e2ant.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/btcoexist/halbtc8723b1ant.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/btcoexist/halbtc8723b2ant.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/btcoexist/halbtc8821a1ant.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/btcoexist/halbtc8821a2ant.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/btcoexist/halbtcoutsrc.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/btcoexist/rtl_btc.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/btcoexist/btcoexist.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192c/main.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192c/dm_common.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192c/fw_common.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192c/phy_common.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192c/rtl8192c-common.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192ce/dm.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192ce/hw.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192ce/led.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192ce/phy.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192ce/rf.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192ce/sw.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192ce/table.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192ce/trx.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192ce/rtl8192ce.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192cu/dm.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192cu/hw.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192cu/led.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192cu/mac.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192cu/phy.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192cu/rf.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192cu/sw.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192cu/table.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192cu/trx.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192cu/rtl8192cu.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192de/dm.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192de/fw.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192de/hw.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192de/led.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192de/phy.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192de/rf.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192de/sw.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192de/table.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192de/trx.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192de/rtl8192de.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192se/dm.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192se/fw.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192se/hw.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192se/led.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192se/phy.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192se/rf.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192se/sw.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192se/table.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192se/trx.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192se/rtl8192se.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8821ae/dm.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8821ae/fw.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8821ae/hw.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8821ae/led.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8821ae/phy.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8821ae/pwrseq.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8821ae/rf.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8821ae/sw.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8821ae/table.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8821ae/trx.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8821ae/rtl8821ae.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/base.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/cam.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/core.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/debug.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/efuse.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/ps.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rc.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/regd.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/stats.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/pci.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/usb.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtlwifi.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl_pci.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl_usb.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/main.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/mac80211.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/util.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/debug.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/tx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/mac.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/phy.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/coex.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/efuse.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/fw.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/ps.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/sec.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/bf.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/wow.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/regd.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw8822b.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw8822b_table.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw8822be.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw8822c.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw8822c_table.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw8822ce.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw8723d.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw8723d_table.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw8723de.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/pci.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw88_core.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw88_8822b.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw88_8822be.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw88_8822c.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw88_8822ce.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw88_8723d.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw88_8723de.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw88_pci.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/rsi/rsi_91x_main.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/rsi/rsi_91x_core.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/rsi/rsi_91x_mac80211.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/rsi/rsi_91x_mgmt.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/rsi/rsi_91x_hal.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/rsi/rsi_91x_ps.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/rsi/rsi_91x_sdio.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/rsi/rsi_91x_sdio_ops.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/rsi/rsi_91x_usb.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/rsi/rsi_91x_usb_ops.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/rsi/rsi_91x.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/rsi/rsi_sdio.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/rsi/rsi_usb.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wl12xx/main.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wl12xx/cmd.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wl12xx/acx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wl12xx/debugfs.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wl12xx/scan.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wl18xx/main.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wl12xx/event.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wl12xx/wl12xx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wl18xx/acx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wlcore/main.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wl18xx/tx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wl18xx/io.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wl18xx/debugfs.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wlcore/cmd.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wl18xx/scan.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wlcore/io.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wl18xx/cmd.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wlcore/event.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wl18xx/event.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wlcore/tx.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wl18xx/wl18xx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wlcore/rx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wlcore/ps.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wlcore/acx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wlcore/boot.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wlcore/init.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wlcore/debugfs.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wlcore/scan.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wlcore/sysfs.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wlcore/vendor_cmd.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wlcore/sdio.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wlcore/wlcore.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wlcore/wlcore_sdio.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/zydas/zd1211rw/zd_chip.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/zydas/zd1211rw/zd_mac.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/zydas/zd1211rw/zd_rf_al2230.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/zydas/zd1211rw/zd_rf_rf2959.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/zydas/zd1211rw/zd_rf_al7230b.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/zydas/zd1211rw/zd_rf_uw2453.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/core/rtw_ap.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/zydas/zd1211rw/zd_rf.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/core/rtw_btcoex.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/zydas/zd1211rw/zd_usb.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/core/rtw_cmd.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/zydas/zd1211rw/zd1211rw.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/mac80211_hwsim.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/core/rtw_debug.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/core/rtw_efuse.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/core/rtw_io.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/core/rtw_ioctl_set.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/core/rtw_ieee80211.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/core/rtw_mlme.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/main.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/core/rtw_mlme_ext.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/status.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/driver-ops.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/core/rtw_odm.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/sta_info.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/core/rtw_pwrctrl.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/core/rtw_recv.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/wep.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/core/rtw_rf.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/wpa.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/core/rtw_security.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/scan.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/core/rtw_sta_mgt.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/core/rtw_wlan_util.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/offchannel.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/ht.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/core/rtw_xmit.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/agg-tx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/hal_intf.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/hal_com.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/agg-rx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/hal_com_phycfg.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/vht.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/he.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/hal_btcoex.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/s1g.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/hal_sdio.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/ibss.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/hal_pwr_seq.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/HalPhyRf.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/iface.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/HalPwrSeqCmd.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/odm.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/odm_CfoTracking.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/rate.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/odm_debug.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/michael.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/tkip.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/odm_DIG.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/odm_DynamicBBPowerSaving.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/aes_ccm.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/odm_DynamicTxPower.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/aes_cmac.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/odm_EdcaTurboCheck.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/fils_aead.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/cfg.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/odm_HWConfig.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/odm_NoiseMonitor.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/odm_PathDiv.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/ethtool.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/odm_RegConfig8723B.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/odm_RTL8723B.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/rx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/rtl8723b_cmd.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/rtl8723b_dm.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/rtl8723b_hal_init.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/spectmgmt.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/tx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/rtl8723b_phycfg.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/rtl8723b_rf6052.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/rtl8723b_rxdesc.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/rtl8723bs_recv.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/key.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/rtl8723bs_xmit.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/sdio_halinit.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/util.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/sdio_ops.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/HalBtc8723b1Ant.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/wme.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/HalBtc8723b2Ant.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/chan.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/HalHWImg8723B_BB.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/HalHWImg8723B_MAC.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/trace.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/HalHWImg8723B_RF.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/mlme.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/hal/HalPhyRf_8723B.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/os_dep/ioctl_cfg80211.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/tdls.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/os_dep/ioctl_linux.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/ocb.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/os_dep/mlme_linux.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/airtime.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/os_dep/osdep_service.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/os_dep/os_intfs.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/led.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/os_dep/recv_linux.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/debugfs.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/os_dep/sdio_intf.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/debugfs_sta.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/os_dep/sdio_ops_linux.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/os_dep/wifi_regd.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/debugfs_netdev.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/os_dep/xmit_linux.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/r8723bs.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/core.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/debugfs_key.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/sysfs.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/mesh.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/radiotap.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/util.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/mesh_pathtbl.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/mesh_plink.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/reg.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/mesh_hwmp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/scan.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/mesh_sync.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/mesh_ps.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/nl80211.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/pm.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/rc80211_minstrel_ht.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/rc80211_minstrel_ht_debugfs.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/mac80211.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/mlme.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/ibss.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/sme.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/chan.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/ethtool.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/mesh.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/ap.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/trace.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/ocb.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/pmsr.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/debugfs.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/wext-compat.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/wext-sme.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/lib80211.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/lib80211_crypt_wep.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/lib80211_crypt_ccmp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/lib80211_crypt_tkip.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/cfg80211.o
  Building modules, stage 2.
  MODPOST 97 modules
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/compat/compat.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/admtek/adm8211.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ar5523/ar5523.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath10k/ath10k_core.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath10k/ath10k_pci.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath5k/ath5k.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath6kl/ath6kl_core.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath6kl/ath6kl_sdio.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath6kl/ath6kl_usb.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/ath9k.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/ath9k_common.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/ath9k_htc.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/ath9k_hw.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/ath9k_pci_owl_loader.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/carl9170/carl9170.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/wil6210/wil6210.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43/b43.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43legacy/b43legacy.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmfmac/brcmfmac.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmsmac/brcmsmac.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmutil/brcmutil.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/ipw2x00/ipw2100.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/ipw2x00/ipw2200.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/ipw2x00/libipw.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlegacy/iwl3945.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlegacy/iwl4965.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlegacy/iwlegacy.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/dvm/iwldvm.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/iwlwifi.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/mvm/iwlmvm.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/orinoco/orinoco.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/orinoco/orinoco_cs.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/orinoco/orinoco_pci.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/orinoco/orinoco_plx.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/p54/p54common.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/p54/p54pci.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/p54/p54usb.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/mac80211_hwsim.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/libertas/libertas.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/libertas/libertas_sdio.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/libertas/libertas_spi.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/libertas/usb8xxx.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/mwifiex.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/mwifiex_pcie.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/mwifiex_sdio.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwl8k.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/mediatek/mt7601u/mt7601u.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2400pci.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2500pci.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2500usb.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2800lib.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2800mmio.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2800pci.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2800usb.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2x00lib.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2x00mmio.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2x00pci.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2x00usb.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt61pci.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt73usb.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl818x_pci.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8187/rtl8187.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl8xxxu/rtl8xxxu.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/btcoexist/btcoexist.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192c/rtl8192c-common.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192ce/rtl8192ce.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192cu/rtl8192cu.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192de/rtl8192de.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192se/rtl8192se.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8821ae/rtl8821ae.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl_pci.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl_usb.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtlwifi.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw88_8723d.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw88_8723de.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw88_8822b.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw88_8822be.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw88_8822c.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw88_8822ce.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw88_core.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw88_pci.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/rsi/rsi_91x.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/rsi/rsi_sdio.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/rsi/rsi_usb.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wl12xx/wl12xx.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wl18xx/wl18xx.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wlcore/wlcore.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wlcore/wlcore_sdio.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/zydas/zd1211rw/zd1211rw.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/r8723bs.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/mac80211.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/cfg80211.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/lib80211.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/lib80211_crypt_ccmp.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/lib80211_crypt_tkip.mod.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/lib80211_crypt_wep.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/compat/compat.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/admtek/adm8211.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ar5523/ar5523.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath10k/ath10k_core.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath10k/ath10k_pci.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath5k/ath5k.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath6kl/ath6kl_core.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath6kl/ath6kl_sdio.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath6kl/ath6kl_usb.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/ath9k.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/ath9k_common.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/ath9k_htc.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/ath9k_hw.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/ath9k/ath9k_pci_owl_loader.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/carl9170/carl9170.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ath/wil6210/wil6210.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43/b43.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/b43legacy/b43legacy.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmfmac/brcmfmac.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmsmac/brcmsmac.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/broadcom/brcm80211/brcmutil/brcmutil.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/ipw2x00/ipw2100.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/ipw2x00/ipw2200.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/ipw2x00/libipw.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlegacy/iwl3945.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlegacy/iwl4965.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlegacy/iwlegacy.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/dvm/iwldvm.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/iwlwifi.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intel/iwlwifi/mvm/iwlmvm.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/orinoco/orinoco.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/orinoco/orinoco_cs.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/orinoco/orinoco_pci.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/orinoco/orinoco_plx.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/p54/p54common.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/p54/p54pci.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/intersil/p54/p54usb.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/mac80211_hwsim.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/libertas/libertas.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/libertas/libertas_sdio.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/libertas/libertas_spi.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/libertas/usb8xxx.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/mwifiex.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/mwifiex_pcie.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwifiex/mwifiex_sdio.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/marvell/mwl8k.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/mediatek/mt7601u/mt7601u.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2400pci.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2500pci.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2500usb.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2800lib.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2800mmio.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2800pci.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2800usb.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2x00lib.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2x00mmio.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2x00pci.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt2x00usb.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt61pci.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ralink/rt2x00/rt73usb.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8180/rtl818x_pci.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl818x/rtl8187/rtl8187.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtl8xxxu/rtl8xxxu.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/btcoexist/btcoexist.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192c/rtl8192c-common.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192ce/rtl8192ce.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192cu/rtl8192cu.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192de/rtl8192de.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8192se/rtl8192se.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl8821ae/rtl8821ae.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl_pci.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtl_usb.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtlwifi/rtlwifi.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw88_8723d.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw88_8723de.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw88_8822b.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw88_8822be.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw88_8822c.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw88_8822ce.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw88_core.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/realtek/rtw88/rtw88_pci.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/rsi/rsi_91x.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/rsi/rsi_sdio.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/rsi/rsi_usb.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wl12xx/wl12xx.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wl18xx/wl18xx.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wlcore/wlcore.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/ti/wlcore/wlcore_sdio.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/net/wireless/zydas/zd1211rw/zd1211rw.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/drivers/staging/rtl8723bs/r8723bs.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/mac80211/mac80211.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/cfg80211.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/lib80211.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/lib80211_crypt_ccmp.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/lib80211_crypt_tkip.ko
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/net/wireless/lib80211_crypt_wep.ko
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1'
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/ipkg-x86_64/kmod-cfg80211/lib/modules/5.4.121/compat.ko: relocatable
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/ipkg-x86_64/kmod-cfg80211/lib/modules/5.4.121/cfg80211.ko: relocatable
Packaged contents of /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/ipkg-x86_64/kmod-cfg80211 into /openwrt/bin/targets/x86/64/packages/kmod-cfg80211_5.4.121+5.10.34-1-1_x86_64.ipk
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/ipkg-x86_64/kmod-mac80211/lib/modules/5.4.121/mac80211.ko: relocatable
Packaged contents of /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-5.10.34-1/ipkg-x86_64/kmod-mac80211 into /openwrt/bin/targets/x86/64/packages/kmod-mac80211_5.4.121+5.10.34-1-1_x86_64.ipk
Package kmod-adm8211 is missing dependencies for the following libraries:
eeprom_93cx6.ko
make[3]: *** [Makefile:565: /openwrt/bin/targets/x86/64/packages/kmod-adm8211_5.4.121+5.10.34-1-1_x86_64.ipk] Error 1
```
