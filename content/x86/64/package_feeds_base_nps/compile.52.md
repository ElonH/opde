---
title: "compile.52"
date: 2021-03-09 13:46:57.317744
hidden: false
draft: false
weight: -52
---

build number: `52`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/base/nps/compile -j$(nproc) || make package/feeds/base/nps/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/100-remove-useless-sdk-in-npc.patch using plaintext: 
patching file cmd/npc/sdk.go.bak (renamed from cmd/npc/sdk.go)
Copying files from /openwrt/build_dir/target-x86_64_musl/nps-0.26.9 into /openwrt/build_dir/target-x86_64_musl/nps-0.26.9/.go_work/build/src/ehang.io/nps
bridge/bridge.go
client/client.go
client/control.go
client/health.go
client/local.go
client/register.go
cmd/npc/npc.go
cmd/nps/nps.go
go.mod
go.sum
gui/npc/npc.go
lib/cache/lru.go
lib/common/const.go
lib/common/logs.go
lib/common/netpackager.go
lib/common/pool.go
lib/common/pprof.go
lib/common/run.go
lib/common/util.go
lib/config/config.go
lib/config/config_test.go
lib/conn/conn.go
lib/conn/link.go
lib/conn/listener.go
lib/conn/snappy.go
lib/crypt/clientHello.go
lib/crypt/crypt.go
lib/crypt/tls.go
lib/daemon/daemon.go
lib/daemon/reload.go
lib/file/db.go
lib/file/file.go
lib/file/obj.go
lib/file/sort.go
lib/goroutine/pool.go
lib/install/install.go
lib/pmux/pconn.go
lib/pmux/plistener.go
lib/pmux/pmux.go
lib/pmux/pmux_test.go
lib/rate/conn.go
lib/rate/rate.go
lib/sheap/heap.go
lib/version/version.go
server/connection/connection.go
server/proxy/base.go
server/proxy/http.go
server/proxy/https.go
server/proxy/p2p.go
server/proxy/socks5.go
server/proxy/tcp.go
server/proxy/transport.go
server/proxy/transport_windows.go
server/proxy/udp.go
server/server.go
server/test/test.go
server/tool/utils.go
web/controllers/auth.go
web/controllers/base.go
web/controllers/client.go
web/controllers/index.go
web/controllers/login.go
web/routers/router.go

Symlinking directories from /openwrt/staging_dir/target-x86_64_musl/usr/share/gocode/src into /openwrt/build_dir/target-x86_64_musl/nps-0.26.9/.go_work/build/src
.../github.com

Finding targets
go: downloading github.com/exfly/beego v1.12.0-export-init
go: downloading github.com/kardianos/service v1.0.0
go: downloading github.com/ccding/go-stun v0.0.0-20180726100737-be486d185f3d
go: downloading github.com/c4milo/unpackit v0.0.0-20170704181138-4ed373e9ef1c
go: downloading github.com/shirou/gopsutil v2.19.11+incompatible
go: downloading ehang.io/nps-mux v0.0.0-20200617154922-5dc86cc6082a
go: downloading github.com/xtaci/kcp-go v5.4.20+incompatible
go: downloading golang.org/x/net v0.0.0-20200602114024-627f9648deb9
go: downloading github.com/golang/snappy v0.0.2
go: downloading github.com/klauspost/reedsolomon v1.9.9
go: downloading github.com/templexxx/xor v0.0.0-20191217153810-f85b25db303b
go: downloading github.com/tjfoc/gmsm v1.3.2
go: downloading golang.org/x/crypto v0.0.0-20200604202706-70a84ac30bf9
go: downloading github.com/panjf2000/ants/v2 v2.4.2
go: downloading golang.org/x/sys v0.0.0-20200615200032-f1bc736245b1
go: downloading github.com/shiena/ansicolor v0.0.0-20151119151921-a422bbe96644
go: downloading gopkg.in/yaml.v2 v2.2.8

Building targets
go: downloading github.com/c4milo/unpackit v0.0.0-20170704181138-4ed373e9ef1c
go: downloading golang.org/x/crypto v0.0.0-20200604202706-70a84ac30bf9
go: downloading github.com/golang/snappy v0.0.2
go: downloading github.com/klauspost/reedsolomon v1.9.9
go: downloading github.com/templexxx/xor v0.0.0-20191217153810-f85b25db303b
go: downloading github.com/tjfoc/gmsm v1.3.2
go: downloading github.com/templexxx/cpufeat v0.0.0-20180724012125-cef66df7f161
go: downloading github.com/klauspost/cpuid v1.3.0
go: downloading golang.org/x/text v0.3.2
go: downloading github.com/ulikunitz/xz v0.5.6
go: downloading github.com/dsnet/compress v0.0.1
go: downloading github.com/klauspost/pgzip v1.2.1
/openwrt/dl/go-mod-cache/github.com/c4milo/unpackit@v0.0.0-20170704181138-4ed373e9ef1c/unpackit.go:25:2: github.com/dsnet/compress@v0.0.1: unexpected EOF
/openwrt/dl/go-mod-cache/github.com/c4milo/unpackit@v0.0.0-20170704181138-4ed373e9ef1c/unpackit.go:26:2: github.com/klauspost/pgzip@v1.2.1: unexpected EOF
/openwrt/dl/go-mod-cache/github.com/c4milo/unpackit@v0.0.0-20170704181138-4ed373e9ef1c/unpackit.go:28:2: github.com/ulikunitz/xz@v0.5.6: unexpected EOF
/openwrt/dl/go-mod-cache/golang.org/x/net@v0.0.0-20200602114024-627f9648deb9/idna/idna10.0.0.go:25:2: golang.org/x/text@v0.3.2: unexpected EOF
/openwrt/dl/go-mod-cache/golang.org/x/net@v0.0.0-20200602114024-627f9648deb9/idna/idna10.0.0.go:26:2: golang.org/x/text@v0.3.2: unexpected EOF
/openwrt/dl/go-mod-cache/golang.org/x/net@v0.0.0-20200602114024-627f9648deb9/idna/idna10.0.0.go:27:2: golang.org/x/text@v0.3.2: unexpected EOF

make[3]: *** [Makefile:99: /openwrt/build_dir/target-x86_64_musl/nps-0.26.9/.built] Error 1
```
