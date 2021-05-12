---
title: "compile.14"
date: 2021-05-12 23:09:05.743206
hidden: false
draft: false
weight: -14
---

build number: `14`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/base/trelay/compile -j$(nproc) || make package/feeds/base/trelay/compile V=s
```

#### Compile.txt

``` bash
make[4]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/linux-5.4.117'
  HOSTCC  scripts/basic/fixdep
  HOSTCC  scripts/dtc/dtc.o
  HOSTCC  scripts/dtc/flattree.o
  HOSTCC  scripts/dtc/fstree.o
  HOSTCC  scripts/dtc/data.o
  HOSTCC  scripts/dtc/livetree.o
  HOSTCC  scripts/dtc/treesource.o
  HOSTCC  scripts/dtc/srcpos.o
  HOSTCC  scripts/dtc/checks.o
  HOSTCC  scripts/dtc/util.o
  HOSTCC  scripts/dtc/dtc-lexer.lex.o
  HOSTCC  scripts/dtc/dtc-parser.tab.o
  HOSTLD  scripts/dtc/dtc
  HOSTCC  scripts/kallsyms
  HOSTCC  scripts/pnmtologo
  HOSTCC  scripts/conmakehash
  HOSTCC  scripts/sortextable
scripts/sortextable.c:31:10: fatal error: tools/be_byteshift.h: No such file or directory
   31 | #include <tools/be_byteshift.h>
      |          ^~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
make[5]: *** [scripts/Makefile.host:107: scripts/sortextable] Error 1
make[4]: *** [Makefile:1120: scripts] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/linux-5.4.117'
make[3]: *** [Makefile:51: /openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-bcm27xx_bcm2711/trelay/.built] Error 2
```
