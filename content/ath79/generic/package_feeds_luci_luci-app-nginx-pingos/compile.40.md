---
title: "compile.40"
date: 2021-06-22 10:45:15.506507
hidden: false
draft: false
weight: -40
---

build number: `40`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/luci/luci-app-nginx-pingos/compile -j$(nproc) || make package/feeds/luci/luci-app-nginx-pingos/compile V=s
```

#### Compile.txt

``` bash
nginx-1.19.6/
nginx-1.19.6/auto/
nginx-1.19.6/conf/
nginx-1.19.6/contrib/
nginx-1.19.6/src/
nginx-1.19.6/configure
nginx-1.19.6/LICENSE
nginx-1.19.6/README
nginx-1.19.6/html/
nginx-1.19.6/man/
nginx-1.19.6/CHANGES.ru
nginx-1.19.6/CHANGES
nginx-1.19.6/man/nginx.8
nginx-1.19.6/html/50x.html
nginx-1.19.6/html/index.html
nginx-1.19.6/src/core/
nginx-1.19.6/src/event/
nginx-1.19.6/src/http/
nginx-1.19.6/src/mail/
nginx-1.19.6/src/misc/
nginx-1.19.6/src/os/
nginx-1.19.6/src/stream/
nginx-1.19.6/src/stream/ngx_stream.c
nginx-1.19.6/src/stream/ngx_stream.h
nginx-1.19.6/src/stream/ngx_stream_access_module.c
nginx-1.19.6/src/stream/ngx_stream_core_module.c
nginx-1.19.6/src/stream/ngx_stream_geo_module.c
nginx-1.19.6/src/stream/ngx_stream_geoip_module.c
nginx-1.19.6/src/stream/ngx_stream_handler.c
nginx-1.19.6/src/stream/ngx_stream_limit_conn_module.c
nginx-1.19.6/src/stream/ngx_stream_log_module.c
nginx-1.19.6/src/stream/ngx_stream_map_module.c
nginx-1.19.6/src/stream/ngx_stream_proxy_module.c
nginx-1.19.6/src/stream/ngx_stream_realip_module.c
nginx-1.19.6/src/stream/ngx_stream_return_module.c
nginx-1.19.6/src/stream/ngx_stream_script.c
nginx-1.19.6/src/stream/ngx_stream_script.h
nginx-1.19.6/src/stream/ngx_stream_set_module.c
nginx-1.19.6/src/stream/ngx_stream_split_clients_module.c
nginx-1.19.6/src/stream/ngx_stream_ssl_module.c
nginx-1.19.6/src/stream/ngx_stream_ssl_module.h
nginx-1.19.6/src/stream/ngx_stream_ssl_preread_module.c
nginx-1.19.6/src/stream/ngx_stream_upstream.c
nginx-1.19.6/src/stream/ngx_stream_upstream.h
nginx-1.19.6/src/stream/ngx_stream_upstream_hash_module.c
nginx-1.19.6/src/stream/ngx_stream_upstream_least_conn_module.c
nginx-1.19.6/src/stream/ngx_stream_upstream_random_module.c
nginx-1.19.6/src/stream/ngx_stream_upstream_round_robin.c
nginx-1.19.6/src/stream/ngx_stream_upstream_round_robin.h
nginx-1.19.6/src/stream/ngx_stream_upstream_zone_module.c
nginx-1.19.6/src/stream/ngx_stream_variables.c
nginx-1.19.6/src/stream/ngx_stream_variables.h
nginx-1.19.6/src/stream/ngx_stream_write_filter_module.c
nginx-1.19.6/src/os/unix/
nginx-1.19.6/src/os/unix/ngx_alloc.c
nginx-1.19.6/src/os/unix/ngx_alloc.h
nginx-1.19.6/src/os/unix/ngx_atomic.h
nginx-1.19.6/src/os/unix/ngx_channel.c
nginx-1.19.6/src/os/unix/ngx_channel.h
nginx-1.19.6/src/os/unix/ngx_daemon.c
nginx-1.19.6/src/os/unix/ngx_darwin.h
nginx-1.19.6/src/os/unix/ngx_darwin_config.h
nginx-1.19.6/src/os/unix/ngx_darwin_init.c
nginx-1.19.6/src/os/unix/ngx_darwin_sendfile_chain.c
nginx-1.19.6/src/os/unix/ngx_dlopen.c
nginx-1.19.6/src/os/unix/ngx_dlopen.h
nginx-1.19.6/src/os/unix/ngx_errno.c
nginx-1.19.6/src/os/unix/ngx_errno.h
nginx-1.19.6/src/os/unix/ngx_file_aio_read.c
nginx-1.19.6/src/os/unix/ngx_files.c
nginx-1.19.6/src/os/unix/ngx_files.h
nginx-1.19.6/src/os/unix/ngx_freebsd.h
nginx-1.19.6/src/os/unix/ngx_freebsd_config.h
nginx-1.19.6/src/os/unix/ngx_linux.h
nginx-1.19.6/src/os/unix/ngx_freebsd_init.c
nginx-1.19.6/src/os/unix/ngx_freebsd_sendfile_chain.c
nginx-1.19.6/src/os/unix/ngx_gcc_atomic_amd64.h
nginx-1.19.6/src/os/unix/ngx_gcc_atomic_ppc.h
nginx-1.19.6/src/os/unix/ngx_gcc_atomic_sparc64.h
nginx-1.19.6/src/os/unix/ngx_gcc_atomic_x86.h
nginx-1.19.6/src/os/unix/ngx_linux_aio_read.c
nginx-1.19.6/src/os/unix/ngx_linux_config.h
nginx-1.19.6/src/os/unix/ngx_linux_init.c
nginx-1.19.6/src/os/unix/ngx_linux_sendfile_chain.c
nginx-1.19.6/src/os/unix/ngx_os.h
nginx-1.19.6/src/os/unix/ngx_posix_config.h
nginx-1.19.6/src/os/unix/ngx_posix_init.c
nginx-1.19.6/src/os/unix/ngx_process.c
nginx-1.19.6/src/os/unix/ngx_process.h
nginx-1.19.6/src/os/unix/ngx_process_cycle.c
nginx-1.19.6/src/os/unix/ngx_process_cycle.h
nginx-1.19.6/src/os/unix/ngx_readv_chain.c
nginx-1.19.6/src/os/unix/ngx_recv.c
nginx-1.19.6/src/os/unix/ngx_send.c
nginx-1.19.6/src/os/unix/ngx_setaffinity.c
nginx-1.19.6/src/os/unix/ngx_setaffinity.h
nginx-1.19.6/src/os/unix/ngx_setproctitle.c
nginx-1.19.6/src/os/unix/ngx_setproctitle.h
nginx-1.19.6/src/os/unix/ngx_shmem.c
nginx-1.19.6/src/os/unix/ngx_shmem.h
nginx-1.19.6/src/os/unix/ngx_socket.c
nginx-1.19.6/src/os/unix/ngx_socket.h
nginx-1.19.6/src/os/unix/ngx_solaris.h
nginx-1.19.6/src/os/unix/ngx_solaris_config.h
nginx-1.19.6/src/os/unix/ngx_solaris_init.c
nginx-1.19.6/src/os/unix/ngx_solaris_sendfilev_chain.c
nginx-1.19.6/src/os/unix/ngx_sunpro_amd64.il
nginx-1.19.6/src/os/unix/ngx_sunpro_atomic_sparc64.h
nginx-1.19.6/src/os/unix/ngx_sunpro_sparc64.il
nginx-1.19.6/src/os/unix/ngx_thread.h
nginx-1.19.6/src/os/unix/ngx_sunpro_x86.il
nginx-1.19.6/src/os/unix/ngx_thread_cond.c
nginx-1.19.6/src/os/unix/ngx_thread_id.c
nginx-1.19.6/src/os/unix/ngx_thread_mutex.c
nginx-1.19.6/src/os/unix/ngx_time.c
nginx-1.19.6/src/os/unix/ngx_time.h
nginx-1.19.6/src/os/unix/ngx_udp_recv.c
nginx-1.19.6/src/os/unix/ngx_udp_send.c
nginx-1.19.6/src/os/unix/ngx_udp_sendmsg_chain.c
nginx-1.19.6/src/os/unix/ngx_user.c
nginx-1.19.6/src/os/unix/ngx_user.h
nginx-1.19.6/src/os/unix/ngx_writev_chain.c
nginx-1.19.6/src/misc/ngx_cpp_test_module.cpp
nginx-1.19.6/src/misc/ngx_google_perftools_module.c
nginx-1.19.6/src/mail/ngx_mail.c
nginx-1.19.6/src/mail/ngx_mail.h
nginx-1.19.6/src/mail/ngx_mail_auth_http_module.c
nginx-1.19.6/src/mail/ngx_mail_core_module.c
nginx-1.19.6/src/mail/ngx_mail_handler.c
nginx-1.19.6/src/mail/ngx_mail_imap_handler.c
nginx-1.19.6/src/mail/ngx_mail_imap_module.c
nginx-1.19.6/src/mail/ngx_mail_imap_module.h
nginx-1.19.6/src/mail/ngx_mail_parse.c
nginx-1.19.6/src/mail/ngx_mail_pop3_handler.c
nginx-1.19.6/src/mail/ngx_mail_pop3_module.c
nginx-1.19.6/src/mail/ngx_mail_pop3_module.h
nginx-1.19.6/src/mail/ngx_mail_proxy_module.c
nginx-1.19.6/src/mail/ngx_mail_smtp_handler.c
nginx-1.19.6/src/mail/ngx_mail_smtp_module.c
nginx-1.19.6/src/mail/ngx_mail_smtp_module.h
nginx-1.19.6/src/mail/ngx_mail_ssl_module.c
nginx-1.19.6/src/mail/ngx_mail_ssl_module.h
nginx-1.19.6/src/http/modules/
nginx-1.19.6/src/http/ngx_http.c
nginx-1.19.6/src/http/ngx_http.h
nginx-1.19.6/src/http/ngx_http_cache.h
nginx-1.19.6/src/http/ngx_http_config.h
nginx-1.19.6/src/http/ngx_http_copy_filter_module.c
nginx-1.19.6/src/http/ngx_http_core_module.c
nginx-1.19.6/src/http/ngx_http_core_module.h
nginx-1.19.6/src/http/ngx_http_file_cache.c
nginx-1.19.6/src/http/ngx_http_header_filter_module.c
nginx-1.19.6/src/http/ngx_http_parse.c
nginx-1.19.6/src/http/ngx_http_postpone_filter_module.c
nginx-1.19.6/src/http/ngx_http_request.c
nginx-1.19.6/src/http/ngx_http_request.h
nginx-1.19.6/src/http/ngx_http_request_body.c
nginx-1.19.6/src/http/ngx_http_script.c
nginx-1.19.6/src/http/v2/
nginx-1.19.6/src/http/ngx_http_script.h
nginx-1.19.6/src/http/ngx_http_special_response.c
nginx-1.19.6/src/http/ngx_http_upstream.c
nginx-1.19.6/src/http/ngx_http_upstream.h
nginx-1.19.6/src/http/ngx_http_upstream_round_robin.c
nginx-1.19.6/src/http/ngx_http_upstream_round_robin.h
nginx-1.19.6/src/http/ngx_http_variables.c
nginx-1.19.6/src/http/ngx_http_variables.h
nginx-1.19.6/src/http/ngx_http_write_filter_module.c
nginx-1.19.6/src/http/v2/ngx_http_v2.c
nginx-1.19.6/src/http/v2/ngx_http_v2.h
nginx-1.19.6/src/http/v2/ngx_http_v2_encode.c
nginx-1.19.6/src/http/v2/ngx_http_v2_filter_module.c
nginx-1.19.6/src/http/v2/ngx_http_v2_huff_decode.c
nginx-1.19.6/src/http/v2/ngx_http_v2_huff_encode.c
nginx-1.19.6/src/http/v2/ngx_http_v2_module.c
nginx-1.19.6/src/http/v2/ngx_http_v2_module.h
nginx-1.19.6/src/http/v2/ngx_http_v2_table.c
nginx-1.19.6/src/http/modules/ngx_http_access_module.c
nginx-1.19.6/src/http/modules/ngx_http_addition_filter_module.c
nginx-1.19.6/src/http/modules/ngx_http_auth_basic_module.c
nginx-1.19.6/src/http/modules/ngx_http_auth_request_module.c
nginx-1.19.6/src/http/modules/ngx_http_autoindex_module.c
nginx-1.19.6/src/http/modules/ngx_http_browser_module.c
nginx-1.19.6/src/http/modules/ngx_http_charset_filter_module.c
nginx-1.19.6/src/http/modules/ngx_http_chunked_filter_module.c
nginx-1.19.6/src/http/modules/ngx_http_dav_module.c
nginx-1.19.6/src/http/modules/ngx_http_degradation_module.c
nginx-1.19.6/src/http/modules/ngx_http_empty_gif_module.c
nginx-1.19.6/src/http/modules/ngx_http_fastcgi_module.c
nginx-1.19.6/src/http/modules/perl/
nginx-1.19.6/src/http/modules/ngx_http_flv_module.c
nginx-1.19.6/src/http/modules/ngx_http_geo_module.c
nginx-1.19.6/src/http/modules/ngx_http_geoip_module.c
nginx-1.19.6/src/http/modules/ngx_http_grpc_module.c
nginx-1.19.6/src/http/modules/ngx_http_gunzip_filter_module.c
nginx-1.19.6/src/http/modules/ngx_http_gzip_filter_module.c
nginx-1.19.6/src/http/modules/ngx_http_gzip_static_module.c
nginx-1.19.6/src/http/modules/ngx_http_headers_filter_module.c
nginx-1.19.6/src/http/modules/ngx_http_image_filter_module.c
nginx-1.19.6/src/http/modules/ngx_http_index_module.c
nginx-1.19.6/src/http/modules/ngx_http_limit_conn_module.c
nginx-1.19.6/src/http/modules/ngx_http_limit_req_module.c
nginx-1.19.6/src/http/modules/ngx_http_log_module.c
nginx-1.19.6/src/http/modules/ngx_http_map_module.c
nginx-1.19.6/src/http/modules/ngx_http_memcached_module.c
nginx-1.19.6/src/http/modules/ngx_http_mirror_module.c
nginx-1.19.6/src/http/modules/ngx_http_mp4_module.c
nginx-1.19.6/src/http/modules/ngx_http_not_modified_filter_module.c
nginx-1.19.6/src/http/modules/ngx_http_proxy_module.c
nginx-1.19.6/src/http/modules/ngx_http_random_index_module.c
nginx-1.19.6/src/http/modules/ngx_http_range_filter_module.c
nginx-1.19.6/src/http/modules/ngx_http_realip_module.c
nginx-1.19.6/src/http/modules/ngx_http_referer_module.c
nginx-1.19.6/src/http/modules/ngx_http_rewrite_module.c
nginx-1.19.6/src/http/modules/ngx_http_scgi_module.c
nginx-1.19.6/src/http/modules/ngx_http_secure_link_module.c
nginx-1.19.6/src/http/modules/ngx_http_slice_filter_module.c
nginx-1.19.6/src/http/modules/ngx_http_split_clients_module.c
nginx-1.19.6/src/http/modules/ngx_http_ssi_filter_module.c
nginx-1.19.6/src/http/modules/ngx_http_ssi_filter_module.h
nginx-1.19.6/src/http/modules/ngx_http_ssl_module.c
nginx-1.19.6/src/http/modules/ngx_http_ssl_module.h
nginx-1.19.6/src/http/modules/ngx_http_static_module.c
nginx-1.19.6/src/http/modules/ngx_http_stub_status_module.c
nginx-1.19.6/src/http/modules/ngx_http_sub_filter_module.c
nginx-1.19.6/src/http/modules/ngx_http_try_files_module.c
nginx-1.19.6/src/http/modules/ngx_http_upstream_hash_module.c
nginx-1.19.6/src/http/modules/ngx_http_upstream_ip_hash_module.c
nginx-1.19.6/src/http/modules/ngx_http_upstream_keepalive_module.c
nginx-1.19.6/src/http/modules/ngx_http_upstream_random_module.c
nginx-1.19.6/src/http/modules/ngx_http_upstream_least_conn_module.c
nginx-1.19.6/src/http/modules/ngx_http_upstream_zone_module.c
nginx-1.19.6/src/http/modules/ngx_http_userid_filter_module.c
nginx-1.19.6/src/http/modules/ngx_http_uwsgi_module.c
nginx-1.19.6/src/http/modules/ngx_http_xslt_filter_module.c
nginx-1.19.6/src/http/modules/perl/Makefile.PL
nginx-1.19.6/src/http/modules/perl/nginx.pm
nginx-1.19.6/src/http/modules/perl/nginx.xs
nginx-1.19.6/src/http/modules/perl/ngx_http_perl_module.c
nginx-1.19.6/src/http/modules/perl/ngx_http_perl_module.h
nginx-1.19.6/src/http/modules/perl/typemap
nginx-1.19.6/src/event/modules/
nginx-1.19.6/src/event/ngx_event.c
nginx-1.19.6/src/event/ngx_event.h
nginx-1.19.6/src/event/ngx_event_accept.c
nginx-1.19.6/src/event/ngx_event_connect.c
nginx-1.19.6/src/event/ngx_event_connect.h
nginx-1.19.6/src/event/ngx_event_openssl.c
nginx-1.19.6/src/event/ngx_event_openssl.h
nginx-1.19.6/src/event/ngx_event_openssl_stapling.c
nginx-1.19.6/src/event/ngx_event_pipe.c
nginx-1.19.6/src/event/ngx_event_pipe.h
nginx-1.19.6/src/event/ngx_event_posted.c
nginx-1.19.6/src/event/ngx_event_posted.h
nginx-1.19.6/src/event/ngx_event_timer.c
nginx-1.19.6/src/event/ngx_event_timer.h
nginx-1.19.6/src/event/ngx_event_udp.c
nginx-1.19.6/src/event/modules/ngx_devpoll_module.c
nginx-1.19.6/src/event/modules/ngx_epoll_module.c
nginx-1.19.6/src/event/modules/ngx_eventport_module.c
nginx-1.19.6/src/event/modules/ngx_kqueue_module.c
nginx-1.19.6/src/event/modules/ngx_poll_module.c
nginx-1.19.6/src/event/modules/ngx_select_module.c
nginx-1.19.6/src/event/modules/ngx_win32_poll_module.c
nginx-1.19.6/src/event/modules/ngx_win32_select_module.c
nginx-1.19.6/src/core/nginx.c
nginx-1.19.6/src/core/nginx.h
nginx-1.19.6/src/core/ngx_array.c
nginx-1.19.6/src/core/ngx_array.h
nginx-1.19.6/src/core/ngx_buf.c
nginx-1.19.6/src/core/ngx_buf.h
nginx-1.19.6/src/core/ngx_conf_file.c
nginx-1.19.6/src/core/ngx_conf_file.h
nginx-1.19.6/src/core/ngx_config.h
nginx-1.19.6/src/core/ngx_connection.c
nginx-1.19.6/src/core/ngx_connection.h
nginx-1.19.6/src/core/ngx_core.h
nginx-1.19.6/src/core/ngx_cpuinfo.c
nginx-1.19.6/src/core/ngx_crc.h
nginx-1.19.6/src/core/ngx_crc32.c
nginx-1.19.6/src/core/ngx_crc32.h
nginx-1.19.6/src/core/ngx_crypt.c
nginx-1.19.6/src/core/ngx_crypt.h
nginx-1.19.6/src/core/ngx_cycle.c
nginx-1.19.6/src/core/ngx_cycle.h
nginx-1.19.6/src/core/ngx_file.c
nginx-1.19.6/src/core/ngx_file.h
nginx-1.19.6/src/core/ngx_hash.c
nginx-1.19.6/src/core/ngx_hash.h
nginx-1.19.6/src/core/ngx_inet.c
nginx-1.19.6/src/core/ngx_inet.h
nginx-1.19.6/src/core/ngx_list.c
nginx-1.19.6/src/core/ngx_list.h
nginx-1.19.6/src/core/ngx_log.c
nginx-1.19.6/src/core/ngx_log.h
nginx-1.19.6/src/core/ngx_md5.c
nginx-1.19.6/src/core/ngx_md5.h
nginx-1.19.6/src/core/ngx_module.c
nginx-1.19.6/src/core/ngx_module.h
nginx-1.19.6/src/core/ngx_murmurhash.c
nginx-1.19.6/src/core/ngx_murmurhash.h
nginx-1.19.6/src/core/ngx_open_file_cache.c
nginx-1.19.6/src/core/ngx_open_file_cache.h
nginx-1.19.6/src/core/ngx_output_chain.c
nginx-1.19.6/src/core/ngx_palloc.c
nginx-1.19.6/src/core/ngx_palloc.h
nginx-1.19.6/src/core/ngx_parse.c
nginx-1.19.6/src/core/ngx_parse.h
nginx-1.19.6/src/core/ngx_parse_time.c
nginx-1.19.6/src/core/ngx_queue.c
nginx-1.19.6/src/core/ngx_parse_time.h
nginx-1.19.6/src/core/ngx_proxy_protocol.c
nginx-1.19.6/src/core/ngx_proxy_protocol.h
nginx-1.19.6/src/core/ngx_queue.h
nginx-1.19.6/src/core/ngx_radix_tree.c
nginx-1.19.6/src/core/ngx_radix_tree.h
nginx-1.19.6/src/core/ngx_rbtree.c
nginx-1.19.6/src/core/ngx_rbtree.h
nginx-1.19.6/src/core/ngx_regex.c
nginx-1.19.6/src/core/ngx_regex.h
nginx-1.19.6/src/core/ngx_resolver.c
nginx-1.19.6/src/core/ngx_resolver.h
nginx-1.19.6/src/core/ngx_rwlock.c
nginx-1.19.6/src/core/ngx_rwlock.h
nginx-1.19.6/src/core/ngx_sha1.c
nginx-1.19.6/src/core/ngx_sha1.h
nginx-1.19.6/src/core/ngx_shmtx.c
nginx-1.19.6/src/core/ngx_shmtx.h
nginx-1.19.6/src/core/ngx_slab.c
nginx-1.19.6/src/core/ngx_slab.h
nginx-1.19.6/src/core/ngx_spinlock.c
nginx-1.19.6/src/core/ngx_string.c
nginx-1.19.6/src/core/ngx_string.h
nginx-1.19.6/src/core/ngx_syslog.c
nginx-1.19.6/src/core/ngx_syslog.h
nginx-1.19.6/src/core/ngx_thread_pool.c
nginx-1.19.6/src/core/ngx_thread_pool.h
nginx-1.19.6/src/core/ngx_times.c
nginx-1.19.6/src/core/ngx_times.h
nginx-1.19.6/contrib/README
nginx-1.19.6/contrib/geo2nginx.pl
nginx-1.19.6/contrib/unicode2nginx/
nginx-1.19.6/contrib/vim/
nginx-1.19.6/contrib/vim/ftdetect/
nginx-1.19.6/contrib/vim/ftplugin/
nginx-1.19.6/contrib/vim/indent/
nginx-1.19.6/contrib/vim/syntax/
nginx-1.19.6/contrib/vim/syntax/nginx.vim
nginx-1.19.6/contrib/vim/indent/nginx.vim
nginx-1.19.6/contrib/vim/ftplugin/nginx.vim
nginx-1.19.6/contrib/vim/ftdetect/nginx.vim
nginx-1.19.6/contrib/unicode2nginx/koi-utf
nginx-1.19.6/contrib/unicode2nginx/unicode-to-nginx.pl
nginx-1.19.6/contrib/unicode2nginx/win-utf
nginx-1.19.6/conf/fastcgi.conf
nginx-1.19.6/conf/fastcgi_params
nginx-1.19.6/conf/koi-utf
nginx-1.19.6/conf/koi-win
nginx-1.19.6/conf/mime.types
nginx-1.19.6/conf/nginx.conf
nginx-1.19.6/conf/scgi_params
nginx-1.19.6/conf/uwsgi_params
nginx-1.19.6/conf/win-utf
nginx-1.19.6/auto/cc/
nginx-1.19.6/auto/define
nginx-1.19.6/auto/endianness
nginx-1.19.6/auto/feature
nginx-1.19.6/auto/have
nginx-1.19.6/auto/have_headers
nginx-1.19.6/auto/headers
nginx-1.19.6/auto/include
nginx-1.19.6/auto/init
nginx-1.19.6/auto/install
nginx-1.19.6/auto/lib/
nginx-1.19.6/auto/make
nginx-1.19.6/auto/module
nginx-1.19.6/auto/modules
nginx-1.19.6/auto/nohave
nginx-1.19.6/auto/options
nginx-1.19.6/auto/os/
nginx-1.19.6/auto/sources
nginx-1.19.6/auto/stubs
nginx-1.19.6/auto/summary
nginx-1.19.6/auto/threads
nginx-1.19.6/auto/types/
nginx-1.19.6/auto/unix
nginx-1.19.6/auto/types/sizeof
nginx-1.19.6/auto/types/typedef
nginx-1.19.6/auto/types/uintptr_t
nginx-1.19.6/auto/types/value
nginx-1.19.6/auto/os/conf
nginx-1.19.6/auto/os/darwin
nginx-1.19.6/auto/os/freebsd
nginx-1.19.6/auto/os/linux
nginx-1.19.6/auto/os/solaris
nginx-1.19.6/auto/os/win32
nginx-1.19.6/auto/lib/conf
nginx-1.19.6/auto/lib/geoip/
nginx-1.19.6/auto/lib/google-perftools/
nginx-1.19.6/auto/lib/libatomic/
nginx-1.19.6/auto/lib/libgd/
nginx-1.19.6/auto/lib/libxslt/
nginx-1.19.6/auto/lib/make
nginx-1.19.6/auto/lib/openssl/
nginx-1.19.6/auto/lib/pcre/
nginx-1.19.6/auto/lib/perl/
nginx-1.19.6/auto/lib/zlib/
nginx-1.19.6/auto/lib/zlib/conf
nginx-1.19.6/auto/lib/zlib/make
nginx-1.19.6/auto/lib/zlib/makefile.bcc
nginx-1.19.6/auto/lib/zlib/makefile.msvc
nginx-1.19.6/auto/lib/zlib/makefile.owc
nginx-1.19.6/auto/lib/perl/conf
nginx-1.19.6/auto/lib/perl/make
nginx-1.19.6/auto/lib/pcre/conf
nginx-1.19.6/auto/lib/pcre/make
nginx-1.19.6/auto/lib/pcre/makefile.bcc
nginx-1.19.6/auto/lib/pcre/makefile.msvc
nginx-1.19.6/auto/lib/pcre/makefile.owc
nginx-1.19.6/auto/lib/openssl/conf
nginx-1.19.6/auto/lib/openssl/make
nginx-1.19.6/auto/lib/openssl/makefile.bcc
nginx-1.19.6/auto/lib/openssl/makefile.msvc
nginx-1.19.6/auto/lib/libxslt/conf
nginx-1.19.6/auto/lib/libgd/conf
nginx-1.19.6/auto/lib/libatomic/conf
nginx-1.19.6/auto/lib/libatomic/make
nginx-1.19.6/auto/lib/google-perftools/conf
nginx-1.19.6/auto/lib/geoip/conf
nginx-1.19.6/auto/cc/acc
nginx-1.19.6/auto/cc/bcc
nginx-1.19.6/auto/cc/ccc
nginx-1.19.6/auto/cc/clang
nginx-1.19.6/auto/cc/conf
nginx-1.19.6/auto/cc/gcc
nginx-1.19.6/auto/cc/icc
nginx-1.19.6/auto/cc/msvc
nginx-1.19.6/auto/cc/name
nginx-1.19.6/auto/cc/owc
nginx-1.19.6/auto/cc/sunc

Applying ./patches/101-feature_test_fix.patch using plaintext: 
patching file auto/cc/name
patching file auto/cc/conf
patching file auto/os/linux
patching file auto/unix

Applying ./patches/102-sizeof_test_fix.patch using plaintext: 
patching file auto/types/sizeof

Applying ./patches/103-sys_nerr.patch using plaintext: 
patching file src/os/unix/ngx_errno.c

Applying ./patches/104-endianness_fix.patch using plaintext: 
patching file auto/endianness

Applying ./patches/200-config.patch using plaintext: 
patching file conf/nginx.conf

Applying ./patches/201-ignore-invalid-options.patch using plaintext: 
patching file auto/options
Hunk #1 succeeded at 400 (offset 4 lines).
./configure: error: ignoring invalid option "--target=mips-openwrt-linux"
./configure: error: ignoring invalid option "--host=mips-openwrt-linux"
./configure: error: ignoring invalid option "--program-prefix="
./configure: error: ignoring invalid option "--program-suffix="
./configure: error: ignoring invalid option "--exec-prefix=/usr"
./configure: error: ignoring invalid option "--bindir=/usr/bin"
./configure: error: ignoring invalid option "--sbindir=/usr/sbin"
./configure: error: ignoring invalid option "--libexecdir=/usr/lib"
./configure: error: ignoring invalid option "--sysconfdir=/etc"
./configure: error: ignoring invalid option "--datadir=/usr/share"
./configure: error: ignoring invalid option "--localstatedir=/var"
./configure: error: ignoring invalid option "--mandir=/usr/man"
./configure: error: ignoring invalid option "--infodir=/usr/info"
./configure: error: ignoring invalid option "--disable-nls"
building for Linux::mips
checking for C compiler ... found
 + using GNU C compiler
checking for --with-ld-opt="-L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -Wl,--gc-sections" ... found
checking for -Wl,-E switch ... found
checking for gcc builtin atomic operations ... found
checking for C99 variadic macros ... found
checking for gcc variadic macros ... found
checking for gcc builtin 64 bit byteswap ... found
checking for unistd.h ... found
checking for inttypes.h ... found
checking for limits.h ... found
checking for sys/filio.h ... not found
checking for sys/param.h ... found
checking for sys/mount.h ... found
checking for sys/statvfs.h ... found
checking for crypt.h ... found
checking for Linux::mips specific features
checking for epoll ... found
checking for EPOLLRDHUP ... found
checking for EPOLLEXCLUSIVE ... found
checking for O_PATH ... found
checking for sendfile() ... found
checking for sendfile64() ... found
checking for sys/prctl.h ... found
checking for prctl(PR_SET_DUMPABLE) ... found
checking for prctl(PR_SET_KEEPCAPS) ... found but is not working
checking for capabilities ... found
checking for crypt_r() ... found
checking for sys/vfs.h ... found
checking for nobody group ... not found
checking for nogroup group ... found
checking for poll() ... found
checking for /dev/poll ... not found
checking for kqueue ... not found
checking for crypt() ... found
checking for F_READAHEAD ... not found
checking for posix_fadvise() ... found
checking for O_DIRECT ... found
checking for F_NOCACHE ... not found
checking for directio() ... not found
checking for statfs() ... found
checking for statvfs() ... found
checking for dlopen() ... found
checking for sched_yield() ... found
checking for sched_setaffinity() ... found
checking for SO_SETFIB ... not found
checking for SO_REUSEPORT ... found
checking for SO_ACCEPTFILTER ... not found
checking for SO_BINDANY ... not found
checking for IP_TRANSPARENT ... found
checking for IP_BINDANY ... not found
checking for IP_BIND_ADDRESS_NO_PORT ... found
checking for IP_RECVDSTADDR ... not found
checking for IP_SENDSRCADDR ... not found
checking for IP_PKTINFO ... found
checking for IPV6_RECVPKTINFO ... found
checking for TCP_DEFER_ACCEPT ... found
checking for TCP_KEEPIDLE ... found
checking for TCP_FASTOPEN ... found
checking for TCP_INFO ... found
checking for accept4() ... found
checking for eventfd() ... found
checking for int size ... 4 bytes
checking for long size ... 4 bytes
checking for long long size ... 8 bytes
checking for void * size ... 4 bytes
checking for uint32_t ... found
checking for uint64_t ... found
checking for sig_atomic_t ... found
checking for sig_atomic_t size ... 4 bytes
checking for socklen_t ... found
checking for in_addr_t ... found
checking for in_port_t ... found
checking for rlim_t ... found
checking for uintptr_t ... uintptr_t found
checking for system byte ordering ... little endian
checking for size_t size ... 4 bytes
checking for off_t size ... 8 bytes
checking for time_t size ... 4 bytes
checking for AF_INET6 ... found
checking for setproctitle() ... not found
checking for pread() ... found
checking for pwrite() ... found
checking for pwritev() ... found
checking for sys_nerr ... not found
checking for _sys_nerr ... not found
checking for maximum errno ... found but is not working
checking for localtime_r() ... found
checking for clock_gettime(CLOCK_MONOTONIC) ... found
checking for posix_memalign() ... found
checking for memalign() ... found
checking for mmap(MAP_ANON|MAP_SHARED) ... found
checking for mmap("/dev/zero", MAP_SHARED) ... found
checking for System V shared memory ... found
checking for POSIX semaphores ... found
checking for struct msghdr.msg_control ... found
checking for ioctl(FIONBIO) ... found
checking for ioctl(FIONREAD) ... found
checking for struct tm.tm_gmtoff ... found
checking for struct dirent.d_namlen ... not found
checking for struct dirent.d_type ... found
checking for sysconf(_SC_NPROCESSORS_ONLN) ... found
checking for sysconf(_SC_LEVEL1_DCACHE_LINESIZE) ... not found
checking for openat(), fstatat() ... found
checking for getaddrinfo() ... found
configuring additional modules
adding module in ./modules/nginx-rtmp-module
 + ngx_rtmp_module was configured
adding module in ./modules/nginx-client-module
 + ngx_client_module was configured
adding module in ./modules/nginx-multiport-module
 + ngx_multiport_module was configured
adding module in ./modules/nginx-toolkit-module
 + ngx_toolkit_module was configured
checking for PCRE library ... found
checking for PCRE JIT support ... found
checking for OpenSSL library ... not found
checking for OpenSSL library in /usr/local/ ... not found
checking for OpenSSL library in /usr/pkg/ ... not found
checking for OpenSSL library in /opt/local/ ... not found

./configure: error: SSL modules require the OpenSSL library.
You can either do not enable the modules, or install the OpenSSL library
into the system, or build the OpenSSL library statically from the source
with nginx by using --with-openssl=<path> option.

make[3]: *** [Makefile:104: /openwrt/build_dir/target-mips_24kc_musl/luci-app-nginx-pingos/nginx-1.19.6/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
