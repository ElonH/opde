---
title: "compile.50"
date: 2021-02-25 14:20:49.077914
hidden: false
draft: false
weight: -50
---

build number: `50`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/base/ndpi-netfilter/compile -j$(nproc) || make package/feeds/base/ndpi-netfilter/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-main.patch using plaintext: 
patching file nDPI-patch/src/lib/protocols/netflow.c
patching file src/main.c
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0'
make -C ipt
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/ipt'
if test -d ndpi_cpy; then \
	cp /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/nDPI/src/* ndpi_cpy -R; \
else \
	mkdir ndpi_cpy; \
	cp /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/nDPI/src/* ndpi_cpy -R; \
fi
make libxt_ndpi.so
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/ipt'
ccache_cc -fPIC -Indpi_cpy/include -Indpi_cpy/lib -I../src -DOPENDPI_NETFILTER_MODULE -O2 -Wall -DNDPI_IPTABLES_EXT -D_INIT=libxt_ndpi_init -c -o libxt_ndpi.o libxt_ndpi.c;
libxt_ndpi.c: In function 'ndpi_mt_init':
libxt_ndpi.c:112:25: warning: unused variable 'info' [-Wunused-variable]
  struct xt_ndpi_mtinfo *info = (void *)match->data;
                         ^~~~
ccache_cc -shared -o libxt_ndpi.so libxt_ndpi.o;
rm libxt_ndpi.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/ipt'
rm -r ndpi_cpy
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/ipt'
make -C src
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src'
if test -d ndpi_cpy; then \
	cp /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/nDPI/src/* ndpi_cpy -R; \
else \
	mkdir ndpi_cpy; \
	cp /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/nDPI/src/* ndpi_cpy -R; \
fi
cp ndpi_cpy/../../nDPI-patch/src/* ndpi_cpy/ -R;
cp ndpi_cpy/lib/third_party/src/*.c ndpi_cpy/lib -R;
cp ndpi_cpy/lib/third_party/include/*.h ndpi_cpy/lib -R;
cp ndpi_cpy/lib/third_party/include/*.h ndpi_cpy/include -R;
sed -i "s/^\s*void ndpi_free_flow/\/\/void ndpi_free_flow/" ndpi_cpy/include/ndpi_api.h;
make -C /openwrt/build_dir/target-x86_64_musl/linux-x86_64/linux-5.4.99 M=$PWD;
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/linux-5.4.99'
  AR      /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/built-in.a
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/main.o
../../ndpi-netfilter-3.0/src/main.c:99:13: warning: 'debug_printf' defined but not used [-Wunused-function]
 static void debug_printf(u32 protocol, void *id_struct,
             ^~~~~~~~~~~~
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/ndpi_main.o
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/ndpi_main.c: In function 'ndpi_guess_protocol_id':
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/ndpi_main.c:2035:34: warning: unused variable 'node' [-Wunused-variable]
   ndpi_default_ports_tree_node_t node;
                                  ^~~~
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/ndpi_main.c:2034:15: warning: unused variable 'ret' [-Wunused-variable]
   const void *ret;
               ^~~
In file included from ../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/ndpi_main.c:51:
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/third_party/src/ndpi_patricia.c: In function 'ndpi_Clear_Patricia':
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/third_party/src/ndpi_patricia.c:489:1: warning: the frame size of 1040 bytes is larger than 1024 bytes [-Wframe-larger-than=]
 }
 ^
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/third_party/src/ndpi_patricia.c: In function 'ndpi_patricia_process':
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/third_party/src/ndpi_patricia.c:513:1: warning: the frame size of 1032 bytes is larger than 1024 bytes [-Wframe-larger-than=]
 }
 ^
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/third_party/src/ndpi_patricia.c: In function 'ndpi_patricia_search_best2':
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/third_party/src/ndpi_patricia.c:699:1: warning: the frame size of 1032 bytes is larger than 1024 bytes [-Wframe-larger-than=]
 }
 ^
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/ahocorasick.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/node.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/sort.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/afp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/aimini.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/applejuice.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/armagetron.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/battlefield.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/bgp.o
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/bgp.c:28:13: warning: 'ndpi_int_bgp_add_connection' defined but not used [-Wunused-function]
 static void ndpi_int_bgp_add_connection(struct ndpi_detection_module_struct *ndpi_struct, struct ndpi_flow_struct *flow)
             ^~~~~~~~~~~~~~~~~~~~~~~~~~~
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/bittorrent.o
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/bittorrent.c: In function 'ndpi_search_bittorrent':
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/bittorrent.c:390:7: warning: unused variable 'no_bittorrent' [-Wunused-variable]
   int no_bittorrent = 0;
       ^~~~~~~~~~~~~
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/citrix.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/ciscovpn.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/corba.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/crossfire.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/dcerpc.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/dhcp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/dhcpv6.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/directconnect.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/directdownloadlink.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/dns.o
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/dns.c: In function 'ndpi_search_dns':
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/dns.c:186:7: warning: ISO C90 forbids mixed declarations and code [-Wdeclaration-after-statement]
       int j = 0, max_len = sizeof(flow->host_server_name)-1, off = sizeof(struct ndpi_dns_packet_header) + 1;
       ^~~
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/dofus.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/drda.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/dropbox.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/edonkey.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/git.o
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/git.c: In function 'ndpi_search_git':
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/git.c:46:17: warning: unused variable 'git_len' [-Wunused-variable]
       u_int16_t git_len = 0, offset = 0;
                 ^~~~~~~
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/gtp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/lotus_notes.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/fasttrack.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/fiesta.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/filetopia.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/florensia.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/ftp_control.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/ftp_data.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/gnutella.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/guildwars.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/hangout.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/halflife2_and_mods.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/h323.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/http.o
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/http.c: In function 'parseHttpSubprotocol':
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/http.c:167:30: warning: unused variable 'packet' [-Wunused-variable]
   struct ndpi_packet_struct *packet = &flow->packet;
                              ^~~~~~
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/http_activesync.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/iax.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/icecast.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/ipp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/irc.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/jabber.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/kerberos.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/kontiki.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/ldap.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/mail_imap.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/mail_pop.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/mail_smtp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/maplestory.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/mdns.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/mgcp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/mms.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/msn.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/mssql_tds.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/mysql.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/whoisdas.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/netbios.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/netflow.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/nfs.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/noe.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/non_tcp_udp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/ntp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/openft.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/openvpn.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/oracle.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/oscar.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/pando.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/pcanywhere.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/postgres.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/pplive.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/ppstream.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/pptp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/qq.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/quake.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/quic.o
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/quic.c: In function 'ndpi_search_quic':
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/quic.c:76:11: warning: unused variable 'begin' [-Wunused-variable]
     char *begin;
           ^~~~~
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/eaq.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/kakaotalk_voice.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/mpegts.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/starcraft.o
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/starcraft.c: In function 'sc2_match_logon_ip':
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/starcraft.c:33:3: warning: ISO C90 forbids mixed declarations and code [-Wdeclaration-after-statement]
   u_int32_t source_ip = ntohl(packet->iph->saddr);
   ^~~~~~~~~
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/teredo.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/hep.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/ubntac2.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/radius.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/rdp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/rtp.o
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/rtp.c: In function 'ndpi_rtp_search':
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/rtp.c:79:3: warning: ISO C90 forbids mixed declarations and code [-Wdeclaration-after-statement]
   u_int8_t payloadType, payload_type = payload[1] & 0x7F;
   ^~~~~~~~
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/rtsp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/rtmp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/rtcp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/rsync.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/sflow.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/shoutcast.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/sip.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/zeromq.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/skinny.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/skype.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/smb.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/snmp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/coap.o
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/coap.c: In function 'ndpi_search_coap':
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/coap.c:116:15: warning: unused variable 'd_port' [-Wunused-variable]
     u_int16_t d_port = ntohs(flow->packet.udp->dest);
               ^~~~~~
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/socrates.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/socks45.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/sopcast.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/soulseek.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/spotify.o
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/spotify.c: In function 'ndpi_check_spotify':
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/spotify.c:97:76: warning: bitwise comparison always evaluates to false [-Wtautological-compare]
           || ((ntohl(packet->iph->saddr) & 0xFFFFFC00 /* 255.255.252.0 */) == 0xC284A200 /* 194.132.162.0 */)
                                                                            ^~
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/spotify.c:98:76: warning: bitwise comparison always evaluates to false [-Wtautological-compare]
           || ((ntohl(packet->iph->daddr) & 0xFFFFFC00 /* 255.255.252.0 */) == 0xC284A200 /* 194.132.162.0 */)
                                                                            ^~
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/ssdp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/ssh.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/ssl.o
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/ssl.c: In function 'sslDetectProtocolFromCertificate':
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/ssl.c:332:2: warning: ISO C90 forbids mixed declarations and code [-Wdeclaration-after-statement]
  u_int32_t subproto = ndpi_match_host_subprotocol(ndpi_struct, flow, certificate,
  ^~~~~~~~~
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/stealthnet.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/steam.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/stun.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/syslog.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/tcp_udp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/teamviewer.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/telegram.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/telnet.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/teamspeak.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/tftp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/thunder.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/tvants.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/tvuplayer.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/tor.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/usenet.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/viber.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/vmware.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/vnc.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/warcraft3.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/world_of_kung_fu.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/world_of_warcraft.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/xbox.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/xdmcp.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/yahoo.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/megaco.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/redis_net.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/vhua.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/ayiya.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/zattoo.o
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/rx.o
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/rx.c: In function 'ndpi_check_rx':
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/rx.c:94:3: warning: ISO C90 forbids mixed declarations and code [-Wdeclaration-after-statement]
   struct ndpi_rx_header *header = (struct ndpi_rx_header*) packet->payload;
   ^~~~~~
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/rx.c:81:7: warning: unused variable 'found' [-Wunused-variable]
   int found = 0;
       ^~~~~
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/rx.c:131:57: warning: this statement may fall through [-Wimplicit-fallthrough=]
     header->flags == PLUS_2 || header->flags == REQ_ACK ||
                                                         ^
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/rx.c:134:7: note: here
       case ACK:
       ^~~~
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/rx.c:135:70: warning: this statement may fall through [-Wimplicit-fallthrough=]
  if(header->flags == CLIENT_INIT_1 || header->flags == CLIENT_INIT_2 ||
                                                                      ^
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/rx.c:138:7: note: here
       case CHALLENGE:
       ^~~~
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/rx.c:139:28: warning: this statement may fall through [-Wimplicit-fallthrough=]
  if(header->flags == EMPTY || header->call_number == 0)
     ~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/rx.c:141:7: note: here
       case RESPONSE:
       ^~~~
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/rx.c:142:28: warning: this statement may fall through [-Wimplicit-fallthrough=]
  if(header->flags == EMPTY || header->call_number == 0)
     ~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/rx.c:144:7: note: here
       case ACKALL:
       ^~~~
  CC [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/mqtt.o
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/mqtt.c: In function 'ndpi_search_mqtt':
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/mqtt.c:65:2: warning: ISO C90 forbids mixed declarations and code [-Wdeclaration-after-statement]
  struct ndpi_packet_struct *packet = &flow->packet;
  ^~~~~~
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/mqtt.c:89:2: warning: ISO C90 forbids mixed declarations and code [-Wdeclaration-after-statement]
  u_int8_t rl = (u_int8_t) (packet->payload[1]);
  ^~~~~~~~
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/mqtt.c:96:2: warning: ISO C90 forbids mixed declarations and code [-Wdeclaration-after-statement]
  u_int8_t pt = (u_int8_t) ((packet->payload[0] & 0xF0) >> 4);
  ^~~~~~~~
../../ndpi-netfilter-3.0/src/ndpi_cpy/lib/protocols/mqtt.c:104:2: warning: ISO C90 forbids mixed declarations and code [-Wdeclaration-after-statement]
  u_int8_t flags = (u_int8_t) (packet->payload[0] & 0x0F);
  ^~~~~~~~
  LD [M]  /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/xt_ndpi.o
  Building modules, stage 2.
  MODPOST 1 modules
ERROR: "nf_ct_l3proto_try_module_get" [/openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/xt_ndpi.ko] undefined!
ERROR: "nf_ct_l3proto_module_put" [/openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src/xt_ndpi.ko] undefined!
make[7]: *** [scripts/Makefile.modpost:94: __modpost] Error 1
make[6]: *** [Makefile:1639: modules] Error 2
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/linux-x86_64/linux-5.4.99'
make[5]: *** [Makefile:161: all] Error 2
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/src'
make[4]: *** [Makefile:6: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0'
make[3]: *** [Makefile:68: /openwrt/build_dir/target-x86_64_musl/ndpi-netfilter-3.0/.built] Error 2
```
