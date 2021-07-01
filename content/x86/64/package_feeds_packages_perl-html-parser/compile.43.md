---
title: "compile.43"
date: 2021-07-01 09:14:00.050771
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
make package/feeds/packages/perl-html-parser/compile -j$(nproc) || make package/feeds/packages/perl-html-parser/compile V=s
```

#### Compile.txt

``` bash
Warning: prerequisite HTML::Tagset 0 not found.
Warning: prerequisite HTTP::Headers 0 not found.
Warning: prerequisite URI 0 not found.
Warning: prerequisite URI::URL 0 not found.
Checking if your kit is complete...
Looks good
Generating a Unix-style Makefile
Writing Makefile for HTML::Parser
Writing MYMETA.yml and MYMETA.json
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/HTML-Parser-3.75'
cp lib/HTML/Parser.pm blib/lib/HTML/Parser.pm
cp lib/HTML/HeadParser.pm blib/lib/HTML/HeadParser.pm
cp lib/HTML/Entities.pm blib/lib/HTML/Entities.pm
cp lib/HTML/Filter.pm blib/lib/HTML/Filter.pm
cp lib/HTML/LinkExtor.pm blib/lib/HTML/LinkExtor.pm
cp lib/HTML/PullParser.pm blib/lib/HTML/PullParser.pm
cp lib/HTML/TokeParser.pm blib/lib/HTML/TokeParser.pm
Running Mkbootstrap for Parser ()
chmod 644 "Parser.bs"
"/openwrt/staging_dir/hostpkg/usr/bin/perl5.28.1" -MExtUtils::Command::MM -e 'cp_nonempty' -- Parser.bs blib/arch/auto/HTML/Parser/Parser.bs 644
"/openwrt/staging_dir/hostpkg/usr/bin/perl5.28.1" "/openwrt/staging_dir/hostpkg/usr/lib/perl5/5.28.1/ExtUtils/xsubpp"  -typemap '/openwrt/staging_dir/hostpkg/usr/lib/perl5/5.28.1/ExtUtils/typemap' -typemap '/openwrt/build_dir/target-x86_64_musl/perl/HTML-Parser-3.75/typemap'  Parser.xs > Parser.xsc
mv Parser.xsc Parser.c
x86_64-openwrt-linux-gcc -c   -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/perl/HTML-Parser-3.75=HTML-Parser-3.75 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -D_REENTRANT -D_GNU_SOURCE -O2   -DVERSION=\"3.75\" -DXS_VERSION=\"3.75\" -fPIC "-I/openwrt/staging_dir/target-x86_64_musl/usr/lib/perl5/5.28/CORE/"  -DMARKED_SECTION Parser.c
Parser.xs:17:10: fatal error: EXTERN.h: No such file or directory
 #include "EXTERN.h"
          ^~~~~~~~~~
compilation terminated.
make[4]: *** [Makefile:356: Parser.o] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/HTML-Parser-3.75'
make[3]: *** [Makefile:66: /openwrt/build_dir/target-x86_64_musl/perl/HTML-Parser-3.75/.built] Error 2
```
