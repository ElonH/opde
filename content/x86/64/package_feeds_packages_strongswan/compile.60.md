---
title: "compile.60"
date: 2021-02-18 15:10:27.215391
hidden: false
draft: false
weight: -60
---

build number: `60`

path: `package/feeds/packages/strongswan/compile`


``` bash
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1'
make  all-recursive
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1'
Making all in src
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src'
Making all in .
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src'
make[7]: Nothing to be done for 'all-am'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src'
Making all in include
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src/include'
make[7]: Nothing to be done for 'all'.
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src/include'
Making all in libstrongswan
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src/libstrongswan'
make  all-recursive
make[8]: Entering directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src/libstrongswan'
Making all in .
make[9]: Entering directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src/libstrongswan'
make[9]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src/libstrongswan'
Making all in plugins/af_alg
make[9]: Entering directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src/libstrongswan/plugins/af_alg'
make[9]: Nothing to be done for 'all'.
make[9]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src/libstrongswan/plugins/af_alg'
Making all in plugins/aes
make[9]: Entering directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src/libstrongswan/plugins/aes'
make[9]: Nothing to be done for 'all'.
make[9]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src/libstrongswan/plugins/aes'
Making all in plugins/des
make[9]: Entering directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src/libstrongswan/plugins/des'
make[9]: Nothing to be done for 'all'.
make[9]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src/libstrongswan/plugins/des'
Making all in plugins/blowfish
make[9]: Entering directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src/libstrongswan/plugins/blowfish'
make[9]: Nothing to be done for 'all'.
make[9]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src/libstrongswan/plugins/blowfish'
Making all in plugins/rc2
make[9]: Entering directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src/libstrongswan/plugins/rc2'
make[9]: Nothing to be done for 'all'.
make[9]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src/libstrongswan/plugins/rc2'
Making all in plugins/md4
make[9]: Entering directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src/libstrongswan/plugins/md4'
make[9]: Nothing to be done for 'all'.
make[9]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src/libstrongswan/plugins/md4'
Making all in plugins/md5
make[9]: Entering directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src/libstrongswan/plugins/md5'
make[9]: Nothing to be done for 'all'.
make[9]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src/libstrongswan/plugins/md5'
Making all in plugins/sha1
make[9]: Entering directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src/libstrongswan/plugins/sha1'
make[9]: Nothing to be done for 'all'.
make[9]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src/libstrongswan/plugins/sha1'
Making all in plugins/sha2
make[9]: Entering directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src/libstrongswan/plugins/sha2'
make[9]: Nothing to be done for 'all'.
make[9]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src/libstrongswan/plugins/sha2'
Making all in plugins/gmp
make[9]: Entering directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src/libstrongswan/plugins/gmp'
depbase=`echo gmp_rsa_private_key.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/bash ../../../../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I../../../..  -I../../../../src/libstrongswan -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include  -rdynamic -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1=strongswan-5.9.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include  -include /openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/config.h -MT gmp_rsa_private_key.lo -MD -MP -MF $depbase.Tpo -c -o gmp_rsa_private_key.lo gmp_rsa_private_key.c &&\
mv -f $depbase.Tpo $depbase.Plo
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I../../../.. -I../../../../src/libstrongswan -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -rdynamic -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1=strongswan-5.9.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -include /openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/config.h -MT gmp_rsa_private_key.lo -MD -MP -MF .deps/gmp_rsa_private_key.Tpo -c gmp_rsa_private_key.c  -fPIC -DPIC -o .libs/gmp_rsa_private_key.o
depbase=`echo gmp_rsa_public_key.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/bash ../../../../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I../../../..  -I../../../../src/libstrongswan -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include  -rdynamic -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1=strongswan-5.9.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include  -include /openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/config.h -MT gmp_rsa_public_key.lo -MD -MP -MF $depbase.Tpo -c -o gmp_rsa_public_key.lo gmp_rsa_public_key.c &&\
mv -f $depbase.Tpo $depbase.Plo
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I../../../.. -I../../../../src/libstrongswan -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -rdynamic -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1=strongswan-5.9.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -include /openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/config.h -MT gmp_rsa_public_key.lo -MD -MP -MF .deps/gmp_rsa_public_key.Tpo -c gmp_rsa_public_key.c  -fPIC -DPIC -o .libs/gmp_rsa_public_key.o
/bin/bash ../../../../libtool  --tag=CC   --mode=link ccache_cc -rdynamic -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1=strongswan-5.9.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include  -include /openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/config.h -module -avoid-version -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link,/openwrt/staging_dir/target-x86_64_musl/usr/lib -o libstrongswan-gmp.la -rpath /usr/lib/ipsec/plugins gmp_plugin.lo gmp_diffie_hellman.lo gmp_rsa_private_key.lo gmp_rsa_public_key.lo -lgmp 
OpenWrt-libtool: link: rm -fr  .libs/libstrongswan-gmp.la .libs/libstrongswan-gmp.lai .libs/libstrongswan-gmp.so
OpenWrt-libtool: link: ccache_cc -shared  -fPIC -DPIC  .libs/gmp_plugin.o .libs/gmp_diffie_hellman.o .libs/gmp_rsa_private_key.o .libs/gmp_rsa_public_key.o   -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib -lgmp  -Os -fstack-protector -Wl,-z -Wl,now -Wl,-z -Wl,relro -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link -Wl,/openwrt/staging_dir/target-x86_64_musl/usr/lib   -Wl,-soname -Wl,libstrongswan-gmp.so -o .libs/libstrongswan-gmp.so
OpenWrt-libtool: link: ( cd ".libs" && rm -f "libstrongswan-gmp.la" && ln -s "../libstrongswan-gmp.la" "libstrongswan-gmp.la" )
make[9]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src/libstrongswan/plugins/gmp'
Making all in plugins/gmpdh
make[9]: Entering directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src/libstrongswan/plugins/gmpdh'
depbase=`echo ../gmp/gmp_diffie_hellman.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/bash ../../../../libtool  --tag=CC   --mode=compile ccache_cc -DHAVE_CONFIG_H -I. -I../../../..  -I../../../../src/libstrongswan -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include  -rdynamic -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1=strongswan-5.9.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include  -include /openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/config.h -MT ../gmp/gmp_diffie_hellman.lo -MD -MP -MF $depbase.Tpo -c -o ../gmp/gmp_diffie_hellman.lo ../gmp/gmp_diffie_hellman.c &&\
mv -f $depbase.Tpo $depbase.Plo
OpenWrt-libtool: compile:  ccache_cc -DHAVE_CONFIG_H -I. -I../../../.. -I../../../../src/libstrongswan -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -rdynamic -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1=strongswan-5.9.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -include /openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/config.h -MT ../gmp/gmp_diffie_hellman.lo -MD -MP -MF ../gmp/.deps/gmp_diffie_hellman.Tpo -c ../gmp/gmp_diffie_hellman.c  -fPIC -DPIC -o ../gmp/.libs/gmp_diffie_hellman.o
/bin/bash ../../../../libtool  --tag=CC   --mode=link ccache_cc -rdynamic -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1=strongswan-5.9.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include  -include /openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/config.h -module -avoid-version -Wl,-Bstatic -Wl,-lgmp -Wl,-Bdynamic -Wl,--as-needed -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link,/openwrt/staging_dir/target-x86_64_musl/usr/lib -o libstrongswan-gmpdh.la -rpath /usr/lib/ipsec/plugins gmpdh_plugin.lo ../gmp/gmp_diffie_hellman.lo  
OpenWrt-libtool: link: ccache_cc -shared  -fPIC -DPIC  .libs/gmpdh_plugin.o ../gmp/.libs/gmp_diffie_hellman.o   -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib  -Os -fstack-protector -Wl,-z -Wl,now -Wl,-z -Wl,relro -Wl,-Bstatic -Wl,-lgmp -Wl,-Bdynamic -Wl,--as-needed -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link -Wl,/openwrt/staging_dir/target-x86_64_musl/usr/lib   -Wl,-soname -Wl,libstrongswan-gmpdh.so -o .libs/libstrongswan-gmpdh.so
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libgmp.a(bdiv_q_1.o): relocation R_X86_64_PC32 against symbol `__gmp_binvert_limb_table' can not be used when making a shared object; recompile with -fPIC
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib/gcc/x86_64-openwrt-linux-musl/8.4.0/../../../../x86_64-openwrt-linux-musl/bin/ld: final link failed: bad value
collect2: error: ld returned 1 exit status
make[9]: *** [Makefile:560: libstrongswan-gmpdh.la] Error 1
make[9]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src/libstrongswan/plugins/gmpdh'
make[8]: *** [Makefile:2092: all-recursive] Error 1
make[8]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src/libstrongswan'
make[7]: *** [Makefile:1208: all] Error 2
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src/libstrongswan'
make[6]: *** [Makefile:533: all-recursive] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/src'
make[5]: *** [Makefile:594: all-recursive] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1'
make[4]: *** [Makefile:505: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1'
make[3]: *** [Makefile:600: /openwrt/build_dir/target-x86_64_musl/strongswan-5.9.1/.built] Error 2
```
