---
title: "compile.36"
date: 2021-06-20 17:01:47.590387
hidden: false
draft: false
weight: -36
---

build number: `36`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/mosdns/compile -j$(nproc) || make package/feeds/packages/mosdns/compile V=s
```

#### Compile.txt

``` bash
Copying files from /openwrt/build_dir/target-aarch64_generic_musl/mosdns-1.8.6 into /openwrt/build_dir/target-aarch64_generic_musl/mosdns-1.8.6/.go_work/build/src/github.com/IrineSistiana/mosdns
dispatcher/coremain/config.go
dispatcher/coremain/run.go
dispatcher/handler/config.go
dispatcher/handler/config_test.go
dispatcher/handler/context.go
dispatcher/handler/context_test.go
dispatcher/handler/error.go
dispatcher/handler/interface.go
dispatcher/handler/plugin_wrapper.go
dispatcher/handler/register.go
dispatcher/handler/register_test.go
dispatcher/handler/test_utils.go
dispatcher/mlog/logger.go
dispatcher/pkg/arbitrary/arbitrary.go
dispatcher/pkg/arbitrary/arbitrary_test.go
dispatcher/pkg/cache/cache.go
dispatcher/pkg/cache/mem_cache/mem_cache.go
dispatcher/pkg/cache/mem_cache/mem_cache_test.go
dispatcher/pkg/cache/redis_cache/redis_cache.go
dispatcher/pkg/cache/redis_cache/redis_cache_test.go
dispatcher/pkg/concurrent_limiter/client_limiter.go
dispatcher/pkg/concurrent_limiter/client_limiter_test.go
dispatcher/pkg/concurrent_limiter/concurrent_limiter.go
dispatcher/pkg/concurrent_limiter/concurrent_limiter_test.go
dispatcher/pkg/concurrent_lru/concurrent_lru.go
dispatcher/pkg/concurrent_lru/concurrent_lru_test.go
dispatcher/pkg/concurrent_map/concurrent_map.go
dispatcher/pkg/concurrent_map/concurrent_map_test.go
dispatcher/pkg/dnsutils/msg.go
dispatcher/pkg/dnsutils/net_io.go
dispatcher/pkg/dnsutils/net_io_test.go
dispatcher/pkg/executable_seq/executable_cmd.go
dispatcher/pkg/executable_seq/executable_cmd_sequence.go
dispatcher/pkg/executable_seq/executable_cmd_sequence_test.go
dispatcher/pkg/executable_seq/fallback.go
dispatcher/pkg/executable_seq/fallback_test.go
dispatcher/pkg/executable_seq/parallel.go
dispatcher/pkg/executable_seq/parallel_test.go
dispatcher/pkg/executable_seq/utils.go
dispatcher/pkg/hosts/hosts.go
dispatcher/pkg/hosts/hosts_test.go
dispatcher/pkg/load_cache/load_cache.go
dispatcher/pkg/lru/lru.go
dispatcher/pkg/lru/lru_test.go
dispatcher/pkg/matcher/domain/domain_matcher.go
dispatcher/pkg/matcher/domain/domain_matcher_test.go
dispatcher/pkg/matcher/domain/interface.go
dispatcher/pkg/matcher/domain/load_helper.go
dispatcher/pkg/matcher/domain/load_helper_test.go
dispatcher/pkg/matcher/domain/matcher.go
dispatcher/pkg/matcher/domain/matcher_test.go
dispatcher/pkg/matcher/elem/rr_type.go
dispatcher/pkg/matcher/elem/rr_type_test.go
dispatcher/pkg/matcher/msg_matcher/query.go
dispatcher/pkg/matcher/msg_matcher/response.go
dispatcher/pkg/matcher/netlist/interface.go
dispatcher/pkg/matcher/netlist/list.go
dispatcher/pkg/matcher/netlist/load_helper.go
dispatcher/pkg/matcher/netlist/net.go
dispatcher/pkg/matcher/netlist/netlist_test.go
dispatcher/pkg/matcher/v2data/data.pb.go
dispatcher/pkg/matcher/v2data/data.proto
dispatcher/pkg/matcher/v2data/domain_matcher_loader.go
dispatcher/pkg/matcher/v2data/init.go
dispatcher/pkg/matcher/v2data/netlist_loader.go
dispatcher/pkg/pool/allocator.go
dispatcher/pkg/pool/allocator_test.go
dispatcher/pkg/pool/bytes_buf.go
dispatcher/pkg/pool/msg_buf.go
dispatcher/pkg/pool/msg_buf_test.go
dispatcher/pkg/pool/timer.go
dispatcher/pkg/server/dns_handler/server_handler.go
dispatcher/pkg/server/doh.go
dispatcher/pkg/server/http_handler/handler.go
dispatcher/pkg/server/http_handler/option.go
dispatcher/pkg/server/option.go
dispatcher/pkg/server/server.go
dispatcher/pkg/server/server_test.go
dispatcher/pkg/server/tcp.go
dispatcher/pkg/server/testdata/test.test.cert
dispatcher/pkg/server/testdata/test.test.key
dispatcher/pkg/server/udp.go
dispatcher/pkg/upstream/option.go
dispatcher/pkg/upstream/transport.go
dispatcher/pkg/upstream/transport_test.go
dispatcher/pkg/upstream/upstream.go
dispatcher/pkg/upstream/upstream_doh.go
dispatcher/pkg/upstream/upstream_test.go
dispatcher/pkg/utils/utils.go
dispatcher/pkg/utils/utils_test.go
dispatcher/plugin/enabled_plugin.go
dispatcher/plugin/enabled_plugin_test.go
dispatcher/plugin/executable/arbitrary/arbitrary.go
dispatcher/plugin/executable/blackhole/blackhole.go
dispatcher/plugin/executable/blackhole/blackhole_test.go
dispatcher/plugin/executable/cache/cache.go
dispatcher/plugin/executable/ecs/ecs.go
dispatcher/plugin/executable/ecs/ecs_test.go
dispatcher/plugin/executable/fallback/fallback.go
dispatcher/plugin/executable/fast_forward/fast_forward.go
dispatcher/plugin/executable/forward/forward.go
dispatcher/plugin/executable/hosts/hosts.go
dispatcher/plugin/executable/ipset/ipset.go
dispatcher/plugin/executable/ipset/ipset_handler_linux.go
dispatcher/plugin/executable/ipset/ipset_handler_other.go
dispatcher/plugin/executable/ipset/ipset_linux.go
dispatcher/plugin/executable/parallel/parallel.go
dispatcher/plugin/executable/pipeline/pipeline.go
dispatcher/plugin/executable/sequence/sequence.go
dispatcher/plugin/executable/sleep/sleep.go
dispatcher/plugin/executable/sleep/sleep_test.go
dispatcher/plugin/executable/ttl/ttl.go
dispatcher/plugin/matcher/query_matcher/query_matcher.go
dispatcher/plugin/matcher/response_matcher/response_matcher.go
dispatcher/plugin/server/server.go
go.mod
go.sum
main.go
tools/tools.go

/openwrt/staging_dir/target-aarch64_generic_musl/usr/share/gocode/src does not exist, skipping symlinks

Finding targets
go: downloading go.uber.org/zap v1.16.0
go: downloading gopkg.in/yaml.v3 v3.0.0-20210107192922-496545a6307b
go: downloading github.com/kardianos/service v1.2.0
go: downloading github.com/miekg/dns v1.1.42
go: downloading github.com/go-redis/redis/v8 v8.8.2
go: downloading github.com/mitchellh/mapstructure v1.4.1
go: downloading github.com/golang/protobuf v1.5.2
go: downloading google.golang.org/protobuf v1.26.0
go: downloading golang.org/x/net v0.0.0-20210510120150-4163338589ed
go: downloading golang.org/x/sync v0.0.0-20210220032951-036812b2e83c
go: downloading github.com/AdguardTeam/dnsproxy v0.37.3
go: downloading github.com/vishvananda/netlink v1.1.1-0.20201029203352-d40f9887b852
go: downloading golang.org/x/sys v0.0.0-20210514084401-e8d321eab015
go: downloading go.uber.org/atomic v1.7.0
go: downloading go.uber.org/multierr v1.7.0
go: downloading github.com/cespare/xxhash/v2 v2.1.1
go: downloading github.com/dgryski/go-rendezvous v0.0.0-20200823014737-9f7001d12a5f
go: downloading go.opentelemetry.io/otel v0.20.0
go: downloading github.com/AdguardTeam/golibs v0.4.5
go: downloading github.com/ameshkov/dnscrypt/v2 v2.1.3
go: downloading github.com/ameshkov/dnsstamps v1.0.3
go: downloading github.com/joomcode/errorx v1.0.3
go: downloading github.com/lucas-clemente/quic-go v0.20.1
go: downloading github.com/vishvananda/netns v0.0.0-20210104183010-2eb08e3e575f
go: downloading go.opentelemetry.io/otel/metric v0.20.0
go: downloading go.opentelemetry.io/otel/trace v0.20.0
go: downloading golang.org/x/text v0.3.6
go: downloading golang.org/x/crypto v0.0.0-20210513164829-c07d793c2f9a
go: downloading github.com/cheekybits/genny v1.0.0
go: downloading github.com/aead/chacha20 v0.0.0-20180709150244-8b13a72661da
go: downloading github.com/aead/poly1305 v0.0.0-20180717145839-3fee0db0b635
go: downloading github.com/marten-seemann/qtls-go1-16 v0.1.3

Building targets
internal/unsafeheader
internal/cpu
runtime/internal/atomic
internal/bytealg
runtime/internal/sys
runtime/internal/math
math/bits
runtime
math
unicode/utf8
internal/race
sync/atomic
unicode
encoding
unicode/utf16
container/list
crypto/internal/subtle
crypto/subtle
vendor/golang.org/x/crypto/cryptobyte/asn1
internal/nettrace
runtime/cgo
internal/reflectlite
errors
strconv
sync
sort
reflect
io
internal/oserror
syscall
internal/syscall/unix
time
internal/fmtsort
internal/syscall/execenv
internal/testlog
path
internal/poll
io/fs
strings
os
context
bytes
encoding/binary
fmt
encoding/base64
go.uber.org/zap/buffer
go.uber.org/zap/internal/bufferpool
go.uber.org/zap/internal/exit
path/filepath
io/ioutil
bufio
flag
encoding/json
go.uber.org/zap/internal/color
log
compress/flate
hash
hash/crc32
compress/gzip
go.uber.org/atomic
crypto/cipher
go.uber.org/multierr
go.uber.org/zap/zapcore
crypto/aes
math/rand
math/big
crypto
crypto/des
crypto/internal/randutil
crypto/sha512
crypto/ed25519/internal/edwards25519
crypto/hmac
crypto/md5
crypto/rc4
crypto/rand
crypto/elliptic
encoding/asn1
crypto/ed25519
vendor/golang.org/x/crypto/cryptobyte
crypto/rsa
crypto/sha1
crypto/sha256
crypto/ecdsa
crypto/dsa
encoding/hex
encoding/pem
crypto/x509/pkix
vendor/golang.org/x/net/dns/dnsmessage
internal/singleflight
net/url
vendor/golang.org/x/crypto/internal/subtle
vendor/golang.org/x/crypto/chacha20
net
vendor/golang.org/x/crypto/poly1305
vendor/golang.org/x/crypto/chacha20poly1305
vendor/golang.org/x/crypto/curve25519
vendor/golang.org/x/crypto/hkdf
vendor/golang.org/x/text/transform
vendor/golang.org/x/text/unicode/bidi
vendor/golang.org/x/text/secure/bidirule
vendor/golang.org/x/text/unicode/norm
vendor/golang.org/x/net/idna
vendor/golang.org/x/net/http2/hpack
mime
mime/quotedprintable
net/http/internal
encoding/base32
golang.org/x/net/bpf
golang.org/x/net/internal/iana
golang.org/x/sys/internal/unsafeheader
golang.org/x/sys/unix
hash/maphash
github.com/IrineSistiana/mosdns/dispatcher/pkg/concurrent_map
github.com/IrineSistiana/mosdns/dispatcher/pkg/concurrent_limiter
github.com/IrineSistiana/mosdns/dispatcher/pkg/load_cache
runtime/debug
golang.org/x/sync/singleflight
regexp/syntax
regexp
crypto/x509
net/textproto
vendor/golang.org/x/net/http/httpguts
vendor/golang.org/x/net/http/httpproxy
mime/multipart
golang.org/x/net/internal/socket
golang.org/x/net/ipv4
crypto/tls
golang.org/x/net/ipv6
github.com/mitchellh/mapstructure
hash/fnv
google.golang.org/protobuf/internal/detrand
google.golang.org/protobuf/internal/errors
google.golang.org/protobuf/encoding/protowire
google.golang.org/protobuf/internal/pragma
google.golang.org/protobuf/reflect/protoreflect
net/http/httptrace
github.com/miekg/dns
net/http
github.com/IrineSistiana/mosdns/dispatcher/pkg/pool
github.com/IrineSistiana/mosdns/dispatcher/pkg/dnsutils
google.golang.org/protobuf/internal/encoding/messageset
go.uber.org/zap
google.golang.org/protobuf/internal/flags
go/token
google.golang.org/protobuf/internal/strs
google.golang.org/protobuf/internal/encoding/text
google.golang.org/protobuf/internal/genid
github.com/IrineSistiana/mosdns/dispatcher/mlog
google.golang.org/protobuf/internal/order
github.com/IrineSistiana/mosdns/dispatcher/handler
google.golang.org/protobuf/internal/set
google.golang.org/protobuf/reflect/protoregistry
github.com/IrineSistiana/mosdns/dispatcher/pkg/utils
google.golang.org/protobuf/runtime/protoiface
google.golang.org/protobuf/proto
github.com/IrineSistiana/mosdns/dispatcher/pkg/matcher/domain
github.com/IrineSistiana/mosdns/dispatcher/pkg/matcher/netlist
google.golang.org/protobuf/encoding/prototext
google.golang.org/protobuf/internal/encoding/defval
google.golang.org/protobuf/internal/descfmt
google.golang.org/protobuf/internal/descopts
google.golang.org/protobuf/internal/filedesc
google.golang.org/protobuf/internal/version
github.com/IrineSistiana/mosdns/dispatcher/pkg/arbitrary
github.com/IrineSistiana/mosdns/dispatcher/plugin/executable/arbitrary
github.com/IrineSistiana/mosdns/dispatcher/plugin/executable/blackhole
github.com/IrineSistiana/mosdns/dispatcher/pkg/cache
github.com/IrineSistiana/mosdns/dispatcher/pkg/lru
github.com/IrineSistiana/mosdns/dispatcher/pkg/concurrent_lru
github.com/IrineSistiana/mosdns/dispatcher/pkg/cache/mem_cache
github.com/cespare/xxhash/v2
github.com/dgryski/go-rendezvous
github.com/go-redis/redis/v8/internal/util
github.com/go-redis/redis/v8/internal/proto
google.golang.org/protobuf/internal/encoding/tag
github.com/go-redis/redis/v8/internal/rand
google.golang.org/protobuf/internal/impl
go.opentelemetry.io/otel/internal
go.opentelemetry.io/otel/attribute
go.opentelemetry.io/otel/codes
go.opentelemetry.io/otel/trace
go.opentelemetry.io/otel/internal/trace/noop
go.opentelemetry.io/otel/metric/number
go.opentelemetry.io/otel/unit
go.opentelemetry.io/otel/metric
go.opentelemetry.io/otel/metric/registry
go.opentelemetry.io/otel/internal/baggage
go.opentelemetry.io/otel/propagation
go.opentelemetry.io/otel/internal/global
go.opentelemetry.io/otel
go.opentelemetry.io/otel/metric/global
github.com/go-redis/redis/v8/internal
github.com/go-redis/redis/v8/internal/hashtag
github.com/go-redis/redis/v8/internal/hscan
github.com/go-redis/redis/v8/internal/pool
github.com/go-redis/redis/v8
google.golang.org/protobuf/internal/filetype
google.golang.org/protobuf/runtime/protoimpl
google.golang.org/protobuf/types/descriptorpb
google.golang.org/protobuf/reflect/protodesc
github.com/golang/protobuf/proto
github.com/IrineSistiana/mosdns/dispatcher/pkg/matcher/v2data
github.com/IrineSistiana/mosdns/dispatcher/plugin/executable/ecs
github.com/IrineSistiana/mosdns/dispatcher/pkg/executable_seq
github.com/IrineSistiana/mosdns/dispatcher/plugin/executable/fallback
golang.org/x/text/transform
golang.org/x/text/unicode/bidi
golang.org/x/text/secure/bidirule
golang.org/x/text/unicode/norm
golang.org/x/net/idna
golang.org/x/net/http/httpguts
golang.org/x/net/http2/hpack
golang.org/x/net/http2
golang.org/x/net/internal/socks
golang.org/x/net/proxy
github.com/IrineSistiana/mosdns/dispatcher/pkg/upstream
github.com/IrineSistiana/mosdns/dispatcher/pkg/cache/redis_cache
github.com/IrineSistiana/mosdns/dispatcher/plugin/executable/cache
github.com/AdguardTeam/dnsproxy/proxyutil
github.com/IrineSistiana/mosdns/dispatcher/plugin/executable/fast_forward
github.com/AdguardTeam/golibs/log
github.com/aead/chacha20/chacha
github.com/aead/poly1305
golang.org/x/crypto/curve25519/internal/field
github.com/ameshkov/dnsstamps
golang.org/x/crypto/blake2b
golang.org/x/crypto/curve25519
github.com/ameshkov/dnscrypt/v2/xsecretbox
golang.org/x/crypto/internal/subtle
golang.org/x/crypto/poly1305
golang.org/x/crypto/salsa20/salsa
github.com/joomcode/errorx
golang.org/x/crypto/nacl/secretbox
golang.org/x/crypto/nacl/box
github.com/ameshkov/dnscrypt/v2
github.com/cheekybits/genny/generic
github.com/lucas-clemente/quic-go/internal/protocol
golang.org/x/crypto/chacha20
github.com/lucas-clemente/quic-go/internal/utils
golang.org/x/crypto/chacha20poly1305
golang.org/x/crypto/cryptobyte/asn1
golang.org/x/crypto/cryptobyte
golang.org/x/crypto/hkdf
golang.org/x/sys/cpu
github.com/lucas-clemente/quic-go/quicvarint
github.com/AdguardTeam/golibs/cache
github.com/marten-seemann/qtls-go1-16
github.com/IrineSistiana/mosdns/dispatcher/pkg/hosts
github.com/IrineSistiana/mosdns/dispatcher/plugin/executable/hosts
github.com/vishvananda/netns
github.com/vishvananda/netlink/nl
github.com/IrineSistiana/mosdns/dispatcher/plugin/executable/ipset
github.com/IrineSistiana/mosdns/dispatcher/plugin/executable/parallel
github.com/IrineSistiana/mosdns/dispatcher/plugin/executable/pipeline
github.com/IrineSistiana/mosdns/dispatcher/plugin/executable/sequence
github.com/IrineSistiana/mosdns/dispatcher/plugin/executable/sleep
github.com/IrineSistiana/mosdns/dispatcher/plugin/executable/ttl
github.com/IrineSistiana/mosdns/dispatcher/pkg/matcher/elem
github.com/IrineSistiana/mosdns/dispatcher/pkg/matcher/msg_matcher
github.com/IrineSistiana/mosdns/dispatcher/plugin/matcher/query_matcher
github.com/IrineSistiana/mosdns/dispatcher/plugin/matcher/response_matcher
internal/sysinfo
runtime/trace
testing
github.com/lucas-clemente/quic-go/internal/qtls
github.com/lucas-clemente/quic-go/internal/qerr
github.com/lucas-clemente/quic-go/internal/wire
github.com/lucas-clemente/quic-go/internal/flowcontrol
github.com/IrineSistiana/mosdns/dispatcher/pkg/server/dns_handler
github.com/IrineSistiana/mosdns/dispatcher/pkg/server
github.com/IrineSistiana/mosdns/dispatcher/pkg/server/http_handler
github.com/IrineSistiana/mosdns/dispatcher/plugin/server
github.com/lucas-clemente/quic-go/logging
github.com/lucas-clemente/quic-go/internal/congestion
gopkg.in/yaml.v3
github.com/lucas-clemente/quic-go/internal/ackhandler
github.com/lucas-clemente/quic-go/internal/handshake
github.com/lucas-clemente/quic-go/internal/logutils
github.com/lucas-clemente/quic-go
os/signal
plugin
github.com/AdguardTeam/dnsproxy/upstream
github.com/AdguardTeam/dnsproxy/fastip
github.com/IrineSistiana/mosdns/dispatcher/plugin/executable/forward
github.com/IrineSistiana/mosdns/tools
github.com/IrineSistiana/mosdns/dispatcher/plugin
github.com/IrineSistiana/mosdns/dispatcher/coremain
log/syslog
os/exec
text/template/parse
html
internal/profile
text/template
text/tabwriter
runtime/pprof
github.com/kardianos/service
net/http/pprof
github.com/IrineSistiana/mosdns
# github.com/IrineSistiana/mosdns
/openwrt/staging_dir/hostpkg/lib/go-cross/pkg/tool/linux_amd64/link: running ccache_cc failed: exit status 1
collect2: fatal error: cannot find 'ld'
compilation terminated.


make[3]: *** [Makefile:132: /openwrt/build_dir/target-aarch64_generic_musl/mosdns-1.8.6/.built] Error 2
```
