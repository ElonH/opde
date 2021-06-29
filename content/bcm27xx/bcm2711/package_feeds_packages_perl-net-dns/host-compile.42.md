---
title: "host-compile.42"
date: 2021-06-29 09:28:26.566871
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
make package/feeds/packages/perl-net-dns/host-compile -j$(nproc) || make package/feeds/packages/perl-net-dns/host-compile V=s
```

#### Compile.txt

``` bash
Warning: prerequisite Digest::HMAC 1.03 not found.

Activating Non Fatal Online Tests...

Activating IPv6 Tests...

Warning!
========
Online tests depend on conditions beyond the control of Net::DNS. The tests 
check for the expected results when both Net::DNS and the outside world are
functioning properly. In case of failure it is often undecidable if the error
lies within Net::DNS or elsewhere.

Checking if your kit is complete...
Looks good
Generating a Unix-style Makefile
Writing Makefile for Net::DNS
Writing MYMETA.yml and MYMETA.json
make[4]: Entering directory '/openwrt/build_dir/hostpkg/perl/Net-DNS-1.30'
/bin/sh: 1: /openwrt/staging_dir/hostpkg/usr/bin/perl5.28.1: Text file busy
make[4]: *** [Makefile:424: blib/lib/Net/.exists] Error 2
make[4]: Leaving directory '/openwrt/build_dir/hostpkg/perl/Net-DNS-1.30'
make[3]: *** [Makefile:57: /openwrt/build_dir/hostpkg/perl/Net-DNS-1.30/.built] Error 2
```
