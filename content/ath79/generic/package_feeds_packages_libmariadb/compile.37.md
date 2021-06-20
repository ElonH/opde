---
title: "compile.37"
date: 2021-06-20 22:39:07.394037
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
make package/feeds/packages/libmariadb/compile -j$(nproc) || make package/feeds/packages/libmariadb/compile V=s
```

#### Compile.txt

``` bash
CMake Deprecation Warning at CMakeLists.txt:5 (CMAKE_MINIMUM_REQUIRED):
  Compatibility with CMake < 2.8.12 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- The C compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Could NOT find CURL (missing: CURL_LIBRARY CURL_INCLUDE_DIR) 
-- Performing Test HAS_-Wunused_FLAG
-- Performing Test HAS_-Wunused_FLAG - Success
-- Performing Test HAS_-Wlogical-op_FLAG
-- Performing Test HAS_-Wlogical-op_FLAG - Success
-- Performing Test HAS_-Wno-uninitialized_FLAG
-- Performing Test HAS_-Wno-uninitialized_FLAG - Success
-- Performing Test HAS_-Wall_FLAG
-- Performing Test HAS_-Wall_FLAG - Success
-- Performing Test HAS_-Wextra_FLAG
-- Performing Test HAS_-Wextra_FLAG - Success
-- Performing Test HAS_-Wformat-security_FLAG
-- Performing Test HAS_-Wformat-security_FLAG - Success
-- Performing Test HAS_-Wno-init-self_FLAG
-- Performing Test HAS_-Wno-init-self_FLAG - Success
-- Performing Test HAS_-Wwrite-strings_FLAG
-- Performing Test HAS_-Wwrite-strings_FLAG - Success
-- Performing Test HAS_-Wshift-count-overflow_FLAG
-- Performing Test HAS_-Wshift-count-overflow_FLAG - Success
-- Performing Test HAS_-Wdeclaration-after-statement_FLAG
-- Performing Test HAS_-Wdeclaration-after-statement_FLAG - Success
-- Performing Test HAS_-Wno-undef_FLAG
-- Performing Test HAS_-Wno-undef_FLAG - Success
-- Performing Test HAS_-Wno-unknown-pragmas_FLAG
-- Performing Test HAS_-Wno-unknown-pragmas_FLAG - Success
-- Found Git: /openwrt/staging_dir/host/bin/git (found version "2.25.1") 
-- MariaDB Connector C: INSTALL_BINDIR=bin
-- MariaDB Connector C: INSTALL_LIBDIR=lib
-- MariaDB Connector C: INSTALL_PCDIR=lib/pkgconfig
-- MariaDB Connector C: INSTALL_INCLUDEDIR=include/mysql
-- MariaDB Connector C: INSTALL_DOCSDIR=
-- MariaDB Connector C: INSTALL_PLUGINDIR=lib/mariadb/plugin
-- MariaDB Connector C: LIBMARIADB_STATIC_NAME mariadbclient
-- Found ZLIB: /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libz.so (found version "1.2.11") 
-- Check if the system is big endian
-- Searching 16 bit integer
-- Looking for sys/types.h
-- Looking for sys/types.h - found
-- Looking for stdint.h
-- Looking for stdint.h - found
-- Looking for stddef.h
-- Looking for stddef.h - found
-- Check size of unsigned short
-- Check size of unsigned short - done
-- Searching 16 bit integer - Using unsigned short
-- Check if the system is big endian - big endian
-- Looking for include file alloca.h
-- Looking for include file alloca.h - found
-- Looking for include file arpa/inet.h
-- Looking for include file arpa/inet.h - found
-- Looking for include file dlfcn.h
-- Looking for include file dlfcn.h - found
-- Looking for include file fcntl.h
-- Looking for include file fcntl.h - found
-- Looking for include file float.h
-- Looking for include file float.h - found
-- Looking for include file limits.h
-- Looking for include file limits.h - found
-- Looking for include file linux/limits.h
-- Looking for include file linux/limits.h - found
-- Looking for include file pwd.h
-- Looking for include file pwd.h - found
-- Looking for include file sched.h
-- Looking for include file sched.h - found
-- Looking for include file select.h
-- Looking for include file select.h - not found
-- Looking for include file signal.h
-- Looking for include file signal.h - found
-- Looking for include file stdlib.h
-- Looking for include file stdlib.h - found
-- Looking for include file string.h
-- Looking for include file string.h - found
-- Looking for include file strings.h
-- Looking for include file strings.h - found
-- Looking for include file sys/ioctl.h
-- Looking for include file sys/ioctl.h - found
-- Looking for include file sys/select.h
-- Looking for include file sys/select.h - found
-- Looking for include file sys/socket.h
-- Looking for include file sys/socket.h - found
-- Looking for include file sys/stat.h
-- Looking for include file sys/stat.h - found
-- Looking for include file sys/un.h
-- Looking for include file sys/un.h - found
-- Looking for include file unistd.h
-- Looking for include file unistd.h - found
-- Looking for include file utime.h
-- Looking for include file utime.h - found
-- Looking for include file ucontext.h
-- Looking for include file ucontext.h - found
-- Looking for alloca
-- Looking for alloca - not found
-- Looking for dlerror
-- Looking for dlerror - found
-- Looking for dlopen
-- Looking for dlopen - found
-- Looking for fcntl
-- Looking for fcntl - found
-- Looking for memcpy
-- Looking for memcpy - found
-- Looking for nl_langinfo
-- Looking for nl_langinfo - found
-- Looking for setlocale
-- Looking for setlocale - found
-- Looking for poll
-- Looking for poll - found
-- Looking for getpwuid
-- Looking for getpwuid - found
-- Looking for makecontext
-- Looking for makecontext - not found
-- Looking for cuserid
-- Looking for cuserid - found
-- Check size of char *
-- Check size of char * - done
-- Check size of int
-- Check size of int - done
-- Check size of long
-- Check size of long - done
-- Check size of long long
-- Check size of long long - done
-- Check size of size_t
-- Check size of size_t - done
-- Check size of uchar
-- Check size of uchar - failed
-- Check size of uint
-- Check size of uint - done
-- Check size of ulong
-- Check size of ulong - done
-- Check size of int8
-- Check size of int8 - failed
-- Check size of uint8
-- Check size of uint8 - failed
-- Check size of int16
-- Check size of int16 - failed
-- Check size of uint16
-- Check size of uint16 - failed
-- Check size of int32
-- Check size of int32 - failed
-- Check size of uint32
-- Check size of uint32 - failed
-- Check size of int64
-- Check size of int64 - failed
-- Check size of uint64
-- Check size of uint64 - failed
-- Check size of socklen_t
-- Check size of socklen_t - failed
-- Performing Test SOCKET_SIZE_FOUND_socklen_t
-- Performing Test SOCKET_SIZE_FOUND_socklen_t - Success
-- Looking for floor
-- Looking for floor - found
-- Looking for pthread_getspecific
-- Looking for pthread_getspecific - found
-- Looking for gethostbyname_r
-- Looking for gethostbyname_r - found
-- Looking for setsockopt
-- Looking for setsockopt - found
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
-- Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY OPENSSL_INCLUDE_DIR) 
-- OpenSSL/LibreSSL not found
-- TLS library/version: 
-- SYSTEM_LIBS /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libz.so;dl;dl
-- Found GSSAPI: -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -lgssapi_krb5 -lkrb5 -lk5crypto -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lcom_err
-- Could NOT find CURL (missing: CURL_LIBRARY CURL_INCLUDE_DIR) 
-- Dynamic column API support: ON
-- SYSTEM processor: mips
-- MariaDB Connector/c configuration:
-- Static PLUGINS mysql_native_password;mysql_old_password;pvio_socket
-- Dynamic PLUGINS dialog;client_ed25519;caching_sha2_password;sha256_password;auth_gssapi_client;mysql_clear_password
-- CPack generation: TGZ
-- SSL support: OPENSSL Libs: 
-- Zlib support: YES
-- Installation layout: DEFAULT
-- Include files will be installed in include/mysql
-- Libraries will be installed in lib
-- Binaries will be installed in bin
-- Documentation included from 
-- Required: /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libz.so;dl
-- Configuring done
-- Generating done
CMake Warning:
  Manually-specified variables were not used by the project:

    CLIENT_PLUGIN_REMOTE_IO
    CMAKE_ASM_COMPILER
    CMAKE_ASM_COMPILER_LAUNCHER
    CMAKE_CXX_COMPILER
    CMAKE_EXPORT_NO_PACKAGE_REGISTRY
    CMAKE_EXPORT_PACKAGE_REGISTRY
    CMAKE_FIND_PACKAGE_NO_PACKAGE_REGISTRY
    CMAKE_FIND_PACKAGE_NO_SYSTEM_PACKAGE_REGISTRY
    DL_LIBRARY
    ICONV_LIBRARIES


-- Build files have been written to: /openwrt/build_dir/target-mips_24kc_musl/mariadb-connector-c-3.1.12-src
ninja: Entering directory `/openwrt/build_dir/target-mips_24kc_musl/mariadb-connector-c-3.1.12-src'
[1/98] Building C object CMakeFiles/caching_sha2_password.dir/plugins/auth/caching_sha2_pw.c.o
[2/98] Building C object CMakeFiles/caching_sha2_password.dir/libmariadb/secure/openssl_crypt.c.o
FAILED: CMakeFiles/caching_sha2_password.dir/libmariadb/secure/openssl_crypt.c.o 
/openwrt/staging_dir/host/bin/ccache /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc -DMARIADB_MACHINE_TYPE=\"mips\" -DMARIADB_SYSTEM_TYPE=\"Linux\" -Dcaching_sha2_password_EXPORTS -Iinclude -Iplugins/auth -Iplugins/pvio -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/mariadb-connector-c-3.1.12-src=mariadb-connector-c-3.1.12-src -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -Wunused -Wlogical-op -Wno-uninitialized -Wall -Wextra -Wformat-security -Wno-init-self -Wwrite-strings -Wshift-count-overflow -Wdeclaration-after-statement -Wno-undef -Wno-unknown-pragmas -DNDEBUG -DDBUG_OFF -fPIC -DPLUGIN_DYNAMIC=1 -MD -MT CMakeFiles/caching_sha2_password.dir/libmariadb/secure/openssl_crypt.c.o -MF CMakeFiles/caching_sha2_password.dir/libmariadb/secure/openssl_crypt.c.o.d -o CMakeFiles/caching_sha2_password.dir/libmariadb/secure/openssl_crypt.c.o -c libmariadb/secure/openssl_crypt.c
In file included from libmariadb/secure/openssl_crypt.c:20:
include/ma_crypt.h:74:1: error: unknown type name 'MA_HASH_CTX'; did you mean 'MA_HASH_MD5'?
 MA_HASH_CTX *ma_hash_new(unsigned int algorithm, MA_HASH_CTX *ctx);
 ^~~~~~~~~~~
 MA_HASH_MD5
include/ma_crypt.h:74:50: error: unknown type name 'MA_HASH_CTX'; did you mean 'MA_HASH_MD5'?
 MA_HASH_CTX *ma_hash_new(unsigned int algorithm, MA_HASH_CTX *ctx);
                                                  ^~~~~~~~~~~
                                                  MA_HASH_MD5
include/ma_crypt.h:83:19: error: unknown type name 'MA_HASH_CTX'; did you mean 'MA_HASH_MD5'?
 void ma_hash_free(MA_HASH_CTX *ctx);
                   ^~~~~~~~~~~
                   MA_HASH_MD5
include/ma_crypt.h:96:20: error: unknown type name 'MA_HASH_CTX'; did you mean 'MA_HASH_MD5'?
 void ma_hash_input(MA_HASH_CTX *ctx,
                    ^~~~~~~~~~~
                    MA_HASH_MD5
include/ma_crypt.h:108:21: error: unknown type name 'MA_HASH_CTX'; did you mean 'MA_HASH_MD5'?
 void ma_hash_result(MA_HASH_CTX *ctx, unsigned char *digest);
                     ^~~~~~~~~~~
                     MA_HASH_MD5
include/ma_crypt.h: In function 'ma_hash':
include/ma_crypt.h:155:3: error: unknown type name 'MA_HASH_CTX'; did you mean 'MA_HASH_MD5'?
   MA_HASH_CTX *ctx= NULL;
   ^~~~~~~~~~~
   MA_HASH_MD5
include/ma_crypt.h:160:8: warning: implicit declaration of function 'ma_hash_new'; did you mean 'ma_hash'? [-Wimplicit-function-declaration]
   ctx= ma_hash_new(algorithm, ctx);
        ^~~~~~~~~~~
        ma_hash
include/ma_crypt.h:160:6: warning: assignment to 'int *' from 'int' makes pointer from integer without a cast [-Wint-conversion]
   ctx= ma_hash_new(algorithm, ctx);
      ^
include/ma_crypt.h:161:3: warning: implicit declaration of function 'ma_hash_input'; did you mean 'ma_hash'? [-Wimplicit-function-declaration]
   ma_hash_input(ctx, buffer, buffer_length);
   ^~~~~~~~~~~~~
   ma_hash
include/ma_crypt.h:162:3: warning: implicit declaration of function 'ma_hash_result'; did you mean 'ma_hash'? [-Wimplicit-function-declaration]
   ma_hash_result(ctx, digest);
   ^~~~~~~~~~~~~~
   ma_hash
include/ma_crypt.h:163:3: warning: implicit declaration of function 'ma_hash_free'; did you mean 'ma_hash'? [-Wimplicit-function-declaration]
   ma_hash_free(ctx);
   ^~~~~~~~~~~~
   ma_hash
libmariadb/secure/openssl_crypt.c: At top level:
libmariadb/secure/openssl_crypt.c:21:10: fatal error: openssl/evp.h: No such file or directory
 #include <openssl/evp.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
ninja: build stopped: subcommand failed.
make[3]: *** [Makefile:183: /openwrt/build_dir/target-mips_24kc_musl/mariadb-connector-c-3.1.12-src/.built] Error 1
```
