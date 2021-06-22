---
title: "compile.40"
date: 2021-06-22 10:50:44.054183
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
make package/feeds/packages/python-augeas/compile -j$(nproc) || make package/feeds/packages/python-augeas/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-backport-ffi-fix.patch using plaintext: 
patching file augeas/__init__.py
patching file augeas/ffi.py
patching file setup.py
Collecting cffi==1.14.5
  Downloading cffi-1.14.5.tar.gz (475 kB)
Collecting pycparser==2.20
  Downloading pycparser-2.20.tar.gz (161 kB)
Skipping wheel build for cffi, due to binaries being disabled for it.
Skipping wheel build for pycparser, due to binaries being disabled for it.
Installing collected packages: pycparser, cffi
    Running setup.py install for pycparser: started
    Running setup.py install for pycparser: finished with status 'done'
    Running setup.py install for cffi: started
    Running setup.py install for cffi: finished with status 'done'
Successfully installed cffi-1.14.5 pycparser-2.20
running install
running build
running build_py
creating build
creating build/lib.-3.9
creating build/lib.-3.9/augeas
copying augeas/__init__.py -> build/lib.-3.9/augeas
copying augeas/ffi.py -> build/lib.-3.9/augeas
creating build/lib.-3.9/test
copying test/test_augeas.py -> build/lib.-3.9/test
copying test/__init__.py -> build/lib.-3.9/test
warning: build_py: byte-compiling is disabled, skipping.

running build_ext
generating cffi module 'build/temp.-3.9/_augeas.c'
creating build/temp.-3.9
building '_augeas' extension
creating build/temp.-3.9/build
creating build/temp.-3.9/build/temp.-3.9
ccache_cc -Wno-unused-result -Wsign-compare -DNDEBUG -g -O3 -Wall -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/pypi/python-augeas-1.1.0=python-augeas-1.1.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -fPIC -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/libxml2 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -c build/temp.-3.9/_augeas.c -o build/temp.-3.9/build/temp.-3.9/_augeas.o
build/temp.-3.9/_augeas.c:50:14: fatal error: pyconfig.h: No such file or directory
 #    include <pyconfig.h>
              ^~~~~~~~~~~~
compilation terminated.
error: command '/openwrt/staging_dir/host/bin/ccache_cc' failed with exit code 1
make[3]: *** [Makefile:46: /openwrt/build_dir/target-mips_24kc_musl/pypi/python-augeas-1.1.0/.built] Error 1
```
