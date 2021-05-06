---
title: "compile.8"
date: 2021-05-06 05:08:54.017880
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
make package/feeds/telephony/asterisk-opus/compile -j$(nproc) || make package/feeds/telephony/asterisk-opus/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/01-Makefile.patch using plaintext: 
patching file Makefile
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/asterisk-opus-2017-10-09-83e1b458'
ccache_cc -o codecs/codec_opus_open_source.so  -DAST_MODULE=\"codec_opus_open_source\"  -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/asterisk-opus-2017-10-09-83e1b458=asterisk-opus-2017-10-09-83e1b458 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DAST_MODULE_SELF_SYM=__internal_codec_opus_open_source_self -DPIC -fpic  -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include  -pthread -lopus -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  -shared -pthread -Wl,--warn-common codecs/codec_opus_open_source.c
codecs/codec_opus_open_source.c:39:10: fatal error: asterisk.h: No such file or directory
 #include "asterisk.h"
          ^~~~~~~~~~~~
compilation terminated.
make[4]: *** [Makefile:50: codecs/codec_opus_open_source.so] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/asterisk-opus-2017-10-09-83e1b458'
make[3]: *** [Makefile:64: /openwrt/build_dir/target-x86_64_musl/asterisk-opus-2017-10-09-83e1b458/.built] Error 2
```
