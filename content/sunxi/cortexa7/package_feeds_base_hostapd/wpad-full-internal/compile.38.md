---
title: "compile.38"
date: 2021-06-21 06:02:01.005083
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
make package/feeds/base/hostapd/compile -j$(nproc) || make package/feeds/base/hostapd/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-wolfssl-init-RNG-with-ECC-key.patch using plaintext: 
patching file src/crypto/crypto_wolfssl.c

Applying ./patches/010-mesh-Allow-DFS-channels-to-be-selected-if-dfs-is-ena.patch using plaintext: 
patching file wpa_supplicant/wpa_supplicant.c

Applying ./patches/011-mesh-use-deterministic-channel-on-channel-switch.patch using plaintext: 
patching file src/ap/dfs.c
patching file src/drivers/driver_nl80211.c

Applying ./patches/020-mesh-make-forwarding-configurable.patch using plaintext: 
patching file src/ap/ap_config.h
patching file src/drivers/driver.h
patching file src/drivers/driver_nl80211.c
patching file wpa_supplicant/config.c
patching file wpa_supplicant/config.h
patching file wpa_supplicant/config_file.c
patching file wpa_supplicant/config_ssid.h
patching file wpa_supplicant/mesh.c
patching file wpa_supplicant/mesh_mpm.c
patching file wpa_supplicant/wpa_supplicant.conf

Applying ./patches/021-fix-sta-add-after-previous-connection.patch using plaintext: 
patching file src/ap/ieee802_11.c

Applying ./patches/100-daemonize_fix.patch using plaintext: 
patching file src/utils/os_unix.c

Applying ./patches/200-multicall.patch using plaintext: 
patching file hostapd/Makefile
patching file wpa_supplicant/Makefile
patching file src/drivers/driver.h
patching file src/ap/drv_callbacks.c
patching file wpa_supplicant/wpa_priv.c
patching file wpa_supplicant/events.c
patching file wpa_supplicant/wpa_supplicant.c
patching file hostapd/main.c
patching file src/drivers/drivers.c
patching file wpa_supplicant/eapol_test.c

Applying ./patches/300-noscan.patch using plaintext: 
patching file hostapd/config_file.c
patching file src/ap/ap_config.h
patching file src/ap/hw_features.c
patching file src/ap/ieee802_11_ht.c

Applying ./patches/301-mesh-noscan.patch using plaintext: 
patching file wpa_supplicant/config.c
patching file wpa_supplicant/config_file.c
patching file wpa_supplicant/mesh.c
patching file wpa_supplicant/wpa_supplicant.c
patching file wpa_supplicant/config_ssid.h

Applying ./patches/310-rescan_immediately.patch using plaintext: 
patching file wpa_supplicant/wpa_supplicant.c

Applying ./patches/320-optional_rfkill.patch using plaintext: 
patching file src/drivers/drivers.mak
patching file src/drivers/rfkill.h

Applying ./patches/330-nl80211_fix_set_freq.patch using plaintext: 
patching file src/drivers/driver_nl80211.c

Applying ./patches/340-reload_freq_change.patch using plaintext: 
patching file src/ap/hostapd.c

Applying ./patches/341-mesh-ctrl-iface-channel-switch.patch using plaintext: 
patching file wpa_supplicant/ap.c

Applying ./patches/350-nl80211_del_beacon_bss.patch using plaintext: 
patching file src/drivers/driver_nl80211.c

Applying ./patches/360-ctrl_iface_reload.patch using plaintext: 
patching file hostapd/ctrl_iface.c
patching file src/ap/ctrl_iface_ap.c

Applying ./patches/370-ap_sta_support.patch using plaintext: 
patching file wpa_supplicant/Makefile
patching file wpa_supplicant/bss.c
patching file wpa_supplicant/bss.h
patching file wpa_supplicant/main.c
patching file wpa_supplicant/wpa_supplicant.c
patching file wpa_supplicant/wpa_supplicant_i.h
patching file hostapd/ctrl_iface.c
patching file src/ap/beacon.c
patching file wpa_supplicant/events.c
patching file src/drivers/driver.h
patching file src/drivers/driver_nl80211_event.c

Applying ./patches/380-disable_ctrl_iface_mib.patch using plaintext: 
patching file hostapd/Makefile
patching file hostapd/ctrl_iface.c
patching file wpa_supplicant/Makefile
patching file wpa_supplicant/ctrl_iface.c
patching file src/ap/ctrl_iface_ap.c
patching file src/ap/ieee802_1x.c
patching file src/ap/wpa_auth.c
patching file src/rsn_supp/wpa.c
patching file wpa_supplicant/ap.c

Applying ./patches/381-hostapd_cli_UNKNOWN-COMMAND.patch using plaintext: 
patching file hostapd/hostapd_cli.c

Applying ./patches/390-wpa_ie_cap_workaround.patch using plaintext: 
patching file src/common/wpa_common.c

Applying ./patches/400-wps_single_auth_enc_type.patch using plaintext: 
patching file src/ap/wps_hostapd.c

Applying ./patches/410-limit_debug_messages.patch using plaintext: 
patching file src/utils/wpa_debug.c
patching file src/utils/wpa_debug.h

Applying ./patches/420-indicate-features.patch using plaintext: 
patching file hostapd/main.c
patching file wpa_supplicant/main.c

Applying ./patches/430-hostapd_cli_ifdef.patch using plaintext: 
patching file hostapd/hostapd_cli.c

Applying ./patches/431-wpa_cli_ifdef.patch using plaintext: 
patching file wpa_supplicant/wpa_cli.c

Applying ./patches/432-missing-typedef.patch using plaintext: 
patching file src/drivers/linux_wext.h

Applying ./patches/450-scan_wait.patch using plaintext: 
patching file hostapd/main.c

Applying ./patches/460-wpa_supplicant-add-new-config-params-to-be-used-with.patch using plaintext: 
patching file src/drivers/driver.h
patching file wpa_supplicant/config.c
patching file wpa_supplicant/config_ssid.h
patching file wpa_supplicant/wpa_supplicant.c

Applying ./patches/461-driver_nl80211-use-new-parameters-during-ibss-join.patch using plaintext: 
patching file src/drivers/driver_nl80211.c

Applying ./patches/463-add-mcast_rate-to-11s.patch using plaintext: 
patching file src/drivers/driver.h
patching file src/drivers/driver_nl80211.c
patching file wpa_supplicant/mesh.c

Applying ./patches/464-fix-mesh-obss-check.patch using plaintext: 
patching file wpa_supplicant/wpa_supplicant.c

Applying ./patches/470-survey_data_fallback.patch using plaintext: 
patching file src/ap/acs.c

Applying ./patches/500-lto-jobserver-support.patch using plaintext: 
patching file hostapd/Makefile
patching file wpa_supplicant/Makefile

Applying ./patches/599-wpa_supplicant-fix-warnings.patch using plaintext: 
patching file wpa_supplicant/wps_supplicant.h

Applying ./patches/600-ubus_support.patch using plaintext: 
patching file hostapd/Makefile
patching file src/ap/hostapd.h
patching file src/ap/hostapd.c
patching file src/ap/ieee802_11.c
patching file src/ap/beacon.c
patching file src/ap/drv_callbacks.c
patching file src/ap/sta_info.c
patching file src/ap/wpa_auth_glue.c
patching file wpa_supplicant/Makefile
patching file wpa_supplicant/wpa_supplicant.c
patching file wpa_supplicant/wpa_supplicant_i.h
patching file wpa_supplicant/wps_supplicant.c
patching file hostapd/main.c
patching file wpa_supplicant/main.c
patching file src/ap/rrm.c
patching file src/ap/vlan_init.c
patching file src/ap/dfs.c

Applying ./patches/700-wifi-reload.patch using plaintext: 
patching file hostapd/config_file.c
patching file src/ap/ap_config.c
patching file src/ap/ap_config.h
patching file src/ap/hostapd.c
patching file src/ap/hostapd.h
patching file src/drivers/driver_nl80211.c
patching file hostapd/ctrl_iface.c
patching file hostapd/main.c
patching file src/ap/wps_hostapd.c

Applying ./patches/710-vlan_no_bridge.patch using plaintext: 
patching file src/ap/ap_config.h
patching file src/ap/vlan_full.c
patching file hostapd/config_file.c

Applying ./patches/720-ACS-fix-channel-100-frequency.patch using plaintext: 
patching file src/ap/acs.c

Applying ./patches/720-iface_max_num_sta.patch using plaintext: 
patching file hostapd/config_file.c
patching file src/ap/hostapd.h
patching file src/ap/hostapd.c
patching file src/ap/beacon.c
patching file src/ap/ap_config.h

Applying ./patches/730-ft_iface.patch using plaintext: 
patching file hostapd/config_file.c
patching file src/ap/ap_config.h
patching file src/ap/wpa_auth_glue.c
make[4]: warning: jobserver unavailable: using -j1.  Add '+' to parent make rule.
make[4]: warning: jobserver unavailable: using -j1.  Add '+' to parent make rule.
make[4]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/hostapd-wpad-full-internal/hostapd-2021-05-22-b102f19b/hostapd'
  CC  hostapd_cli.c
  CC  ../src/common/wpa_ctrl.c
  CC  ../src/utils/os_unix.c
  CC  ../src/common/cli.c
  CC  ../src/utils/eloop.c
  CC  ../src/utils/common.c
  CC  ../src/utils/wpa_debug.c
  CC  ../src/utils/edit_simple.c
  CC  main.c
  CC  config_file.c
  CC  ../src/ap/hostapd.c
  CC  ../src/ap/wpa_auth_glue.c
  CC  ../src/ap/drv_callbacks.c
  CC  ../src/ap/ap_drv_ops.c
  CC  ../src/ap/utils.c
  CC  ../src/ap/authsrv.c
  CC  ../src/ap/ieee802_1x.c
  CC  ../src/ap/ap_config.c
  CC  ../src/ap/eap_user_db.c
  CC  ../src/ap/ieee802_11_auth.c
  CC  ../src/ap/sta_info.c
  CC  ../src/ap/wpa_auth.c
  CC  ../src/ap/tkip_countermeasures.c
  CC  ../src/ap/ap_mlme.c
  CC  ../src/ap/wpa_auth_ie.c
  CC  ../src/ap/preauth_auth.c
  CC  ../src/ap/pmksa_cache_auth.c
  CC  ../src/ap/ieee802_11_shared.c
  CC  ../src/ap/beacon.c
  CC  ../src/ap/bss_load.c
  CC  ../src/ap/neighbor_db.c
  CC  ../src/ap/rrm.c
  CC  ../src/drivers/drivers.c
  CC  ../src/ap/taxonomy.c
  CC  ../src/utils/wpabuf.c
  CC  ../src/utils/ip_addr.c
  CC  ../src/utils/crc32.c
  CC  ../src/common/ieee802_11_common.c
  CC  ../src/common/wpa_common.c
  CC  ../src/common/hw_features_common.c
  CC  ../src/eapol_auth/eapol_auth_sm.c
  CC  ../src/ap/ubus.c
  CC  ../src/radius/radius.c
  CC  ../src/radius/radius_client.c
  CC  ../src/radius/radius_das.c
  CC  ../src/ap/accounting.c
  CC  ../src/ap/vlan_init.c
  CC  ../src/ap/vlan_ifconfig.c
  CC  ../src/ap/vlan.c
  CC  ../src/ap/vlan_full.c
  CC  ../src/ap/vlan_ioctl.c
  CC  ../src/common/ctrl_iface_common.c
  CC  ctrl_iface.c
  CC  ../src/ap/ctrl_iface_ap.c
  CC  ../src/ap/wpa_auth_ft.c
  CC  ../src/ap/eth_p_oui.c
  CC  ../src/ap/airtime_policy.c
  CC  ../src/ap/wnm_ap.c
  CC  ../src/drivers/driver_wext.c
  CC  ../src/drivers/driver_wired.c
  CC  ../src/drivers/driver_wired_common.c
  CC  ../src/drivers/linux_ioctl.c
  CC  ../src/drivers/netlink.c
  CC  ../src/l2_packet/l2_packet_linux.c
  CC  ../src/eap_server/eap_server_md5.c
  CC  ../src/eap_server/eap_server_tls.c
  CC  ../src/eap_server/eap_server_peap.c
  CC  ../src/eap_common/eap_peap_common.c
  CC  ../src/eap_server/eap_server_ttls.c
  CC  ../src/eap_server/eap_server_mschapv2.c
  CC  ../src/eap_server/eap_server_gtc.c
  CC  ../src/eap_server/eap_server_fast.c
  CC  ../src/eap_common/eap_fast_common.c
  CC  ../src/utils/uuid.c
  CC  ../src/ap/wps_hostapd.c
  CC  ../src/eap_server/eap_server_wsc.c
  CC  ../src/eap_common/eap_wsc_common.c
  CC  ../src/wps/wps.c
  CC  ../src/wps/wps_common.c
  CC  ../src/wps/wps_attr_parse.c
  CC  ../src/wps/wps_attr_build.c
  CC  ../src/wps/wps_attr_process.c
  CC  ../src/wps/wps_dev_attr.c
  CC  ../src/wps/wps_enrollee.c
  CC  ../src/wps/wps_registrar.c
  CC  eap_register.c
  CC  ../src/eap_server/eap_server.c
  CC  ../src/eap_common/eap_common.c
  CC  ../src/eap_server/eap_server_methods.c
  CC  ../src/eap_server/eap_server_identity.c
  CC  ../src/crypto/ms_funcs.c
  CC  ../src/eap_common/chap.c
  CC  ../src/eap_server/eap_server_tls_common.c
  CC  ../src/crypto/crypto_internal-rsa.c
  CC  ../src/crypto/tls_internal.c
  CC  ../src/tls/tlsv1_common.c
  CC  ../src/tls/tlsv1_record.c
  CC  ../src/tls/tlsv1_cred.c
  CC  ../src/tls/tlsv1_server.c
  CC  ../src/tls/tlsv1_server_write.c
  CC  ../src/tls/tlsv1_server_read.c
  CC  ../src/tls/rsa.c
  CC  ../src/tls/x509v3.c
  CC  ../src/tls/pkcs1.c
  CC  ../src/tls/pkcs5.c
  CC  ../src/tls/pkcs8.c
  CC  ../src/crypto/crypto_internal-cipher.c
  CC  ../src/crypto/crypto_internal-modexp.c
  CC  ../src/tls/bignum.c
  CC  ../src/crypto/crypto_internal.c
  CC  ../src/crypto/aes-internal.c
  CC  ../src/crypto/aes-internal-enc.c
  CC  ../src/crypto/aes-wrap.c
  CC  ../src/crypto/aes-siv.c
  CC  ../src/crypto/aes-ctr.c
  CC  ../src/crypto/aes-omac1.c
  CC  ../src/crypto/aes-unwrap.c
  CC  ../src/crypto/aes-cbc.c
  CC  ../src/crypto/aes-internal-dec.c
  CC  ../src/crypto/sha1.c
  CC  ../src/crypto/sha1-prf.c
  CC  ../src/crypto/sha1-internal.c
  CC  ../src/crypto/sha1-pbkdf2.c
  CC  ../src/crypto/sha1-tprf.c
  CC  ../src/crypto/sha1-tlsprf.c
  CC  ../src/crypto/md5.c
  CC  ../src/crypto/md5-internal.c
  CC  ../src/crypto/md4-internal.c
  CC  ../src/crypto/des-internal.c
  CC  ../src/crypto/rc4.c
  CC  ../src/crypto/sha256.c
  CC  ../src/crypto/sha256-prf.c
  CC  ../src/crypto/sha256-internal.c
  CC  ../src/crypto/sha256-kdf.c
  CC  ../src/crypto/sha384-internal.c
  CC  ../src/crypto/sha512-internal.c
  CC  ../src/tls/asn1.c
  CC  ../src/crypto/dh_groups.c
  CC  ../src/crypto/dh_group5.c
  CC  ../src/utils/base64.c
  CC  ../src/ap/ieee802_11_ht.c
  CC  ../src/ap/ieee802_11_vht.c
  CC  ../src/ap/hs20.c
  CC  ../src/common/gas.c
  CC  ../src/ap/gas_serv.c
  CC  ../src/ap/x_snoop.c
  CC  ../src/ap/dhcp_snoop.c
  CC  ../src/ap/ndisc_snoop.c
  CC  ../src/drivers/driver_common.c
  LD  hostapd_cli
  CC  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/hostapd-wpad-full-internal/hostapd-2021-05-22-b102f19b/build/hostapd/main.o
make[4]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/hostapd-wpad-full-internal/hostapd-2021-05-22-b102f19b/hostapd'
make[4]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/hostapd-wpad-full-internal/hostapd-2021-05-22-b102f19b/wpa_supplicant'
  CC  wpa_cli.c
  CC  ../src/common/wpa_ctrl.c
  CC  ../src/utils/wpa_debug.c
  CC  ../src/utils/common.c
  CC  ../src/common/cli.c
  CC  ../src/utils/os_unix.c
  CC  ../src/utils/eloop.c
  CC  ../src/utils/edit_simple.c
  CC  config.c
  CC  notify.c
  CC  bss.c
  CC  eap_register.c
  CC  ../src/utils/config.c
  CC  ../src/utils/wpabuf.c
  CC  ../src/utils/bitfield.c
  CC  ../src/utils/ip_addr.c
  CC  ../src/utils/crc32.c
  CC  op_classes.c
  CC  rrm.c
  CC  twt.c
  CC  robust_av.c
  CC  wmm_ac.c
  CC  ubus.c
  CC  config_file.c
  CC  ../src/rsn_supp/wpa_ft.c
  CC  wnm_sta.c
  CC  ../src/rsn_supp/wpa.c
  CC  ../src/rsn_supp/preauth.c
  CC  ../src/rsn_supp/pmksa_cache.c
  CC  ../src/rsn_supp/wpa_ie.c
  CC  ../src/common/wpa_common.c
  CC  ibss_rsn.c
  CC  hs20_supplicant.c
  CC  interworking.c
  CC  ../src/eap_peer/eap_tls.c
  CC  ../src/eap_peer/eap_peap.c
  CC  ../src/eap_common/eap_peap_common.c
  CC  ../src/eap_peer/eap_ttls.c
  CC  ../src/eap_peer/eap_md5.c
  CC  ../src/eap_peer/eap_mschapv2.c
  CC  ../src/eap_peer/mschapv2.c
  CC  ../src/eap_peer/eap_gtc.c
  CC  ../src/eap_peer/eap_otp.c
  CC  ../src/eap_peer/eap_leap.c
  CC  ../src/eap_peer/eap_fast.c
  CC  ../src/eap_peer/eap_fast_pac.c
  CC  ../src/eap_common/eap_fast_common.c
  CC  wps_supplicant.c
  CC  ../src/utils/uuid.c
  CC  ../src/eap_peer/eap_wsc.c
  CC  ../src/eap_common/eap_wsc_common.c
  CC  ../src/wps/wps.c
  CC  ../src/wps/wps_common.c
  CC  ../src/wps/wps_attr_parse.c
  CC  ../src/wps/wps_attr_build.c
  CC  ../src/wps/wps_attr_process.c
  CC  ../src/wps/wps_dev_attr.c
  CC  ../src/wps/wps_enrollee.c
  CC  ../src/wps/wps_registrar.c
  CC  ../src/eapol_supp/eapol_supp_sm.c
  CC  ../src/eap_peer/eap.c
  CC  ../src/eap_peer/eap_methods.c
  CC  ../src/eap_server/eap_server.c
  CC  ../src/eap_server/eap_server_identity.c
  CC  ../src/eap_server/eap_server_methods.c
  CC  ../src/ap/wpa_auth.c
  CC  ../src/ap/wpa_auth_ie.c
  CC  ../src/ap/pmksa_cache_auth.c
  CC  ../src/crypto/ms_funcs.c
  CC  ../src/eap_common/chap.c
  CC  ../src/eap_peer/eap_tls_common.c
  CC  ../src/crypto/crypto_internal-rsa.c
  CC  ../src/crypto/tls_internal.c
  CC  ../src/tls/tlsv1_common.c
  CC  ../src/tls/tlsv1_record.c
  CC  ../src/tls/tlsv1_cred.c
  CC  ../src/tls/tlsv1_client.c
  CC  ../src/tls/tlsv1_client_write.c
  CC  ../src/tls/tlsv1_client_read.c
  CC  ../src/tls/tlsv1_client_ocsp.c
  CC  ../src/tls/rsa.c
  CC  ../src/tls/x509v3.c
  CC  ../src/tls/pkcs1.c
  CC  ../src/tls/pkcs5.c
  CC  ../src/tls/pkcs8.c
  CC  ../src/crypto/crypto_internal-cipher.c
  CC  ../src/crypto/crypto_internal-modexp.c
  CC  ../src/tls/bignum.c
  CC  ../src/crypto/crypto_internal.c
  CC  ../src/crypto/aes-internal.c
  CC  ../src/crypto/aes-internal-dec.c
  CC  ../src/crypto/aes-unwrap.c
  CC  ../src/crypto/aes-omac1.c
  CC  ../src/crypto/aes-wrap.c
  CC  ../src/crypto/aes-cbc.c
  CC  ../src/crypto/aes-internal-enc.c
  CC  ../src/crypto/md5.c
  CC  ../src/crypto/md5-internal.c
  CC  ../src/crypto/md4-internal.c
  CC  ../src/crypto/rc4.c
  CC  ../src/crypto/sha256.c
  CC  ../src/crypto/sha256-prf.c
  CC  ../src/crypto/sha256-internal.c
  CC  ../src/crypto/sha384-internal.c
  CC  ../src/crypto/sha512-internal.c
  CC  ../src/tls/asn1.c
  CC  ../src/crypto/dh_groups.c
  CC  ../src/crypto/dh_group5.c
  CC  ../src/common/ctrl_iface_common.c
  CC  ctrl_iface.c
  CC  ctrl_iface_unix.c
  CC  ../src/utils/base64.c
  CC  ../src/common/ieee802_11_common.c
  CC  ../src/common/hw_features_common.c
  CC  ../src/eap_common/eap_common.c
  CC  ../src/crypto/sha1.c
  CC  ../src/crypto/sha1-prf.c
  CC  ../src/crypto/sha1-internal.c
  CC  ../src/crypto/sha1-pbkdf2.c
  CC  ../src/crypto/sha1-tprf.c
  CC  ../src/crypto/sha1-tlsprf.c
  CC  ../src/crypto/des-internal.c
  CC  ../src/common/gas.c
  CC  gas_query.c
  CC  offchannel.c
  CC  ../src/drivers/driver_common.c
  CC  wpa_supplicant.c
  CC  events.c
  CC  bssid_ignore.c
  CC  wpas_glue.c
  CC  scan.c
  CC  main.c
  CC  ../src/drivers/driver_wext.c
  CC  ../src/drivers/driver_wired.c
  CC  ../src/drivers/driver_wired_common.c
  CC  ../src/drivers/netlink.c
  CC  ../src/drivers/linux_ioctl.c
  CC  ../src/drivers/drivers.c
  CC  ../src/l2_packet/l2_packet_linux.c
  LD  wpa_cli
  CC  .config
make[4]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/hostapd-wpad-full-internal/hostapd-2021-05-22-b102f19b/wpa_supplicant'
/openwrt/staging_dir/toolchain-arm_cortex-a7+neon-vfpv4_gcc-8.4.0_musl_eabi/lib/gcc/arm-openwrt-linux-muslgnueabi/8.4.0/../../../../arm-openwrt-linux-muslgnueabi/bin/ld: /openwrt/tmp/ccNcRLCZ.ltrans18.ltrans.o: in function `ap_sta_add':
<artificial>:(.text.ap_sta_add+0x1a4): undefined reference to `sta_track_claim_taxonomy_info'
collect2: error: ld returned 1 exit status
make[3]: *** [Makefile:689: /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/hostapd-wpad-full-internal/hostapd-2021-05-22-b102f19b/.built] Error 1
```
