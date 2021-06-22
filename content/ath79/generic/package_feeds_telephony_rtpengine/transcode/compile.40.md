---
title: "compile.40"
date: 2021-06-22 10:45:15.549948
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
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/kernel-module'
make -C /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124 M=/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/kernel-module O=/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124 modules
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124'
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/kernel-module/xt_RTPENGINE.o
  Building modules, stage 2.
  MODPOST 1 modules
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/kernel-module/xt_RTPENGINE.mod.o
  LD [M]  /openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/kernel-module/xt_RTPENGINE.ko
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.124'
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/kernel-module'
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/iptables-extension'
ccache_cc -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -O2 -Wall -Wstrict-prototypes -shared -fPIC -DRTPENGINE_VERSION="\"8.5.3.3\"" -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lxtables  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3=rtpengine-mr8.5.3.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -o libxt_RTPENGINE.so libxt_RTPENGINE.c
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/iptables-extension'
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
../utils/const_str_hash < control_ng.c > control_ng.strhash.c
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[4]: mysql_config: Command not found
../utils/const_str_hash < sdp.c > sdp.strhash.c
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[4]: mysql_config: Command not found
../utils/const_str_hash < call_interfaces.c > call_interfaces.strhash.c
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[4]: mysql_config: Command not found
( echo '/******** GENERATED FILE ********/' && \
	cat ../lib/"loglib.c" ) > "loglib.c"
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[4]: mysql_config: Command not found
( echo '/******** GENERATED FILE ********/' && \
	cat ../lib/"auxlib.c" ) > "auxlib.c"
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[4]: mysql_config: Command not found
( echo '/******** GENERATED FILE ********/' && \
	cat ../lib/"rtplib.c" ) > "rtplib.c"
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[4]: mysql_config: Command not found
( echo '/******** GENERATED FILE ********/' && \
	cat ../lib/"str.c" ) > "str.c"
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[4]: mysql_config: Command not found
( echo '/******** GENERATED FILE ********/' && \
	cat ../lib/"socket.c" ) > "socket.c"
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[4]: mysql_config: Command not found
( echo '/******** GENERATED FILE ********/' && \
	cat ../lib/"streambuf.c" ) > "streambuf.c"
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[4]: mysql_config: Command not found
( echo '/******** GENERATED FILE ********/' && \
	cat ../lib/"ssllib.c" ) > "ssllib.c"
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[4]: mysql_config: Command not found
( echo '/******** GENERATED FILE ********/' && \
	cat ../lib/"dtmflib.c" ) > "dtmflib.c"
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[4]: mysql_config: Command not found
( echo '/******** GENERATED FILE ********/' && \
	cat ../lib/"codeclib.c" ) > "codeclib.c"
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[4]: mysql_config: Command not found
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
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[4]: mysql_config: Command not found
Looking for usable alternative for fix_frame_channel_layout.h
Trying build with ../lib/fix_frame_channel_layout-01.h
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
( echo '/******** GENERATED FILE ********/' && \
	cat ../lib/"resample.c" ) > "resample.c"
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[5]: mysql_config: Command not found
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
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[5]: mysql_config: Command not found
Looking for usable alternative for dtmf_rx_fillin.h
Trying build with ../lib/dtmf_rx_fillin-01.h
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
ccache_cc -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3=rtpengine-mr8.5.3.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -M main.c kernel.c poller.c aux.c control_tcp.c call.c control_udp.c redis.c bencode.c cookie_cache.c udp_listener.c control_ng.strhash.c sdp.strhash.c stun.c rtcp.c crypto.c rtp.c call_interfaces.strhash.c dtls.c log.c cli.c graphite.c ice.c media_socket.c homer.c recording.c statistics.c cdr.c ssrc.c iptables.c tcp_listener.c codec.c load.c dtmf.c timerthread.c media_player.c jitter_buffer.c t38.c loglib.c auxlib.c rtplib.c str.c socket.c streambuf.c ssllib.c dtmflib.c codeclib.c resample.c  | sed -e 's/:/ .depend:/' > .depend
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
In file included from ../include/aux.h:21,
                 from ../include/main.h:5,
                 from main.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from kernel.c:14:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from poller.c:16:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from aux.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/control_tcp.h:12,
                 from control_tcp.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from call.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/control_udp.h:12,
                 from control_udp.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/redis.h:9,
                 from redis.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/cookie_cache.h:6,
                 from cookie_cache.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/udp_listener.h:7,
                 from udp_listener.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/control_ng.h:4,
                 from control_ng.strhash.c:151:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/sdp.h:6,
                 from sdp.strhash.c:191:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/stun.h:9,
                 from stun.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/rtcp.h:5,
                 from rtcp.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/crypto.h:10,
                 from crypto.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/crypto.h:10,
                 from rtp.c:9:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/call_interfaces.h:9,
                 from call_interfaces.strhash.c:246:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from dtls.c:1:
../include/dtls.h:7:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from log.h:6,
                 from log.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from cli.c:13:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from log.h:6,
                 from graphite.c:19:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/ice.h:11,
                 from ice.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/media_socket.h:9,
                 from media_socket.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/homer.h:4,
                 from homer.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/recording.h:16,
                 from recording.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from statistics.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:6,
                 from cdr.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/ssrc.h:8,
                 from ssrc.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/iptables.h:5,
                 from iptables.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/tcp_listener.h:4,
                 from tcp_listener.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/codec.h:8,
                 from codec.c:1:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from load.c:8:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/media_socket.h:9,
                 from dtmf.c:3:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/timerthread.h:4,
                 from timerthread.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/media_player.h:5,
                 from media_player.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/jitter_buffer.h:4,
                 from jitter_buffer.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:6,
                 from ../include/t38.h:41,
                 from t38.c:1:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from loglib.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from auxlib.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:6,
                 from rtplib.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from str.c:3:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from socket.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/streambuf.h:13,
                 from streambuf.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
ssllib.c:3:10: fatal error: openssl/ssl.h: No such file or directory
 #include <openssl/ssl.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from log.h:6,
                 from dtmflib.c:5:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from codeclib.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/resample.h:5,
                 from resample.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
Package libcrypto was not found in the pkg-config search path.
Perhaps you should add the directory containing `libcrypto.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libcrypto', required by 'virtual:world', not found
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
ccache_cc -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3=rtpengine-mr8.5.3.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include   -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib   dtmf_rx_fillin-test.c  -lm -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lglib-2.0  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lgthread-2.0 -pthread -lglib-2.0  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lz  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lpcre     -lpcap -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib   -lxmlrpc_client -lxmlrpc  -lxmlrpc_xmlparse -lxmlrpc_xmltok -lxmlrpc_util -lpthread    -lhiredis -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -ljson-glib-1.0 -lgio-2.0 -lgobject-2.0 -lglib-2.0  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lip4tc -lip6tc       -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lspandsp  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lbcg729   -o dtmf_rx_fillin-test
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ld: cannot find -lxmlrpc_client
collect2: error: ld returned 1 exit status
make[6]: *** [<builtin>: dtmf_rx_fillin-test] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
Failed build with ../lib/dtmf_rx_fillin-01.h
Trying build with ../lib/dtmf_rx_fillin-02.h
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
ccache_cc -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3=rtpengine-mr8.5.3.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -M main.c kernel.c poller.c aux.c control_tcp.c call.c control_udp.c redis.c bencode.c cookie_cache.c udp_listener.c control_ng.strhash.c sdp.strhash.c stun.c rtcp.c crypto.c rtp.c call_interfaces.strhash.c dtls.c log.c cli.c graphite.c ice.c media_socket.c homer.c recording.c statistics.c cdr.c ssrc.c iptables.c tcp_listener.c codec.c load.c dtmf.c timerthread.c media_player.c jitter_buffer.c t38.c loglib.c auxlib.c rtplib.c str.c socket.c streambuf.c ssllib.c dtmflib.c codeclib.c resample.c  | sed -e 's/:/ .depend:/' > .depend
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
In file included from ../include/aux.h:21,
                 from ../include/main.h:5,
                 from main.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from kernel.c:14:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from poller.c:16:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from aux.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/control_tcp.h:12,
                 from control_tcp.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from call.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/control_udp.h:12,
                 from control_udp.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/redis.h:9,
                 from redis.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/cookie_cache.h:6,
                 from cookie_cache.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/udp_listener.h:7,
                 from udp_listener.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/control_ng.h:4,
                 from control_ng.strhash.c:151:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/sdp.h:6,
                 from sdp.strhash.c:191:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/stun.h:9,
                 from stun.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/rtcp.h:5,
                 from rtcp.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/crypto.h:10,
                 from crypto.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/crypto.h:10,
                 from rtp.c:9:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/call_interfaces.h:9,
                 from call_interfaces.strhash.c:246:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from dtls.c:1:
../include/dtls.h:7:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from log.h:6,
                 from log.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from cli.c:13:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from log.h:6,
                 from graphite.c:19:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/ice.h:11,
                 from ice.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/media_socket.h:9,
                 from media_socket.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/homer.h:4,
                 from homer.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/recording.h:16,
                 from recording.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from statistics.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:6,
                 from cdr.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/ssrc.h:8,
                 from ssrc.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/iptables.h:5,
                 from iptables.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/tcp_listener.h:4,
                 from tcp_listener.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/codec.h:8,
                 from codec.c:1:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from load.c:8:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/media_socket.h:9,
                 from dtmf.c:3:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/timerthread.h:4,
                 from timerthread.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/media_player.h:5,
                 from media_player.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/jitter_buffer.h:4,
                 from jitter_buffer.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:6,
                 from ../include/t38.h:41,
                 from t38.c:1:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from loglib.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from auxlib.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:6,
                 from rtplib.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from str.c:3:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from socket.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/streambuf.h:13,
                 from streambuf.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
ssllib.c:3:10: fatal error: openssl/ssl.h: No such file or directory
 #include <openssl/ssl.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from log.h:6,
                 from dtmflib.c:5:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from codeclib.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/resample.h:5,
                 from resample.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
Package libcrypto was not found in the pkg-config search path.
Perhaps you should add the directory containing `libcrypto.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libcrypto', required by 'virtual:world', not found
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
ccache_cc -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3=rtpengine-mr8.5.3.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include   -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib   dtmf_rx_fillin-test.c  -lm -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lglib-2.0  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lgthread-2.0 -pthread -lglib-2.0  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lz  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lpcre     -lpcap -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib   -lxmlrpc_client -lxmlrpc  -lxmlrpc_xmlparse -lxmlrpc_xmltok -lxmlrpc_util -lpthread    -lhiredis -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -ljson-glib-1.0 -lgio-2.0 -lgobject-2.0 -lglib-2.0  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lip4tc -lip6tc       -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lspandsp  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lbcg729   -o dtmf_rx_fillin-test
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
In file included from dtmf_rx_fillin-test.c:1:
dtmf_rx_fillin.h:11:13: error: conflicting types for 'dtmf_rx_fillin'
 INLINE void dtmf_rx_fillin(dtmf_rx_state_t *dsp, int n) {
             ^~~~~~~~~~~~~~
In file included from dtmf_rx_fillin.h:8,
                 from dtmf_rx_fillin-test.c:1:
/openwrt/staging_dir/target-mips_24kc_musl/usr/include/spandsp/dtmf.h:179:19: note: previous declaration of 'dtmf_rx_fillin' was here
 SPAN_DECLARE(int) dtmf_rx_fillin(dtmf_rx_state_t *s, int samples);
                   ^~~~~~~~~~~~~~
make[6]: *** [<builtin>: dtmf_rx_fillin-test] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
Failed build with ../lib/dtmf_rx_fillin-02.h
Makefile:149: .depend: No such file or directory
make[5]: *** [../lib/common.Makefile:48: dtmf_rx_fillin.h] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
Failed build with ../lib/fix_frame_channel_layout-01.h
Trying build with ../lib/fix_frame_channel_layout-02.h
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
( echo '/******** GENERATED FILE ********/' && \
	cat ../lib/"resample.c" ) > "resample.c"
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[5]: mysql_config: Command not found
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
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[5]: mysql_config: Command not found
Looking for usable alternative for dtmf_rx_fillin.h
ln: failed to create symbolic link './dtmf_rx_fillin-test.c': File exists
Trying build with ../lib/dtmf_rx_fillin-01.h
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
ccache_cc -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3=rtpengine-mr8.5.3.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -M main.c kernel.c poller.c aux.c control_tcp.c call.c control_udp.c redis.c bencode.c cookie_cache.c udp_listener.c control_ng.strhash.c sdp.strhash.c stun.c rtcp.c crypto.c rtp.c call_interfaces.strhash.c dtls.c log.c cli.c graphite.c ice.c media_socket.c homer.c recording.c statistics.c cdr.c ssrc.c iptables.c tcp_listener.c codec.c load.c dtmf.c timerthread.c media_player.c jitter_buffer.c t38.c loglib.c auxlib.c rtplib.c str.c socket.c streambuf.c ssllib.c dtmflib.c codeclib.c resample.c  | sed -e 's/:/ .depend:/' > .depend
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
In file included from ../include/aux.h:21,
                 from ../include/main.h:5,
                 from main.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from kernel.c:14:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from poller.c:16:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from aux.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/control_tcp.h:12,
                 from control_tcp.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from call.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/control_udp.h:12,
                 from control_udp.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/redis.h:9,
                 from redis.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/cookie_cache.h:6,
                 from cookie_cache.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/udp_listener.h:7,
                 from udp_listener.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/control_ng.h:4,
                 from control_ng.strhash.c:151:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/sdp.h:6,
                 from sdp.strhash.c:191:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/stun.h:9,
                 from stun.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/rtcp.h:5,
                 from rtcp.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/crypto.h:10,
                 from crypto.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/crypto.h:10,
                 from rtp.c:9:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/call_interfaces.h:9,
                 from call_interfaces.strhash.c:246:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from dtls.c:1:
../include/dtls.h:7:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from log.h:6,
                 from log.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from cli.c:13:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from log.h:6,
                 from graphite.c:19:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/ice.h:11,
                 from ice.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/media_socket.h:9,
                 from media_socket.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/homer.h:4,
                 from homer.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/recording.h:16,
                 from recording.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from statistics.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:6,
                 from cdr.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/ssrc.h:8,
                 from ssrc.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/iptables.h:5,
                 from iptables.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/tcp_listener.h:4,
                 from tcp_listener.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/codec.h:8,
                 from codec.c:1:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from load.c:8:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/media_socket.h:9,
                 from dtmf.c:3:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/timerthread.h:4,
                 from timerthread.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/media_player.h:5,
                 from media_player.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/jitter_buffer.h:4,
                 from jitter_buffer.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:6,
                 from ../include/t38.h:41,
                 from t38.c:1:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from loglib.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from auxlib.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:6,
                 from rtplib.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from str.c:3:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from socket.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/streambuf.h:13,
                 from streambuf.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
ssllib.c:3:10: fatal error: openssl/ssl.h: No such file or directory
 #include <openssl/ssl.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from log.h:6,
                 from dtmflib.c:5:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from codeclib.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/resample.h:5,
                 from resample.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
Package libcrypto was not found in the pkg-config search path.
Perhaps you should add the directory containing `libcrypto.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libcrypto', required by 'virtual:world', not found
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
ccache_cc -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3=rtpengine-mr8.5.3.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include   -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib   dtmf_rx_fillin-test.c  -lm -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lglib-2.0  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lgthread-2.0 -pthread -lglib-2.0  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lz  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lpcre     -lpcap -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib   -lxmlrpc_client -lxmlrpc  -lxmlrpc_xmlparse -lxmlrpc_xmltok -lxmlrpc_util -lpthread    -lhiredis -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -ljson-glib-1.0 -lgio-2.0 -lgobject-2.0 -lglib-2.0  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lip4tc -lip6tc       -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lspandsp  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lbcg729   -o dtmf_rx_fillin-test
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ld: cannot find -lxmlrpc_client
collect2: error: ld returned 1 exit status
make[6]: *** [<builtin>: dtmf_rx_fillin-test] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
Failed build with ../lib/dtmf_rx_fillin-01.h
Trying build with ../lib/dtmf_rx_fillin-02.h
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
ccache_cc -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3=rtpengine-mr8.5.3.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -M main.c kernel.c poller.c aux.c control_tcp.c call.c control_udp.c redis.c bencode.c cookie_cache.c udp_listener.c control_ng.strhash.c sdp.strhash.c stun.c rtcp.c crypto.c rtp.c call_interfaces.strhash.c dtls.c log.c cli.c graphite.c ice.c media_socket.c homer.c recording.c statistics.c cdr.c ssrc.c iptables.c tcp_listener.c codec.c load.c dtmf.c timerthread.c media_player.c jitter_buffer.c t38.c loglib.c auxlib.c rtplib.c str.c socket.c streambuf.c ssllib.c dtmflib.c codeclib.c resample.c  | sed -e 's/:/ .depend:/' > .depend
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
In file included from ../include/aux.h:21,
                 from ../include/main.h:5,
                 from main.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from kernel.c:14:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from poller.c:16:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from aux.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/control_tcp.h:12,
                 from control_tcp.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from call.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/control_udp.h:12,
                 from control_udp.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/redis.h:9,
                 from redis.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/cookie_cache.h:6,
                 from cookie_cache.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/udp_listener.h:7,
                 from udp_listener.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/control_ng.h:4,
                 from control_ng.strhash.c:151:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/sdp.h:6,
                 from sdp.strhash.c:191:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/stun.h:9,
                 from stun.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/rtcp.h:5,
                 from rtcp.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/crypto.h:10,
                 from crypto.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/crypto.h:10,
                 from rtp.c:9:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/call_interfaces.h:9,
                 from call_interfaces.strhash.c:246:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from dtls.c:1:
../include/dtls.h:7:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from log.h:6,
                 from log.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from cli.c:13:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from log.h:6,
                 from graphite.c:19:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/ice.h:11,
                 from ice.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/media_socket.h:9,
                 from media_socket.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/homer.h:4,
                 from homer.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/recording.h:16,
                 from recording.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from statistics.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:6,
                 from cdr.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/ssrc.h:8,
                 from ssrc.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/iptables.h:5,
                 from iptables.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/tcp_listener.h:4,
                 from tcp_listener.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/codec.h:8,
                 from codec.c:1:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from load.c:8:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/media_socket.h:9,
                 from dtmf.c:3:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/timerthread.h:4,
                 from timerthread.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/media_player.h:5,
                 from media_player.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/jitter_buffer.h:4,
                 from jitter_buffer.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:6,
                 from ../include/t38.h:41,
                 from t38.c:1:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from loglib.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from auxlib.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:6,
                 from rtplib.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from str.c:3:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from socket.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/streambuf.h:13,
                 from streambuf.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
ssllib.c:3:10: fatal error: openssl/ssl.h: No such file or directory
 #include <openssl/ssl.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from log.h:6,
                 from dtmflib.c:5:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from codeclib.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/resample.h:5,
                 from resample.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
Package libcrypto was not found in the pkg-config search path.
Perhaps you should add the directory containing `libcrypto.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libcrypto', required by 'virtual:world', not found
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
ccache_cc -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3=rtpengine-mr8.5.3.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include   -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib   dtmf_rx_fillin-test.c  -lm -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lglib-2.0  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lgthread-2.0 -pthread -lglib-2.0  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lz  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lpcre     -lpcap -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib   -lxmlrpc_client -lxmlrpc  -lxmlrpc_xmlparse -lxmlrpc_xmltok -lxmlrpc_util -lpthread    -lhiredis -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -ljson-glib-1.0 -lgio-2.0 -lgobject-2.0 -lglib-2.0  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lip4tc -lip6tc       -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lspandsp  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lbcg729   -o dtmf_rx_fillin-test
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
In file included from dtmf_rx_fillin-test.c:1:
dtmf_rx_fillin.h:11:13: error: conflicting types for 'dtmf_rx_fillin'
 INLINE void dtmf_rx_fillin(dtmf_rx_state_t *dsp, int n) {
             ^~~~~~~~~~~~~~
In file included from dtmf_rx_fillin.h:8,
                 from dtmf_rx_fillin-test.c:1:
/openwrt/staging_dir/target-mips_24kc_musl/usr/include/spandsp/dtmf.h:179:19: note: previous declaration of 'dtmf_rx_fillin' was here
 SPAN_DECLARE(int) dtmf_rx_fillin(dtmf_rx_state_t *s, int samples);
                   ^~~~~~~~~~~~~~
make[6]: *** [<builtin>: dtmf_rx_fillin-test] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
Failed build with ../lib/dtmf_rx_fillin-02.h
make[5]: *** [../lib/common.Makefile:48: dtmf_rx_fillin.h] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
Failed build with ../lib/fix_frame_channel_layout-02.h
Trying build with ../lib/fix_frame_channel_layout-03.h
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
( echo '/******** GENERATED FILE ********/' && \
	cat ../lib/"resample.c" ) > "resample.c"
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[5]: mysql_config: Command not found
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
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[5]: mysql_config: Command not found
Looking for usable alternative for dtmf_rx_fillin.h
ln: failed to create symbolic link './dtmf_rx_fillin-test.c': File exists
Trying build with ../lib/dtmf_rx_fillin-01.h
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
ccache_cc -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3=rtpengine-mr8.5.3.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -M main.c kernel.c poller.c aux.c control_tcp.c call.c control_udp.c redis.c bencode.c cookie_cache.c udp_listener.c control_ng.strhash.c sdp.strhash.c stun.c rtcp.c crypto.c rtp.c call_interfaces.strhash.c dtls.c log.c cli.c graphite.c ice.c media_socket.c homer.c recording.c statistics.c cdr.c ssrc.c iptables.c tcp_listener.c codec.c load.c dtmf.c timerthread.c media_player.c jitter_buffer.c t38.c loglib.c auxlib.c rtplib.c str.c socket.c streambuf.c ssllib.c dtmflib.c codeclib.c resample.c  | sed -e 's/:/ .depend:/' > .depend
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
In file included from ../include/aux.h:21,
                 from ../include/main.h:5,
                 from main.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from kernel.c:14:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from poller.c:16:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from aux.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/control_tcp.h:12,
                 from control_tcp.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from call.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/control_udp.h:12,
                 from control_udp.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/redis.h:9,
                 from redis.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/cookie_cache.h:6,
                 from cookie_cache.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/udp_listener.h:7,
                 from udp_listener.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/control_ng.h:4,
                 from control_ng.strhash.c:151:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/sdp.h:6,
                 from sdp.strhash.c:191:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/stun.h:9,
                 from stun.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/rtcp.h:5,
                 from rtcp.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/crypto.h:10,
                 from crypto.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/crypto.h:10,
                 from rtp.c:9:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/call_interfaces.h:9,
                 from call_interfaces.strhash.c:246:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from dtls.c:1:
../include/dtls.h:7:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from log.h:6,
                 from log.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from cli.c:13:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from log.h:6,
                 from graphite.c:19:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/ice.h:11,
                 from ice.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/media_socket.h:9,
                 from media_socket.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/homer.h:4,
                 from homer.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/recording.h:16,
                 from recording.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from statistics.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:6,
                 from cdr.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/ssrc.h:8,
                 from ssrc.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/iptables.h:5,
                 from iptables.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/tcp_listener.h:4,
                 from tcp_listener.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/codec.h:8,
                 from codec.c:1:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from load.c:8:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/media_socket.h:9,
                 from dtmf.c:3:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/timerthread.h:4,
                 from timerthread.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/media_player.h:5,
                 from media_player.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/jitter_buffer.h:4,
                 from jitter_buffer.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:6,
                 from ../include/t38.h:41,
                 from t38.c:1:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from loglib.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from auxlib.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:6,
                 from rtplib.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from str.c:3:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from socket.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/streambuf.h:13,
                 from streambuf.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
ssllib.c:3:10: fatal error: openssl/ssl.h: No such file or directory
 #include <openssl/ssl.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from log.h:6,
                 from dtmflib.c:5:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from codeclib.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/resample.h:5,
                 from resample.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
Package libcrypto was not found in the pkg-config search path.
Perhaps you should add the directory containing `libcrypto.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libcrypto', required by 'virtual:world', not found
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
ccache_cc -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3=rtpengine-mr8.5.3.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include   -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib   dtmf_rx_fillin-test.c  -lm -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lglib-2.0  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lgthread-2.0 -pthread -lglib-2.0  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lz  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lpcre     -lpcap -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib   -lxmlrpc_client -lxmlrpc  -lxmlrpc_xmlparse -lxmlrpc_xmltok -lxmlrpc_util -lpthread    -lhiredis -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -ljson-glib-1.0 -lgio-2.0 -lgobject-2.0 -lglib-2.0  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lip4tc -lip6tc       -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lspandsp  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lbcg729   -o dtmf_rx_fillin-test
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ld: cannot find -lxmlrpc_client
collect2: error: ld returned 1 exit status
make[6]: *** [<builtin>: dtmf_rx_fillin-test] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
Failed build with ../lib/dtmf_rx_fillin-01.h
Trying build with ../lib/dtmf_rx_fillin-02.h
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
ccache_cc -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3=rtpengine-mr8.5.3.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -M main.c kernel.c poller.c aux.c control_tcp.c call.c control_udp.c redis.c bencode.c cookie_cache.c udp_listener.c control_ng.strhash.c sdp.strhash.c stun.c rtcp.c crypto.c rtp.c call_interfaces.strhash.c dtls.c log.c cli.c graphite.c ice.c media_socket.c homer.c recording.c statistics.c cdr.c ssrc.c iptables.c tcp_listener.c codec.c load.c dtmf.c timerthread.c media_player.c jitter_buffer.c t38.c loglib.c auxlib.c rtplib.c str.c socket.c streambuf.c ssllib.c dtmflib.c codeclib.c resample.c  | sed -e 's/:/ .depend:/' > .depend
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
In file included from ../include/aux.h:21,
                 from ../include/main.h:5,
                 from main.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from kernel.c:14:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from poller.c:16:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from aux.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/control_tcp.h:12,
                 from control_tcp.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from call.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/control_udp.h:12,
                 from control_udp.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/redis.h:9,
                 from redis.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/cookie_cache.h:6,
                 from cookie_cache.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/udp_listener.h:7,
                 from udp_listener.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/control_ng.h:4,
                 from control_ng.strhash.c:151:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/sdp.h:6,
                 from sdp.strhash.c:191:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/stun.h:9,
                 from stun.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/rtcp.h:5,
                 from rtcp.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/crypto.h:10,
                 from crypto.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/crypto.h:10,
                 from rtp.c:9:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/call_interfaces.h:9,
                 from call_interfaces.strhash.c:246:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from dtls.c:1:
../include/dtls.h:7:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from log.h:6,
                 from log.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from cli.c:13:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from log.h:6,
                 from graphite.c:19:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/ice.h:11,
                 from ice.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/media_socket.h:9,
                 from media_socket.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/homer.h:4,
                 from homer.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/recording.h:16,
                 from recording.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from statistics.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:6,
                 from cdr.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/ssrc.h:8,
                 from ssrc.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/iptables.h:5,
                 from iptables.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/tcp_listener.h:4,
                 from tcp_listener.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/codec.h:8,
                 from codec.c:1:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from load.c:8:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/media_socket.h:9,
                 from dtmf.c:3:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/timerthread.h:4,
                 from timerthread.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/media_player.h:5,
                 from media_player.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/jitter_buffer.h:4,
                 from jitter_buffer.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:6,
                 from ../include/t38.h:41,
                 from t38.c:1:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from loglib.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from auxlib.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:6,
                 from rtplib.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from str.c:3:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from socket.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/streambuf.h:13,
                 from streambuf.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
ssllib.c:3:10: fatal error: openssl/ssl.h: No such file or directory
 #include <openssl/ssl.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from log.h:6,
                 from dtmflib.c:5:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from codeclib.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/resample.h:5,
                 from resample.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
Package libcrypto was not found in the pkg-config search path.
Perhaps you should add the directory containing `libcrypto.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libcrypto', required by 'virtual:world', not found
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
ccache_cc -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3=rtpengine-mr8.5.3.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include   -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib   dtmf_rx_fillin-test.c  -lm -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lglib-2.0  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lgthread-2.0 -pthread -lglib-2.0  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lz  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lpcre     -lpcap -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib   -lxmlrpc_client -lxmlrpc  -lxmlrpc_xmlparse -lxmlrpc_xmltok -lxmlrpc_util -lpthread    -lhiredis -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -ljson-glib-1.0 -lgio-2.0 -lgobject-2.0 -lglib-2.0  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lip4tc -lip6tc       -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lspandsp  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lbcg729   -o dtmf_rx_fillin-test
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
In file included from dtmf_rx_fillin-test.c:1:
dtmf_rx_fillin.h:11:13: error: conflicting types for 'dtmf_rx_fillin'
 INLINE void dtmf_rx_fillin(dtmf_rx_state_t *dsp, int n) {
             ^~~~~~~~~~~~~~
In file included from dtmf_rx_fillin.h:8,
                 from dtmf_rx_fillin-test.c:1:
/openwrt/staging_dir/target-mips_24kc_musl/usr/include/spandsp/dtmf.h:179:19: note: previous declaration of 'dtmf_rx_fillin' was here
 SPAN_DECLARE(int) dtmf_rx_fillin(dtmf_rx_state_t *s, int samples);
                   ^~~~~~~~~~~~~~
make[6]: *** [<builtin>: dtmf_rx_fillin-test] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
Failed build with ../lib/dtmf_rx_fillin-02.h
make[5]: *** [../lib/common.Makefile:48: dtmf_rx_fillin.h] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
Failed build with ../lib/fix_frame_channel_layout-03.h
Trying build with ../lib/fix_frame_channel_layout-04.h
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
( echo '/******** GENERATED FILE ********/' && \
	cat ../lib/"resample.c" ) > "resample.c"
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[5]: mysql_config: Command not found
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
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[5]: mysql_config: Command not found
Looking for usable alternative for dtmf_rx_fillin.h
ln: failed to create symbolic link './dtmf_rx_fillin-test.c': File exists
Trying build with ../lib/dtmf_rx_fillin-01.h
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
ccache_cc -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3=rtpengine-mr8.5.3.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -M main.c kernel.c poller.c aux.c control_tcp.c call.c control_udp.c redis.c bencode.c cookie_cache.c udp_listener.c control_ng.strhash.c sdp.strhash.c stun.c rtcp.c crypto.c rtp.c call_interfaces.strhash.c dtls.c log.c cli.c graphite.c ice.c media_socket.c homer.c recording.c statistics.c cdr.c ssrc.c iptables.c tcp_listener.c codec.c load.c dtmf.c timerthread.c media_player.c jitter_buffer.c t38.c loglib.c auxlib.c rtplib.c str.c socket.c streambuf.c ssllib.c dtmflib.c codeclib.c resample.c  | sed -e 's/:/ .depend:/' > .depend
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
In file included from ../include/aux.h:21,
                 from ../include/main.h:5,
                 from main.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from kernel.c:14:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from poller.c:16:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from aux.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/control_tcp.h:12,
                 from control_tcp.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from call.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/control_udp.h:12,
                 from control_udp.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/redis.h:9,
                 from redis.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/cookie_cache.h:6,
                 from cookie_cache.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/udp_listener.h:7,
                 from udp_listener.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/control_ng.h:4,
                 from control_ng.strhash.c:151:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/sdp.h:6,
                 from sdp.strhash.c:191:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/stun.h:9,
                 from stun.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/rtcp.h:5,
                 from rtcp.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/crypto.h:10,
                 from crypto.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/crypto.h:10,
                 from rtp.c:9:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/call_interfaces.h:9,
                 from call_interfaces.strhash.c:246:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from dtls.c:1:
../include/dtls.h:7:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from log.h:6,
                 from log.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from cli.c:13:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from log.h:6,
                 from graphite.c:19:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/ice.h:11,
                 from ice.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/media_socket.h:9,
                 from media_socket.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/homer.h:4,
                 from homer.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/recording.h:16,
                 from recording.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from statistics.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:6,
                 from cdr.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/ssrc.h:8,
                 from ssrc.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/iptables.h:5,
                 from iptables.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/tcp_listener.h:4,
                 from tcp_listener.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/codec.h:8,
                 from codec.c:1:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from load.c:8:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/media_socket.h:9,
                 from dtmf.c:3:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/timerthread.h:4,
                 from timerthread.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/media_player.h:5,
                 from media_player.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/jitter_buffer.h:4,
                 from jitter_buffer.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:6,
                 from ../include/t38.h:41,
                 from t38.c:1:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from loglib.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from auxlib.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:6,
                 from rtplib.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from str.c:3:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from socket.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/streambuf.h:13,
                 from streambuf.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
ssllib.c:3:10: fatal error: openssl/ssl.h: No such file or directory
 #include <openssl/ssl.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from log.h:6,
                 from dtmflib.c:5:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from codeclib.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/resample.h:5,
                 from resample.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
Package libcrypto was not found in the pkg-config search path.
Perhaps you should add the directory containing `libcrypto.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libcrypto', required by 'virtual:world', not found
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
ccache_cc -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3=rtpengine-mr8.5.3.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include   -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib   dtmf_rx_fillin-test.c  -lm -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lglib-2.0  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lgthread-2.0 -pthread -lglib-2.0  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lz  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lpcre     -lpcap -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib   -lxmlrpc_client -lxmlrpc  -lxmlrpc_xmlparse -lxmlrpc_xmltok -lxmlrpc_util -lpthread    -lhiredis -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -ljson-glib-1.0 -lgio-2.0 -lgobject-2.0 -lglib-2.0  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lip4tc -lip6tc       -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lspandsp  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lbcg729   -o dtmf_rx_fillin-test
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ld: cannot find -lxmlrpc_client
collect2: error: ld returned 1 exit status
make[6]: *** [<builtin>: dtmf_rx_fillin-test] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
Failed build with ../lib/dtmf_rx_fillin-01.h
Trying build with ../lib/dtmf_rx_fillin-02.h
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
ccache_cc -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3=rtpengine-mr8.5.3.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -M main.c kernel.c poller.c aux.c control_tcp.c call.c control_udp.c redis.c bencode.c cookie_cache.c udp_listener.c control_ng.strhash.c sdp.strhash.c stun.c rtcp.c crypto.c rtp.c call_interfaces.strhash.c dtls.c log.c cli.c graphite.c ice.c media_socket.c homer.c recording.c statistics.c cdr.c ssrc.c iptables.c tcp_listener.c codec.c load.c dtmf.c timerthread.c media_player.c jitter_buffer.c t38.c loglib.c auxlib.c rtplib.c str.c socket.c streambuf.c ssllib.c dtmflib.c codeclib.c resample.c  | sed -e 's/:/ .depend:/' > .depend
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
In file included from ../include/aux.h:21,
                 from ../include/main.h:5,
                 from main.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from kernel.c:14:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from poller.c:16:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from aux.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/control_tcp.h:12,
                 from control_tcp.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from call.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/control_udp.h:12,
                 from control_udp.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/redis.h:9,
                 from redis.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/cookie_cache.h:6,
                 from cookie_cache.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/udp_listener.h:7,
                 from udp_listener.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/control_ng.h:4,
                 from control_ng.strhash.c:151:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/sdp.h:6,
                 from sdp.strhash.c:191:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/stun.h:9,
                 from stun.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/rtcp.h:5,
                 from rtcp.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/crypto.h:10,
                 from crypto.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/crypto.h:10,
                 from rtp.c:9:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/call_interfaces.h:9,
                 from call_interfaces.strhash.c:246:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from dtls.c:1:
../include/dtls.h:7:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from log.h:6,
                 from log.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from cli.c:13:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from log.h:6,
                 from graphite.c:19:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/ice.h:11,
                 from ice.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/media_socket.h:9,
                 from media_socket.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/homer.h:4,
                 from homer.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/recording.h:16,
                 from recording.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from statistics.c:1:
../include/call.h:15:10: fatal error: openssl/x509.h: No such file or directory
 #include <openssl/x509.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:6,
                 from cdr.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from ../include/ssrc.h:8,
                 from ssrc.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/iptables.h:5,
                 from iptables.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from ../include/tcp_listener.h:4,
                 from tcp_listener.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/codec.h:8,
                 from codec.c:1:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/aux.h:21,
                 from load.c:8:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/media_socket.h:9,
                 from dtmf.c:3:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from ./log.h:6,
                 from ../include/obj.h:93,
                 from ../include/timerthread.h:4,
                 from timerthread.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/media_player.h:5,
                 from media_player.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../include/jitter_buffer.h:4,
                 from jitter_buffer.c:1:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:6,
                 from ../include/t38.h:41,
                 from t38.c:1:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from loglib.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from auxlib.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/rtplib.h:6,
                 from rtplib.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from str.c:3:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/socket.h:108,
                 from socket.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/streambuf.h:13,
                 from streambuf.c:2:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
ssllib.c:3:10: fatal error: openssl/ssl.h: No such file or directory
 #include <openssl/ssl.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/loglib.h:9,
                 from log.h:6,
                 from dtmflib.c:5:
../lib/auxlib.h:7:10: fatal error: openssl/rand.h: No such file or directory
 #include <openssl/rand.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
In file included from codeclib.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from ../lib/resample.h:5,
                 from resample.c:2:
../lib/codeclib.h:41:10: fatal error: libswresample/swresample.h: No such file or directory
 #include <libswresample/swresample.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
Package libcrypto was not found in the pkg-config search path.
Perhaps you should add the directory containing `libcrypto.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libcrypto', required by 'virtual:world', not found
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
ccache_cc -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -g -Wall -Wstrict-prototypes -pthread -fno-strict-aliasing -std=c99 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -pthread -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/json-glib-1.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/glib-2.0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/glib-2.0/include -pthread  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_IPTABLES_OPTION -I. -I../kernel-module/ -I../lib/ -I../include/ -D_GNU_SOURCE      -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DWITH_TRANSCODING -DHAVE_BCG729 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include   -DRE_PLUGIN_DIR="\"/usr/lib/rtpengine\"" -DRTPENGINE_VERSION="\"8.5.3.3\"" -O3 -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3=rtpengine-mr8.5.3.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include   -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib   dtmf_rx_fillin-test.c  -lm -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lglib-2.0  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lgthread-2.0 -pthread -lglib-2.0  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lz  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lpcre     -lpcap -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib   -lxmlrpc_client -lxmlrpc  -lxmlrpc_xmlparse -lxmlrpc_xmltok -lxmlrpc_util -lpthread    -lhiredis -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -ljson-glib-1.0 -lgio-2.0 -lgobject-2.0 -lglib-2.0  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lip4tc -lip6tc       -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lspandsp  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lbcg729   -o dtmf_rx_fillin-test
Package openssl was not found in the pkg-config search path.
Perhaps you should add the directory containing `openssl.pc'
to the PKG_CONFIG_PATH environment variable
Package 'openssl', required by 'virtual:world', not found
Package libevent_pthreads was not found in the pkg-config search path.
Perhaps you should add the directory containing `libevent_pthreads.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libevent_pthreads', required by 'virtual:world', not found
Package libavcodec was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavcodec.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavcodec', required by 'virtual:world', not found
Package libavformat was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavformat.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavformat', required by 'virtual:world', not found
Package libavutil was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavutil.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavutil', required by 'virtual:world', not found
Package libswresample was not found in the pkg-config search path.
Perhaps you should add the directory containing `libswresample.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libswresample', required by 'virtual:world', not found
Package libavfilter was not found in the pkg-config search path.
Perhaps you should add the directory containing `libavfilter.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libavfilter', required by 'virtual:world', not found
make[6]: mysql_config: Command not found
In file included from dtmf_rx_fillin-test.c:1:
dtmf_rx_fillin.h:11:13: error: conflicting types for 'dtmf_rx_fillin'
 INLINE void dtmf_rx_fillin(dtmf_rx_state_t *dsp, int n) {
             ^~~~~~~~~~~~~~
In file included from dtmf_rx_fillin.h:8,
                 from dtmf_rx_fillin-test.c:1:
/openwrt/staging_dir/target-mips_24kc_musl/usr/include/spandsp/dtmf.h:179:19: note: previous declaration of 'dtmf_rx_fillin' was here
 SPAN_DECLARE(int) dtmf_rx_fillin(dtmf_rx_state_t *s, int samples);
                   ^~~~~~~~~~~~~~
make[6]: *** [<builtin>: dtmf_rx_fillin-test] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
Failed build with ../lib/dtmf_rx_fillin-02.h
make[5]: *** [../lib/common.Makefile:48: dtmf_rx_fillin.h] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
Failed build with ../lib/fix_frame_channel_layout-04.h
Makefile:149: .depend: No such file or directory
make[4]: *** [../lib/common.Makefile:48: fix_frame_channel_layout.h] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/daemon'
make[3]: *** [Makefile:277: /openwrt/build_dir/target-mips_24kc_musl/rtpengine-transcode/rtpengine-mr8.5.3.3/.built] Error 2
```
