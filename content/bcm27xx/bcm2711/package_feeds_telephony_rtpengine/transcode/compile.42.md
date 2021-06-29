---
title: "compile.42"
date: 2021-06-29 09:28:26.575314
hidden: false
draft: false
weight: -42
---

build number: `42`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/telephony/rtpengine/compile -j$(nproc) || make package/feeds/telephony/rtpengine/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/01-cflags.patch using plaintext: 
patching file lib/lib.Makefile
patching file daemon/Makefile
patching file recording-daemon/Makefile
patching file iptables-extension/Makefile

Applying ./patches/04-prevent-systemd-detection.patch using plaintext: 
patching file lib/lib.Makefile

Applying ./patches/200-openssl-deprecated.patch using plaintext: 
patching file daemon/dtls.c
patching file lib/ssllib.c
make[4]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/kernel-module'
make -C /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/linux-5.4.123 M=/openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/kernel-module O=/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/linux-5.4.123 modules
make[5]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/linux-5.4.123'
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/kernel-module/xt_RTPENGINE.o
  Building modules, stage 2.
  MODPOST 1 modules
  CC [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/kernel-module/xt_RTPENGINE.mod.o
  LD [M]  /openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/kernel-module/xt_RTPENGINE.ko
make[5]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/linux-5.4.123'
make[4]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/kernel-module'
make[4]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/iptables-extension'
ccache_cc -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib  -O2 -Wall -Wstrict-prototypes -shared -fPIC -DRTPENGINE_VERSION="\"8.5.3.3\"" -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lxtables  -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3=rtpengine-mr8.5.3.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include  -o libxt_RTPENGINE.so libxt_RTPENGINE.c
make[4]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/iptables-extension'
make[4]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
../utils/const_str_hash < control_ng.c > control_ng.strhash.c
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
../utils/const_str_hash < sdp.c > sdp.strhash.c
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
../utils/const_str_hash < call_interfaces.c > call_interfaces.strhash.c
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
( echo '/******** GENERATED FILE ********/' && \
	cat ../lib/"loglib.c" ) > "loglib.c"
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
( echo '/******** GENERATED FILE ********/' && \
	cat ../lib/"auxlib.c" ) > "auxlib.c"
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
( echo '/******** GENERATED FILE ********/' && \
	cat ../lib/"rtplib.c" ) > "rtplib.c"
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
( echo '/******** GENERATED FILE ********/' && \
	cat ../lib/"str.c" ) > "str.c"
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
( echo '/******** GENERATED FILE ********/' && \
	cat ../lib/"socket.c" ) > "socket.c"
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
( echo '/******** GENERATED FILE ********/' && \
	cat ../lib/"streambuf.c" ) > "streambuf.c"
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
( echo '/******** GENERATED FILE ********/' && \
	cat ../lib/"ssllib.c" ) > "ssllib.c"
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
( echo '/******** GENERATED FILE ********/' && \
	cat ../lib/"dtmflib.c" ) > "dtmflib.c"
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
( echo '/******** GENERATED FILE ********/' && \
	cat ../lib/"codeclib.c" ) > "codeclib.c"
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
echo "Looking for usable alternative for fix_frame_channel_layout.h"; \
rm -f fix_frame_channel_layout-test{.c,}; \
ln -s ../lib/fix_frame_channel_layout-test.c; \
for x in ../lib/fix_frame_channel_layout-*.h; do \
	echo "Trying build with $x"; \
	rm -f "fix_frame_channel_layout.h"; \
	echo '/******** GENERATED FILE ********/' > "fix_frame_channel_layout.h"; \
	cat "$x" >> "fix_frame_channel_layout.h"; \
	make fix_frame_channel_layout-test && break; \
	echo "Failed build with $x"; \
	rm -f "fix_frame_channel_layout.h"; \
done; \
rm -f fix_frame_channel_layout-test{.c,}; \
test -f "fix_frame_channel_layout.h"
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
Looking for usable alternative for fix_frame_channel_layout.h
Trying build with ../lib/fix_frame_channel_layout-01.h
make[5]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
( echo '/******** GENERATED FILE ********/' && \
	cat ../lib/"resample.c" ) > "resample.c"
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
echo "Looking for usable alternative for dtmf_rx_fillin.h"; \
rm -f dtmf_rx_fillin-test{.c,}; \
ln -s ../lib/dtmf_rx_fillin-test.c; \
for x in ../lib/dtmf_rx_fillin-*.h; do \
	echo "Trying build with $x"; \
	rm -f "dtmf_rx_fillin.h"; \
	echo '/******** GENERATED FILE ********/' > "dtmf_rx_fillin.h"; \
	cat "$x" >> "dtmf_rx_fillin.h"; \
	make dtmf_rx_fillin-test && break; \
	echo "Failed build with $x"; \
	rm -f "dtmf_rx_fillin.h"; \
done; \
rm -f dtmf_rx_fillin-test{.c,}; \
test -f "dtmf_rx_fillin.h"
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
Looking for usable alternative for dtmf_rx_fillin.h
Trying build with ../lib/dtmf_rx_fillin-01.h
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
ccache_cc -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99   -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include     -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include/mysql/  -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99   -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include     -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include/mysql/  -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99   -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include     -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include/mysql/  -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3=rtpengine-mr8.5.3.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include  -M main.c kernel.c poller.c aux.c control_tcp.c call.c control_udp.c redis.c bencode.c cookie_cache.c udp_listener.c control_ng.strhash.c sdp.strhash.c stun.c rtcp.c crypto.c rtp.c call_interfaces.strhash.c dtls.c log.c cli.c graphite.c ice.c media_socket.c homer.c recording.c statistics.c cdr.c ssrc.c iptables.c tcp_listener.c codec.c load.c dtmf.c timerthread.c media_player.c jitter_buffer.c t38.c loglib.c auxlib.c rtplib.c str.c socket.c streambuf.c ssllib.c dtmflib.c codeclib.c resample.c  | sed -e 's/:/ .depend:/' > .depend
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
In file included from ../include/main.h:5,
                 from main.c:1:
../include/aux.h:11:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from kernel.c:1:
../include/kernel.h:7:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from poller.c:1:
../include/poller.h:9:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from aux.c:1:
../include/aux.h:11:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from control_tcp.c:1:
../include/control_tcp.h:10:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from call.c:1:
../include/call.h:8:10: fatal error: glib-object.h: No such file or directory
 #include <glib-object.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
In file included from control_udp.c:1:
../include/control_udp.h:9:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/compat.h:16,
                 from ../include/redis.h:8,
                 from redis.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/compat.h:16,
                 from ../include/bencode.h:7,
                 from bencode.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from cookie_cache.c:1:
../include/cookie_cache.h:5:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/udp_listener.h:5,
                 from udp_listener.c:1:
../include/poller.h:9:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from control_ng.strhash.c:144:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from sdp.strhash.c:184:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/compat.h:16,
                 from ../include/stun.h:8,
                 from stun.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/rtcp.h:4,
                 from rtcp.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from crypto.c:1:
../include/crypto.h:7:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/rtp.h:6,
                 from rtp.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from call_interfaces.strhash.c:239:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/compat.h:16,
                 from ../include/dtls.h:11,
                 from dtls.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from log.h:5,
                 from log.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
cli.c:9:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from log.h:5,
                 from graphite.c:19:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ice.c:1:
../include/ice.h:7:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from media_socket.c:1:
../include/media_socket.h:5:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:35,
                 from ../include/homer.h:4,
                 from homer.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/recording.h:15,
                 from recording.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from statistics.c:1:
../include/call.h:8:10: fatal error: glib-object.h: No such file or directory
 #include <glib-object.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:5,
                 from cdr.c:2:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ssrc.c:1:
../include/ssrc.h:6:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:35,
                 from ../include/iptables.h:5,
                 from iptables.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:35,
                 from ../include/tcp_listener.h:4,
                 from tcp_listener.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from codec.c:1:
../include/codec.h:5:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
load.c:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from dtmf.c:2:
../include/dtmf.h:5:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/timerthread.h:4,
                 from timerthread.c:1:
../include/obj.h:6:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/media_player.h:5,
                 from media_player.c:1:
../lib/auxlib.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/jitter_buffer.h:4,
                 from jitter_buffer.c:1:
../lib/auxlib.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:5,
                 from ../include/t38.h:41,
                 from t38.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from loglib.c:2:
../lib/loglib.h:5:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from auxlib.c:2:
../lib/auxlib.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:5,
                 from rtplib.c:2:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from str.c:2:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:35,
                 from socket.c:2:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from streambuf.c:2:
../lib/streambuf.h:8:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ssllib.c:5:
../lib/auxlib.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from dtmflib.c:2:
../lib/dtmflib.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/codeclib.h:20,
                 from codeclib.c:2:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/codeclib.h:20,
                 from ../lib/resample.h:5,
                 from resample.c:2:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
ccache_cc -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99   -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include     -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include/mysql/  -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99   -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include     -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include/mysql/  -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99   -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include     -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include/mysql/  -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3=rtpengine-mr8.5.3.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include   -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib   dtmf_rx_fillin-test.c  -lm   -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lz  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lpcre  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lcrypto  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lssl -lcrypto  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -levent_pthreads -levent  -lpcap -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib   -lxmlrpc_client -lxmlrpc  -lxmlrpc_xmlparse -lxmlrpc_xmltok -lxmlrpc_util -lpthread -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lcurl    -lhiredis  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lip4tc -lip6tc  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lavcodec  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lavformat  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lavutil  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lswresample  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lavfilter  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lspandsp  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lbcg729  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/ -lmariadb  -o dtmf_rx_fillin-test
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
ccache_cc -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99   -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include     -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include/mysql/  -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99   -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include     -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include/mysql/  -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3=rtpengine-mr8.5.3.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include  -M main.c kernel.c poller.c aux.c control_tcp.c call.c control_udp.c redis.c bencode.c cookie_cache.c udp_listener.c control_ng.strhash.c sdp.strhash.c stun.c rtcp.c crypto.c rtp.c call_interfaces.strhash.c dtls.c log.c cli.c graphite.c ice.c media_socket.c homer.c recording.c statistics.c cdr.c ssrc.c iptables.c tcp_listener.c codec.c load.c dtmf.c timerthread.c media_player.c jitter_buffer.c t38.c loglib.c auxlib.c rtplib.c str.c socket.c streambuf.c ssllib.c dtmflib.c codeclib.c resample.c  | sed -e 's/:/ .depend:/' > .depend
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
In file included from ../include/main.h:5,
                 from main.c:1:
../include/aux.h:11:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from kernel.c:1:
../include/kernel.h:7:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from poller.c:1:
../include/poller.h:9:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from aux.c:1:
../include/aux.h:11:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from control_tcp.c:1:
../include/control_tcp.h:10:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from call.c:1:
../include/call.h:8:10: fatal error: glib-object.h: No such file or directory
 #include <glib-object.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
In file included from control_udp.c:1:
../include/control_udp.h:9:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/compat.h:16,
                 from ../include/redis.h:8,
                 from redis.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/compat.h:16,
                 from ../include/bencode.h:7,
                 from bencode.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from cookie_cache.c:1:
../include/cookie_cache.h:5:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/udp_listener.h:5,
                 from udp_listener.c:1:
../include/poller.h:9:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from control_ng.strhash.c:144:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from sdp.strhash.c:184:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/compat.h:16,
                 from ../include/stun.h:8,
                 from stun.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/rtcp.h:4,
                 from rtcp.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from crypto.c:1:
../include/crypto.h:7:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/rtp.h:6,
                 from rtp.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from call_interfaces.strhash.c:239:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/compat.h:16,
                 from ../include/dtls.h:11,
                 from dtls.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from log.h:5,
                 from log.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
cli.c:9:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from log.h:5,
                 from graphite.c:19:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ice.c:1:
../include/ice.h:7:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from media_socket.c:1:
../include/media_socket.h:5:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:35,
                 from ../include/homer.h:4,
                 from homer.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/recording.h:15,
                 from recording.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from statistics.c:1:
../include/call.h:8:10: fatal error: glib-object.h: No such file or directory
 #include <glib-object.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:5,
                 from cdr.c:2:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ssrc.c:1:
../include/ssrc.h:6:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:35,
                 from ../include/iptables.h:5,
                 from iptables.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:35,
                 from ../include/tcp_listener.h:4,
                 from tcp_listener.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from codec.c:1:
../include/codec.h:5:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
load.c:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from dtmf.c:2:
../include/dtmf.h:5:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/timerthread.h:4,
                 from timerthread.c:1:
../include/obj.h:6:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/media_player.h:5,
                 from media_player.c:1:
../lib/auxlib.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/jitter_buffer.h:4,
                 from jitter_buffer.c:1:
../lib/auxlib.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:5,
                 from ../include/t38.h:41,
                 from t38.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from loglib.c:2:
../lib/loglib.h:5:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from auxlib.c:2:
../lib/auxlib.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:5,
                 from rtplib.c:2:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from str.c:2:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:35,
                 from socket.c:2:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from streambuf.c:2:
../lib/streambuf.h:8:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ssllib.c:5:
../lib/auxlib.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from dtmflib.c:2:
../lib/dtmflib.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/codeclib.h:20,
                 from codeclib.c:2:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/codeclib.h:20,
                 from ../lib/resample.h:5,
                 from resample.c:2:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
ccache_cc -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99   -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include     -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include/mysql/  -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99   -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include     -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include/mysql/  -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3=rtpengine-mr8.5.3.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include   -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib   fix_frame_channel_layout-test.c  -lm   -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lz  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lpcre  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lcrypto  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lssl -lcrypto  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -levent_pthreads -levent  -lpcap -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib   -lxmlrpc_client -lxmlrpc  -lxmlrpc_xmlparse -lxmlrpc_xmltok -lxmlrpc_util -lpthread -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lcurl    -lhiredis  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lip4tc -lip6tc  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lavcodec  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lavformat  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lavutil  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lswresample  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lavfilter  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lspandsp  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lbcg729  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/ -lmariadb  -o fix_frame_channel_layout-test
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
In file included from ../lib/compat.h:16,
                 from fix_frame_channel_layout.h:4,
                 from fix_frame_channel_layout-test.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
make[5]: *** [<builtin>: fix_frame_channel_layout-test] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
Failed build with ../lib/fix_frame_channel_layout-01.h
Trying build with ../lib/fix_frame_channel_layout-02.h
make[5]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
( echo '/******** GENERATED FILE ********/' && \
	cat ../lib/"resample.c" ) > "resample.c"
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
ccache_cc -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99   -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include     -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include/mysql/  -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99   -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include     -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include/mysql/  -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3=rtpengine-mr8.5.3.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include  -M main.c kernel.c poller.c aux.c control_tcp.c call.c control_udp.c redis.c bencode.c cookie_cache.c udp_listener.c control_ng.strhash.c sdp.strhash.c stun.c rtcp.c crypto.c rtp.c call_interfaces.strhash.c dtls.c log.c cli.c graphite.c ice.c media_socket.c homer.c recording.c statistics.c cdr.c ssrc.c iptables.c tcp_listener.c codec.c load.c dtmf.c timerthread.c media_player.c jitter_buffer.c t38.c loglib.c auxlib.c rtplib.c str.c socket.c streambuf.c ssllib.c dtmflib.c codeclib.c resample.c  | sed -e 's/:/ .depend:/' > .depend
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
In file included from ../include/main.h:5,
                 from main.c:1:
../include/aux.h:11:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from kernel.c:1:
../include/kernel.h:7:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from poller.c:1:
../include/poller.h:9:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from aux.c:1:
../include/aux.h:11:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from control_tcp.c:1:
../include/control_tcp.h:10:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from call.c:1:
../include/call.h:8:10: fatal error: glib-object.h: No such file or directory
 #include <glib-object.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
In file included from control_udp.c:1:
../include/control_udp.h:9:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/compat.h:16,
                 from ../include/redis.h:8,
                 from redis.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/compat.h:16,
                 from ../include/bencode.h:7,
                 from bencode.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from cookie_cache.c:1:
../include/cookie_cache.h:5:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/udp_listener.h:5,
                 from udp_listener.c:1:
../include/poller.h:9:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from control_ng.strhash.c:144:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from sdp.strhash.c:184:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/compat.h:16,
                 from ../include/stun.h:8,
                 from stun.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/rtcp.h:4,
                 from rtcp.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from crypto.c:1:
../include/crypto.h:7:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/rtp.h:6,
                 from rtp.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from call_interfaces.strhash.c:239:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/compat.h:16,
                 from ../include/dtls.h:11,
                 from dtls.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from log.h:5,
                 from log.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
cli.c:9:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from log.h:5,
                 from graphite.c:19:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ice.c:1:
../include/ice.h:7:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from media_socket.c:1:
../include/media_socket.h:5:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:35,
                 from ../include/homer.h:4,
                 from homer.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/recording.h:15,
                 from recording.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from statistics.c:1:
../include/call.h:8:10: fatal error: glib-object.h: No such file or directory
 #include <glib-object.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:5,
                 from cdr.c:2:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ssrc.c:1:
../include/ssrc.h:6:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:35,
                 from ../include/iptables.h:5,
                 from iptables.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:35,
                 from ../include/tcp_listener.h:4,
                 from tcp_listener.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from codec.c:1:
../include/codec.h:5:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
load.c:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from dtmf.c:2:
../include/dtmf.h:5:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/timerthread.h:4,
                 from timerthread.c:1:
../include/obj.h:6:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/media_player.h:5,
                 from media_player.c:1:
../lib/auxlib.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/jitter_buffer.h:4,
                 from jitter_buffer.c:1:
../lib/auxlib.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:5,
                 from ../include/t38.h:41,
                 from t38.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from loglib.c:2:
../lib/loglib.h:5:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from auxlib.c:2:
../lib/auxlib.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:5,
                 from rtplib.c:2:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from str.c:2:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:35,
                 from socket.c:2:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from streambuf.c:2:
../lib/streambuf.h:8:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ssllib.c:5:
../lib/auxlib.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from dtmflib.c:2:
../lib/dtmflib.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/codeclib.h:20,
                 from codeclib.c:2:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/codeclib.h:20,
                 from ../lib/resample.h:5,
                 from resample.c:2:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
ccache_cc -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99   -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include     -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include/mysql/  -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99   -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include     -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include/mysql/  -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3=rtpengine-mr8.5.3.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include   -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib   fix_frame_channel_layout-test.c  -lm   -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lz  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lpcre  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lcrypto  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lssl -lcrypto  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -levent_pthreads -levent  -lpcap -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib   -lxmlrpc_client -lxmlrpc  -lxmlrpc_xmlparse -lxmlrpc_xmltok -lxmlrpc_util -lpthread -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lcurl    -lhiredis  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lip4tc -lip6tc  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lavcodec  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lavformat  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lavutil  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lswresample  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lavfilter  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lspandsp  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lbcg729  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/ -lmariadb  -o fix_frame_channel_layout-test
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
In file included from ../lib/compat.h:16,
                 from fix_frame_channel_layout.h:4,
                 from fix_frame_channel_layout-test.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
make[5]: *** [<builtin>: fix_frame_channel_layout-test] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
Failed build with ../lib/fix_frame_channel_layout-02.h
Trying build with ../lib/fix_frame_channel_layout-03.h
make[5]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
( echo '/******** GENERATED FILE ********/' && \
	cat ../lib/"resample.c" ) > "resample.c"
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
ccache_cc -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99   -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include     -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include/mysql/  -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99   -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include     -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include/mysql/  -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3=rtpengine-mr8.5.3.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include  -M main.c kernel.c poller.c aux.c control_tcp.c call.c control_udp.c redis.c bencode.c cookie_cache.c udp_listener.c control_ng.strhash.c sdp.strhash.c stun.c rtcp.c crypto.c rtp.c call_interfaces.strhash.c dtls.c log.c cli.c graphite.c ice.c media_socket.c homer.c recording.c statistics.c cdr.c ssrc.c iptables.c tcp_listener.c codec.c load.c dtmf.c timerthread.c media_player.c jitter_buffer.c t38.c loglib.c auxlib.c rtplib.c str.c socket.c streambuf.c ssllib.c dtmflib.c codeclib.c resample.c  | sed -e 's/:/ .depend:/' > .depend
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
In file included from ../include/main.h:5,
                 from main.c:1:
../include/aux.h:11:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from kernel.c:1:
../include/kernel.h:7:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from poller.c:1:
../include/poller.h:9:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from aux.c:1:
../include/aux.h:11:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from control_tcp.c:1:
../include/control_tcp.h:10:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from call.c:1:
../include/call.h:8:10: fatal error: glib-object.h: No such file or directory
 #include <glib-object.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
In file included from control_udp.c:1:
../include/control_udp.h:9:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/compat.h:16,
                 from ../include/redis.h:8,
                 from redis.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/compat.h:16,
                 from ../include/bencode.h:7,
                 from bencode.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from cookie_cache.c:1:
../include/cookie_cache.h:5:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/udp_listener.h:5,
                 from udp_listener.c:1:
../include/poller.h:9:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from control_ng.strhash.c:144:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from sdp.strhash.c:184:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/compat.h:16,
                 from ../include/stun.h:8,
                 from stun.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/rtcp.h:4,
                 from rtcp.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from crypto.c:1:
../include/crypto.h:7:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/rtp.h:6,
                 from rtp.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from call_interfaces.strhash.c:239:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/compat.h:16,
                 from ../include/dtls.h:11,
                 from dtls.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from log.h:5,
                 from log.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
cli.c:9:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from log.h:5,
                 from graphite.c:19:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ice.c:1:
../include/ice.h:7:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from media_socket.c:1:
../include/media_socket.h:5:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:35,
                 from ../include/homer.h:4,
                 from homer.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/recording.h:15,
                 from recording.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from statistics.c:1:
../include/call.h:8:10: fatal error: glib-object.h: No such file or directory
 #include <glib-object.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:5,
                 from cdr.c:2:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ssrc.c:1:
../include/ssrc.h:6:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:35,
                 from ../include/iptables.h:5,
                 from iptables.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:35,
                 from ../include/tcp_listener.h:4,
                 from tcp_listener.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from codec.c:1:
../include/codec.h:5:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
load.c:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from dtmf.c:2:
../include/dtmf.h:5:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/timerthread.h:4,
                 from timerthread.c:1:
../include/obj.h:6:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/media_player.h:5,
                 from media_player.c:1:
../lib/auxlib.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/jitter_buffer.h:4,
                 from jitter_buffer.c:1:
../lib/auxlib.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:5,
                 from ../include/t38.h:41,
                 from t38.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from loglib.c:2:
../lib/loglib.h:5:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from auxlib.c:2:
../lib/auxlib.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:5,
                 from rtplib.c:2:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from str.c:2:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:35,
                 from socket.c:2:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from streambuf.c:2:
../lib/streambuf.h:8:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ssllib.c:5:
../lib/auxlib.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from dtmflib.c:2:
../lib/dtmflib.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/codeclib.h:20,
                 from codeclib.c:2:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/codeclib.h:20,
                 from ../lib/resample.h:5,
                 from resample.c:2:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
ccache_cc -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99   -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include     -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include/mysql/  -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99   -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include     -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include/mysql/  -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3=rtpengine-mr8.5.3.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include   -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib   fix_frame_channel_layout-test.c  -lm   -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lz  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lpcre  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lcrypto  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lssl -lcrypto  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -levent_pthreads -levent  -lpcap -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib   -lxmlrpc_client -lxmlrpc  -lxmlrpc_xmlparse -lxmlrpc_xmltok -lxmlrpc_util -lpthread -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lcurl    -lhiredis  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lip4tc -lip6tc  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lavcodec  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lavformat  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lavutil  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lswresample  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lavfilter  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lspandsp  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lbcg729  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/ -lmariadb  -o fix_frame_channel_layout-test
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
In file included from ../lib/compat.h:16,
                 from fix_frame_channel_layout.h:4,
                 from fix_frame_channel_layout-test.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
make[5]: *** [<builtin>: fix_frame_channel_layout-test] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
Failed build with ../lib/fix_frame_channel_layout-03.h
Trying build with ../lib/fix_frame_channel_layout-04.h
make[5]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
( echo '/******** GENERATED FILE ********/' && \
	cat ../lib/"resample.c" ) > "resample.c"
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
ccache_cc -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99   -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include     -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include/mysql/  -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99   -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include     -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include/mysql/  -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3=rtpengine-mr8.5.3.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include  -M main.c kernel.c poller.c aux.c control_tcp.c call.c control_udp.c redis.c bencode.c cookie_cache.c udp_listener.c control_ng.strhash.c sdp.strhash.c stun.c rtcp.c crypto.c rtp.c call_interfaces.strhash.c dtls.c log.c cli.c graphite.c ice.c media_socket.c homer.c recording.c statistics.c cdr.c ssrc.c iptables.c tcp_listener.c codec.c load.c dtmf.c timerthread.c media_player.c jitter_buffer.c t38.c loglib.c auxlib.c rtplib.c str.c socket.c streambuf.c ssllib.c dtmflib.c codeclib.c resample.c  | sed -e 's/:/ .depend:/' > .depend
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
In file included from ../include/main.h:5,
                 from main.c:1:
../include/aux.h:11:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from kernel.c:1:
../include/kernel.h:7:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from poller.c:1:
../include/poller.h:9:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from aux.c:1:
../include/aux.h:11:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from control_tcp.c:1:
../include/control_tcp.h:10:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from call.c:1:
../include/call.h:8:10: fatal error: glib-object.h: No such file or directory
 #include <glib-object.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
In file included from control_udp.c:1:
../include/control_udp.h:9:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/compat.h:16,
                 from ../include/redis.h:8,
                 from redis.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/compat.h:16,
                 from ../include/bencode.h:7,
                 from bencode.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from cookie_cache.c:1:
../include/cookie_cache.h:5:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/udp_listener.h:5,
                 from udp_listener.c:1:
../include/poller.h:9:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from control_ng.strhash.c:144:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from sdp.strhash.c:184:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/compat.h:16,
                 from ../include/stun.h:8,
                 from stun.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/rtcp.h:4,
                 from rtcp.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from crypto.c:1:
../include/crypto.h:7:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/rtp.h:6,
                 from rtp.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from call_interfaces.strhash.c:239:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/compat.h:16,
                 from ../include/dtls.h:11,
                 from dtls.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from log.h:5,
                 from log.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
cli.c:9:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from log.h:5,
                 from graphite.c:19:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ice.c:1:
../include/ice.h:7:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from media_socket.c:1:
../include/media_socket.h:5:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:35,
                 from ../include/homer.h:4,
                 from homer.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/recording.h:15,
                 from recording.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from statistics.c:1:
../include/call.h:8:10: fatal error: glib-object.h: No such file or directory
 #include <glib-object.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:5,
                 from cdr.c:2:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ssrc.c:1:
../include/ssrc.h:6:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:35,
                 from ../include/iptables.h:5,
                 from iptables.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:35,
                 from ../include/tcp_listener.h:4,
                 from tcp_listener.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from codec.c:1:
../include/codec.h:5:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
load.c:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from dtmf.c:2:
../include/dtmf.h:5:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/timerthread.h:4,
                 from timerthread.c:1:
../include/obj.h:6:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/media_player.h:5,
                 from media_player.c:1:
../lib/auxlib.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../include/jitter_buffer.h:4,
                 from jitter_buffer.c:1:
../lib/auxlib.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:5,
                 from ../include/t38.h:41,
                 from t38.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from loglib.c:2:
../lib/loglib.h:5:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from auxlib.c:2:
../lib/auxlib.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:5,
                 from rtplib.c:2:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from str.c:2:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:35,
                 from socket.c:2:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from streambuf.c:2:
../lib/streambuf.h:8:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ssllib.c:5:
../lib/auxlib.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from dtmflib.c:2:
../lib/dtmflib.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/codeclib.h:20,
                 from codeclib.c:2:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
In file included from ../lib/codeclib.h:20,
                 from ../lib/resample.h:5,
                 from resample.c:2:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
ccache_cc -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99   -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include     -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include/mysql/  -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99   -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include     -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include  -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/include/mysql/  -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3=rtpengine-mr8.5.3.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/include   -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/libintl-stub/lib   fix_frame_channel_layout-test.c  -lm   -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lz  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lpcre  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lcrypto  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lssl -lcrypto  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -levent_pthreads -levent  -lpcap -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib   -lxmlrpc_client -lxmlrpc  -lxmlrpc_xmlparse -lxmlrpc_xmltok -lxmlrpc_util -lpthread -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lcurl    -lhiredis  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lip4tc -lip6tc  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lavcodec  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lavformat  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lavutil  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lswresample  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lavfilter  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lspandsp  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib -lbcg729  -L/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/ -lmariadb  -o fix_frame_channel_layout-test
Package glib-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `glib-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'glib-2.0', required by 'virtual:world', not found
Package gthread-2.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gthread-2.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'gthread-2.0', required by 'virtual:world', not found
Package json-glib-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `json-glib-1.0.pc'
to the PKG_CONFIG_PATH environment variable
Package 'json-glib-1.0', required by 'virtual:world', not found
In file included from ../lib/compat.h:16,
                 from fix_frame_channel_layout.h:4,
                 from fix_frame_channel_layout-test.c:1:
../lib/str.h:4:10: fatal error: glib.h: No such file or directory
 #include <glib.h>
          ^~~~~~~~
compilation terminated.
make[5]: *** [<builtin>: fix_frame_channel_layout-test] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
Failed build with ../lib/fix_frame_channel_layout-04.h
Makefile:149: .depend: No such file or directory
make[4]: *** [../lib/common.Makefile:48: fix_frame_channel_layout.h] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
make[3]: *** [Makefile:277: /openwrt/build_dir/target-aarch64_cortex-a72_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/.built] Error 2
```
