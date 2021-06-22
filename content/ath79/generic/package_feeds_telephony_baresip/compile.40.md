---
title: "compile.40"
date: 2021-06-22 10:41:19.992598
hidden: false
draft: false
weight: -40
---

build number: `40`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/telephony/baresip/compile -j$(nproc) || make package/feeds/telephony/baresip/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/002-fix-rem-include.patch using plaintext: 
patching file Makefile
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0'
  CC [M]  build-mips/modules/account/account.o
  CC [M]  build-mips/modules/auloop/auloop.o
  CC [M]  build-mips/modules/b2bua/b2bua.o
  CC [M]  build-mips/modules/contact/contact.o
  CC [M]  build-mips/modules/ctrl_tcp/ctrl_tcp.o
  CC [M]  build-mips/modules/ctrl_tcp/tcp_netstring.o
  CC [M]  build-mips/modules/ctrl_tcp/./netstring/netstring.o
  CC [M]  build-mips/modules/debug_cmd/debug_cmd.o
  CC [M]  build-mips/modules/ebuacip/ebuacip.o
  CC [M]  build-mips/modules/echo/echo.o
  CC [M]  build-mips/modules/fakevideo/fakevideo.o
  CC [M]  build-mips/modules/httpd/httpd.o
  CC [M]  build-mips/modules/ice/ice.o
  CC [M]  build-mips/modules/menu/menu.o
  CC [M]  build-mips/modules/mwi/mwi.o
  CC [M]  build-mips/modules/natpmp/natpmp.o
  CC [M]  build-mips/modules/natpmp/libnatpmp.o
  CC [M]  build-mips/modules/presence/presence.o
  CC [M]  build-mips/modules/presence/subscriber.o
  CC [M]  build-mips/modules/presence/notifier.o
  CC [M]  build-mips/modules/presence/publisher.o
  CC [M]  build-mips/modules/selfview/selfview.o
  CC [M]  build-mips/modules/srtp/srtp.o
  CC [M]  build-mips/modules/srtp/sdes.o
  CC [M]  build-mips/modules/stun/stun.o
  CC [M]  build-mips/modules/turn/turn.o
  CC [M]  build-mips/modules/uuid/uuid.o
  CC [M]  build-mips/modules/vidbridge/vidbridge.o
  CC [M]  build-mips/modules/vidbridge/src.o
  CC [M]  build-mips/modules/vidbridge/disp.o
  CC [M]  build-mips/modules/vidinfo/draw.o
  CC [M]  build-mips/modules/vidinfo/vidinfo.o
  CC [M]  build-mips/modules/vidinfo/xga_font_data.o
  CC [M]  build-mips/modules/vidloop/vidloop.o
  CC [M]  build-mips/modules/vumeter/vumeter.o
  CC [M]  build-mips/modules/aubridge/aubridge.o
  CC [M]  build-mips/modules/aubridge/device.o
  CC [M]  build-mips/modules/aubridge/src.o
  CC [M]  build-mips/modules/aubridge/play.o
  CC [M]  build-mips/modules/aufile/aufile.o
  CC [M]  build-mips/modules/ausine/ausine.o
  CC [M]  build-mips/modules/alsa/alsa.o
  CC [M]  build-mips/modules/alsa/alsa_src.o
  CC [M]  build-mips/modules/alsa/alsa_play.o
  CC [M]  build-mips/modules/cons/cons.o
  CC [M]  build-mips/modules/evdev/evdev.o
  CC [M]  build-mips/modules/evdev/print.o
  CC [M]  build-mips/modules/g711/g711.o
  CC [M]  build-mips/modules/g722/g722.o
  CC [M]  build-mips/modules/g726/g726.o
  CC [M]  build-mips/modules/opus/decode.o
  CC [M]  build-mips/modules/opus/encode.o
  CC [M]  build-mips/modules/opus/opus.o
  CC [M]  build-mips/modules/opus/sdp.o
  CC [M]  build-mips/modules/oss/oss.o
  CC [M]  build-mips/modules/plc/plc.o
  CC [M]  build-mips/modules/portaudio/portaudio.o
  CC [M]  build-mips/modules/sndfile/sndfile.o
  CC [M]  build-mips/modules/stdio/stdio.o
  CC [M]  build-mips/modules/v4l2/v4l2.o
  CC [M]  build-mips/modules/v4l2_codec/v4l2_codec.o
  CC [M]  build-mips/modules/vp8/decode.o
  CC [M]  build-mips/modules/vp8/encode.o
  CC [M]  build-mips/modules/vp8/vp8.o
  CC [M]  build-mips/modules/vp8/sdp.o
  CC [M]  build-mips/modules/vp9/decode.o
  CC [M]  build-mips/modules/vp9/encode.o
  CC [M]  build-mips/modules/vp9/vp9.o
  CC [M]  build-mips/modules/vp9/sdp.o
  CC [M]  build-mips/modules/rtcpsummary/rtcpsummary.o
  CC      build-mips/src/account.o
  CC      build-mips/src/aucodec.o
  CC      build-mips/src/audio.o
  CC      build-mips/src/aufilt.o
  CC      build-mips/src/auframe.o
  CC      build-mips/src/aulevel.o
  CC      build-mips/src/auplay.o
  CC      build-mips/src/ausrc.o
  CC      build-mips/src/baresip.o
  CC      build-mips/src/call.o
  CC      build-mips/src/cmd.o
  CC      build-mips/src/conf.o
  CC      build-mips/src/config.o
  CC      build-mips/src/contact.o
  CC      build-mips/src/custom_hdrs.o
  CC      build-mips/src/event.o
  CC      build-mips/src/h264.o
  CC      build-mips/src/log.o
  CC      build-mips/src/mctrl.o
  CC      build-mips/src/mediadev.o
  CC      build-mips/src/menc.o
  CC      build-mips/src/message.o
  CC      build-mips/src/metric.o
  CC      build-mips/src/mnat.o
  CC      build-mips/src/module.o
  CC      build-mips/src/net.o
  CC      build-mips/src/play.o
  CC      build-mips/src/reg.o
  CC      build-mips/src/rtpext.o
  CC      build-mips/src/rtpstat.o
  CC      build-mips/src/sdp.o
  CC      build-mips/src/sipreq.o
  CC      build-mips/src/stream.o
  CC      build-mips/src/stunuri.o
  CC      build-mips/src/timer.o
  CC      build-mips/src/timestamp.o
  CC      build-mips/src/ua.o
  CC      build-mips/src/ui.o
  CC      build-mips/src/vidcodec.o
  CC      build-mips/src/video.o
  CC      build-mips/src/vidfilt.o
  CC      build-mips/src/vidisp.o
  CC      build-mips/src/vidsrc.o
  CC      build-mips/src/vidutil.o
  CC      build-mips/src/main.o
  LD [M]  account.so
  LD [M]  auloop.so
  LD [M]  b2bua.so
  LD [M]  contact.so
  LD [M]  ctrl_tcp.so
  LD [M]  debug_cmd.so
  LD [M]  ebuacip.so
  LD [M]  echo.so
  LD [M]  fakevideo.so
  LD [M]  httpd.so
  LD [M]  ice.so
  LD [M]  menu.so
  LD [M]  mwi.so
  LD [M]  natpmp.so
  LD [M]  presence.so
  LD [M]  selfview.so
  LD [M]  srtp.so
  LD [M]  stun.so
  LD [M]  turn.so
  LD [M]  uuid.so
  LD [M]  vidbridge.so
  LD [M]  vidinfo.so
  LD [M]  vidloop.so
  LD [M]  vumeter.so
  LD [M]  aubridge.so
  LD [M]  aufile.so
  LD [M]  ausine.so
  LD [M]  alsa.so
  LD [M]  cons.so
  LD [M]  evdev.so
  LD [M]  g711.so
  LD [M]  g722.so
  LD [M]  g726.so
  LD [M]  opus.so
  LD [M]  oss.so
  LD [M]  plc.so
  LD [M]  portaudio.so
  LD [M]  sndfile.so
  LD [M]  stdio.so
  LD [M]  v4l2.so
  LD [M]  v4l2_codec.so
  LD [M]  vp8.so
  LD [M]  vp9.so
  LD [M]  rtcpsummary.so
  LD      baresip
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0'
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0'
install -m 0755 baresip /openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0/ipkg-install/usr/bin
install -m 0644 account.so auloop.so b2bua.so contact.so ctrl_tcp.so debug_cmd.so ebuacip.so echo.so fakevideo.so httpd.so ice.so menu.so mwi.so natpmp.so presence.so selfview.so srtp.so stun.so turn.so uuid.so vidbridge.so vidinfo.so vidloop.so vumeter.so aubridge.so aufile.so ausine.so alsa.so cons.so evdev.so g711.so g722.so g726.so opus.so oss.so plc.so portaudio.so sndfile.so stdio.so v4l2.so v4l2_codec.so vp8.so vp9.so rtcpsummary.so /openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0/ipkg-install/usr/lib/baresip/modules
install -m 0644 share/* /openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0/ipkg-install/usr/share/baresip
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0'
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0/ipkg-mips_24kc/baresip/usr/bin/baresip: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0/ipkg-mips_24kc/baresip/usr/lib/baresip/modules/stun.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0/ipkg-mips_24kc/baresip/usr/lib/baresip/modules/contact.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0/ipkg-mips_24kc/baresip/usr/lib/baresip/modules/auloop.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0/ipkg-mips_24kc/baresip/usr/lib/baresip/modules/ice.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0/ipkg-mips_24kc/baresip/usr/lib/baresip/modules/menu.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0/ipkg-mips_24kc/baresip/usr/lib/baresip/modules/turn.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0/ipkg-mips_24kc/baresip/usr/lib/baresip/modules/account.so: shared object
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0/ipkg-mips_24kc/baresip into /openwrt/bin/packages/mips_24kc/telephony/baresip_1.0.0-1_mips_24kc.ipk
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0/ipkg-mips_24kc/baresip-mod-alsa/usr/lib/baresip/modules/alsa.so: shared object
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0/ipkg-mips_24kc/baresip-mod-alsa into /openwrt/bin/packages/mips_24kc/telephony/baresip-mod-alsa_1.0.0-1_mips_24kc.ipk
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0/ipkg-mips_24kc/baresip-mod-aubridge/usr/lib/baresip/modules/aubridge.so: shared object
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0/ipkg-mips_24kc/baresip-mod-aubridge into /openwrt/bin/packages/mips_24kc/telephony/baresip-mod-aubridge_1.0.0-1_mips_24kc.ipk
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0/ipkg-mips_24kc/baresip-mod-aufile/usr/lib/baresip/modules/aufile.so: shared object
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0/ipkg-mips_24kc/baresip-mod-aufile into /openwrt/bin/packages/mips_24kc/telephony/baresip-mod-aufile_1.0.0-1_mips_24kc.ipk
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0/ipkg-mips_24kc/baresip-mod-b2bua/usr/lib/baresip/modules/b2bua.so: shared object
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0/ipkg-mips_24kc/baresip-mod-b2bua into /openwrt/bin/packages/mips_24kc/telephony/baresip-mod-b2bua_1.0.0-1_mips_24kc.ipk
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0/ipkg-mips_24kc/baresip-mod-cons/usr/lib/baresip/modules/cons.so: shared object
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0/ipkg-mips_24kc/baresip-mod-cons into /openwrt/bin/packages/mips_24kc/telephony/baresip-mod-cons_1.0.0-1_mips_24kc.ipk
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0/ipkg-mips_24kc/baresip-mod-ctrl-tcp/usr/lib/baresip/modules/ctrl_tcp.so: shared object
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0/ipkg-mips_24kc/baresip-mod-ctrl-tcp into /openwrt/bin/packages/mips_24kc/telephony/baresip-mod-ctrl-tcp_1.0.0-1_mips_24kc.ipk
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0/ipkg-mips_24kc/baresip-mod-debug-cmd/usr/lib/baresip/modules/debug_cmd.so: shared object
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0/ipkg-mips_24kc/baresip-mod-debug-cmd into /openwrt/bin/packages/mips_24kc/telephony/baresip-mod-debug-cmd_1.0.0-1_mips_24kc.ipk
install: cannot stat '/openwrt/build_dir/target-mips_24kc_musl/baresip-1.0.0/ipkg-install/usr/lib/baresip/modules/dtls_srtp.so': No such file or directory
make[3]: *** [Makefile:187: /openwrt/bin/packages/mips_24kc/telephony/baresip-mod-dtls-srtp_1.0.0-1_mips_24kc.ipk] Error 1
```
