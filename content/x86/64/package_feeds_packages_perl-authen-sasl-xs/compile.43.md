---
title: "compile.43"
date: 2021-07-01 09:14:00.051573
hidden: false
draft: false
weight: -43
---

build number: `43`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/perl-authen-sasl-xs/compile -j$(nproc) || make package/feeds/packages/perl-authen-sasl-xs/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/100-remove-devel-checklib-checks.patch using plaintext: 
patching file Makefile.PL
Warning: prerequisite Authen::SASL 2.08 not found.
Checking if your kit is complete...
Looks good
Generating a Unix-style Makefile
Writing Makefile for Authen::SASL::XS
Writing MYMETA.yml and MYMETA.json
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/Authen-SASL-XS-1.00'
cp XS.pm blib/lib/Authen/SASL/XS.pm
cp XS.pod blib/lib/Authen/SASL/XS.pod
cp lib/Authen/SASL/XS/Security.pm blib/lib/Authen/SASL/XS/Security.pm
Running Mkbootstrap for XS ()
chmod 644 "XS.bs"
"/openwrt/staging_dir/hostpkg/usr/bin/perl5.28.1" -MExtUtils::Command::MM -e 'cp_nonempty' -- XS.bs blib/arch/auto/Authen/SASL/XS/XS.bs 644
"/openwrt/staging_dir/hostpkg/usr/bin/perl5.28.1" "/openwrt/staging_dir/hostpkg/usr/lib/perl5/5.28.1/ExtUtils/xsubpp"  -typemap '/openwrt/staging_dir/hostpkg/usr/lib/perl5/5.28.1/ExtUtils/typemap' -typemap '/openwrt/build_dir/target-x86_64_musl/perl/Authen-SASL-XS-1.00/typemap'  XS.xs > XS.xsc
Please specify prototyping behavior for XS.xs (see perlxs manual)
mv XS.xsc XS.c
x86_64-openwrt-linux-gcc -c  -I/usr/local/include -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/perl/Authen-SASL-XS-1.00=Authen-SASL-XS-1.00 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -D_REENTRANT -D_GNU_SOURCE -O2   -DVERSION=\"1.00\" -DXS_VERSION=\"1.00\" -fPIC "-I/openwrt/staging_dir/target-x86_64_musl/usr/lib/perl5/5.28/CORE/"  -DSASL2 XS.c
XS.xs:42:10: fatal error: EXTERN.h: No such file or directory
 #include <EXTERN.h>
          ^~~~~~~~~~
compilation terminated.
make[4]: *** [Makefile:340: XS.o] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/Authen-SASL-XS-1.00'
make[3]: *** [Makefile:53: /openwrt/build_dir/target-x86_64_musl/perl/Authen-SASL-XS-1.00/.built] Error 2
```
