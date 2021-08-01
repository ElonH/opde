---
title: "compile.22"
date: 2021-05-26 12:53:22.898284
hidden: false
draft: false
weight: -22
---

build number: `22`

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

Applying ./patches/build/100-backports-pci-Include-linux-pci-aspm.h.patch using plaintext: 
patching file backport-include/linux/pci.h

Applying ./patches/build/101-backport-add-pci_disable_link_state-wrapper-with-ret.patch using plaintext: 
patching file backport-include/linux/pci.h

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

Applying ./patches/subsys/140-tweak-TSQ-setting.patch using plaintext: 
patching file net/mac80211/tx.c

Applying ./patches/subsys/150-disable_addr_notifier.patch using plaintext: 
patching file net/mac80211/main.c

Applying ./patches/subsys/210-ap_scan.patch using plaintext: 
patching file net/mac80211/cfg.c

Applying ./patches/subsys/300-mac80211-add-stop-start-logic-for-software-TXQs.patch using plaintext: 
patching file include/net/mac80211.h
patching file net/mac80211/ieee80211_i.h
patching file net/mac80211/main.c
patching file net/mac80211/tx.c
patching file net/mac80211/util.c

Applying ./patches/subsys/303-mac80211-minstrel-Enable-STBC-and-LDPC-for-VHT-Rates.patch using plaintext: 
patching file include/linux/ieee80211.h
patching file net/mac80211/rc80211_minstrel_ht.c

Applying ./patches/subsys/304-mac80211-minstrel-remove-unnecessary-debugfs-cleanup.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel.c
patching file net/mac80211/rc80211_minstrel.h
patching file net/mac80211/rc80211_minstrel_debugfs.c
patching file net/mac80211/rc80211_minstrel_ht.c
patching file net/mac80211/rc80211_minstrel_ht.h
patching file net/mac80211/rc80211_minstrel_ht_debugfs.c

Applying ./patches/subsys/305-mac80211-fix-tx-status-for-no-ack-cases.patch using plaintext: 
patching file net/mac80211/status.c

Applying ./patches/subsys/305-mac80211-minstrel-merge-with-minstrel_ht-always-enab.patch using plaintext: 
patching file net/mac80211/Kconfig
patching file net/mac80211/Makefile
patching file net/mac80211/main.c
patching file net/mac80211/rate.h
patching file net/mac80211/rc80211_minstrel.c
patching file net/mac80211/rc80211_minstrel.h
patching file net/mac80211/rc80211_minstrel_debugfs.c
patching file net/mac80211/rc80211_minstrel_ht.c
patching file net/mac80211/rc80211_minstrel_ht.h
patching file net/mac80211/rc80211_minstrel_ht_debugfs.c

Applying ./patches/subsys/306-mac80211-minstrel-reduce-minstrel_mcs_groups-size.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c
patching file net/mac80211/rc80211_minstrel_ht.h
patching file net/mac80211/rc80211_minstrel_ht_debugfs.c

Applying ./patches/subsys/310-mac80211-minstrel-do-not-sample-rates-3-times-slower.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c

Applying ./patches/subsys/312-mac80211-minstrel_ht-add-flag-to-indicate-missing-in.patch using plaintext: 
patching file include/net/mac80211.h
patching file net/mac80211/debugfs.c
patching file net/mac80211/rc80211_minstrel_ht.c
patching file net/mac80211/rc80211_minstrel_ht_debugfs.c

Applying ./patches/subsys/314-mac80211-minstrel_ht-reduce-unnecessary-rate-probing.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c

Applying ./patches/subsys/315-mac80211-minstrel_ht-fix-default-max-throughput-rate.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c

Applying ./patches/subsys/316-mac80211-minstrel_ht-improve-rate-probing-for-device.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel.h
patching file net/mac80211/rc80211_minstrel_ht.c
patching file net/mac80211/rc80211_minstrel_ht.h

Applying ./patches/subsys/317-mac80211-minstrel_ht-fix-infinite-loop-because-suppo.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c

Applying ./patches/subsys/320-mac80211-Add-TXQ-scheduling-API.patch using plaintext: 
patching file include/net/mac80211.h
patching file net/mac80211/agg-tx.c
patching file net/mac80211/driver-ops.h
patching file net/mac80211/ieee80211_i.h
patching file net/mac80211/main.c
patching file net/mac80211/sta_info.c
patching file net/mac80211/tx.c

Applying ./patches/subsys/321-cfg80211-Add-airtime-statistics-and-settings.patch using plaintext: 
patching file include/net/cfg80211.h
patching file include/uapi/linux/nl80211.h
patching file net/wireless/nl80211.c

Applying ./patches/subsys/322-mac80211-Add-airtime-accounting-and-scheduling-to-TX.patch using plaintext: 
patching file include/net/mac80211.h
patching file net/mac80211/cfg.c
patching file net/mac80211/debugfs.c
patching file net/mac80211/debugfs_sta.c
patching file net/mac80211/ieee80211_i.h
patching file net/mac80211/main.c
patching file net/mac80211/sta_info.c
patching file net/mac80211/sta_info.h
patching file net/mac80211/status.c
patching file net/mac80211/tx.c

Applying ./patches/subsys/323-mac80211-Expose-ieee80211_schedule_txq-function.patch using plaintext: 
patching file include/net/mac80211.h
patching file net/mac80211/driver-ops.h
patching file net/mac80211/tx.c

Applying ./patches/subsys/350-mac80211-add-hdrlen-to-ieee80211_tx_data.patch using plaintext: 
patching file net/mac80211/ieee80211_i.h
patching file net/mac80211/tx.c
patching file net/mac80211/util.c
patching file net/mac80211/wep.c
patching file net/mac80211/wep.h
patching file net/mac80211/wpa.c

Applying ./patches/subsys/351-mac80211-add-TX_NEEDS_ALIGNED4_SKBS-hw-flag.patch using plaintext: 
patching file include/net/mac80211.h
patching file net/mac80211/iface.c
patching file net/mac80211/mesh_pathtbl.c
patching file net/mac80211/rx.c
patching file net/mac80211/sta_info.h
patching file net/mac80211/status.c
patching file net/mac80211/tkip.c
patching file net/mac80211/tx.c
patching file net/mac80211/debugfs.c

Applying ./patches/subsys/352-mac80211-rework-locking-for-txq-scheduling-airtime-f.patch using plaintext: 
patching file include/net/mac80211.h
patching file net/mac80211/tx.c

Applying ./patches/subsys/353-mac80211-mesh-drop-redundant-rcu_read_lock-unlock-ca.patch using plaintext: 
patching file net/mac80211/mesh_hwmp.c
patching file net/mac80211/mesh_pathtbl.c

Applying ./patches/subsys/354-mac80211-calculate-hash-for-fq-without-holding-fq-lo.patch using plaintext: 
patching file include/net/fq_impl.h
patching file net/mac80211/tx.c

Applying ./patches/subsys/355-mac80211-run-late-dequeue-late-tx-handlers-without-h.patch using plaintext: 
patching file net/mac80211/tx.c

Applying ./patches/subsys/356-mac80211-set-NETIF_F_LLTX-when-using-intermediate-tx.patch using plaintext: 
patching file net/mac80211/iface.c

Applying ./patches/subsys/358-mac80211-make-ieee80211_schedule_txq-schedule-empty-.patch using plaintext: 
patching file include/net/mac80211.h
patching file net/mac80211/tx.c

Applying ./patches/subsys/359-mac80211-un-schedule-TXQs-on-powersave-start.patch using plaintext: 
patching file net/mac80211/rx.c

Applying ./patches/subsys/360-mac80211-when-using-iTXQ-select-the-queue-in-ieee802.patch using plaintext: 
patching file net/mac80211/tx.c
patching file net/mac80211/wme.c
patching file net/mac80211/wme.h

Applying ./patches/subsys/361-mac80211-add-IEEE80211_KEY_FLAG_GENERATE_MMIE-to-iee.patch using plaintext: 
patching file include/net/mac80211.h
patching file net/mac80211/wpa.c

Applying ./patches/subsys/362-mac80211-minstrel-remove-divisions-in-tx-status-path.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel.c
patching file net/mac80211/rc80211_minstrel_ht.c

Applying ./patches/subsys/363-mac80211-minstrel_ht-replace-rate-stats-ewma-with-a-.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel.c
patching file net/mac80211/rc80211_minstrel.h
patching file net/mac80211/rc80211_minstrel_ht.c

Applying ./patches/subsys/364-mac80211-minstrel_ht-rename-prob_ewma-to-prob_avg-us.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel.c
patching file net/mac80211/rc80211_minstrel.h
patching file net/mac80211/rc80211_minstrel_debugfs.c
patching file net/mac80211/rc80211_minstrel_ht.c
patching file net/mac80211/rc80211_minstrel_ht.h
patching file net/mac80211/rc80211_minstrel_ht_debugfs.c

Applying ./patches/subsys/365-mac80211-IBSS-send-deauth-when-expiring-inactive-STA.patch using plaintext: 
patching file net/mac80211/ibss.c
patching file net/mac80211/ieee80211_i.h
patching file net/mac80211/mlme.c
patching file net/mac80211/util.c

Applying ./patches/subsys/367-mac80211-sta-randomize-BA-session-dialog-token-alloc.patch using plaintext: 
patching file net/mac80211/sta_info.c

Applying ./patches/subsys/368-cfg80211-add-local-BSS-receive-time-to-survey-inform.patch using plaintext: 
patching file include/net/cfg80211.h
patching file include/uapi/linux/nl80211.h
patching file net/wireless/nl80211.c

Applying ./patches/subsys/522-mac80211_configure_antenna_gain.patch using plaintext: 
patching file include/net/cfg80211.h
patching file include/net/mac80211.h
patching file include/uapi/linux/nl80211.h
patching file net/mac80211/cfg.c
patching file net/mac80211/ieee80211_i.h
patching file net/mac80211/main.c
patching file net/wireless/nl80211.c

Applying ./patches/subsys/600-mac80211-allow-vht-on-2g.patch using plaintext: 
patching file net/mac80211/vht.c
Hunk #1 succeeded at 137 (offset 2 lines).
patching file net/mac80211/util.c
Hunk #1 succeeded at 1616 (offset -153 lines).
patching file net/mac80211/mlme.c
Hunk #1 succeeded at 4682 (offset -142 lines).

Applying ./patches/ath/070-ath_common_config.patch using plaintext: 
patching file drivers/net/wireless/ath/Kconfig

Applying ./patches/ath/080-ath10k_thermal_config.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/Kconfig
patching file drivers/net/wireless/ath/ath10k/Makefile
patching file drivers/net/wireless/ath/ath10k/thermal.h
patching file local-symbols

Applying ./patches/ath/201-ath5k-WAR-for-AR71xx-PCI-bug.patch using plaintext: 
patching file drivers/net/wireless/ath/ath5k/initvals.c
patching file drivers/net/wireless/ath/ath5k/dma.c

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

Applying ./patches/ath/403-world_regd_fixup.patch using plaintext: 
patching file drivers/net/wireless/ath/regd.c

Applying ./patches/ath/404-regd_no_assoc_hints.patch using plaintext: 
patching file net/wireless/reg.c

Applying ./patches/ath/405-ath_regd_us.patch using plaintext: 
patching file drivers/net/wireless/ath/regd_common.h

Applying ./patches/ath/406-ath_relax_default_regd.patch using plaintext: 
patching file drivers/net/wireless/ath/regd.c

Applying ./patches/ath/407-regd_add_extra_country_codes.patch using plaintext: 
patching file drivers/net/wireless/ath/regd.h
patching file drivers/net/wireless/ath/regd_common.h

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
patching file include/linux/ath9k_platform.h
patching file local-symbols
patching file drivers/net/wireless/ath/ath9k/Kconfig

Applying ./patches/ath/552-ahb_of.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/ahb.c
patching file drivers/net/wireless/ath/ath9k/ath9k.h

Applying ./patches/ath/553-ath9k_of_gpio_mask.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/init.c
Hunk #2 succeeded at 766 (offset 2 lines).

Applying ./patches/ath/554-ath9k-dynack-move-debug-log-after-buffer-increments.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/dynack.c

Applying ./patches/ath/557-ath9k-dynack-remove-experimental-tag.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/Kconfig

Applying ./patches/ath/558-ath9k-dynack-introduce-ath_dynack_set_timeout-routin.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/dynack.c

Applying ./patches/ath/559-ath9k-dynack-properly-set-last-timeout-timestamp-in-.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/dynack.c

Applying ./patches/ath/560-ath9k-dynack-set-max-timeout-according-to-channel-wi.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/dynack.c

Applying ./patches/ath/561-ath9k-dynack-set-ackto-to-max-timeout-in-ath_dynack_.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/dynack.c

Applying ./patches/ath/921-ath10k_init_devices_synchronously.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/core.c

Applying ./patches/ath/922-ath10k-increase-rx-buffer-size-to-2048.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/htt.h

Applying ./patches/ath/930-ath10k_add_tpt_led_trigger.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/mac.c

Applying ./patches/ath/960-0010-ath10k-limit-htt-rx-ring-size.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/htt.h

Applying ./patches/ath/960-0011-ath10k-limit-pci-buffer-size.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/pci.c

Applying ./patches/ath/972-ath10k_fix-crash-due-to-wrong-handling-of-peer_bw_rxnss_override-parameter.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/mac.c
patching file drivers/net/wireless/ath/ath10k/wmi.c
patching file drivers/net/wireless/ath/ath10k/wmi.h

Applying ./patches/ath/973-ath10k_fix-band_center_freq-handling-for-VHT160-in-recent-firmwares.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/mac.c
patching file drivers/net/wireless/ath/ath10k/wmi.c

Applying ./patches/ath/974-ath10k_add-LED-and-GPIO-controlling-support-for-various-chipsets.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/Kconfig
patching file drivers/net/wireless/ath/ath10k/Makefile
patching file local-symbols
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

Applying ./patches/ath/977-ath10k-add-support-for-configuring-management-packet.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/mac.c

Applying ./patches/ath/978-ath10k-fix-possible-out-of-bound-access-of-ath10k_ra.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/mac.c

Applying ./patches/ath/979-ath10k-fix-incorrect-multicast-broadcast-rate-settin.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/mac.c

Applying ./patches/ath/980-ath10k-fix-max-antenna-gain-unit.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/mac.c

Applying ./patches/ath/981-ath10k-adjust-tx-power-reduction-for-US-regulatory-d.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/mac.c

Applying ./patches/ath/983-ath10k-allow-vht-on-2g.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/mac.c
Hunk #1 succeeded at 4636 (offset -82 lines).

Applying ./patches/ath/998-ignore-peer-stats-debug-info.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/htt_rx.c
Hunk #1 succeeded at 2534 (offset 14 lines).
Hunk #2 succeeded at 2592 (offset 14 lines).
Hunk #3 succeeded at 2604 (offset 14 lines).
patching file drivers/net/wireless/ath/ath10k/txrx.c
Hunk #1 succeeded at 254 (offset -7 lines).

Applying ./patches/rt2x00/001-rt2x00-use-simple_read_from_buffer.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2x00debug.c

Applying ./patches/rt2x00/002-rt2800-move-usb-specific-txdone-txstatus-routines-to.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.h
patching file drivers/net/wireless/ralink/rt2x00/rt2800usb.c

Applying ./patches/rt2x00/003-rt2800mmio-use-txdone-txstatus-routines-from-lib.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800mmio.c
patching file drivers/net/wireless/ralink/rt2x00/rt2x00queue.c

Applying ./patches/rt2x00/004-rt2x00-do-not-check-for-txstatus-timeout-every-time-.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800mmio.c
patching file drivers/net/wireless/ralink/rt2x00/rt2x00.h
patching file drivers/net/wireless/ralink/rt2x00/rt2x00queue.c

Applying ./patches/rt2x00/005-rt2x00-use-different-txstatus-timeouts-when-flushing.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c
patching file drivers/net/wireless/ralink/rt2x00/rt2x00.h
patching file drivers/net/wireless/ralink/rt2x00/rt2x00mac.c

Applying ./patches/rt2x00/006-rt2800-flush-and-txstatus-rework-for-rt2800mmio.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800mmio.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800mmio.h
patching file drivers/net/wireless/ralink/rt2x00/rt2800pci.c

Applying ./patches/rt2x00/007-rt2x00-rt2400pci-mark-expected-switch-fall-through.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2400pci.c

Applying ./patches/rt2x00/008-rt2x00-rt2500pci-mark-expected-switch-fall-through.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2500pci.c

Applying ./patches/rt2x00/009-rt2x00-rt2800lib-mark-expected-switch-fall-throughs.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c

Applying ./patches/rt2x00/010-rt2x00-rt61pci-mark-expected-switch-fall-through.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt61pci.c

Applying ./patches/rt2x00/011-cross-tree-phase-out-dma_zalloc_coherent.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2x00mmio.c

Applying ./patches/rt2x00/012-rt2x00-reduce-tx-power-to-nominal-level-on-RT6352.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c

Applying ./patches/rt2x00/013-rt2x00-Work-around-a-firmware-bug-with-shared-keys.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt61pci.c

Applying ./patches/rt2x00/014-rt2x00-no-need-to-check-return-value-of-debugfs_crea.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2x00debug.c

Applying ./patches/rt2x00/015-rt2x00-remove-unneeded-check.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c

Applying ./patches/rt2x00/016-rt2x00-remove-confusing-AGC-register.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c

Applying ./patches/rt2x00/017-rt2800-enable-TX_PIN_CFG_LNA_PE_-bits-per-band.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c

Applying ./patches/rt2x00/018-rt2800-enable-TX_PIN_CFG_RFRX_EN-only-for-MT7620.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c

Applying ./patches/rt2x00/019-rt2800-comment-and-simplify-AGC-init-for-RT6352.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c

Applying ./patches/rt2x00/020-cfg80211-add-ratelimited-variants-of-err-and-warn.patch using plaintext: 
patching file include/net/cfg80211.h

Applying ./patches/rt2x00/021-rt2x00-use-ratelimited-variants-dev_warn-dev_err.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2x00.h

Applying ./patches/rt2x00/022-rt2x00-check-number-of-EPROTO-errors.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2x00.h
patching file drivers/net/wireless/ralink/rt2x00/rt2x00usb.c

Applying ./patches/rt2x00/023-rt2x00-do-not-print-error-when-queue-is-full.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2x00queue.c

Applying ./patches/rt2x00/024-rt2800-partially-restore-old-mmio-txstatus-behaviour.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.h
patching file drivers/net/wireless/ralink/rt2x00/rt2800mmio.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800usb.c

Applying ./patches/rt2x00/025-rt2800-new-flush-implementation-for-SoC-devices.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800soc.c

Applying ./patches/rt2x00/026-rt2800-move-txstatus-pending-routine.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.h
patching file drivers/net/wireless/ralink/rt2x00/rt2800usb.c

Applying ./patches/rt2x00/027-rt2800mmio-fetch-tx-status-changes.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800mmio.c

Applying ./patches/rt2x00/028-rt2800mmio-use-timer-and-work-for-handling-tx-status.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800mmio.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800mmio.h
patching file drivers/net/wireless/ralink/rt2x00/rt2800pci.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800soc.c
patching file drivers/net/wireless/ralink/rt2x00/rt2x00dev.c

Applying ./patches/rt2x00/029-rt2x00-remove-last_nostatus_check.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c
patching file drivers/net/wireless/ralink/rt2x00/rt2x00.h
patching file drivers/net/wireless/ralink/rt2x00/rt2x00queue.c

Applying ./patches/rt2x00/030-rt2x00-remove-not-used-entry-field.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2x00queue.h

Applying ./patches/rt2x00/031-rt2x00mmio-remove-legacy-comment.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2x00mmio.h

Applying ./patches/rt2x00/050-rt2x00-add-RT3883-support.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800.h
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800soc.c

Applying ./patches/rt2x00/060-rt2x00-allow-to-specify-watchdog-interval.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2x00.h
patching file drivers/net/wireless/ralink/rt2x00/rt2x00link.c

Applying ./patches/rt2x00/061-rt2800-add-helpers-for-reading-dma-done-index.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.h
patching file drivers/net/wireless/ralink/rt2x00/rt2800mmio.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800mmio.h
patching file drivers/net/wireless/ralink/rt2x00/rt2800pci.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800soc.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800usb.c

Applying ./patches/rt2x00/062-rt2800-initial-watchdog-implementation.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.h
patching file drivers/net/wireless/ralink/rt2x00/rt2800pci.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800soc.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800usb.c
patching file drivers/net/wireless/ralink/rt2x00/rt2x00queue.h

Applying ./patches/rt2x00/063-rt2800-add-pre_reset_hw-callback.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.h
patching file drivers/net/wireless/ralink/rt2x00/rt2800pci.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800soc.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800usb.c
patching file drivers/net/wireless/ralink/rt2x00/rt2x00.h

Applying ./patches/rt2x00/064-rt2800-do-not-nullify-initialization-vector-data.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c

Applying ./patches/rt2x00/065-rt2x00-add-restart-hw.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c
patching file drivers/net/wireless/ralink/rt2x00/rt2x00.h
patching file drivers/net/wireless/ralink/rt2x00/rt2x00debug.c
patching file drivers/net/wireless/ralink/rt2x00/rt2x00dev.c

Applying ./patches/rt2x00/066-rt2800-do-not-enable-watchdog-by-default.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c
patching file drivers/net/wireless/ralink/rt2x00/rt2x00.h
patching file drivers/net/wireless/ralink/rt2x00/rt2x00link.c

Applying ./patches/rt2x00/067-rt2x00usb-fix-rx-queue-hang.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2x00usb.c

Applying ./patches/rt2x00/068-rt2x00usb-remove-unnecessary-rx-flag-checks.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2x00usb.c

Applying ./patches/rt2x00/069-rt2x00-no-need-to-check-return-value-of-debugfs_crea.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2x00debug.c

Applying ./patches/rt2x00/070-rt2800usb-Add-new-rt2800usb-device-PLANEX-GW-USMicro.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800usb.c

Applying ./patches/rt2x00/071-rt2x00-clear-IV-s-on-start-to-fix-AP-mode-regression.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c
patching file drivers/net/wireless/ralink/rt2x00/rt2x00.h
patching file drivers/net/wireless/ralink/rt2x00/rt2x00dev.c

Applying ./patches/rt2x00/072-rt2x00-do-not-set-IEEE80211_TX_STAT_AMPDU_NO_BACK-on.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2x00dev.c

Applying ./patches/rt2x00/073-rt2x00-clear-up-IV-s-on-key-removal.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c

Applying ./patches/rt2x00/074-Revert-rt2800-enable-TX_PIN_CFG_LNA_PE_-bits-per-ban.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c

Applying ./patches/rt2x00/075-rt2800-remove-errornous-duplicate-condition.patch using plaintext: 
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
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.h
patching file drivers/net/wireless/ralink/rt2x00/rt2x00.h

Applying ./patches/rt2x00/983-rt2x00-add-r-calibration.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.h
patching file drivers/net/wireless/ralink/rt2x00/rt2x00.h

Applying ./patches/rt2x00/984-rt2x00-add-rxdcoc-calibration.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.h
patching file drivers/net/wireless/ralink/rt2x00/rt2x00.h

Applying ./patches/rt2x00/985-rt2x00-add-rxiq-calibration.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.h
patching file drivers/net/wireless/ralink/rt2x00/rt2x00.h

Applying ./patches/rt2x00/986-rt2x00-add-TX-LOFT-calibration.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.h
patching file drivers/net/wireless/ralink/rt2x00/rt2x00.h

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

Applying ./patches/brcm/300-v4.20-0001-brcmfmac-add-CYW89342-mini-PCIe-device.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/pcie.c

Applying ./patches/brcm/305-v4.20-0001-brcmfmac-remove-set-but-not-used-variables-sfdoff-an.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/sdio.c

Applying ./patches/brcm/320-v5.0-0001-brcmfmac-Remove-firmware-loading-code-duplication.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/firmware.c

Applying ./patches/brcm/320-v5.0-0002-brcmfmac-Remove-recursion-from-firmware-load-error-h.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/firmware.c

Applying ./patches/brcm/320-v5.0-0003-brcmfmac-Add-support-for-first-trying-to-get-a-board.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/firmware.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/firmware.h

Applying ./patches/brcm/320-v5.0-0004-brcmfmac-Set-board_type-used-for-nvram-file-selectio.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/common.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/of.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/pcie.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/sdio.c

Applying ./patches/brcm/320-v5.0-0005-brcmfmac-Set-board_type-from-DMI-on-x86-based-machin.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/Makefile
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/common.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/common.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/dmi.c

Applying ./patches/brcm/320-v5.0-0006-brcmfmac-Cleanup-brcmf_fw_request_done.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/firmware.c

Applying ./patches/brcm/321-v5.0-0001-brcmfmac-Add-support-for-getting-nvram-contents-from.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/firmware.c

Applying ./patches/brcm/321-v5.0-0002-brcmfmac-Fix-ccode-from-EFI-nvram-when-necessary.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/firmware.c

Applying ./patches/brcm/322-v5.0-0001-brcmfmac-fix-spelling-mistake-Retreiving-Retrieving.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/common.c

Applying ./patches/brcm/323-v5.0-0001-brcmutil-print-invalid-chanspec-when-WARN-ing.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmutil/d11.c

Applying ./patches/brcm/325-v5.0-brcmfmac-support-STA-info-struct-v7.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/fwil_types.h

Applying ./patches/brcm/326-v5.0-brcmfmac-Call-brcmf_dmi_probe-before-brcmf_of_probe.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/common.c

Applying ./patches/brcm/328-v5.0-0001-brcmfmac-add-credit-numbers-updating-support.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/fwsignal.c

Applying ./patches/brcm/328-v5.0-0002-brcmfmac-enable-frameburst-mode-in-default-firmware-.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/cfg80211.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/fwil.h

Applying ./patches/brcm/328-v5.0-0003-brcmfmac-handle-compressed-tx-status-signal.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/fwsignal.c

Applying ./patches/brcm/329-v5.0-0001-brcmfmac-add-4354-raw-pcie-device-id.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/pcie.c
patching file drivers/net/wireless/broadcom/brcm80211/include/brcm_hw_ids.h

Applying ./patches/brcm/329-v5.0-0004-brcmfmac-add-support-for-CYW43012-SDIO-chipset.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/bcmsdh.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/chip.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/sdio.c
patching file drivers/net/wireless/broadcom/brcm80211/include/brcm_hw_ids.h
patching file include/linux/mmc/sdio_ids.h

Applying ./patches/brcm/329-v5.0-0005-brcmfmac-allow-GCI-core-enumuration.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/chip.c

Applying ./patches/brcm/329-v5.0-0006-brcmfmac-update-43012-F2-watermark-setting-to-fix-DM.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/sdio.c

Applying ./patches/brcm/329-v5.0-0007-brcmfmac-4373-save-restore-support.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/chip.c
patching file drivers/net/wireless/broadcom/brcm80211/include/chipcommon.h

Applying ./patches/brcm/329-v5.0-0008-brcmfmac-disable-command-decode-in-sdio_aos.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/sdio.c

Applying ./patches/brcm/330-v5.0-0001-brcmfmac-fix-false-positive-Wmaybe-unintialized-warn.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/firmware.c

Applying ./patches/brcm/340-v5.1-brcmfmac-Add-DMI-nvram-filename-quirk-for-PoV-TAB-P1.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/dmi.c

Applying ./patches/brcm/341-v5.1-brcmfmac-add-a-check-for-the-status-of-usb_register.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/usb.c

Applying ./patches/brcm/342-v5.1-brcmfmac-fix-system-warning-message-during-wowl-susp.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/pno.c

Applying ./patches/brcm/344-v5.1-brcmfmac-modify-__brcmf_err-to-take-bus-as-a-paramet.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/common.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/debug.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/tracepoint.c

Applying ./patches/brcm/345-v5.1-brcmfmac-pass-bus-to-the-__brcmf_err-in-pcie.c.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/debug.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/pcie.c

Applying ./patches/brcm/346-v5.1-brcmfmac-add-bphy_err-and-use-it-in-the-cfg80211.c.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/cfg80211.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/debug.h

Applying ./patches/brcm/347-v5.1-brcmfmac-fix-typos.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/core.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/firmware.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/fweh.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/usb.c

Applying ./patches/brcm/348-v5.1-brcmfmac-support-monitor-frames-with-the-hardware-uc.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/core.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/feature.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/feature.h

Applying ./patches/brcm/349-v5.1-0004-brcmfmac-disable-MBSS-feature-for-bcm4330-device.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/feature.c

Applying ./patches/brcm/349-v5.1-0005-brcmfmac-check-and-dump-trap-info-during-sdio-probe.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/sdio.c

Applying ./patches/brcm/349-v5.1-0006-brcmfmac-use-chipname-in-brcmf_fw_alloc_request-for-.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/firmware.c

Applying ./patches/brcm/350-v5.1-brcmfmac-print-firmware-reported-ring-status-errors.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/msgbuf.c

Applying ./patches/brcm/351-v5.1-0001-brcmfmac-improve-code-handling-bandwidth-of-firmware.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/cfg80211.c

Applying ./patches/brcm/351-v5.1-0002-brcmfmac-support-firmware-reporting-160-MHz-channels.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/cfg80211.c

Applying ./patches/brcm/352-v5.1-brcmfmac-rework-bphy_err-to-take-struct-brcmf_pub-ar.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/cfg80211.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/debug.h

Applying ./patches/brcm/353-v5.1-brcmfmac-remove-set-but-not-used-variable-old_state.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/usb.c

Applying ./patches/brcm/354-v5.1-brcmfmac-use-bphy_err-in-all-wiphy-related-code.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/bcdc.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/common.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/core.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/feature.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/fweh.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/fwil.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/fwsignal.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/msgbuf.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/p2p.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/pno.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/proto.c

Applying ./patches/brcm/355-v5.1-brcmfmac-add-basic-validation-of-shared-RAM-address.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/pcie.c

Applying ./patches/brcm/356-v5.1-0001-brcmfmac-fix-size-of-the-struct-msgbuf_ring_status.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/msgbuf.c

Applying ./patches/brcm/356-v5.1-0002-brcmfmac-print-firmware-reported-general-status-erro.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/msgbuf.c

Applying ./patches/brcm/360-v5.2-0001-brcmfmac-support-repeated-brcmf_fw_alloc_request-cal.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/firmware.c

Applying ./patches/brcm/360-v5.2-0002-brcmfmac-add-a-function-designated-for-handling-firm.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/bus.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/core.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/pcie.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/sdio.c

Applying ./patches/brcm/360-v5.2-0003-brcmfmac-reset-PCIe-bus-on-a-firmware-crash.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/bus.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/core.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/core.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/pcie.c

Applying ./patches/brcm/362-v5.2-0002-brcmfmac-remove-pending-parameter-from-brcmf_usb_fre.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/usb.c

Applying ./patches/brcm/362-v5.2-0003-brcmfmac-remove-unused-variable-i-from-brcmf_usb_fre.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/usb.c

Applying ./patches/brcm/366-v5.2-brcmfmac-Use-struct_size-in-kzalloc.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/firmware.c

Applying ./patches/brcm/367-v5.2-brcmfmac-Loading-the-correct-firmware-for-brcm43456.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/sdio.c

Applying ./patches/brcm/369-v5.2-brcmfmac-Add-DMI-nvram-filename-quirk-for-ACEPC-T8-a.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/dmi.c

Applying ./patches/brcm/370-v5.2-brcmfmac-send-mailbox-interrupt-twice-for-specific-h.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/pcie.c

Applying ./patches/brcm/371-v5.2-Revert-brcmfmac-send-mailbox-interrupt-twice-for-spe.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/pcie.c

Applying ./patches/brcm/372-v5.2-brcmfmac-send-mailbox-interrupt-twice-for-specific-h.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/pcie.c

Applying ./patches/brcm/374-v5.2-brcmfmac-set-txflow-request-id-from-1-to-pktids-arra.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/msgbuf.c

Applying ./patches/brcm/375-v5.2-brcmfmac-print-firmware-messages-after-a-firmware-cr.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/pcie.c

Applying ./patches/brcm/380-v5.4-0001-brcmfmac-switch-source-files-to-using-SPDX-license-i.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/Makefile
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/Makefile
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/bcdc.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/bcdc.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/bcmsdh.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/btcoex.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/btcoex.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/bus.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/cfg80211.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/cfg80211.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/chip.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/chip.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/common.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/common.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/commonring.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/commonring.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/core.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/core.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/debug.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/debug.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/dmi.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/feature.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/feature.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/firmware.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/firmware.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/flowring.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/flowring.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/fweh.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/fweh.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/fwil.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/fwil.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/fwil_types.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/fwsignal.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/fwsignal.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/msgbuf.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/msgbuf.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/of.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/of.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/p2p.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/p2p.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/pcie.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/pcie.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/pno.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/pno.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/proto.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/proto.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/sdio.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/sdio.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/tracepoint.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/tracepoint.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/usb.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/usb.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/vendor.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/vendor.h

Applying ./patches/brcm/381-v5.4-brcmfmac-fix-typos-in-code-comments.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/fwil.c

Applying ./patches/brcm/382-v5.4-brcmfmac-use-strlcpy-instead-of-strcpy.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/common.c

Applying ./patches/brcm/383-v5.4-0001-brcmfmac-add-160MHz-in-chandef_to_chanspec.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/cfg80211.c

Applying ./patches/brcm/383-v5.4-0002-brcmfmac-enable-DFS_OFFLOAD-extended-feature-if-supp.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/cfg80211.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/feature.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/feature.h

Applying ./patches/brcm/383-v5.4-0003-brcmfmac-allow-160MHz-in-custom-regulatory-rules.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/cfg80211.c

Applying ./patches/brcm/384-v5.4-0001-Revert-brcmfmac-fix-NULL-pointer-derefence-during-US.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/bcdc.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/bcdc.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/core.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/fwsignal.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/fwsignal.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/proto.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/proto.h

Applying ./patches/brcm/384-v5.4-0002-brcmfmac-change-the-order-of-things-in-brcmf_detach.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/core.c

Applying ./patches/brcm/384-v5.4-0003-brcmfmac-avoid-firmware-command-in-brcmf_netdev_open.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/core.c

Applying ./patches/brcm/384-v5.4-0004-brcmfmac-clear-events-in-brcmf_fweh_detach-will-alwa.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/fweh.c

Applying ./patches/brcm/384-v5.4-0005-brcmfmac-avoid-firmware-commands-when-bus-is-down.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/cfg80211.c

Applying ./patches/brcm/384-v5.4-0006-brcmfmac-simply-remove-flowring-if-bus-is-down.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/msgbuf.c

Applying ./patches/brcm/384-v5.4-0007-brcmfmac-remove-unnecessary-strlcpy-upon-obtaining-v.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/common.c

Applying ./patches/brcm/385-v5.4-brcmfmac-don-t-net_ratelimit-CONSOLE-messages-on-fir.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/pcie.c

Applying ./patches/brcm/386-v5.4-brcmfmac-remove-set-but-not-used-variable-dtim_perio.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/cfg80211.c

Applying ./patches/brcm/387-v5.4-brcmfmac-remove-redundant-assignment-to-pointer-hash.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/msgbuf.c

Applying ./patches/brcm/388-v5.4-brcmfmac-replace-strncpy-by-strscpy.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/cfg80211.c

Applying ./patches/brcm/389-v5.4-brcmfmac-get-chip-s-default-RAM-info-during-PCIe-set.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/chip.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/chip.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/pcie.c

Applying ./patches/brcm/390-v5.4-0001-brcmfmac-add-stub-version-of-brcmf_debugfs_get_devdi.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/debug.h

Applying ./patches/brcm/390-v5.4-0002-brcmfmac-add-reset-debugfs-entry-for-testing-reset.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/core.c

Applying ./patches/brcm/391-v5.4-brcmfmac-use-ph-to-print-small-buffer.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/cfg80211.c

Applying ./patches/brcm/392-v5.4-0001-brcmfmac-move-cfg80211_ops-pointer-to-another-struct.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/cfg80211.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/cfg80211.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/core.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/core.h

Applying ./patches/brcm/392-v5.4-0002-brcmfmac-split-brcmf_attach-and-brcmf_detach-functio.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/bus.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/core.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/pcie.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/sdio.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/usb.c

Applying ./patches/brcm/392-v5.4-0003-brcmfmac-don-t-realloc-wiphy-during-PCIe-reset.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/pcie.c

Applying ./patches/brcm/401-v5.5-0001-brcmfmac-don-t-WARN-when-there-are-no-requests.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/pno.c

Applying ./patches/brcm/401-v5.5-0002-brcmfmac-fix-suspend-resume-when-power-is-cut-off.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/bcmsdh.c

Applying ./patches/brcm/403-v5.5-brcmfmac-remove-set-but-not-used-variable-mpnum-nsp-.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/chip.c

Applying ./patches/brcm/404-v5.5-brcmfmac-disable-PCIe-interrupts-before-bus-reset.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/pcie.c

Applying ./patches/brcm/410-v5.6-brcmfmac-Fix-memory-leak-in-brcmf_p2p_create_p2pdev.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/p2p.c

Applying ./patches/brcm/412-v5.6-brcmfmac-set-interface-carrier-to-off-by-default.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/core.c

Applying ./patches/brcm/414-v5.6-0001-brcmfmac-reset-two-D11-cores-if-chip-has-two-D11-cor.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/chip.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/chip.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/pcie.c

Applying ./patches/brcm/414-v5.6-0002-brcmfmac-set-F2-blocksize-and-watermark-for-4359.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/bcmsdh.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/sdio.c

Applying ./patches/brcm/414-v5.6-0003-brcmfmac-fix-rambase-for-4359-9.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/chip.c

Applying ./patches/brcm/414-v5.6-0004-brcmfmac-make-errors-when-setting-roaming-parameters.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/cfg80211.c

Applying ./patches/brcm/414-v5.6-0005-brcmfmac-add-support-for-BCM4359-SDIO-chipset.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/bcmsdh.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/chip.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/sdio.c
patching file include/linux/mmc/sdio_ids.h

Applying ./patches/brcm/414-v5.6-0006-brcmfmac-add-RSDB-condition-when-setting-interface-c.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/cfg80211.c

Applying ./patches/brcm/414-v5.6-0007-brcmfmac-not-set-mbss-in-vif-if-firmware-does-not-su.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/cfg80211.c

Applying ./patches/brcm/416-v5.6-brcmfmac-Keep-OOB-wake-interrupt-disabled-when-it-sh.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/bcmsdh.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/sdio.h

Applying ./patches/brcm/417-v5.6-brcmfmac-use-true-false-for-bool-variable.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/fwsignal.c

Applying ./patches/brcm/418-v5.6-brcmfmac-sdio-Fix-OOB-interrupt-initialization-on-br.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/sdio.c

Applying ./patches/brcm/419-v5.6-0001-brcmfmac-simplify-building-interface-combinations.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/cfg80211.c

Applying ./patches/brcm/419-v5.6-0002-brcmfmac-add-initial-support-for-monitor-mode.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/cfg80211.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/core.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/core.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/feature.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/feature.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/fwil.h

Applying ./patches/brcm/420-v5.6-brcmfmac-Remove-always-false-idx-0-statement.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/msgbuf.c

Applying ./patches/brcm/500-brcmfmac-add-stub-for-monitor-interface-xmit.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/core.c

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
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-4.19.189-1/include/linux/ath9k_platform.h /openwrt/build_dir/target-x86_64_musl/linux-x86_64/linux-5.4.121/include/linux/ath9k_platform.h differ: char 1571, line 56
make[3]: *** [Makefile:563: /openwrt/build_dir/target-x86_64_musl/linux-x86_64/backports-4.19.189-1/.configured_8bf20ae24ff8e1329e40259a18fa7cb3] Error 1
```