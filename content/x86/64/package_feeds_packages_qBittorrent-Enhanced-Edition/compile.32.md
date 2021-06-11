---
title: "compile.32"
date: 2021-06-11 17:52:12.514785
hidden: false
draft: false
weight: -32
---

build number: `32`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/qBittorrent-Enhanced-Edition/compile -j$(nproc) || make package/feeds/packages/qBittorrent-Enhanced-Edition/compile V=s
```

#### Compile.txt

``` bash
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/x86_64
checking for x86_64-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether the compiler supports GNU C... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to enable C11 features... none needed
checking whether ccache_cc understands -c and -o together... yes
checking whether the compiler supports GNU C++... yes
checking whether ccache_cxx accepts -g... yes
checking for ccache_cxx option to enable C++11 features... none needed
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-openwrt-linux-gnu
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for x86_64-openwrt-linux-strip... x86_64-openwrt-linux-musl-strip
checking for a race-free mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports the include directive... yes (GNU style)
checking whether make supports nested variables... yes
checking dependency style of ccache_cc... none
checking dependency style of ccache_cxx... none
checking whether OS is FreeBSD... no
checking whether OS is macOS... no
checking pkg-config is at least version 0.23... yes
checking whether to enable the Debug build... no
checking whether to enable the stacktrace feature... no
checking whether to enable the GUI... no
checking whether to install the systemd service file... no
checking whether to enable the WebUI... yes
checking for Qt5 qmake >= 5.11... /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/bin/qmake
checking whether QtDBus should be enabled... no
checking for boostlib >= 1.65 (106500) includes in "/openwrt/staging_dir/target-x86_64_musl/usr/include"... yes
checking for boostlib >= 1.65 (106500) lib path in "/openwrt/staging_dir/target-x86_64_musl/usr/lib/x86_64-linux-gnu"... no
checking for boostlib >= 1.65 (106500) lib path in "/openwrt/staging_dir/target-x86_64_musl/usr/lib64"... no
checking for boostlib >= 1.65 (106500) lib path in "/openwrt/staging_dir/target-x86_64_musl/usr/libx32"... no
checking for boostlib >= 1.65 (106500) lib path in "/openwrt/staging_dir/target-x86_64_musl/usr/lib"... yes
checking for boostlib >= 1.65 (106500)... yes
configure: Boost CXXFLAGS: "-I/openwrt/staging_dir/target-x86_64_musl/usr/include"
configure: Boost LDFLAGS: "-L/openwrt/staging_dir/target-x86_64_musl/usr/lib"
checking whether the Boost::System library is available... yes
checking for exit in -lboost_system... yes
configure: Boost.System LIB: "-lboost_system"
checking for libtorrent... yes
checking for openssl... yes
checking for zlib... yes
checking if compiler defaults to C++17 or later mode... no
checking if compiler supports C++17... yes
checking if C++17 is disabled by the set compiler flags... no
configure: WARNING: C++17 mode is now force enabled. The C++ mode should match the mode that other libraries were built with, otherwise you'll likely get linking errors.
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating conf.pri
config.status: executing depfiles commands
configure: WARNING: unrecognized options: --disable-nls
configure: Running qmake to generate the makefile...
Info: creating stash file /openwrt/build_dir/target-x86_64_musl/qBittorrent-Enhanced-Edition-release-4.3.4.10/.qmake.stash
Reading /openwrt/build_dir/target-x86_64_musl/qBittorrent-Enhanced-Edition-release-4.3.4.10/src/src.pro
Project MESSAGE: Project is built in RELEASE mode.
Project MESSAGE: Disabling debug output.

configure: Good, the configure finished.

make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/qBittorrent-Enhanced-Edition-release-4.3.4.10'
cd src/ && ( test -e Makefile || /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/bin/qmake -o Makefile /openwrt/build_dir/target-x86_64_musl/qBittorrent-Enhanced-Edition-release-4.3.4.10/src/src.pro QMAKE_LRELEASE= ) && make -f Makefile 
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/qBittorrent-Enhanced-Edition-release-4.3.4.10/src'
lrelease webui/www/translations/webui_ar.ts
lrelease webui/www/translations/webui_az@latin.ts
lrelease webui/www/translations/webui_be.ts
lrelease webui/www/translations/webui_bg.ts
lrelease webui/www/translations/webui_ca.ts
lrelease webui/www/translations/webui_cs.ts
lrelease webui/www/translations/webui_da.ts
lrelease webui/www/translations/webui_de.ts
lrelease webui/www/translations/webui_el.ts
lrelease webui/www/translations/webui_en.ts
lrelease webui/www/translations/webui_en_AU.ts
lrelease webui/www/translations/webui_en_GB.ts
lrelease webui/www/translations/webui_eo.ts
lrelease webui/www/translations/webui_es.ts
lrelease webui/www/translations/webui_et.ts
lrelease webui/www/translations/webui_eu.ts
lrelease webui/www/translations/webui_fi.ts
lrelease webui/www/translations/webui_fr.ts
lrelease webui/www/translations/webui_gl.ts
lrelease webui/www/translations/webui_he.ts
lrelease webui/www/translations/webui_hi_IN.ts
lrelease webui/www/translations/webui_hr.ts
lrelease webui/www/translations/webui_hu.ts
lrelease webui/www/translations/webui_hy.ts
lrelease webui/www/translations/webui_id.ts
lrelease webui/www/translations/webui_is.ts
lrelease webui/www/translations/webui_it.ts
lrelease webui/www/translations/webui_ja.ts
lrelease webui/www/translations/webui_ka.ts
lrelease webui/www/translations/webui_ko.ts
lrelease webui/www/translations/webui_lt.ts
lrelease webui/www/translations/webui_ltg.ts
lrelease webui/www/translations/webui_lv_LV.ts
lrelease webui/www/translations/webui_ms_MY.ts
lrelease webui/www/translations/webui_nb.ts
lrelease webui/www/translations/webui_nl.ts
lrelease webui/www/translations/webui_oc.ts
lrelease webui/www/translations/webui_pl.ts
lrelease webui/www/translations/webui_pt_BR.ts
lrelease webui/www/translations/webui_pt_PT.ts
lrelease webui/www/translations/webui_ro.ts
lrelease webui/www/translations/webui_ru.ts
lrelease webui/www/translations/webui_sk.ts
lrelease webui/www/translations/webui_sl.ts
lrelease webui/www/translations/webui_sr.ts
lrelease webui/www/translations/webui_sv.ts
lrelease webui/www/translations/webui_tr.ts
lrelease webui/www/translations/webui_uk.ts
lrelease webui/www/translations/webui_uz@Latn.ts
lrelease webui/www/translations/webui_vi.ts
lrelease webui/www/translations/webui_zh.ts
lrelease webui/www/translations/webui_zh_HK.ts
lrelease webui/www/translations/webui_zh_TW.ts
lrelease lang/qbittorrent_ar.ts
lrelease lang/qbittorrent_az@latin.ts
lrelease lang/qbittorrent_be.ts
lrelease lang/qbittorrent_bg.ts
lrelease lang/qbittorrent_ca.ts
lrelease lang/qbittorrent_cs.ts
lrelease lang/qbittorrent_da.ts
lrelease lang/qbittorrent_de.ts
lrelease lang/qbittorrent_el.ts
lrelease lang/qbittorrent_en.ts
lrelease lang/qbittorrent_en_AU.ts
lrelease lang/qbittorrent_en_GB.ts
lrelease lang/qbittorrent_eo.ts
lrelease lang/qbittorrent_es.ts
lrelease lang/qbittorrent_et.ts
lrelease lang/qbittorrent_eu.ts
lrelease lang/qbittorrent_fi.ts
lrelease lang/qbittorrent_fr.ts
lrelease lang/qbittorrent_gl.ts
lrelease lang/qbittorrent_he.ts
lrelease lang/qbittorrent_hi_IN.ts
lrelease lang/qbittorrent_hr.ts
lrelease lang/qbittorrent_hu.ts
lrelease lang/qbittorrent_hy.ts
lrelease lang/qbittorrent_id.ts
lrelease lang/qbittorrent_is.ts
lrelease lang/qbittorrent_it.ts
lrelease lang/qbittorrent_ja.ts
lrelease lang/qbittorrent_ka.ts
lrelease lang/qbittorrent_ko.ts
lrelease lang/qbittorrent_lt.ts
lrelease lang/qbittorrent_ltg.ts
lrelease lang/qbittorrent_lv_LV.ts
lrelease lang/qbittorrent_ms_MY.ts
lrelease lang/qbittorrent_nb.ts
lrelease lang/qbittorrent_nl.ts
lrelease lang/qbittorrent_oc.ts
lrelease lang/qbittorrent_pl.ts
lrelease lang/qbittorrent_pt_BR.ts
lrelease lang/qbittorrent_pt_PT.ts
lrelease lang/qbittorrent_ro.ts
lrelease lang/qbittorrent_ru.ts
lrelease lang/qbittorrent_sk.ts
lrelease lang/qbittorrent_sl.ts
lrelease lang/qbittorrent_sr.ts
lrelease lang/qbittorrent_sv.ts
lrelease lang/qbittorrent_tr.ts
lrelease lang/qbittorrent_uk.ts
lrelease lang/qbittorrent_uz@Latn.ts
lrelease lang/qbittorrent_vi.ts
lrelease lang/qbittorrent_zh.ts
lrelease lang/qbittorrent_zh_HK.ts
lrelease lang/qbittorrent_zh_TW.ts
ccache_cxx -c -pipe -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/qt-everywhere-src-5.15.2=qt-everywhere-src-5.15.2 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro --sysroot=/openwrt/staging_dir/target-x86_64_musl -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/qBittorrent-Enhanced-Edition-release-4.3.4.10=qBittorrent-Enhanced-Edition-release-4.3.4.10 -Wformat -Werror=format-security -fstack-protector -Wl,-z,now -Wl,-z,relro -fexceptions -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/qBittorrent-Enhanced-Edition-release-4.3.4.10=qBittorrent-Enhanced-Edition-release-4.3.4.10 -Wformat -Werror=format-security -fstack-protector -Wl,-z,now -Wl,-z,relro -Wall -Wextra -Wpedantic -Wformat-security -O2 -std=gnu++1z -D_REENTRANT -Wall -Wextra -fPIC -D_FORTIFY_SOURCE=1 -DTORRENT_LINKING_SHARED -DBOOST_ASIO_ENABLE_CANCELIO -DTORRENT_USE_ICONV -DTORRENT_USE_OPENSSL -DTORRENT_USE_LIBCRYPTO -D_FORTIFY_SOURCE=1 -DDISABLE_GUI -DQT_NO_DEBUG_OUTPUT -DQT_DEPRECATED_WARNINGS -DQT_NO_CAST_TO_ASCII -DQT_NO_CAST_FROM_BYTEARRAY -DQT_USE_QSTRINGBUILDER -DQT_STRICT_ITERATORS -DQT_NO_DEBUG -DQT_NETWORK_LIB -DQT_XML_LIB -DQT_SQL_LIB -DQT_CORE_LIB -I. -I/usr/include -I. -Iapp -I../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtNetwork -I../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtXml -I../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtSql -I../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore -I. -I../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/mkspecs/linux-openwrt-g++ -o application.o app/application.cpp
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/cstdlib:75,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/stl_algo.h:59,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/algorithm:62,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qglobal.h:142,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/stdlib.h:44:1: error: '_Noreturn' does not name a type
 _Noreturn void abort (void);
 ^~~~~~~~~
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/stdlib.h:46:1: error: '_Noreturn' does not name a type
 _Noreturn void exit (int);
 ^~~~~~~~~
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/stdlib.h:47:1: error: '_Noreturn' does not name a type
 _Noreturn void _Exit (int);
 ^~~~~~~~~
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/stdlib.h:49:1: error: '_Noreturn' does not name a type
 _Noreturn void quick_exit (int);
 ^~~~~~~~~
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/stl_algo.h:59,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/algorithm:62,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qglobal.h:142,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/cstdlib:130:11: error: '::abort' has not been declared
   using ::abort;
           ^~~~~
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/cstdlib:146:11: error: '::exit' has not been declared
   using ::exit;
           ^~~~
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/cstdlib:160:11: error: '::quick_exit' has not been declared
   using ::quick_exit;
           ^~~~~~~~~~
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/cstdlib:206:11: error: '::_Exit' has not been declared
   using ::_Exit;
           ^~~~~
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/cstdlib:242:22: error: '__gnu_cxx::_Exit' has not been declared
   using ::__gnu_cxx::_Exit;
                      ^~~~~
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/cwchar:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/postypes.h:40,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/char_traits.h:40,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:40,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/usr/include/wchar.h:600:9: error: '__gnuc_va_list' has not been declared
         __gnuc_va_list __arg)
         ^~~~~~~~~~~~~~
/usr/include/wchar.h:607:8: error: '__gnuc_va_list' has not been declared
        __gnuc_va_list __arg)
        ^~~~~~~~~~~~~~
/usr/include/wchar.h:613:9: error: '__gnuc_va_list' has not been declared
         __gnuc_va_list __arg)
         ^~~~~~~~~~~~~~
/usr/include/wchar.h:673:8: error: '__gnuc_va_list' has not been declared
        __gnuc_va_list __arg)
        ^~~~~~~~~~~~~~
/usr/include/wchar.h:680:7: error: '__gnuc_va_list' has not been declared
       __gnuc_va_list __arg)
       ^~~~~~~~~~~~~~
/usr/include/wchar.h:685:8: error: '__gnuc_va_list' has not been declared
        __gnuc_va_list __arg)
        ^~~~~~~~~~~~~~
In file included from /usr/include/features.h:461,
                 from /usr/include/assert.h:35,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qglobal.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/usr/include/wchar.h:693:12: error: '__gnuc_va_list' has not been declared
 extern int __REDIRECT (vfwscanf, (__FILE *__restrict __s,
            ^~~~~~~~~~
/usr/include/wchar.h:697:12: error: '__gnuc_va_list' has not been declared
 extern int __REDIRECT (vwscanf, (const wchar_t *__restrict __format,
            ^~~~~~~~~~
/usr/include/wchar.h:700:12: error: '__gnuc_va_list' has not been declared
 extern int __REDIRECT_NTH (vswscanf, (const wchar_t *__restrict __s,
            ^~~~~~~~~~~~~~
In file included from /usr/include/wchar.h:849,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/cwchar:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/postypes.h:40,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/char_traits.h:40,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:40,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/usr/include/bits/wchar2.h:306:8: error: '__gnuc_va_list' has not been declared
        __gnuc_va_list __arg)
        ^~~~~~~~~~~~~~
In file included from /usr/include/features.h:461,
                 from /usr/include/assert.h:35,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qglobal.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/usr/include/bits/wchar2.h:309:12: error: '__gnuc_va_list' has not been declared
 extern int __REDIRECT_NTH_LDBL (__vswprintf_alias,
            ^~~~~~~~~~~~~~~~~~~
/usr/include/bits/wchar2.h:315:1: error: '__gnuc_va_list' has not been declared
 __NTH (vswprintf (wchar_t *__restrict __s, size_t __n,
 ^~~~~
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/cstdio:42,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:43,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6400,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/usr/include/stdio.h:52:9: error: '__gnuc_va_list' does not name a type; did you mean 'va_list'?
 typedef __gnuc_va_list va_list;
         ^~~~~~~~~~~~~~
         va_list
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/cstdio:42,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:43,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6400,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/usr/include/stdio.h:342:8: error: '__gnuc_va_list' has not been declared
        __gnuc_va_list __arg);
        ^~~~~~~~~~~~~~
/usr/include/stdio.h:347:54: error: '__gnuc_va_list' has not been declared
 extern int vprintf (const char *__restrict __format, __gnuc_va_list __arg);
                                                      ^~~~~~~~~~~~~~
/usr/include/stdio.h:350:8: error: '__gnuc_va_list' has not been declared
        __gnuc_va_list __arg) __THROWNL;
        ^~~~~~~~~~~~~~
/usr/include/stdio.h:359:42: error: '__gnuc_va_list' has not been declared
         const char *__restrict __format, __gnuc_va_list __arg)
                                          ^~~~~~~~~~~~~~
/usr/include/stdio.h:367:9: error: '__gnuc_va_list' has not been declared
         __gnuc_va_list __arg)
         ^~~~~~~~~~~~~~
/usr/include/stdio.h:380:8: error: '__gnuc_va_list' has not been declared
        __gnuc_va_list __arg)
        ^~~~~~~~~~~~~~
/usr/include/stdio.h:433:7: error: '__gnuc_va_list' has not been declared
       __gnuc_va_list __arg)
       ^~~~~~~~~~~~~~
/usr/include/stdio.h:440:53: error: '__gnuc_va_list' has not been declared
 extern int vscanf (const char *__restrict __format, __gnuc_va_list __arg)
                                                     ^~~~~~~~~~~~~~
/usr/include/stdio.h:445:40: error: '__gnuc_va_list' has not been declared
       const char *__restrict __format, __gnuc_va_list __arg)
                                        ^~~~~~~~~~~~~~
In file included from /usr/include/features.h:461,
                 from /usr/include/assert.h:35,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qglobal.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/usr/include/stdio.h:451:12: error: '__gnuc_va_list' has not been declared
 extern int __REDIRECT (vfscanf,
            ^~~~~~~~~~
/usr/include/stdio.h:456:12: error: '__gnuc_va_list' has not been declared
 extern int __REDIRECT (vscanf, (const char *__restrict __format,
            ^~~~~~~~~~
/usr/include/stdio.h:459:12: error: '__gnuc_va_list' has not been declared
 extern int __REDIRECT_NTH (vsscanf,
            ^~~~~~~~~~~~~~
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/cstdio:42,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:43,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6400,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/usr/include/stdio.h:831:8: error: '__gnuc_va_list' has not been declared
        __gnuc_va_list __args)
        ^~~~~~~~~~~~~~
In file included from /usr/include/stdio.h:867,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/cstdio:42,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:43,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6400,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/usr/include/bits/stdio2.h:30:7: error: '__gnuc_va_list' has not been declared
       __gnuc_va_list __ap) __THROW;
       ^~~~~~~~~~~~~~
In file included from /usr/include/features.h:461,
                 from /usr/include/assert.h:35,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qglobal.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/usr/include/bits/stdio2.h:46:1: error: '__gnuc_va_list' has not been declared
 __NTH (vsprintf (char *__restrict __s, const char *__restrict __fmt,
 ^~~~~
In file included from /usr/include/stdio.h:867,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/cstdio:42,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:43,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6400,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/usr/include/bits/stdio2.h: In function 'int vsprintf(char*, const char*, int)':
/usr/include/bits/stdio2.h:50:28: error: invalid conversion from 'int' to '__va_list_tag*' [-fpermissive]
        __bos (__s), __fmt, __ap);
                            ^~~~
<built-in>: note:   initializing argument 5 of 'int __builtin___vsprintf_chk(char*, int, long unsigned int, const char*, __va_list_tag*)'
/usr/include/bits/stdio2.h: At global scope:
/usr/include/bits/stdio2.h:60:8: error: '__gnuc_va_list' has not been declared
        __gnuc_va_list __ap) __THROW;
        ^~~~~~~~~~~~~~
In file included from /usr/include/features.h:461,
                 from /usr/include/assert.h:35,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qglobal.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/usr/include/bits/stdio2.h:77:1: error: '__gnuc_va_list' has not been declared
 __NTH (vsnprintf (char *__restrict __s, size_t __n,
 ^~~~~
In file included from /usr/include/stdio.h:867,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/cstdio:42,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:43,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6400,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/usr/include/bits/stdio2.h: In function 'int vsnprintf(char*, size_t, const char*, int)':
/usr/include/bits/stdio2.h:81:29: error: invalid conversion from 'int' to '__va_list_tag*' [-fpermissive]
         __bos (__s), __fmt, __ap);
                             ^~~~
<built-in>: note:   initializing argument 6 of 'int __builtin___vsnprintf_chk(char*, long unsigned int, int, long unsigned int, const char*, __va_list_tag*)'
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h: In function 'std::string std::to_string(int)':
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6455:20: error: no matching function for call to '__to_xstring<std::string>(int (*)(char*, size_t, const char*, int) noexcept, long unsigned int, const char [3], int&)'
         "%d", __val); }
                    ^
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6400,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note: candidate: 'template<class _String, class _CharT> _String __gnu_cxx::__to_xstring(int (*)(_CharT*, std::size_t, const _CharT*, __va_list_tag*), std::size_t, const _CharT*, ...)'
     __to_xstring(int (*__convf) (_CharT*, std::size_t, const _CharT*,
     ^~~~~~~~~~~~
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note:   template argument deduction/substitution failed:
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6455:20: note:   mismatched types '__va_list_tag*' and 'int'
         "%d", __val); }
                    ^
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h: In function 'std::string std::to_string(unsigned int)':
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6461:20: error: no matching function for call to '__to_xstring<std::string>(int (*)(char*, size_t, const char*, int) noexcept, long unsigned int, const char [3], unsigned int&)'
         "%u", __val); }
                    ^
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6400,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note: candidate: 'template<class _String, class _CharT> _String __gnu_cxx::__to_xstring(int (*)(_CharT*, std::size_t, const _CharT*, __va_list_tag*), std::size_t, const _CharT*, ...)'
     __to_xstring(int (*__convf) (_CharT*, std::size_t, const _CharT*,
     ^~~~~~~~~~~~
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note:   template argument deduction/substitution failed:
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6461:20: note:   mismatched types '__va_list_tag*' and 'int'
         "%u", __val); }
                    ^
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h: In function 'std::string std::to_string(long int)':
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6466:21: error: no matching function for call to '__to_xstring<std::string>(int (*)(char*, size_t, const char*, int) noexcept, long unsigned int, const char [4], long int&)'
         "%ld", __val); }
                     ^
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6400,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note: candidate: 'template<class _String, class _CharT> _String __gnu_cxx::__to_xstring(int (*)(_CharT*, std::size_t, const _CharT*, __va_list_tag*), std::size_t, const _CharT*, ...)'
     __to_xstring(int (*__convf) (_CharT*, std::size_t, const _CharT*,
     ^~~~~~~~~~~~
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note:   template argument deduction/substitution failed:
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6466:21: note:   mismatched types '__va_list_tag*' and 'int'
         "%ld", __val); }
                     ^
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h: In function 'std::string std::to_string(long unsigned int)':
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6472:21: error: no matching function for call to '__to_xstring<std::string>(int (*)(char*, size_t, const char*, int) noexcept, long unsigned int, const char [4], long unsigned int&)'
         "%lu", __val); }
                     ^
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6400,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note: candidate: 'template<class _String, class _CharT> _String __gnu_cxx::__to_xstring(int (*)(_CharT*, std::size_t, const _CharT*, __va_list_tag*), std::size_t, const _CharT*, ...)'
     __to_xstring(int (*__convf) (_CharT*, std::size_t, const _CharT*,
     ^~~~~~~~~~~~
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note:   template argument deduction/substitution failed:
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6472:21: note:   mismatched types '__va_list_tag*' and 'int'
         "%lu", __val); }
                     ^
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h: In function 'std::string std::to_string(long long int)':
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6478:22: error: no matching function for call to '__to_xstring<std::string>(int (*)(char*, size_t, const char*, int) noexcept, long unsigned int, const char [5], long long int&)'
         "%lld", __val); }
                      ^
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6400,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note: candidate: 'template<class _String, class _CharT> _String __gnu_cxx::__to_xstring(int (*)(_CharT*, std::size_t, const _CharT*, __va_list_tag*), std::size_t, const _CharT*, ...)'
     __to_xstring(int (*__convf) (_CharT*, std::size_t, const _CharT*,
     ^~~~~~~~~~~~
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note:   template argument deduction/substitution failed:
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6478:22: note:   mismatched types '__va_list_tag*' and 'int'
         "%lld", __val); }
                      ^
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h: In function 'std::string std::to_string(long long unsigned int)':
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6484:22: error: no matching function for call to '__to_xstring<std::string>(int (*)(char*, size_t, const char*, int) noexcept, long unsigned int, const char [5], long long unsigned int&)'
         "%llu", __val); }
                      ^
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6400,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note: candidate: 'template<class _String, class _CharT> _String __gnu_cxx::__to_xstring(int (*)(_CharT*, std::size_t, const _CharT*, __va_list_tag*), std::size_t, const _CharT*, ...)'
     __to_xstring(int (*__convf) (_CharT*, std::size_t, const _CharT*,
     ^~~~~~~~~~~~
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note:   template argument deduction/substitution failed:
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6484:22: note:   mismatched types '__va_list_tag*' and 'int'
         "%llu", __val); }
                      ^
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h: In function 'std::string std::to_string(float)':
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6492:20: error: no matching function for call to '__to_xstring<std::string>(int (*)(char*, size_t, const char*, int) noexcept, const int&, const char [3], float&)'
         "%f", __val);
                    ^
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6400,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note: candidate: 'template<class _String, class _CharT> _String __gnu_cxx::__to_xstring(int (*)(_CharT*, std::size_t, const _CharT*, __va_list_tag*), std::size_t, const _CharT*, ...)'
     __to_xstring(int (*__convf) (_CharT*, std::size_t, const _CharT*,
     ^~~~~~~~~~~~
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note:   template argument deduction/substitution failed:
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6492:20: note:   mismatched types '__va_list_tag*' and 'int'
         "%f", __val);
                    ^
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h: In function 'std::string std::to_string(double)':
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6501:20: error: no matching function for call to '__to_xstring<std::string>(int (*)(char*, size_t, const char*, int) noexcept, const int&, const char [3], double&)'
         "%f", __val);
                    ^
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6400,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note: candidate: 'template<class _String, class _CharT> _String __gnu_cxx::__to_xstring(int (*)(_CharT*, std::size_t, const _CharT*, __va_list_tag*), std::size_t, const _CharT*, ...)'
     __to_xstring(int (*__convf) (_CharT*, std::size_t, const _CharT*,
     ^~~~~~~~~~~~
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note:   template argument deduction/substitution failed:
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6501:20: note:   mismatched types '__va_list_tag*' and 'int'
         "%f", __val);
                    ^
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h: In function 'std::string std::to_string(long double)':
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6510:21: error: no matching function for call to '__to_xstring<std::string>(int (*)(char*, size_t, const char*, int) noexcept, const int&, const char [4], long double&)'
         "%Lf", __val);
                     ^
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6400,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note: candidate: 'template<class _String, class _CharT> _String __gnu_cxx::__to_xstring(int (*)(_CharT*, std::size_t, const _CharT*, __va_list_tag*), std::size_t, const _CharT*, ...)'
     __to_xstring(int (*__convf) (_CharT*, std::size_t, const _CharT*,
     ^~~~~~~~~~~~
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note:   template argument deduction/substitution failed:
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6510:21: note:   mismatched types '__va_list_tag*' and 'int'
         "%Lf", __val);
                     ^
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h: In function 'std::wstring std::to_wstring(int)':
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6558:22: error: no matching function for call to '__to_xstring<std::wstring>(int (*)(wchar_t*, size_t, const wchar_t*, int) noexcept, long unsigned int, const wchar_t [3], int&)'
          L"%d", __val); }
                      ^
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6400,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note: candidate: 'template<class _String, class _CharT> _String __gnu_cxx::__to_xstring(int (*)(_CharT*, std::size_t, const _CharT*, __va_list_tag*), std::size_t, const _CharT*, ...)'
     __to_xstring(int (*__convf) (_CharT*, std::size_t, const _CharT*,
     ^~~~~~~~~~~~
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note:   template argument deduction/substitution failed:
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6558:22: note:   mismatched types '__va_list_tag*' and 'int'
          L"%d", __val); }
                      ^
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h: In function 'std::wstring std::to_wstring(unsigned int)':
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6564:22: error: no matching function for call to '__to_xstring<std::wstring>(int (*)(wchar_t*, size_t, const wchar_t*, int) noexcept, long unsigned int, const wchar_t [3], unsigned int&)'
          L"%u", __val); }
                      ^
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6400,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note: candidate: 'template<class _String, class _CharT> _String __gnu_cxx::__to_xstring(int (*)(_CharT*, std::size_t, const _CharT*, __va_list_tag*), std::size_t, const _CharT*, ...)'
     __to_xstring(int (*__convf) (_CharT*, std::size_t, const _CharT*,
     ^~~~~~~~~~~~
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note:   template argument deduction/substitution failed:
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6564:22: note:   mismatched types '__va_list_tag*' and 'int'
          L"%u", __val); }
                      ^
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h: In function 'std::wstring std::to_wstring(long int)':
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6569:23: error: no matching function for call to '__to_xstring<std::wstring>(int (*)(wchar_t*, size_t, const wchar_t*, int) noexcept, long unsigned int, const wchar_t [4], long int&)'
          L"%ld", __val); }
                       ^
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6400,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note: candidate: 'template<class _String, class _CharT> _String __gnu_cxx::__to_xstring(int (*)(_CharT*, std::size_t, const _CharT*, __va_list_tag*), std::size_t, const _CharT*, ...)'
     __to_xstring(int (*__convf) (_CharT*, std::size_t, const _CharT*,
     ^~~~~~~~~~~~
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note:   template argument deduction/substitution failed:
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6569:23: note:   mismatched types '__va_list_tag*' and 'int'
          L"%ld", __val); }
                       ^
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h: In function 'std::wstring std::to_wstring(long unsigned int)':
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6575:23: error: no matching function for call to '__to_xstring<std::wstring>(int (*)(wchar_t*, size_t, const wchar_t*, int) noexcept, long unsigned int, const wchar_t [4], long unsigned int&)'
          L"%lu", __val); }
                       ^
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6400,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note: candidate: 'template<class _String, class _CharT> _String __gnu_cxx::__to_xstring(int (*)(_CharT*, std::size_t, const _CharT*, __va_list_tag*), std::size_t, const _CharT*, ...)'
     __to_xstring(int (*__convf) (_CharT*, std::size_t, const _CharT*,
     ^~~~~~~~~~~~
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note:   template argument deduction/substitution failed:
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6575:23: note:   mismatched types '__va_list_tag*' and 'int'
          L"%lu", __val); }
                       ^
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h: In function 'std::wstring std::to_wstring(long long int)':
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6581:24: error: no matching function for call to '__to_xstring<std::wstring>(int (*)(wchar_t*, size_t, const wchar_t*, int) noexcept, long unsigned int, const wchar_t [5], long long int&)'
          L"%lld", __val); }
                        ^
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6400,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note: candidate: 'template<class _String, class _CharT> _String __gnu_cxx::__to_xstring(int (*)(_CharT*, std::size_t, const _CharT*, __va_list_tag*), std::size_t, const _CharT*, ...)'
     __to_xstring(int (*__convf) (_CharT*, std::size_t, const _CharT*,
     ^~~~~~~~~~~~
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note:   template argument deduction/substitution failed:
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6581:24: note:   mismatched types '__va_list_tag*' and 'int'
          L"%lld", __val); }
                        ^
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h: In function 'std::wstring std::to_wstring(long long unsigned int)':
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6587:24: error: no matching function for call to '__to_xstring<std::wstring>(int (*)(wchar_t*, size_t, const wchar_t*, int) noexcept, long unsigned int, const wchar_t [5], long long unsigned int&)'
          L"%llu", __val); }
                        ^
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6400,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note: candidate: 'template<class _String, class _CharT> _String __gnu_cxx::__to_xstring(int (*)(_CharT*, std::size_t, const _CharT*, __va_list_tag*), std::size_t, const _CharT*, ...)'
     __to_xstring(int (*__convf) (_CharT*, std::size_t, const _CharT*,
     ^~~~~~~~~~~~
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note:   template argument deduction/substitution failed:
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6587:24: note:   mismatched types '__va_list_tag*' and 'int'
          L"%llu", __val); }
                        ^
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h: In function 'std::wstring std::to_wstring(float)':
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6595:22: error: no matching function for call to '__to_xstring<std::wstring>(int (*)(wchar_t*, size_t, const wchar_t*, int) noexcept, const int&, const wchar_t [3], float&)'
          L"%f", __val);
                      ^
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6400,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note: candidate: 'template<class _String, class _CharT> _String __gnu_cxx::__to_xstring(int (*)(_CharT*, std::size_t, const _CharT*, __va_list_tag*), std::size_t, const _CharT*, ...)'
     __to_xstring(int (*__convf) (_CharT*, std::size_t, const _CharT*,
     ^~~~~~~~~~~~
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note:   template argument deduction/substitution failed:
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6595:22: note:   mismatched types '__va_list_tag*' and 'int'
          L"%f", __val);
                      ^
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h: In function 'std::wstring std::to_wstring(double)':
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6604:22: error: no matching function for call to '__to_xstring<std::wstring>(int (*)(wchar_t*, size_t, const wchar_t*, int) noexcept, const int&, const wchar_t [3], double&)'
          L"%f", __val);
                      ^
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6400,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note: candidate: 'template<class _String, class _CharT> _String __gnu_cxx::__to_xstring(int (*)(_CharT*, std::size_t, const _CharT*, __va_list_tag*), std::size_t, const _CharT*, ...)'
     __to_xstring(int (*__convf) (_CharT*, std::size_t, const _CharT*,
     ^~~~~~~~~~~~
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note:   template argument deduction/substitution failed:
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6604:22: note:   mismatched types '__va_list_tag*' and 'int'
          L"%f", __val);
                      ^
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h: In function 'std::wstring std::to_wstring(long double)':
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6613:23: error: no matching function for call to '__to_xstring<std::wstring>(int (*)(wchar_t*, size_t, const wchar_t*, int) noexcept, const int&, const wchar_t [4], long double&)'
          L"%Lf", __val);
                       ^
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6400,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note: candidate: 'template<class _String, class _CharT> _String __gnu_cxx::__to_xstring(int (*)(_CharT*, std::size_t, const _CharT*, __va_list_tag*), std::size_t, const _CharT*, ...)'
     __to_xstring(int (*__convf) (_CharT*, std::size_t, const _CharT*,
     ^~~~~~~~~~~~
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/ext/string_conversions.h:99:5: note:   template argument deduction/substitution failed:
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/string:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qbytearray.h:52,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:50,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/x86_64-openwrt-linux-musl/include/c++/8.4.0/bits/basic_string.h:6613:23: note:   mismatched types '__va_list_tag*' and 'int'
          L"%Lf", __val);
                       ^
app/application.cpp: In member function 'void Application::processMessage(const QString&)':
app/application.cpp:305:73: warning: 'SkipEmptyParts' is deprecated [-Wdeprecated-declarations]
     const QStringList params = message.split(PARAMS_SEPARATOR, QString::SkipEmptyParts);
                                                                         ^~~~~~~~~~~~~~
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:605:9: note: declared here
         SkipEmptyParts Q_DECL_ENUMERATOR_DEPRECATED
         ^~~~~~~~~~~~~~
app/application.cpp:305:73: warning: 'SkipEmptyParts' is deprecated [-Wdeprecated-declarations]
     const QStringList params = message.split(PARAMS_SEPARATOR, QString::SkipEmptyParts);
                                                                         ^~~~~~~~~~~~~~
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:605:9: note: declared here
         SkipEmptyParts Q_DECL_ENUMERATOR_DEPRECATED
         ^~~~~~~~~~~~~~
app/application.cpp:305:87: warning: 'QStringList QString::split(QChar, QString::SplitBehavior, Qt::CaseSensitivity) const' is deprecated: Use Qt::SplitBehavior variant instead [-Wdeprecated-declarations]
     const QStringList params = message.split(PARAMS_SEPARATOR, QString::SkipEmptyParts);
                                                                                       ^
In file included from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhashfunctions.h:44,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qlist.h:47,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qhash.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qshareddata.h:46,
                 from /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qsharedpointer.h:45,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qpointer.h:43,
                 from ../../../../staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/QPointer:1,
                 from app/application.h:32,
                 from app/application.cpp:30:
/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/QtCore/qstring.h:615:17: note: declared here
     QStringList split(QChar sep, SplitBehavior behavior,
                 ^~~~~
make[5]: *** [Makefile:9455: application.o] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/qBittorrent-Enhanced-Edition-release-4.3.4.10/src'
make[4]: *** [Makefile:47: sub-src-make_first] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/qBittorrent-Enhanced-Edition-release-4.3.4.10'
make[3]: *** [Makefile:63: /openwrt/build_dir/target-x86_64_musl/qBittorrent-Enhanced-Edition-release-4.3.4.10/.built] Error 2
```
