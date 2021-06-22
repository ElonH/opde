---
title: "compile.40"
date: 2021-06-22 10:41:19.988612
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
make package/feeds/packages/mailsend/compile -j$(nproc) || make package/feeds/packages/mailsend/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/0001-OpenSSL-1.1-support-for-HMAC-api.patch using plaintext: 
patching file utils.c

Applying ./patches/0002-Removed-API-deprecated-by-OpenSSL-1.1.0.patch using plaintext: 
patching file main.c
patching file utils.c
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/mips
checking for mips-openwrt-linux-ranlib... mips-openwrt-linux-musl-gcc-ranlib
checking whether make sets $(MAKE)... yes
checking for mips-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking how to run the C preprocessor... ccache_cc -E
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
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
checking for string.h... (cached) yes
checking for strings.h... (cached) yes
checking for memory.h... (cached) yes
checking malloc.h usability... yes
checking malloc.h presence... yes
checking for malloc.h... yes
checking for unistd.h... (cached) yes
checking ctype.h usability... yes
checking ctype.h presence... yes
checking for ctype.h... yes
checking for stdint.h... (cached) yes
checking for sys/types.h... (cached) yes
checking for stdlib.h... (cached) yes
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking sys/file.h usability... yes
checking sys/file.h presence... yes
checking for sys/file.h... yes
checking limits.h usability... yes
checking limits.h presence... yes
checking for limits.h... yes
checking sys/syslimits.h usability... no
checking sys/syslimits.h presence... no
checking for sys/syslimits.h... no
checking for mips-openwrt-linux-strip... /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-strip
checking for flock... yes
checking for socket... yes
checking for htonl... yes
checking for gethostname... yes
checking for gethostbyaddr... yes
checking for yp_get_default_domain... no
checking for __yp_get_default_domain... no
checking for yp_get_default_domain in -lnsl... no
checking for __yp_get_default_domain in -lnsl... no
checking for res_search... yes
checking for inet_aton... yes
checking for dn_skipname... yes
checking for mkstemp... yes
checking for getaddrinfo... yes
checking for OpenSSL... no
configure: creating ./config.status
config.status: creating Makefile
config.status: creating libs/libmsock/Makefile
config.status: creating libs/libmutils/mkey.c
config.status: creating libs/libmutils/Makefile
config.status: creating libs/libsll/Makefile
configure: WARNING: unrecognized options: --disable-nls
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/mailsend-ssl/mailsend-1.19'
make -C libs/libmutils
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/mailsend-ssl/mailsend-1.19/libs/libmutils'
rm -f string.o
ccache_cc -O -I.  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STRING_H=1 -DHAVE_STRINGS_H=1 -DHAVE_MEMORY_H=1 -DHAVE_MALLOC_H=1 -DHAVE_UNISTD_H=1 -DHAVE_CTYPE_H=1 -DHAVE_STDINT_H=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_STDLIB_H=1 -DHAVE_FCNTL_H=1 -DHAVE_SYS_FILE_H=1 -DHAVE_LIMITS_H=1 -DHAVE_FLOCK=1 -DHAVE_SOCKET=1 -DHAVE_HTONL=1 -DHAVE_GETHOSTNAME=1 -DHAVE_GETHOSTBYADDR=1 -DHAVE_RES_SEARCH=1 -DHAVE_INET_ATON=1 -DHAVE_DN_SKIPNAME=1 -DHAVE_MKSTEMP=1 -DHAVE_GETADDRINFO=1 -DSYS_UNIX=1 -c string.c
cc1: note: someone does not honour COPTS correctly, passed 0 times
rm -f mutils.o
ccache_cc -O -I.  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STRING_H=1 -DHAVE_STRINGS_H=1 -DHAVE_MEMORY_H=1 -DHAVE_MALLOC_H=1 -DHAVE_UNISTD_H=1 -DHAVE_CTYPE_H=1 -DHAVE_STDINT_H=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_STDLIB_H=1 -DHAVE_FCNTL_H=1 -DHAVE_SYS_FILE_H=1 -DHAVE_LIMITS_H=1 -DHAVE_FLOCK=1 -DHAVE_SOCKET=1 -DHAVE_HTONL=1 -DHAVE_GETHOSTNAME=1 -DHAVE_GETHOSTBYADDR=1 -DHAVE_RES_SEARCH=1 -DHAVE_INET_ATON=1 -DHAVE_DN_SKIPNAME=1 -DHAVE_MKSTEMP=1 -DHAVE_GETADDRINFO=1 -DSYS_UNIX=1 -c mutils.c
cc1: note: someone does not honour COPTS correctly, passed 0 times
mutils.c: In function 'mutils_basename':
mutils.c:1110:15: warning: initialization discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
         *bn = path;
               ^~~~
mutils.c:1116:32: warning: return discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
     return (bn == NULL) ? path : ++bn;
            ~~~~~~~~~~~~~~~~~~~~^~~~~~
rm -f mutils_mime.o
ccache_cc -O -I.  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STRING_H=1 -DHAVE_STRINGS_H=1 -DHAVE_MEMORY_H=1 -DHAVE_MALLOC_H=1 -DHAVE_UNISTD_H=1 -DHAVE_CTYPE_H=1 -DHAVE_STDINT_H=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_STDLIB_H=1 -DHAVE_FCNTL_H=1 -DHAVE_SYS_FILE_H=1 -DHAVE_LIMITS_H=1 -DHAVE_FLOCK=1 -DHAVE_SOCKET=1 -DHAVE_HTONL=1 -DHAVE_GETHOSTNAME=1 -DHAVE_GETHOSTBYADDR=1 -DHAVE_RES_SEARCH=1 -DHAVE_INET_ATON=1 -DHAVE_DN_SKIPNAME=1 -DHAVE_MKSTEMP=1 -DHAVE_GETADDRINFO=1 -DSYS_UNIX=1 -c mutils_mime.c
cc1: note: someone does not honour COPTS correctly, passed 0 times
rm -f mutils_blob.o
ccache_cc -O -I.  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STRING_H=1 -DHAVE_STRINGS_H=1 -DHAVE_MEMORY_H=1 -DHAVE_MALLOC_H=1 -DHAVE_UNISTD_H=1 -DHAVE_CTYPE_H=1 -DHAVE_STDINT_H=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_STDLIB_H=1 -DHAVE_FCNTL_H=1 -DHAVE_SYS_FILE_H=1 -DHAVE_LIMITS_H=1 -DHAVE_FLOCK=1 -DHAVE_SOCKET=1 -DHAVE_HTONL=1 -DHAVE_GETHOSTNAME=1 -DHAVE_GETHOSTBYADDR=1 -DHAVE_RES_SEARCH=1 -DHAVE_INET_ATON=1 -DHAVE_DN_SKIPNAME=1 -DHAVE_MKSTEMP=1 -DHAVE_GETADDRINFO=1 -DSYS_UNIX=1 -c mutils_blob.c
cc1: note: someone does not honour COPTS correctly, passed 0 times
rm -f mutils_error.o
ccache_cc -O -I.  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STRING_H=1 -DHAVE_STRINGS_H=1 -DHAVE_MEMORY_H=1 -DHAVE_MALLOC_H=1 -DHAVE_UNISTD_H=1 -DHAVE_CTYPE_H=1 -DHAVE_STDINT_H=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_STDLIB_H=1 -DHAVE_FCNTL_H=1 -DHAVE_SYS_FILE_H=1 -DHAVE_LIMITS_H=1 -DHAVE_FLOCK=1 -DHAVE_SOCKET=1 -DHAVE_HTONL=1 -DHAVE_GETHOSTNAME=1 -DHAVE_GETHOSTBYADDR=1 -DHAVE_RES_SEARCH=1 -DHAVE_INET_ATON=1 -DHAVE_DN_SKIPNAME=1 -DHAVE_MKSTEMP=1 -DHAVE_GETADDRINFO=1 -DSYS_UNIX=1 -c mutils_error.c
cc1: note: someone does not honour COPTS correctly, passed 0 times
rm -f mutils_temp.o
ccache_cc -O -I.  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STRING_H=1 -DHAVE_STRINGS_H=1 -DHAVE_MEMORY_H=1 -DHAVE_MALLOC_H=1 -DHAVE_UNISTD_H=1 -DHAVE_CTYPE_H=1 -DHAVE_STDINT_H=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_STDLIB_H=1 -DHAVE_FCNTL_H=1 -DHAVE_SYS_FILE_H=1 -DHAVE_LIMITS_H=1 -DHAVE_FLOCK=1 -DHAVE_SOCKET=1 -DHAVE_HTONL=1 -DHAVE_GETHOSTNAME=1 -DHAVE_GETHOSTBYADDR=1 -DHAVE_RES_SEARCH=1 -DHAVE_INET_ATON=1 -DHAVE_DN_SKIPNAME=1 -DHAVE_MKSTEMP=1 -DHAVE_GETADDRINFO=1 -DSYS_UNIX=1 -c mutils_temp.c
cc1: note: someone does not honour COPTS correctly, passed 0 times
rm -f mutils_time.o
ccache_cc -O -I.  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STRING_H=1 -DHAVE_STRINGS_H=1 -DHAVE_MEMORY_H=1 -DHAVE_MALLOC_H=1 -DHAVE_UNISTD_H=1 -DHAVE_CTYPE_H=1 -DHAVE_STDINT_H=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_STDLIB_H=1 -DHAVE_FCNTL_H=1 -DHAVE_SYS_FILE_H=1 -DHAVE_LIMITS_H=1 -DHAVE_FLOCK=1 -DHAVE_SOCKET=1 -DHAVE_HTONL=1 -DHAVE_GETHOSTNAME=1 -DHAVE_GETHOSTBYADDR=1 -DHAVE_RES_SEARCH=1 -DHAVE_INET_ATON=1 -DHAVE_DN_SKIPNAME=1 -DHAVE_MKSTEMP=1 -DHAVE_GETADDRINFO=1 -DSYS_UNIX=1 -c mutils_time.c
cc1: note: someone does not honour COPTS correctly, passed 0 times
mutils_time.c: In function 'mutils_time_now':
mutils_time.c:26:8: warning: implicit declaration of function 'gettimeofday' [-Wimplicit-function-declaration]
     rc=gettimeofday(&tv,NULL);
        ^~~~~~~~~~~~
rm -f libmutils.a
ar cq libmutils.a string.o mutils.o mutils_mime.o mutils_blob.o mutils_error.o mutils_temp.o mutils_time.o
mips-openwrt-linux-musl-gcc-ranlib libmutils.a
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/mailsend-ssl/mailsend-1.19/libs/libmutils'
make -C libs/libmsock
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/mailsend-ssl/mailsend-1.19/libs/libmsock'
rm -f msock.o
ccache_cc -O -I.  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STRING_H=1 -DHAVE_STRINGS_H=1 -DHAVE_MEMORY_H=1 -DHAVE_MALLOC_H=1 -DHAVE_UNISTD_H=1 -DHAVE_CTYPE_H=1 -DHAVE_STDINT_H=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_STDLIB_H=1 -DHAVE_FCNTL_H=1 -DHAVE_SYS_FILE_H=1 -DHAVE_LIMITS_H=1 -DHAVE_FLOCK=1 -DHAVE_SOCKET=1 -DHAVE_HTONL=1 -DHAVE_GETHOSTNAME=1 -DHAVE_GETHOSTBYADDR=1 -DHAVE_RES_SEARCH=1 -DHAVE_INET_ATON=1 -DHAVE_DN_SKIPNAME=1 -DHAVE_MKSTEMP=1 -DHAVE_GETADDRINFO=1  -DSYS_UNIX=1 -c msock.c
cc1: note: someone does not honour COPTS correctly, passed 0 times
rm -f libmsock.a
ar cq libmsock.a msock.o
mips-openwrt-linux-musl-gcc-ranlib libmsock.a
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/mailsend-ssl/mailsend-1.19/libs/libmsock'
make -C libs/libsll
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/mailsend-ssl/mailsend-1.19/libs/libsll'
rm -f sll.o
ccache_cc -O -I.  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STRING_H=1 -DHAVE_STRINGS_H=1 -DHAVE_MEMORY_H=1 -DHAVE_MALLOC_H=1 -DHAVE_UNISTD_H=1 -DHAVE_CTYPE_H=1 -DHAVE_STDINT_H=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_STDLIB_H=1 -DHAVE_FCNTL_H=1 -DHAVE_SYS_FILE_H=1 -DHAVE_LIMITS_H=1 -DHAVE_FLOCK=1 -DHAVE_SOCKET=1 -DHAVE_HTONL=1 -DHAVE_GETHOSTNAME=1 -DHAVE_GETHOSTBYADDR=1 -DHAVE_RES_SEARCH=1 -DHAVE_INET_ATON=1 -DHAVE_DN_SKIPNAME=1 -DHAVE_MKSTEMP=1 -DHAVE_GETADDRINFO=1 -DSYS_UNIX=1 -c sll.c
cc1: note: someone does not honour COPTS correctly, passed 0 times
rm -f libsll.a
ar cq libsll.a sll.o
mips-openwrt-linux-musl-gcc-ranlib libsll.a
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/mailsend-ssl/mailsend-1.19/libs/libsll'
rm -f main.o
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/mailsend-ssl/mailsend-1.19=mailsend-1.19 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -Wall -I. -I./libs/libmutils -I./libs/libmsock -I./libs/libsll  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STRING_H=1 -DHAVE_STRINGS_H=1 -DHAVE_MEMORY_H=1 -DHAVE_MALLOC_H=1 -DHAVE_UNISTD_H=1 -DHAVE_CTYPE_H=1 -DHAVE_STDINT_H=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_STDLIB_H=1 -DHAVE_FCNTL_H=1 -DHAVE_SYS_FILE_H=1 -DHAVE_LIMITS_H=1 -DHAVE_FLOCK=1 -DHAVE_SOCKET=1 -DHAVE_HTONL=1 -DHAVE_GETHOSTNAME=1 -DHAVE_GETHOSTBYADDR=1 -DHAVE_RES_SEARCH=1 -DHAVE_INET_ATON=1 -DHAVE_DN_SKIPNAME=1 -DHAVE_MKSTEMP=1 -DHAVE_GETADDRINFO=1 -DUNIX -DHAVE_STRING_H=1 -DHAVE_STDLIB_H=1 -DHAVE_MATH_H=1 -c main.c
main.c: In function 'main':
main.c:968:21: warning: implicit declaration of function 'show_mime_types'; did you mean 'get_mime_type'? [-Wimplicit-function-declaration]
                     show_mime_types();
                     ^~~~~~~~~~~~~~~
                     get_mime_type
rm -f smtp.o
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/mailsend-ssl/mailsend-1.19=mailsend-1.19 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -Wall -I. -I./libs/libmutils -I./libs/libmsock -I./libs/libsll  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STRING_H=1 -DHAVE_STRINGS_H=1 -DHAVE_MEMORY_H=1 -DHAVE_MALLOC_H=1 -DHAVE_UNISTD_H=1 -DHAVE_CTYPE_H=1 -DHAVE_STDINT_H=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_STDLIB_H=1 -DHAVE_FCNTL_H=1 -DHAVE_SYS_FILE_H=1 -DHAVE_LIMITS_H=1 -DHAVE_FLOCK=1 -DHAVE_SOCKET=1 -DHAVE_HTONL=1 -DHAVE_GETHOSTNAME=1 -DHAVE_GETHOSTBYADDR=1 -DHAVE_RES_SEARCH=1 -DHAVE_INET_ATON=1 -DHAVE_DN_SKIPNAME=1 -DHAVE_MKSTEMP=1 -DHAVE_GETADDRINFO=1 -DUNIX -DHAVE_STRING_H=1 -DHAVE_STDLIB_H=1 -DHAVE_MATH_H=1 -c smtp.c
smtp.c: In function 'process_embeded_images':
smtp.c:988:7: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
     b = boundary;
       ^
smtp.c:989:8: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
     ib = boundary;
        ^
smtp.c: In function 'send_the_mail':
smtp.c:1731:12: warning: pointer targets in assignment from 'char *' to 'unsigned char *' differ in signedness [-Wpointer-sign]
         b64=mutils_encode_base64_noformat(buf,len);
            ^
smtp.c: In function 'read_smtp_line':
smtp.c:150:62: warning: 'snprintf' output may be truncated before the last format character [-Wformat-truncation=]
         (void) snprintf(smtp_errbuf,sizeof(smtp_errbuf)-1,"%s",lbuf);
                                                              ^
smtp.c:150:16: note: 'snprintf' output between 1 and 1024 bytes into a destination of size 1023
         (void) snprintf(smtp_errbuf,sizeof(smtp_errbuf)-1,"%s",lbuf);
                ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
smtp.c: In function 'process_embeded_images':
smtp.c:1027:51: warning: '%s' directive output may be truncated writing up to 16 bytes into a region of size between 10 and 19 [-Wformat-truncation=]
         (void) snprintf(tbuf,sizeof(tbuf)-1,"ii%d_%s",ic,cid);
                                                   ^~     ~~~
smtp.c:1027:16: note: 'snprintf' output between 5 and 30 bytes into a destination of size 23
         (void) snprintf(tbuf,sizeof(tbuf)-1,"ii%d_%s",ic,cid);
                ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
rm -f utils.o
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/mailsend-ssl/mailsend-1.19=mailsend-1.19 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -Wall -I. -I./libs/libmutils -I./libs/libmsock -I./libs/libsll  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STRING_H=1 -DHAVE_STRINGS_H=1 -DHAVE_MEMORY_H=1 -DHAVE_MALLOC_H=1 -DHAVE_UNISTD_H=1 -DHAVE_CTYPE_H=1 -DHAVE_STDINT_H=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_STDLIB_H=1 -DHAVE_FCNTL_H=1 -DHAVE_SYS_FILE_H=1 -DHAVE_LIMITS_H=1 -DHAVE_FLOCK=1 -DHAVE_SOCKET=1 -DHAVE_HTONL=1 -DHAVE_GETHOSTNAME=1 -DHAVE_GETHOSTBYADDR=1 -DHAVE_RES_SEARCH=1 -DHAVE_INET_ATON=1 -DHAVE_DN_SKIPNAME=1 -DHAVE_MKSTEMP=1 -DHAVE_GETADDRINFO=1 -DUNIX -DHAVE_STRING_H=1 -DHAVE_STDLIB_H=1 -DHAVE_MATH_H=1 -c utils.c
rm -f setget.o
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/mailsend-ssl/mailsend-1.19=mailsend-1.19 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -Wall -I. -I./libs/libmutils -I./libs/libmsock -I./libs/libsll  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STRING_H=1 -DHAVE_STRINGS_H=1 -DHAVE_MEMORY_H=1 -DHAVE_MALLOC_H=1 -DHAVE_UNISTD_H=1 -DHAVE_CTYPE_H=1 -DHAVE_STDINT_H=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_STDLIB_H=1 -DHAVE_FCNTL_H=1 -DHAVE_SYS_FILE_H=1 -DHAVE_LIMITS_H=1 -DHAVE_FLOCK=1 -DHAVE_SOCKET=1 -DHAVE_HTONL=1 -DHAVE_GETHOSTNAME=1 -DHAVE_GETHOSTBYADDR=1 -DHAVE_RES_SEARCH=1 -DHAVE_INET_ATON=1 -DHAVE_DN_SKIPNAME=1 -DHAVE_MKSTEMP=1 -DHAVE_GETADDRINFO=1 -DUNIX -DHAVE_STRING_H=1 -DHAVE_STDLIB_H=1 -DHAVE_MATH_H=1 -c setget.c
rm -f examples.o
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/mailsend-ssl/mailsend-1.19=mailsend-1.19 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -Wall -I. -I./libs/libmutils -I./libs/libmsock -I./libs/libsll  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STRING_H=1 -DHAVE_STRINGS_H=1 -DHAVE_MEMORY_H=1 -DHAVE_MALLOC_H=1 -DHAVE_UNISTD_H=1 -DHAVE_CTYPE_H=1 -DHAVE_STDINT_H=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_STDLIB_H=1 -DHAVE_FCNTL_H=1 -DHAVE_SYS_FILE_H=1 -DHAVE_LIMITS_H=1 -DHAVE_FLOCK=1 -DHAVE_SOCKET=1 -DHAVE_HTONL=1 -DHAVE_GETHOSTNAME=1 -DHAVE_GETHOSTBYADDR=1 -DHAVE_RES_SEARCH=1 -DHAVE_INET_ATON=1 -DHAVE_DN_SKIPNAME=1 -DHAVE_MKSTEMP=1 -DHAVE_GETADDRINFO=1 -DUNIX -DHAVE_STRING_H=1 -DHAVE_STDLIB_H=1 -DHAVE_MATH_H=1 -c examples.c
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/mailsend-ssl/mailsend-1.19=mailsend-1.19 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -Wall -I. -I./libs/libmutils -I./libs/libmsock -I./libs/libsll  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STRING_H=1 -DHAVE_STRINGS_H=1 -DHAVE_MEMORY_H=1 -DHAVE_MALLOC_H=1 -DHAVE_UNISTD_H=1 -DHAVE_CTYPE_H=1 -DHAVE_STDINT_H=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_STDLIB_H=1 -DHAVE_FCNTL_H=1 -DHAVE_SYS_FILE_H=1 -DHAVE_LIMITS_H=1 -DHAVE_FLOCK=1 -DHAVE_SOCKET=1 -DHAVE_HTONL=1 -DHAVE_GETHOSTNAME=1 -DHAVE_GETHOSTBYADDR=1 -DHAVE_RES_SEARCH=1 -DHAVE_INET_ATON=1 -DHAVE_DN_SKIPNAME=1 -DHAVE_MKSTEMP=1 -DHAVE_GETADDRINFO=1 -DUNIX -DHAVE_STRING_H=1 -DHAVE_STDLIB_H=1 -DHAVE_MATH_H=1 main.o smtp.o utils.o setget.o examples.o -o mailsend ./libs/libmsock/libmsock.a ./libs/libsll/libsll.a ./libs/libmutils/libmutils.a -L/openwrt/staging_dir/target-mips_24kc_musl/usr//lib -lssl -lcrypto  
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ld: cannot find -lssl
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ld: cannot find -lcrypto
collect2: error: ld returned 1 exit status
make[4]: *** [Makefile:63: mailsend] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/mailsend-ssl/mailsend-1.19'
make[3]: *** [Makefile:73: /openwrt/build_dir/target-mips_24kc_musl/mailsend-ssl/mailsend-1.19/.built] Error 2
```
