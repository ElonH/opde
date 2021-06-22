---
title: "compile.40"
date: 2021-06-22 10:49:10.765877
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
make package/feeds/packages/nginx/compile -j$(nproc) || make package/feeds/packages/nginx/compile V=s
```

#### Compile.txt

``` bash
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

Applying ./patches-lua-nginx/100-no_by_lua_block.patch using plaintext: 
patching file lua-nginx/src/ngx_http_lua_module.c

Applying ./patches-rtmp-nginx/100-bigedian.patch using plaintext: 
patching file ngx_rtmp.c
patching file ngx_rtmp.h
patching file ngx_rtmp_amf.c
patching file ngx_rtmp_flv_module.c
patching file ngx_rtmp_handler.c
patching file ngx_rtmp_send.c
patching file hls/ngx_rtmp_hls_module.c
patching file ngx_rtmp.c
patching file ngx_rtmp.h
patching file ngx_rtmp_amf.c
patching file ngx_rtmp_bitop.h
patching file ngx_rtmp_eval.c
patching file ngx_rtmp_flv_module.c
patching file ngx_rtmp_handshake.c
patching file ngx_rtmp_mp4_module.c
patching file ngx_rtmp_receive.c
patching file ngx_rtmp_record_module.c

Applying ./patches-dav-nginx/100-drop-libxslt-dep.patch using plaintext: 
patching file nginx-dav-ext-module/config
Hunk #1 succeeded at 8 with fuzz 1.
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
checking for --with-ld-opt="-L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/lib -Wl,--gc-sections" ... found
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
checking for system byte ordering ... big endian
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
adding module in /openwrt/build_dir/target-mips_24kc_musl/nginx-all-module/nginx-1.19.6/nginx-headers-more
 + ngx_http_headers_more_filter_module was configured
adding module in /openwrt/build_dir/target-mips_24kc_musl/nginx-all-module/nginx-1.19.6/nginx-naxsi/naxsi_src
 + ngx_http_naxsi_module was configured
adding module in /openwrt/build_dir/target-mips_24kc_musl/nginx-all-module/nginx-1.19.6/lua-nginx
checking for Lua library in /openwrt/staging_dir/target-mips_24kc_musl/usr/lib and /openwrt/staging_dir/target-mips_24kc_musl/usr/include (specified by the LUA_LIB and LUA_INC env) ... found
checking for export symbols by default (-E) ... found
checking for export symbols by default (--export-all-symbols) ... not found
checking for SO_PASSCRED ... found
checking for __attribute__(constructor) ... found but is not working
checking for malloc_trim ... not found
 + ngx_http_lua_module was configured
adding module in /openwrt/build_dir/target-mips_24kc_musl/nginx-all-module/nginx-1.19.6/nginx-dav-ext-module
 + ngx_http_dav_ext_module was configured
adding module in /openwrt/build_dir/target-mips_24kc_musl/nginx-all-module/nginx-1.19.6/nginx-brotli
 + ngx_brotli was configured
adding module in /openwrt/build_dir/target-mips_24kc_musl/nginx-all-module/nginx-1.19.6/nginx-rtmp
 + ngx_rtmp_module was configured
adding module in /openwrt/build_dir/target-mips_24kc_musl/nginx-all-module/nginx-1.19.6/nginx-ts
 + ngx_http_ts_module was configured
adding module in /openwrt/build_dir/target-mips_24kc_musl/nginx-all-module/nginx-1.19.6/nginx-ubus-module
 + ngx_http_ubus_module was configured
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

make[3]: *** [Makefile:552: /openwrt/build_dir/target-mips_24kc_musl/nginx-all-module/nginx-1.19.6/.configured_0838168320e54341f45332feac78395d] Error 1
```
