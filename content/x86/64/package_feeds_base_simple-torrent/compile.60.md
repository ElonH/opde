---
title: "compile.60"
date: 2021-02-18 15:10:27.224230
hidden: false
draft: false
weight: -60
---

build number: `60`

path: `package/feeds/base/simple-torrent/compile`


``` bash
Copying files from /openwrt/build_dir/target-x86_64_musl/simple-torrent-1.2.12 into /openwrt/build_dir/target-x86_64_musl/simple-torrent-1.2.12/.go_work/build/src/cloud-torrent
engine/config.go
engine/config_test.go
engine/engine.go
engine/torrent.go
go.mod
go.sum
main.go
server/httpmiddleware/liveness.go
server/httpmiddleware/realip.go
server/server.go
server/server_api.go
server/server_bg.go
server/server_files.go
server/server_http.go
server/server_rss.go
server/server_search.go
server/server_stats.go
static/files.go
static/static.go

Symlinking directories from /openwrt/staging_dir/target-x86_64_musl/usr/share/gocode/src into /openwrt/build_dir/target-x86_64_musl/simple-torrent-1.2.12/.go_work/build/src
.../git.torproject.org
.../CloudflareSpeedTest
.../gitlab.com
.../github.com
.../ehang.io
.../v2ray.com

Finding targets
go: finding module for package github.com/elithrar/simple-scrypt
go: finding module for package github.com/jpillora/ansi
go: finding module for package github.com/andrew-d/go-termutil
go: finding module for package github.com/tomasen/realip
go: finding module for package github.com/jpillora/sizestr

Building targets
go: finding module for package github.com/jpillora/ansi
go: finding module for package github.com/jpillora/sizestr
go: finding module for package github.com/tomasen/realip
go: finding module for package github.com/andrew-d/go-termutil
go: finding module for package github.com/elithrar/simple-scrypt
/openwrt/dl/go-mod-cache/github.com/jpillora/requestlog@v1.0.0/wrap.go:11:2: module github.com/andrew-d/go-termutil: Get "https://proxy.golang.org/github.com/andrew-d/go-termutil/@v/list": net/http: TLS handshake timeout
/openwrt/dl/go-mod-cache/github.com/jpillora/cookieauth@v1.0.0/cookieauth.go:15:2: module github.com/elithrar/simple-scrypt: Get "https://proxy.golang.org/github.com/elithrar/simple-scrypt/@v/list": net/http: TLS handshake timeout
/openwrt/dl/go-mod-cache/github.com/jpillora/requestlog@v1.0.0/wrap.go:12:2: module github.com/jpillora/ansi: Get "https://proxy.golang.org/github.com/jpillora/ansi/@v/list": net/http: TLS handshake timeout
/openwrt/dl/go-mod-cache/github.com/jpillora/requestlog@v1.0.0/wrap.go:13:2: module github.com/jpillora/sizestr: Get "https://proxy.golang.org/github.com/jpillora/sizestr/@v/list": net/http: TLS handshake timeout
/openwrt/dl/go-mod-cache/github.com/jpillora/requestlog@v1.0.0/writer.go:13:2: module github.com/tomasen/realip: Get "https://proxy.golang.org/github.com/tomasen/realip/@v/list": net/http: TLS handshake timeout

make[3]: *** [Makefile:87: /openwrt/build_dir/target-x86_64_musl/simple-torrent-1.2.12/.built] Error 1
```
