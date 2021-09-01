---
title: "compile.45"
date: 2021-09-01 09:22:40.401286
hidden: false
draft: false
weight: -45
---

build number: `45`

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

Applying ./patches/010-no-acl.patch using plaintext: 
patching file Kconfig
patching file smb2pdu.c
patching file smbacl.c
patching file vfs.c
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/linux-5.4.143'
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/unicode.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/auth.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/vfs.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/vfs_cache.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/connection.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/crypto_ctx.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/server.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/misc.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/oplock.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/ksmbd_work.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/smbacl.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/ndr.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/mgmt/ksmbd_ida.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/mgmt/user_config.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/mgmt/share_config.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/mgmt/tree_connect.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/mgmt/user_session.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/smb_common.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/transport_tcp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/transport_ipc.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/smb2pdu.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/smb2ops.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/smb2misc.o
  ASN.1   /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/ksmbd_spnego_negtokeninit.asn1.[ch]
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/ksmbd_spnego_negtokeninit.asn1.o
  ASN.1   /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/ksmbd_spnego_negtokentarg.asn1.[ch]
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/ksmbd_spnego_negtokentarg.asn1.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/asn1.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/smb1pdu.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/smb1ops.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/smb1misc.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/netmisc.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/ksmbd.o
  Building modules, stage 2.
  MODPOST 1 modules
  CC [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/ksmbd.mod.o
  LD [M]  /openwrt/build_dir/target-x86_64_musl/linux-x86_64/ksmbd-3.4.1/ksmbd.ko
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/linux-5.4.143'
Package kmod-fs-ksmbd is missing dependencies for the following libraries:
asn1_decoder.ko
libdes.ko
oid_registry.ko
make[3]: *** [Makefile:84: /openwrt/bin/targets/x86/64/packages/kmod-fs-ksmbd_5.4.143+3.4.1-1_x86_64.ipk] Error 1
```
