---
title: "compile.40"
date: 2021-06-22 10:47:21.990684
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
make package/feeds/packages/libssh/compile -j$(nproc) || make package/feeds/packages/libssh/compile V=s
```

#### Compile.txt

``` bash
-- The C compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Performing Test REQUIRED_FLAGS_WERROR
-- Performing Test REQUIRED_FLAGS_WERROR - Success
-- Performing Test WITH_STD_GNU99_FLAG
-- Performing Test WITH_STD_GNU99_FLAG - Success
-- Performing Test WITH_WPEDANTIC_FLAG
-- Performing Test WITH_WPEDANTIC_FLAG - Success
-- Performing Test WITH_WALL_FLAG
-- Performing Test WITH_WALL_FLAG - Success
-- Performing Test WITH_WSHADOW_FLAG
-- Performing Test WITH_WSHADOW_FLAG - Success
-- Performing Test WITH_WMISSING_PROTOTYPES_FLAG
-- Performing Test WITH_WMISSING_PROTOTYPES_FLAG - Success
-- Performing Test WITH_WCAST_ALIGN_FLAG
-- Performing Test WITH_WCAST_ALIGN_FLAG - Success
-- Performing Test WITH_WERROR_ADDRESS_FLAG
-- Performing Test WITH_WERROR_ADDRESS_FLAG - Success
-- Performing Test WITH_WSTRICT_PROTOTYPES_FLAG
-- Performing Test WITH_WSTRICT_PROTOTYPES_FLAG - Success
-- Performing Test WITH_WERROR_STRICT_PROTOTYPES_FLAG
-- Performing Test WITH_WERROR_STRICT_PROTOTYPES_FLAG - Success
-- Performing Test WITH_WWRITE_STRINGS_FLAG
-- Performing Test WITH_WWRITE_STRINGS_FLAG - Success
-- Performing Test WITH_WERROR_WRITE_STRINGS_FLAG
-- Performing Test WITH_WERROR_WRITE_STRINGS_FLAG - Success
-- Performing Test WITH_WERROR_IMPLICIT_FUNCTION_DECLARATION_FLAG
-- Performing Test WITH_WERROR_IMPLICIT_FUNCTION_DECLARATION_FLAG - Success
-- Performing Test WITH_WPOINTER_ARITH_FLAG
-- Performing Test WITH_WPOINTER_ARITH_FLAG - Success
-- Performing Test WITH_WERROR_POINTER_ARITH_FLAG
-- Performing Test WITH_WERROR_POINTER_ARITH_FLAG - Success
-- Performing Test WITH_WDECLARATION_AFTER_STATEMENT_FLAG
-- Performing Test WITH_WDECLARATION_AFTER_STATEMENT_FLAG - Success
-- Performing Test WITH_WERROR_DECLARATION_AFTER_STATEMENT_FLAG
-- Performing Test WITH_WERROR_DECLARATION_AFTER_STATEMENT_FLAG - Success
-- Performing Test WITH_WRETURN_TYPE_FLAG
-- Performing Test WITH_WRETURN_TYPE_FLAG - Success
-- Performing Test WITH_WERROR_RETURN_TYPE_FLAG
-- Performing Test WITH_WERROR_RETURN_TYPE_FLAG - Success
-- Performing Test WITH_WUNINITIALIZED_FLAG
-- Performing Test WITH_WUNINITIALIZED_FLAG - Success
-- Performing Test WITH_WERROR_UNINITIALIZED_FLAG
-- Performing Test WITH_WERROR_UNINITIALIZED_FLAG - Success
-- Performing Test WITH_WIMPLICIT_FALLTHROUGH_FLAG
-- Performing Test WITH_WIMPLICIT_FALLTHROUGH_FLAG - Success
-- Performing Test WITH_WERROR_STRICT_OVERFLOW_FLAG
-- Performing Test WITH_WERROR_STRICT_OVERFLOW_FLAG - Success
-- Performing Test WITH_WSTRICT_OVERFLOW_2_FLAG
-- Performing Test WITH_WSTRICT_OVERFLOW_2_FLAG - Success
-- Performing Test WITH_WNO_FORMAT_ZERO_LENGTH_FLAG
-- Performing Test WITH_WNO_FORMAT_ZERO_LENGTH_FLAG - Success
-- Performing Test WITH_WMISSING_FIELD_INITIALIZERS_FLAG
-- Performing Test WITH_WMISSING_FIELD_INITIALIZERS_FLAG - Success
-- Performing Test WITH_WSIGN_COMPARE_FLAG
-- Performing Test WITH_WSIGN_COMPARE_FLAG - Success
-- Performing Test REQUIRED_FLAGS_WFORMAT
-- Performing Test REQUIRED_FLAGS_WFORMAT - Success
-- Performing Test WITH_WFORMAT_SECURITY_FLAG
-- Performing Test WITH_WFORMAT_SECURITY_FLAG - Success
-- Performing Test WITH_WERROR_FORMAT_SECURITY_FLAG
-- Performing Test WITH_WERROR_FORMAT_SECURITY_FLAG - Success
-- Performing Test WITH_FNO_COMMON_FLAG
-- Performing Test WITH_FNO_COMMON_FLAG - Success
-- Performing Test WITH_WNO_DEPRECATED_DECLARATIONS_FLAG
-- Performing Test WITH_WNO_DEPRECATED_DECLARATIONS_FLAG - Success
-- Found ZLIB: /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libz.so (found version "1.2.11") 
-- Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY OPENSSL_INCLUDE_DIR) 
-- Found GCrypt: /openwrt/staging_dir/target-mips_24kc_musl/usr/include (found version "1.9.3") 
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
-- Found PythonInterp: /openwrt/staging_dir/host/bin/python (found version "3.8.5") 
-- Could not find `abimap` in PATH. It can be found in PyPI as `abimap` (try `pip install abimap`)
-- Could NOT find ABIMap (missing: ABIMAP_EXECUTABLE) (Required is at least version "0.3.1")
-- Performing Test WITH_VISIBILITY_HIDDEN
-- Performing Test WITH_VISIBILITY_HIDDEN - Success
-- Looking for argp.h
-- Looking for argp.h - found
-- Looking for pty.h
-- Looking for pty.h - found
-- Looking for utmp.h
-- Looking for utmp.h - found
-- Looking for unistd.h
-- Looking for unistd.h - found
-- Looking for stdint.h
-- Looking for stdint.h - found
-- Looking for util.h
-- Looking for util.h - not found
-- Looking for libutil.h
-- Looking for libutil.h - not found
-- Looking for sys/time.h
-- Looking for sys/time.h - found
-- Looking for sys/utime.h
-- Looking for sys/utime.h - not found
-- Looking for sys/param.h
-- Looking for sys/param.h - found
-- Looking for arpa/inet.h
-- Looking for arpa/inet.h - found
-- Looking for byteswap.h
-- Looking for byteswap.h - found
-- Looking for glob.h
-- Looking for glob.h - found
-- Looking for valgrind/valgrind.h
-- Looking for valgrind/valgrind.h - not found
-- Looking for isblank
-- Looking for isblank - found
-- Looking for strncpy
-- Looking for strncpy - found
-- Looking for strndup
-- Looking for strndup - found
-- Looking for explicit_bzero
-- Looking for explicit_bzero - found
-- Looking for memset_s
-- Looking for memset_s - not found
-- Performing Test HAVE_GLOB_GL_FLAGS_MEMBER
-- Performing Test HAVE_GLOB_GL_FLAGS_MEMBER - Failed
-- Looking for glob
-- Looking for glob - found
-- Looking for vsnprintf
-- Looking for vsnprintf - found
-- Looking for snprintf
-- Looking for snprintf - found
-- Looking for poll
-- Looking for poll - found
-- Looking for select
-- Looking for select - found
-- Looking for ntohll
-- Looking for ntohll - not found
-- Looking for htonll
-- Looking for htonll - not found
-- Looking for clock_gettime in rt
-- Looking for clock_gettime in rt - found
-- Looking for forkpty in util
-- Looking for forkpty in util - found
-- Looking for cfmakeraw
-- Looking for cfmakeraw - found
-- Looking for __strtoull
-- Looking for __strtoull - not found
-- Performing Test HAVE_GCC_THREAD_LOCAL_STORAGE
-- Performing Test HAVE_GCC_THREAD_LOCAL_STORAGE - Success
-- Performing Test HAVE_MSC_THREAD_LOCAL_STORAGE
-- Performing Test HAVE_MSC_THREAD_LOCAL_STORAGE - Failed
-- Performing Test HAVE_CONSTRUCTOR_ATTRIBUTE
-- Performing Test HAVE_CONSTRUCTOR_ATTRIBUTE - Success
-- Performing Test HAVE_DESTRUCTOR_ATTRIBUTE
-- Performing Test HAVE_DESTRUCTOR_ATTRIBUTE - Success
-- Performing Test HAVE_FALLTHROUGH_ATTRIBUTE
-- Performing Test HAVE_FALLTHROUGH_ATTRIBUTE - Success
-- Performing Test HAVE_UNUSED_ATTRIBUTE
-- Performing Test HAVE_UNUSED_ATTRIBUTE - Success
-- Performing Test HAVE_GCC_VOLATILE_MEMORY_PROTECTION
-- Performing Test HAVE_GCC_VOLATILE_MEMORY_PROTECTION - Success
-- Performing Test HAVE_COMPILER__FUNC__
-- Performing Test HAVE_COMPILER__FUNC__ - Success
-- Performing Test HAVE_COMPILER__FUNCTION__
-- Performing Test HAVE_COMPILER__FUNCTION__ - Success
-- Performing Test HAVE_LD_VERSION_SCRIPT
-- Performing Test HAVE_LD_VERSION_SCRIPT - Success
-- Could NOT find Doxygen (missing: DOXYGEN_EXECUTABLE) 
-- Threads_FOUND=TRUE
-- ********************************************
-- ********** libssh build options : **********
-- zlib support: ON
-- libgcrypt support: OFF
-- libmbedTLS support: OFF
-- libnacl support: OFF
-- SFTP support: ON
-- Server support : ON
-- GSSAPI support : OFF
-- GEX support : ON
-- Pcap debugging support : OFF
-- Build shared library: ON
-- Unit testing: OFF
-- Client code testing: OFF
-- Blowfish cipher support: OFF
-- Server code testing: OFF
-- Public API documentation generation
-- Benchmarks: OFF
-- Symbol versioning: ON
-- Allow ABI break: OFF
-- Release is final: 
-- Global client config: /etc/ssh/ssh_config
-- Global bind config: /etc/ssh/libssh_server_config
-- ********************************************
-- Configuring done
-- Generating done
CMake Warning:
  Manually-specified variables were not used by the project:

    CMAKE_ASM_COMPILER
    CMAKE_ASM_COMPILER_LAUNCHER
    CMAKE_CXX_COMPILER
    CMAKE_CXX_FLAGS_RELEASE
    CMAKE_EXPORT_NO_PACKAGE_REGISTRY
    CMAKE_EXPORT_PACKAGE_REGISTRY
    CMAKE_FIND_PACKAGE_NO_PACKAGE_REGISTRY
    CMAKE_FIND_PACKAGE_NO_SYSTEM_PACKAGE_REGISTRY
    CMAKE_MODULE_LINKER_FLAGS
    DL_LIBRARY
    HAVE_WORDS_BIGENDIAN


-- Build files have been written to: /openwrt/build_dir/target-mips_24kc_musl/libssh-0.9.5/build
ninja: Entering directory `/openwrt/build_dir/target-mips_24kc_musl/libssh-0.9.5/build'
[1/71] Building C object src/CMakeFiles/ssh.dir/agent.c.o
[2/71] Building C object src/CMakeFiles/ssh.dir/auth.c.o
[3/71] Building C object src/CMakeFiles/ssh.dir/base64.c.o
[4/71] Building C object src/CMakeFiles/ssh.dir/bignum.c.o
[5/71] Building C object src/CMakeFiles/ssh.dir/buffer.c.o
[6/71] Building C object src/CMakeFiles/ssh.dir/callbacks.c.o
[7/71] Building C object src/CMakeFiles/ssh.dir/channels.c.o
[8/71] Building C object src/CMakeFiles/ssh.dir/client.c.o
[9/71] Building C object src/CMakeFiles/ssh.dir/config.c.o
[10/71] Building C object src/CMakeFiles/ssh.dir/connect.c.o
[11/71] Building C object src/CMakeFiles/ssh.dir/connector.c.o
[12/71] Building C object src/CMakeFiles/ssh.dir/curve25519.c.o
[13/71] Building C object src/CMakeFiles/ssh.dir/dh.c.o
[14/71] Building C object src/CMakeFiles/ssh.dir/ecdh.c.o
[15/71] Building C object src/CMakeFiles/ssh.dir/error.c.o
[16/71] Building C object src/CMakeFiles/ssh.dir/getpass.c.o
[17/71] Building C object src/CMakeFiles/ssh.dir/init.c.o
[18/71] Building C object src/CMakeFiles/ssh.dir/kdf.c.o
[19/71] Building C object src/CMakeFiles/ssh.dir/kex.c.o
[20/71] Building C object src/CMakeFiles/ssh.dir/known_hosts.c.o
[21/71] Building C object src/CMakeFiles/ssh.dir/knownhosts.c.o
[22/71] Building C object src/CMakeFiles/ssh.dir/legacy.c.o
[23/71] Building C object src/CMakeFiles/ssh.dir/log.c.o
[24/71] Building C object src/CMakeFiles/ssh.dir/match.c.o
[25/71] Building C object src/CMakeFiles/ssh.dir/messages.c.o
[26/71] Building C object src/CMakeFiles/ssh.dir/misc.c.o
[27/71] Building C object src/CMakeFiles/ssh.dir/options.c.o
[28/71] Building C object src/CMakeFiles/ssh.dir/packet.c.o
[29/71] Building C object src/CMakeFiles/ssh.dir/packet_cb.c.o
[30/71] Building C object src/CMakeFiles/ssh.dir/packet_crypt.c.o
[31/71] Building C object src/CMakeFiles/ssh.dir/pcap.c.o
[32/71] Building C object src/CMakeFiles/ssh.dir/pki.c.o
[33/71] Building C object src/CMakeFiles/ssh.dir/pki_container_openssh.c.o
[34/71] Building C object src/CMakeFiles/ssh.dir/poll.c.o
[35/71] Building C object src/CMakeFiles/ssh.dir/session.c.o
[36/71] Building C object src/CMakeFiles/ssh.dir/scp.c.o
[37/71] Building C object src/CMakeFiles/ssh.dir/socket.c.o
[38/71] Building C object src/CMakeFiles/ssh.dir/string.c.o
[39/71] Building C object src/CMakeFiles/ssh.dir/threads.c.o
[40/71] Building C object src/CMakeFiles/ssh.dir/wrapper.c.o
[41/71] Building C object src/CMakeFiles/ssh.dir/external/bcrypt_pbkdf.c.o
[42/71] Building C object src/CMakeFiles/ssh.dir/external/blowfish.c.o
[43/71] Building C object src/CMakeFiles/ssh.dir/external/chacha.c.o
[44/71] Building C object src/CMakeFiles/ssh.dir/external/poly1305.c.o
[45/71] Building C object src/CMakeFiles/ssh.dir/chachapoly.c.o
[46/71] Building C object src/CMakeFiles/ssh.dir/config_parser.c.o
[47/71] Building C object src/CMakeFiles/ssh.dir/token.c.o
[48/71] Building C object src/CMakeFiles/ssh.dir/pki_ed25519_common.c.o
[49/71] Building C object src/CMakeFiles/ssh.dir/threads/noop.c.o
[50/71] Building C object src/CMakeFiles/ssh.dir/threads/pthread.c.o
[51/71] Building C object src/CMakeFiles/ssh.dir/threads/libcrypto.c.o
FAILED: src/CMakeFiles/ssh.dir/threads/libcrypto.c.o 
/openwrt/staging_dir/host/bin/ccache /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc -DLIBSSH_EXPORTS -Isrc -I../src -I../include -Iinclude -I. -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libssh-0.9.5=libssh-0.9.5 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DNDEBUG -fPIC -fvisibility=hidden -std=gnu99 -Wpedantic -Wall -Wshadow -Wmissing-prototypes -Wcast-align -Werror=address -Wstrict-prototypes -Werror=strict-prototypes -Wwrite-strings -Werror=write-strings -Werror-implicit-function-declaration -Wpointer-arith -Werror=pointer-arith -Wdeclaration-after-statement -Werror=declaration-after-statement -Wreturn-type -Werror=return-type -Wuninitialized -Werror=uninitialized -Wimplicit-fallthrough -Werror=strict-overflow -Wstrict-overflow=2 -Wno-format-zero-length -Wmissing-field-initializers -Wsign-compare -Wformat -Wformat-security -Werror=format-security -fno-common -D_GNU_SOURCE -MD -MT src/CMakeFiles/ssh.dir/threads/libcrypto.c.o -MF src/CMakeFiles/ssh.dir/threads/libcrypto.c.o.d -o src/CMakeFiles/ssh.dir/threads/libcrypto.c.o -c ../src/threads/libcrypto.c
../src/threads/libcrypto.c: In function 'libcrypto_lock_callback':
../src/threads/libcrypto.c:53:16: error: 'CRYPTO_LOCK' undeclared (first use in this function)
     if (mode & CRYPTO_LOCK) {
                ^~~~~~~~~~~
../src/threads/libcrypto.c:53:16: note: each undeclared identifier is reported only once for each function it appears in
../src/threads/libcrypto.c: In function 'crypto_thread_init':
../src/threads/libcrypto.c:71:13: error: implicit declaration of function 'CRYPTO_num_locks' [-Werror=implicit-function-declaration]
     int n = CRYPTO_num_locks();
             ^~~~~~~~~~~~~~~~
../src/threads/libcrypto.c:102:5: error: implicit declaration of function 'CRYPTO_set_id_callback'; did you mean 'ssh_set_log_callback'? [-Werror=implicit-function-declaration]
     CRYPTO_set_id_callback(user_callbacks->thread_id);
     ^~~~~~~~~~~~~~~~~~~~~~
     ssh_set_log_callback
../src/threads/libcrypto.c:105:5: error: implicit declaration of function 'CRYPTO_set_locking_callback'; did you mean 'ssh_set_log_callback'? [-Werror=implicit-function-declaration]
     CRYPTO_set_locking_callback(libcrypto_lock_callback);
     ^~~~~~~~~~~~~~~~~~~~~~~~~~~
     ssh_set_log_callback
cc1: some warnings being treated as errors
ninja: build stopped: subcommand failed.
make[3]: *** [Makefile:71: /openwrt/build_dir/target-mips_24kc_musl/libssh-0.9.5/.built] Error 1
```
