---
title: "compile.60"
date: 2021-02-18 15:10:27.214725
hidden: false
draft: false
weight: -60
---

build number: `60`

path: `package/feeds/packages/gnunet/compile`


``` bash
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3'
make  all-recursive
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3'
Making all in m4
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/m4'
make[6]: Nothing to be done for 'all'.
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/m4'
Making all in bin
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/bin'
make[6]: Nothing to be done for 'all'.
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/bin'
Making all in src
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src'
Making all in include
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/include'
Making all in .
make[8]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/include'
make[8]: Nothing to be done for 'all-am'.
make[8]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/include'
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/include'
Making all in util
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/util'
  CC       bandwidth.lo
  CC       bio.lo
  CC       buffer.lo
  CC       client.lo
  CC       common_allocation.lo
  CC       common_endian.lo
  CC       common_logging.lo
  CC       configuration.lo
  CC       configuration_loader.lo
  CC       container_bloomfilter.lo
  CC       container_heap.lo
  CC       container_meta_data.lo
  CC       container_multihashmap.lo
  CC       container_multishortmap.lo
  CC       container_multiuuidmap.lo
  CC       container_multipeermap.lo
  CC       container_multihashmap32.lo
  CC       crypto_symmetric.lo
  CC       crypto_crc.lo
  CC       crypto_ecc.lo
  CC       crypto_ecc_dlog.lo
  CC       crypto_ecc_setup.lo
  CC       crypto_hash.lo
  CC       crypto_hash_file.lo
  CC       crypto_hkdf.lo
  CC       crypto_kdf.lo
  CC       crypto_mpi.lo
  CC       crypto_paillier.lo
  CC       crypto_pow.lo
  CC       crypto_random.lo
  CC       crypto_rsa.lo
  CC       disk.lo
  CC       dnsparser.lo
  CC       dnsstub.lo
  CC       getopt.lo
  CC       getopt_helpers.lo
  CC       helper.lo
  CC       load.lo
  CC       mst.lo
  CC       mq.lo
  CC       nc.lo
  CC       network.lo
  CC       op.lo
  CC       os_installation.lo
  CC       os_network.lo
  CC       os_priority.lo
  CC       peer.lo
  CC       plugin.lo
  CC       program.lo
  CC       regex.lo
  CC       resolver_api.lo
  CC       scheduler.lo
  CC       service.lo
  CC       signal.lo
  CC       strings.lo
  CC       time.lo
  CC       tun.lo
  CC       speedup.lo
  CC       gnunet-resolver.o
  CC       gnunet-config.o
  CC       gnunet-crypto-tvg.o
  CC       gnunet-ecc.o
  CC       gnunet-scrypt.o
  CC       gnunet-uri.o
  CC       gnunet-service-resolver.o
  CC       gnunet-config-diff.o
  CC       test_common_logging_dummy.o
  CCLD     libgnunetutil.la
  CCLD     gnunet-resolver
  CCLD     gnunet-config
  CCLD     gnunet-crypto-tvg
  CCLD     gnunet-ecc
  CCLD     gnunet-scrypt
  CCLD     gnunet-uri
  CCLD     gnunet-service-resolver
  CCLD     gnunet-config-diff
  CCLD     test_common_logging_dummy
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/util'
Making all in nt
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/nt'
  CC       nt.lo
  CCLD     libgnunetnt.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/nt'
Making all in gnsrecord
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/gnsrecord'
  CC       gnsrecord.lo
  CC       gnsrecord_serialization.lo
  CC       gnsrecord_crypto.lo
  CC       gnsrecord_misc.lo
  CC       plugin_gnsrecord_dns.lo
  CC       gnunet-gnsrecord-tvg.o
  CCLD     libgnunetgnsrecord.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_gnsrecord_dns.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-gnsrecord-tvg
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/gnsrecord'
Making all in hello
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/hello'
  CC       hello.lo
  CC       address.lo
  CC       hello-ng.lo
  CC       gnunet-hello.o
  CCLD     libgnunethello.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-hello
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/hello'
Making all in block
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/block'
  CC       block.lo
  CC       bg_bf.lo
  CC       plugin_block_template.lo
  CC       plugin_block_test.lo
  CCLD     libgnunetblock.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunetblockgroup.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_block_template.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CCLD     libgnunet_plugin_block_test.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/block'
Making all in statistics
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/statistics'
  CC       statistics_api.lo
  CC       gnunet-statistics.o
  CC       gnunet-service-statistics.o
  CCLD     libgnunetstatistics.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-statistics
  CCLD     gnunet-service-statistics
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/statistics'
Making all in arm
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/arm'
  CC       arm_api.lo
  CC       arm_monitor_api.lo
  CC       gnunet-arm.o
  CC       gnunet-service-arm.o
  CC       mockup-service.o
  CCLD     libgnunetarm.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-service-arm
  CCLD     mockup-service
  CCLD     gnunet-arm
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/arm'
Making all in testing
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/testing'
  CC       testing.lo
  CC       gnunet-testing.o
  CC       list-keys.o
  CCLD     libgnunettesting.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     list-keys
  CCLD     gnunet-testing
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/testing'
Making all in json
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/json'
  CC       libgnunetjson_la-json.lo
  CC       libgnunetjson_la-json_mhd.lo
  CC       libgnunetjson_la-json_generator.lo
  CC       libgnunetjson_la-json_helper.lo
  CC       libgnunetjson_la-json_gnsrecord.lo
  CCLD     libgnunetjson.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/json'
Making all in curl
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/curl'
  CC       libgnunetcurl_la-curl.lo
  CC       libgnunetcurl_la-curl_reschedule.lo
  CCLD     libgnunetcurl.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/curl'
Making all in rest
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/rest'
  CC       libgnunetrest_la-rest.lo
  CC       libgnunet_plugin_rest_copying_la-plugin_rest_copying.lo
  CC       libgnunet_plugin_rest_config_la-plugin_rest_config.lo
  CC       gnunet_rest_server-gnunet-rest-server.o
  CCLD     libgnunetrest.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-rest-server
  CCLD     libgnunet_plugin_rest_copying.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_rest_config.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/rest'
Making all in peerinfo
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/peerinfo'
  CC       peerinfo_api.lo
  CC       peerinfo_api_notify.lo
  CC       gnunet-service-peerinfo.o
  CCLD     libgnunetpeerinfo.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-service-peerinfo
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/peerinfo'
Making all in sq
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/sq'
  CC       sq.lo
  CC       sq_exec.lo
  CC       sq_prepare.lo
  CC       sq_query_helper.lo
  CC       sq_result_helper.lo
  CCLD     libgnunetsq.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/sq'
Making all in mysql
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/mysql'
  CC       mysql.lo
  CCLD     libgnunetmysql.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/mysql'
Making all in my
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/my'
  CC       my.lo
  CC       my_query_helper.lo
my_query_helper.c: In function 'my_conv_rsa_public_key':
my_query_helper.c:289:51: warning: passing argument 2 of 'GNUNET_CRYPTO_rsa_public_key_encode' from incompatible pointer type [-Wincompatible-pointer-types]
                                                   &buf);
                                                   ^~~~
In file included from ../../src/include/gnunet_util_lib.h:64,
                 from ../../src/include/gnunet_my_lib.h:34,
                 from my_query_helper.c:28:
../../src/include/gnunet_crypto_lib.h:2151:10: note: expected 'void **' but argument is of type 'char **'
   void **buffer);
   ~~~~~~~^~~~~~
my_query_helper.c: In function 'my_conv_rsa_signature':
my_query_helper.c:341:50: warning: passing argument 2 of 'GNUNET_CRYPTO_rsa_signature_encode' from incompatible pointer type [-Wincompatible-pointer-types]
                                                  &buf);
                                                  ^~~~
In file included from ../../src/include/gnunet_util_lib.h:64,
                 from ../../src/include/gnunet_my_lib.h:34,
                 from my_query_helper.c:28:
../../src/include/gnunet_crypto_lib.h:2275:10: note: expected 'void **' but argument is of type 'char **'
   void **buffer);
   ~~~~~~~^~~~~~
  CC       my_result_helper.lo
my_result_helper.c: In function 'pre_extract_varsize_blob':
my_result_helper.c:53:22: warning: assignment to 'my_bool *' {aka 'char *'} from incompatible pointer type 'MYSQL_BOOL *' {aka '_Bool *'} [-Wincompatible-pointer-types]
   results[0].is_null = &rs->is_null;
                      ^
my_result_helper.c: In function 'pre_extract_fixed_blob':
my_result_helper.c:179:22: warning: assignment to 'my_bool *' {aka 'char *'} from incompatible pointer type 'MYSQL_BOOL *' {aka '_Bool *'} [-Wincompatible-pointer-types]
   results[0].is_null = &rs->is_null;
                      ^
my_result_helper.c: In function 'pre_extract_rsa_public_key':
my_result_helper.c:262:22: warning: assignment to 'my_bool *' {aka 'char *'} from incompatible pointer type 'MYSQL_BOOL *' {aka '_Bool *'} [-Wincompatible-pointer-types]
   results[0].is_null = &rs->is_null;
                      ^
my_result_helper.c: In function 'pre_extract_rsa_signature':
my_result_helper.c:396:22: warning: assignment to 'my_bool *' {aka 'char *'} from incompatible pointer type 'MYSQL_BOOL *' {aka '_Bool *'} [-Wincompatible-pointer-types]
   results[0].is_null = &rs->is_null;
                      ^
my_result_helper.c: In function 'pre_extract_string':
my_result_helper.c:526:22: warning: assignment to 'my_bool *' {aka 'char *'} from incompatible pointer type 'MYSQL_BOOL *' {aka '_Bool *'} [-Wincompatible-pointer-types]
   results[0].is_null = &rs->is_null;
                      ^
my_result_helper.c: In function 'pre_extract_uint16':
my_result_helper.c:658:22: warning: assignment to 'my_bool *' {aka 'char *'} from incompatible pointer type 'MYSQL_BOOL *' {aka '_Bool *'} [-Wincompatible-pointer-types]
   results[0].is_null = &rs->is_null;
                      ^
my_result_helper.c: In function 'pre_extract_uint32':
my_result_helper.c:738:22: warning: assignment to 'my_bool *' {aka 'char *'} from incompatible pointer type 'MYSQL_BOOL *' {aka '_Bool *'} [-Wincompatible-pointer-types]
   results[0].is_null = &rs->is_null;
                      ^
my_result_helper.c: In function 'pre_extract_uint64':
my_result_helper.c:820:22: warning: assignment to 'my_bool *' {aka 'char *'} from incompatible pointer type 'MYSQL_BOOL *' {aka '_Bool *'} [-Wincompatible-pointer-types]
   results[0].is_null = &rs->is_null;
                      ^
  CCLD     libgnunetmy.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/my'
Making all in pq
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/pq'
  CC       pq.lo
  CC       pq_connect.lo
  CC       pq_eval.lo
  CC       pq_exec.lo
  CC       pq_prepare.lo
  CC       pq_query_helper.lo
  CC       pq_result_helper.lo
  CCLD     libgnunetpq.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/pq'
Making all in datacache
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/datacache'
  CC       datacache.lo
  CC       plugin_datacache_template.lo
  CC       plugin_datacache_sqlite.lo
  CC       libgnunet_plugin_datacache_postgres_la-plugin_datacache_postgres.lo
  CC       plugin_datacache_heap.lo
  CCLD     libgnunetdatacache.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_datacache_template.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CCLD     libgnunet_plugin_datacache_sqlite.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_datacache_postgres.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_datacache_heap.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/datacache'
Making all in datastore
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/datastore'
  CC       datastore_api.lo
  CC       plugin_datastore_template.lo
  CC       plugin_datastore_sqlite.lo
  CC       libgnunet_plugin_datastore_mysql_la-plugin_datastore_mysql.lo
  CC       libgnunet_plugin_datastore_postgres_la-plugin_datastore_postgres.lo
  CC       plugin_datastore_heap.lo
  CC       gnunet-datastore.o
  CC       gnunet-service-datastore.o
  CCLD     libgnunetdatastore.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_datastore_template.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CCLD     libgnunet_plugin_datastore_sqlite.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_datastore_mysql.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_datastore_postgres.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_datastore_heap.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-datastore
  CCLD     gnunet-service-datastore
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/datastore'
Making all in template
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/template'
  CC       gnunet-template.o
  CC       gnunet-service-template.o
  CCLD     gnunet-template
  CCLD     gnunet-service-template
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/template'
Making all in peerstore
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/peerstore'
  CC       peerstore_api.lo
  CC       peerstore_common.lo
  CC       plugin_peerstore_sqlite.lo
  CC       plugin_peerstore_flat.lo
  CC       gnunet-peerstore.o
  CC       gnunet_service_peerstore-gnunet-service-peerstore.o
  CC       gnunet_service_peerstore-peerstore_common.o
  CCLD     libgnunetpeerstore.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-service-peerstore
  CCLD     libgnunet_plugin_peerstore_sqlite.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_peerstore_flat.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-peerstore
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/peerstore'
Making all in ats
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/ats'
  CC       ats_api_connectivity.lo
  CC       ats_api_scheduling.lo
  CC       ats_api_scanner.lo
  CC       ats_api_performance.lo
  CC       plugin_ats_proportional.lo
  CC       gnunet-service-ats.o
  CC       gnunet-service-ats_addresses.o
  CC       gnunet-service-ats_connectivity.o
  CC       gnunet-service-ats_normalization.o
  CC       gnunet-service-ats_performance.o
  CC       gnunet-service-ats_plugins.o
  CC       gnunet-service-ats_preferences.o
  CC       gnunet-service-ats_scheduling.o
  CC       gnunet-service-ats_reservations.o
  CCLD     libgnunetats.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_ats_proportional.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-service-ats
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/ats'
Making all in nat
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/nat'
  CC       nat_api.lo
  CC       nat_api_stun.lo
  CC       gnunet-nat.o
  CC       gnunet-service-nat.o
  CC       gnunet-service-nat_externalip.o
  CC       gnunet-service-nat_stun.o
  CC       gnunet-service-nat_mini.o
  CC       gnunet-service-nat_helper.o
  CCLD     libgnunetnatnew.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-service-nat
  CCLD     gnunet-nat
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/nat'
Making all in nat-auto
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/nat-auto'
  CC       nat_auto_api.lo
  CC       nat_auto_api_test.lo
  CC       gnunet-nat-auto.o
  CC       gnunet-nat-server.o
  CC       gnunet-service-nat-auto.o
  CCLD     libgnunetnatauto.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-nat-server
  CCLD     gnunet-service-nat-auto
  CCLD     gnunet-nat-auto
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/nat-auto'
Making all in fragmentation
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/fragmentation'
  CC       fragmentation.lo
  CC       defragmentation.lo
  CCLD     libgnunetfragmentation.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/fragmentation'
Making all in transport
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/transport'
  CC       transport_api_address_to_string.lo
  CC       transport_api_blacklist.lo
  CC       transport_api_core.lo
  CC       transport_api_hello_get.lo
  CC       transport_api_manipulation.lo
  CC       transport_api_monitor_peers.lo
  CC       transport_api_monitor_plugins.lo
  CC       transport_api_offer_hello.lo
  CC       transport_api2_application.lo
  CC       transport_api2_core.lo
  CC       transport_api2_communication.lo
  CC       transport_api2_monitor.lo
  CC       transport-testing.lo
  CC       transport-testing-filenames.lo
  CC       transport-testing-loggers.lo
  CC       transport-testing-main.lo
  CC       transport-testing-send.lo
  CC       transport-testing2.lo
  CC       plugin_transport_template.lo
  CC       plugin_transport_tcp.lo
  CC       plugin_transport_unix.lo
  CC       libgnunet_plugin_transport_http_client_la-plugin_transport_http_client.lo
  CC       libgnunet_plugin_transport_http_client_la-plugin_transport_http_common.lo
  CC       libgnunet_plugin_transport_https_client_la-plugin_transport_http_client.lo
  CC       libgnunet_plugin_transport_https_client_la-plugin_transport_http_common.lo
  CC       libgnunet_plugin_transport_http_server_la-plugin_transport_http_server.lo
  CC       libgnunet_plugin_transport_http_server_la-plugin_transport_http_common.lo
  CC       libgnunet_plugin_transport_https_server_la-plugin_transport_http_server.lo
  CC       libgnunet_plugin_transport_https_server_la-plugin_transport_http_common.lo
  CC       libgnunet_plugin_transport_wlan_la-plugin_transport_wlan.lo
  CC       libgnunet_plugin_transport_bluetooth_la-plugin_transport_wlan.lo
  CC       plugin_transport_udp.lo
plugin_transport_udp.c: In function 'udp_select_send':
plugin_transport_udp.c:3134:5: warning: 'session' may be used uninitialized in this function [-Wmaybe-uninitialized]
     notify_session_monitor (session->plugin,
     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                             session,
                             ~~~~~~~~
                             GNUNET_TRANSPORT_SS_UPDATE);
                             ~~~~~~~~~~~~~~~~~~~~~~~~~~~
plugin_transport_udp.c:3071:30: note: 'session' was declared here
   struct GNUNET_ATS_Session *session;
                              ^~~~~~~
  CC       plugin_transport_udp_broadcasting.lo
  CC       gnunet-transport.o
  CC       gnunet-helper-transport-wlan.o
  CC       gnunet-helper-transport-wlan-dummy.o
  CC       gnunet-helper-transport-bluetooth.o
  CC       gnunet_service_transport-gnunet-service-transport.o
  CC       gnunet_service_transport-gnunet-service-transport_ats.o
  CC       gnunet_service_transport-gnunet-service-transport_hello.o
  CC       gnunet_service_transport-gnunet-service-transport_neighbours.o
  CC       gnunet_service_transport-gnunet-service-transport_plugins.o
  CC       gnunet_service_transport-gnunet-service-transport_validation.o
  CC       gnunet_service_transport-gnunet-service-transport_manipulation.o
  CC       gnunet-communicator-unix.o
  CC       gnunet-communicator-udp.o
  CC       gnunet-communicator-tcp.o
  CC       gnunet-transport-profiler.o
  CC       gnunet-service-tng.o
  CC       gnunet-transport-wlan-sender.o
  CC       gnunet-transport-wlan-receiver.o
  CCLD     libgnunettransport.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunettransportapplication.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunettransportcore.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunettransportcommunicator.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunettransportmonitor.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunettransporttesting.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunettransporttesting2.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_transport_template.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CCLD     libgnunet_plugin_transport_tcp.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_transport_unix.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_transport_http_client.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_transport_https_client.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_transport_http_server.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_transport_https_server.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_transport_wlan.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_transport_bluetooth.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_transport_udp.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-transport
  CCLD     gnunet-helper-transport-wlan
  CCLD     gnunet-helper-transport-wlan-dummy
  CCLD     gnunet-helper-transport-bluetooth
  CCLD     gnunet-service-transport
  CCLD     gnunet-communicator-unix
  CCLD     gnunet-communicator-udp
  CCLD     gnunet-communicator-tcp
  CCLD     gnunet-transport-profiler
  CCLD     gnunet-service-tng
  CCLD     gnunet-transport-wlan-sender
  CCLD     gnunet-transport-wlan-receiver
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/transport'
Making all in ats-tool
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/ats-tool'
  CC       gnunet-ats.o
  CCLD     gnunet-ats
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/ats-tool'
Making all in peerinfo-tool
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/peerinfo-tool'
  CC       libgnunet_plugin_rest_peerinfo_la-plugin_rest_peerinfo.lo
  CC       gnunet-peerinfo.o
  CC       gnunet-peerinfo_plugins.o
  CCLD     libgnunet_plugin_rest_peerinfo.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-peerinfo
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/peerinfo-tool'
Making all in core
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/core'
  CC       core_api.lo
  CC       core_api_monitor_peers.lo
  CC       gnunet-core.o
  CC       gnunet-service-core.o
  CC       gnunet-service-core_kx.o
  CC       gnunet-service-core_sessions.o
  CC       gnunet-service-core_typemap.o
  CCLD     libgnunetcore.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-service-core
  CCLD     gnunet-core
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/core'
Making all in testbed-logger
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/testbed-logger'
  CC       testbed_logger_api.lo
  CC       gnunet-service-testbed-logger.o
  CCLD     libgnunettestbedlogger.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-service-testbed-logger
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/testbed-logger'
Making all in testbed
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/testbed'
  CC       testbed_api.lo
  CC       testbed_api_hosts.lo
  CC       testbed_api_operations.lo
  CC       testbed_api_peers.lo
  CC       testbed_api_services.lo
  CC       testbed_api_statistics.lo
  CC       testbed_api_testbed.lo
  CC       testbed_api_test.lo
  CC       testbed_api_topology.lo
  CC       testbed_api_sd.lo
  CC       testbed_api_barriers.lo
  CC       gnunet-testbed-profiler.o
  CC       gnunet-service-testbed.o
  CC       gnunet-service-testbed_links.o
  CC       gnunet-service-testbed_peers.o
  CC       gnunet-service-testbed_cache.o
  CC       gnunet-service-testbed_oc.o
  CC       gnunet-service-testbed_cpustatus.o
  CC       gnunet-service-testbed_meminfo.o
  CC       gnunet-service-testbed_barriers.o
  CC       gnunet-service-testbed_connectionpool.o
  CC       gnunet-helper-testbed.o
  CC       gnunet-daemon-testbed-blacklist.o
  CC       gnunet-daemon-testbed-underlay.o
  CC       gnunet-daemon-latency-logger.o
  CC       generate-underlay-topology.o
  CCLD     libgnunettestbed.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-daemon-testbed-blacklist
  CCLD     gnunet-daemon-testbed-underlay
  CCLD     gnunet-daemon-latency-logger
  CCLD     generate-underlay-topology
  CCLD     gnunet-testbed-profiler
  CCLD     gnunet-service-testbed
  CCLD     gnunet-helper-testbed
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/testbed'
Making all in ats-tests
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/ats-tests'
  CC       ats-testing.lo
  CC       ats-testing-log.lo
  CC       ats-testing-traffic.lo
  CC       ats-testing-experiment.lo
  CC       ats-testing-preferences.lo
  CC       gnunet-ats-sim.o
  CC       gnunet-solver-eval.o
  CCLD     libgnunetatstesting.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-solver-eval
  CCLD     gnunet-ats-sim
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/ats-tests'
Making all in nse
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/nse'
  CC       nse_api.lo
  CC       gnunet-nse.o
  CC       gnunet-service-nse.o
  CC       gnunet-nse-profiler.o
  CCLD     libgnunetnse.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-nse
  CCLD     gnunet-service-nse
  CCLD     gnunet-nse-profiler
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/nse'
Making all in dht
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/dht'
  CC       dht_test_lib.o
  CC       dht_api.lo
  CC       plugin_block_dht.lo
  CC       gnunet-dht-monitor.o
  CC       gnunet-dht-get.o
  CC       gnunet-dht-put.o
  CC       gnunet-service-dht.o
  CC       gnunet-service-dht_datacache.o
  CC       gnunet-service-dht_hello.o
  CC       gnunet-service-dht_nse.o
  CC       gnunet-service-dht_neighbours.o
  CC       gnunet-service-dht_routing.o
  CC       gnunet_dht_profiler.o
  CCLD     libgnunetdht.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_block_dht.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-dht-monitor
  CCLD     gnunet-dht-get
  CCLD     gnunet-dht-put
  CCLD     gnunet-service-dht
  CCLD     gnunet-dht-profiler
  AR       libgnunetdhttest.a
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/dht'
Making all in hostlist
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/hostlist'
  CC       gnunet_daemon_hostlist-gnunet-daemon-hostlist.o
  CC       gnunet_daemon_hostlist-gnunet-daemon-hostlist_client.o
  CC       gnunet_daemon_hostlist-gnunet-daemon-hostlist_server.o
  CCLD     gnunet-daemon-hostlist
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/hostlist'
Making all in topology
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/topology'
  CC       friends.lo
  CC       gnunet-daemon-topology.o
  CCLD     libgnunetfriends.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-daemon-topology
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/topology'
Making all in regex
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/regex'
  CC       regex_internal.o
  CC       regex_internal_dht.o
  CC       regex_block_lib.lo
  CC       regex_test_lib.o
regex_test_lib.c:102:1: warning: 'space' defined but not used [-Wunused-function]
 space (int n)
 ^~~~~
  CC       regex_test_graph.o
  CC       regex_test_random.o
  CC       regex_api_announce.lo
  CC       regex_api_search.lo
  CC       plugin_block_regex.lo
  CC       gnunet-service-regex.o
  CC       gnunet-daemon-regexprofiler.o
  CC       gnunet-regex-simulation-profiler.o
  CC       perf-regex.o
  CC       gnunet-regex-profiler.o
  CCLD     libgnunetregexblock.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunetregex.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_block_regex.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  AR       libgnunetregex_internal.a
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  AR       libgnunetregextest.a
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CCLD     gnunet-service-regex
  CCLD     gnunet-daemon-regexprofiler
  CCLD     gnunet-regex-simulation-profiler
  CCLD     perf-regex
  CCLD     gnunet-regex-profiler
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/regex'
Making all in dns
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/dns'
  CC       dns_api.lo
  CC       plugin_block_dns.lo
  CC       gnunet-service-dns.o
  CC       gnunet-helper-dns.o
  CC       gnunet-dns-monitor.o
  CC       gnunet-dns-redirector.o
  CC       gnunet-zonewalk.o
  CCLD     libgnunetdns.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_block_dns.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-service-dns
  CCLD     gnunet-helper-dns
  CCLD     gnunet-dns-monitor
  CCLD     gnunet-dns-redirector
  CCLD     gnunet-zonewalk
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/dns'
Making all in identity
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/identity'
  CC       identity_api.lo
  CC       identity_api_lookup.lo
  CC       identity_api_suffix_lookup.lo
  CC       libgnunet_plugin_rest_identity_la-plugin_rest_identity.lo
  CC       gnunet-identity.o
  CC       gnunet-service-identity.o
  CCLD     libgnunetidentity.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-service-identity
  CCLD     libgnunet_plugin_rest_identity.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-identity
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/identity'
Making all in namecache
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/namecache'
  CC       namecache_api.lo
  CC       plugin_namecache_sqlite.lo
  CC       plugin_namecache_flat.lo
  CC       plugin_namecache_postgres.lo
  CC       gnunet-namecache.o
  CC       gnunet-service-namecache.o
  CCLD     libgnunetnamecache.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_namecache_sqlite.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_namecache_flat.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_namecache_postgres.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-namecache
  CCLD     gnunet-service-namecache
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/namecache'
Making all in namestore
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/namestore'
  CC       namestore_api.lo
  CC       namestore_api_monitor.lo
  CC       plugin_namestore_sqlite.lo
  CC       plugin_namestore_postgres.lo
  CC       plugin_namestore_flat.lo
  CC       libgnunet_plugin_rest_namestore_la-plugin_rest_namestore.lo
  CC       gnunet-namestore.o
  CC       gnunet-zoneimport.o
  CC       gnunet-service-namestore.o
  CC       gnunet_namestore_fcfsd-gnunet-namestore-fcfsd.o
  CCLD     libgnunetnamestore.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_namestore_sqlite.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_namestore_postgres.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_namestore_flat.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_rest_namestore.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-namestore
  CCLD     gnunet-zoneimport
  CCLD     gnunet-service-namestore
  CCLD     gnunet-namestore-fcfsd
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/namestore'
Making all in cadet
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/cadet'
  CC       cadet_api.lo
  CC       cadet_api_drop_message.lo
  CC       cadet_api_get_channel.lo
  CC       cadet_api_get_path.lo
  CC       cadet_api_list_peers.lo
  CC       cadet_api_list_tunnels.lo
  CC       cadet_api_helper.lo
  CC       cadet_test_lib.lo
  CC       gnunet-cadet.o
  CC       gnunet-service-cadet.o
  CC       gnunet-service-cadet_channel.o
  CC       gnunet-service-cadet_connection.o
  CC       gnunet-service-cadet_core.o
  CC       gnunet-service-cadet_dht.o
  CC       gnunet-service-cadet_hello.o
  CC       gnunet-service-cadet_tunnels.o
  CC       gnunet-service-cadet_paths.o
  CC       gnunet-service-cadet_peer.o
  CCLD     libgnunetcadet.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-service-cadet
  CCLD     libgnunetcadettest.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CCLD     gnunet-cadet
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/cadet'
Making all in set
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/set'
  CC       set_api.lo
  CC       plugin_block_set_test.lo
  CC       gnunet-set-profiler.o
  CC       gnunet-service-set.o
  CC       gnunet-service-set_union.o
  CC       gnunet-service-set_intersection.o
  CC       ibf.o
  CC       gnunet-service-set_union_strata_estimator.o
  CC       gnunet-set-ibf-profiler.o
  CCLD     libgnunetset.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_block_set_test.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-set-profiler
  CCLD     gnunet-service-set
  CCLD     gnunet-set-ibf-profiler
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/set'
Making all in seti
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/seti'
  CC       seti_api.lo
  CC       plugin_block_seti_test.lo
  CC       gnunet-seti-profiler.o
  CC       gnunet-service-seti.o
  CCLD     libgnunetseti.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_block_seti_test.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-seti-profiler
  CCLD     gnunet-service-seti
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/seti'
Making all in setu
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/setu'
  CC       setu_api.lo
  CC       plugin_block_setu_test.lo
  CC       gnunet-setu-profiler.o
  CC       gnunet-service-setu.o
  CC       ibf.o
  CC       gnunet-service-setu_strata_estimator.o
  CC       gnunet-setu-ibf-profiler.o
  CCLD     libgnunetsetu.la
  CCLD     libgnunet_plugin_block_setu_test.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-setu-ibf-profiler
  CCLD     gnunet-setu-profiler
  CCLD     gnunet-service-setu
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/setu'
Making all in consensus
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/consensus'
  CC       consensus_api.lo
  CC       plugin_block_consensus.lo
  CC       gnunet-consensus-profiler.o
  CC       gnunet-service-consensus.o
  CC       gnunet_service_evil_consensus-gnunet-service-consensus.o
  CCLD     libgnunetconsensus.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_block_consensus.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-consensus-profiler
  CCLD     gnunet-service-consensus
  CCLD     gnunet-service-evil-consensus
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/consensus'
Making all in scalarproduct
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/scalarproduct'
  CC       scalarproduct_api.lo
  CC       gnunet-scalarproduct.o
  CC       gnunet-service-scalarproduct_alice.o
  CC       gnunet-service-scalarproduct_bob.o
  CC       gnunet-service-scalarproduct-ecc_alice.o
  CC       gnunet-service-scalarproduct-ecc_bob.o
  CCLD     libgnunetscalarproduct.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-service-scalarproduct-alice
  CCLD     gnunet-service-scalarproduct-bob
  CCLD     gnunet-service-scalarproduct-ecc-alice
  CCLD     gnunet-service-scalarproduct-ecc-bob
  CCLD     gnunet-scalarproduct
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/scalarproduct'
Making all in revocation
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/revocation'
  CC       revocation_api.lo
  CC       plugin_block_revocation.lo
  CC       gnunet-revocation.o
  CC       gnunet-revocation-tvg.o
  CC       gnunet-service-revocation.o
  CCLD     libgnunetrevocation.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_block_revocation.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-revocation
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-revocation-tvg
  CCLD     gnunet-service-revocation
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/revocation'
Making all in vpn
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/vpn'
  CC       vpn_api.lo
  CC       gnunet-vpn.o
  CC       gnunet-helper-vpn.o
  CC       gnunet_service_vpn-gnunet-service-vpn.o
cc1: note: someone does not honour COPTS correctly, passed 2 times
  CCLD     libgnunetvpn.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-helper-vpn
  CCLD     gnunet-service-vpn
  CCLD     gnunet-vpn
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/vpn'
Making all in gns
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/gns'
Making all in .
make[8]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/gns'
  CC       gns_api.lo
  CC       gns_tld_api.lo
  CC       plugin_block_gns.lo
  CC       plugin_gnsrecord_gns.lo
  CC       libgnunet_plugin_rest_gns_la-plugin_rest_gns.lo
  CC       gnunet-gns.o
  CC       gnunet_bcd-gnunet-bcd.o
  CC       gnunet-service-gns.o
  CC       gnunet-service-gns_resolver.o
  CC       gnunet-service-gns_interceptor.o
  CC       gnunet-dns2gns.o
  CC       gnunet_gns_proxy-gnunet-gns-proxy.o
  CC       gnunet-gns-benchmark.o
  CCLD     libgnunetgns.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_block_gns.la
  CCLD     libgnunet_plugin_gnsrecord_gns.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_rest_gns.la
  CCLD     gnunet-gns
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-bcd
  CCLD     gnunet-service-gns
  CCLD     gnunet-dns2gns
  CCLD     gnunet-gns-proxy
  CCLD     gnunet-gns-benchmark
make[8]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/gns'
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/gns'
Making all in zonemaster
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/zonemaster'
  CC       gnunet-service-zonemaster.o
  CC       gnunet-service-zonemaster-monitor.o
  CCLD     gnunet-service-zonemaster
  CCLD     gnunet-service-zonemaster-monitor
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/zonemaster'
Making all in conversation
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/conversation'
Making all in .
make[8]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/conversation'
  CC       microphone.lo
  CC       speaker.lo
  CC       conversation_api.lo
  CC       conversation_api_call.lo
  CC       plugin_gnsrecord_conversation.lo
  CC       gnunet-conversation-test.o
  CC       gnunet-conversation.o
  CC       gnunet-service-conversation.o
  CC       gnunet_helper_audio_record-gnunet-helper-audio-record.o
  CC       gnunet_helper_audio_playback-gnunet-helper-audio-playback.o
  CCLD     libgnunetmicrophone.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunetspeaker.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunetconversation.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_gnsrecord_conversation.la
  CCLD     gnunet-conversation-test
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-conversation
  CCLD     gnunet-service-conversation
  CCLD     gnunet-helper-audio-record
  CCLD     gnunet-helper-audio-playback
make[8]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/conversation'
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/conversation'
Making all in fs
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/fs'
  CC       fs_test_lib.o
  CC       fs_api.lo
  CC       fs_directory.lo
  CC       fs_dirmetascan.lo
  CC       fs_download.lo
  CC       fs_file_information.lo
  CC       fs_getopt.lo
  CC       fs_list_indexed.lo
  CC       fs_publish.lo
  CC       fs_publish_ksk.lo
  CC       fs_publish_ublock.lo
  CC       fs_misc.lo
  CC       fs_namespace.lo
  CC       fs_search.lo
  CC       fs_sharetree.lo
  CC       fs_tree.lo
  CC       fs_unindex.lo
  CC       fs_uri.lo
  CC       plugin_block_fs.lo
  CC       gnunet-auto-share.o
  CC       gnunet-directory.o
  CC       gnunet-download.o
  CC       gnunet-publish.o
  CC       gnunet-search.o
  CC       gnunet-fs.o
  CC       gnunet-unindex.o
  CC       gnunet-helper-fs-publish.o
  CC       gnunet-service-fs.o
  CC       gnunet-service-fs_cp.o
  CC       gnunet-service-fs_indexing.o
  CC       gnunet-service-fs_pe.o
  CC       gnunet-service-fs_pr.o
  CC       gnunet-service-fs_push.o
  CC       gnunet-service-fs_put.o
  CC       gnunet-service-fs_cadet_client.o
  CC       gnunet-service-fs_cadet_server.o
  CC       gnunet-fs-profiler.o
  CC       gnunet-daemon-fsprofiler.o
  AR       libgnunetfstest.a
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
  CCLD     libgnunetfs.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-auto-share
  CCLD     gnunet-helper-fs-publish
  CCLD     gnunet-service-fs
  CCLD     gnunet-fs-profiler
  CCLD     gnunet-daemon-fsprofiler
  CCLD     libgnunet_plugin_block_fs.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-directory
  CCLD     gnunet-download
  CCLD     gnunet-publish
  CCLD     gnunet-search
  CCLD     gnunet-fs
  CCLD     gnunet-unindex
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/fs'
Making all in exit
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/exit'
  CC       gnunet-daemon-exit.o
  CC       gnunet-helper-exit.o
  CCLD     gnunet-daemon-exit
  CCLD     gnunet-helper-exit
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/exit'
Making all in pt
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/pt'
  CC       gnunet-daemon-pt.o
  CCLD     gnunet-daemon-pt
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/pt'
Making all in secretsharing
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/secretsharing'
  CC       secretsharing_api.lo
  CC       secretsharing_common.lo
  CC       gnunet-secretsharing-profiler.o
  CC       gnunet_service_secretsharing-gnunet-service-secretsharing.o
  CC       gnunet_service_secretsharing-secretsharing_common.o
  CCLD     libgnunetsecretsharing.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-service-secretsharing
  CCLD     gnunet-secretsharing-profiler
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/secretsharing'
Making all in reclaim
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/reclaim'
  CC       reclaim_api.lo
  CC       reclaim_attribute.lo
  CC       reclaim_credential.lo
  CC       plugin_gnsrecord_reclaim.lo
  CC       plugin_reclaim_attribute_basic.lo
  CC       plugin_reclaim_credential_jwt.lo
  CC       libgnunet_plugin_rest_openid_connect_la-plugin_rest_openid_connect.lo
  CC       libgnunet_plugin_rest_openid_connect_la-oidc_helper.lo
  CC       libgnunet_plugin_rest_reclaim_la-plugin_rest_reclaim.lo
  CC       libgnunet_plugin_rest_reclaim_la-json_reclaim.lo
  CC       gnunet-reclaim.o
  CC       gnunet-service-reclaim.o
  CC       gnunet-service-reclaim_tickets.o
  CCLD     libgnunetreclaim.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_gnsrecord_reclaim.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_reclaim_attribute_basic.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_reclaim_credential_jwt.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_rest_openid_connect.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_rest_reclaim.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-reclaim
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-service-reclaim
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/reclaim'
Making all in rps
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/rps'
  CC       libgnunetrps_la-gnunet-service-rps_sampler_elem.lo
  CC       libgnunetrps_la-rps-test_util.lo
  CC       libgnunetrps_la-rps-sampler_common.lo
  CC       libgnunetrps_la-rps-sampler_client.lo
rps-sampler_client.c:277:1: warning: 'prob_observed_n_peers' defined but not used [-Wunused-function]
 prob_observed_n_peers (uint32_t num_peers_estim,
 ^~~~~~~~~~~~~~~~~~~~~
rps-sampler_client.c: In function 'sampler_mod_get_rand_peer':
rps-sampler_client.c:433:3: warning: 'prob_observed_n' may be used uninitialized in this function [-Wmaybe-uninitialized]
   gpc->cont (gpc->cont_cls, gpc->id, prob_observed_n, num_observed);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  CC       libgnunetrps_la-rps_api.lo
  CC       gnunet-rps.o
  CC       gnunet-service-rps_sampler_elem.o
  CC       rps-sampler_common.o
  CC       gnunet-service-rps_sampler.o
  CC       gnunet-service-rps_custommap.o
  CC       gnunet-service-rps_view.o
  CC       gnunet-service-rps.o
gnunet-service-rps.c: In function 'write_histogram_to_file':
gnunet-service-rps.c:3001:44: warning: passing argument 1 of 'store_prefix_file_name' makes integer from pointer without a cast [-Wint-conversion]
   file_name_full = store_prefix_file_name (&own_identity,
                                            ^~~~~~~~~~~~~
In file included from gnunet-service-rps.c:35:
rps-test_util.h:111:1: note: expected 'unsigned int' but argument is of type 'struct GNUNET_PeerIdentity *'
 store_prefix_file_name (const unsigned int index,
 ^~~~~~~~~~~~~~~~~~~~~~
gnunet-service-rps.c: At top level:
gnunet-service-rps.c:600:1: warning: 'do_mal_round' declared 'static' but never defined [-Wunused-function]
 do_mal_round (void *cls);
 ^~~~~~~~~~~~
gnunet-service-rps.c:2475:1: warning: 'add_peer_array_to_set' defined but not used [-Wunused-function]
 add_peer_array_to_set (const struct GNUNET_PeerIdentity *peer_array,
 ^~~~~~~~~~~~~~~~~~~~~
  CC       rps-test_util.o
  CC       gnunet-rps-profiler.o
gnunet-rps-profiler.c: In function 'mal_cb':
gnunet-rps-profiler.c:1686:12: warning: unused variable 'num_mal_peers' [-Wunused-variable]
   uint32_t num_mal_peers;
            ^~~~~~~~~~~~~
gnunet-rps-profiler.c: In function 'profiler_reply_handle_info':
gnunet-rps-profiler.c:2083:16: warning: unused variable 'i' [-Wunused-variable]
   unsigned int i;
                ^
gnunet-rps-profiler.c: In function 'post_profiler':
gnunet-rps-profiler.c:2904:41: warning: passing argument 1 of 'store_prefix_file_name' makes integer from pointer without a cast [-Wint-conversion]
         store_prefix_file_name (rps_peer->peer_id, "stats");
                                 ~~~~~~~~^~~~~~~~~
In file included from gnunet-rps-profiler.c:33:
rps-test_util.h:111:1: note: expected 'unsigned int' but argument is of type 'struct GNUNET_PeerIdentity *'
 store_prefix_file_name (const unsigned int index,
 ^~~~~~~~~~~~~~~~~~~~~~
At top level:
gnunet-rps-profiler.c:1729:1: warning: 'churn_test_cb' defined but not used [-Wunused-function]
 churn_test_cb (struct RPSPeer *rps_peer)
 ^~~~~~~~~~~~~
gnunet-rps-profiler.c:1684:1: warning: 'mal_cb' defined but not used [-Wunused-function]
 mal_cb (struct RPSPeer *rps_peer)
 ^~~~~~
gnunet-rps-profiler.c:1658:1: warning: 'mal_pre' defined but not used [-Wunused-function]
 mal_pre (struct RPSPeer *rps_peer, struct GNUNET_RPS_Handle *h)
 ^~~~~~~
gnunet-rps-profiler.c:1642:1: warning: 'mal_init_peer' defined but not used [-Wunused-function]
 mal_init_peer (struct RPSPeer *rps_peer)
 ^~~~~~~~~~~~~
gnunet-rps-profiler.c:1235:1: warning: 'seed_peers' defined but not used [-Wunused-function]
 seed_peers (void *cls)
 ^~~~~~~~~~
  CCLD     libgnunetrps.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-rps
  CCLD     gnunet-service-rps
  CCLD     gnunet-rps-profiler
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/rps'
Making all in abd
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/abd'
  CC       abd_api.lo
  CC       abd_serialization.lo
  CC       delegate_misc.lo
  CC       plugin_gnsrecord_abd.lo
  CC       gnunet-abd.o
  CC       gnunet-service-abd.o
  CCLD     libgnunetabd.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     libgnunet_plugin_gnsrecord_abd.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
  CCLD     gnunet-abd
  CCLD     gnunet-service-abd
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/abd'
Making all in abe
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/abe'
  CC       abe.lo
  CCLD     libgnunetabe.la
OpenWrt-libtool: link: warning: `/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/libatomic.la' seems to be moved
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/abe'
Making all in auction
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/auction'
  CC       gnunet-auction-create.o
  CC       gnunet-auction-info.o
  CC       gnunet-auction-join.o
  CC       gnunet-service-auction.o
gnunet-service-auction.c: In function 'handle_create':
gnunet-service-auction.c:59:12: warning: variable 'size' set but not used [-Wunused-but-set-variable]
   uint16_t size;
            ^~~~
  CCLD     gnunet-auction-create
  CCLD     gnunet-auction-info
  CCLD     gnunet-auction-join
  CCLD     gnunet-service-auction
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/auction'
Making all in integration-tests
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/integration-tests'
make[7]: Nothing to be done for 'all'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src/integration-tests'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src'
make[7]: Nothing to be done for 'all-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/src'
Making all in po
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/po'
*** error: gettext infrastructure mismatch: using a Makefile.in.in from gettext version 0.18 but the autoconf macros are from gettext version 0.20
make[6]: *** [Makefile:674: check-macro-version] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/po'
make[5]: *** [Makefile:627: all-recursive] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3'
make[4]: *** [Makefile:517: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3'
make[3]: *** [Makefile:404: /openwrt/build_dir/target-x86_64_musl/gnunet-0.13.3/.built] Error 2
```
