---
title: "compile.37"
date: 2021-06-20 22:27:32.460177
hidden: false
draft: false
weight: -37
---

build number: `37`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/hs20/compile -j$(nproc) || make package/feeds/packages/hs20/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/050-use-dm_ddf-v1_3_dtd.patch using plaintext: 
patching file hs20/server/spp_server.c

Applying ./patches/100-fix-hs20_spp_server-path.patch using plaintext: 
patching file hs20/server/www/spp.php

Applying ./patches/200-adapt-config-php.patch using plaintext: 
patching file hs20/server/www/config.php

Applying ./patches/300-paths-in-ca-setup-sh.patch using plaintext: 
patching file hs20/server/ca/setup.sh
make[4]: warning: jobserver unavailable: using -j1.  Add '+' to parent make rule.
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/hs20/hostapd-2020-06-08-5a8b3662/hostapd'
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
  CC  ../src/utils/eloop.c
  CC  ../src/utils/common.c
  CC  ../src/utils/wpa_debug.c
  CC  ../src/utils/wpabuf.c
  CC  ../src/utils/os_unix.c
  CC  ../src/utils/ip_addr.c
  CC  ../src/utils/crc32.c
  CC  ../src/common/ieee802_11_common.c
  CC  ../src/common/wpa_common.c
  CC  ../src/common/hw_features_common.c
  CC  ../src/eapol_auth/eapol_auth_sm.c
  CC  ../src/eapol_auth/eapol_auth_dump.c
  CC  ../src/radius/radius.c
  CC  ../src/radius/radius_client.c
  CC  ../src/radius/radius_das.c
  CC  ../src/ap/accounting.c
  CC  ../src/ap/vlan_init.c
  CC  ../src/ap/vlan_ifconfig.c
  CC  ../src/ap/vlan.c
  CC  ../src/common/ctrl_iface_common.c
  CC  ctrl_iface.c
  CC  ../src/ap/ctrl_iface_ap.c
  CC  ../src/drivers/driver_none.c
  CC  ../src/l2_packet/l2_packet_linux.c
  CC  ../src/eap_server/eap_server_tls.c
  CC  ../src/eap_server/eap_server_peap.c
  CC  ../src/eap_common/eap_peap_common.c
  CC  ../src/eap_server/eap_server_ttls.c
  CC  ../src/eap_server/eap_server_mschapv2.c
  CC  ../src/eap_server/eap_server_gtc.c
  CC  ../src/eap_server/eap_server_sim.c
  CC  ../src/eap_server/eap_server_aka.c
  CC  ../src/eap_common/eap_sim_common.c
  CC  ../src/eap_server/eap_sim_db.c
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
../src/crypto/tls_openssl.c:19:10: fatal error: openssl/ssl.h: No such file or directory
 #include <openssl/ssl.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
make[4]: *** [Makefile:1288: ../src/crypto/tls_openssl.o] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/hs20/hostapd-2020-06-08-5a8b3662/hostapd'
make[3]: *** [Makefile:145: /openwrt/build_dir/target-mips_24kc_musl/hs20/hostapd-2020-06-08-5a8b3662/.built] Error 2
```
