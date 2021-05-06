---
title: "compile.8"
date: 2021-05-06 05:08:54.019403
hidden: false
draft: false
weight: -8
---

build number: `8`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/telephony/dahdi-linux/compile -j$(nproc) || make package/feeds/telephony/dahdi-linux/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/003-fix-oslec-build.patch using plaintext: 
patching file drivers/dahdi/Kbuild

Applying ./patches/050-re-enable-ztdummy.patch using plaintext: 
patching file drivers/dahdi/Kbuild

Applying ./patches/070-no-firmware-blob-download.patch using plaintext: 
patching file Makefile

Applying ./patches/100-add-support-for-hfc-s-pci.patch using plaintext: 
patching file drivers/dahdi/Kbuild
patching file drivers/dahdi/Kconfig
patching file drivers/dahdi/hfcs/base.c
patching file drivers/dahdi/hfcs/dahdi_hfcs.h
patching file drivers/dahdi/hfcs/fifo.c
patching file drivers/dahdi/hfcs/fifo.h
patching file drivers/dahdi/hfcs/Kbuild

Applying ./patches/110-fix-uaccess_h-include.patch using plaintext: 
patching file drivers/dahdi/datamods/syncppp.c
patching file drivers/dahdi/wcb4xxp/base.c
patching file drivers/dahdi/xpp/mmapdrv.c
patching file drivers/dahdi/xpp/xpp_usb.c

Applying ./patches/120-pci-header.patch using plaintext: 
patching file include/dahdi/kernel.h

Applying ./patches/130-DAHLIN-371-pld-linux-math64.patch using plaintext: 
patching file drivers/dahdi/xpp/xbus-core.c
patching file drivers/dahdi/xpp/xbus-pcm.c
patching file drivers/dahdi/xpp/xbus-sysfs.c
patching file drivers/dahdi/xpp/xframe_queue.c
patching file drivers/dahdi/xpp/xpp_usb.c

Applying ./patches/140-Use-proc_ops-on-kernels-5.6.patch using plaintext: 
patching file drivers/dahdi/dahdi-base.c
patching file drivers/dahdi/dahdi_dynamic_ethmf.c
patching file drivers/dahdi/xpp/card_bri.c
patching file drivers/dahdi/xpp/card_fxo.c
patching file drivers/dahdi/xpp/card_fxs.c
patching file drivers/dahdi/xpp/xbus-core.c
patching file drivers/dahdi/xpp/xpp_dahdi.c
patching file drivers/dahdi/xpp/xpp_usb.c
patching file include/dahdi/kernel.h

Applying ./patches/141-Remove-support-for-32-bit-userspace-with-64-bit-kern.patch using plaintext: 
patching file drivers/dahdi/dahdi-base.c

Applying ./patches/142-Remove-checks-for-HAVE_UNLOCKED_IOCTL-for-kernel-5.9.patch using plaintext: 
patching file drivers/dahdi/dahdi-base.c
patching file drivers/dahdi/dahdi_transcode.c
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0'
make -C /openwrt/build_dir/target-x86_64_musl/linux-x86_64/linux-5.4.115 KBUILD_EXTMOD=/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi DAHDI_INCLUDE=/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/include DAHDI_MODULES_EXTRA=" " HOTPLUG_FIRMWARE=yes modules DAHDI_BUILD_ALL=m
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/linux-5.4.115'
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/hfcs/base.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/hfcs/fifo.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/hfcs/dahdi_hfcs.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/oct612x/octdeviceapi/oct6100api/oct6100_api/oct6100_adpcm_chan.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/oct612x/octdeviceapi/oct6100api/oct6100_api/oct6100_channel.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/oct612x/octdeviceapi/oct6100api/oct6100_api/oct6100_chip_open.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/oct612x/octdeviceapi/oct6100api/oct6100_api/oct6100_chip_stats.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/oct612x/octdeviceapi/oct6100api/oct6100_api/oct6100_conf_bridge.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/oct612x/octdeviceapi/oct6100api/oct6100_api/oct6100_debug.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/oct612x/octdeviceapi/oct6100api/oct6100_api/oct6100_events.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/oct612x/octdeviceapi/oct6100api/oct6100_api/oct6100_interrupts.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/oct612x/octdeviceapi/oct6100api/oct6100_api/oct6100_memory.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/oct612x/octdeviceapi/oct6100api/oct6100_api/oct6100_miscellaneous.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/oct612x/octdeviceapi/oct6100api/oct6100_api/oct6100_mixer.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/oct612x/octdeviceapi/oct6100api/oct6100_api/oct6100_phasing_tsst.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/oct612x/octdeviceapi/oct6100api/oct6100_api/oct6100_playout_buf.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/oct612x/octdeviceapi/oct6100api/oct6100_api/oct6100_remote_debug.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/oct612x/octdeviceapi/oct6100api/oct6100_api/oct6100_tlv.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/oct612x/octdeviceapi/oct6100api/oct6100_api/oct6100_tone_detection.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/oct612x/octdeviceapi/oct6100api/oct6100_api/oct6100_tsi_cnct.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/oct612x/octdeviceapi/oct6100api/oct6100_api/oct6100_tsst.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/oct612x/apilib/bt/octapi_bt0.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/oct612x/apilib/largmath/octapi_largmath.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/oct612x/apilib/llman/octapi_llman.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/oct612x/oct612x-user.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/oct612x/oct612x.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/voicebus/voicebus.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/voicebus/GpakCust.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/voicebus/GpakApi.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/voicebus/voicebus_net.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/voicebus/vpmoct.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/voicebus/dahdi_voicebus.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wcb4xxp/base.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wcb4xxp/wcb4xxp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wct4xxp/base.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wct4xxp/vpm450m.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wct4xxp/wct4xxp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wctc4xxp/base.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wctc4xxp/wctc4xxp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wctdm24xxp/base.o
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wctdm24xxp/base.c: In function 'wctdm_check_battery_lost':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wctdm24xxp/base.c:1957:3: warning: this statement may fall through [-Wimplicit-fallthrough=]
   mod_hooksig(wc, mod, DAHDI_RXSIG_ONHOOK);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wctdm24xxp/base.c:1958:2: note: here
  case BATTERY_PRESENT:
  ^~~~
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wctdm24xxp/base.c: In function 'wctdm_check_battery_present':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wctdm24xxp/base.c:2065:3: warning: this statement may fall through [-Wimplicit-fallthrough=]
   mod_hooksig(wc, mod, DAHDI_RXSIG_OFFHOOK);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wctdm24xxp/base.c:2066:2: note: here
  case BATTERY_LOST: /* intentional drop through */
  ^~~~
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wctdm24xxp/xhfc.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wctdm24xxp/wctdm24xxp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xbus-core.o
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xbus-core.c: In function 'xbus_fill_proc_queue':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xbus-core.c:1775:76: warning: format '%ld' expects argument of type 'long int', but argument 10 has type 's32' {aka 'int'} [-Wformat=]
   "%-15s: counts %3d, %3d, %3d worst %3d, overflows %3d worst_lag %02lld.%ld ms\n",
                                                                          ~~^
                                                                          %d
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xbus-core.c:1778:3:
   rem);
   ~~~                                                                       
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xbus-sysfs.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xbus-pcm.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xframe_queue.o
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xframe_queue.c: In function '__xframe_dump_queue':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xframe_queue.c:47:58: warning: format '%ld' expects argument of type 'long int', but argument 6 has type 's32' {aka 'int'} [-Wformat=]
   snprintf(prefix, ARRAY_SIZE(prefix), "  %3d> %5lld.%03ld msec",
                                                      ~~~~^
                                                      %03d
     i++, sec, rem);
               ~~~                                         
In file included from ./include/linux/printk.h:7,
                 from ./include/linux/kernel.h:15,
                 from ./include/linux/list.h:9,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xframe_queue.h:4,
                 from /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xframe_queue.c:2:
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xframe_queue.c: In function '__xframe_enqueue':
./include/linux/kern_levels.h:5:18: warning: format '%ld' expects argument of type 'long int', but argument 12 has type 's32' {aka 'int'} [-Wformat=]
 #define KERN_SOH "\001"  /* ASCII Start Of Header */
                  ^~~~~~
./include/linux/kern_levels.h:13:21: note: in expansion of macro 'KERN_SOH'
 #define KERN_NOTICE KERN_SOH "5" /* normal but significant condition */
                     ^~~~~~~~
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/dahdi_debug.h:30:9: note: in expansion of macro 'KERN_NOTICE'
  printk(KERN_ ## level "%s%s-%s: " fmt, \
         ^~~~~
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/dahdi_debug.h:57:26: note: in expansion of macro 'PRINTK'
 #define NOTICE(fmt, ...) PRINTK(NOTICE, "", fmt, ## __VA_ARGS__)
                          ^~~~~~
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xframe_queue.c:67:4: note: in expansion of macro 'NOTICE'
    NOTICE("Overflow of %-15s: counts %3d, %3d, %3d worst %3d, overflows %3d worst_lag %02lld.%ld ms\n",
    ^~~~~~
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xframe_queue.c:67:96: note: format string is defined here
    NOTICE("Overflow of %-15s: counts %3d, %3d, %3d worst %3d, overflows %3d worst_lag %02lld.%ld ms\n",
                                                                                              ~~^
                                                                                              %d
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xpp_dahdi.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xproto.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/card_global.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/dahdi_debug.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xpp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/card_fxs.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xpd_fxs.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/card_fxo.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xpd_fxo.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/card_pri.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xpd_pri.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/card_bri.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xpd_bri.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/card_echo.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xpd_echo.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xpp_usb.o
  VERIFY  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/init_card_1_30
  VERIFY  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/init_card_2_30
  VERIFY  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/init_card_3_30
  VERIFY  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/init_card_4_30
  HOSTCC  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/print_fxo_modes.o
  HOSTLD  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/print_fxo_modes
  GEN     /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/init_fxo_modes
  CHECK   /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/init_card_2_30
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi-base.o
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi-base.c: In function '__dahdi_hooksig_pvt':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi-base.c:8472:6: warning: this statement may fall through [-Wimplicit-fallthrough=]
   if (chan->txstate != DAHDI_TXSTATE_OFFHOOK) break;
      ^
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi-base.c:8488:5: note: here
     case DAHDI_SIG_FXSGS:  /* FXS Groundstart */
     ^~~~
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi-base.c:8499:6: warning: this statement may fall through [-Wimplicit-fallthrough=]
   if (rxsig == DAHDI_RXSIG_START) {
      ^
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi-base.c:8507:5: note: here
     case DAHDI_SIG_FXOLS: /* FXO Loopstart */
     ^~~~
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi-base.c: In function '__dahdi_process_getaudio_chunk':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi-base.c:7923:4: warning: this statement may fall through [-Wimplicit-fallthrough=]
    memset(txb + 1, txb[0], DAHDI_CHUNKSIZE - 1);
    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi-base.c:7925:3: note: here
   case DAHDI_CONF_CONF: /* Normal conference mode */
   ^~~~
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi-sysfs.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi-sysfs-chan.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi-version.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_dummy.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_dynamic.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_dynamic_loc.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_dynamic_eth.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_dynamic_ethmf.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_transcode.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wcte13xp-base.o
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wcte13xp-base.c: In function 't13x_set_linemode':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wcte13xp-base.c:1877:9: warning: this statement may fall through [-Wimplicit-fallthrough=]
   res = t13x_software_init(wc, J1);
         ^~~~~~~~~~~~~~~~~~~~~~~~~~
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wcte13xp-base.c:1878:2: note: here
  default:
  ^~~~~~~
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wcxb_spi.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wcxb.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wcxb_flash.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wcte13xp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wcte43x-base.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wcte43x.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wcaxx-base.o
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wcaxx-base.c: In function 'wcaxx_check_battery_lost':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wcaxx-base.c:1448:3: warning: this statement may fall through [-Wimplicit-fallthrough=]
   mod_hooksig(wc, mod, DAHDI_RXSIG_ONHOOK);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wcaxx-base.c:1449:2: note: here
  case BATTERY_PRESENT:
  ^~~~
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wcaxx-base.c: In function 'wcaxx_check_battery_present':
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wcaxx-base.c:1556:3: warning: this statement may fall through [-Wimplicit-fallthrough=]
   mod_hooksig(wc, mod, DAHDI_RXSIG_OFFHOOK);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wcaxx-base.c:1557:2: note: here
  case BATTERY_LOST: /* intentional drop through */
  ^~~~
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wcaxx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_echocan_jpah.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_echocan_sec.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_echocan_sec2.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_echocan_kb1.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_echocan_mg2.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_echocan_oslec.o
  Building modules, stage 2.
  MODPOST 30 modules
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi.ko
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_dummy.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_dummy.ko
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_dynamic.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_dynamic.ko
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_dynamic_eth.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_dynamic_eth.ko
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_dynamic_ethmf.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_dynamic_ethmf.ko
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_dynamic_loc.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_dynamic_loc.ko
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_echocan_jpah.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_echocan_jpah.ko
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_echocan_kb1.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_echocan_kb1.ko
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_echocan_mg2.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_echocan_mg2.ko
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_echocan_oslec.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_echocan_oslec.ko
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_echocan_sec.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_echocan_sec.ko
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_echocan_sec2.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_echocan_sec2.ko
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_transcode.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/dahdi_transcode.ko
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/hfcs/dahdi_hfcs.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/hfcs/dahdi_hfcs.ko
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/oct612x/oct612x.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/oct612x/oct612x.ko
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/voicebus/dahdi_voicebus.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/voicebus/dahdi_voicebus.ko
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wcaxx.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wcaxx.ko
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wcb4xxp/wcb4xxp.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wcb4xxp/wcb4xxp.ko
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wct4xxp/wct4xxp.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wct4xxp/wct4xxp.ko
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wctc4xxp/wctc4xxp.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wctc4xxp/wctc4xxp.ko
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wctdm24xxp/wctdm24xxp.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wctdm24xxp/wctdm24xxp.ko
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wcte13xp.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wcte13xp.ko
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wcte43x.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/wcte43x.ko
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xpd_bri.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xpd_bri.ko
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xpd_echo.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xpd_echo.ko
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xpd_fxo.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xpd_fxo.ko
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xpd_fxs.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xpd_fxs.ko
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xpd_pri.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xpd_pri.ko
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xpp.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xpp.ko
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xpp_usb.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0/drivers/dahdi/xpp/xpp_usb.ko
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/linux-5.4.115'
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/dahdi-linux-3.1.0'
Package kmod-dahdi is missing dependencies for the following libraries:
crc-ccitt.ko
make[3]: *** [Makefile:117: /openwrt/bin/targets/x86/64/packages/kmod-dahdi_5.4.115+3.1.0-5_x86_64.ipk] Error 1
```
