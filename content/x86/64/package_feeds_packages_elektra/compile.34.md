---
title: "compile.34"
date: 2021-06-17 08:29:46.551546
hidden: false
draft: false
weight: -34
---

build number: `34`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/elektra/compile -j$(nproc) || make package/feeds/packages/elektra/compile V=s
```

#### Compile.txt

``` bash
-- The C compiler identification is GNU 8.4.0
-- The CXX compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/bin/x86_64-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/bin/x86_64-openwrt-linux-musl-g++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Performing Test HAS_CXX_STD
-- Performing Test HAS_CXX_STD - Success
-- compiler/linker accepts version script? TRUE
-- compiler/linker supports symbol versioning? TRUE
-- GCC detected
-- Performing Test HAS_CFLAG_MAYBE_UNINITIALIZED
-- Performing Test HAS_CFLAG_MAYBE_UNINITIALIZED - Success
-- C flags are -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2=elektra-0.9.2 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -std=gnu99  -Wno-deprecated-declarations  -Wstrict-prototypes  -Wno-long-long -Wpedantic -Wno-variadic-macros -Wall -Wextra -Wno-overlength-strings -Wsign-compare -Wfloat-equal -Wformat -Wformat-security -Wshadow -Wcomments -Wtrigraphs -Wundef -Wuninitialized -Winit-self -Wmaybe-uninitialized -Wsign-compare -Wfloat-equal
-- CXX flags are -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2=elektra-0.9.2 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include -std=c++11  -Wno-deprecated-declarations  -Wold-style-cast -Wstrict-null-sentinel -D_GLIBCXX_USE_NANOSLEEP -Wno-missing-field-initializers -Woverloaded-virtual  -Wsign-promo  -Wno-long-long -Wpedantic -Wno-variadic-macros -Wall -Wextra -Wno-overlength-strings -Wsign-compare -Wfloat-equal -Wformat -Wformat-security -Wshadow -Wcomments -Wtrigraphs -Wundef -Wuninitialized -Winit-self -Wmaybe-uninitialized
-- You are building Elektra 0.9.2
-- Detected unix-x86_64. Use make package to build packages (TBZ2).
-- Exclude Plugin gpgme because explicitly excluded
-- Exclude Plugin internalnotification because explicitly excluded
-- Exclude Plugin multifile because explicitly excluded
-- Looking for mkfifo
-- Looking for mkfifo - found
-- Looking for fork
-- Looking for fork - found
-- Looking for __GNU_LIBRARY__
-- Looking for __GNU_LIBRARY__ - not found
-- Exclude Plugin simpleini because simpleini needs glibc to work, use the mini plugin instead
-- Exclude Plugin augeas because libaugeas not found (libaugeas-dev >= 0.16 needed)
-- Include Plugin base64
-- Include Plugin blockresolver
-- Include Plugin c
-- Looking for nftw
-- Looking for nftw - found
-- Include Plugin cache
-- Include Plugin ccode
-- Include Plugin conditionals
-- Include Plugin constants
-- Include Plugin counter
-- Include Plugin cpptemplate
-- Include Plugin crypto
-- Include Plugin csvstorage
-- Include Plugin curlget
-- Include Plugin date
-- Include Plugin dbus
-- Include Plugin dbusrecv
-- Include Plugin desktop
-- Include Plugin directoryvalue
-- Include Plugin doc
-- Include Plugin dpkg
-- Include Plugin dump
-- Include Plugin error
-- Include Plugin fcrypt
-- Include Plugin file
-- Include Plugin filecheck
-- Looking for setmntent
-- Looking for setmntent - found
-- Include Plugin fstab
-- Exclude Plugin gitresolver because Cannot find libgit2 >= 0.24.1
-- Include Plugin glob
-- gopts: using gopts_procfs.h
-- Include Plugin gopts
-- Include Plugin hexcode
-- Include Plugin hexnumber
-- Include Plugin hidden
-- Include Plugin hosts
-- Include Plugin iconv
-- Include Plugin ini
-- Include Plugin ipaddr
-- Include Plugin iterate
-- Exclude Plugin jni because jni not found
-- Exclude Plugin journald because systemd-journal not found
-- Include Plugin kconfig
-- Include Plugin keytometa
-- Include Plugin line
-- Include Plugin lineendings
-- Include Plugin list
-- Include Plugin logchange
-- Search for swig3 instead
-- Search for swig2 instead
-- Exclude Plugin lua because swig not found
-- Include Plugin macaddr
-- Include Plugin mathcheck
-- Include Plugin mini
-- Include Plugin mmapstorage_crc
-- Include Plugin mmapstorage
-- Include Plugin mozprefs
-- Include Plugin network
-- Include Plugin ni
-- Include Plugin noresolver
-- Include Plugin null
-- Looking for fgetpwent
-- Looking for fgetpwent - found
-- Looking for getline
-- Looking for getline - found
-- Looking for putpwent
-- Looking for putpwent - found
-- Include Plugin passwd
-- Looking for euidaccess
-- Looking for euidaccess - found
-- Looking for access
-- Looking for access - found
-- Looking for geteuid
-- Looking for geteuid - found
-- Looking for getegid
-- Looking for getegid - found
-- Looking for seteuid
-- Looking for seteuid - found
-- Looking for setegid
-- Looking for setegid - found
-- Looking for getpwnam
-- Looking for getpwnam - found
-- Looking for getpwuid
-- Looking for getpwuid - found
-- Looking for getgrouplist
-- Looking for getgrouplist - found
-- Looking for getgrgid
-- Looking for getgrgid - found
-- Include Plugin path
-- Include Plugin process
-- Include Plugin profile
-- Search for swig3 instead
-- Search for swig2 instead
-- Exclude Plugin python because swig not found
-- Include Plugin quickdump
-- Include Plugin range
-- Include Plugin reference
-- Include Plugin rename
-- Include Plugin resolver_fm_pb_b
-- Include Plugin resolver_fm_b_b
-- Include Plugin resolver_fm_hb_b
-- Include Plugin resolver_fm_hp_b
-- Include Plugin resolver_fm_ub_x
-- Include Plugin resolver_fm_xb_x
-- Include Plugin resolver_fm_xp_x
-- Include Plugin resolver_fm_xhp_x
-- Include Plugin resolver_fm_uhb_xb
-- Include Plugin resolver_fm_hpu_b
-- Include Plugin rgbcolor
-- Search for swig3 instead
-- Search for swig2 instead
-- Exclude Plugin ruby because ruby not found
-- Include Plugin shell
-- Include Plugin spec
-- Include Plugin specload
-- Include Plugin sync
-- Include Plugin syslog
-- Include Plugin tcl
-- Include Plugin template
-- Include Plugin timeofday
-- Include Plugin tracer
-- Include Plugin type
-- Include Plugin uname
-- Include Plugin unit
-- Include Plugin validation
-- Include Plugin wresolver
-- Include Plugin xerces
-- Include Plugin xmltool
-- Include Plugin yajl
-- Include Plugin yamlcpp
-- Include Plugin yamlsmith
-- Exclude Plugin yanlr because ANTLR 4 executable (antlr4, antlr) not found
-- Include Plugin zeromqrecv
-- Include Plugin zeromqsend
-- Looking for fnmatch
-- Looking for fnmatch - found
-- Exclude Library notification because internalnotification plugin excluded
-- Include Binding cpp
-- Exclude Binding jna because javac (java compiler) not found, which is only included in a jdk
-- Exclude Binding rust, because cargo not found
-- Search for swig3 instead
-- Search for swig2 instead
-- Exclude Binding python because neither swig2/3/4 found. Please install swig 2/3/4 and set -DSWIG_EXECUTABLE=
-- Exclude Binding lua because neither swig2/3/4 found. Please install swig 2/3/4 and set -DSWIG_EXECUTABLE=
-- Exclude Binding ruby because neither swig2/3/4 found. Please install swig 2/3/4 and set -DSWIG_EXECUTABLE=
-- Exclude Binding intercept_fs because explicitly excluded
-- Exclude Binding intercept_env because explicitly excluded
-- Exclude Binding io_uv because explicitly excluded
-- Exclude Binding io_ev because explicitly excluded
-- Exclude Binding io_glib because explicitly excluded
-- Include Tool kdb
-- Looking for clearenv
-- Looking for clearenv - found
-- Looking for setenv
-- Looking for setenv - found
-- Looking for futimens
-- Looking for futimens - found
-- Looking for hsearch_r
-- Looking for hsearch_r - found
-- Looking for futimes
-- Looking for futimes - found
-- Looking for glob
-- Looking for glob - found
-- Looking for clock_gettime
-- Looking for clock_gettime - found
-- Looking for ctype.h
-- Looking for ctype.h - found
-- Looking for errno.h
-- Looking for errno.h - found
-- Looking for features.h
-- Looking for features.h - found
-- Looking for locale.h
-- Looking for locale.h - found
-- Looking for stdio.h
-- Looking for stdio.h - found
-- Looking for stdlib.h
-- Looking for stdlib.h - found
-- Looking for string.h
-- Looking for string.h - found
-- Looking for time.h
-- Looking for time.h - found
-- Looking for unistd.h
-- Looking for unistd.h - found
-- Looking for sys/types.h
-- Looking for sys/types.h - found
-- Looking for stdint.h
-- Looking for stdint.h - found
-- Looking for stddef.h
-- Looking for stddef.h - found
-- Check size of int
-- Check size of int - done
-- Check size of long
-- Check size of long - done
-- Check size of size_t
-- Check size of size_t - done
-- Check size of long long
-- Check size of long long - done
-- Check size of long double
-- Check size of long double - done
-- Check size of mode_t
-- Check size of mode_t - done
-- Check size of float
-- Check size of float - done
-- Check size of double
-- Check size of double - done
-- Check size of ((struct timeval*)0)->tv_usec
-- Check size of ((struct timeval*)0)->tv_usec - done
-- Check size of ((struct stat*)0)->st_size
-- Check size of ((struct stat*)0)->st_size - done
-- Check if the system is big endian
-- Searching 16 bit integer
-- Check size of unsigned short
-- Check size of unsigned short - done
-- Searching 16 bit integer - Using unsigned short
-- Check if the system is big endian - little endian
-- Configuring done
-- Generating done
CMake Warning:
  Manually-specified variables were not used by the project:

    CMAKE_ASM_COMPILER
    CMAKE_ASM_COMPILER_LAUNCHER
    CMAKE_EXPORT_NO_PACKAGE_REGISTRY
    CMAKE_EXPORT_PACKAGE_REGISTRY
    CMAKE_FIND_PACKAGE_NO_PACKAGE_REGISTRY
    CMAKE_FIND_PACKAGE_NO_SYSTEM_PACKAGE_REGISTRY
    DL_LIBRARY
    FORCE_IN_SOURCE_BUILD


-- Build files have been written to: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build
ninja: Entering directory `/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[1/630] Building C object src/plugins/base64/CMakeFiles/elektra-base64-objects.dir/base64_functions.c.o
[2/630] Building C object src/plugins/base64/CMakeFiles/elektra-base64-objects.dir/base64.c.o
[3/630] Building C object src/plugins/blockresolver/CMakeFiles/elektra-blockresolver-objects.dir/blockresolver.c.o
[4/630] Building C object src/plugins/c/CMakeFiles/elektra-c-objects.dir/c.c.o
[5/630] Building C object src/plugins/cache/CMakeFiles/elektra-cache-objects.dir/cache.c.o
[6/630] Building CXX object src/plugins/ccode/CMakeFiles/elektra-ccode-objects.dir/ccode.cpp.o
[7/630] Building CXX object src/plugins/ccode/CMakeFiles/elektra-ccode-objects.dir/coder.cpp.o
[8/630] Building C object src/plugins/conditionals/CMakeFiles/elektra-conditionals-objects.dir/conditionals.c.o
[9/630] Building C object src/plugins/constants/CMakeFiles/elektra-constants-objects.dir/constants.c.o
[10/630] Building C object src/plugins/counter/CMakeFiles/elektra-counter-objects.dir/counter.c.o
[11/630] Building CXX object src/plugins/cpptemplate/CMakeFiles/elektra-cpptemplate-objects.dir/cpptemplate.cpp.o
[12/630] Building CXX object src/plugins/cpptemplate/CMakeFiles/elektra-cpptemplate-objects.dir/cpptemplate_delegate.cpp.o
[13/630] Building C object src/plugins/crypto/CMakeFiles/elektra-crypto-objects.dir/gcrypt_operations.c.o
[14/630] Building C object src/plugins/crypto/CMakeFiles/elektra-crypto-objects.dir/helper.c.o
[15/630] Building C object src/plugins/crypto/CMakeFiles/elektra-crypto-objects.dir/gpg.c.o
[16/630] Building C object src/plugins/crypto/CMakeFiles/elektra-crypto-objects.dir/crypto.c.o
[17/630] Building C object src/plugins/csvstorage/CMakeFiles/elektra-csvstorage-objects.dir/csvstorage.c.o
[18/630] Building C object src/plugins/curlget/CMakeFiles/elektra-curlget-objects.dir/curlget.c.o
[19/630] Building C object src/plugins/date/CMakeFiles/elektra-date-objects.dir/date.c.o
[20/630] Building C object src/plugins/dbus/CMakeFiles/elektra-dbus-objects.dir/dbus.c.o
[21/630] Building C object src/plugins/dbus/CMakeFiles/elektra-dbus-objects.dir/sendmessage.c.o
[22/630] Building C object src/plugins/dbusrecv/CMakeFiles/elektra-dbusrecv-objects.dir/dbusrecv.c.o
[23/630] Building C object src/plugins/dbusrecv/CMakeFiles/elektra-dbusrecv-objects.dir/receivemessage.c.o
[24/630] Building C object src/plugins/desktop/CMakeFiles/elektra-desktop-objects.dir/desktop.c.o
[25/630] Building CXX object src/plugins/directoryvalue/CMakeFiles/elektra-directoryvalue-objects.dir/directoryvalue.cpp.o
[26/630] Building CXX object src/plugins/directoryvalue/CMakeFiles/elektra-directoryvalue-objects.dir/directoryvalue_delegate.cpp.o
[27/630] Building C object src/plugins/doc/CMakeFiles/elektra-doc-objects.dir/doc.c.o
[28/630] Building C object src/plugins/dpkg/CMakeFiles/elektra-dpkg-objects.dir/dpkg.c.o
[29/630] Building CXX object src/plugins/dump/CMakeFiles/elektra-dump-objects.dir/dump.cpp.o
[30/630] Building C object src/plugins/error/CMakeFiles/elektra-error-objects.dir/error.c.o
[31/630] Building C object src/plugins/fcrypt/CMakeFiles/elektra-fcrypt-objects.dir/__/crypto/gpg.c.o
[32/630] Building C object src/plugins/fcrypt/CMakeFiles/elektra-fcrypt-objects.dir/fcrypt.c.o
[33/630] Building C object src/plugins/file/CMakeFiles/elektra-file-objects.dir/file.c.o
[34/630] Building C object src/plugins/filecheck/CMakeFiles/elektra-filecheck-objects.dir/filecheck.c.o
../src/plugins/filecheck/filecheck.c: In function 'checkFile':
../src/plugins/filecheck/filecheck.c:212:17: warning: initialization of 'iconv_t' {aka 'long int'} from 'void *' makes integer from pointer without a cast [-Wint-conversion]
  iconv_t conv = NULL;
                 ^~~~
[35/630] Building C object src/plugins/fstab/CMakeFiles/elektra-fstab-objects.dir/fstab.c.o
[36/630] Building C object src/plugins/glob/CMakeFiles/elektra-glob-objects.dir/glob.c.o
[37/630] Building C object src/plugins/gopts/CMakeFiles/elektra-gopts-objects.dir/gopts.c.o
[38/630] Building C object src/plugins/hexcode/CMakeFiles/elektra-hexcode-objects.dir/hexcode.c.o
[39/630] Building C object src/plugins/hexnumber/CMakeFiles/elektra-hexnumber-objects.dir/hexnumber.c.o
[40/630] Building C object src/plugins/hidden/CMakeFiles/elektra-hidden-objects.dir/hidden.c.o
[41/630] Building C object src/plugins/hosts/CMakeFiles/elektra-hosts-objects.dir/hosts-get.c.o
[42/630] Building C object src/plugins/hosts/CMakeFiles/elektra-hosts-objects.dir/hosts-set.c.o
[43/630] Building C object src/plugins/hosts/CMakeFiles/elektra-hosts-objects.dir/keymetaformatting.c.o
[44/630] Building C object src/plugins/uname/CMakeFiles/elektra-uname-objects.dir/uname.c.o
[45/630] Building C object src/plugins/iconv/CMakeFiles/elektra-iconv-objects.dir/iconv.c.o
[46/630] Building C object src/plugins/ini/CMakeFiles/elektra-ini-objects.dir/ini.c.o
[47/630] Building C object src/plugins/ini/CMakeFiles/elektra-ini-objects.dir/inih-r29/inih.c.o
[48/630] Building C object src/plugins/ipaddr/CMakeFiles/elektra-ipaddr-objects.dir/ipaddr.c.o
[49/630] Building C object src/plugins/iterate/CMakeFiles/elektra-iterate-objects.dir/iterate.c.o
[50/630] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig-objects.dir/kconfig.cpp.o
[51/630] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig-objects.dir/kconfig_delegate.cpp.o
[52/630] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig-objects.dir/kconfig_parser.cpp.o
[53/630] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig-objects.dir/kconfig_parser_exception.cpp.o
[54/630] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig-objects.dir/kconfig_serializer.cpp.o
[55/630] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig-objects.dir/file_utility.cpp.o
[56/630] Building C object src/plugins/keytometa/CMakeFiles/elektra-keytometa-objects.dir/keytometa.c.o
[57/630] Building C object src/plugins/line/CMakeFiles/elektra-line-objects.dir/line.c.o
[58/630] Building C object src/plugins/lineendings/CMakeFiles/elektra-lineendings-objects.dir/lineendings.c.o
[59/630] Building C object src/plugins/list/CMakeFiles/elektra-list-objects.dir/list.c.o
[60/630] Building C object src/plugins/logchange/CMakeFiles/elektra-logchange-objects.dir/logchange.c.o
[61/630] Building C object src/plugins/macaddr/CMakeFiles/elektra-macaddr-objects.dir/macaddr.c.o
[62/630] Building C object src/plugins/mathcheck/CMakeFiles/elektra-mathcheck-objects.dir/mathcheck.c.o
[63/630] Building C object src/plugins/mathcheck/CMakeFiles/elektra-mathcheck-objects.dir/floathelper.c.o
[64/630] Building C object src/plugins/mini/CMakeFiles/elektra-mini-objects.dir/mini.c.o
[65/630] Building C object src/plugins/mmapstorage/CMakeFiles/elektra-mmapstorage-objects.dir/dynarray.c.o
[66/630] Building C object src/plugins/mmapstorage/CMakeFiles/elektra-mmapstorage-objects.dir/mmapstorage.c.o
[67/630] Building C object src/plugins/mmapstorage/CMakeFiles/elektra-mmapstorage_crc-objects.dir/dynarray.c.o
[68/630] Building C object src/plugins/mmapstorage/CMakeFiles/elektra-mmapstorage_crc-objects.dir/mmapstorage.c.o
[69/630] Building C object src/plugins/mozprefs/CMakeFiles/elektra-mozprefs-objects.dir/mozprefs.c.o
[70/630] Building C object src/plugins/network/CMakeFiles/elektra-network-objects.dir/network.c.o
[71/630] Building C object src/plugins/ni/CMakeFiles/elektra-ni-objects.dir/ni.c.o
[72/630] Building C object src/plugins/ni/CMakeFiles/elektra-ni-objects.dir/nickel-1.1.0/src/buf.c.o
[73/630] Building C object src/plugins/ni/CMakeFiles/elektra-ni-objects.dir/nickel-1.1.0/src/hash.c.o
[74/630] Building C object src/plugins/ni/CMakeFiles/elektra-ni-objects.dir/nickel-1.1.0/src/io.c.o
[75/630] Building C object src/plugins/ni/CMakeFiles/elektra-ni-objects.dir/nickel-1.1.0/src/nickel.c.o
[76/630] Building C object src/plugins/noresolver/CMakeFiles/elektra-noresolver-objects.dir/noresolver.c.o
[77/630] Building C object src/plugins/null/CMakeFiles/elektra-null-objects.dir/null.c.o
[78/630] Building C object src/plugins/passwd/CMakeFiles/elektra-passwd-objects.dir/passwd.c.o
[79/630] Building C object src/plugins/path/CMakeFiles/elektra-path-objects.dir/path.c.o
[80/630] Building C object src/plugins/process/CMakeFiles/elektra-process-objects.dir/process.c.o
[81/630] Building C object src/plugins/profile/CMakeFiles/elektra-profile-objects.dir/profile.c.o
[82/630] Building C object src/plugins/quickdump/CMakeFiles/elektra-quickdump-objects.dir/quickdump.c.o
[83/630] Building C object src/plugins/range/CMakeFiles/elektra-range-objects.dir/range.c.o
[84/630] Building C object src/plugins/reference/CMakeFiles/elektra-reference-objects.dir/reference.c.o
[85/630] Building C object src/plugins/reference/CMakeFiles/elektra-reference-objects.dir/referencegraph.c.o
[86/630] Building C object src/plugins/rename/CMakeFiles/elektra-rename-objects.dir/rename.c.o
[87/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hpu_b-objects.dir/resolver.c.o
[88/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hpu_b-objects.dir/filename.c.o
[89/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xhp_x-objects.dir/resolver.c.o
[90/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xhp_x-objects.dir/filename.c.o
[91/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_pb_b-objects.dir/resolver.c.o
[92/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_pb_b-objects.dir/filename.c.o
[93/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_uhb_xb-objects.dir/resolver.c.o
[94/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_uhb_xb-objects.dir/filename.c.o
[95/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_b_b-objects.dir/resolver.c.o
[96/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_b_b-objects.dir/filename.c.o
[97/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hb_b-objects.dir/resolver.c.o
[98/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hb_b-objects.dir/filename.c.o
[99/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xb_x-objects.dir/resolver.c.o
[100/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xb_x-objects.dir/filename.c.o
[101/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hp_b-objects.dir/resolver.c.o
[102/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hp_b-objects.dir/filename.c.o
[103/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_ub_x-objects.dir/resolver.c.o
[104/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_ub_x-objects.dir/filename.c.o
[105/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xp_x-objects.dir/resolver.c.o
[106/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xp_x-objects.dir/filename.c.o
[107/630] Building C object src/plugins/rgbcolor/CMakeFiles/elektra-rgbcolor-objects.dir/rgbcolor.c.o
[108/630] Building C object src/plugins/shell/CMakeFiles/elektra-shell-objects.dir/shell.c.o
[109/630] Building C object src/plugins/spec/CMakeFiles/elektra-spec-objects.dir/spec.c.o
[110/630] Building C object src/plugins/specload/CMakeFiles/elektra-specload-objects.dir/specload.c.o
[111/630] Building C object src/plugins/sync/CMakeFiles/elektra-sync-objects.dir/sync.c.o
[112/630] Building C object src/plugins/syslog/CMakeFiles/elektra-syslog-objects.dir/syslog.c.o
[113/630] Building CXX object src/plugins/tcl/CMakeFiles/elektra-tcl-objects.dir/tcl.cpp.o
[114/630] Building CXX object src/plugins/tcl/CMakeFiles/elektra-tcl-objects.dir/action.cpp.o
In file included from ../src/plugins/tcl/action.cpp:18:
/openwrt/staging_dir/target-x86_64_musl/usr/include/boost/bind.hpp:41:1: note: #pragma message: The practice of declaring the Bind placeholders (_1, _2, ...) in the global namespace is deprecated. Please use <boost/bind/bind.hpp> + using namespace boost::placeholders, or define BOOST_BIND_GLOBAL_PLACEHOLDERS to retain the current behavior.
 )
 ^
[115/630] Building CXX object src/plugins/tcl/CMakeFiles/elektra-tcl-objects.dir/printer.cpp.o
[116/630] Building C object src/plugins/template/CMakeFiles/elektra-template-objects.dir/template.c.o
[117/630] Building C object src/plugins/timeofday/CMakeFiles/elektra-timeofday-objects.dir/timeofday.c.o
[118/630] Building C object src/plugins/tracer/CMakeFiles/elektra-tracer-objects.dir/tracer.c.o
[119/630] Building C object src/plugins/type/CMakeFiles/elektra-type-objects.dir/type.c.o
[120/630] Building C object src/plugins/type/CMakeFiles/elektra-type-objects.dir/types.c.o
[121/630] Building C object src/plugins/unit/CMakeFiles/elektra-unit-objects.dir/unit.c.o
[122/630] Building C object src/plugins/validation/CMakeFiles/elektra-validation-objects.dir/validation.c.o
[123/630] Building C object src/plugins/validation/CMakeFiles/elektra-validation-objects.dir/lookupre.c.o
[124/630] Building C object src/plugins/wresolver/CMakeFiles/elektra-wresolver-objects.dir/wresolver.c.o
[125/630] Building CXX object src/plugins/xerces/CMakeFiles/elektra-xerces-objects.dir/xerces.cpp.o
[126/630] Building CXX object src/plugins/xerces/CMakeFiles/elektra-xerces-objects.dir/deserializer.cpp.o
[127/630] Building CXX object src/plugins/xerces/CMakeFiles/elektra-xerces-objects.dir/serializer.cpp.o
[128/630] Building C object src/plugins/xmltool/CMakeFiles/elektra-xmltool-objects.dir/xmltool.c.o
[129/630] Building C object src/plugins/xmltool/CMakeFiles/elektra-xmltool-objects.dir/stream.c.o
[130/630] Building C object src/plugins/xmltool/CMakeFiles/elektra-xmltool-objects.dir/kdbtools.c.o
[131/630] Building C object src/plugins/xmltool/CMakeFiles/elektra-xmltool-objects.dir/kscompare.c.o
[132/630] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl-objects.dir/yajl.c.o
[133/630] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl-objects.dir/iterator.c.o
[134/630] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl-objects.dir/yajl_gen.c.o
[135/630] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl-objects.dir/yajl_gen_open.c.o
[136/630] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl-objects.dir/yajl_gen_close.c.o
[137/630] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl-objects.dir/yajl_parse.c.o
[138/630] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl-objects.dir/name.c.o
[139/630] Building CXX object src/plugins/yamlcpp/CMakeFiles/elektra-yamlcpp-objects.dir/yamlcpp.cpp.o
[140/630] Building CXX object src/plugins/yamlcpp/CMakeFiles/elektra-yamlcpp-objects.dir/read.cpp.o
[141/630] Building CXX object src/plugins/yamlcpp/CMakeFiles/elektra-yamlcpp-objects.dir/write.cpp.o
[142/630] Building CXX object src/plugins/yamlsmith/CMakeFiles/elektra-yamlsmith-objects.dir/yamlsmith.cpp.o
[143/630] Building C object src/plugins/zeromqrecv/CMakeFiles/elektra-zeromqrecv-objects.dir/zeromqrecv.c.o
[144/630] Building C object src/plugins/zeromqrecv/CMakeFiles/elektra-zeromqrecv-objects.dir/subscribe.c.o
[145/630] Building C object src/plugins/zeromqsend/CMakeFiles/elektra-zeromqsend-objects.dir/zeromqsend.c.o
[146/630] Building C object src/plugins/zeromqsend/CMakeFiles/elektra-zeromqsend-objects.dir/publish.c.o
[147/630] Creating version script
[148/630] Building C object src/plugins/base64/CMakeFiles/elektra-base64.dir/base64_functions.c.o
[149/630] Building C object src/plugins/base64/CMakeFiles/elektra-base64.dir/base64.c.o
[150/630] Building C object src/plugins/blockresolver/CMakeFiles/elektra-blockresolver.dir/blockresolver.c.o
[151/630] Building C object src/plugins/c/CMakeFiles/elektra-c.dir/c.c.o
[152/630] Building C object src/plugins/cache/CMakeFiles/elektra-cache.dir/cache.c.o
[153/630] Building CXX object src/plugins/ccode/CMakeFiles/elektra-ccode.dir/ccode.cpp.o
[154/630] Building CXX object src/plugins/ccode/CMakeFiles/elektra-ccode.dir/coder.cpp.o
[155/630] Building C object src/plugins/conditionals/CMakeFiles/elektra-conditionals.dir/conditionals.c.o
[156/630] Building C object src/plugins/constants/CMakeFiles/elektra-constants.dir/constants.c.o
[157/630] Building C object src/plugins/counter/CMakeFiles/elektra-counter.dir/counter.c.o
[158/630] Building CXX object src/plugins/cpptemplate/CMakeFiles/elektra-cpptemplate.dir/cpptemplate.cpp.o
[159/630] Building CXX object src/plugins/cpptemplate/CMakeFiles/elektra-cpptemplate.dir/cpptemplate_delegate.cpp.o
[160/630] Building C object src/plugins/crypto/CMakeFiles/elektra-crypto.dir/gcrypt_operations.c.o
[161/630] Building C object src/plugins/crypto/CMakeFiles/elektra-crypto.dir/helper.c.o
[162/630] Building C object src/plugins/crypto/CMakeFiles/elektra-crypto.dir/gpg.c.o
[163/630] Building C object src/plugins/crypto/CMakeFiles/elektra-crypto.dir/crypto.c.o
[164/630] Building C object src/plugins/csvstorage/CMakeFiles/elektra-csvstorage.dir/csvstorage.c.o
[165/630] Building C object src/plugins/iconv/CMakeFiles/elektra-iconv.dir/iconv.c.o
[166/630] Building C object src/plugins/curlget/CMakeFiles/elektra-curlget.dir/curlget.c.o
[167/630] Building C object src/plugins/date/CMakeFiles/elektra-date.dir/date.c.o
[168/630] Building C object src/plugins/dbus/CMakeFiles/elektra-dbus.dir/dbus.c.o
[169/630] Building C object src/plugins/dbus/CMakeFiles/elektra-dbus.dir/sendmessage.c.o
[170/630] Building C object src/plugins/dbusrecv/CMakeFiles/elektra-dbusrecv.dir/dbusrecv.c.o
[171/630] Building C object src/plugins/dbusrecv/CMakeFiles/elektra-dbusrecv.dir/receivemessage.c.o
[172/630] Building C object src/plugins/desktop/CMakeFiles/elektra-desktop.dir/desktop.c.o
[173/630] Building CXX object src/plugins/directoryvalue/CMakeFiles/elektra-directoryvalue.dir/directoryvalue.cpp.o
[174/630] Building CXX object src/plugins/directoryvalue/CMakeFiles/elektra-directoryvalue.dir/directoryvalue_delegate.cpp.o
[175/630] Building C object src/plugins/doc/CMakeFiles/elektra-doc.dir/doc.c.o
[176/630] Building C object src/plugins/dpkg/CMakeFiles/elektra-dpkg.dir/dpkg.c.o
[177/630] Building CXX object src/plugins/dump/CMakeFiles/elektra-dump.dir/dump.cpp.o
[178/630] Building C object src/plugins/error/CMakeFiles/elektra-error.dir/error.c.o
[179/630] Building C object src/plugins/fcrypt/CMakeFiles/elektra-fcrypt.dir/__/crypto/gpg.c.o
[180/630] Building C object src/plugins/fcrypt/CMakeFiles/elektra-fcrypt.dir/fcrypt.c.o
[181/630] Building C object src/plugins/file/CMakeFiles/elektra-file.dir/file.c.o
[182/630] Building C object src/plugins/filecheck/CMakeFiles/elektra-filecheck.dir/filecheck.c.o
../src/plugins/filecheck/filecheck.c: In function 'checkFile':
../src/plugins/filecheck/filecheck.c:212:17: warning: initialization of 'iconv_t' {aka 'long int'} from 'void *' makes integer from pointer without a cast [-Wint-conversion]
  iconv_t conv = NULL;
                 ^~~~
[183/630] Building C object src/plugins/fstab/CMakeFiles/elektra-fstab.dir/fstab.c.o
[184/630] Building C object src/plugins/glob/CMakeFiles/elektra-glob.dir/glob.c.o
[185/630] Building C object src/plugins/gopts/CMakeFiles/elektra-gopts.dir/gopts.c.o
[186/630] Building C object src/plugins/hexcode/CMakeFiles/elektra-hexcode.dir/hexcode.c.o
[187/630] Building C object src/plugins/hexnumber/CMakeFiles/elektra-hexnumber.dir/hexnumber.c.o
[188/630] Building C object src/plugins/hidden/CMakeFiles/elektra-hidden.dir/hidden.c.o
[189/630] Building C object src/plugins/hosts/CMakeFiles/elektra-hosts.dir/hosts-get.c.o
[190/630] Building C object src/plugins/hosts/CMakeFiles/elektra-hosts.dir/hosts-set.c.o
[191/630] Building C object src/plugins/hosts/CMakeFiles/elektra-hosts.dir/keymetaformatting.c.o
[192/630] Building C object src/plugins/unit/CMakeFiles/elektra-unit.dir/unit.c.o
[193/630] Building C object src/plugins/ini/CMakeFiles/elektra-ini.dir/ini.c.o
[194/630] Building C object src/plugins/ini/CMakeFiles/elektra-ini.dir/inih-r29/inih.c.o
[195/630] Building C object src/plugins/ipaddr/CMakeFiles/elektra-ipaddr.dir/ipaddr.c.o
[196/630] Building C object src/plugins/uname/CMakeFiles/elektra-uname.dir/uname.c.o
[197/630] Building C object src/plugins/iterate/CMakeFiles/elektra-iterate.dir/iterate.c.o
[198/630] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig.dir/kconfig.cpp.o
[199/630] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig.dir/kconfig_delegate.cpp.o
[200/630] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig.dir/kconfig_parser.cpp.o
[201/630] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig.dir/kconfig_parser_exception.cpp.o
[202/630] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig.dir/kconfig_serializer.cpp.o
[203/630] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig.dir/file_utility.cpp.o
[204/630] Building C object src/plugins/keytometa/CMakeFiles/elektra-keytometa.dir/keytometa.c.o
[205/630] Building C object src/plugins/line/CMakeFiles/elektra-line.dir/line.c.o
[206/630] Building C object src/plugins/lineendings/CMakeFiles/elektra-lineendings.dir/lineendings.c.o
[207/630] Building C object src/plugins/list/CMakeFiles/elektra-list.dir/list.c.o
[208/630] Building C object src/plugins/logchange/CMakeFiles/elektra-logchange.dir/logchange.c.o
[209/630] Building C object src/plugins/macaddr/CMakeFiles/elektra-macaddr.dir/macaddr.c.o
[210/630] Building C object src/plugins/mathcheck/CMakeFiles/elektra-mathcheck.dir/mathcheck.c.o
[211/630] Building C object src/plugins/mathcheck/CMakeFiles/elektra-mathcheck.dir/floathelper.c.o
[212/630] Building C object src/plugins/mini/CMakeFiles/elektra-mini.dir/mini.c.o
[213/630] Building C object src/plugins/mmapstorage/CMakeFiles/elektra-mmapstorage.dir/dynarray.c.o
[214/630] Building C object src/plugins/mmapstorage/CMakeFiles/elektra-mmapstorage.dir/mmapstorage.c.o
[215/630] Building C object src/plugins/mmapstorage/CMakeFiles/elektra-mmapstorage_crc.dir/dynarray.c.o
[216/630] Building C object src/plugins/mmapstorage/CMakeFiles/elektra-mmapstorage_crc.dir/mmapstorage.c.o
[217/630] Building C object src/plugins/mozprefs/CMakeFiles/elektra-mozprefs.dir/mozprefs.c.o
[218/630] Building C object src/plugins/network/CMakeFiles/elektra-network.dir/network.c.o
[219/630] Building C object src/plugins/ni/CMakeFiles/elektra-ni.dir/ni.c.o
[220/630] Building C object src/plugins/ni/CMakeFiles/elektra-ni.dir/nickel-1.1.0/src/buf.c.o
[221/630] Building C object src/plugins/ni/CMakeFiles/elektra-ni.dir/nickel-1.1.0/src/hash.c.o
[222/630] Building C object src/plugins/ni/CMakeFiles/elektra-ni.dir/nickel-1.1.0/src/io.c.o
[223/630] Building C object src/plugins/ni/CMakeFiles/elektra-ni.dir/nickel-1.1.0/src/nickel.c.o
[224/630] Building C object src/plugins/noresolver/CMakeFiles/elektra-noresolver.dir/noresolver.c.o
[225/630] Building C object src/plugins/null/CMakeFiles/elektra-null.dir/null.c.o
[226/630] Building C object src/plugins/passwd/CMakeFiles/elektra-passwd.dir/passwd.c.o
[227/630] Building C object src/plugins/path/CMakeFiles/elektra-path.dir/path.c.o
[228/630] Building C object src/plugins/process/CMakeFiles/elektra-process.dir/process.c.o
[229/630] Building C object src/plugins/profile/CMakeFiles/elektra-profile.dir/profile.c.o
[230/630] Building C object src/plugins/quickdump/CMakeFiles/elektra-quickdump.dir/quickdump.c.o
[231/630] Building C object src/plugins/range/CMakeFiles/elektra-range.dir/range.c.o
[232/630] Building C object src/plugins/reference/CMakeFiles/elektra-reference.dir/reference.c.o
[233/630] Building C object src/plugins/reference/CMakeFiles/elektra-reference.dir/referencegraph.c.o
[234/630] Building C object src/plugins/rename/CMakeFiles/elektra-rename.dir/rename.c.o
[235/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_uhb_xb.dir/resolver.c.o
[236/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_uhb_xb.dir/filename.c.o
[237/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xhp_x.dir/resolver.c.o
[238/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xhp_x.dir/filename.c.o
[239/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xp_x.dir/resolver.c.o
[240/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xp_x.dir/filename.c.o
[241/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_pb_b.dir/resolver.c.o
[242/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_pb_b.dir/filename.c.o
[243/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hp_b.dir/resolver.c.o
[244/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hp_b.dir/filename.c.o
[245/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_b_b.dir/resolver.c.o
[246/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_b_b.dir/filename.c.o
[247/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hpu_b.dir/resolver.c.o
[248/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hpu_b.dir/filename.c.o
[249/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hb_b.dir/resolver.c.o
[250/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hb_b.dir/filename.c.o
[251/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xb_x.dir/resolver.c.o
[252/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xb_x.dir/filename.c.o
[253/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_ub_x.dir/resolver.c.o
[254/630] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_ub_x.dir/filename.c.o
[255/630] Building C object src/plugins/rgbcolor/CMakeFiles/elektra-rgbcolor.dir/rgbcolor.c.o
[256/630] Building C object src/plugins/shell/CMakeFiles/elektra-shell.dir/shell.c.o
[257/630] Building C object src/plugins/spec/CMakeFiles/elektra-spec.dir/spec.c.o
[258/630] Building C object src/plugins/specload/CMakeFiles/elektra-specload.dir/specload.c.o
[259/630] Building C object src/plugins/sync/CMakeFiles/elektra-sync.dir/sync.c.o
[260/630] Building C object src/plugins/syslog/CMakeFiles/elektra-syslog.dir/syslog.c.o
[261/630] Building CXX object src/plugins/tcl/CMakeFiles/elektra-tcl.dir/tcl.cpp.o
[262/630] Building CXX object src/plugins/tcl/CMakeFiles/elektra-tcl.dir/action.cpp.o
In file included from ../src/plugins/tcl/action.cpp:18:
/openwrt/staging_dir/target-x86_64_musl/usr/include/boost/bind.hpp:41:1: note: #pragma message: The practice of declaring the Bind placeholders (_1, _2, ...) in the global namespace is deprecated. Please use <boost/bind/bind.hpp> + using namespace boost::placeholders, or define BOOST_BIND_GLOBAL_PLACEHOLDERS to retain the current behavior.
 )
 ^
[263/630] Building CXX object src/plugins/tcl/CMakeFiles/elektra-tcl.dir/printer.cpp.o
[264/630] Building C object src/plugins/template/CMakeFiles/elektra-template.dir/template.c.o
[265/630] Building C object src/plugins/timeofday/CMakeFiles/elektra-timeofday.dir/timeofday.c.o
[266/630] Building C object src/plugins/tracer/CMakeFiles/elektra-tracer.dir/tracer.c.o
[267/630] Building C object src/plugins/type/CMakeFiles/elektra-type.dir/type.c.o
[268/630] Building C object src/plugins/type/CMakeFiles/elektra-type.dir/types.c.o
[269/630] Building C object src/plugins/validation/CMakeFiles/elektra-validation.dir/validation.c.o
[270/630] Building C object src/plugins/validation/CMakeFiles/elektra-validation.dir/lookupre.c.o
[271/630] Building C object src/plugins/wresolver/CMakeFiles/elektra-wresolver.dir/wresolver.c.o
[272/630] Building CXX object src/plugins/xerces/CMakeFiles/elektra-xerces.dir/xerces.cpp.o
[273/630] Building CXX object src/plugins/xerces/CMakeFiles/elektra-xerces.dir/deserializer.cpp.o
[274/630] Building CXX object src/plugins/xerces/CMakeFiles/elektra-xerces.dir/serializer.cpp.o
[275/630] Building C object src/plugins/xmltool/CMakeFiles/elektra-xmltool.dir/xmltool.c.o
[276/630] Building C object src/plugins/xmltool/CMakeFiles/elektra-xmltool.dir/stream.c.o
[277/630] Building C object src/plugins/xmltool/CMakeFiles/elektra-xmltool.dir/kdbtools.c.o
[278/630] Building C object src/plugins/xmltool/CMakeFiles/elektra-xmltool.dir/kscompare.c.o
[279/630] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl.dir/yajl.c.o
[280/630] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl.dir/iterator.c.o
[281/630] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl.dir/yajl_gen.c.o
[282/630] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl.dir/yajl_gen_open.c.o
[283/630] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl.dir/yajl_gen_close.c.o
[284/630] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl.dir/yajl_parse.c.o
[285/630] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl.dir/name.c.o
[286/630] Building CXX object src/plugins/yamlcpp/CMakeFiles/elektra-yamlcpp.dir/yamlcpp.cpp.o
[287/630] Building CXX object src/plugins/yamlcpp/CMakeFiles/elektra-yamlcpp.dir/read.cpp.o
[288/630] Building CXX object src/plugins/yamlcpp/CMakeFiles/elektra-yamlcpp.dir/write.cpp.o
[289/630] Building CXX object src/plugins/yamlsmith/CMakeFiles/elektra-yamlsmith.dir/yamlsmith.cpp.o
[290/630] Building C object src/plugins/zeromqrecv/CMakeFiles/elektra-zeromqrecv.dir/zeromqrecv.c.o
[291/630] Building C object src/plugins/zeromqrecv/CMakeFiles/elektra-zeromqrecv.dir/subscribe.c.o
[292/630] Building C object src/plugins/zeromqsend/CMakeFiles/elektra-zeromqsend.dir/zeromqsend.c.o
[293/630] Building C object src/plugins/zeromqsend/CMakeFiles/elektra-zeromqsend.dir/publish.c.o
[294/630] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/backend.cpp.o
[295/630] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/backendbuilder.cpp.o
[296/630] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/backendparser.cpp.o
[297/630] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/backends.cpp.o
[298/630] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/helper/comparison.cpp.o
[299/630] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/helper/keyhelper.cpp.o
[300/630] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/automergeconfiguration.cpp.o
[301/630] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/automergestrategy.cpp.o
[302/630] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/importmergeconfiguration.cpp.o
[303/630] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/interactivemergestrategy.cpp.o
[304/630] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/mergeconflictstrategy.cpp.o
[305/630] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/mergeresult.cpp.o
[306/630] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/mergingkdb.cpp.o
[307/630] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/metamergestrategy.cpp.o
[308/630] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/newkeystrategy.cpp.o
[309/630] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/onesidemergeconfiguration.cpp.o
[310/630] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/onesidestrategy.cpp.o
[311/630] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/onesidevaluestrategy.cpp.o
[312/630] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/overwritemergeconfiguration.cpp.o
[313/630] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/threewaymerge.cpp.o
[314/630] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/modules.cpp.o
[315/630] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/plugin.cpp.o
[316/630] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/plugindatabase.cpp.o
[317/630] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/plugins.cpp.o
[318/630] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/pluginspec.cpp.o
[319/630] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/specreader.cpp.o
[320/630] Building CXX object src/libs/tools/examples/CMakeFiles/merging.dir/merging.cpp.o
[321/630] Building CXX object src/libs/tools/examples/CMakeFiles/backend.dir/backend.cpp.o
[322/630] Building CXX object src/libs/tools/benchmarks/CMakeFiles/benchmark_plugins.dir/benchmark_plugins.cpp.o
[323/630] Building C object src/libs/ease/CMakeFiles/elektra-ease-objects.dir/array.c.o
[324/630] Building C object src/libs/ease/CMakeFiles/elektra-ease-objects.dir/conversion.c.o
[325/630] Building C object src/libs/ease/CMakeFiles/elektra-ease-objects.dir/functional.c.o
[326/630] Building C object src/libs/ease/CMakeFiles/elektra-ease-objects.dir/keyname.c.o
[327/630] Building C object src/libs/ease/CMakeFiles/elektra-ease-objects.dir/reference.c.o
[328/630] Building C object src/libs/globbing/CMakeFiles/elektra-globbing-objects.dir/globbing.c.o
[329/630] Building C object src/libs/proposal/CMakeFiles/elektra-proposal-objects.dir/proposal.c.o
[330/630] Building C object src/libs/meta/CMakeFiles/elektra-meta-objects.dir/meta.c.o
[331/630] Building C object src/libs/plugin/CMakeFiles/elektra-plugin-objects.dir/plugin.c.o
[332/630] Building C object src/libs/pluginprocess/CMakeFiles/elektra-pluginprocess-objects.dir/pluginprocess.c.o
[333/630] Building C object src/libs/utility/CMakeFiles/elektra-utility-objects.dir/text.c.o
[334/630] Building C object src/libs/io/CMakeFiles/elektra-io-objects.dir/io.c.o
[335/630] Building C object src/libs/io/adapter/dbus/CMakeFiles/io-adapter-dbus.dir/dbus.c.o
[336/630] Building C object src/libs/io/adapter/zeromq/CMakeFiles/io-adapter-zeromq.dir/zeromq.c.o
[337/630] Building C object src/libs/invoke/CMakeFiles/elektra-invoke-objects.dir/invoke.c.o
[338/630] Building C object src/libs/highlevel/CMakeFiles/elektra-highlevel-objects.dir/elektra.c.o
[339/630] Building C object src/libs/highlevel/CMakeFiles/elektra-highlevel-objects.dir/elektra_array_value.c.o
[340/630] Building C object src/libs/highlevel/CMakeFiles/elektra-highlevel-objects.dir/elektra_error.c.o
[341/630] Building C object src/libs/highlevel/CMakeFiles/elektra-highlevel-objects.dir/elektra_value.c.o
[342/630] Building C object src/libs/merge/CMakeFiles/elektra-merge-objects.dir/kdbmerge.c.o
[343/630] Building C object src/libs/opts/CMakeFiles/elektra-opts-objects.dir/opts.c.o
[344/630] Building C object src/libs/elektra/CMakeFiles/elektra-kdb.dir/backend.c.o
[345/630] Building C object src/libs/elektra/CMakeFiles/elektra-kdb.dir/kdb.c.o
[346/630] Building C object src/libs/elektra/CMakeFiles/elektra-kdb.dir/mount.c.o
[347/630] Building C object src/libs/elektra/CMakeFiles/elektra-kdb.dir/plugin.c.o
[348/630] Building C object src/libs/elektra/CMakeFiles/elektra-kdb.dir/split.c.o
[349/630] Building C object src/libs/elektra/CMakeFiles/elektra-kdb.dir/trie.c.o
[350/630] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/errors.c.o
[351/630] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/global.c.o
[352/630] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/internal.c.o
[353/630] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/kdbenum.c.o
[354/630] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/key.c.o
[355/630] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/keyhelpers.c.o
[356/630] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/keymeta.c.o
[357/630] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/keyname.c.o
[358/630] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/keyset.c.o
[359/630] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/keytest.c.o
[360/630] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/keyvalue.c.o
[361/630] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/nolog.c.o
[362/630] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/owner.c.o
[363/630] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/proposal.c.o
[364/630] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/rand.c.o
[365/630] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/__/loader/dl.c.o
[366/630] Linking C shared library lib/libelektra-core.so.0.9.2
[367/630] Creating library symlink lib/libelektra-core.so.4 lib/libelektra-core.so
[368/630] Linking C shared library lib/libelektra-ease.so.0.9.2
[369/630] Creating library symlink lib/libelektra-ease.so.4 lib/libelektra-ease.so
[370/630] Linking C shared library lib/libelektra-globbing.so.0.9.2
[371/630] Creating library symlink lib/libelektra-globbing.so.4 lib/libelektra-globbing.so
[372/630] Linking C shared library lib/libelektra-proposal.so.0.9.2
[373/630] Creating library symlink lib/libelektra-proposal.so.4 lib/libelektra-proposal.so
[374/630] Linking C shared library lib/libelektra-meta.so.0.9.2
[375/630] Creating library symlink lib/libelektra-meta.so.4 lib/libelektra-meta.so
[376/630] Linking C shared library lib/libelektra-plugin.so.0.9.2
[377/630] Creating library symlink lib/libelektra-plugin.so.4 lib/libelektra-plugin.so
[378/630] Linking C shared module lib/libelektra-base64.so
[379/630] Linking C shared module lib/libelektra-c.so
[380/630] Linking CXX shared module lib/libelektra-ccode.so
[381/630] Linking C shared module lib/libelektra-conditionals.so
[382/630] Linking C shared module lib/libelektra-constants.so
[383/630] Linking C shared module lib/libelektra-counter.so
[384/630] Linking CXX shared module lib/libelektra-cpptemplate.so
[385/630] Linking C shared module lib/libelektra-date.so
[386/630] Linking C shared module lib/libelektra-dbus.so
[387/630] Linking C shared module lib/libelektra-desktop.so
[388/630] Linking CXX shared module lib/libelektra-directoryvalue.so
[389/630] Linking C shared module lib/libelektra-dpkg.so
[390/630] Linking CXX shared module lib/libelektra-dump.so
[391/630] Linking C shared module lib/libelektra-error.so
[392/630] Linking C shared module lib/libelektra-fcrypt.so
[393/630] Linking C shared module lib/libelektra-file.so
[394/630] Linking C shared module lib/libelektra-filecheck.so
[395/630] Linking C shared module lib/libelektra-fstab.so
[396/630] Linking C shared module lib/libelektra-glob.so
[397/630] Linking C shared module lib/libelektra-hexcode.so
[398/630] Linking C shared module lib/libelektra-hexnumber.so
[399/630] Linking C shared module lib/libelektra-hidden.so
[400/630] Linking C shared module lib/libelektra-hosts.so
[401/630] Linking C shared module lib/libelektra-unit.so
[402/630] Linking C shared module lib/libelektra-iconv.so
[403/630] Linking C shared module lib/libelektra-ini.so
[404/630] Linking C shared module lib/libelektra-ipaddr.so
[405/630] Linking C shared module lib/libelektra-uname.so
[406/630] Linking C shared module lib/libelektra-iterate.so
[407/630] Linking CXX shared module lib/libelektra-kconfig.so
[408/630] Linking C shared module lib/libelektra-keytometa.so
[409/630] Linking C shared module lib/libelektra-line.so
[410/630] Linking C shared module lib/libelektra-lineendings.so
[411/630] Linking C shared module lib/libelektra-logchange.so
[412/630] Linking C shared module lib/libelektra-macaddr.so
[413/630] Linking C shared module lib/libelektra-mathcheck.so
[414/630] Linking C shared module lib/libelektra-mmapstorage.so
[415/630] Linking C shared module lib/libelektra-mmapstorage_crc.so
[416/630] Linking C shared module lib/libelektra-network.so
[417/630] Linking C shared module lib/libelektra-ni.so
[418/630] Linking C shared module lib/libelektra-noresolver.so
[419/630] Linking C shared module lib/libelektra-null.so
[420/630] Linking C shared module lib/libelektra-passwd.so
[421/630] Linking C shared module lib/libelektra-path.so
[422/630] Linking C shared module lib/libelektra-profile.so
[423/630] Linking C shared module lib/libelektra-quickdump.so
[424/630] Linking C shared module lib/libelektra-range.so
[425/630] Linking C shared module lib/libelektra-reference.so
[426/630] Linking C shared module lib/libelektra-rename.so
[427/630] Linking C shared module lib/libelektra-resolver_fm_uhb_xb.so
[428/630] Linking C shared module lib/libelektra-resolver_fm_xhp_x.so
[429/630] Linking C shared module lib/libelektra-resolver_fm_xp_x.so
[430/630] Linking C shared module lib/libelektra-resolver_fm_pb_b.so
[431/630] Linking C shared module lib/libelektra-resolver_fm_hp_b.so
[432/630] Linking C shared module lib/libelektra-resolver_fm_b_b.so
[433/630] Linking C shared module lib/libelektra-resolver_fm_hpu_b.so
[434/630] Linking C shared module lib/libelektra-resolver_fm_hb_b.so
[435/630] Linking C shared module lib/libelektra-resolver_fm_xb_x.so
[436/630] Linking C shared module lib/libelektra-resolver_fm_ub_x.so
[437/630] Linking C shared module lib/libelektra-rgbcolor.so
[438/630] Linking C shared module lib/libelektra-shell.so
[439/630] Linking C shared module lib/libelektra-spec.so
[440/630] Linking C shared module lib/libelektra-sync.so
[441/630] Linking C shared module lib/libelektra-syslog.so
[442/630] Linking CXX shared module lib/libelektra-tcl.so
[443/630] Linking C shared module lib/libelektra-template.so
[444/630] Linking C shared module lib/libelektra-timeofday.so
[445/630] Linking C shared module lib/libelektra-tracer.so
[446/630] Linking C shared module lib/libelektra-type.so
[447/630] Linking C shared module lib/libelektra-validation.so
[448/630] Linking C shared module lib/libelektra-wresolver.so
[449/630] Linking CXX shared module lib/libelektra-xerces.so
[450/630] Linking C shared module lib/libelektra-xmltool.so
[451/630] Linking C shared module lib/libelektra-yajl.so
[452/630] Linking CXX shared module lib/libelektra-yamlcpp.so
[453/630] Linking CXX shared module lib/libelektra-yamlsmith.so
[454/630] Linking C shared module lib/libelektra-zeromqsend.so
[455/630] Linking C shared library lib/libelektra-utility.so.0.9.2
[456/630] Creating library symlink lib/libelektra-utility.so.4 lib/libelektra-utility.so
[457/630] Linking C shared module lib/libelektra-mini.so
[458/630] Linking C shared module lib/libelektra-mozprefs.so
[459/630] Linking C shared library lib/libelektra-merge.so.0.9.2
[460/630] Creating library symlink lib/libelektra-merge.so.4 lib/libelektra-merge.so
[461/630] Linking C shared library lib/libelektra-opts.so.0.9.2
[462/630] Creating library symlink lib/libelektra-opts.so.4 lib/libelektra-opts.so
[463/630] Linking C shared module lib/libelektra-gopts.so
[464/630] Linking C shared library lib/libelektra-kdb.so.0.9.2
[465/630] Creating library symlink lib/libelektra-kdb.so.4 lib/libelektra-kdb.so
[466/630] Linking C shared module lib/libelektra-cache.so
[467/630] Linking C shared module lib/libelektra-csvstorage.so
[468/630] Linking C shared module lib/libelektra-doc.so
[469/630] Linking CXX shared library lib/libelektratools.so.0.9.2
[470/630] Creating library symlink lib/libelektratools.so.2 lib/libelektratools.so
[471/630] Linking CXX executable bin/merging
[472/630] Linking CXX executable bin/backend
[473/630] Linking CXX executable bin/benchmark_plugins
[474/630] Linking C shared library lib/libelektra-invoke.so.0.9.2
[475/630] Creating library symlink lib/libelektra-invoke.so.4 lib/libelektra-invoke.so
[476/630] Linking C shared module lib/libelektra-blockresolver.so
[477/630] Linking C shared module lib/libelektra-crypto.so
[478/630] Linking C shared module lib/libelektra-curlget.so
[479/630] Linking C shared module lib/libelektra-list.so
[480/630] Linking C shared module lib/libelektra-specload.so
[481/630] Linking C shared library lib/libelektra-pluginprocess.so.0.9.2
[482/630] Creating library symlink lib/libelektra-pluginprocess.so.4 lib/libelektra-pluginprocess.so
[483/630] Linking C shared module lib/libelektra-process.so
[484/630] Linking C shared library lib/libelektra-io.so.0.9.2
[485/630] Creating library symlink lib/libelektra-io.so.4 lib/libelektra-io.so
[486/630] Linking C shared module lib/libelektra-dbusrecv.so
[487/630] Linking C shared module lib/libelektra-zeromqrecv.so
[488/630] Linking C shared library lib/libelektra-highlevel.so.0.9.2
[489/630] Creating library symlink lib/libelektra-highlevel.so.4 lib/libelektra-highlevel.so
[490/630] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_cascading.dir/cpp_cascading.cpp.o
[491/630] Linking CXX executable bin/cpp_cascading
[492/630] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_dup.dir/cpp_example_dup.cpp.o
[493/630] Linking CXX executable bin/cpp_example_dup
[494/630] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_get.dir/cpp_example_get.cpp.o
[495/630] Linking CXX executable bin/cpp_example_get
[496/630] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_set.dir/cpp_example_set.cpp.o
[497/630] Linking CXX executable bin/cpp_example_set
[498/630] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_userio.dir/cpp_example_userio.cpp.o
[499/630] Linking CXX executable bin/cpp_example_userio
[500/630] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_hello.dir/cpp_example_hello.cpp.o
[501/630] Linking CXX executable bin/cpp_example_hello
[502/630] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_hierarchy.dir/cpp_example_hierarchy.cpp.o
[503/630] Linking CXX executable bin/cpp_example_hierarchy
[504/630] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_iter.dir/cpp_example_iter.cpp.o
[505/630] Linking CXX executable bin/cpp_example_iter
[506/630] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_io.dir/cpp_example_io.cpp.o
[507/630] Linking CXX executable bin/cpp_example_io
[508/630] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_iter_name.dir/cpp_example_iter_name.cpp.o
[509/630] Linking CXX executable bin/cpp_example_iter_name
[510/630] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_ks.dir/cpp_example_ks.cpp.o
[511/630] Linking CXX executable bin/cpp_example_ks
[512/630] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_ordering.dir/cpp_example_ordering.cpp.o
[513/630] Linking CXX executable bin/cpp_example_ordering
[514/630] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_userexception.dir/cpp_example_userexception.cpp.o
[515/630] Linking CXX executable bin/cpp_example_userexception
[516/630] Building CXX object src/bindings/cpp/benchmarks/CMakeFiles/benchmark_thread.dir/benchmark_thread.cpp.o
[517/630] Linking CXX executable bin/benchmark_thread
[518/630] Building CXX object src/bindings/cpp/benchmarks/CMakeFiles/benchmark_sync.dir/benchmark_sync.cpp.o
[519/630] Linking CXX executable bin/benchmark_sync
[520/630] Generating ../../../../include/gen/templates.hpp
[521/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/ansicolors.cpp.o
[522/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/cache.cpp.o
[523/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/cmdline.cpp.o
[524/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/cmerge.cpp.o
[525/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/command.cpp.o
[526/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/complete.cpp.o
[527/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/convert.cpp.o
[528/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/cp.cpp.o
[529/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/editor.cpp.o
[530/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/export.cpp.o
[531/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/external.cpp.o
[532/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/file.cpp.o
[533/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/find.cpp.o
[534/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/gen.cpp.o
[535/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/gen/highlevel/common.cpp.o
[536/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/gen/highlevel/enums.cpp.o
[537/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/gen/highlevel/highlevel.cpp.o
[538/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/gen/highlevel/structs.cpp.o
[539/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/gen/template.cpp.o
[540/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/get.cpp.o
[541/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/globalmount.cpp.o
[542/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/globalumount.cpp.o
[543/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/import.cpp.o
[544/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/listcommands.cpp.o
[545/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/ls.cpp.o
[546/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/main.cpp.o
[547/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/merge.cpp.o
[548/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/mergehelper.cpp.o
[549/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/metaget.cpp.o
[550/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/metals.cpp.o
[551/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/metaremove.cpp.o
[552/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/metaset.cpp.o
[553/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/mount.cpp.o
[554/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/mountbase.cpp.o
[555/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/mv.cpp.o
[556/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/plugincheck.cpp.o
[557/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/plugininfo.cpp.o
[558/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/pluginlist.cpp.o
[559/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/remount.cpp.o
[560/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/rm.cpp.o
[561/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/set.cpp.o
[562/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/sget.cpp.o
[563/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/shell.cpp.o
[564/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/showmeta.cpp.o
[565/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/specmount.cpp.o
[566/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/test.cpp.o
[567/630] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/umount.cpp.o
[568/630] Linking CXX executable bin/kdb
[569/630] Building C object examples/CMakeFiles/set_key.dir/set_key.c.o
[570/630] Linking C executable bin/set_key
[571/630] Building C object examples/CMakeFiles/keyBasename.dir/keyBasename.c.o
[572/630] Linking C executable bin/keyBasename
[573/630] Building C object examples/CMakeFiles/kdbopen.dir/kdbopen.c.o
[574/630] Linking C executable bin/kdbopen
[575/630] Building C object examples/CMakeFiles/optsSnippets.dir/optsSnippets.c.o
[576/630] Linking C executable bin/optsSnippets
[577/630] Building C object examples/CMakeFiles/kdbget_error.dir/kdbget_error.c.o
[578/630] Linking C executable bin/kdbget_error
[579/630] Building C object examples/CMakeFiles/reference.dir/reference.c.o
[580/630] Linking C executable bin/reference
[581/630] Building C object examples/CMakeFiles/kdbget.dir/kdbget.c.o
[582/630] Linking C executable bin/kdbget
[583/630] Building C object examples/CMakeFiles/hello.dir/hello.c.o
[584/630] Linking C executable bin/hello
[585/630] Building C object examples/CMakeFiles/keyNew.dir/keyNew.c.o
[586/630] Linking C executable bin/keyNew
[587/630] Building C object examples/CMakeFiles/keyCopy.dir/keyCopy.c.o
[588/630] Linking C executable bin/keyCopy
[589/630] Building C object examples/CMakeFiles/ksIterate.dir/ksIterate.c.o
[590/630] Linking C executable bin/ksIterate
[591/630] Building C object examples/CMakeFiles/functional.dir/functional.c.o
[592/630] Linking C executable bin/functional
[593/630] Building C object examples/CMakeFiles/keyNewExample.dir/keyNewExample.c.o
[594/630] Linking C executable bin/keyNewExample
[595/630] Building C object examples/CMakeFiles/keyMetaKeySet.dir/keyMetaKeySet.c.o
[596/630] Linking C executable bin/keyMetaKeySet
[597/630] Building C object examples/CMakeFiles/cascading.dir/cascading.c.o
[598/630] Linking C executable bin/cascading
[599/630] Building C object examples/CMakeFiles/gopts.dir/gopts.c.o
[600/630] Linking C executable bin/gopts
[601/630] Building C object examples/CMakeFiles/keyName.dir/keyName.c.o
[602/630] Linking C executable bin/keyName
[603/630] Building C object examples/CMakeFiles/kdbintro.dir/kdbintro.c.o
[604/630] Linking C executable bin/kdbintro
[605/630] Building C object examples/CMakeFiles/opts.dir/opts.c.o
[606/630] Linking C executable bin/opts
[607/630] Building C object examples/CMakeFiles/iterate.dir/iterate.c.o
[608/630] Linking C executable bin/iterate
[609/630] Building C object examples/CMakeFiles/kdbset.dir/kdbset.c.o
[610/630] Linking C executable bin/kdbset
[611/630] Building C object examples/CMakeFiles/helloElektra.dir/helloElektra.c.o
[612/630] Linking C executable bin/helloElektra
[613/630] Building C object examples/CMakeFiles/keyset.dir/keyset.c.o
[614/630] Linking C executable bin/keyset
[615/630] Building C object examples/CMakeFiles/meta.dir/meta.c.o
[616/630] Linking C executable bin/meta
[617/630] Building C object examples/CMakeFiles/ksCut.dir/ksCut.c.o
[618/630] Linking C executable bin/ksCut
[619/630] Building C object examples/CMakeFiles/ksNewExample.dir/ksNewExample.c.o
[620/630] Linking C executable bin/ksNewExample
[621/630] Building C object examples/CMakeFiles/optsCommands.dir/optsCommands.c.o
[622/630] Linking C executable bin/optsCommands
[623/630] Building C object examples/CMakeFiles/ksLookupPop.dir/ksLookupPop.c.o
[624/630] Linking C executable bin/ksLookupPop
[625/630] Building C object examples/CMakeFiles/keyMeta.dir/keyMeta.c.o
[626/630] Linking C executable bin/keyMeta
[627/630] Building C object examples/CMakeFiles/ksNew.dir/ksNew.c.o
[628/630] Linking C executable bin/ksNew
[629/630] Building C object examples/CMakeFiles/namespace.dir/namespace.c.o
[630/630] Linking C executable bin/namespace
ninja: Entering directory `/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[0/1] Install the project...
-- Install configuration: "Release"
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/share/doc/elektra/LICENSE.md
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/cmake/Elektra/ElektraConfig.cmake
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/cmake/Elektra/ElektraConfigVersion.cmake
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/pkgconfig/elektra.pc
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/benchmark-createtree
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/upgrade-bootstrap
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/mountpoint-info
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/check-env-dep
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/configure-firefox
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/change-resolver-symlink
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/change-storage-symlink
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/stash
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/restore
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/reset
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/reset-elektra
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/umount-all
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/ffconfig/writeConfigFiles
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/ffconfig/setupConfig
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/ffconfig/setupProxy
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/ffconfig/setupHomepage
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/backup
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/elektrify-getenv
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/elektrify-open
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/list-tools
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/cmerge-config-files
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/find-tools
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/install-config-file
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/mount-augeas
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/mount-info
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/mount-kde
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/mount-list-all-files
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/mount-openicc
-- Up-to-date: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/mountpoint-info
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/update-snippet-repository
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/install-sh-completion
-- Installing symlink: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib//libelektra-storage.so -> libelektra-ini.so
-- Installing symlink: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib//libelektra-resolver.so -> libelektra-resolver_fm_pb_b.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-base64.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-blockresolver.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-c.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-cache.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-ccode.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-conditionals.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-constants.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-counter.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-cpptemplate.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-crypto.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-csvstorage.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-curlget.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-date.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-dbus.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-dbusrecv.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-desktop.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-directoryvalue.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-doc.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-dpkg.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-dump.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-error.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-fcrypt.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-file.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-filecheck.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-fstab.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-glob.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-gopts.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-hexcode.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-hexnumber.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-hidden.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-hosts.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-iconv.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-ini.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-ipaddr.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-iterate.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-kconfig.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-keytometa.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-line.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-lineendings.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-list.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-logchange.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-macaddr.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-mathcheck.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-mini.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-mmapstorage_crc.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-mmapstorage.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-mozprefs.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-network.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-ni.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-noresolver.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-null.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-passwd.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-path.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-process.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-profile.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-quickdump.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-range.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-reference.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-rename.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-resolver_fm_pb_b.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-resolver_fm_b_b.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-resolver_fm_hb_b.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-resolver_fm_hp_b.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-resolver_fm_ub_x.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-resolver_fm_xb_x.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-resolver_fm_xp_x.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-resolver_fm_xhp_x.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-resolver_fm_uhb_xb.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-resolver_fm_hpu_b.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-rgbcolor.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-shell.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-spec.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-specload.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-sync.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-syslog.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-tcl.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-template.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-timeofday.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-tracer.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-type.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-uname.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-unit.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-validation.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-wresolver.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-xerces.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-xmltool.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-yajl.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-yamlcpp.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-yamlsmith.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-zeromqrecv.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-zeromqsend.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/backend.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/backendbuilder.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/backendparser.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/backends.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/modules.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/plugin.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/plugindatabase.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/plugins.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/pluginspec.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/specreader.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/toolexcept.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/helper/comparison.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/helper/keyhelper.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/automergeconfiguration.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/automergestrategy.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/importmergeconfiguration.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/interactivemergestrategy.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/mergeconfiguration.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/mergeconflict.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/mergeconflictstrategy.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/mergeresult.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/mergetask.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/mergingkdb.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/metamergestrategy.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/newkeystrategy.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/onesidemergeconfiguration.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/onesidestrategy.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/onesidevaluestrategy.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/overwritemergeconfiguration.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/threewaymerge.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektratools.so.0.9.2
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektratools.so.2
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektratools.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-ease.so.0.9.2
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-ease.so.4
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-ease.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-globbing.so.0.9.2
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-globbing.so.4
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-globbing.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-proposal.so.0.9.2
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-proposal.so.4
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-proposal.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-meta.so.0.9.2
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-meta.so.4
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-meta.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-plugin.so.0.9.2
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-plugin.so.4
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-plugin.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-pluginprocess.so.0.9.2
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-pluginprocess.so.4
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-pluginprocess.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-utility.so.0.9.2
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-utility.so.4
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-utility.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-io.so.0.9.2
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-io.so.4
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-io.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/pkgconfig/elektra-io.pc
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-invoke.so.0.9.2
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-invoke.so.4
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-invoke.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-highlevel.so.0.9.2
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-highlevel.so.4
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-highlevel.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/pkgconfig/elektra-highlevel.pc
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/pkgconfig/elektra-codegen.pc
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-merge.so.0.9.2
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-merge.so.4
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-merge.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/pkgconfig/elektra-merge.pc
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-opts.so.0.9.2
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-opts.so.4
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-opts.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-core.so.0.9.2
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-core.so.4
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-core.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-kdb.so.0.9.2
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-kdb.so.4
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-kdb.so
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/cmake/Elektra/ElektraTargetsLibelektra.cmake
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/cmake/Elektra/ElektraTargetsLibelektra-release.cmake
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdb.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbcontext.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbexcept.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbio.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbplugin.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbthread.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbtimer.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbvalue.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/key.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/keyexcept.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/keyio.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/keyset.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/keysetget.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/keysetio.hpp
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/bin/kdb
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbextension.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbmeta.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbease.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbtypes.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbhelper.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdb.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbmodule.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbos.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbopts.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbplugin.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbpluginprocess.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbprivate.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbproposal.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbinvoke.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbutility.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbio.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbnotification.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbglobbing.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbversion.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/elektra.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbendian.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbmacros.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbmerge.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/elektra/error.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/elektra/conversion.h
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/elektra/types.h
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-ni.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-ini.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-plugin.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-merge.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-pluginprocess.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-highlevel.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-mmapstorage.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-resolver_fm_pb_b.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-core.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-io.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-utility.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-opts.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-kdb.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-invoke.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-meta.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-proposal.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-globbing.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-ease.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-cache.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-sync.so: shared object
Packaged contents of /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core into /openwrt/bin/packages/x86_64/packages/libelektra-core_0.9.2-2_x86_64.ipk
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/elektra-kdb/usr/bin/kdb: executable
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/elektra-kdb/usr/lib/libelektratools.so.0.9.2: shared object
Packaged contents of /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/elektra-kdb into /openwrt/bin/packages/x86_64/packages/elektra-kdb_0.9.2-2_x86_64.ipk
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-resolvers/usr/lib/libelektra-resolver_fm_ub_x.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-resolvers/usr/lib/libelektra-noresolver.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-resolvers/usr/lib/libelektra-resolver_fm_hpu_b.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-resolvers/usr/lib/libelektra-resolver_fm_hp_b.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-resolvers/usr/lib/libelektra-resolver_fm_b_b.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-resolvers/usr/lib/libelektra-wresolver.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-resolvers/usr/lib/libelektra-resolver_fm_xp_x.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-resolvers/usr/lib/libelektra-resolver_fm_uhb_xb.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-resolvers/usr/lib/libelektra-resolver_fm_hb_b.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-resolvers/usr/lib/libelektra-resolver_fm_xb_x.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-resolvers/usr/lib/libelektra-resolver_fm_xhp_x.so: shared object
Packaged contents of /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-resolvers into /openwrt/bin/packages/x86_64/packages/libelektra-resolvers_0.9.2-2_x86_64.ipk
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-syslog.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-conditionals.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-shell.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-glob.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-profile.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-path.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-csvstorage.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-line.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-hexcode.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-hidden.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-macaddr.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-network.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-rgbcolor.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-base64.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-ipaddr.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-iconv.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-validation.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-mini.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-date.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-reference.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-null.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-hosts.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-list.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-quickdump.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-uname.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-hexnumber.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-file.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-lineendings.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-unit.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-type.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-range.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-filecheck.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-keytometa.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-mathcheck.so: shared object
Packaged contents of /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins into /openwrt/bin/packages/x86_64/packages/libelektra-plugins_0.9.2-2_x86_64.ipk
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-boost/usr/lib/libelektra-tcl.so: shared object
Packaged contents of /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-boost into /openwrt/bin/packages/x86_64/packages/libelektra-boost_0.9.2-2_x86_64.ipk
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-cpp/usr/lib/libelektra-dump.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-cpp/usr/lib/libelektra-ccode.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-cpp/usr/lib/libelektra-directoryvalue.so: shared object
Packaged contents of /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-cpp into /openwrt/bin/packages/x86_64/packages/libelektra-cpp_0.9.2-2_x86_64.ipk
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-curlget/usr/lib/libelektra-curlget.so: shared object
Packaged contents of /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-curlget into /openwrt/bin/packages/x86_64/packages/libelektra-curlget_0.9.2-2_x86_64.ipk
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-crypto/usr/lib/libelektra-crypto.so: shared object
Packaged contents of /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-crypto into /openwrt/bin/packages/x86_64/packages/libelektra-crypto_0.9.2-2_x86_64.ipk
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-dbus/usr/lib/libelektra-dbusrecv.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-dbus/usr/lib/libelektra-dbus.so: shared object
Packaged contents of /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-dbus into /openwrt/bin/packages/x86_64/packages/libelektra-dbus_0.9.2-2_x86_64.ipk
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-xerces/usr/lib/libelektra-xerces.so: shared object
Packaged contents of /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-xerces into /openwrt/bin/packages/x86_64/packages/libelektra-xerces_0.9.2-2_x86_64.ipk
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-yamlcpp/usr/lib/libelektra-yamlcpp.so: shared object
Packaged contents of /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-yamlcpp into /openwrt/bin/packages/x86_64/packages/libelektra-yamlcpp_0.9.2-2_x86_64.ipk
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-xml/usr/lib/libelektra-xmltool.so: shared object
Packaged contents of /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-xml into /openwrt/bin/packages/x86_64/packages/libelektra-xml_0.9.2-2_x86_64.ipk
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-yajl/usr/lib/libelektra-yajl.so: shared object
Packaged contents of /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-yajl into /openwrt/bin/packages/x86_64/packages/libelektra-yajl_0.9.2-2_x86_64.ipk
cp: cannot stat '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-python.so': No such file or directory
make[3]: *** [Makefile:447: /openwrt/bin/packages/x86_64/packages/libelektra-python3_0.9.2-2_x86_64.ipk] Error 1
```
