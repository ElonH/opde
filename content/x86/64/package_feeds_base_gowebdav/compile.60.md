---
title: "compile.60"
date: 2021-02-18 15:10:27.225861
hidden: false
draft: false
weight: -60
---

build number: `60`

path: `package/feeds/base/gowebdav/compile`


``` bash
Finding targets
go: finding module for package golang.org/x/net/context
go: finding module for package golang.org/x/net/webdav

Building targets
go: finding module for package golang.org/x/net/context
go: finding module for package golang.org/x/net/webdav
../../gowebdav.go:10:5: module golang.org/x/net/context: Get "https://proxy.golang.org/golang.org/x/net/context/@v/list": net/http: TLS handshake timeout
../../gowebdav.go:11:5: module golang.org/x/net/webdav: Get "https://proxy.golang.org/golang.org/x/net/webdav/@v/list": net/http: TLS handshake timeout

make[3]: *** [Makefile:86: /openwrt/build_dir/target-x86_64_musl/gowebdav-0.0.1/.built] Error 1
```
