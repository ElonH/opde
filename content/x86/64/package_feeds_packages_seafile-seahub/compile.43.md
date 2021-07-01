---
title: "compile.43"
date: 2021-07-01 09:02:12.128110
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
make package/feeds/packages/seafile-seahub/compile -j$(nproc) || make package/feeds/packages/seafile-seahub/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/020-Makefile-fixes.patch using plaintext: 
patching file Makefile

Applying ./patches/030-uci-conf.patch using plaintext: 
patching file seahub/settings.py

Applying ./patches/040-manage-shebang.patch using plaintext: 
patching file manage.py
Collecting Django==2.2.24
  Downloading Django-2.2.24.tar.gz (9.2 MB)
Collecting pytz==2021.1
  Downloading pytz-2021.1.tar.gz (317 kB)
Collecting sqlparse>=0.2.2
ERROR: In --require-hashes mode, all requirements must have their versions pinned with ==. These do not:
    sqlparse>=0.2.2 from https://files.pythonhosted.org/packages/a2/54/da10f9a0235681179144a5ca02147428f955745e9393f859dec8d0d05b41/sqlparse-0.4.1.tar.gz#sha256=0f91fd2e829c44362cbcfab3e9ae12e22badaa8a29ad5ff599f9ec109f0454e8 (from Django==2.2.24->-r ../../lang/python/host-pip-requirements/Django-1.11.txt (line 1))
make[3]: *** [Makefile:98: /openwrt/build_dir/target-x86_64_musl/seahub-7.1.5-server/.built] Error 1
```
