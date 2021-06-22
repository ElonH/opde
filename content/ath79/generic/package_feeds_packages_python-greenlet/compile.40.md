---
title: "compile.40"
date: 2021-06-22 10:48:13.533299
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
make package/feeds/packages/python-greenlet/compile -j$(nproc) || make package/feeds/packages/python-greenlet/compile V=s
```

#### Compile.txt

``` bash
running install
running build
running build_py
creating build
creating build/lib.-3.9
creating build/lib.-3.9/greenlet
copying src/greenlet/__init__.py -> build/lib.-3.9/greenlet
creating build/lib.-3.9/greenlet/tests
copying src/greenlet/tests/test_leaks.py -> build/lib.-3.9/greenlet/tests
copying src/greenlet/tests/test_contextvars.py -> build/lib.-3.9/greenlet/tests
copying src/greenlet/tests/test_gc.py -> build/lib.-3.9/greenlet/tests
copying src/greenlet/tests/test_stack_saved.py -> build/lib.-3.9/greenlet/tests
copying src/greenlet/tests/__init__.py -> build/lib.-3.9/greenlet/tests
copying src/greenlet/tests/test_generator.py -> build/lib.-3.9/greenlet/tests
copying src/greenlet/tests/test_greenlet.py -> build/lib.-3.9/greenlet/tests
copying src/greenlet/tests/test_version.py -> build/lib.-3.9/greenlet/tests
copying src/greenlet/tests/test_extension_interface.py -> build/lib.-3.9/greenlet/tests
copying src/greenlet/tests/test_tracing.py -> build/lib.-3.9/greenlet/tests
copying src/greenlet/tests/test_generator_nested.py -> build/lib.-3.9/greenlet/tests
copying src/greenlet/tests/test_weakref.py -> build/lib.-3.9/greenlet/tests
copying src/greenlet/tests/test_throw.py -> build/lib.-3.9/greenlet/tests
copying src/greenlet/tests/test_cpp.py -> build/lib.-3.9/greenlet/tests
running egg_info
writing src/greenlet.egg-info/PKG-INFO
writing dependency_links to src/greenlet.egg-info/dependency_links.txt
writing requirements to src/greenlet.egg-info/requires.txt
writing top-level names to src/greenlet.egg-info/top_level.txt
adding license file 'LICENSE' (matched pattern 'LICEN[CS]E*')
adding license file 'LICENSE.PSF' (matched pattern 'LICEN[CS]E*')
adding license file 'AUTHORS' (matched pattern 'AUTHORS*')
reading manifest file 'src/greenlet.egg-info/SOURCES.txt'
reading manifest template 'MANIFEST.in'
no previously-included directories found matching 'docs/_build'
warning: no files found matching '*.py' under directory 'appveyor'
warning: no previously-included files matching '*.pyc' found anywhere in distribution
warning: no previously-included files matching '*.pyd' found anywhere in distribution
warning: no previously-included files matching '*.so' found anywhere in distribution
warning: no previously-included files matching '.coverage' found anywhere in distribution
writing manifest file 'src/greenlet.egg-info/SOURCES.txt'
copying src/greenlet/greenlet.c -> build/lib.-3.9/greenlet
copying src/greenlet/greenlet.h -> build/lib.-3.9/greenlet
copying src/greenlet/slp_platformselect.h -> build/lib.-3.9/greenlet
creating build/lib.-3.9/greenlet/platform
copying src/greenlet/platform/setup_switch_x64_masm.cmd -> build/lib.-3.9/greenlet/platform
copying src/greenlet/platform/switch_aarch64_gcc.h -> build/lib.-3.9/greenlet/platform
copying src/greenlet/platform/switch_alpha_unix.h -> build/lib.-3.9/greenlet/platform
copying src/greenlet/platform/switch_amd64_unix.h -> build/lib.-3.9/greenlet/platform
copying src/greenlet/platform/switch_arm32_gcc.h -> build/lib.-3.9/greenlet/platform
copying src/greenlet/platform/switch_arm32_ios.h -> build/lib.-3.9/greenlet/platform
copying src/greenlet/platform/switch_csky_gcc.h -> build/lib.-3.9/greenlet/platform
copying src/greenlet/platform/switch_m68k_gcc.h -> build/lib.-3.9/greenlet/platform
copying src/greenlet/platform/switch_mips_unix.h -> build/lib.-3.9/greenlet/platform
copying src/greenlet/platform/switch_ppc64_aix.h -> build/lib.-3.9/greenlet/platform
copying src/greenlet/platform/switch_ppc64_linux.h -> build/lib.-3.9/greenlet/platform
copying src/greenlet/platform/switch_ppc_aix.h -> build/lib.-3.9/greenlet/platform
copying src/greenlet/platform/switch_ppc_linux.h -> build/lib.-3.9/greenlet/platform
copying src/greenlet/platform/switch_ppc_macosx.h -> build/lib.-3.9/greenlet/platform
copying src/greenlet/platform/switch_ppc_unix.h -> build/lib.-3.9/greenlet/platform
copying src/greenlet/platform/switch_riscv_unix.h -> build/lib.-3.9/greenlet/platform
copying src/greenlet/platform/switch_s390_unix.h -> build/lib.-3.9/greenlet/platform
copying src/greenlet/platform/switch_sparc_sun_gcc.h -> build/lib.-3.9/greenlet/platform
copying src/greenlet/platform/switch_x32_unix.h -> build/lib.-3.9/greenlet/platform
copying src/greenlet/platform/switch_x64_masm.asm -> build/lib.-3.9/greenlet/platform
copying src/greenlet/platform/switch_x64_masm.obj -> build/lib.-3.9/greenlet/platform
copying src/greenlet/platform/switch_x64_msvc.h -> build/lib.-3.9/greenlet/platform
copying src/greenlet/platform/switch_x86_msvc.h -> build/lib.-3.9/greenlet/platform
copying src/greenlet/platform/switch_x86_unix.h -> build/lib.-3.9/greenlet/platform
copying src/greenlet/tests/_test_extension.c -> build/lib.-3.9/greenlet/tests
copying src/greenlet/tests/_test_extension_cpp.cpp -> build/lib.-3.9/greenlet/tests
warning: build_py: byte-compiling is disabled, skipping.

running build_ext
building 'greenlet._greenlet' extension
creating build/temp.-3.9
creating build/temp.-3.9/src
creating build/temp.-3.9/src/greenlet
ccache_cc -Wno-unused-result -Wsign-compare -DNDEBUG -g -O3 -Wall -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/pypi/greenlet-1.0.0=greenlet-1.0.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -mno-mips16 -mno-interlink-mips16 -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -fPIC -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -c src/greenlet/greenlet.c -o build/temp.-3.9/src/greenlet/greenlet.o
In file included from src/greenlet/greenlet.c:11:
src/greenlet/greenlet.h:8:10: fatal error: Python.h: No such file or directory
 #include <Python.h>
          ^~~~~~~~~~
compilation terminated.
error: command '/openwrt/staging_dir/host/bin/ccache_cc' failed with exit code 1
make[3]: *** [Makefile:57: /openwrt/build_dir/target-mips_24kc_musl/pypi/greenlet-1.0.0/.built] Error 1
```
