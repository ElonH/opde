---
title: "compile.37"
date: 2021-06-20 22:39:07.405579
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
make package/feeds/packages/python-yaml/compile -j$(nproc) || make package/feeds/packages/python-yaml/compile V=s
```

#### Compile.txt

``` bash
/openwrt/staging_dir/hostpkg/lib/python3.9/distutils/dist.py:274: UserWarning: Unknown distribution option: 'python_requires'
  warnings.warn(msg)
running install
running build
running build_py
creating build
creating build/lib.-3.9
creating build/lib.-3.9/yaml
copying lib3/yaml/tokens.py -> build/lib.-3.9/yaml
copying lib3/yaml/constructor.py -> build/lib.-3.9/yaml
copying lib3/yaml/error.py -> build/lib.-3.9/yaml
copying lib3/yaml/loader.py -> build/lib.-3.9/yaml
copying lib3/yaml/events.py -> build/lib.-3.9/yaml
copying lib3/yaml/dumper.py -> build/lib.-3.9/yaml
copying lib3/yaml/parser.py -> build/lib.-3.9/yaml
copying lib3/yaml/composer.py -> build/lib.-3.9/yaml
copying lib3/yaml/__init__.py -> build/lib.-3.9/yaml
copying lib3/yaml/representer.py -> build/lib.-3.9/yaml
copying lib3/yaml/serializer.py -> build/lib.-3.9/yaml
copying lib3/yaml/resolver.py -> build/lib.-3.9/yaml
copying lib3/yaml/cyaml.py -> build/lib.-3.9/yaml
copying lib3/yaml/emitter.py -> build/lib.-3.9/yaml
copying lib3/yaml/reader.py -> build/lib.-3.9/yaml
copying lib3/yaml/nodes.py -> build/lib.-3.9/yaml
copying lib3/yaml/scanner.py -> build/lib.-3.9/yaml
warning: build_py: byte-compiling is disabled, skipping.

running build_ext
building '_yaml' extension
creating build/temp.-3.9
creating build/temp.-3.9/ext
ccache_cc -Wno-unused-result -Wsign-compare -DNDEBUG -g -O3 -Wall -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/pypi/PyYAML-5.3.1=PyYAML-5.3.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -fPIC -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -c ext/_yaml.c -o build/temp.-3.9/ext/_yaml.o
ext/_yaml.c:4:10: fatal error: Python.h: No such file or directory
 #include "Python.h"
          ^~~~~~~~~~
compilation terminated.
error: command '/openwrt/staging_dir/host/bin/ccache_cc' failed with exit code 1
make[3]: *** [Makefile:48: /openwrt/build_dir/target-mips_24kc_musl/pypi/PyYAML-5.3.1/.built] Error 1
```
