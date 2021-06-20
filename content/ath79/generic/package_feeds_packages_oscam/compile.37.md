---
title: "compile.37"
date: 2021-06-20 22:26:36.900600
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
make package/feeds/packages/oscam/compile -j$(nproc) || make package/feeds/packages/oscam/compile V=s
```

#### Compile.txt

``` bash
[WARN] Unknown parameter: --target=mips-openwrt-linux
[WARN] Unknown parameter: --host=mips-openwrt-linux
[WARN] Unknown parameter: --build=x86_64-pc-linux-gnu
[WARN] Unknown parameter: --program-prefix=
[WARN] Unknown parameter: --program-suffix=
[WARN] Unknown parameter: --prefix=/usr
[WARN] Unknown parameter: --exec-prefix=/usr
[WARN] Unknown parameter: --bindir=/usr/bin
[WARN] Unknown parameter: --sbindir=/usr/sbin
[WARN] Unknown parameter: --libexecdir=/usr/lib
[WARN] Unknown parameter: --sysconfdir=/etc
[WARN] Unknown parameter: --datadir=/usr/share
[WARN] Unknown parameter: --localstatedir=/var
[WARN] Unknown parameter: --mandir=/usr/man
[WARN] Unknown parameter: --infodir=/usr/info
[WARN] Unknown parameter: --disable-nls
Disable WITH_SSL
Disable CARDREADER_SC8IN1
Disable CARDREADER_SMARGO
Enable TOUCH
Enable CS_ANTICASC
Enable CW_CYCLE_CHECK
Enable CLOCKFIX
Enable MODULE_CAMD33
Enable MODULE_RADEGAST
Enable MODULE_SERIAL
Enable MODULE_CONSTCW
Enable MODULE_PANDORA
Enable MODULE_GHTTP
Enable CARDREADER_SC8IN1
Enable CARDREADER_MP35
Enable CARDREADER_SMARGO
Enable CARDREADER_DRECAS
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/oscam-2020-12-12-aafda4bc'
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
+-------------------------------------------------------------------------------
| OSCam ver: 1.20_svn rev: 11677_908ce target: mips-openwrt-linux-musl-ssl-libusb-pcsc
| Tools:
|  CROSS    = mips-openwrt-linux-musl-
|  CC       = ccache_cc
| Settings:
|  CONF_DIR = /etc/oscam
|  CC_OPTS  = -O2 -ggdb -pipe -ffunction-sections -fdata-sections
|  CC_WARN  = -W -Wall -Wshadow -Wredundant-decls -Wstrict-prototypes -Wold-style-definition
|  CFLAGS   = -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/oscam-2020-12-12-aafda4bc=oscam-2020-12-12-aafda4bc -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -fexpensive-optimizations -DWITH_SSL=1 -DWITH_LIBCRYPTO=1 -DWITH_LIBUSB=1 -DWITH_PCSC=1 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/PCSC -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/../local/include/PCSC
|  LDFLAGS  = -Wl,--gc-sections -DWITH_SSL=1 -DWITH_LIBCRYPTO=1 -DWITH_LIBUSB=1 -DWITH_PCSC=1 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/PCSC -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/../local/include/PCSC
|  LIBS     = -lssl -lcrypto -lusb-1.0 -lrt -lpcsclite -lm -lpthread -ldl -lrt
|  UseFlags = USE_SSL=1 USE_LIBCRYPTO=1 USE_LIBUSB=1 USE_PCSC=1
| Config:
|  Addons   : WEBIF WEBIF_LIVELOG WEBIF_JQUERY TOUCH WITH_SSL HAVE_DVBAPI READ_SDT_CHARSETS IRDETO_GUESSING CS_ANTICASC WITH_DEBUG MODULE_MONITOR WITH_LB CW_CYCLE_CHECK CLOCKFIX WITH_EMU WITH_SOFTCAM
|  Protocols: CAMD33 CAMD35 CAMD35_TCP NEWCAMD CCCAM CCCSHARE GBOX RADEGAST SCAM SERIAL CONSTCW PANDORA GHTTP
|  Readers  : NAGRA NAGRA_MERLIN IRDETO CONAX CRYPTOWORKS SECA VIACCESS VIDEOGUARD DRE TONGFANG STREAMGUARD JET BULCRYPT GRIFFIN DGCRYPT
|  CardRdrs : PHOENIX INTERNAL SC8IN1 MP35 SMARGO STINGER DRECAS SMART PCSC
|  Compiler : mips-openwrt-linux-musl-gcc (OpenWrt GCC 8.4.0 r0-91deb05) 8.4.0
|  Config   : build/mips-openwrt-linux-musl-ssl-libusb-pcsc/config.mak
|  Binary   : Distribution/oscam
+-------------------------------------------------------------------------------
HOSTCC	webif/pages_gen
GEN	webif/pages.c
GEN	Compressed 437728 template bytes into 176675 bytes. 261053 saved bytes (59.64%).
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
CC	cscrypt/des.c
In file included from cscrypt/../globals.h:113,
                 from cscrypt/des.c:136:
cscrypt/../cscrypt/aes.h:2:12: fatal error: openssl/aes.h: No such file or directory
 #  include <openssl/aes.h>
            ^~~~~~~~~~~~~~~
compilation terminated.
make[5]: *** [Makefile:464: build/mips-openwrt-linux-musl-ssl-libusb-pcsc/cscrypt/des.o] Error 1
make[4]: *** [Makefile:418: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/oscam-2020-12-12-aafda4bc'
make[3]: *** [Makefile:158: /openwrt/build_dir/target-mips_24kc_musl/oscam-2020-12-12-aafda4bc/.built] Error 2
```
