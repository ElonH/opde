---
title: "compile.37"
date: 2021-06-20 22:26:36.867386
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
make package/feeds/base/mt7601u-ap/compile -j$(nproc) || make package/feeds/base/mt7601u-ap/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-fix-control-reaches-end-of-non-void.patch using plaintext: 
patching file mcu/rtmp_mcu.c
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124'
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../os/linux/rt_profile.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap_mbss.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap.o
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap.c: In function 'DOT1X_InternalCmdAction':
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap.c:2217:2: warning: ISO C90 forbids variable length array 'FrameBuf' [-Wvla]
  UCHAR   FrameBuf[frame_len];
  ^~~~~
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap.c: In function 'DOT1X_EapTriggerAction':
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap.c:2278:2: warning: ISO C90 forbids variable length array 'FrameBuf' [-Wvla]
  UCHAR   FrameBuf[frame_len];
  ^~~~~
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap.c: In function 'APStartUp':
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap.c:722:1: warning: the frame size of 1032 bytes is larger than 1024 bytes [-Wframe-larger-than=]
 }
 ^
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap_assoc.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap_auth.o
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap_auth.c: In function 'APPeerDeauthReqAction':
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap_auth.c:166:5: warning: this 'if' clause does not guard... [-Wmisleading-indentation]
     if (!PeerDeauthReqSanity(pAd, Elem->Msg, Elem->MsgLen, Addr2, &SeqNum, &Reason))
     ^~
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap_auth.c:169:2: note: ...this statement, but the latter is misleadingly indented as if it were guarded by the 'if'
  pEntry = NULL;
  ^~~~~~
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap_connect.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap_mlme.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap_sanity.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap_sync.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap_wpa.o
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap_wpa.c: In function 'HandleCounterMeasure':
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap_wpa.c:566:5: warning: this 'if' clause does not guard... [-Wmisleading-indentation]
     if (!pEntry)
     ^~
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap_wpa.c:570:2: note: ...this statement, but the latter is misleadingly indented as if it were guarded by the 'if'
  if (IS_ENTRY_APCLI(pEntry))
  ^~
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap_wpa.c: In function 'RTMPHandleSTAKey':
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap_wpa.c:1298:62: warning: '<<' in boolean context, did you mean '<' ? [-Wint-in-bool-context]
     MICMsgLen = pSTAKey->Body_Len[1] | ((pSTAKey->Body_Len[0]<<8) && 0xff00);
                                         ~~~~~~~~~~~~~~~~~~~~~^~~~
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap_wpa.c:1342:5: warning: this 'else' clause does not guard... [-Wmisleading-indentation]
     else
     ^~~~
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap_wpa.c:1347:2: note: ...this statement, but the latter is misleadingly indented as if it were guarded by the 'else'
  if (pEntry->bDlsInit && !peerKeyInfo.Request) /*Benson add for big-endian 20081016 --> */
  ^~
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap_data.o
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap_data.c: In function 'APHandleRxDataFrame_Hdr_Trns':
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap_data.c:5213:30: warning: passing argument 2 of 'hex_dump' from incompatible pointer type [-Wincompatible-pointer-types]
  hex_dump("DataFrameHeader", pHeader, 36);
                              ^~~~~~~
In file included from /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/include/rtmp_os.h:42,
                 from /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/include/rtmp_comm.h:66,
                 from /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/include/rt_config.h:36,
                 from /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap_data.c:33:
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/include/os/rt_linux.h:698:41: note: expected 'unsigned char *' but argument is of type 'HEADER_802_11 *' {aka 'struct _HEADER_802_11 *'}
 void hex_dump(char *str, unsigned char *pSrcBufVA, unsigned int SrcBufLen);
                          ~~~~~~~~~~~~~~~^~~~~~~~~
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap_autoChSel.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap_qload.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap_cfg.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/crypt_md5.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/crypt_sha2.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/crypt_hmac.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/crypt_aes.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/crypt_arc4.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/mlme.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_wep.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/action.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_data.o
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_data.c: In function 'Indicate_Legacy_Packet_Hdr_Trns':
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_data.c:2327:31: warning: passing argument 2 of 'hex_dump' from incompatible pointer type [-Wincompatible-pointer-types]
  hex_dump("802_11_hdr", pRxBlk->pHeader, LENGTH_802_11);
                         ~~~~~~^~~~~~~~~
In file included from /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/include/rtmp_os.h:42,
                 from /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/include/rtmp_comm.h:66,
                 from /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/include/rt_config.h:36,
                 from /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_data.c:27:
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/include/os/rt_linux.h:698:41: note: expected 'unsigned char *' but argument is of type 'PHEADER_802_11' {aka 'struct _HEADER_802_11 *'}
 void hex_dump(char *str, unsigned char *pSrcBufVA, unsigned int SrcBufLen);
                          ~~~~~~~~~~~~~~~^~~~~~~~~
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/rtmp_init.o
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/rtmp_init.c: In function 'NICInitializeAsic':
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/rtmp_init.c:1560:1: warning: the frame size of 1032 bytes is larger than 1024 bytes [-Wframe-larger-than=]
 }
 ^
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/rtmp_init_inf.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_tkip.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_aes.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_sync.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/eeprom.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_sanity.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_info.o
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_info.c: In function 'GetEncryptType':
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_info.c:1756:5: warning: this 'if' clause does not guard... [-Wmisleading-indentation]
     if(enc == Ndis802_11Encryption3Enabled)
     ^~
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_info.c:1758:2: note: ...this statement, but the latter is misleadingly indented as if it were guarded by the 'if'
  if(enc == Ndis802_11Encryption4Enabled)
  ^~
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_info.c: In function 'GetAuthMode':
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_info.c:1772:5: warning: this 'if' clause does not guard... [-Wmisleading-indentation]
     if(auth == Ndis802_11AuthModeShared)
     ^~
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_info.c:1774:2: note: ...this statement, but the latter is misleadingly indented as if it were guarded by the 'if'
  if(auth == Ndis802_11AuthModeAutoSwitch)
  ^~
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_info.c:1784:5: warning: this 'if' clause does not guard... [-Wmisleading-indentation]
     if(auth == Ndis802_11AuthModeWPA2PSK)
     ^~
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_info.c:1786:2: note: ...this statement, but the latter is misleadingly indented as if it were guarded by the 'if'
  if(auth == Ndis802_11AuthModeWPA1WPA2)
  ^~
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_info.c: In function 'Show_PMK_Proc':
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_info.c:4426:5: warning: this 'for' clause does not guard... [-Wmisleading-indentation]
     for (idx = 0; idx < 32; idx++)
     ^~~
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_info.c:4429:2: note: ...this statement, but the latter is misleadingly indented as if it were guarded by the 'for'
  return 0;
  ^~~~~~
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_cfg.o
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_cfg.c: In function 'RT_CfgSetFixedTxPhyMode':
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_cfg.c:611:17: warning: this statement may fall through [-Wimplicit-fallthrough=]
     fix_tx_mode = value;
     ~~~~~~~~~~~~^~~~~~~
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_cfg.c:612:4: note: here
    default:
    ^~~~~~~
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_wpa.o
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_wpa.c: In function 'RTMPCheckWPAframe_Hdr_Trns':
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_wpa.c:3081:5: warning: this 'if' clause does not guard... [-Wmisleading-indentation]
     if(DataByteCount < (LENGTH_802_3 + LENGTH_EAPOL_H))
     ^~
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_wpa.c:3087:2: note: ...this statement, but the latter is misleadingly indented as if it were guarded by the 'if'
  pData += LENGTH_802_3;
  ^~~~~
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_radar.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/spectrum.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/rtmp_timer.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/rt_channel.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_profile.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_asic.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/scan.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_cmd.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/uapsd.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/ps.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../rate_ctrl/ra_ctrl.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../rate_ctrl/alg_legacy.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../rate_ctrl/alg_ags.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../chips/rtmp_chip.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/txpower.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mac/rtmp_mac.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mgmt/mgmt_hw.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mgmt/mgmt_entrytb.o
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mgmt/mgmt_entrytb.c: In function 'MacTableInsertEntry':
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mgmt/mgmt_entrytb.c:80:2: warning: this 'if' clause does not guard... [-Wmisleading-indentation]
  if (pAd->MacTab.Size >= MAX_LEN_OF_MAC_TABLE)
  ^~
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mgmt/mgmt_entrytb.c:83:3: note: ...this statement, but the latter is misleadingly indented as if it were guarded by the 'if'
   FirstWcid = 1;
   ^~~~~~~~~
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../phy/rtmp_phy.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../phy/rlt_phy.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../phy/rlt_rf.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/netif_block.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../rate_ctrl/alg_grp.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/ba_action.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mgmt/mgmt_ht.o
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mgmt/mgmt_ht.c: In function 'RTMPSetHT':
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mgmt/mgmt_ht.c:245:22: warning: this statement may fall through [-Wimplicit-fallthrough=]
    ht_cap->MCSSet[2] =  0xff;
    ~~~~~~~~~~~~~~~~~~^~~~~~~
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mgmt/mgmt_ht.c:246:3: note: here
   case 2:
   ^~~~
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mgmt/mgmt_ht.c:247:22: warning: this statement may fall through [-Wimplicit-fallthrough=]
    ht_cap->MCSSet[1] =  0xff;
    ~~~~~~~~~~~~~~~~~~^~~~~~~
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mgmt/mgmt_ht.c:248:3: note: here
   case 1:
   ^~~~
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mcu/rtmp_and.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap_mbss_inf.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/rt_os_util.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../os/linux/ap_ioctl.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../os/linux/rt_linux.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../os/linux/rt_main_dev.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap_dls.o
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap_dls.c: In function 'APPeerDlsTearDownAction':
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap_dls.c:310:5: warning: this 'if' clause does not guard... [-Wmisleading-indentation]
     if (!pSAEntry)
     ^~
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../ap/ap_dls.c:313:2: note: ...this statement, but the latter is misleadingly indented as if it were guarded by the 'if'
  pDAEntry = MacTableLookup(pAd, DA);
  ^~~~~~~~
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_mac_usb.o
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_mac_usb.c: In function 'RTMPAllocTxRxRingMemory':
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_mac_usb.c:550:31: warning: initialization of 'PTX_CONTEXT' {aka 'struct _TX_CONTEXT *'} from incompatible pointer type 'TX_CONTEXT (*)[2]' {aka 'struct _TX_CONTEXT (*)[2]'} [-Wincompatible-pointer-types]
  PTX_CONTEXT pNullContext   = &(pAd->NullContext);
                               ^
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_data_usb.o
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_data_usb.c: In function 'ComposeNullFrame':
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/cmm_data_usb.c:210:2: warning: ISO C90 forbids mixed declarations and code [-Wdeclaration-after-statement]
  PTX_CONTEXT pNullContext = &pAd->NullContext[0];
  ^~~~~~~~~~~
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/rtusb_io.o
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/rtusb_io.c: In function 'RTUSBEnqueueCmdFromNdis':
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/rtusb_io.c:821:2: warning: this 'if' clause does not guard... [-Wmisleading-indentation]
  if ((status != NDIS_STATUS_SUCCESS) || (cmdqelmt == NULL))
  ^~
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/rtusb_io.c:824:3: note: ...this statement, but the latter is misleadingly indented as if it were guarded by the 'if'
   cmdqelmt->buffer = NULL;
   ^~~~~~~~
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/rtusb_data.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/rtusb_bulk.o
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/rtusb_bulk.c: In function 'RTUSBCancelPendingBulkOutIRP':
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/rtusb_bulk.c:1676:15: warning: assignment to 'PTX_CONTEXT' {aka 'struct _TX_CONTEXT *'} from incompatible pointer type 'TX_CONTEXT (*)[2]' {aka 'struct _TX_CONTEXT (*)[2]'} [-Wincompatible-pointer-types]
  pNullContext = &(pAd->NullContext);
               ^
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../os/linux/rt_usb.o
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../os/linux/rt_usb.c: In function 'cmd_rsp_event_tasklet':
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../os/linux/rt_usb.c:558:22: warning: assignment to 'PCMD_RSP_CONTEXT' {aka 'struct _CMD_RSP_CONTEXT *'} from incompatible pointer type 'struct _RX_CONTEXT *' [-Wincompatible-pointer-types]
  pCmdRspEventContext = (PRX_CONTEXT)RTMP_USB_URB_DATA_GET(pUrb);
                      ^
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/ee_prom.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/ee_efuse.o
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/ee_efuse.c: In function 'rtmp_ee_efuse_write16':
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/ee_efuse.c:1463:5: warning: this 'else' clause does not guard... [-Wmisleading-indentation]
     else
     ^~~~
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/ee_efuse.c:1465:2: note: ...this statement, but the latter is misleadingly indented as if it were guarded by the 'else'
  return 0;
  ^~~~~~
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mcu/rtmp_mcu.o
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mcu/rtmp_mcu.c: In function 'MCUBurstWrite':
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mcu/rtmp_mcu.c:33:38: warning: passing argument 3 of 'RTUSBMultiWrite_nBytes' from incompatible pointer type [-Wincompatible-pointer-types]
  RTUSBMultiWrite_nBytes(pAd, Offset, Data, Cnt * 4, 64);
                                      ^~~~
In file included from /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/include/rt_config.h:62,
                 from /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mcu/rtmp_mcu.c:29:
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/include/rtmp.h:8258:41: note: expected 'PUCHAR' {aka 'unsigned char *'} but argument is of type 'UINT32 *' {aka 'unsigned int *'}
         IN      PUCHAR                  pData,
                 ~~~~~~~~~~~~~~~~~~~~~~~~^~~~~
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mcu/rtmp_mcu.c: In function 'ChipOpsMCUHook':
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mcu/rtmp_mcu.c:68:25: warning: assignment to 'VOID (*)(struct _RTMP_ADAPTER *, UINT32,  UINT32)' {aka 'void (*)(struct _RTMP_ADAPTER *, unsigned int,  unsigned int)'} from incompatible pointer type 'INT (*)(struct _RTMP_ADAPTER *, UINT32,  UINT32)' {aka 'int (*)(struct _RTMP_ADAPTER *, unsigned int,  unsigned int)'} [-Wincompatible-pointer-types]
   pChipOps->Calibration = AndesCalibrationOP;
                         ^
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mcu/rtmp_mcu.c:75:25: warning: assignment to 'INT (*)(struct _RTMP_ADAPTER *, RTMP_REG_PAIR *, UINT32)' {aka 'int (*)(struct _RTMP_ADAPTER *, struct _RTMP_REG_PAIR *, unsigned int)'} from incompatible pointer type 'INT (*)(struct _RTMP_ADAPTER *, UINT32,  ...)' {aka 'int (*)(struct _RTMP_ADAPTER *, unsigned int,  ...)'} [-Wincompatible-pointer-types]
   pChipOps->RandomWrite = AndesRandomWrite;
                         ^
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mcu/rtmp_mcu.c:76:27: warning: assignment to 'INT (*)(struct _RTMP_ADAPTER *, BANK_RF_REG_PAIR *, UINT32)' {aka 'int (*)(struct _RTMP_ADAPTER *, struct _BANK_RF_REG_PAIR *, unsigned int)'} from incompatible pointer type 'INT (*)(struct _RTMP_ADAPTER *, UINT32,  ...)' {aka 'int (*)(struct _RTMP_ADAPTER *, unsigned int,  ...)'} [-Wincompatible-pointer-types]
   pChipOps->RFRandomWrite = AndesRFRandomWrite;
                           ^
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mcu/rtmp_M51.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/rt_rf.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../chips/mt7601.o
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../chips/mt7601.c: In function 'MT7601_Init':
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../chips/mt7601.c:3090:24: warning: assignment to 'VOID (*)(struct _RTMP_ADAPTER *, UCHAR)' {aka 'void (*)(struct _RTMP_ADAPTER *, unsigned char)'} from incompatible pointer type 'NTSTATUS (*)(struct _RTMP_ADAPTER *, UCHAR)' {aka 'int (*)(struct _RTMP_ADAPTER *, unsigned char)'} [-Wincompatible-pointer-types]
  pChipOps->DisableTxRx = MT7601DisableTxRx;
                        ^
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mac/ral_omac.o
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mac/ral_omac.c: In function 'get_pkt_rssi_by_rxwi':
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mac/ral_omac.c:18:12: warning: this statement may fall through [-Wimplicit-fallthrough=]
    rssi[2] = rxwi->RxWIRSSI2;
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mac/ral_omac.c:19:3: note: here
   case 2:
   ^~~~
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mac/ral_omac.c:20:12: warning: this statement may fall through [-Wimplicit-fallthrough=]
    rssi[1] = rxwi->RxWIRSSI1;
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mac/ral_omac.c:21:3: note: here
   case 1:
   ^~~~
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mac/ral_omac.c: In function 'get_pkt_snr_by_rxwi':
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mac/ral_omac.c:56:11: warning: this statement may fall through [-Wimplicit-fallthrough=]
    snr[2] = rxwi->RxWISNR2;
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mac/ral_omac.c:57:3: note: here
   case 2:
   ^~~~
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mac/ral_omac.c:58:11: warning: this statement may fall through [-Wimplicit-fallthrough=]
    snr[1] = rxwi->RxWISNR1;
/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../mac/ral_omac.c:59:3: note: here
   case 1:
   ^~~~
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../os/linux/rt_usb_util.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../os/linux/usb_main_dev.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/rtusb_dev_id.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/../../common/frq_cal.o
  LD [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/mt7601Uap.o
  Building modules, stage 2.
  MODPOST 1 modules
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/mt7601Uap.mod.o
  LD [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/os/linux/mt7601Uap.ko
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124'
grep: /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/mt7601u-ap-2020-05-01-62430742/./Module.symvers: No such file or directory
Package kmod-mt7601u-ap is missing dependencies for the following libraries:
usbcore.ko
make[3]: *** [Makefile:78: /openwrt/bin/targets/ath79/generic/packages/kmod-mt7601u-ap_5.4.124+2020-05-01-62430742-1_mips_24kc.ipk] Error 1
```
