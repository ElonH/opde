---
title: "compile.40"
date: 2021-06-22 10:43:26.844782
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
make package/feeds/packages/perl-www-curl/compile -j$(nproc) || make package/feeds/packages/perl-www-curl/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/100-perl-www-curl_disable_curl-config_hack.patch using plaintext: 
patching file Makefile.PL

Applying ./patches/101-skip-preprocessor-symbol.path using plaintext: 
patching file Makefile.PL

Applying ./patches/200-fix_default_lflags.patch using plaintext: 
patching file Makefile.PL

Applying ./patches/210-curl_7.66_compat.patch using plaintext: 
patching file Curl.xs

Applying ./patches/220-curl_7.69_compat.patch using plaintext: 
patching file Makefile.PL
Cannot find curl.h - cannot build constants files  - see Makefile.PL at - line 100.
make[3]: *** [Makefile:53: /openwrt/build_dir/target-mips_24kc_musl/perl/WWW-Curl-4.17/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 2
```
