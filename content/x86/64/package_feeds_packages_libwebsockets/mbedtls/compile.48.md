---
title: "compile.48"
date: 2021-02-22 14:41:15.179363
hidden: false
draft: false
weight: -48
---

build number: `48`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/libwebsockets/compile -j$(nproc) || make package/feeds/packages/libwebsockets/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/020-fix-travis.patch using plaintext: 
patching file CMakeLists.txt
CMake Deprecation Warning at CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 2.8.12 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- The C compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/bin/x86_64-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- CMAKE_TOOLCHAIN_FILE=''
-- Found Git: /openwrt/staging_dir/host/bin/git  
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
Git commit hash: 
-- Found MBEDTLS: /openwrt/staging_dir/target-x86_64_musl/usr/include  
-- Performing Test LWS_HAVE_inline
-- Performing Test LWS_HAVE_inline - Success
-- Performing Test LWS_HAVE___inline__
-- Performing Test LWS_HAVE___inline__ - Success
-- Performing Test LWS_HAVE___inline
-- Performing Test LWS_HAVE___inline - Success
-- Performing Test LWS_HAVE_BZERO
-- Performing Test LWS_HAVE_BZERO - Success
-- Looking for fork
-- Looking for fork - found
-- Looking for getenv
-- Looking for getenv - found
-- Looking for malloc
-- Looking for malloc - found
-- Looking for memset
-- Looking for memset - found
-- Looking for realloc
-- Looking for realloc - found
-- Looking for socket
-- Looking for socket - found
-- Looking for strerror
-- Looking for strerror - found
-- Looking for vfork
-- Looking for vfork - found
-- Looking for execvpe
-- Looking for execvpe - found
-- Looking for getifaddrs
-- Looking for getifaddrs - found
-- Looking for snprintf
-- Looking for snprintf - found
-- Looking for _snprintf
-- Looking for _snprintf - not found
-- Looking for _vsnprintf
-- Looking for _vsnprintf - not found
-- Looking for getloadavg
-- Looking for getloadavg - found
-- Looking for atoll
-- Looking for atoll - found
-- Looking for _atoi64
-- Looking for _atoi64 - not found
-- Looking for _stat32i64
-- Looking for _stat32i64 - not found
-- Looking for dlfcn.h
-- Looking for dlfcn.h - found
-- Looking for fcntl.h
-- Looking for fcntl.h - found
-- Looking for in6addr.h
-- Looking for in6addr.h - not found
-- Looking for memory.h
-- Looking for memory.h - found
-- Looking for netinet/in.h
-- Looking for netinet/in.h - found
-- Looking for stdint.h
-- Looking for stdint.h - found
-- Looking for stdlib.h
-- Looking for stdlib.h - found
-- Looking for strings.h
-- Looking for strings.h - found
-- Looking for string.h
-- Looking for string.h - found
-- Looking for sys/prctl.h
-- Looking for sys/prctl.h - found
-- Looking for sys/socket.h
-- Looking for sys/socket.h - found
-- Looking for sys/sockio.h
-- Looking for sys/sockio.h - not found
-- Looking for sys/stat.h
-- Looking for sys/stat.h - found
-- Looking for sys/types.h
-- Looking for sys/types.h - found
-- Looking for unistd.h
-- Looking for unistd.h - found
-- Looking for vfork.h
-- Looking for vfork.h - not found
-- Looking for sys/capability.h
-- Looking for sys/capability.h - found
-- Looking for malloc.h
-- Looking for malloc.h - found
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for cap_set_flag in cap
-- Looking for cap_set_flag in cap - found
-- Looking for 4 include files stdlib.h, ..., float.h
-- Looking for 4 include files stdlib.h, ..., float.h - found
-- Performing Test LWS_HAS_INTPTR_T
-- Performing Test LWS_HAS_INTPTR_T - Success
-- Performing Test LWS_HAS_PTHREAD_SETNAME_NP
-- Performing Test LWS_HAS_PTHREAD_SETNAME_NP - Success
-- Performing Test LWS_HAVE_VISIBILITY
-- Performing Test LWS_HAVE_VISIBILITY - Success
Compiling with SSL support
MBEDTLS include dir: /openwrt/staging_dir/target-x86_64_musl/usr/include
MBEDTLS libraries: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libmbedtls.so;/openwrt/staging_dir/target-x86_64_musl/usr/lib/libmbedx509.so;/openwrt/staging_dir/target-x86_64_musl/usr/lib/libmbedcrypto.so
-- Looking for SSL_CTX_set1_param
-- Looking for SSL_CTX_set1_param - not found
-- Looking for SSL_set_info_callback
-- Looking for SSL_set_info_callback - not found
-- Looking for X509_VERIFY_PARAM_set1_host
-- Looking for X509_VERIFY_PARAM_set1_host - not found
-- Looking for RSA_set0_key
-- Looking for RSA_set0_key - not found
-- Looking for X509_get_key_usage
-- Looking for X509_get_key_usage - not found
-- Looking for SSL_CTX_get0_certificate
-- Looking for SSL_CTX_get0_certificate - not found
-- Looking for SSL_get0_alpn_selected
-- Looking for SSL_get0_alpn_selected - not found
-- Looking for SSL_set_alpn_protos
-- Looking for SSL_set_alpn_protos - not found
-- Looking for SSL_CTX_set_ciphersuites
-- Looking for SSL_CTX_set_ciphersuites - not found
-- Performing Test LWS_HAVE_PIPE2
-- Performing Test LWS_HAVE_PIPE2 - Success
-- Performing Test LWS_HAVE_TCP_USER_TIMEOUT
-- Performing Test LWS_HAVE_TCP_USER_TIMEOUT - Success
Searching for OpenSSL executable and dlls
OpenSSL executable: 
 GENCERTS = 0
-- Looking for RPMTools... - rpmbuild NOT FOUND
---------------------------------------------------------------------
  Settings:  (For more help do cmake -LH <srcpath>)
---------------------------------------------------------------------
 LWS_WITH_STATIC = ON
 LWS_WITH_SHARED = ON
 LWS_WITH_SSL = ON (SSL Support)
 LWS_SSL_CLIENT_USE_OS_CA_CERTS = 1
 LWS_WITH_WOLFSSL = OFF (wolfSSL/CyaSSL replacement for OpenSSL)
 LWS_WITH_MBEDTLS = 1 (mbedTLS replacement for OpenSSL)
 LWS_WITHOUT_BUILTIN_SHA1 = OFF
 LWS_WITHOUT_BUILTIN_GETIFADDRS = OFF
 LWS_WITHOUT_CLIENT = OFF
 LWS_WITHOUT_SERVER = OFF
 LWS_LINK_TESTAPPS_DYNAMIC = OFF
 LWS_WITHOUT_TESTAPPS = ON
 LWS_WITHOUT_TEST_SERVER = OFF
 LWS_WITHOUT_TEST_SERVER_EXTPOLL = OFF
 LWS_WITHOUT_TEST_PING = OFF
 LWS_WITHOUT_TEST_CLIENT = OFF
 LWS_WITHOUT_EXTENSIONS = ON
 LWS_WITH_LATENCY = OFF
 LWS_WITHOUT_DAEMONIZE = ON
 LWS_WITH_LIBEV = OFF
 LWS_WITH_LIBUV = OFF
 LWS_WITH_LIBEVENT = OFF
 LWS_IPV6 = ON
 LWS_UNIX_SOCK = OFF
 LWS_WITH_HTTP2 = 1
 LWS_SSL_SERVER_WITH_ECDH_CERT = OFF
 LWS_MAX_SMP = 1
 LWS_HAVE_PTHREAD_H = 1
 LWS_WITH_CGI = OFF
 LWS_HAVE_OPENSSL_ECDH_H = 
 LWS_HAVE_SSL_CTX_set1_param = 
 LWS_HAVE_RSA_SET0_KEY = 
 LWS_WITH_HTTP_PROXY = OFF
 LIBHUBBUB_LIBRARIES = 
 PLUGINS = 
 LWS_WITH_ACCESS_LOG = OFF
 LWS_WITH_SERVER_STATUS = OFF
 LWS_WITH_LEJP = ON
 LWS_WITH_LEJP_CONF = ON
 LWS_WITH_SMTP = OFF
 LWS_WITH_GENERIC_SESSIONS = OFF
 LWS_STATIC_PIC = OFF
 LWS_WITH_RANGES = OFF
 LWS_PLAT_OPTEE = OFF
 LWS_WITH_ESP32 = OFF
 LWS_WITH_ZIP_FOPS = OFF
 LWS_AVOID_SIGPIPE_IGN = OFF
 LWS_WITH_STATS = OFF
 LWS_WITH_SOCKS5 = OFF
 LWS_HAVE_SYS_CAPABILITY_H = 1
 LWS_HAVE_LIBCAP = 1
 LWS_WITH_PEER_LIMITS = OFF
 LWS_HAVE_ATOLL = 1
 LWS_HAVE__ATOI64 = 
 LWS_HAVE_STAT32I64 = 
 LWS_HAS_INTPTR_T = 1
 LWS_WITH_EXPORT_LWSTARGETS = ON
---------------------------------------------------------------------
-- Configuring done
-- Generating done
CMake Warning:
  Manually-specified variables were not used by the project:

    CMAKE_ASM_COMPILER
    CMAKE_ASM_COMPILER_LAUNCHER
    CMAKE_CXX_COMPILER
    CMAKE_CXX_FLAGS_RELEASE
    CMAKE_EXE_LINKER_FLAGS
    CMAKE_EXPORT_PACKAGE_REGISTRY
    CMAKE_FIND_PACKAGE_NO_PACKAGE_REGISTRY
    CMAKE_FIND_PACKAGE_NO_SYSTEM_PACKAGE_REGISTRY
    CMAKE_MODULE_LINKER_FLAGS
    DL_LIBRARY


-- Build files have been written to: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0'
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0'
Scanning dependencies of target websockets_shared
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0'
[  0%] Building C object CMakeFiles/websockets_shared.dir/lib/core/alloc.c.o
[  1%] Building C object CMakeFiles/websockets_shared.dir/lib/core/context.c.o
[  2%] Building C object CMakeFiles/websockets_shared.dir/lib/core/dummy-callback.c.o
[  3%] Building C object CMakeFiles/websockets_shared.dir/lib/core/libwebsockets.c.o
[  4%] Building C object CMakeFiles/websockets_shared.dir/lib/core/output.c.o
[  5%] Building C object CMakeFiles/websockets_shared.dir/lib/core/pollfd.c.o
[  6%] Building C object CMakeFiles/websockets_shared.dir/lib/core/service.c.o
[  6%] Building C object CMakeFiles/websockets_shared.dir/lib/misc/base64-decode.c.o
[  7%] Building C object CMakeFiles/websockets_shared.dir/lib/misc/lws-ring.c.o
[  8%] Building C object CMakeFiles/websockets_shared.dir/lib/roles/pipe/ops-pipe.c.o
[  9%] Building C object CMakeFiles/websockets_shared.dir/lib/roles/http/header.c.o
[ 10%] Building C object CMakeFiles/websockets_shared.dir/lib/roles/http/server/parsers.c.o
[ 11%] Building C object CMakeFiles/websockets_shared.dir/lib/roles/h1/ops-h1.c.o
[ 12%] Building C object CMakeFiles/websockets_shared.dir/lib/roles/ws/ops-ws.c.o
[ 12%] Building C object CMakeFiles/websockets_shared.dir/lib/roles/ws/client-ws.c.o
[ 13%] Building C object CMakeFiles/websockets_shared.dir/lib/roles/ws/client-parser-ws.c.o
[ 14%] Building C object CMakeFiles/websockets_shared.dir/lib/roles/ws/server-ws.c.o
[ 15%] Building C object CMakeFiles/websockets_shared.dir/lib/roles/raw-skt/ops-raw-skt.c.o
[ 16%] Building C object CMakeFiles/websockets_shared.dir/lib/roles/raw-file/ops-raw-file.c.o
[ 17%] Building C object CMakeFiles/websockets_shared.dir/lib/misc/lwsac/lwsac.c.o
[ 18%] Building C object CMakeFiles/websockets_shared.dir/lib/misc/lwsac/cached-file.c.o
[ 18%] Building C object CMakeFiles/websockets_shared.dir/lib/core/connect.c.o
[ 19%] Building C object CMakeFiles/websockets_shared.dir/lib/roles/http/client/client.c.o
[ 20%] Building C object CMakeFiles/websockets_shared.dir/lib/roles/http/client/client-handshake.c.o
[ 21%] Building C object CMakeFiles/websockets_shared.dir/lib/core/adopt.c.o
[ 22%] Building C object CMakeFiles/websockets_shared.dir/lib/roles/listen/ops-listen.c.o
[ 23%] Building C object CMakeFiles/websockets_shared.dir/lib/tls/mbedtls/wrapper/library/ssl_cert.c.o
[ 24%] Building C object CMakeFiles/websockets_shared.dir/lib/tls/mbedtls/wrapper/library/ssl_lib.c.o
[ 25%] Building C object CMakeFiles/websockets_shared.dir/lib/tls/mbedtls/wrapper/library/ssl_methods.c.o
[ 25%] Building C object CMakeFiles/websockets_shared.dir/lib/tls/mbedtls/wrapper/library/ssl_pkey.c.o
[ 26%] Building C object CMakeFiles/websockets_shared.dir/lib/tls/mbedtls/wrapper/library/ssl_stack.c.o
[ 27%] Building C object CMakeFiles/websockets_shared.dir/lib/tls/mbedtls/wrapper/library/ssl_x509.c.o
[ 28%] Building C object CMakeFiles/websockets_shared.dir/lib/tls/mbedtls/wrapper/platform/ssl_pm.c.o
[ 29%] Building C object CMakeFiles/websockets_shared.dir/lib/tls/mbedtls/wrapper/platform/ssl_port.c.o
[ 30%] Building C object CMakeFiles/websockets_shared.dir/lib/tls/tls.c.o
[ 31%] Building C object CMakeFiles/websockets_shared.dir/lib/tls/mbedtls/ssl.c.o
[ 31%] Building C object CMakeFiles/websockets_shared.dir/lib/tls/tls-server.c.o
[ 32%] Building C object CMakeFiles/websockets_shared.dir/lib/tls/mbedtls/mbedtls-server.c.o
[ 33%] Building C object CMakeFiles/websockets_shared.dir/lib/tls/tls-client.c.o
[ 34%] Building C object CMakeFiles/websockets_shared.dir/lib/tls/mbedtls/mbedtls-client.c.o
[ 35%] Building C object CMakeFiles/websockets_shared.dir/lib/misc/sha-1.c.o
[ 36%] Building C object CMakeFiles/websockets_shared.dir/lib/roles/h2/http2.c.o
[ 37%] Building C object CMakeFiles/websockets_shared.dir/lib/roles/h2/hpack.c.o
[ 37%] Building C object CMakeFiles/websockets_shared.dir/lib/roles/h2/ops-h2.c.o
[ 38%] Building C object CMakeFiles/websockets_shared.dir/lib/plat/unix/unix-caps.c.o
[ 39%] Building C object CMakeFiles/websockets_shared.dir/lib/plat/unix/unix-fds.c.o
[ 40%] Building C object CMakeFiles/websockets_shared.dir/lib/plat/unix/unix-file.c.o
[ 41%] Building C object CMakeFiles/websockets_shared.dir/lib/plat/unix/unix-misc.c.o
[ 42%] Building C object CMakeFiles/websockets_shared.dir/lib/plat/unix/unix-init.c.o
[ 43%] Building C object CMakeFiles/websockets_shared.dir/lib/plat/unix/unix-pipe.c.o
[ 43%] Building C object CMakeFiles/websockets_shared.dir/lib/plat/unix/unix-service.c.o
[ 44%] Building C object CMakeFiles/websockets_shared.dir/lib/plat/unix/unix-sockets.c.o
[ 45%] Building C object CMakeFiles/websockets_shared.dir/lib/roles/http/server/server.c.o
[ 46%] Building C object CMakeFiles/websockets_shared.dir/lib/roles/http/server/lws-spa.c.o
[ 47%] Building C object CMakeFiles/websockets_shared.dir/lib/event-libs/poll/poll.c.o
[ 48%] Building C object CMakeFiles/websockets_shared.dir/lib/misc/lejp.c.o
[ 49%] Building C object CMakeFiles/websockets_shared.dir/lib/roles/http/server/lejp-conf.c.o
[ 50%] Linking C shared library lib/libwebsockets.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0'
[ 50%] Built target websockets_shared
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0'
Scanning dependencies of target websockets
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0'
[ 50%] Building C object CMakeFiles/websockets.dir/lib/core/alloc.c.o
[ 51%] Building C object CMakeFiles/websockets.dir/lib/core/context.c.o
[ 52%] Building C object CMakeFiles/websockets.dir/lib/core/dummy-callback.c.o
[ 53%] Building C object CMakeFiles/websockets.dir/lib/core/libwebsockets.c.o
[ 54%] Building C object CMakeFiles/websockets.dir/lib/core/output.c.o
[ 55%] Building C object CMakeFiles/websockets.dir/lib/core/pollfd.c.o
[ 56%] Building C object CMakeFiles/websockets.dir/lib/core/service.c.o
[ 56%] Building C object CMakeFiles/websockets.dir/lib/misc/base64-decode.c.o
[ 57%] Building C object CMakeFiles/websockets.dir/lib/misc/lws-ring.c.o
[ 58%] Building C object CMakeFiles/websockets.dir/lib/roles/pipe/ops-pipe.c.o
[ 59%] Building C object CMakeFiles/websockets.dir/lib/roles/http/header.c.o
[ 60%] Building C object CMakeFiles/websockets.dir/lib/roles/http/server/parsers.c.o
[ 61%] Building C object CMakeFiles/websockets.dir/lib/roles/h1/ops-h1.c.o
[ 62%] Building C object CMakeFiles/websockets.dir/lib/roles/ws/ops-ws.c.o
[ 62%] Building C object CMakeFiles/websockets.dir/lib/roles/ws/client-ws.c.o
[ 63%] Building C object CMakeFiles/websockets.dir/lib/roles/ws/client-parser-ws.c.o
[ 64%] Building C object CMakeFiles/websockets.dir/lib/roles/ws/server-ws.c.o
[ 65%] Building C object CMakeFiles/websockets.dir/lib/roles/raw-skt/ops-raw-skt.c.o
[ 66%] Building C object CMakeFiles/websockets.dir/lib/roles/raw-file/ops-raw-file.c.o
[ 67%] Building C object CMakeFiles/websockets.dir/lib/misc/lwsac/lwsac.c.o
[ 68%] Building C object CMakeFiles/websockets.dir/lib/misc/lwsac/cached-file.c.o
[ 68%] Building C object CMakeFiles/websockets.dir/lib/core/connect.c.o
[ 69%] Building C object CMakeFiles/websockets.dir/lib/roles/http/client/client.c.o
[ 70%] Building C object CMakeFiles/websockets.dir/lib/roles/http/client/client-handshake.c.o
[ 71%] Building C object CMakeFiles/websockets.dir/lib/core/adopt.c.o
[ 72%] Building C object CMakeFiles/websockets.dir/lib/roles/listen/ops-listen.c.o
[ 73%] Building C object CMakeFiles/websockets.dir/lib/tls/mbedtls/wrapper/library/ssl_cert.c.o
[ 74%] Building C object CMakeFiles/websockets.dir/lib/tls/mbedtls/wrapper/library/ssl_lib.c.o
[ 75%] Building C object CMakeFiles/websockets.dir/lib/tls/mbedtls/wrapper/library/ssl_methods.c.o
[ 75%] Building C object CMakeFiles/websockets.dir/lib/tls/mbedtls/wrapper/library/ssl_pkey.c.o
[ 76%] Building C object CMakeFiles/websockets.dir/lib/tls/mbedtls/wrapper/library/ssl_stack.c.o
[ 77%] Building C object CMakeFiles/websockets.dir/lib/tls/mbedtls/wrapper/library/ssl_x509.c.o
[ 78%] Building C object CMakeFiles/websockets.dir/lib/tls/mbedtls/wrapper/platform/ssl_pm.c.o
[ 79%] Building C object CMakeFiles/websockets.dir/lib/tls/mbedtls/wrapper/platform/ssl_port.c.o
[ 80%] Building C object CMakeFiles/websockets.dir/lib/tls/tls.c.o
[ 81%] Building C object CMakeFiles/websockets.dir/lib/tls/mbedtls/ssl.c.o
[ 81%] Building C object CMakeFiles/websockets.dir/lib/tls/tls-server.c.o
[ 82%] Building C object CMakeFiles/websockets.dir/lib/tls/mbedtls/mbedtls-server.c.o
[ 83%] Building C object CMakeFiles/websockets.dir/lib/tls/tls-client.c.o
[ 84%] Building C object CMakeFiles/websockets.dir/lib/tls/mbedtls/mbedtls-client.c.o
[ 85%] Building C object CMakeFiles/websockets.dir/lib/misc/sha-1.c.o
[ 86%] Building C object CMakeFiles/websockets.dir/lib/roles/h2/http2.c.o
[ 87%] Building C object CMakeFiles/websockets.dir/lib/roles/h2/hpack.c.o
[ 87%] Building C object CMakeFiles/websockets.dir/lib/roles/h2/ops-h2.c.o
[ 88%] Building C object CMakeFiles/websockets.dir/lib/plat/unix/unix-caps.c.o
[ 89%] Building C object CMakeFiles/websockets.dir/lib/plat/unix/unix-fds.c.o
[ 90%] Building C object CMakeFiles/websockets.dir/lib/plat/unix/unix-file.c.o
[ 91%] Building C object CMakeFiles/websockets.dir/lib/plat/unix/unix-misc.c.o
[ 92%] Building C object CMakeFiles/websockets.dir/lib/plat/unix/unix-init.c.o
[ 93%] Building C object CMakeFiles/websockets.dir/lib/plat/unix/unix-pipe.c.o
[ 93%] Building C object CMakeFiles/websockets.dir/lib/plat/unix/unix-service.c.o
[ 94%] Building C object CMakeFiles/websockets.dir/lib/plat/unix/unix-sockets.c.o
[ 95%] Building C object CMakeFiles/websockets.dir/lib/roles/http/server/server.c.o
[ 96%] Building C object CMakeFiles/websockets.dir/lib/roles/http/server/lws-spa.c.o
[ 97%] Building C object CMakeFiles/websockets.dir/lib/event-libs/poll/poll.c.o
[ 98%] Building C object CMakeFiles/websockets.dir/lib/misc/lejp.c.o
[ 99%] Building C object CMakeFiles/websockets.dir/lib/roles/http/server/lejp-conf.c.o
[100%] Linking C static library lib/libwebsockets.a
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0'
[100%] Built target websockets
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0'
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0'
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0'
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0'
[ 50%] Built target websockets_shared
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0'
Scanning dependencies of target websockets
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0'
[ 50%] Building C object CMakeFiles/websockets.dir/lib/core/alloc.c.o
[ 51%] Building C object CMakeFiles/websockets.dir/lib/core/context.c.o
[ 52%] Building C object CMakeFiles/websockets.dir/lib/core/dummy-callback.c.o
[ 53%] Building C object CMakeFiles/websockets.dir/lib/core/libwebsockets.c.o
[ 54%] Building C object CMakeFiles/websockets.dir/lib/core/output.c.o
[ 55%] Building C object CMakeFiles/websockets.dir/lib/core/pollfd.c.o
[ 56%] Building C object CMakeFiles/websockets.dir/lib/core/service.c.o
[ 56%] Building C object CMakeFiles/websockets.dir/lib/misc/base64-decode.c.o
[ 57%] Building C object CMakeFiles/websockets.dir/lib/misc/lws-ring.c.o
[ 58%] Building C object CMakeFiles/websockets.dir/lib/roles/pipe/ops-pipe.c.o
[ 59%] Building C object CMakeFiles/websockets.dir/lib/roles/http/header.c.o
[ 60%] Building C object CMakeFiles/websockets.dir/lib/roles/http/server/parsers.c.o
[ 61%] Building C object CMakeFiles/websockets.dir/lib/roles/h1/ops-h1.c.o
[ 62%] Building C object CMakeFiles/websockets.dir/lib/roles/ws/ops-ws.c.o
[ 62%] Building C object CMakeFiles/websockets.dir/lib/roles/ws/client-ws.c.o
[ 63%] Building C object CMakeFiles/websockets.dir/lib/roles/ws/client-parser-ws.c.o
[ 64%] Building C object CMakeFiles/websockets.dir/lib/roles/ws/server-ws.c.o
[ 65%] Building C object CMakeFiles/websockets.dir/lib/roles/raw-skt/ops-raw-skt.c.o
[ 66%] Building C object CMakeFiles/websockets.dir/lib/roles/raw-file/ops-raw-file.c.o
[ 67%] Building C object CMakeFiles/websockets.dir/lib/misc/lwsac/lwsac.c.o
[ 68%] Building C object CMakeFiles/websockets.dir/lib/misc/lwsac/cached-file.c.o
[ 68%] Building C object CMakeFiles/websockets.dir/lib/core/connect.c.o
[ 69%] Building C object CMakeFiles/websockets.dir/lib/roles/http/client/client.c.o
[ 70%] Building C object CMakeFiles/websockets.dir/lib/roles/http/client/client-handshake.c.o
[ 71%] Building C object CMakeFiles/websockets.dir/lib/core/adopt.c.o
[ 72%] Building C object CMakeFiles/websockets.dir/lib/roles/listen/ops-listen.c.o
[ 73%] Building C object CMakeFiles/websockets.dir/lib/tls/mbedtls/wrapper/library/ssl_cert.c.o
[ 74%] Building C object CMakeFiles/websockets.dir/lib/tls/mbedtls/wrapper/library/ssl_lib.c.o
[ 75%] Building C object CMakeFiles/websockets.dir/lib/tls/mbedtls/wrapper/library/ssl_methods.c.o
[ 75%] Building C object CMakeFiles/websockets.dir/lib/tls/mbedtls/wrapper/library/ssl_pkey.c.o
[ 76%] Building C object CMakeFiles/websockets.dir/lib/tls/mbedtls/wrapper/library/ssl_stack.c.o
[ 77%] Building C object CMakeFiles/websockets.dir/lib/tls/mbedtls/wrapper/library/ssl_x509.c.o
[ 78%] Building C object CMakeFiles/websockets.dir/lib/tls/mbedtls/wrapper/platform/ssl_pm.c.o
[ 79%] Building C object CMakeFiles/websockets.dir/lib/tls/tls.c.o
[ 80%] Building C object CMakeFiles/websockets.dir/lib/tls/mbedtls/ssl.c.o
[ 80%] Building C object CMakeFiles/websockets.dir/lib/tls/tls-server.c.o
[ 81%] Building C object CMakeFiles/websockets.dir/lib/tls/mbedtls/mbedtls-server.c.o
[ 82%] Building C object CMakeFiles/websockets.dir/lib/tls/tls-client.c.o
[ 83%] Building C object CMakeFiles/websockets.dir/lib/tls/mbedtls/mbedtls-client.c.o
[ 84%] Building C object CMakeFiles/websockets.dir/lib/misc/sha-1.c.o
[ 85%] Building C object CMakeFiles/websockets.dir/lib/roles/h2/http2.c.o
[ 86%] Building C object CMakeFiles/websockets.dir/lib/roles/h2/hpack.c.o
[ 86%] Building C object CMakeFiles/websockets.dir/lib/roles/h2/ops-h2.c.o
[ 87%] Building C object CMakeFiles/websockets.dir/lib/plat/unix/unix-caps.c.o
[ 88%] Building C object CMakeFiles/websockets.dir/lib/plat/unix/unix-fds.c.o
[ 89%] Building C object CMakeFiles/websockets.dir/lib/plat/unix/unix-file.c.o
[ 90%] Building C object CMakeFiles/websockets.dir/lib/plat/unix/unix-misc.c.o
[ 91%] Building C object CMakeFiles/websockets.dir/lib/plat/unix/unix-init.c.o
[ 92%] Building C object CMakeFiles/websockets.dir/lib/plat/unix/unix-pipe.c.o
[ 92%] Building C object CMakeFiles/websockets.dir/lib/plat/unix/unix-service.c.o
[ 93%] Building C object CMakeFiles/websockets.dir/lib/plat/unix/unix-sockets.c.o
[ 94%] Building C object CMakeFiles/websockets.dir/lib/roles/http/server/server.c.o
[ 95%] Building C object CMakeFiles/websockets.dir/lib/roles/http/server/lws-spa.c.o
[ 96%] Building C object CMakeFiles/websockets.dir/lib/event-libs/poll/poll.c.o
[ 97%] Building C object CMakeFiles/websockets.dir/lib/misc/lejp.c.o
[ 98%] Building C object CMakeFiles/websockets.dir/lib/roles/http/server/lejp-conf.c.o
[ 99%] Linking C static library lib/libwebsockets.a
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0'
[100%] Built target websockets
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0'
Install the project...
-- Install configuration: "Release"
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/lib/pkgconfig/libwebsockets.pc
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/lib/pkgconfig/libwebsockets_static.pc
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-ring.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-diskcache.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-x509.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-client.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-service.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-fts.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-http.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-cgi.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-ws-state.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-plugin-generic-sessions.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-write.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-logs.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-context-vhost.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-writeable.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-ws-ext.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-threadpool.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-network-helper.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-jws.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-timeout-timer.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-dbus.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-adopt.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-ws-close.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-esp32.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-lejp.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-callbacks.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-genrsa.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-tokenize.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-sha1-base64.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-spa.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-lwsac.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-stats.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-jwk.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-vfs.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-protocols-plugins.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-genhash.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-misc.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets/lws-purify.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/lib/libwebsockets.a
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/lws_config.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/lws-plugin-ssh.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/lib/libwebsockets.so.14
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/lib/libwebsockets.so
-- Up-to-date: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/libwebsockets.h
-- Up-to-date: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/lws_config.h
-- Up-to-date: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/include/lws-plugin-ssh.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/lib/cmake/libwebsockets/LibwebsocketsConfig.cmake
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/lib/cmake/libwebsockets/LibwebsocketsConfigVersion.cmake
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/lib/cmake/libwebsockets/LibwebsocketsTargets.cmake
-- Installing: /openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0/ipkg-install/usr/lib/cmake/libwebsockets/LibwebsocketsTargets-release.cmake
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/libwebsockets-mbedtls/libwebsockets-3.1.0'
Package libwebsockets-mbedtls is missing dependencies for the following libraries:
libmbedtls.so.9
make[3]: *** [Makefile:111: /openwrt/bin/packages/x86_64/packages/libwebsockets-mbedtls_3.1.0-2_x86_64.ipk] Error 1
```
