---
title: "compile.40"
date: 2021-06-22 10:46:12.832947
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
make package/feeds/packages/getdns/compile -j$(nproc) || make package/feeds/packages/getdns/compile V=s
```

#### Compile.txt

``` bash
-- The C compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Looking for assert.h
-- Looking for assert.h - found
-- Looking for inttypes.h
-- Looking for inttypes.h - found
-- Looking for limits.h
-- Looking for limits.h - found
-- Looking for sys/limits.h
-- Looking for sys/limits.h - not found
-- Looking for stdarg.h
-- Looking for stdarg.h - found
-- Looking for stdint.h
-- Looking for stdint.h - found
-- Looking for stdio.h
-- Looking for stdio.h - found
-- Looking for stdlib.h
-- Looking for stdlib.h - found
-- Looking for string.h
-- Looking for string.h - found
-- Looking for strings.h
-- Looking for strings.h - found
-- Looking for time.h
-- Looking for time.h - found
-- Looking for unistd.h
-- Looking for unistd.h - found
-- Looking for fcntl.h
-- Looking for fcntl.h - found
-- Looking for signal.h
-- Looking for signal.h - found
-- Looking for sys/poll.h
-- Looking for sys/poll.h - found
-- Looking for poll.h
-- Looking for poll.h - found
-- Looking for resource.h
-- Looking for resource.h - not found
-- Looking for sys/types.h
-- Looking for sys/types.h - found
-- Looking for sys/stat.h
-- Looking for sys/stat.h - found
-- Looking for endian.h
-- Looking for endian.h - found
-- Looking for netdb.h
-- Looking for netdb.h - found
-- Looking for arpa/inet.h
-- Looking for arpa/inet.h - found
-- Looking for netinet/in.h
-- Looking for netinet/in.h - found
-- Looking for sys/select.h
-- Looking for sys/select.h - found
-- Looking for sys/socket.h
-- Looking for sys/socket.h - found
-- Looking for sys/sysctl.h
-- Looking for sys/sysctl.h - not found
-- Looking for sys/time.h
-- Looking for sys/time.h - found
-- Looking for sys/wait.h
-- Looking for sys/wait.h - found
-- Looking for windows.h
-- Looking for windows.h - not found
-- Looking for winsock.h
-- Looking for winsock.h - not found
-- Looking for winsock2.h
-- Looking for winsock2.h - not found
-- Looking for ws2tcpip.h
-- Looking for ws2tcpip.h - not found
-- Looking for getentropy
-- Looking for getentropy - found
-- Looking for inet_pton
-- Looking for inet_pton - found
-- Looking for inet_ntop
-- Looking for inet_ntop - found
-- Looking for mkstemp
-- Looking for mkstemp - found
-- Looking for sigemptyset
-- Looking for sigemptyset - found
-- Looking for sigfillset
-- Looking for sigfillset - found
-- Looking for sigaddset
-- Looking for sigaddset - found
-- Looking for strptime
-- Looking for strptime - found
-- Looking for fcntl
-- Looking for fcntl - found
-- Looking for getauxval
-- Looking for getauxval - found
-- Looking for gettimeofday
-- Looking for gettimeofday - found
-- Looking for ioctlsocket
-- Looking for ioctlsocket - not found
-- Looking for sigemptyset
-- Looking for sigemptyset - found
-- Looking for sigfillset
-- Looking for sigfillset - found
-- Looking for sigaddset
-- Looking for sigaddset - found
-- Looking for strptime
-- Looking for strptime - found
-- Looking for stddef.h
-- Looking for stddef.h - found
-- Check size of sigset_t
-- Check size of sigset_t - done
-- Check size of _sigset_t
-- Check size of _sigset_t - failed
CMake Error at /openwrt/staging_dir/host/share/cmake-3.20/Modules/FindPackageHandleStandardArgs.cmake:230 (message):
  Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the
  system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY
  OPENSSL_INCLUDE_DIR) (Required is at least version "1.0.2")
Call Stack (most recent call first):
  /openwrt/staging_dir/host/share/cmake-3.20/Modules/FindPackageHandleStandardArgs.cmake:594 (_FPHSA_FAILURE_MESSAGE)
  /openwrt/staging_dir/host/share/cmake-3.20/Modules/FindOpenSSL.cmake:570 (find_package_handle_standard_args)
  CMakeLists.txt:328 (find_package)


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-mips_24kc_musl/getdns-1.7.0/CMakeFiles/CMakeOutput.log".
See also "/openwrt/build_dir/target-mips_24kc_musl/getdns-1.7.0/CMakeFiles/CMakeError.log".
make[3]: *** [Makefile:83: /openwrt/build_dir/target-mips_24kc_musl/getdns-1.7.0/.configured_0be367681993b9977e61dce544c71415] Error 1
```
