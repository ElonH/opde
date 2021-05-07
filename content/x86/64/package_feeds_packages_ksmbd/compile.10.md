---
title: "compile.10"
date: 2021-05-07 12:42:57.368051
hidden: false
draft: false
weight: -10
---

build number: `10`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/ksmbd/compile -j$(nproc) || make package/feeds/packages/ksmbd/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/01-keep_kmod_metadata.patch using plaintext: 
patching file glob.h
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/linux-5.4.115'
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/unicode.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/auth.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/vfs.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/vfs_cache.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/connection.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/crypto_ctx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/server.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/misc.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/oplock.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/ksmbd_work.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/smbacl.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/ndr.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/mgmt/ksmbd_ida.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/mgmt/user_config.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/mgmt/share_config.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/mgmt/tree_connect.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/mgmt/user_session.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/smb_common.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/buffer_pool.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/transport_tcp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/transport_ipc.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/smb2pdu.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/smb2ops.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/smb2misc.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/asn1.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/smb1pdu.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/smb1ops.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/smb1misc.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/netmisc.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/ksmbd.o
  Building modules, stage 2.
  MODPOST 1 modules
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/ksmbd.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.3.9/ksmbd.ko
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/linux-5.4.115'
Package kmod-fs-ksmbd is missing dependencies for the following libraries:
libdes.ko
make[3]: *** [Makefile:81: /openwrt/bin/targets/x86/64/packages/kmod-fs-ksmbd_5.4.115+3.3.9-1_x86_64.ipk] Error 1
```
