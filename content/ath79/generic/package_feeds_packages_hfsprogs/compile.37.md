---
title: "compile.37"
date: 2021-06-20 22:36:26.379893
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
make package/feeds/packages/hfsprogs/compile -j$(nproc) || make package/feeds/packages/hfsprogs/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/0001-Create-short-Makefiles-for-Debian.patch using plaintext: 
patching file Makefile.lnx
patching file fsck_hfs.tproj/Makefile.lnx
patching file fsck_hfs.tproj/dfalib/Makefile.lnx
patching file newfs_hfs.tproj/Makefile.lnx

Applying ./patches/0002-Add-exclude-Darwin-specific-code.patch using plaintext: 
patching file fsck_hfs.tproj/cache.c
patching file fsck_hfs.tproj/dfalib/BTree.c
patching file fsck_hfs.tproj/dfalib/BlockCache.c
patching file fsck_hfs.tproj/dfalib/SBTree.c
patching file fsck_hfs.tproj/dfalib/SDevice.c
patching file fsck_hfs.tproj/dfalib/SKeyCompare.c
patching file fsck_hfs.tproj/dfalib/SRepair.c
patching file fsck_hfs.tproj/dfalib/SRuntime.h
patching file fsck_hfs.tproj/dfalib/SUtils.c
patching file fsck_hfs.tproj/dfalib/SVerify2.c
patching file fsck_hfs.tproj/dfalib/Scavenger.h
patching file fsck_hfs.tproj/dfalib/hfs_endian.c
patching file fsck_hfs.tproj/dfalib/hfs_endian.h
patching file fsck_hfs.tproj/fsck_hfs.c
patching file fsck_hfs.tproj/utilities.c
patching file include/missing.h
patching file newfs_hfs.tproj/hfs_endian.c
patching file newfs_hfs.tproj/hfs_endian.h
patching file newfs_hfs.tproj/makehfs.c
patching file newfs_hfs.tproj/newfs_hfs.c
patching file newfs_hfs.tproj/newfs_hfs.h

Applying ./patches/0003-Add-helper-include-files-absent-from-the-upstream-pa.patch using plaintext: 
patching file include/bitstring.h
patching file include/hfs/hfs_format.h
patching file include/hfs/hfs_mount.h
patching file include/sys/appleapiopts.h

Applying ./patches/0004-Fix-compilation-on-64-bit-arches.patch using plaintext: 
patching file fsck_hfs.tproj/dfalib/BTreePrivate.h
patching file fsck_hfs.tproj/dfalib/SControl.c
patching file fsck_hfs.tproj/dfalib/SVerify1.c
patching file fsck_hfs.tproj/dfalib/hfs_endian.c

Applying ./patches/0005-Remove-Apple-specific-p-from-strings.patch using plaintext: 
patching file fsck_hfs.tproj/dfalib/BTreeTreeOps.c
patching file fsck_hfs.tproj/dfalib/SBTree.c

Applying ./patches/0006-Adjust-types-for-printing.patch using plaintext: 
patching file fsck_hfs.tproj/dfalib/SControl.c
patching file fsck_hfs.tproj/dfalib/hfs_endian.c

Applying ./patches/0007-Fix-path-for-HFS-wrapper-block.patch using plaintext: 
patching file newfs_hfs.tproj/makehfs.c

Applying ./patches/0008-Provide-command-line-option-a.patch using plaintext: 
patching file fsck_hfs.tproj/fsck_hfs.c

Applying ./patches/0009-Rename-dprintf-to-dbg_printf.patch using plaintext: 
patching file fsck_hfs.tproj/dfalib/SRepair.c
patching file fsck_hfs.tproj/dfalib/SVerify1.c
patching file fsck_hfs.tproj/fsck_debug.c
patching file fsck_hfs.tproj/fsck_debug.h

Applying ./patches/0010-Rename-custom-macro-nil-with-NULL.patch using plaintext: 
patching file fsck_hfs.tproj/dfalib/BTree.c
patching file fsck_hfs.tproj/dfalib/BTreeAllocate.c
patching file fsck_hfs.tproj/dfalib/BTreeMiscOps.c
patching file fsck_hfs.tproj/dfalib/BTreeNodeOps.c
patching file fsck_hfs.tproj/dfalib/BTreeTreeOps.c
patching file fsck_hfs.tproj/dfalib/SControl.c
patching file fsck_hfs.tproj/dfalib/SRepair.c
patching file fsck_hfs.tproj/dfalib/SUtils.c
patching file fsck_hfs.tproj/dfalib/SVerify1.c
patching file fsck_hfs.tproj/dfalib/SVerify2.c

Applying ./patches/0011-Fix-types.patch using plaintext: 
patching file fsck_hfs.tproj/cache.c

Applying ./patches/0012-Fix-mkfs-not-creating-UUIDs-for-new-filesystems.patch using plaintext: 
patching file include/missing.h

Applying ./patches/0013-Fix-manpages.patch using plaintext: 
patching file fsck_hfs.tproj/fsck_hfs.8
patching file newfs_hfs.tproj/newfs_hfs.8

Applying ./patches/0014-uClibc_no_loadavg.patch using plaintext: 
patching file newfs_hfs.tproj/makehfs.c

Applying ./patches/0015-sysctl-only-on-glibc.patch using plaintext: 
patching file newfs_hfs.tproj/makehfs.c

Applying ./patches/0016-Fix-fsckhfs-wide-literal.patch using plaintext: 
patching file fsck_hfs.tproj/dfalib/SVerify1.c

Applying ./patches/010-valloc-to-memalign.patch using plaintext: 
patching file newfs_hfs.tproj/makehfs.c

Applying ./patches/020-cdefs.patch using plaintext: 
patching file fsck_hfs.tproj/fsck_hfs.h
patching file newfs_hfs.tproj/makehfs.c
patching file newfs_hfs.tproj/newfs_hfs.c

Applying ./patches/030-no-cdefs.patch using plaintext: 
patching file disklib/dump.h
patching file dump.tproj/unctime.c
patching file fdisk.tproj/getrawpartition.c
patching file fdisk.tproj/util.h
patching file fsck_hfs.tproj/fsck_hfs.h
patching file fsck_msdos.tproj/boot.c
patching file fsck_msdos.tproj/check.c
patching file fsck_msdos.tproj/dir.c
patching file fsck_msdos.tproj/fat.c
patching file fsck_msdos.tproj/fsutil.c
patching file fsck_msdos.tproj/main.c
patching file newfs_hfs.tproj/makehfs.c
patching file newfs_hfs.tproj/newfs_hfs.c
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25'
for d in newfs_hfs.tproj fsck_hfs.tproj; do make -C $d -f Makefile.lnx all; done
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/newfs_hfs.tproj'
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o hfs_endian.o hfs_endian.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o makehfs.o makehfs.c
In file included from makehfs.c:38:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/errno.h:1:2: warning: #warning redirecting incorrect #include <sys/errno.h> to <errno.h> [-Wcpp]
 #warning redirecting incorrect #include <sys/errno.h> to <errno.h>
  ^~~~~~~
makehfs.c:56:10: fatal error: openssl/sha.h: No such file or directory
 #include <openssl/sha.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
make[5]: *** [<builtin>: makehfs.o] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/newfs_hfs.tproj'
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/fsck_hfs.tproj'
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o fsck_hfs.o fsck_hfs.c
In file included from fsck_hfs.c:46:
fsck_hfs.h:27: warning: "__P" redefined
 #define __P(x) x
 
In file included from /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/glibc-types.h:4,
                 from /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/features.h:46,
                 from /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/types.h:7,
                 from fsck_hfs.c:24:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/cdefs.h:83: note: this is the location of the previous definition
 #define __P(args) args
 
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o strings.o strings.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o utilities.o utilities.c
In file included from utilities.c:67:
fsck_hfs.h:27: warning: "__P" redefined
 #define __P(x) x
 
In file included from /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/glibc-types.h:4,
                 from /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/features.h:46,
                 from /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/types.h:7,
                 from utilities.c:57:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/cdefs.h:83: note: this is the location of the previous definition
 #define __P(args) args
 
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o cache.o cache.c
cache.c: In function 'CalculateCacheSize':
cache.c:158:69: warning: format '%lu' expects argument of type 'long unsigned int', but argument 3 has type 'size_t' {aka 'unsigned int'} [-Wformat=]
    printf ("\tCache size should be greater than %uM and less than %luM\n", MinCacheSize/(1024*1024), max_size_t/(1024*1024));
                                                                   ~~^                                ~~~~~~~~~~~~~~~~~~~~~~
                                                                   %u
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o fsck_debug.o fsck_debug.c
make -C dfalib -f Makefile.lnx CFLAGS="-Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1" LDFLAGS="-L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib " libdfa.a
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/fsck_hfs.tproj/dfalib'
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o hfs_endian.o hfs_endian.c
In file included from Scavenger.h:49,
                 from hfs_endian.c:41:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/errno.h:1:2: warning: #warning redirecting incorrect #include <sys/errno.h> to <errno.h> [-Wcpp]
 #warning redirecting incorrect #include <sys/errno.h> to <errno.h>
  ^~~~~~~
In file included from hfs_endian.c:44:
../fsck_hfs.h:27: warning: "__P" redefined
 #define __P(x) x
 
In file included from /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/glibc-types.h:4,
                 from /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/features.h:46,
                 from /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/types.h:7,
                 from hfs_endian.c:31:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/cdefs.h:83: note: this is the location of the previous definition
 #define __P(args) args
 
In file included from hfs_endian.c:35:
hfs_endian.c: In function 'hfs_swap_HFSBTInternalNode':
hfs_endian.c:1052:90: warning: iteration 3 invokes undefined behavior [-Waggressive-loop-optimizations]
                     srcRec->dataExtents[j].startBlock = SWAP_BE16 (srcRec->dataExtents[j].startBlock);
../../include/missing.h:102:25: note: in definition of macro 'be16_to_cpu'
 #define be16_to_cpu(x) (x)
                         ^
hfs_endian.h:43:31: note: in expansion of macro 'OSSwapBigToHostInt16'
 #define SWAP_BE16(__a)        OSSwapBigToHostInt16 (__a)
                               ^~~~~~~~~~~~~~~~~~~~
hfs_endian.c:1052:57: note: in expansion of macro 'SWAP_BE16'
                     srcRec->dataExtents[j].startBlock = SWAP_BE16 (srcRec->dataExtents[j].startBlock);
                                                         ^~~~~~~~~
hfs_endian.c:1051:17: note: within this loop
                 for (j = 0; j < kHFSExtentDensity * 2; j++) {
                 ^~~
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o BlockCache.o BlockCache.c
In file included from Scavenger.h:49,
                 from BlockCache.c:27:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/errno.h:1:2: warning: #warning redirecting incorrect #include <sys/errno.h> to <errno.h> [-Wcpp]
 #warning redirecting incorrect #include <sys/errno.h> to <errno.h>
  ^~~~~~~
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o BTree.o BTree.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o BTreeAllocate.o BTreeAllocate.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o BTreeMiscOps.o BTreeMiscOps.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o BTreeNodeOps.o BTreeNodeOps.c
In file included from BTreeNodeOps.c:38:
../fsck_hfs.h:27: warning: "__P" redefined
 #define __P(x) x
 
In file included from /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/glibc-types.h:4,
                 from /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/features.h:46,
                 from /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/endian.h:4,
                 from ../../include/missing.h:4,
                 from SRuntime.h:31,
                 from BTree.h:37,
                 from BTreePrivate.h:39,
                 from BTreeNodeOps.c:36:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/cdefs.h:83: note: this is the location of the previous definition
 #define __P(args) args
 
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o BTreeScanner.o BTreeScanner.c
In file included from Scavenger.h:49,
                 from BTreeScanner.c:27:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/errno.h:1:2: warning: #warning redirecting incorrect #include <sys/errno.h> to <errno.h> [-Wcpp]
 #warning redirecting incorrect #include <sys/errno.h> to <errno.h>
  ^~~~~~~
In file included from BTreeScanner.c:29:
../fsck_hfs.h:27: warning: "__P" redefined
 #define __P(x) x
 
In file included from /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/glibc-types.h:4,
                 from /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/features.h:46,
                 from /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/endian.h:4,
                 from ../../include/missing.h:4,
                 from SRuntime.h:31,
                 from BTree.h:37,
                 from BTreePrivate.h:39,
                 from BTreeScanner.h:28,
                 from BTreeScanner.c:26:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/cdefs.h:83: note: this is the location of the previous definition
 #define __P(args) args
 
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o BTreeTreeOps.o BTreeTreeOps.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o CatalogCheck.o CatalogCheck.c
In file included from Scavenger.h:49,
                 from CatalogCheck.c:23:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/errno.h:1:2: warning: #warning redirecting incorrect #include <sys/errno.h> to <errno.h> [-Wcpp]
 #warning redirecting incorrect #include <sys/errno.h> to <errno.h>
  ^~~~~~~
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o HardLinkCheck.o HardLinkCheck.c
In file included from Scavenger.h:49,
                 from HardLinkCheck.c:23:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/errno.h:1:2: warning: #warning redirecting incorrect #include <sys/errno.h> to <errno.h> [-Wcpp]
 #warning redirecting incorrect #include <sys/errno.h> to <errno.h>
  ^~~~~~~
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o SBTree.o SBTree.c
In file included from Scavenger.h:49,
                 from SBTree.c:38:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/errno.h:1:2: warning: #warning redirecting incorrect #include <sys/errno.h> to <errno.h> [-Wcpp]
 #warning redirecting incorrect #include <sys/errno.h> to <errno.h>
  ^~~~~~~
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o SControl.o SControl.c
In file included from Scavenger.h:49,
                 from SControl.c:43:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/errno.h:1:2: warning: #warning redirecting incorrect #include <sys/errno.h> to <errno.h> [-Wcpp]
 #warning redirecting incorrect #include <sys/errno.h> to <errno.h>
  ^~~~~~~
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o SVerify1.o SVerify1.c
In file included from Scavenger.h:49,
                 from SVerify1.c:35:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/errno.h:1:2: warning: #warning redirecting incorrect #include <sys/errno.h> to <errno.h> [-Wcpp]
 #warning redirecting incorrect #include <sys/errno.h> to <errno.h>
  ^~~~~~~
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o SVerify2.o SVerify2.c
In file included from Scavenger.h:49,
                 from SVerify2.c:42:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/errno.h:1:2: warning: #warning redirecting incorrect #include <sys/errno.h> to <errno.h> [-Wcpp]
 #warning redirecting incorrect #include <sys/errno.h> to <errno.h>
  ^~~~~~~
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o SRepair.o SRepair.c
In file included from Scavenger.h:49,
                 from SRepair.c:35:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/errno.h:1:2: warning: #warning redirecting incorrect #include <sys/errno.h> to <errno.h> [-Wcpp]
 #warning redirecting incorrect #include <sys/errno.h> to <errno.h>
  ^~~~~~~
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o SRebuildCatalogBTree.o SRebuildCatalogBTree.c
In file included from Scavenger.h:49,
                 from SRebuildCatalogBTree.c:42:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/errno.h:1:2: warning: #warning redirecting incorrect #include <sys/errno.h> to <errno.h> [-Wcpp]
 #warning redirecting incorrect #include <sys/errno.h> to <errno.h>
  ^~~~~~~
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o SUtils.o SUtils.c
In file included from Scavenger.h:49,
                 from SUtils.c:34:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/errno.h:1:2: warning: #warning redirecting incorrect #include <sys/errno.h> to <errno.h> [-Wcpp]
 #warning redirecting incorrect #include <sys/errno.h> to <errno.h>
  ^~~~~~~
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o SKeyCompare.o SKeyCompare.c
In file included from Scavenger.h:49,
                 from SKeyCompare.c:27:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/errno.h:1:2: warning: #warning redirecting incorrect #include <sys/errno.h> to <errno.h> [-Wcpp]
 #warning redirecting incorrect #include <sys/errno.h> to <errno.h>
  ^~~~~~~
SKeyCompare.c: In function 'CompareAttributeKeys':
SKeyCompare.c:475:19: warning: initialization discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
   UInt16 * str1 = searchKey->attrName;
                   ^~~~~~~~~
SKeyCompare.c:476:19: warning: initialization discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
   UInt16 * str2 = trialKey->attrName;
                   ^~~~~~~~
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o SDevice.o SDevice.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o SExtents.o SExtents.c
In file included from Scavenger.h:49,
                 from SExtents.c:38:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/errno.h:1:2: warning: #warning redirecting incorrect #include <sys/errno.h> to <errno.h> [-Wcpp]
 #warning redirecting incorrect #include <sys/errno.h> to <errno.h>
  ^~~~~~~
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o SAllocate.o SAllocate.c
In file included from Scavenger.h:49,
                 from SAllocate.c:72:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/errno.h:1:2: warning: #warning redirecting incorrect #include <sys/errno.h> to <errno.h> [-Wcpp]
 #warning redirecting incorrect #include <sys/errno.h> to <errno.h>
  ^~~~~~~
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o SCatalog.o SCatalog.c
In file included from Scavenger.h:49,
                 from SCatalog.c:25:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/errno.h:1:2: warning: #warning redirecting incorrect #include <sys/errno.h> to <errno.h> [-Wcpp]
 #warning redirecting incorrect #include <sys/errno.h> to <errno.h>
  ^~~~~~~
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o SStubs.o SStubs.c
In file included from Scavenger.h:49,
                 from SStubs.c:33:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/errno.h:1:2: warning: #warning redirecting incorrect #include <sys/errno.h> to <errno.h> [-Wcpp]
 #warning redirecting incorrect #include <sys/errno.h> to <errno.h>
  ^~~~~~~
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1   -c -o VolumeBitmapCheck.o VolumeBitmapCheck.c
In file included from Scavenger.h:49,
                 from VolumeBitmapCheck.c:31:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/errno.h:1:2: warning: #warning redirecting incorrect #include <sys/errno.h> to <errno.h> [-Wcpp]
 #warning redirecting incorrect #include <sys/errno.h> to <errno.h>
  ^~~~~~~
mips-openwrt-linux-musl-gcc-ar rc libdfa.a hfs_endian.o BlockCache.o BTree.o BTreeAllocate.o BTreeMiscOps.o BTreeNodeOps.o BTreeScanner.o BTreeTreeOps.o CatalogCheck.o HardLinkCheck.o SBTree.o SControl.o SVerify1.o SVerify2.o SRepair.o SRebuildCatalogBTree.o SUtils.o SKeyCompare.o SDevice.o SExtents.o SAllocate.o SCatalog.o SStubs.o VolumeBitmapCheck.o
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/fsck_hfs.tproj/dfalib'
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25=diskdev_cmds-332.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/include -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1 -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib  -o fsck_hfs fsck_hfs.o strings.o utilities.o cache.o fsck_debug.o dfalib/libdfa.a
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/fsck_hfs.tproj'
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25'
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/ipkg-mips_24kc/hfsfsck/usr/sbin/fsck.hfsplus: executable
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/ipkg-mips_24kc/hfsfsck into /openwrt/bin/packages/mips_24kc/packages/hfsfsck_332.25-4_mips_24kc.ipk
install: cannot stat '/openwrt/build_dir/target-mips_24kc_musl/diskdev_cmds-332.25/newfs_hfs.tproj/newfs_hfs': No such file or directory
make[3]: *** [Makefile:83: /openwrt/bin/packages/mips_24kc/packages/mkhfs_332.25-4_mips_24kc.ipk] Error 1
```
