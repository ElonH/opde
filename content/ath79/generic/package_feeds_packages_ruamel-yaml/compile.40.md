---
title: "compile.40"
date: 2021-06-22 10:42:16.502533
hidden: false
draft: false
weight: -40
---

build number: `40`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/ruamel-yaml/compile -j$(nproc) || make package/feeds/packages/ruamel-yaml/compile V=s
```

#### Compile.txt

``` bash
sys.argv ['setup.py', 'install', '--prefix=/usr', '--root=/openwrt/build_dir/target-mips_24kc_musl/pypi/ruamel.yaml-0.15.100/ipkg-install', '--single-version-externally-managed']
test compiling test_ruamel_yaml
running install
running build
running build_py
creating build
creating build/lib.-3.9
creating build/lib.-3.9/ruamel
copying .ruamel/__init__.py -> build/lib.-3.9/ruamel
creating build/lib.-3.9/ruamel/yaml
copying ./tokens.py -> build/lib.-3.9/ruamel/yaml
copying ./constructor.py -> build/lib.-3.9/ruamel/yaml
copying ./main.py -> build/lib.-3.9/ruamel/yaml
copying ./anchor.py -> build/lib.-3.9/ruamel/yaml
copying ./error.py -> build/lib.-3.9/ruamel/yaml
copying ./scalarfloat.py -> build/lib.-3.9/ruamel/yaml
copying ./loader.py -> build/lib.-3.9/ruamel/yaml
copying ./events.py -> build/lib.-3.9/ruamel/yaml
copying ./dumper.py -> build/lib.-3.9/ruamel/yaml
copying ./parser.py -> build/lib.-3.9/ruamel/yaml
copying ./composer.py -> build/lib.-3.9/ruamel/yaml
copying ./__init__.py -> build/lib.-3.9/ruamel/yaml
copying ./scalarint.py -> build/lib.-3.9/ruamel/yaml
copying ./configobjwalker.py -> build/lib.-3.9/ruamel/yaml
copying ./comments.py -> build/lib.-3.9/ruamel/yaml
copying ./representer.py -> build/lib.-3.9/ruamel/yaml
copying ./serializer.py -> build/lib.-3.9/ruamel/yaml
copying ./timestamp.py -> build/lib.-3.9/ruamel/yaml
copying ./resolver.py -> build/lib.-3.9/ruamel/yaml
copying ./util.py -> build/lib.-3.9/ruamel/yaml
copying ./cyaml.py -> build/lib.-3.9/ruamel/yaml
copying ./emitter.py -> build/lib.-3.9/ruamel/yaml
copying ./scalarstring.py -> build/lib.-3.9/ruamel/yaml
copying ./reader.py -> build/lib.-3.9/ruamel/yaml
copying ./nodes.py -> build/lib.-3.9/ruamel/yaml
copying ./scalarbool.py -> build/lib.-3.9/ruamel/yaml
copying ./scanner.py -> build/lib.-3.9/ruamel/yaml
copying ./compat.py -> build/lib.-3.9/ruamel/yaml
copying ./LICENSE -> build/lib.-3.9/ruamel/yaml
copying ./py.typed -> build/lib.-3.9/ruamel/yaml
warning: build_py: byte-compiling is disabled, skipping.

running build_ext
building '_ruamel_yaml' extension
creating build/temp.-3.9
creating build/temp.-3.9/ext
ccache_cc -Wno-unused-result -Wsign-compare -DNDEBUG -g -O3 -Wall -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/pypi/ruamel.yaml-0.15.100=ruamel.yaml-0.15.100 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -fPIC -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -c ext/_ruamel_yaml.c -o build/temp.-3.9/ext/_ruamel_yaml.o
ext/_ruamel_yaml.c:4:10: fatal error: Python.h: No such file or directory
 #include "Python.h"
          ^~~~~~~~~~
compilation terminated.
error: command '/openwrt/staging_dir/host/bin/ccache_cc' failed with exit code 1
make[3]: *** [Makefile:45: /openwrt/build_dir/target-mips_24kc_musl/pypi/ruamel.yaml-0.15.100/.built] Error 1
```
