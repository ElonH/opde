---
title: "compile.37"
date: 2021-06-20 22:39:07.403282
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
make package/feeds/packages/sendmail/compile -j$(nproc) || make package/feeds/packages/sendmail/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-enable-nonroot-install.patch using plaintext: 
patching file cf/cf/Makefile

Applying ./patches/011-libmilter-so-version.patch using plaintext: 
patching file libmilter/Makefile.m4

Applying ./patches/100-misc-os-musl-fixes.patch using plaintext: 
patching file devtools/bin/Build
patching file include/sm/conf.h

Applying ./patches/102-pthreads-stack-size.patch using plaintext: 
patching file libmilter/libmilter.h
patching file libmilter/main.c

Applying ./patches/103-create-install-dirs.patch using plaintext: 
patching file sendmail/Makefile.m4
patching file devtools/M4/UNIX/links.m4
patching file cf/cf/Makefile

Applying ./patches/210-cdefs.patch using plaintext: 
patching file include/sm/os/sm_os_linux.h
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1'
Making all in:
/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/libsm
Configuration: pfx=, os=OpenWrt, rel=any, rbase=any, rroot=any, arch=any, sfx=, variant=optimized
Using M4=/openwrt/staging_dir/host/bin/m4
Creating /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsm using /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/devtools/OS/OpenWrt
Including /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/devtools/Site/site.OpenWrt.m4
Making dependencies in /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsm
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsm'
rm -f sm_os.h
ln -f -s ../../include/sm/os/sm_os_linux.h sm_os.h
ccache_cc -M -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic  assert.c debug.c errstring.c exc.c heap.c match.c rpool.c strdup.c strerror.c strl.c clrerr.c fclose.c feof.c ferror.c fflush.c fget.c fpos.c findfp.c flags.c fopen.c fprintf.c fpurge.c fput.c fread.c fscanf.c fseek.c fvwrite.c fwalk.c fwrite.c get.c makebuf.c put.c refill.c rewind.c setvbuf.c smstdio.c snprintf.c sscanf.c stdio.c strio.c ungetc.c vasprintf.c vfprintf.c vfscanf.c vprintf.c vsnprintf.c wbuf.c wsetup.c string.c stringf.c xtrap.c strto.c test.c strcasecmp.c strrevcmp.c signal.c clock.c config.c shm.c sem.c mbdb.c strexit.c cf.c ldap.c niprop.c mpeix.c memstat.c util.c inet6_ntop.c notify.c    >> Makefile
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsm'
Making in /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsm
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsm'
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o assert.o assert.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o debug.o debug.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o errstring.o errstring.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o exc.o exc.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o heap.o heap.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o match.o match.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o rpool.o rpool.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o strdup.o strdup.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o strerror.o strerror.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o strl.o strl.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o clrerr.o clrerr.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o fclose.o fclose.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o feof.o feof.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o ferror.o ferror.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o fflush.o fflush.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o fget.o fget.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o fpos.o fpos.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o findfp.o findfp.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o flags.o flags.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o fopen.o fopen.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o fprintf.o fprintf.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o fpurge.o fpurge.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o fput.o fput.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o fread.o fread.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o fscanf.o fscanf.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o fseek.o fseek.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o fvwrite.o fvwrite.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o fwalk.o fwalk.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o fwrite.o fwrite.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o get.o get.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o makebuf.o makebuf.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o put.o put.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o refill.o refill.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o rewind.o rewind.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o setvbuf.o setvbuf.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o smstdio.o smstdio.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o snprintf.o snprintf.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o sscanf.o sscanf.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o stdio.o stdio.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o strio.o strio.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o ungetc.o ungetc.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o vasprintf.o vasprintf.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o vfprintf.o vfprintf.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o vfscanf.o vfscanf.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o vprintf.o vprintf.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o vsnprintf.o vsnprintf.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o wbuf.o wbuf.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o wsetup.o wsetup.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o string.o string.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o stringf.o stringf.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o xtrap.o xtrap.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o strto.o strto.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o test.o test.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o strcasecmp.o strcasecmp.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o strrevcmp.o strrevcmp.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o signal.o signal.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o clock.o clock.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o config.o config.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o shm.o shm.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o sem.o sem.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o mbdb.o mbdb.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o strexit.o strexit.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o cf.o cf.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o ldap.o ldap.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o niprop.o niprop.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o mpeix.o mpeix.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o memstat.o memstat.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o util.o util.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o inet6_ntop.o inet6_ntop.c
ccache_cc -O2 -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o notify.o notify.c
mips-openwrt-linux-musl-gcc-ar crv libsm.a assert.o debug.o errstring.o exc.o heap.o match.o rpool.o strdup.o strerror.o strl.o clrerr.o fclose.o feof.o ferror.o fflush.o fget.o fpos.o findfp.o flags.o fopen.o fprintf.o fpurge.o fput.o fread.o fscanf.o fseek.o fvwrite.o fwalk.o fwrite.o get.o makebuf.o put.o refill.o rewind.o setvbuf.o smstdio.o snprintf.o sscanf.o stdio.o strio.o ungetc.o vasprintf.o vfprintf.o vfscanf.o vprintf.o vsnprintf.o wbuf.o wsetup.o string.o stringf.o xtrap.o strto.o test.o strcasecmp.o strrevcmp.o signal.o clock.o config.o shm.o sem.o mbdb.o strexit.o cf.o ldap.o niprop.o mpeix.o memstat.o util.o inet6_ntop.o notify.o    
a - assert.o
a - debug.o
a - errstring.o
a - exc.o
a - heap.o
a - match.o
a - rpool.o
a - strdup.o
a - strerror.o
a - strl.o
a - clrerr.o
a - fclose.o
a - feof.o
a - ferror.o
a - fflush.o
a - fget.o
a - fpos.o
a - findfp.o
a - flags.o
a - fopen.o
a - fprintf.o
a - fpurge.o
a - fput.o
a - fread.o
a - fscanf.o
a - fseek.o
a - fvwrite.o
a - fwalk.o
a - fwrite.o
a - get.o
a - makebuf.o
a - put.o
a - refill.o
a - rewind.o
a - setvbuf.o
a - smstdio.o
a - snprintf.o
a - sscanf.o
a - stdio.o
a - strio.o
a - ungetc.o
a - vasprintf.o
a - vfprintf.o
a - vfscanf.o
a - vprintf.o
a - vsnprintf.o
a - wbuf.o
a - wsetup.o
a - string.o
a - stringf.o
a - xtrap.o
a - strto.o
a - test.o
a - strcasecmp.o
a - strrevcmp.o
a - signal.o
a - clock.o
a - config.o
a - shm.o
a - sem.o
a - mbdb.o
a - strexit.o
a - cf.o
a - ldap.o
a - niprop.o
a - mpeix.o
a - memstat.o
a - util.o
a - inet6_ntop.o
a - notify.o
mips-openwrt-linux-musl-gcc-ranlib  libsm.a
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsm'
Making all in:
/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/libsmutil
Configuration: pfx=, os=OpenWrt, rel=any, rbase=any, rroot=any, arch=any, sfx=, variant=optimized
Using M4=/openwrt/staging_dir/host/bin/m4
Creating /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil using /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/devtools/OS/OpenWrt
Including /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/devtools/Site/site.OpenWrt.m4
Making dependencies in /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil'
rm -f sm_os.h
ln -f -s ../../include/sm/os/sm_os_linux.h sm_os.h
ccache_cc -M -I. -I../../sendmail   -I../../include  -DNEWDB  -DSTARTTLS -DNOT_SENDMAIL  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic  debug.c err.c lockfile.c safefile.c snprintf.c cf.c    >> Makefile
In file included from debug.c:11:
../../sendmail/sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from err.c:11:
../../sendmail/sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from lockfile.c:14:
../../sendmail/sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from safefile.c:14:
../../sendmail/sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from snprintf.c:14:
../../sendmail/sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from cf.c:11:
../../sendmail/sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
make[5]: *** [Makefile:309: depend] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil'
Making in /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil'
ccache_cc -O2 -I. -I../../sendmail   -I../../include  -DNEWDB  -DSTARTTLS -DNOT_SENDMAIL  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o debug.o debug.c
In file included from debug.c:11:
../../sendmail/sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
make[5]: *** [<builtin>: debug.o] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil'
Making all in:
/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/libsmdb
Configuration: pfx=, os=OpenWrt, rel=any, rbase=any, rroot=any, arch=any, sfx=, variant=optimized
Using M4=/openwrt/staging_dir/host/bin/m4
Creating /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmdb using /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/devtools/OS/OpenWrt
Including /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/devtools/Site/site.OpenWrt.m4
Making dependencies in /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmdb
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmdb'
rm -f sm_os.h
ln -f -s ../../include/sm/os/sm_os_linux.h sm_os.h
ccache_cc -M -I. -I../../sendmail   -I../../include  -DNEWDB  -DSTARTTLS -DNOT_SENDMAIL  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic  smdb.c smdb1.c smdb2.c smndbm.c smcdb.c    >> Makefile
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmdb'
Making in /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmdb
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmdb'
ccache_cc -O2 -I. -I../../sendmail   -I../../include  -DNEWDB  -DSTARTTLS -DNOT_SENDMAIL  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o smdb.o smdb.c
ccache_cc -O2 -I. -I../../sendmail   -I../../include  -DNEWDB  -DSTARTTLS -DNOT_SENDMAIL  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o smdb1.o smdb1.c
ccache_cc -O2 -I. -I../../sendmail   -I../../include  -DNEWDB  -DSTARTTLS -DNOT_SENDMAIL  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o smdb2.o smdb2.c
ccache_cc -O2 -I. -I../../sendmail   -I../../include  -DNEWDB  -DSTARTTLS -DNOT_SENDMAIL  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o smndbm.o smndbm.c
ccache_cc -O2 -I. -I../../sendmail   -I../../include  -DNEWDB  -DSTARTTLS -DNOT_SENDMAIL  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o smcdb.o smcdb.c
mips-openwrt-linux-musl-gcc-ar crv libsmdb.a smdb.o smdb1.o smdb2.o smndbm.o smcdb.o    
a - smdb.o
a - smdb1.o
a - smdb2.o
a - smndbm.o
a - smcdb.o
mips-openwrt-linux-musl-gcc-ranlib  libsmdb.a
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmdb'
Making all in:
/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/sendmail
Configuration: pfx=, os=OpenWrt, rel=any, rbase=any, rroot=any, arch=any, sfx=, variant=optimized
Using M4=/openwrt/staging_dir/host/bin/m4
Creating /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/sendmail using /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/devtools/OS/OpenWrt
Including /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/devtools/Site/site.OpenWrt.m4
Making dependencies in /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/sendmail
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/sendmail'
rm -f sm_os.h
ln -f -s ../../include/sm/os/sm_os_linux.h sm_os.h
ccache_cc -M -I. -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic  main.c alias.c arpadate.c bf.c collect.c conf.c control.c convtime.c daemon.c deliver.c domain.c envelope.c err.c headers.c macro.c map.c mci.c milter.c mime.c parseaddr.c queue.c ratectrl.c readcf.c recipient.c sasl.c savemail.c sfsasl.c shmticklib.c sm_resolve.c srvrsmtp.c stab.c stats.c sysexits.c timers.c tlsh.c tls.c trace.c udb.c usersmtp.c util.c version.c    >> Makefile
In file included from main.c:15:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from alias.c:14:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from arpadate.c:14:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from bf.c:31:
sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from collect.c:14:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from conf.c:14:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from control.c:11:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from convtime.c:14:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from daemon.c:14:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from deliver.c:14:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from domain.c:14:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from envelope.c:14:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from err.c:14:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from headers.c:14:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from macro.c:14:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from map.c:14:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from mci.c:14:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from milter.c:11:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from mime.c:14:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from parseaddr.c:14:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from queue.c:14:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from ./ratectrl.h:50,
                 from ratectrl.c:47:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from readcf.c:14:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from recipient.c:14:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from savemail.c:14:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from sfsasl.c:14:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from sm_resolve.c:44:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from srvrsmtp.c:14:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from stab.c:14:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from stats.c:14:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from sysexits.c:14:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from tlsh.c:11:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from tls.c:11:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from trace.c:14:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from udb.c:14:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from usersmtp.c:14:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
In file included from util.c:14:
./sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
make[5]: *** [Makefile:395: depend] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/sendmail'
Making in /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/sendmail
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/sendmail'
(cd ../../libsmutil; sh Build )
Configuration: pfx=, os=OpenWrt, rel=any, rbase=any, rroot=any, arch=any, sfx=, variant=optimized
Making in /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil'
ccache_cc -O2 -I. -I../../sendmail   -I../../include  -DNEWDB  -DSTARTTLS -DNOT_SENDMAIL  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o debug.o debug.c
In file included from debug.c:11:
../../sendmail/sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
make[6]: *** [<builtin>: debug.o] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil'
make[5]: *** [Makefile:404: /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil/libsmutil.a] Error 2
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/sendmail'
Making all in:
/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/editmap
Configuration: pfx=, os=OpenWrt, rel=any, rbase=any, rroot=any, arch=any, sfx=, variant=optimized
Using M4=/openwrt/staging_dir/host/bin/m4
Creating /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/editmap using /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/devtools/OS/OpenWrt
Including /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/devtools/Site/site.OpenWrt.m4
Making dependencies in /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/editmap
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/editmap'
rm -f sm_os.h
ln -f -s ../../include/sm/os/sm_os_linux.h sm_os.h
ccache_cc -M -I. -I../../sendmail   -I../../include  -DNEWDB  -DSTARTTLS -DNOT_SENDMAIL  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic  editmap.c    >> Makefile
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/editmap'
Making in /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/editmap
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/editmap'
(cd ../../libsmutil; sh Build )
Configuration: pfx=, os=OpenWrt, rel=any, rbase=any, rroot=any, arch=any, sfx=, variant=optimized
Making in /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil'
ccache_cc -O2 -I. -I../../sendmail   -I../../include  -DNEWDB  -DSTARTTLS -DNOT_SENDMAIL  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o debug.o debug.c
In file included from debug.c:11:
../../sendmail/sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
make[6]: *** [<builtin>: debug.o] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil'
make[5]: *** [Makefile:381: /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil/libsmutil.a] Error 2
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/editmap'
Making all in:
/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/mail.local
Configuration: pfx=, os=OpenWrt, rel=any, rbase=any, rroot=any, arch=any, sfx=, variant=optimized
Using M4=/openwrt/staging_dir/host/bin/m4
Creating /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/mail.local using /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/devtools/OS/OpenWrt
Including /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/devtools/Site/site.OpenWrt.m4
Making dependencies in /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/mail.local
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/mail.local'
rm -f sm_os.h
ln -f -s ../../include/sm/os/sm_os_linux.h sm_os.h
ccache_cc -M -I. -I../../sendmail   -I../../include  -DNEWDB  -DSTARTTLS -DNOT_SENDMAIL  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic  mail.local.c    >> Makefile
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/mail.local'
Making in /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/mail.local
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/mail.local'
ccache_cc -O2 -I. -I../../sendmail   -I../../include  -DNEWDB  -DSTARTTLS -DNOT_SENDMAIL  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o mail.local.o mail.local.c
ccache_cc -o mail.local   mail.local.o      /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsm/libsm.a  -ldb -ldl -lssl -lcrypto 
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ld: cannot find -lssl
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ld: cannot find -lcrypto
collect2: error: ld returned 1 exit status
make[5]: *** [Makefile:366: mail.local] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/mail.local'
Making all in:
/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/mailstats
Configuration: pfx=, os=OpenWrt, rel=any, rbase=any, rroot=any, arch=any, sfx=, variant=optimized
Using M4=/openwrt/staging_dir/host/bin/m4
Creating /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/mailstats using /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/devtools/OS/OpenWrt
Including /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/devtools/Site/site.OpenWrt.m4
Making dependencies in /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/mailstats
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/mailstats'
rm -f sm_os.h
ln -f -s ../../include/sm/os/sm_os_linux.h sm_os.h
ccache_cc -M -I. -I../../sendmail   -I../../include  -DNEWDB  -DSTARTTLS -DNOT_SENDMAIL  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic  mailstats.c    >> Makefile
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/mailstats'
Making in /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/mailstats
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/mailstats'
(cd ../../libsmutil; sh Build )
Configuration: pfx=, os=OpenWrt, rel=any, rbase=any, rroot=any, arch=any, sfx=, variant=optimized
Making in /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil'
ccache_cc -O2 -I. -I../../sendmail   -I../../include  -DNEWDB  -DSTARTTLS -DNOT_SENDMAIL  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o debug.o debug.c
In file included from debug.c:11:
../../sendmail/sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
make[6]: *** [<builtin>: debug.o] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil'
make[5]: *** [Makefile:375: /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil/libsmutil.a] Error 2
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/mailstats'
Making all in:
/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/makemap
Configuration: pfx=, os=OpenWrt, rel=any, rbase=any, rroot=any, arch=any, sfx=, variant=optimized
Using M4=/openwrt/staging_dir/host/bin/m4
Creating /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/makemap using /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/devtools/OS/OpenWrt
Including /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/devtools/Site/site.OpenWrt.m4
Making dependencies in /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/makemap
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/makemap'
rm -f sm_os.h
ln -f -s ../../include/sm/os/sm_os_linux.h sm_os.h
ccache_cc -M -I. -I../../sendmail   -I../../include  -DNEWDB  -DSTARTTLS -DNOT_SENDMAIL  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic  makemap.c    >> Makefile
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/makemap'
Making in /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/makemap
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/makemap'
(cd ../../libsmutil; sh Build )
Configuration: pfx=, os=OpenWrt, rel=any, rbase=any, rroot=any, arch=any, sfx=, variant=optimized
Making in /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil'
ccache_cc -O2 -I. -I../../sendmail   -I../../include  -DNEWDB  -DSTARTTLS -DNOT_SENDMAIL  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o debug.o debug.c
In file included from debug.c:11:
../../sendmail/sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
make[6]: *** [<builtin>: debug.o] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil'
make[5]: *** [Makefile:382: /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil/libsmutil.a] Error 2
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/makemap'
Making all in:
/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/praliases
Configuration: pfx=, os=OpenWrt, rel=any, rbase=any, rroot=any, arch=any, sfx=, variant=optimized
Using M4=/openwrt/staging_dir/host/bin/m4
Creating /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/praliases using /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/devtools/OS/OpenWrt
Including /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/devtools/Site/site.OpenWrt.m4
Making dependencies in /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/praliases
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/praliases'
rm -f sm_os.h
ln -f -s ../../include/sm/os/sm_os_linux.h sm_os.h
ccache_cc -M -I. -I../../sendmail   -I../../include  -DNEWDB  -DSTARTTLS -DNOT_SENDMAIL  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic  praliases.c    >> Makefile
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/praliases'
Making in /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/praliases
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/praliases'
(cd ../../libsmutil; sh Build )
Configuration: pfx=, os=OpenWrt, rel=any, rbase=any, rroot=any, arch=any, sfx=, variant=optimized
Making in /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil'
ccache_cc -O2 -I. -I../../sendmail   -I../../include  -DNEWDB  -DSTARTTLS -DNOT_SENDMAIL  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o debug.o debug.c
In file included from debug.c:11:
../../sendmail/sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
make[6]: *** [<builtin>: debug.o] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil'
make[5]: *** [Makefile:382: /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil/libsmutil.a] Error 2
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/praliases'
Making all in:
/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/rmail
Configuration: pfx=, os=OpenWrt, rel=any, rbase=any, rroot=any, arch=any, sfx=, variant=optimized
Using M4=/openwrt/staging_dir/host/bin/m4
Creating /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/rmail using /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/devtools/OS/OpenWrt
Including /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/devtools/Site/site.OpenWrt.m4
Making dependencies in /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/rmail
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/rmail'
rm -f sm_os.h
ln -f -s ../../include/sm/os/sm_os_linux.h sm_os.h
ccache_cc -M -I. -I../../sendmail   -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic  rmail.c    >> Makefile
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/rmail'
Making in /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/rmail
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/rmail'
ccache_cc -O2 -I. -I../../sendmail   -I../../include  -DNEWDB  -DSTARTTLS  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o rmail.o rmail.c
ccache_cc -o rmail   rmail.o      /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsm/libsm.a  -ldb -ldl -lssl -lcrypto 
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ld: cannot find -lssl
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ld: cannot find -lcrypto
collect2: error: ld returned 1 exit status
make[5]: *** [Makefile:367: rmail] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/rmail'
Making all in:
/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/smrsh
Configuration: pfx=, os=OpenWrt, rel=any, rbase=any, rroot=any, arch=any, sfx=, variant=optimized
Using M4=/openwrt/staging_dir/host/bin/m4
Creating /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/smrsh using /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/devtools/OS/OpenWrt
Including /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/devtools/Site/site.OpenWrt.m4
Making dependencies in /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/smrsh
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/smrsh'
rm -f sm_os.h
ln -f -s ../../include/sm/os/sm_os_linux.h sm_os.h
ccache_cc -M -I. -I../../sendmail   -I../../include  -DNEWDB  -DSTARTTLS -DNOT_SENDMAIL  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic  smrsh.c    >> Makefile
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/smrsh'
Making in /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/smrsh
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/smrsh'
ccache_cc -O2 -I. -I../../sendmail   -I../../include  -DNEWDB  -DSTARTTLS -DNOT_SENDMAIL  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o smrsh.o smrsh.c
ccache_cc -o smrsh   smrsh.o      /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsm/libsm.a  -ldb -ldl -lssl -lcrypto 
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ld: cannot find -lssl
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ld: cannot find -lcrypto
collect2: error: ld returned 1 exit status
make[5]: *** [Makefile:367: smrsh] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/smrsh'
Making all in:
/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/vacation
Configuration: pfx=, os=OpenWrt, rel=any, rbase=any, rroot=any, arch=any, sfx=, variant=optimized
Using M4=/openwrt/staging_dir/host/bin/m4
Creating /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/vacation using /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/devtools/OS/OpenWrt
Including /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/devtools/Site/site.OpenWrt.m4
Making dependencies in /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/vacation
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/vacation'
rm -f sm_os.h
ln -f -s ../../include/sm/os/sm_os_linux.h sm_os.h
ccache_cc -M -I. -I../../sendmail   -I../../include  -DNEWDB  -DSTARTTLS -DNOT_SENDMAIL  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic  vacation.c    >> Makefile
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/vacation'
Making in /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/vacation
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/vacation'
(cd ../../libsmutil; sh Build )
Configuration: pfx=, os=OpenWrt, rel=any, rbase=any, rroot=any, arch=any, sfx=, variant=optimized
Making in /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil'
ccache_cc -O2 -I. -I../../sendmail   -I../../include  -DNEWDB  -DSTARTTLS -DNOT_SENDMAIL  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1=sendmail-8.16.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DPIC -fpic     -c -o debug.o debug.c
In file included from debug.c:11:
../../sendmail/sendmail.h:46:11: fatal error: openssl/ssl.h: No such file or directory
 # include <openssl/ssl.h>
           ^~~~~~~~~~~~~~~
compilation terminated.
make[6]: *** [<builtin>: debug.o] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil'
make[5]: *** [Makefile:380: /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/libsmutil/libsmutil.a] Error 2
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/obj.OpenWrt.any.any/vacation'
make[4]: *** [Makefile:11: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1'
make[3]: *** [Makefile:135: /openwrt/build_dir/target-mips_24kc_musl/sendmail-8.16.1/.built] Error 2
```
