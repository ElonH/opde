---
title: "compile.37"
date: 2021-06-20 22:39:07.403936
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
make package/feeds/packages/emailrelay/compile -j$(nproc) || make package/feeds/packages/emailrelay/compile V=s
```

#### Compile.txt

``` bash
configure: loading site script /openwrt/include/site/mips
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether to enable maintainer-specific portions of Makefiles... no
checking for mips-openwrt-linux-cc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
checking whether ccache_cc understands -c and -o together... yes
checking for style of include used by make... GNU
checking dependency style of ccache_cc... gcc3
checking whether we are using the GNU C++ compiler... yes
checking whether ccache_cxx accepts -g... yes
checking dependency style of ccache_cxx... gcc3
checking whether ccache_cxx supports C++11 features with -std=gnu++11... yes
checking for mips-openwrt-linux-ranlib... mips-openwrt-linux-musl-gcc-ranlib
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for make... make
checking for ar... mips-openwrt-linux-musl-gcc-ar
checking for gzip... gzip
checking for doxygen... no
checking for man2html... no
checking for resource compiler... ccache_cxx -std=gnu++11
checking message compiler... ccache_cxx -std=gnu++11
checking for library containing gethostbyname... none required
checking for library containing connect... none required
checking how to run the C++ preprocessor... ccache_cxx -std=gnu++11 -E
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for ANSI C header files... yes
checking for sys/types.h... yes
checking for sys/stat.h... yes
checking for stdlib.h... yes
checking for string.h... yes
checking for memory.h... yes
checking for strings.h... yes
checking for inttypes.h... yes
checking for stdint.h... yes
checking for unistd.h... yes
checking for sys/types.h... (cached) yes
checking for sys/stat.h... (cached) yes
checking sys/wait.h usability... yes
checking sys/wait.h presence... yes
checking for sys/wait.h... yes
checking sys/mman.h usability... yes
checking sys/mman.h presence... yes
checking for sys/mman.h... yes
checking sys/select.h usability... yes
checking sys/select.h presence... yes
checking for sys/select.h... yes
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking sys/utsname.h usability... yes
checking sys/utsname.h presence... yes
checking for sys/utsname.h... yes
checking netdb.h usability... yes
checking netdb.h presence... yes
checking for netdb.h... yes
checking netinet/in.h usability... yes
checking netinet/in.h presence... yes
checking for netinet/in.h... yes
checking net/if.h usability... yes
checking net/if.h presence... yes
checking for net/if.h... yes
checking arpa/inet.h usability... yes
checking arpa/inet.h presence... yes
checking for arpa/inet.h... yes
checking for stdint.h... (cached) yes
checking for inttypes.h... (cached) yes
checking for unistd.h... (cached) yes
checking errno.h usability... yes
checking errno.h presence... yes
checking for errno.h... yes
checking pwd.h usability... yes
checking pwd.h presence... yes
checking for pwd.h... yes
checking grp.h usability... yes
checking grp.h presence... yes
checking for grp.h... yes
checking for socklen_t... yes
checking for errno_t... no
checking for ssize_t... yes
checking for uintptr_t... yes
checking for 'int64'... yes
checking for 'int32'... yes
checking for 'int16'... yes
checking for statbuf timespec... no
checking for statbuf nanoseconds... yes
checking for pid_t... yes
checking for uid_t... yes
checking for gid_t... yes
checking for c++ nullptr... yes
checking for c++ constexpr... yes
checking for c++ class enums... yes
checking for c++ noexcept... yes
checking for c++ override... yes
checking for c++ final keyword... yes
checking for c++ type_traits... yes
checking for c++ emplace_back and friends... yes
checking for c++ std::align... yes
checking for c++ std::move... yes
checking for c++ std::shared_ptr and friends... yes
checking for c++ std::make_unique... no
checking for c++ std::thread without -pthread... yes
checking for c++ std::thread at runtime... yes
checking for c++ std::wstring... yes
checking for c++ eq delete... yes
checking for c++ eq default... yes
checking for c++ initializer_list... yes
checking for ipv6... yes
checking for sin6_len... no
checking for inet_ntop()... yes
checking for inet_pton()... yes
checking for epoll... yes
checking for rtnetlink... yes
checking for routing sockets... no
checking for if_nametoindex()... yes
checking for ConvertInterfaceNameToLuid()... no
checking for gai_strerror()... yes
checking for getpwnam... yes
checking for getpwnam_r... yes
checking for getgrnam... yes
checking for getgrnam_r... yes
checking for gmtime_r... yes
checking for gmtime_s... no
checking for localtime_r... yes
checking for localtime_s... no
checking for strncpy_s... no
checking for getenv_s... no
checking for putenv_s... no
checking for _fsopen()... no
checking for _sopen()... no
checking for _sopen_s()... no
checking for extended fstream open... no
checking for readlink... yes
checking for proc_pidpath... no
checking for bsd setpgrp... no
checking for setgroups... yes
checking for execvpe... yes
checking for sigprocmask... yes
checking for pthread_sigmask... yes
checking for windows CreateWaitableTimerEx... no
checking for windows CreateEventEx... no
checking for windows InitCommonControlsEx... no
checking pkg-config is at least version 0.9.0... yes
checking for QT... no
configure: no QT 5 pkg-config
checking for moc... no
checking for openssl... no
checking for mbedtls... yes
checking pkg-config is at least version 0.9.0... yes
configure: error: cannot use --with-openssl: openssl is not available: check config.log and try setting CPPFLAGS
make[3]: *** [Makefile:120: /openwrt/build_dir/target-mips_24kc_musl/emailrelay-2.2/.configured_c35e918dcf72f9336574efdc2f1226c4] Error 1
```
