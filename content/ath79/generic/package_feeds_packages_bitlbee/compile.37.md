---
title: "compile.37"
date: 2021-06-20 22:36:26.376932
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
make package/feeds/packages/bitlbee/compile -j$(nproc) || make package/feeds/packages/bitlbee/compile V=s
```

#### Compile.txt

``` bash
BitlBee configure

No detection code exists for OpenSSL. Make sure that you have a complete
installation of OpenSSL (including devel/header files) before reporting
compilation problems.

Also, keep in mind that the OpenSSL is, according to some people, not
completely GPL-compatible. Using GnuTLS is recommended and better supported
by us. However, on many BSD machines, OpenSSL can be considered part of the
operating system, which makes it GPL-compatible.

For more info, see: http://www.openssl.org/support/faq.html#LEGAL2
                    http://www.gnome.org/~markmc/openssl-and-the-gpl.html

Please note that distributing a BitlBee binary which links to OpenSSL is
probably illegal. If you want to create and distribute a binary BitlBee
package, you really should use GnuTLS instead.

Also, the OpenSSL license requires us to say this:
 *    "This product includes software developed by the OpenSSL Project
 *    for use in the OpenSSL Toolkit. (http://www.openssl.org/)"
Insufficient resolv routines. Jabber server must be set explicitly
Architecture: Linux
Cross-compiling for: mips-openwrt-linux

Configuration done:
  Debugging disabled.
  AddressSanitizer (ASAN) disabled.
  Building PIE executable
  Binary stripping disabled.
  Off-the-Record (OTR) Messaging disabled.
  systemd disabled.
  Using event handler: glib
  Using SSL library: openssl
  Building with these protocols: jabber twitter
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/bitlbee-3.6'
* Compiling bitlbee.c
* Compiling dcc.c
* Compiling help.c
* Compiling ipc.c
* Compiling irc.c
* Compiling irc_im.c
* Compiling irc_cap.c
* Compiling irc_channel.c
* Compiling irc_commands.c
* Compiling irc_send.c
* Compiling irc_user.c
* Compiling irc_util.c
* Compiling nick.c
* Compiling query.c
* Compiling root_commands.c
* Compiling set.c
* Compiling storage.c
* Compiling storage_xml.c
* Compiling auth.c
* Compiling unix.c
* Compiling conf.c
* Compiling log.c
make -C lib 
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/bitlbee-3.6/lib'
* Compiling arc.c
* Compiling base64.c
* Compiling canohost.c
* Compiling events_glib.c
events_glib.c: In function 'b_main_init':
events_glib.c:53:13: warning: Deprecated pre-processor symbol, replace with 
   loop = g_main_new(FALSE);
             ^~~~~~~~~~~~~~~                                 
events_glib.c: In function 'b_main_run':
events_glib.c:59:13: warning: Deprecated pre-processor symbol, replace with 
  g_main_run(loop);
             ^~~~~~                                          
events_glib.c: In function 'b_main_quit':
events_glib.c:64:13: warning: Deprecated pre-processor symbol, replace with 
  g_main_quit(loop);
             ^~~~~~~                                         
* Compiling ftutil.c
* Compiling http_client.c
http_client.c: In function 'http_process_chunked_data':
http_client.c:374:3: warning: 'g_memdup' is deprecated: Use 'g_memdup2' instead [-Wdeprecated-declarations]
   s = g_memdup(chunk, req->cblen + 1);
   ^
In file included from ../../../../staging_dir/target-mips_24kc_musl/usr/include/glib-2.0/glib.h:82,
                 from http_client.h:35,
                 from http_client.c:29:
../../../../staging_dir/target-mips_24kc_musl/usr/include/glib-2.0/glib/gstrfuncs.h:257:23: note: declared here
 gpointer              g_memdup         (gconstpointer mem,
                       ^~~~~~~~
http_client.c: In function 'http_handle_headers':
http_client.c:464:2: warning: 'g_memdup' is deprecated: Use 'g_memdup2' instead [-Wdeprecated-declarations]
  req->sbuf = req->reply_body = g_memdup(req->reply_body, req->body_size + 1);
  ^~~
In file included from ../../../../staging_dir/target-mips_24kc_musl/usr/include/glib-2.0/glib.h:82,
                 from http_client.h:35,
                 from http_client.c:29:
../../../../staging_dir/target-mips_24kc_musl/usr/include/glib-2.0/glib/gstrfuncs.h:257:23: note: declared here
 gpointer              g_memdup         (gconstpointer mem,
                       ^~~~~~~~
http_client.c: In function 'http_flush_bytes':
http_client.c:682:3: warning: 'g_memdup' is deprecated: Use 'g_memdup2' instead [-Wdeprecated-declarations]
   char *new = g_memdup(req->reply_body, req->body_size + 1);
   ^~~~
In file included from ../../../../staging_dir/target-mips_24kc_musl/usr/include/glib-2.0/glib.h:82,
                 from http_client.h:35,
                 from http_client.c:29:
../../../../staging_dir/target-mips_24kc_musl/usr/include/glib-2.0/glib/gstrfuncs.h:257:23: note: declared here
 gpointer              g_memdup         (gconstpointer mem,
                       ^~~~~~~~
* Compiling ini.c
* Compiling json.c
* Compiling json_util.c
json_util.c: In function 'json_o_strdup':
json_util.c:63:3: warning: 'g_memdup' is deprecated: Use 'g_memdup2' instead [-Wdeprecated-declarations]
   return g_memdup(ret->u.string.ptr, ret->u.string.length + 1);
   ^~~~~~
In file included from ../../../../staging_dir/target-mips_24kc_musl/usr/include/glib-2.0/glib.h:82,
                 from json_util.c:26:
../../../../staging_dir/target-mips_24kc_musl/usr/include/glib-2.0/glib/gstrfuncs.h:257:23: note: declared here
 gpointer              g_memdup         (gconstpointer mem,
                       ^~~~~~~~
* Compiling md5.c
* Compiling misc.c
* Compiling oauth.c
* Compiling oauth2.c
* Compiling proxy.c
* Compiling sha1.c
* Compiling ssl_openssl.c
ssl_openssl.c:26:10: fatal error: openssl/crypto.h: No such file or directory
 #include <openssl/crypto.h>
          ^~~~~~~~~~~~~~~~~~
compilation terminated.
make[5]: *** [Makefile:44: ssl_openssl.o] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/bitlbee-3.6/lib'
make[4]: *** [Makefile:153: lib] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/bitlbee-3.6'
make[3]: *** [Makefile:72: /openwrt/build_dir/target-mips_24kc_musl/bitlbee-3.6/.built] Error 2
```
