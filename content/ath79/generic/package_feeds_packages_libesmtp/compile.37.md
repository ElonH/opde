---
title: "compile.37"
date: 2021-06-20 22:26:36.903630
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
make package/feeds/packages/libesmtp/compile -j$(nproc) || make package/feeds/packages/libesmtp/compile V=s
```

#### Compile.txt

``` bash
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-mips_24kc_musl/libESMTP-1.1.0
Build dir: /openwrt/build_dir/target-mips_24kc_musl/libESMTP-1.1.0/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: libESMTP
Project version: 1.1.0
C compiler for the host machine: ccache_cc (gcc 8.4.0 "mips-openwrt-linux-musl-gcc (OpenWrt GCC 8.4.0 r0-91deb05) 8.4.0")
C linker for the host machine: ccache_cc ld.bfd 2.34
C compiler for the build machine: ccache gcc (gcc 9.3.0 "gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0")
C linker for the build machine: gcc ld.bfd 2.34
Build machine cpu family: x86_64
Build machine cpu: x86_64
Host machine cpu family: mips
Host machine cpu: generic
Target machine cpu family: mips
Target machine cpu: generic
Compiler for C supports arguments -D_POSIX_C_SOURCE=200809L: YES 
Library dl found: YES
Found pkg-config: /openwrt/staging_dir/host/bin/pkg-config (1.7.3)
Found CMake: NO
Run-time dependency openssl found: NO (tried pkgconfig and cmake)
Run-time dependency threads found: YES
Library lwres skipped: feature lwres disabled
Checking for function "strlcpy" : YES 
Checking for function "strdup" : YES 
Checking for function "strncasecmp" : YES 
Checking for function "strcasecmp" : YES 
Header <string.h> has symbol "memrchr" : NO 
Checking for size of "unsigned int" : 4
Checking for size of "unsigned long" : 4
Checking for size of "unsigned short" : 2
Configuring config.h using configuration
Configuring libesmtp.spec using configuration
../../../../build_dir/target-mips_24kc_musl/libESMTP-1.1.0/meson.build:157: WARNING: The variable(s) 'RPM_BUILDREQUIRES', 'RPM_OPENSSL', 'RPM_OPENSSLDEVEL', 'RPM_REQUIRES' in the input file 'libesmtp.spec.in' are not present in the given configuration data.
Build targets in project: 4

libESMTP 1.1.0

    current:revision:age: 8:0:2
    so version          : 6.2.0
    prefix              : /usr
    libdir              : lib
    threads             : True
    lwres               : False
    AUTH modules        : /usr/lib/esmtp-plugins-6.2.0
    Legacy file layout  : False
    STARTTLS            : False
    CHUNKING            : True
    ETRN                : True
    XUSR                : True

Found ninja-1.10.2 at /openwrt/staging_dir/hostpkg/bin/ninja
ninja: Entering directory `/openwrt/build_dir/target-mips_24kc_musl/libESMTP-1.1.0/openwrt-build'
[1/28] Compiling C object libesmtp.so.6.2.0.p/base64.c.o
[2/28] Compiling C object libesmtp.so.6.2.0.p/concatenate.c.o
[3/28] Compiling C object libesmtp.so.6.2.0.p/auth-client.c.o
[4/28] Compiling C object libesmtp.so.6.2.0.p/errors.c.o
[5/28] Compiling C object libesmtp.so.6.2.0.p/htable.c.o
[6/28] Compiling C object libesmtp.so.6.2.0.p/message-callbacks.c.o
[7/28] Compiling C object libesmtp.so.6.2.0.p/headers.c.o
[8/28] Compiling C object libesmtp.so.6.2.0.p/message-source.c.o
[9/28] Compiling C object libesmtp.so.6.2.0.p/missing.c.o
[10/28] Compiling C object libesmtp.so.6.2.0.p/rfc2822date.c.o
[11/28] Compiling C object libesmtp.so.6.2.0.p/siobuf.c.o
In file included from ../siobuf.c:39:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/poll.h:1:2: warning: #warning redirecting incorrect #include <sys/poll.h> to <poll.h> [-Wcpp]
 #warning redirecting incorrect #include <sys/poll.h> to <poll.h>
  ^~~~~~~
[12/28] Compiling C object libesmtp.so.6.2.0.p/smtp-auth.c.o
[13/28] Compiling C object libesmtp.so.6.2.0.p/smtp-api.c.o
../smtp-api.c: In function 'smtp_version':
../smtp-api.c:1183:7: warning: implicit declaration of function 'strlcpy'; did you mean 'strncpy'? [-Wimplicit-function-declaration]
   if (strlcpy (buf, v, len) > len)
       ^~~~~~~
       strncpy
[14/28] Compiling C object libesmtp.so.6.2.0.p/protocol.c.o
[15/28] Compiling C object libesmtp.so.6.2.0.p/smtp-bdat.c.o
[16/28] Compiling C object libesmtp.so.6.2.0.p/smtp-etrn.c.o
[17/28] Compiling C object libesmtp.so.6.2.0.p/smtp-tls.c.o
[18/28] Compiling C object login/sasl-login.so.p/client-login.c.o
[19/28] Compiling C object libesmtp.so.6.2.0.p/tlsutils.c.o
[20/28] Compiling C object libesmtp.so.6.2.0.p/tokens.c.o
[21/28] Linking target login/sasl-login.so
[22/28] Linking target libesmtp.so.6.2.0
[23/28] Compiling C object plain/sasl-plain.so.p/client-plain.c.o
[24/28] Compiling C object crammd5/sasl-crammd5.so.p/hmacmd5.c.o
[25/28] Linking target plain/sasl-plain.so
[26/28] Compiling C object crammd5/sasl-crammd5.so.p/client-crammd5.c.o
[27/28] Compiling C object crammd5/sasl-crammd5.so.p/md5.c.o
[28/28] Linking target crammd5/sasl-crammd5.so
ninja: Entering directory `/openwrt/build_dir/target-mips_24kc_musl/libESMTP-1.1.0/openwrt-build'
[0/1] Installing files.
Installing libesmtp.so.6.2.0 to /openwrt/build_dir/target-mips_24kc_musl/libESMTP-1.1.0/ipkg-install/usr/lib
Installing login/sasl-login.so to /openwrt/build_dir/target-mips_24kc_musl/libESMTP-1.1.0/ipkg-install/usr/lib/esmtp-plugins-6.2.0
Installing plain/sasl-plain.so to /openwrt/build_dir/target-mips_24kc_musl/libESMTP-1.1.0/ipkg-install/usr/lib/esmtp-plugins-6.2.0
Installing crammd5/sasl-crammd5.so to /openwrt/build_dir/target-mips_24kc_musl/libESMTP-1.1.0/ipkg-install/usr/lib/esmtp-plugins-6.2.0
Installing /openwrt/build_dir/target-mips_24kc_musl/libESMTP-1.1.0/libesmtp.h to /openwrt/build_dir/target-mips_24kc_musl/libESMTP-1.1.0/ipkg-install/usr/include/
Installing /openwrt/build_dir/target-mips_24kc_musl/libESMTP-1.1.0/auth-client.h to /openwrt/build_dir/target-mips_24kc_musl/libESMTP-1.1.0/ipkg-install/usr/include/
Installing /openwrt/build_dir/target-mips_24kc_musl/libESMTP-1.1.0/openwrt-build/meson-private/libesmtp-1.0.pc to /openwrt/build_dir/target-mips_24kc_musl/libESMTP-1.1.0/ipkg-install/usr/lib/pkgconfig
cp: cannot stat '/openwrt/build_dir/target-mips_24kc_musl/libESMTP-1.1.0/ipkg-install/usr/lib/esmtp-plugins-6.2.0/sasl-ntlm.so': No such file or directory
make[3]: *** [Makefile:67: /openwrt/build_dir/target-mips_24kc_musl/libESMTP-1.1.0/.pkgdir/libesmtp.installed] Error 1
```
