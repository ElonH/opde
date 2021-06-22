---
title: "compile.40"
date: 2021-06-22 10:51:50.605077
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
make package/feeds/packages/xupnpd/compile -j$(nproc) || make package/feeds/packages/xupnpd/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/100-default_config.patch using plaintext: 
patching file src/xupnpd.lua

Applying ./patches/101-root_dir_param.patch using plaintext: 
patching file src/main.cpp
Reading specs from /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/specs
COLLECT_GCC=/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc
COLLECT_LTO_WRAPPER=/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/libexec/gcc/mips-openwrt-linux-musl/8.4.0/lto-wrapper
Target: mips-openwrt-linux-musl
Configured with: /openwrt/build_dir/toolchain-mips_24kc_gcc-8.4.0_musl/gcc-8.4.0/configure --with-bugurl=http://bugs.openwrt.org/ --with-pkgversion='OpenWrt GCC 8.4.0 r0-d97b735' --prefix=/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl --build=x86_64-pc-linux-gnu --host=x86_64-pc-linux-gnu --target=mips-openwrt-linux-musl --with-gnu-ld --enable-target-optspace --disable-libgomp --disable-libmudflap --disable-multilib --disable-libmpx --disable-nls --disable-libssp --without-isl --without-cloog --with-host-libstdcxx=-lstdc++ --with-float=soft --with-gmp=/openwrt/staging_dir/host --with-mpfr=/openwrt/staging_dir/host --with-mpc=/openwrt/staging_dir/host --disable-decimal-float --with-diagnostics-color=auto-if-env --enable-__cxa_atexit --disable-libstdcxx-dual-abi --with-default-libstdcxx-abi=new --with-mips-plt --with-headers=/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include --enable-languages=c,c++ --enable-shared --enable-threads --with-slibdir=/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib --enable-lto --with-libelf=/openwrt/staging_dir/host --disable-libsanitizer
Thread model: posix
gcc version 8.4.0 (OpenWrt GCC 8.4.0 r0-d97b735) 
COLLECT_GCC_OPTIONS='-v' '-Os' '-pipe' '-mno-branch-likely' '-mips32r2' '-mtune=24kc' '-fno-caller-saves' '-fno-plt' '-fhonour-copts' '-Wno-error=unused-but-set-variable' '-Wno-error=unused-result' '-msoft-float' '-mips16' '-minterlink-mips16' '-fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950=xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950' '-Wformat=1' '-Werror=format-security' '-fstack-protector' '-D' '_FORTIFY_SOURCE=1' '-fno-exceptions' '-fno-rtti' '-D' 'WITH_URANDOM' '-I' '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include' '-I' '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify' '-I' '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include' '-L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib' '-L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib' '-z' 'now' '-z' 'relro' '-o' 'xupnpd' '-mllsc' '-mplt' '-mno-shared' '-EB' '-mabi=32'
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/libexec/gcc/mips-openwrt-linux-musl/8.4.0/cc1 -quiet -v -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -idirafter /openwrt/staging_dir/target-mips_24kc_musl/usr/include -D _FORTIFY_SOURCE=1 -D WITH_URANDOM md5c.c -meb -quiet -dumpbase md5c.c -mno-branch-likely -mips32r2 -mtune=24kc -msoft-float -mips16 -minterlink-mips16 -mllsc -mplt -mno-shared -mabi=32 -auxbase md5c -Os -Wno-error=unused-but-set-variable -Wno-error=unused-result -Wformat=1 -Werror=format-security -version -fno-caller-saves -fno-plt -fhonour-copts -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950=xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950 -fstack-protector -fno-exceptions -fno-rtti -o - |
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/as -v -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -EB -mips32r2 -mips16 -O2 -mabi=32 -mno-shared -mtune=24kc -msoft-float -call_nonpic -o /openwrt/tmp/cc4DmvPz.o
cc1: warning: command line option '-fno-rtti' is valid for C++/ObjC++ but not for C
GNU C17 (OpenWrt GCC 8.4.0 r0-d97b735) version 8.4.0 (mips-openwrt-linux-musl)
	compiled by GNU C version 9.3.0, GMP version 6.2.1, MPFR version 4.1.0, MPC version 1.2.1, isl version none
GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
ignoring duplicate directory "/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include"
  as it is a non-system directory that duplicates a system directory
#include "..." search starts here:
#include <...> search starts here:
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/sys-include
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/include
 /openwrt/staging_dir/target-mips_24kc_musl/usr/include
End of search list.
GNU C17 (OpenWrt GCC 8.4.0 r0-d97b735) version 8.4.0 (mips-openwrt-linux-musl)
	compiled by GNU C version 9.3.0, GMP version 6.2.1, MPFR version 4.1.0, MPC version 1.2.1, isl version none
GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
Compiler executable checksum: c2e009f41fe8e287a2e5fad0d03624ab
GNU assembler version 2.34 (mips-openwrt-linux-musl) using BFD version (GNU Binutils) 2.34
COLLECT_GCC_OPTIONS='-v' '-Os' '-pipe' '-mno-branch-likely' '-mips32r2' '-mtune=24kc' '-fno-caller-saves' '-fno-plt' '-fhonour-copts' '-Wno-error=unused-but-set-variable' '-Wno-error=unused-result' '-msoft-float' '-mips16' '-minterlink-mips16' '-fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950=xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950' '-Wformat=1' '-Werror=format-security' '-fstack-protector' '-D' '_FORTIFY_SOURCE=1' '-fno-exceptions' '-fno-rtti' '-D' 'WITH_URANDOM' '-I' '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include' '-I' '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify' '-I' '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include' '-L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib' '-L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib' '-z' 'now' '-z' 'relro' '-o' 'xupnpd' '-mllsc' '-mplt' '-mno-shared' '-EB' '-mabi=32'
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/libexec/gcc/mips-openwrt-linux-musl/8.4.0/cc1plus -quiet -v -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -D_GNU_SOURCE -idirafter /openwrt/staging_dir/target-mips_24kc_musl/usr/include -D _FORTIFY_SOURCE=1 -D WITH_URANDOM luajson.cpp -meb -quiet -dumpbase luajson.cpp -mno-branch-likely -mips32r2 -mtune=24kc -msoft-float -mips16 -minterlink-mips16 -mllsc -mplt -mno-shared -mabi=32 -auxbase luajson -Os -Wno-error=unused-but-set-variable -Wno-error=unused-result -Wformat=1 -Werror=format-security -version -fno-caller-saves -fno-plt -fhonour-copts -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950=xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950 -fstack-protector -fno-exceptions -fno-rtti -o - |
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/as -v -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -EB -mips32r2 -mips16 -O2 -mabi=32 -mno-shared -mtune=24kc -msoft-float -call_nonpic -o /openwrt/tmp/ccZYHoEA.o
GNU C++14 (OpenWrt GCC 8.4.0 r0-d97b735) version 8.4.0 (mips-openwrt-linux-musl)
	compiled by GNU C version 9.3.0, GMP version 6.2.1, MPFR version 4.1.0, MPC version 1.2.1, isl version none
GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
ignoring duplicate directory "/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include"
  as it is a non-system directory that duplicates a system directory
#include "..." search starts here:
#include <...> search starts here:
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include/c++/8.4.0
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include/c++/8.4.0/mips-openwrt-linux-musl
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include/c++/8.4.0/backward
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/sys-include
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/include
 /openwrt/staging_dir/target-mips_24kc_musl/usr/include
End of search list.
GNU C++14 (OpenWrt GCC 8.4.0 r0-d97b735) version 8.4.0 (mips-openwrt-linux-musl)
	compiled by GNU C version 9.3.0, GMP version 6.2.1, MPFR version 4.1.0, MPC version 1.2.1, isl version none
GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
Compiler executable checksum: GNU assembler version 2.34 (mips-openwrt-linux-musl) using BFD version (GNU Binutils) 2.34
c0f11eb4d5bf754b309699d9f82760c8
COLLECT_GCC_OPTIONS='-v' '-Os' '-pipe' '-mno-branch-likely' '-mips32r2' '-mtune=24kc' '-fno-caller-saves' '-fno-plt' '-fhonour-copts' '-Wno-error=unused-but-set-variable' '-Wno-error=unused-result' '-msoft-float' '-mips16' '-minterlink-mips16' '-fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950=xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950' '-Wformat=1' '-Werror=format-security' '-fstack-protector' '-D' '_FORTIFY_SOURCE=1' '-fno-exceptions' '-fno-rtti' '-D' 'WITH_URANDOM' '-I' '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include' '-I' '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify' '-I' '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include' '-L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib' '-L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib' '-z' 'now' '-z' 'relro' '-o' 'xupnpd' '-mllsc' '-mplt' '-mno-shared' '-EB' '-mabi=32'
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/libexec/gcc/mips-openwrt-linux-musl/8.4.0/cc1plus -quiet -v -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -D_GNU_SOURCE -idirafter /openwrt/staging_dir/target-mips_24kc_musl/usr/include -D _FORTIFY_SOURCE=1 -D WITH_URANDOM luajson_parser.cpp -meb -quiet -dumpbase luajson_parser.cpp -mno-branch-likely -mips32r2 -mtune=24kc -msoft-float -mips16 -minterlink-mips16 -mllsc -mplt -mno-shared -mabi=32 -auxbase luajson_parser -Os -Wno-error=unused-but-set-variable -Wno-error=unused-result -Wformat=1 -Werror=format-security -version -fno-caller-saves -fno-plt -fhonour-copts -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950=xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950 -fstack-protector -fno-exceptions -fno-rtti -o - |
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/as -v -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -EB -mips32r2 -mips16 -O2 -mabi=32 -mno-shared -mtune=24kc -msoft-float -call_nonpic -o /openwrt/tmp/cclVMLty.o
GNU C++14 (OpenWrt GCC 8.4.0 r0-d97b735) version 8.4.0 (mips-openwrt-linux-musl)
	compiled by GNU C version 9.3.0, GMP version 6.2.1, MPFR version 4.1.0, MPC version 1.2.1, isl version none
GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
ignoring duplicate directory "/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include"
  as it is a non-system directory that duplicates a system directory
#include "..." search starts here:
#include <...> search starts here:
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include/c++/8.4.0
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include/c++/8.4.0/mips-openwrt-linux-musl
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include/c++/8.4.0/backward
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/sys-include
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/include
 /openwrt/staging_dir/target-mips_24kc_musl/usr/include
End of search list.
GNU C++14 (OpenWrt GCC 8.4.0 r0-d97b735) version 8.4.0 (mips-openwrt-linux-musl)
	compiled by GNU C version 9.3.0, GMP version 6.2.1, MPFR version 4.1.0, MPC version 1.2.1, isl version none
GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
Compiler executable checksum: c0f11eb4d5bf754b309699d9f82760c8
GNU assembler version 2.34 (mips-openwrt-linux-musl) using BFD version (GNU Binutils) 2.34
COLLECT_GCC_OPTIONS='-v' '-Os' '-pipe' '-mno-branch-likely' '-mips32r2' '-mtune=24kc' '-fno-caller-saves' '-fno-plt' '-fhonour-copts' '-Wno-error=unused-but-set-variable' '-Wno-error=unused-result' '-msoft-float' '-mips16' '-minterlink-mips16' '-fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950=xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950' '-Wformat=1' '-Werror=format-security' '-fstack-protector' '-D' '_FORTIFY_SOURCE=1' '-fno-exceptions' '-fno-rtti' '-D' 'WITH_URANDOM' '-I' '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include' '-I' '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify' '-I' '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include' '-L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib' '-L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib' '-z' 'now' '-z' 'relro' '-o' 'xupnpd' '-mllsc' '-mplt' '-mno-shared' '-EB' '-mabi=32'
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/libexec/gcc/mips-openwrt-linux-musl/8.4.0/cc1plus -quiet -v -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -D_GNU_SOURCE -idirafter /openwrt/staging_dir/target-mips_24kc_musl/usr/include -D _FORTIFY_SOURCE=1 -D WITH_URANDOM luaxcore.cpp -meb -quiet -dumpbase luaxcore.cpp -mno-branch-likely -mips32r2 -mtune=24kc -msoft-float -mips16 -minterlink-mips16 -mllsc -mplt -mno-shared -mabi=32 -auxbase luaxcore -Os -Wno-error=unused-but-set-variable -Wno-error=unused-result -Wformat=1 -Werror=format-security -version -fno-caller-saves -fno-plt -fhonour-copts -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950=xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950 -fstack-protector -fno-exceptions -fno-rtti -o - |
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/as -v -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -EB -mips32r2 -mips16 -O2 -mabi=32 -mno-shared -mtune=24kc -msoft-float -call_nonpic -o /openwrt/tmp/ccnYDz0A.o
GNU C++14 (OpenWrt GCC 8.4.0 r0-d97b735) version 8.4.0 (mips-openwrt-linux-musl)
	compiled by GNU C version 9.3.0, GMP version 6.2.1, MPFR version 4.1.0, MPC version 1.2.1, isl version none
GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
ignoring duplicate directory "/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include"
  as it is a non-system directory that duplicates a system directory
#include "..." search starts here:
#include <...> search starts here:
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include/c++/8.4.0
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include/c++/8.4.0/mips-openwrt-linux-musl
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include/c++/8.4.0/backward
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/sys-include
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/include
 /openwrt/staging_dir/target-mips_24kc_musl/usr/include
End of search list.
GNU C++14 (OpenWrt GCC 8.4.0 r0-d97b735) version 8.4.0 (mips-openwrt-linux-musl)
	compiled by GNU C version 9.3.0, GMP version 6.2.1, MPFR version 4.1.0, MPC version 1.2.1, isl version none
GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
Compiler executable checksum: GNU assembler version 2.34 (mips-openwrt-linux-musl) using BFD version (GNU Binutils) 2.34
c0f11eb4d5bf754b309699d9f82760c8
luaxcore.cpp:32:10: fatal error: openssl/ssl.h: No such file or directory
 #include "openssl/ssl.h"
          ^~~~~~~~~~~~~~~
compilation terminated.
COLLECT_GCC_OPTIONS='-v' '-Os' '-pipe' '-mno-branch-likely' '-mips32r2' '-mtune=24kc' '-fno-caller-saves' '-fno-plt' '-fhonour-copts' '-Wno-error=unused-but-set-variable' '-Wno-error=unused-result' '-msoft-float' '-mips16' '-minterlink-mips16' '-fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950=xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950' '-Wformat=1' '-Werror=format-security' '-fstack-protector' '-D' '_FORTIFY_SOURCE=1' '-fno-exceptions' '-fno-rtti' '-D' 'WITH_URANDOM' '-I' '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include' '-I' '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify' '-I' '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include' '-L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib' '-L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib' '-z' 'now' '-z' 'relro' '-o' 'xupnpd' '-mllsc' '-mplt' '-mno-shared' '-EB' '-mabi=32'
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/libexec/gcc/mips-openwrt-linux-musl/8.4.0/cc1plus -quiet -v -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -D_GNU_SOURCE -idirafter /openwrt/staging_dir/target-mips_24kc_musl/usr/include -D _FORTIFY_SOURCE=1 -D WITH_URANDOM luaxlib.cpp -meb -quiet -dumpbase luaxlib.cpp -mno-branch-likely -mips32r2 -mtune=24kc -msoft-float -mips16 -minterlink-mips16 -mllsc -mplt -mno-shared -mabi=32 -auxbase luaxlib -Os -Wno-error=unused-but-set-variable -Wno-error=unused-result -Wformat=1 -Werror=format-security -version -fno-caller-saves -fno-plt -fhonour-copts -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950=xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950 -fstack-protector -fno-exceptions -fno-rtti -o - |
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/as -v -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -EB -mips32r2 -mips16 -O2 -mabi=32 -mno-shared -mtune=24kc -msoft-float -call_nonpic -o /openwrt/tmp/cciEULRy.o
GNU C++14 (OpenWrt GCC 8.4.0 r0-d97b735) version 8.4.0 (mips-openwrt-linux-musl)
	compiled by GNU C version 9.3.0, GMP version 6.2.1, MPFR version 4.1.0, MPC version 1.2.1, isl version none
GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
ignoring duplicate directory "/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include"
  as it is a non-system directory that duplicates a system directory
#include "..." search starts here:
#include <...> search starts here:
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include/c++/8.4.0
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include/c++/8.4.0/mips-openwrt-linux-musl
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include/c++/8.4.0/backward
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/sys-include
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/include
 /openwrt/staging_dir/target-mips_24kc_musl/usr/include
End of search list.
GNU C++14 (OpenWrt GCC 8.4.0 r0-d97b735) version 8.4.0 (mips-openwrt-linux-musl)
	compiled by GNU C version 9.3.0, GMP version 6.2.1, MPFR version 4.1.0, MPC version 1.2.1, isl version none
GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
Compiler executable checksum: c0f11eb4d5bf754b309699d9f82760c8
GNU assembler version 2.34 (mips-openwrt-linux-musl) using BFD version (GNU Binutils) 2.34
COLLECT_GCC_OPTIONS='-v' '-Os' '-pipe' '-mno-branch-likely' '-mips32r2' '-mtune=24kc' '-fno-caller-saves' '-fno-plt' '-fhonour-copts' '-Wno-error=unused-but-set-variable' '-Wno-error=unused-result' '-msoft-float' '-mips16' '-minterlink-mips16' '-fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950=xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950' '-Wformat=1' '-Werror=format-security' '-fstack-protector' '-D' '_FORTIFY_SOURCE=1' '-fno-exceptions' '-fno-rtti' '-D' 'WITH_URANDOM' '-I' '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include' '-I' '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify' '-I' '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include' '-L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib' '-L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib' '-z' 'now' '-z' 'relro' '-o' 'xupnpd' '-mllsc' '-mplt' '-mno-shared' '-EB' '-mabi=32'
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/libexec/gcc/mips-openwrt-linux-musl/8.4.0/cc1plus -quiet -v -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -D_GNU_SOURCE -idirafter /openwrt/staging_dir/target-mips_24kc_musl/usr/include -D _FORTIFY_SOURCE=1 -D WITH_URANDOM main.cpp -meb -quiet -dumpbase main.cpp -mno-branch-likely -mips32r2 -mtune=24kc -msoft-float -mips16 -minterlink-mips16 -mllsc -mplt -mno-shared -mabi=32 -auxbase main -Os -Wno-error=unused-but-set-variable -Wno-error=unused-result -Wformat=1 -Werror=format-security -version -fno-caller-saves -fno-plt -fhonour-copts -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950=xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950 -fstack-protector -fno-exceptions -fno-rtti -o - |
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/as -v -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -EB -mips32r2 -mips16 -O2 -mabi=32 -mno-shared -mtune=24kc -msoft-float -call_nonpic -o /openwrt/tmp/ccteE6Ny.o
GNU C++14 (OpenWrt GCC 8.4.0 r0-d97b735) version 8.4.0 (mips-openwrt-linux-musl)
	compiled by GNU C version 9.3.0, GMP version 6.2.1, MPFR version 4.1.0, MPC version 1.2.1, isl version none
GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
ignoring duplicate directory "/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include"
  as it is a non-system directory that duplicates a system directory
#include "..." search starts here:
#include <...> search starts here:
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include/c++/8.4.0
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include/c++/8.4.0/mips-openwrt-linux-musl
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include/c++/8.4.0/backward
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/sys-include
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/include
 /openwrt/staging_dir/target-mips_24kc_musl/usr/include
End of search list.
GNU C++14 (OpenWrt GCC 8.4.0 r0-d97b735) version 8.4.0 (mips-openwrt-linux-musl)
	compiled by GNU C version 9.3.0, GMP version 6.2.1, MPFR version 4.1.0, MPC version 1.2.1, isl version none
GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
Compiler executable checksum: c0f11eb4d5bf754b309699d9f82760c8
GNU assembler version 2.34 (mips-openwrt-linux-musl) using BFD version (GNU Binutils) 2.34
main.cpp: In function 'int main(int, char**)':
main.cpp:23:22: warning: ISO C++ forbids converting a string constant to 'char*' [-Wwrite-strings]
  char *xupnpd_root = "/usr/share/xupnpd/";
                      ^~~~~~~~~~~~~~~~~~~~
COLLECT_GCC_OPTIONS='-v' '-Os' '-pipe' '-mno-branch-likely' '-mips32r2' '-mtune=24kc' '-fno-caller-saves' '-fno-plt' '-fhonour-copts' '-Wno-error=unused-but-set-variable' '-Wno-error=unused-result' '-msoft-float' '-mips16' '-minterlink-mips16' '-fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950=xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950' '-Wformat=1' '-Werror=format-security' '-fstack-protector' '-D' '_FORTIFY_SOURCE=1' '-fno-exceptions' '-fno-rtti' '-D' 'WITH_URANDOM' '-I' '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include' '-I' '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify' '-I' '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include' '-L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib' '-L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib' '-z' 'now' '-z' 'relro' '-o' 'xupnpd' '-mllsc' '-mplt' '-mno-shared' '-EB' '-mabi=32'
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/libexec/gcc/mips-openwrt-linux-musl/8.4.0/cc1plus -quiet -v -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -D_GNU_SOURCE -idirafter /openwrt/staging_dir/target-mips_24kc_musl/usr/include -D _FORTIFY_SOURCE=1 -D WITH_URANDOM mcast.cpp -meb -quiet -dumpbase mcast.cpp -mno-branch-likely -mips32r2 -mtune=24kc -msoft-float -mips16 -minterlink-mips16 -mllsc -mplt -mno-shared -mabi=32 -auxbase mcast -Os -Wno-error=unused-but-set-variable -Wno-error=unused-result -Wformat=1 -Werror=format-security -version -fno-caller-saves -fno-plt -fhonour-copts -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950=xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950 -fstack-protector -fno-exceptions -fno-rtti -o - |
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/as -v -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -EB -mips32r2 -mips16 -O2 -mabi=32 -mno-shared -mtune=24kc -msoft-float -call_nonpic -o /openwrt/tmp/ccBEsIeA.o
GNU assembler version 2.34 (mips-openwrt-linux-musl) using BFD version (GNU Binutils) 2.34
GNU C++14 (OpenWrt GCC 8.4.0 r0-d97b735) version 8.4.0 (mips-openwrt-linux-musl)
	compiled by GNU C version 9.3.0, GMP version 6.2.1, MPFR version 4.1.0, MPC version 1.2.1, isl version none
GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
ignoring duplicate directory "/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include"
  as it is a non-system directory that duplicates a system directory
#include "..." search starts here:
#include <...> search starts here:
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include/c++/8.4.0
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include/c++/8.4.0/mips-openwrt-linux-musl
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include/c++/8.4.0/backward
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/sys-include
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/include
 /openwrt/staging_dir/target-mips_24kc_musl/usr/include
End of search list.
GNU C++14 (OpenWrt GCC 8.4.0 r0-d97b735) version 8.4.0 (mips-openwrt-linux-musl)
	compiled by GNU C version 9.3.0, GMP version 6.2.1, MPFR version 4.1.0, MPC version 1.2.1, isl version none
GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
Compiler executable checksum: c0f11eb4d5bf754b309699d9f82760c8
COLLECT_GCC_OPTIONS='-v' '-Os' '-pipe' '-mno-branch-likely' '-mips32r2' '-mtune=24kc' '-fno-caller-saves' '-fno-plt' '-fhonour-copts' '-Wno-error=unused-but-set-variable' '-Wno-error=unused-result' '-msoft-float' '-mips16' '-minterlink-mips16' '-fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950=xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950' '-Wformat=1' '-Werror=format-security' '-fstack-protector' '-D' '_FORTIFY_SOURCE=1' '-fno-exceptions' '-fno-rtti' '-D' 'WITH_URANDOM' '-I' '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include' '-I' '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify' '-I' '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include' '-L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib' '-L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib' '-z' 'now' '-z' 'relro' '-o' 'xupnpd' '-mllsc' '-mplt' '-mno-shared' '-EB' '-mabi=32'
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/libexec/gcc/mips-openwrt-linux-musl/8.4.0/cc1plus -quiet -v -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -D_GNU_SOURCE -idirafter /openwrt/staging_dir/target-mips_24kc_musl/usr/include -D _FORTIFY_SOURCE=1 -D WITH_URANDOM mem.cpp -meb -quiet -dumpbase mem.cpp -mno-branch-likely -mips32r2 -mtune=24kc -msoft-float -mips16 -minterlink-mips16 -mllsc -mplt -mno-shared -mabi=32 -auxbase mem -Os -Wno-error=unused-but-set-variable -Wno-error=unused-result -Wformat=1 -Werror=format-security -version -fno-caller-saves -fno-plt -fhonour-copts -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950=xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950 -fstack-protector -fno-exceptions -fno-rtti -o - |
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/as -v -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -EB -mips32r2 -mips16 -O2 -mabi=32 -mno-shared -mtune=24kc -msoft-float -call_nonpic -o /openwrt/tmp/cco165XA.o
GNU C++14 (OpenWrt GCC 8.4.0 r0-d97b735) version 8.4.0 (mips-openwrt-linux-musl)
	compiled by GNU C version 9.3.0, GMP version 6.2.1, MPFR version 4.1.0, MPC version 1.2.1, isl version none
GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
ignoring duplicate directory "/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include"
  as it is a non-system directory that duplicates a system directory
#include "..." search starts here:
#include <...> search starts here:
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include/c++/8.4.0
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include/c++/8.4.0/mips-openwrt-linux-musl
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include/c++/8.4.0/backward
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/sys-include
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/include
 /openwrt/staging_dir/target-mips_24kc_musl/usr/include
End of search list.
GNU C++14 (OpenWrt GCC 8.4.0 r0-d97b735) version 8.4.0 (mips-openwrt-linux-musl)
	compiled by GNU C version 9.3.0, GMP version 6.2.1, MPFR version 4.1.0, MPC version 1.2.1, isl version none
GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
Compiler executable checksum: GNU assembler version 2.34 (mips-openwrt-linux-musl) using BFD version (GNU Binutils) 2.34
c0f11eb4d5bf754b309699d9f82760c8
COLLECT_GCC_OPTIONS='-v' '-Os' '-pipe' '-mno-branch-likely' '-mips32r2' '-mtune=24kc' '-fno-caller-saves' '-fno-plt' '-fhonour-copts' '-Wno-error=unused-but-set-variable' '-Wno-error=unused-result' '-msoft-float' '-mips16' '-minterlink-mips16' '-fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950=xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950' '-Wformat=1' '-Werror=format-security' '-fstack-protector' '-D' '_FORTIFY_SOURCE=1' '-fno-exceptions' '-fno-rtti' '-D' 'WITH_URANDOM' '-I' '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include' '-I' '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify' '-I' '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include' '-L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib' '-L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib' '-z' 'now' '-z' 'relro' '-o' 'xupnpd' '-mllsc' '-mplt' '-mno-shared' '-EB' '-mabi=32'
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/libexec/gcc/mips-openwrt-linux-musl/8.4.0/cc1plus -quiet -v -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -D_GNU_SOURCE -idirafter /openwrt/staging_dir/target-mips_24kc_musl/usr/include -D _FORTIFY_SOURCE=1 -D WITH_URANDOM soap.cpp -meb -quiet -dumpbase soap.cpp -mno-branch-likely -mips32r2 -mtune=24kc -msoft-float -mips16 -minterlink-mips16 -mllsc -mplt -mno-shared -mabi=32 -auxbase soap -Os -Wno-error=unused-but-set-variable -Wno-error=unused-result -Wformat=1 -Werror=format-security -version -fno-caller-saves -fno-plt -fhonour-copts -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950=xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950 -fstack-protector -fno-exceptions -fno-rtti -o - |
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/as -v -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -EB -mips32r2 -mips16 -O2 -mabi=32 -mno-shared -mtune=24kc -msoft-float -call_nonpic -o /openwrt/tmp/ccS9fuhB.o
GNU C++14 (OpenWrt GCC 8.4.0 r0-d97b735) version 8.4.0 (mips-openwrt-linux-musl)
	compiled by GNU C version 9.3.0, GMP version 6.2.1, MPFR version 4.1.0, MPC version 1.2.1, isl version none
GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
ignoring duplicate directory "/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include"
  as it is a non-system directory that duplicates a system directory
#include "..." search starts here:
#include <...> search starts here:
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include/c++/8.4.0
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include/c++/8.4.0/mips-openwrt-linux-musl
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include/c++/8.4.0/backward
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/sys-include
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include
 /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/include
 /openwrt/staging_dir/target-mips_24kc_musl/usr/include
End of search list.
GNU C++14 (OpenWrt GCC 8.4.0 r0-d97b735) version 8.4.0 (mips-openwrt-linux-musl)
	compiled by GNU C version 9.3.0, GMP version 6.2.1, MPFR version 4.1.0, MPC version 1.2.1, isl version none
GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
Compiler executable checksum: c0f11eb4d5bf754b309699d9f82760c8
GNU assembler version 2.34 (mips-openwrt-linux-musl) using BFD version (GNU Binutils) 2.34
make[3]: *** [Makefile:77: /openwrt/build_dir/target-mips_24kc_musl/xupnpd-e4e542d9b6d0043d470fda283e2cd325bbb91950/.built] Error 1
```
