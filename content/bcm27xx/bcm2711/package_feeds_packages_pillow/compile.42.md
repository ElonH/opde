---
title: "compile.42"
date: 2021-06-29 09:27:20.679129
hidden: false
draft: false
weight: -42
---

build number: `42`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/pillow/compile -j$(nproc) || make package/feeds/packages/pillow/compile V=s
```

#### Compile.txt

``` bash
running build_ext


The headers or library files could not be found for freetype,
which was requested by the option flag --enable-freetype

Traceback (most recent call last):
  File "/openwrt/build_dir/target-aarch64_cortex-a72_musl/pypi/Pillow-8.2.0/setup.py", line 976, in <module>
    setup(
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/setuptools/__init__.py", line 153, in setup
    return distutils.core.setup(**attrs)
  File "/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/python3.9/distutils/core.py", line 148, in setup
    dist.run_commands()
  File "/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/python3.9/distutils/dist.py", line 966, in run_commands
    self.run_command(cmd)
  File "/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/python3.9/distutils/dist.py", line 985, in run_command
    cmd_obj.run()
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/setuptools/command/build_ext.py", line 79, in run
    _build_ext.run(self)
  File "/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/python3.9/distutils/command/build_ext.py", line 343, in run
    self.build_extensions()
  File "/openwrt/build_dir/target-aarch64_cortex-a72_musl/pypi/Pillow-8.2.0/setup.py", line 789, in build_extensions
    raise DependencyException(f)
__main__.DependencyException: freetype

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/openwrt/build_dir/target-aarch64_cortex-a72_musl/pypi/Pillow-8.2.0/setup.py", line 1042, in <module>
    raise DependencyException(msg)
__main__.DependencyException: 

The headers or library files could not be found for freetype,
which was requested by the option flag --enable-freetype


make[3]: *** [Makefile:56: /openwrt/build_dir/target-aarch64_cortex-a72_musl/pypi/Pillow-8.2.0/.built] Error 1
```
