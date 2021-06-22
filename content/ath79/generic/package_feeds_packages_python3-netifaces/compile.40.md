---
title: "compile.40"
date: 2021-06-22 10:50:44.052006
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
make package/feeds/packages/python3-netifaces/compile -j$(nproc) || make package/feeds/packages/python3-netifaces/compile V=s
```

#### Compile.txt

``` bash
running install
running build
running build_ext
checking for getifaddrs...found. 
checking for getnameinfo...found. 
checking for IPv6 socket IOCTLs...not found. 
checking for optional header files...netpacket/packet.h linux/atm.h linux/llc.h linux/tipc.h linux/dn.h. 
checking whether struct sockaddr has a length field...no. 
checking which sockaddr_xxx structs are defined...in in6 un ll atmpvc atmsvc dn llc. 
checking for routing socket support...no. 
checking for sysctl(CTL_NET...) support...no. 
checking for netlink support...yes. 
will use netlink to read routing table
building 'netifaces' extension
ccache_cc -Wno-unused-result -Wsign-compare -DNDEBUG -g -O3 -Wall -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/pypi/netifaces-0.10.9=netifaces-0.10.9 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -fPIC -DNETIFACES_VERSION=0.10.9 -DHAVE_GETIFADDRS=1 -DHAVE_GETNAMEINFO=1 -DHAVE_NETPACKET_PACKET_H=1 -DHAVE_LINUX_ATM_H=1 -DHAVE_LINUX_LLC_H=1 -DHAVE_LINUX_TIPC_H=1 -DHAVE_LINUX_DN_H=1 -DHAVE_SOCKADDR_IN=1 -DHAVE_SOCKADDR_IN6=1 -DHAVE_SOCKADDR_UN=1 -DHAVE_SOCKADDR_LL=1 -DHAVE_SOCKADDR_ATMPVC=1 -DHAVE_SOCKADDR_ATMSVC=1 -DHAVE_SOCKADDR_DN=1 -DHAVE_SOCKADDR_LLC=1 -DHAVE_PF_NETLINK=1 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -c netifaces.c -o build/temp.-3.9/netifaces.o
netifaces.c:1:10: fatal error: Python.h: No such file or directory
 #include <Python.h>
          ^~~~~~~~~~
compilation terminated.
error: command '/openwrt/staging_dir/host/bin/ccache_cc' failed with exit code 1
make[3]: *** [Makefile:44: /openwrt/build_dir/target-mips_24kc_musl/pypi/netifaces-0.10.9/.built] Error 1
```
