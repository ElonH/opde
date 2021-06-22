---
title: "compile.40"
date: 2021-06-22 10:41:19.981522
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
make package/feeds/packages/openconnect/compile -j$(nproc) || make package/feeds/packages/openconnect/compile V=s
```

#### Compile.txt

``` bash
configure: loading site script /openwrt/include/site/mips
checking pkg-config is at least version 0.9.0... yes
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking whether to enable maintainer-specific portions of Makefiles... yes
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether UID '1000' is supported by ustar format... yes
checking whether GID '1000' is supported by ustar format... yes
checking how to create a ustar tar archive... gnutar
checking whether make supports nested variables... (cached) yes
configure: Applying feature macros for GNU build
checking whether make supports the include directive... yes (GNU style)
checking for mips-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
checking whether ccache_cc understands -c and -o together... yes
checking dependency style of ccache_cc... gcc3
checking for fdevname_r... no
checking for statfs... yes
checking for getline... yes
checking for strcasestr... yes
checking for strndup... yes
checking for asprintf... yes
checking for vasprintf... yes
checking for supported compiler flags...  -Wall -Wextra -Wno-missing-field-initializers -Wno-sign-compare -Wno-unused-parameter -Werror=pointer-to-int-cast -Wdeclaration-after-statement -Werror-implicit-function-declaration -Wformat-nonliteral -Wformat-security -Winit-self -Wmissing-declarations -Wmissing-include-dirs -Wnested-externs -Wpointer-arith -Wwrite-strings
checking For memset_s... no
checking for explicit_memset... no
checking for explicit_bzero... yes
checking For localtime_r... yes
checking for socket... yes
checking for inet_aton... yes
checking for IPV6_PATHMTU socket option... yes
checking for __android_log_vprint... no
checking for __android_log_vprint in -llog... no
checking for nl_langinfo... yes
checking for ld used by ccache_cc... mips-openwrt-linux-musl-ld
checking if the linker (mips-openwrt-linux-musl-ld) is GNU ld... yes
checking for shared library run path origin... done
checking how to run the C preprocessor... ccache_cc -E
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for iconv... yes
checking for working iconv... guessing yes
checking how to link with libiconv... /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib/libiconv.a
checking for iconv declaration... 
         extern size_t iconv (iconv_t cd, char * *inbuf, size_t *inbytesleft, char * *outbuf, size_t *outbytesleft);
checking for GNUTLS... no
checking for OPENSSL... no
checking for OpenSSL without pkg-config... no
configure: error: Could not build against OpenSSL
make[3]: *** [Makefile:93: /openwrt/build_dir/target-mips_24kc_musl/openconnect-8.10/.configured_7a95e9e47025bf8b30aa55c7748065df] Error 1
```
