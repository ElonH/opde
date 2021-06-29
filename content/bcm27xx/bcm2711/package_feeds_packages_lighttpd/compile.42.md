---
title: "compile.42"
date: 2021-06-29 09:35:35.001326
hidden: false
draft: false
weight: -42
---

build number: `42`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/lighttpd/compile -j$(nproc) || make package/feeds/packages/lighttpd/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-meson-lua.patch using plaintext: 
patching file src/meson.build

Applying ./patches/020-meson-zstd.patch using plaintext: 
patching file meson_options.txt

Applying ./patches/030-101-upgrade-w-content-length.patch using plaintext: 
patching file src/http-header-glue.c

Applying ./patches/040-mod_auth-close-http2-after-bad-pass.patch using plaintext: 
patching file src/connections.c
patching file src/mod_accesslog.c
patching file src/mod_auth.c
patching file src/reqpool.c
patching file src/request.h
patching file src/response.c

Applying ./patches/050-openssl-skip-chain-build-self-issued.patch using plaintext: 
patching file src/mod_openssl.c

Applying ./patches/060-meson-zstd.patch using plaintext: 
patching file src/meson.build

Applying ./patches/070-ls-hpack-update.patch using plaintext: 
patching file src/ls-hpack/lshpack.c
patching file src/ls-hpack/lshpack.h

Applying ./patches/080-http2-data-after-response.patch using plaintext: 
patching file src/h2.c
patching file src/h2.h
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/lighttpd-1.4.59
Build dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/lighttpd-1.4.59/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: lighttpd
Project version: 1.4.59
C compiler for the host machine: ccache_cc (gcc 8.4.0 "aarch64-openwrt-linux-musl-gcc (OpenWrt GCC 8.4.0 r0-af265d3) 8.4.0")
C linker for the host machine: ccache_cc ld.bfd 2.34
C compiler for the build machine: ccache gcc (gcc 9.3.0 "gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0")
C linker for the build machine: gcc ld.bfd 2.34
Build machine cpu family: x86_64
Build machine cpu: x86_64
Host machine cpu family: aarch64
Host machine cpu: generic
Target machine cpu family: aarch64
Target machine cpu: generic
Has header "sys/devpoll.h" : NO 
Has header "sys/epoll.h" : YES 
Has header "sys/event.h" : NO 
Has header "sys/inotify.h" : YES 
Has header "sys/loadavg.h" : NO 
Has header "sys/mman.h" : YES 
Has header "sys/poll.h" : YES 
Has header "sys/port.h" : NO 
Has header "sys/prctl.h" : YES 
Has header "sys/resource.h" : YES 
Has header "sys/sendfile.h" : YES 
Has header "sys/select.h" : YES 
Has header "sys/types.h" : YES 
Has header "sys/uio.h" : YES 
Has header "sys/un.h" : YES 
Has header "sys/wait.h" : YES 
Has header "sys/time.h" : YES 
Has header "unistd.h" : YES 
Has header "pthread.h" : YES 
Has header "getopt.h" : YES 
Has header "inttypes.h" : YES 
Has header "poll.h" : YES 
Has header "pwd.h" : YES 
Has header "stddef.h" : YES 
Has header "stdint.h" : YES 
Has header "strings.h" : YES 
Has header "syslog.h" : YES 
Has header "crypt.h" : YES 
Checking for function "crypt_r" : YES 
Has header "sys/inotify.h" : YES (cached)
Checking for function "inotify_init" : YES 
Checking for type "socklen_t" : YES 
Has header "sys/random.h" : YES 
Checking for function "getentropy" : NO 
Has header "linux/random.h" : YES 
Checking for function "getrandom" : NO 
Checking for size of "long" : 8
Checking for size of "off_t" : 8
Checking for function "arc4random_buf" : NO 
Checking for function "chroot" : YES 
Checking for function "copy_file_range" : YES 
Checking for function "epoll_ctl" : YES 
Checking for function "fork" : YES 
Checking for function "getloadavg" : YES 
Checking for function "getrlimit" : YES 
Checking for function "getuid" : YES 
Checking for function "gmtime_r" : YES 
Checking for function "inet_aton" : YES 
Checking for function "inet_ntop" : YES 
Checking for function "jrand48" : YES 
Checking for function "kqueue" : NO 
Checking for function "localtime_r" : YES 
Checking for function "lstat" : YES 
Checking for function "madvise" : YES 
Checking for function "memcpy" : YES 
Checking for function "memset" : YES 
Checking for function "mmap" : YES 
Checking for function "pathconf" : YES 
Checking for function "pipe2" : YES 
Checking for function "poll" : YES 
Checking for function "port_create" : NO 
Checking for function "prctl" : YES 
Checking for function "pread" : YES 
Checking for function "posix_fadvise" : YES 
Checking for function "select" : YES 
Checking for function "sendfile" : YES 
Checking for function "send_file" : NO 
Checking for function "sendfile64" : YES 
Checking for function "sendfilev" : NO 
Checking for function "sigaction" : YES 
Checking for function "signal" : YES 
Checking for function "sigtimedwait" : YES 
Checking for function "srandom" : YES 
Checking for function "strptime" : YES 
Checking for function "syslog" : YES 
Checking for function "timegm" : YES 
Checking for function "writev" : YES 
Checking for function "inet_aton" : YES (cached)
Checking for function "issetugid" : YES 
Checking for function "inet_pton" : YES 
Checking for function "memset_s" : NO 
Checking for function "explicit_bzero" : YES 
Checking for function "explicit_memset" : NO 
Header <time.h> has symbol "clock_gettime" : NO 
Checking for function "clock_gettime" : YES 
Library rt found: YES
Checking for function "elftc_copyfile" : NO 
Checking if "IPv6 support" compiles: YES 
Checking if "weak symbols" compiles: YES 
Checking if "struct tm gmt offset" compiles: YES 
Library dl found: YES
Checking for function "dlopen" with dependency -ldl: YES 
Found pkg-config: /openwrt/staging_dir/host/bin/pkg-config (1.7.3)
Run-time dependency dbi found: YES 0.9.0
Library maxminddb found: YES
Checking for function "MMDB_open" with dependency -lmaxminddb: YES 
Library gdbm found: YES
Checking for function "gdbm_open" with dependency -lgdbm: YES 
Run-time dependency krb5 found: YES 1.19.1
Run-time dependency krb5-gssapi found: YES 1.19.1
Library ldap found: YES
Checking for function "ldap_sasl_bind_s" with dependency -lldap: YES 
Library lber found: YES
Checking for function "ber_printf" with dependency -llber: YES 
Library pam found: YES
Checking for function "pam_start" with dependency -lpam: YES 
Run-time dependency lua found: YES 5.1.5
Run-time dependency libmariadb found: YES 3.1.12
Run-time dependency libssl found: YES 1.1.1k
Run-time dependency libcrypto found: YES 1.1.1k
Dependency libcrypto found: YES 1.1.1k (cached)
Run-time dependency wolfssl found: YES 4.7.0
Dependency wolfssl found: YES 4.7.0 (cached)
Library mbedtls found: YES
Library mbedx509 found: YES
Library mbedcrypto found: YES
Library mbedcrypto found: YES
Run-time dependency nettle found: YES 3.6
Run-time dependency gnutls found: YES 3.7.2
Run-time dependency nss found: YES 3.65.0
Run-time dependency libpcre found: YES 8.44
Run-time dependency libpq found: YES 13.2
Found CMake: NO
Run-time dependency sasl2 found: NO (tried pkgconfig and cmake)
Library sasl2 found: YES
Checking for function "sasl_server_init" with dependency -lsasl2: YES 
Run-time dependency uuid found: YES 2.36.1
Run-time dependency libxml-2.0 found: YES 2.9.12
Run-time dependency sqlite31 found: NO (tried pkgconfig and cmake)
Library sqlite3 found: YES
Checking for function "sqlite3_reset" with dependency -lsqlite3: YES 
Run-time dependency zlib found: YES 1.2.11
Configuring config.h using configuration
Program ./prepare.sh found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/lighttpd-1.4.59/tests/./prepare.sh)
Program ./cachable.t found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/lighttpd-1.4.59/tests/./cachable.t)
Program ./core-404-handler.t found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/lighttpd-1.4.59/tests/./core-404-handler.t)
Program ./core-condition.t found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/lighttpd-1.4.59/tests/./core-condition.t)
Program ./core-keepalive.t found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/lighttpd-1.4.59/tests/./core-keepalive.t)
Program ./core-request.t found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/lighttpd-1.4.59/tests/./core-request.t)
Program ./core-response.t found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/lighttpd-1.4.59/tests/./core-response.t)
Program ./core-var-include.t found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/lighttpd-1.4.59/tests/./core-var-include.t)
Program ./lowercase.t found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/lighttpd-1.4.59/tests/./lowercase.t)
Program ./mod-auth.t found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/lighttpd-1.4.59/tests/./mod-auth.t)
Program ./mod-cgi.t found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/lighttpd-1.4.59/tests/./mod-cgi.t)
Program ./mod-deflate.t found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/lighttpd-1.4.59/tests/./mod-deflate.t)
Program ./mod-extforward.t found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/lighttpd-1.4.59/tests/./mod-extforward.t)
Program ./mod-fastcgi.t found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/lighttpd-1.4.59/tests/./mod-fastcgi.t)
Program ./mod-proxy.t found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/lighttpd-1.4.59/tests/./mod-proxy.t)
Program ./mod-secdownload.t found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/lighttpd-1.4.59/tests/./mod-secdownload.t)
Program ./mod-setenv.t found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/lighttpd-1.4.59/tests/./mod-setenv.t)
Program ./mod-ssi.t found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/lighttpd-1.4.59/tests/./mod-ssi.t)
Program ./request.t found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/lighttpd-1.4.59/tests/./request.t)
Program ./symlink.t found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/lighttpd-1.4.59/tests/./symlink.t)
Program ./cleanup.sh found: YES (/openwrt/build_dir/target-aarch64_cortex-a72_musl/lighttpd-1.4.59/tests/./cleanup.sh)
Build targets in project: 72


ERROR: Could not detect Ninja v1.8.2 or newer

A full log can be found at /openwrt/build_dir/target-aarch64_cortex-a72_musl/lighttpd-1.4.59/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:176: /openwrt/build_dir/target-aarch64_cortex-a72_musl/lighttpd-1.4.59/.configured_cc6b28215ba92b78187e2b6772d8b16e] Error 1
```
