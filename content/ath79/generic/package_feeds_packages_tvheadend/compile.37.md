---
title: "compile.37"
date: 2021-06-20 22:26:36.896190
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
make package/feeds/packages/tvheadend/compile -j$(nproc) || make package/feeds/packages/tvheadend/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-openssl-deprecated.patch using plaintext: 
patching file src/main.c

Applying ./patches/020-strncpy-issue.patch using plaintext: 
patching file Makefile

Applying ./patches/030-gcc10.patch using plaintext: 
patching file src/input.h
patching file src/input/mpegts.h
Checking support/features
  checking for cc execinfo.h ...                    fail
  checking for cc -mmmx ...                         fail
  checking for cc -msse2 ...                        fail
  checking for cc getloadavg ...                    ok
  checking for cc atomic64 ...                      fail
  checking for cc lockowner ...                     fail
  checking for cc qsort_r ...                       fail
  checking for cc stime ...                         ok
  checking for cc recvmmsg ...                      ok
  checking for cc sendmmsg ...                      ok
  checking for cc libiconv ...                      ok
  checking for cc libdvben50221 ...                 fail
  checking for py module gzip ...                   ok
  checking for gzip ...                             ok
  checking for bzip2 ...                            ok
  checking for pkg openssl  ...                     fail (detected <none>)
  checking for pkg libssl  ...                      fail (detected <none>)
  checking for cc openssl/ssl.h ...                 fail
ERROR: SSL development support not found
make[3]: *** [Makefile:99: /openwrt/build_dir/target-mips_24kc_musl/tvheadend-4.0.10/.configured_a17fb5ef857664f03cd0ce37cc5ea591] Error 1
```
