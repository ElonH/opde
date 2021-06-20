---
title: "compile.37"
date: 2021-06-20 22:30:11.470921
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
make package/feeds/packages/python-lxml/compile -j$(nproc) || make package/feeds/packages/python-lxml/compile V=s
```

#### Compile.txt

``` bash
Building lxml version 4.6.3.
Building without Cython.
Building against libxml2 2.9.12 and libxslt 1.1.34
Building against libxml2/libxslt in the following directory: /openwrt/staging_dir/target-mips_24kc_musl/usr/lib
running install
running build
running build_py
creating build
creating build/lib.-3.9
creating build/lib.-3.9/lxml
copying src/lxml/cssselect.py -> build/lib.-3.9/lxml
copying src/lxml/pyclasslookup.py -> build/lib.-3.9/lxml
copying src/lxml/__init__.py -> build/lib.-3.9/lxml
copying src/lxml/sax.py -> build/lib.-3.9/lxml
copying src/lxml/_elementpath.py -> build/lib.-3.9/lxml
copying src/lxml/ElementInclude.py -> build/lib.-3.9/lxml
copying src/lxml/builder.py -> build/lib.-3.9/lxml
copying src/lxml/doctestcompare.py -> build/lib.-3.9/lxml
copying src/lxml/usedoctest.py -> build/lib.-3.9/lxml
creating build/lib.-3.9/lxml/includes
copying src/lxml/includes/__init__.py -> build/lib.-3.9/lxml/includes
creating build/lib.-3.9/lxml/html
copying src/lxml/html/html5parser.py -> build/lib.-3.9/lxml/html
copying src/lxml/html/_setmixin.py -> build/lib.-3.9/lxml/html
copying src/lxml/html/soupparser.py -> build/lib.-3.9/lxml/html
copying src/lxml/html/defs.py -> build/lib.-3.9/lxml/html
copying src/lxml/html/ElementSoup.py -> build/lib.-3.9/lxml/html
copying src/lxml/html/__init__.py -> build/lib.-3.9/lxml/html
copying src/lxml/html/_html5builder.py -> build/lib.-3.9/lxml/html
copying src/lxml/html/diff.py -> build/lib.-3.9/lxml/html
copying src/lxml/html/formfill.py -> build/lib.-3.9/lxml/html
copying src/lxml/html/builder.py -> build/lib.-3.9/lxml/html
copying src/lxml/html/_diffcommand.py -> build/lib.-3.9/lxml/html
copying src/lxml/html/clean.py -> build/lib.-3.9/lxml/html
copying src/lxml/html/usedoctest.py -> build/lib.-3.9/lxml/html
creating build/lib.-3.9/lxml/isoschematron
copying src/lxml/isoschematron/__init__.py -> build/lib.-3.9/lxml/isoschematron
copying src/lxml/etree.h -> build/lib.-3.9/lxml
copying src/lxml/etree_api.h -> build/lib.-3.9/lxml
copying src/lxml/lxml.etree.h -> build/lib.-3.9/lxml
copying src/lxml/lxml.etree_api.h -> build/lib.-3.9/lxml
copying src/lxml/includes/xmlerror.pxd -> build/lib.-3.9/lxml/includes
copying src/lxml/includes/htmlparser.pxd -> build/lib.-3.9/lxml/includes
copying src/lxml/includes/xpath.pxd -> build/lib.-3.9/lxml/includes
copying src/lxml/includes/xslt.pxd -> build/lib.-3.9/lxml/includes
copying src/lxml/includes/xmlschema.pxd -> build/lib.-3.9/lxml/includes
copying src/lxml/includes/xmlparser.pxd -> build/lib.-3.9/lxml/includes
copying src/lxml/includes/config.pxd -> build/lib.-3.9/lxml/includes
copying src/lxml/includes/uri.pxd -> build/lib.-3.9/lxml/includes
copying src/lxml/includes/__init__.pxd -> build/lib.-3.9/lxml/includes
copying src/lxml/includes/etreepublic.pxd -> build/lib.-3.9/lxml/includes
copying src/lxml/includes/schematron.pxd -> build/lib.-3.9/lxml/includes
copying src/lxml/includes/xinclude.pxd -> build/lib.-3.9/lxml/includes
copying src/lxml/includes/relaxng.pxd -> build/lib.-3.9/lxml/includes
copying src/lxml/includes/dtdvalid.pxd -> build/lib.-3.9/lxml/includes
copying src/lxml/includes/tree.pxd -> build/lib.-3.9/lxml/includes
copying src/lxml/includes/c14n.pxd -> build/lib.-3.9/lxml/includes
copying src/lxml/includes/lxml-version.h -> build/lib.-3.9/lxml/includes
copying src/lxml/includes/etree_defs.h -> build/lib.-3.9/lxml/includes
creating build/lib.-3.9/lxml/isoschematron/resources
creating build/lib.-3.9/lxml/isoschematron/resources/rng
copying src/lxml/isoschematron/resources/rng/iso-schematron.rng -> build/lib.-3.9/lxml/isoschematron/resources/rng
creating build/lib.-3.9/lxml/isoschematron/resources/xsl
copying src/lxml/isoschematron/resources/xsl/XSD2Schtrn.xsl -> build/lib.-3.9/lxml/isoschematron/resources/xsl
copying src/lxml/isoschematron/resources/xsl/RNG2Schtrn.xsl -> build/lib.-3.9/lxml/isoschematron/resources/xsl
creating build/lib.-3.9/lxml/isoschematron/resources/xsl/iso-schematron-xslt1
copying src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/iso_dsdl_include.xsl -> build/lib.-3.9/lxml/isoschematron/resources/xsl/iso-schematron-xslt1
copying src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/iso_abstract_expand.xsl -> build/lib.-3.9/lxml/isoschematron/resources/xsl/iso-schematron-xslt1
copying src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/iso_schematron_skeleton_for_xslt1.xsl -> build/lib.-3.9/lxml/isoschematron/resources/xsl/iso-schematron-xslt1
copying src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/iso_schematron_message.xsl -> build/lib.-3.9/lxml/isoschematron/resources/xsl/iso-schematron-xslt1
copying src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/iso_svrl_for_xslt1.xsl -> build/lib.-3.9/lxml/isoschematron/resources/xsl/iso-schematron-xslt1
copying src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/readme.txt -> build/lib.-3.9/lxml/isoschematron/resources/xsl/iso-schematron-xslt1
warning: build_py: byte-compiling is disabled, skipping.

running build_ext
building 'lxml.etree' extension
creating build/temp.-3.9
creating build/temp.-3.9/src
creating build/temp.-3.9/src/lxml
ccache_cc -Wno-unused-result -Wsign-compare -DNDEBUG -g -O3 -Wall -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/pypi/lxml-4.6.3=lxml-4.6.3 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -fPIC -DCYTHON_CLINE_IN_TRACEBACK=0 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/libxml2 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -Isrc -Isrc/lxml/includes -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -c src/lxml/etree.c -o build/temp.-3.9/src/lxml/etree.o -w
src/lxml/etree.c:97:10: fatal error: Python.h: No such file or directory
 #include "Python.h"
          ^~~~~~~~~~
compilation terminated.
Compile failed: command '/openwrt/staging_dir/host/bin/ccache_cc' failed with exit code 1
creating openwrt
creating openwrt/tmp
cc -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/libxml2 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -I/usr/include/libxml2 -c /openwrt/tmp/xmlXPathInitvc_c7au8.c -o openwrt/tmp/xmlXPathInitvc_c7au8.o
cc openwrt/tmp/xmlXPathInitvc_c7au8.o -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lxml2 -o a.out
/usr/bin/ld: skipping incompatible /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libxml2.so when searching for -lxml2
/usr/bin/ld: skipping incompatible /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libxml2.a when searching for -lxml2
/usr/bin/ld: cannot find -lxml2
collect2: error: ld returned 1 exit status
*********************************************************************************
Could not find function xmlCheckVersion in library libxml2. Is libxml2 installed?
*********************************************************************************
error: command '/openwrt/staging_dir/host/bin/ccache_cc' failed with exit code 1
make[3]: *** [Makefile:50: /openwrt/build_dir/target-mips_24kc_musl/pypi/lxml-4.6.3/.built] Error 1
```
