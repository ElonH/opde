---
title: "compile.14"
date: 2021-05-12 23:05:59.604531
hidden: false
draft: false
weight: -14
---

build number: `14`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/adguardhome/compile -j$(nproc) || make package/feeds/packages/adguardhome/compile V=s
```

#### Compile.txt

``` bash
Copying files from /openwrt/build_dir/target-aarch64_cortex-a72_musl/adguardhome-0.106.1 into /openwrt/build_dir/target-aarch64_cortex-a72_musl/adguardhome-0.106.1/.go_work/build/src/github.com/AdguardTeam/AdGuardHome
go.mod
go.sum
internal/agherr/agherr.go
internal/agherr/agherr_test.go
internal/aghio/limitedreadcloser.go
internal/aghio/limitedreadcloser_test.go
internal/aghnet/addr.go
internal/aghnet/addr_test.go
internal/aghnet/etchostscontainer.go
internal/aghnet/etshostscontainer_test.go
internal/aghnet/net.go
internal/aghnet/net_darwin.go
internal/aghnet/net_linux.go
internal/aghnet/net_linux_test.go
internal/aghnet/net_others.go
internal/aghnet/net_test.go
internal/aghnet/subnetdetector.go
internal/aghnet/subnetdetector_test.go
internal/aghnet/systemresolvers.go
internal/aghnet/systemresolvers_others.go
internal/aghnet/systemresolvers_others_test.go
internal/aghnet/systemresolvers_test.go
internal/aghnet/systemresolvers_windows.go
internal/aghnet/systemresolvers_windows_test.go
internal/aghos/endian_big.go
internal/aghos/endian_little.go
internal/aghos/os.go
internal/aghos/os_darwin.go
internal/aghos/os_freebsd.go
internal/aghos/os_linux.go
internal/aghos/os_windows.go
internal/aghos/syslog.go
internal/aghos/syslog_others.go
internal/aghos/syslog_windows.go
internal/aghos/sysutil_test.go
internal/aghstrings/set.go
internal/aghstrings/set_test.go
internal/aghstrings/strings.go
internal/aghstrings/strings_test.go
internal/aghtest/aghtest.go
internal/aghtest/exchanger.go
internal/aghtest/resolver.go
internal/aghtest/upstream.go
internal/dhcpd/bitset.go
internal/dhcpd/bitset_test.go
internal/dhcpd/checkother.go
internal/dhcpd/checkother_windows.go
internal/dhcpd/db.go
internal/dhcpd/dhcpd.go
internal/dhcpd/dhcpd_test.go
internal/dhcpd/helpers.go
internal/dhcpd/http.go
internal/dhcpd/http_test.go
internal/dhcpd/iprange.go
internal/dhcpd/iprange_test.go
internal/dhcpd/nullbool.go
internal/dhcpd/nullbool_test.go
internal/dhcpd/options.go
internal/dhcpd/options_test.go
internal/dhcpd/os_windows.go
internal/dhcpd/routeradv.go
internal/dhcpd/routeradv_test.go
internal/dhcpd/server.go
internal/dhcpd/v4.go
internal/dhcpd/v46.go
internal/dhcpd/v46_test.go
internal/dhcpd/v46_windows.go
internal/dhcpd/v4_test.go
internal/dhcpd/v6.go
internal/dhcpd/v6_test.go
internal/dnsfilter/blocked.go
internal/dnsfilter/blocked_test.go
internal/dnsfilter/dnsfilter.go
internal/dnsfilter/dnsfilter_test.go
internal/dnsfilter/dnsrewrite.go
internal/dnsfilter/dnsrewrite_test.go
internal/dnsfilter/rewrites.go
internal/dnsfilter/rewrites_test.go
internal/dnsfilter/safebrowsing.go
internal/dnsfilter/safebrowsing_test.go
internal/dnsfilter/safesearch.go
internal/dnsforward/access.go
internal/dnsforward/access_test.go
internal/dnsforward/clientid.go
internal/dnsforward/clientid_test.go
internal/dnsforward/config.go
internal/dnsforward/dns.go
internal/dnsforward/dns_test.go
internal/dnsforward/dnsforward.go
internal/dnsforward/dnsforward_test.go
internal/dnsforward/dnsrewrite.go
internal/dnsforward/dnsrewrite_test.go
internal/dnsforward/filter.go
internal/dnsforward/http.go
internal/dnsforward/http_test.go
internal/dnsforward/ipset_linux.go
internal/dnsforward/ipset_others.go
internal/dnsforward/msg.go
internal/dnsforward/stats.go
internal/dnsforward/stats_test.go
internal/dnsforward/svcbmsg.go
internal/dnsforward/svcbmsg_test.go
internal/dnsforward/testdata/TestDNSForwardHTTTP_handleGetConfig.json
internal/dnsforward/testdata/TestDNSForwardHTTTP_handleSetConfig.json
internal/dnsforward/util.go
internal/dnsforward/util_test.go
internal/home/auth.go
internal/home/auth_test.go
internal/home/authglinet.go
internal/home/authglinet_test.go
internal/home/authratelimiter.go
internal/home/authratelimiter_test.go
internal/home/clients.go
internal/home/clients_test.go
internal/home/clientshttp.go
internal/home/clientstags.go
internal/home/config.go
internal/home/control.go
internal/home/control_test.go
internal/home/controlfiltering.go
internal/home/controlinstall.go
internal/home/controlupdate.go
internal/home/dns.go
internal/home/filter.go
internal/home/filter_test.go
internal/home/home.go
internal/home/home_test.go
internal/home/i18n.go
internal/home/memory.go
internal/home/middlewares.go
internal/home/middlewares_test.go
internal/home/mobileconfig.go
internal/home/mobileconfig_test.go
internal/home/options.go
internal/home/options_test.go
internal/home/rdns.go
internal/home/rdns_test.go
internal/home/service.go
internal/home/tls.go
internal/home/upgrade.go
internal/home/upgrade_test.go
internal/home/web.go
internal/home/whois.go
internal/home/whois_test.go
internal/querylog/client.go
internal/querylog/decode.go
internal/querylog/decode_test.go
internal/querylog/http.go
internal/querylog/json.go
internal/querylog/qlog.go
internal/querylog/qlog_test.go
internal/querylog/qlogfile.go
internal/querylog/qlogfile_test.go
internal/querylog/qlogreader.go
internal/querylog/qlogreader_test.go
internal/querylog/querylog.go
internal/querylog/querylogfile.go
internal/querylog/search.go
internal/querylog/search_test.go
internal/querylog/searchcriterion.go
internal/querylog/searchparams.go
internal/stats/http.go
internal/stats/stats.go
internal/stats/stats_test.go
internal/stats/unit.go
internal/tools/doc.go
internal/tools/go.mod
internal/tools/go.sum
internal/tools/tools.go
internal/updater/check.go
internal/updater/testdata/AdGuardHome.tar.gz
internal/updater/testdata/AdGuardHome.zip
internal/updater/updater.go
internal/updater/updater_test.go
internal/version/norace.go
internal/version/race.go
internal/version/version.go
main.go
tools.go

Symlinking directories from /openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/gocode/src into /openwrt/build_dir/target-aarch64_cortex-a72_musl/adguardhome-0.106.1/.go_work/build/src
.../github.com/Erope
.../github.com/iawia002
.../github.com/xtls
.../github.com/txthinking

/openwrt/build_dir/target-aarch64_cortex-a72_musl/adguardhome-0.106.1 /openwrt/feeds/packages/net/adguardhome
make[4]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/adguardhome-0.106.1'
npm --prefix client --quiet --no-progress --ignore-engines --ignore-optional --ignore-platform --ignore-scripts ci
npm ERR! code ECONNRESET
npm ERR! errno ECONNRESET
npm ERR! network request to https://registry.npmjs.org/eslint-plugin-react/-/eslint-plugin-react-7.20.0.tgz failed, reason: Client network socket disconnected before secure TLS connection was established
npm ERR! network This is a problem related to network connectivity.
npm ERR! network In most cases you are behind a proxy or have bad network settings.
npm ERR! network 
npm ERR! network If you are behind a proxy, please make sure that the
npm ERR! network 'proxy' config is set properly.  See: 'npm help config'

npm ERR! A complete log of this run can be found in:
npm ERR!     /home/opde/.npm/_logs/2021-05-12T15_55_05_072Z-debug.log
make[4]: *** [Makefile:78: js-deps] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/adguardhome-0.106.1'
building box ../../build/static
Error: lstat build: no such file or directory
Usage:
  packr [flags]
  packr [command]

Available Commands:
  build       Wraps the go build command with packr
  clean       removes any *-packr.go files
  help        Help about any command
  install     Wraps the go install command with packr
  version     prints packr version

Flags:
  -z, --compress       compress box contents
  -h, --help           help for packr
  -i, --input string   path to scan for packr Boxes (default "/openwrt/build_dir/target-aarch64_cortex-a72_musl/adguardhome-0.106.1")
  -v, --verbose        print verbose logging information

Use "packr [command] --help" for more information about a command.

/openwrt/feeds/packages/net/adguardhome
Finding targets
go: github.com/AdguardTeam/dnsproxy@v0.37.2: Get "https://proxy.golang.org/github.com/%21adguard%21team/dnsproxy/@v/v0.37.2.mod": net/http: TLS handshake timeout

Building targets
go: github.com/AdguardTeam/dnsproxy@v0.37.2: Get "https://proxy.golang.org/github.com/%21adguard%21team/dnsproxy/@v/v0.37.2.mod": write tcp 172.17.0.2:54140->192.168.123.159:10801: write: connection reset by peer

make[3]: *** [Makefile:97: /openwrt/build_dir/target-aarch64_cortex-a72_musl/adguardhome-0.106.1/.built] Error 1
```
