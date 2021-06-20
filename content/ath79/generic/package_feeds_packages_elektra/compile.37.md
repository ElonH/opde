---
title: "compile.37"
date: 2021-06-20 22:31:33.724430
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
make package/feeds/packages/elektra/compile -j$(nproc) || make package/feeds/packages/elektra/compile V=s
```

#### Compile.txt

``` bash
-- The C compiler identification is GNU 8.4.0
-- The CXX compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-g++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Performing Test HAS_CXX_STD
-- Performing Test HAS_CXX_STD - Success
-- compiler/linker accepts version script? TRUE
-- compiler/linker supports symbol versioning? TRUE
-- GCC detected
-- Performing Test HAS_CFLAG_MAYBE_UNINITIALIZED
-- Performing Test HAS_CFLAG_MAYBE_UNINITIALIZED - Success
-- C flags are -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2=elektra-0.9.2 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -std=gnu99  -Wno-deprecated-declarations  -Wstrict-prototypes  -Wno-long-long -Wpedantic -Wno-variadic-macros -Wall -Wextra -Wno-overlength-strings -Wsign-compare -Wfloat-equal -Wformat -Wformat-security -Wshadow -Wcomments -Wtrigraphs -Wundef -Wuninitialized -Winit-self -Wmaybe-uninitialized -Wsign-compare -Wfloat-equal
-- CXX flags are -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2=elektra-0.9.2 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libintl-stub/include -std=c++11  -Wno-deprecated-declarations  -Wold-style-cast -Wstrict-null-sentinel -D_GLIBCXX_USE_NANOSLEEP -Wno-missing-field-initializers -Woverloaded-virtual  -Wsign-promo  -Wno-long-long -Wpedantic -Wno-variadic-macros -Wall -Wextra -Wno-overlength-strings -Wsign-compare -Wfloat-equal -Wformat -Wformat-security -Wshadow -Wcomments -Wtrigraphs -Wundef -Wuninitialized -Winit-self -Wmaybe-uninitialized
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
-- Exclude Plugin curlget because Curl-dev not found
-- Exclude Plugin curlget because libcurl >= 7.28.0 required
-- Exclude Plugin curlget because OpenSSL-dev not found
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
-- Exclude Plugin gitresolver because OpenSSL-dev not found
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
-- Exclude Plugin python because python 3 libs (libpython3-dev) not found
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
-- Check if the system is big endian - big endian
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


-- Build files have been written to: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/build
ninja: Entering directory `/openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/build'
[1/627] Building C object src/plugins/base64/CMakeFiles/elektra-base64-objects.dir/base64_functions.c.o
[2/627] Building C object src/plugins/base64/CMakeFiles/elektra-base64-objects.dir/base64.c.o
[3/627] Building C object src/plugins/blockresolver/CMakeFiles/elektra-blockresolver-objects.dir/blockresolver.c.o
[4/627] Building C object src/plugins/c/CMakeFiles/elektra-c-objects.dir/c.c.o
[5/627] Building C object src/plugins/cache/CMakeFiles/elektra-cache-objects.dir/cache.c.o
[6/627] Building CXX object src/plugins/ccode/CMakeFiles/elektra-ccode-objects.dir/ccode.cpp.o
[7/627] Building CXX object src/plugins/ccode/CMakeFiles/elektra-ccode-objects.dir/coder.cpp.o
[8/627] Building C object src/plugins/conditionals/CMakeFiles/elektra-conditionals-objects.dir/conditionals.c.o
[9/627] Building C object src/plugins/constants/CMakeFiles/elektra-constants-objects.dir/constants.c.o
[10/627] Building C object src/plugins/counter/CMakeFiles/elektra-counter-objects.dir/counter.c.o
[11/627] Building CXX object src/plugins/cpptemplate/CMakeFiles/elektra-cpptemplate-objects.dir/cpptemplate.cpp.o
[12/627] Building CXX object src/plugins/cpptemplate/CMakeFiles/elektra-cpptemplate-objects.dir/cpptemplate_delegate.cpp.o
[13/627] Building C object src/plugins/crypto/CMakeFiles/elektra-crypto-objects.dir/gcrypt_operations.c.o
[14/627] Building C object src/plugins/crypto/CMakeFiles/elektra-crypto-objects.dir/helper.c.o
[15/627] Building C object src/plugins/crypto/CMakeFiles/elektra-crypto-objects.dir/gpg.c.o
[16/627] Building C object src/plugins/crypto/CMakeFiles/elektra-crypto-objects.dir/crypto.c.o
[17/627] Building C object src/plugins/csvstorage/CMakeFiles/elektra-csvstorage-objects.dir/csvstorage.c.o
[18/627] Building C object src/plugins/iconv/CMakeFiles/elektra-iconv-objects.dir/iconv.c.o
[19/627] Building C object src/plugins/date/CMakeFiles/elektra-date-objects.dir/date.c.o
[20/627] Building C object src/plugins/dbus/CMakeFiles/elektra-dbus-objects.dir/dbus.c.o
[21/627] Building C object src/plugins/dbus/CMakeFiles/elektra-dbus-objects.dir/sendmessage.c.o
[22/627] Building C object src/plugins/dbusrecv/CMakeFiles/elektra-dbusrecv-objects.dir/dbusrecv.c.o
[23/627] Building C object src/plugins/dbusrecv/CMakeFiles/elektra-dbusrecv-objects.dir/receivemessage.c.o
[24/627] Building C object src/plugins/desktop/CMakeFiles/elektra-desktop-objects.dir/desktop.c.o
[25/627] Building CXX object src/plugins/directoryvalue/CMakeFiles/elektra-directoryvalue-objects.dir/directoryvalue.cpp.o
[26/627] Building CXX object src/plugins/directoryvalue/CMakeFiles/elektra-directoryvalue-objects.dir/directoryvalue_delegate.cpp.o
[27/627] Building C object src/plugins/doc/CMakeFiles/elektra-doc-objects.dir/doc.c.o
[28/627] Building C object src/plugins/dpkg/CMakeFiles/elektra-dpkg-objects.dir/dpkg.c.o
[29/627] Building CXX object src/plugins/dump/CMakeFiles/elektra-dump-objects.dir/dump.cpp.o
[30/627] Building C object src/plugins/error/CMakeFiles/elektra-error-objects.dir/error.c.o
[31/627] Building C object src/plugins/fcrypt/CMakeFiles/elektra-fcrypt-objects.dir/__/crypto/gpg.c.o
[32/627] Building C object src/plugins/fcrypt/CMakeFiles/elektra-fcrypt-objects.dir/fcrypt.c.o
[33/627] Building C object src/plugins/file/CMakeFiles/elektra-file-objects.dir/file.c.o
[34/627] Building C object src/plugins/filecheck/CMakeFiles/elektra-filecheck-objects.dir/filecheck.c.o
../src/plugins/filecheck/filecheck.c: In function 'checkFile':
../src/plugins/filecheck/filecheck.c:212:17: warning: initialization of 'iconv_t' {aka 'long int'} from 'void *' makes integer from pointer without a cast [-Wint-conversion]
  iconv_t conv = NULL;
                 ^~~~
[35/627] Building C object src/plugins/fstab/CMakeFiles/elektra-fstab-objects.dir/fstab.c.o
[36/627] Building C object src/plugins/glob/CMakeFiles/elektra-glob-objects.dir/glob.c.o
[37/627] Building C object src/plugins/gopts/CMakeFiles/elektra-gopts-objects.dir/gopts.c.o
[38/627] Building C object src/plugins/hexcode/CMakeFiles/elektra-hexcode-objects.dir/hexcode.c.o
[39/627] Building C object src/plugins/hexnumber/CMakeFiles/elektra-hexnumber-objects.dir/hexnumber.c.o
[40/627] Building C object src/plugins/hidden/CMakeFiles/elektra-hidden-objects.dir/hidden.c.o
[41/627] Building C object src/plugins/hosts/CMakeFiles/elektra-hosts-objects.dir/hosts-get.c.o
[42/627] Building C object src/plugins/hosts/CMakeFiles/elektra-hosts-objects.dir/hosts-set.c.o
[43/627] Building C object src/plugins/hosts/CMakeFiles/elektra-hosts-objects.dir/keymetaformatting.c.o
[44/627] Building C object src/plugins/ini/CMakeFiles/elektra-ini-objects.dir/ini.c.o
[45/627] Building C object src/plugins/ini/CMakeFiles/elektra-ini-objects.dir/inih-r29/inih.c.o
[46/627] Building C object src/plugins/ipaddr/CMakeFiles/elektra-ipaddr-objects.dir/ipaddr.c.o
[47/627] Building C object src/plugins/uname/CMakeFiles/elektra-uname-objects.dir/uname.c.o
[48/627] Building C object src/plugins/iterate/CMakeFiles/elektra-iterate-objects.dir/iterate.c.o
[49/627] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig-objects.dir/kconfig.cpp.o
[50/627] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig-objects.dir/kconfig_delegate.cpp.o
[51/627] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig-objects.dir/kconfig_parser.cpp.o
[52/627] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig-objects.dir/kconfig_parser_exception.cpp.o
[53/627] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig-objects.dir/kconfig_serializer.cpp.o
[54/627] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig-objects.dir/file_utility.cpp.o
[55/627] Building C object src/plugins/keytometa/CMakeFiles/elektra-keytometa-objects.dir/keytometa.c.o
[56/627] Building C object src/plugins/line/CMakeFiles/elektra-line-objects.dir/line.c.o
[57/627] Building C object src/plugins/lineendings/CMakeFiles/elektra-lineendings-objects.dir/lineendings.c.o
[58/627] Building C object src/plugins/list/CMakeFiles/elektra-list-objects.dir/list.c.o
[59/627] Building C object src/plugins/logchange/CMakeFiles/elektra-logchange-objects.dir/logchange.c.o
[60/627] Building C object src/plugins/macaddr/CMakeFiles/elektra-macaddr-objects.dir/macaddr.c.o
[61/627] Building C object src/plugins/mathcheck/CMakeFiles/elektra-mathcheck-objects.dir/mathcheck.c.o
[62/627] Building C object src/plugins/mathcheck/CMakeFiles/elektra-mathcheck-objects.dir/floathelper.c.o
[63/627] Building C object src/plugins/mini/CMakeFiles/elektra-mini-objects.dir/mini.c.o
[64/627] Building C object src/plugins/mmapstorage/CMakeFiles/elektra-mmapstorage-objects.dir/dynarray.c.o
[65/627] Building C object src/plugins/mmapstorage/CMakeFiles/elektra-mmapstorage-objects.dir/mmapstorage.c.o
[66/627] Building C object src/plugins/mmapstorage/CMakeFiles/elektra-mmapstorage_crc-objects.dir/dynarray.c.o
[67/627] Building C object src/plugins/mmapstorage/CMakeFiles/elektra-mmapstorage_crc-objects.dir/mmapstorage.c.o
[68/627] Building C object src/plugins/mozprefs/CMakeFiles/elektra-mozprefs-objects.dir/mozprefs.c.o
[69/627] Building C object src/plugins/network/CMakeFiles/elektra-network-objects.dir/network.c.o
[70/627] Building C object src/plugins/ni/CMakeFiles/elektra-ni-objects.dir/ni.c.o
[71/627] Building C object src/plugins/ni/CMakeFiles/elektra-ni-objects.dir/nickel-1.1.0/src/buf.c.o
[72/627] Building C object src/plugins/ni/CMakeFiles/elektra-ni-objects.dir/nickel-1.1.0/src/hash.c.o
../src/plugins/ni/nickel-1.1.0/src/hash.c: In function 'hashbig':
../src/plugins/ni/nickel-1.1.0/src/hash.c:1057:6: warning: this statement may fall through [-Wimplicit-fallthrough=]
    c += k[11];
    ~~^~~~~~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1058:3: note: here
   case 11:
   ^~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1059:6: warning: this statement may fall through [-Wimplicit-fallthrough=]
    c += ((uint32_t) k[10]) << 8;
    ~~^~~~~~~~~~~~~~~~~~~~~~~~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1060:3: note: here
   case 10:
   ^~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1061:6: warning: this statement may fall through [-Wimplicit-fallthrough=]
    c += ((uint32_t) k[9]) << 16;
    ~~^~~~~~~~~~~~~~~~~~~~~~~~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1062:3: note: here
   case 9:
   ^~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1063:6: warning: this statement may fall through [-Wimplicit-fallthrough=]
    c += ((uint32_t) k[8]) << 24;
    ~~^~~~~~~~~~~~~~~~~~~~~~~~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1064:3: note: here
   case 8:
   ^~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1065:6: warning: this statement may fall through [-Wimplicit-fallthrough=]
    b += k[7];
    ~~^~~~~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1066:3: note: here
   case 7:
   ^~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1067:6: warning: this statement may fall through [-Wimplicit-fallthrough=]
    b += ((uint32_t) k[6]) << 8;
    ~~^~~~~~~~~~~~~~~~~~~~~~~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1068:3: note: here
   case 6:
   ^~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1069:6: warning: this statement may fall through [-Wimplicit-fallthrough=]
    b += ((uint32_t) k[5]) << 16;
    ~~^~~~~~~~~~~~~~~~~~~~~~~~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1070:3: note: here
   case 5:
   ^~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1071:6: warning: this statement may fall through [-Wimplicit-fallthrough=]
    b += ((uint32_t) k[4]) << 24;
    ~~^~~~~~~~~~~~~~~~~~~~~~~~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1072:3: note: here
   case 4:
   ^~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1073:6: warning: this statement may fall through [-Wimplicit-fallthrough=]
    a += k[3];
    ~~^~~~~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1074:3: note: here
   case 3:
   ^~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1075:6: warning: this statement may fall through [-Wimplicit-fallthrough=]
    a += ((uint32_t) k[2]) << 8;
    ~~^~~~~~~~~~~~~~~~~~~~~~~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1076:3: note: here
   case 2:
   ^~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1077:6: warning: this statement may fall through [-Wimplicit-fallthrough=]
    a += ((uint32_t) k[1]) << 16;
    ~~^~~~~~~~~~~~~~~~~~~~~~~~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1078:3: note: here
   case 1:
   ^~~~
[73/627] Building C object src/plugins/ni/CMakeFiles/elektra-ni-objects.dir/nickel-1.1.0/src/io.c.o
[74/627] Building C object src/plugins/ni/CMakeFiles/elektra-ni-objects.dir/nickel-1.1.0/src/nickel.c.o
[75/627] Building C object src/plugins/noresolver/CMakeFiles/elektra-noresolver-objects.dir/noresolver.c.o
[76/627] Building C object src/plugins/null/CMakeFiles/elektra-null-objects.dir/null.c.o
[77/627] Building C object src/plugins/passwd/CMakeFiles/elektra-passwd-objects.dir/passwd.c.o
[78/627] Building C object src/plugins/path/CMakeFiles/elektra-path-objects.dir/path.c.o
[79/627] Building C object src/plugins/process/CMakeFiles/elektra-process-objects.dir/process.c.o
[80/627] Building C object src/plugins/profile/CMakeFiles/elektra-profile-objects.dir/profile.c.o
[81/627] Building C object src/plugins/quickdump/CMakeFiles/elektra-quickdump-objects.dir/quickdump.c.o
[82/627] Building C object src/plugins/range/CMakeFiles/elektra-range-objects.dir/range.c.o
[83/627] Building C object src/plugins/reference/CMakeFiles/elektra-reference-objects.dir/reference.c.o
[84/627] Building C object src/plugins/reference/CMakeFiles/elektra-reference-objects.dir/referencegraph.c.o
[85/627] Building C object src/plugins/rename/CMakeFiles/elektra-rename-objects.dir/rename.c.o
[86/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hpu_b-objects.dir/resolver.c.o
[87/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hpu_b-objects.dir/filename.c.o
[88/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xhp_x-objects.dir/resolver.c.o
[89/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xhp_x-objects.dir/filename.c.o
[90/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_pb_b-objects.dir/resolver.c.o
[91/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_pb_b-objects.dir/filename.c.o
[92/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_uhb_xb-objects.dir/resolver.c.o
[93/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_uhb_xb-objects.dir/filename.c.o
[94/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_b_b-objects.dir/resolver.c.o
[95/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_b_b-objects.dir/filename.c.o
[96/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hb_b-objects.dir/resolver.c.o
[97/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hb_b-objects.dir/filename.c.o
[98/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xb_x-objects.dir/resolver.c.o
[99/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xb_x-objects.dir/filename.c.o
[100/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hp_b-objects.dir/resolver.c.o
[101/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hp_b-objects.dir/filename.c.o
[102/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_ub_x-objects.dir/resolver.c.o
[103/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_ub_x-objects.dir/filename.c.o
[104/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xp_x-objects.dir/resolver.c.o
[105/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xp_x-objects.dir/filename.c.o
[106/627] Building C object src/plugins/rgbcolor/CMakeFiles/elektra-rgbcolor-objects.dir/rgbcolor.c.o
[107/627] Building C object src/plugins/shell/CMakeFiles/elektra-shell-objects.dir/shell.c.o
[108/627] Building C object src/plugins/spec/CMakeFiles/elektra-spec-objects.dir/spec.c.o
[109/627] Building C object src/plugins/specload/CMakeFiles/elektra-specload-objects.dir/specload.c.o
[110/627] Building C object src/plugins/sync/CMakeFiles/elektra-sync-objects.dir/sync.c.o
[111/627] Building C object src/plugins/syslog/CMakeFiles/elektra-syslog-objects.dir/syslog.c.o
[112/627] Building CXX object src/plugins/tcl/CMakeFiles/elektra-tcl-objects.dir/tcl.cpp.o
[113/627] Building CXX object src/plugins/tcl/CMakeFiles/elektra-tcl-objects.dir/action.cpp.o
In file included from ../src/plugins/tcl/action.cpp:18:
/openwrt/staging_dir/hostpkg/include/boost/bind.hpp:41:1: note: #pragma message: The practice of declaring the Bind placeholders (_1, _2, ...) in the global namespace is deprecated. Please use <boost/bind/bind.hpp> + using namespace boost::placeholders, or define BOOST_BIND_GLOBAL_PLACEHOLDERS to retain the current behavior.
 )
 ^
[114/627] Building CXX object src/plugins/tcl/CMakeFiles/elektra-tcl-objects.dir/printer.cpp.o
[115/627] Building C object src/plugins/template/CMakeFiles/elektra-template-objects.dir/template.c.o
[116/627] Building C object src/plugins/timeofday/CMakeFiles/elektra-timeofday-objects.dir/timeofday.c.o
[117/627] Building C object src/plugins/tracer/CMakeFiles/elektra-tracer-objects.dir/tracer.c.o
[118/627] Building C object src/plugins/type/CMakeFiles/elektra-type-objects.dir/type.c.o
[119/627] Building C object src/plugins/type/CMakeFiles/elektra-type-objects.dir/types.c.o
[120/627] Building C object src/plugins/unit/CMakeFiles/elektra-unit-objects.dir/unit.c.o
[121/627] Building C object src/plugins/validation/CMakeFiles/elektra-validation-objects.dir/validation.c.o
[122/627] Building C object src/plugins/validation/CMakeFiles/elektra-validation-objects.dir/lookupre.c.o
[123/627] Building C object src/plugins/wresolver/CMakeFiles/elektra-wresolver-objects.dir/wresolver.c.o
[124/627] Building CXX object src/plugins/xerces/CMakeFiles/elektra-xerces-objects.dir/xerces.cpp.o
[125/627] Building CXX object src/plugins/xerces/CMakeFiles/elektra-xerces-objects.dir/deserializer.cpp.o
[126/627] Building CXX object src/plugins/xerces/CMakeFiles/elektra-xerces-objects.dir/serializer.cpp.o
[127/627] Building C object src/plugins/xmltool/CMakeFiles/elektra-xmltool-objects.dir/xmltool.c.o
[128/627] Building C object src/plugins/xmltool/CMakeFiles/elektra-xmltool-objects.dir/stream.c.o
[129/627] Building C object src/plugins/xmltool/CMakeFiles/elektra-xmltool-objects.dir/kdbtools.c.o
[130/627] Building C object src/plugins/xmltool/CMakeFiles/elektra-xmltool-objects.dir/kscompare.c.o
[131/627] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl-objects.dir/yajl.c.o
[132/627] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl-objects.dir/iterator.c.o
[133/627] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl-objects.dir/yajl_gen.c.o
[134/627] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl-objects.dir/yajl_gen_open.c.o
[135/627] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl-objects.dir/yajl_gen_close.c.o
[136/627] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl-objects.dir/yajl_parse.c.o
[137/627] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl-objects.dir/name.c.o
[138/627] Building CXX object src/plugins/yamlcpp/CMakeFiles/elektra-yamlcpp-objects.dir/yamlcpp.cpp.o
[139/627] Building CXX object src/plugins/yamlcpp/CMakeFiles/elektra-yamlcpp-objects.dir/read.cpp.o
[140/627] Building CXX object src/plugins/yamlcpp/CMakeFiles/elektra-yamlcpp-objects.dir/write.cpp.o
[141/627] Building CXX object src/plugins/yamlsmith/CMakeFiles/elektra-yamlsmith-objects.dir/yamlsmith.cpp.o
[142/627] Building C object src/plugins/zeromqrecv/CMakeFiles/elektra-zeromqrecv-objects.dir/zeromqrecv.c.o
[143/627] Building C object src/plugins/zeromqrecv/CMakeFiles/elektra-zeromqrecv-objects.dir/subscribe.c.o
[144/627] Building C object src/plugins/zeromqsend/CMakeFiles/elektra-zeromqsend-objects.dir/zeromqsend.c.o
[145/627] Building C object src/plugins/zeromqsend/CMakeFiles/elektra-zeromqsend-objects.dir/publish.c.o
[146/627] Creating version script
[147/627] Building C object src/plugins/base64/CMakeFiles/elektra-base64.dir/base64_functions.c.o
[148/627] Building C object src/plugins/base64/CMakeFiles/elektra-base64.dir/base64.c.o
[149/627] Building C object src/plugins/blockresolver/CMakeFiles/elektra-blockresolver.dir/blockresolver.c.o
[150/627] Building C object src/plugins/c/CMakeFiles/elektra-c.dir/c.c.o
[151/627] Building C object src/plugins/dbus/CMakeFiles/elektra-dbus.dir/dbus.c.o
[152/627] Building C object src/plugins/cache/CMakeFiles/elektra-cache.dir/cache.c.o
[153/627] Building CXX object src/plugins/ccode/CMakeFiles/elektra-ccode.dir/ccode.cpp.o
[154/627] Building CXX object src/plugins/ccode/CMakeFiles/elektra-ccode.dir/coder.cpp.o
[155/627] Building C object src/plugins/conditionals/CMakeFiles/elektra-conditionals.dir/conditionals.c.o
[156/627] Building C object src/plugins/constants/CMakeFiles/elektra-constants.dir/constants.c.o
[157/627] Building C object src/plugins/counter/CMakeFiles/elektra-counter.dir/counter.c.o
[158/627] Building CXX object src/plugins/cpptemplate/CMakeFiles/elektra-cpptemplate.dir/cpptemplate.cpp.o
[159/627] Building CXX object src/plugins/cpptemplate/CMakeFiles/elektra-cpptemplate.dir/cpptemplate_delegate.cpp.o
[160/627] Building C object src/plugins/crypto/CMakeFiles/elektra-crypto.dir/gcrypt_operations.c.o
[161/627] Building C object src/plugins/crypto/CMakeFiles/elektra-crypto.dir/helper.c.o
[162/627] Building C object src/plugins/crypto/CMakeFiles/elektra-crypto.dir/gpg.c.o
[163/627] Building C object src/plugins/crypto/CMakeFiles/elektra-crypto.dir/crypto.c.o
[164/627] Building C object src/plugins/csvstorage/CMakeFiles/elektra-csvstorage.dir/csvstorage.c.o
[165/627] Building C object src/plugins/date/CMakeFiles/elektra-date.dir/date.c.o
[166/627] Building C object src/plugins/iterate/CMakeFiles/elektra-iterate.dir/iterate.c.o
[167/627] Building C object src/plugins/dbus/CMakeFiles/elektra-dbus.dir/sendmessage.c.o
[168/627] Building C object src/plugins/dbusrecv/CMakeFiles/elektra-dbusrecv.dir/dbusrecv.c.o
[169/627] Building C object src/plugins/dbusrecv/CMakeFiles/elektra-dbusrecv.dir/receivemessage.c.o
[170/627] Building C object src/plugins/desktop/CMakeFiles/elektra-desktop.dir/desktop.c.o
[171/627] Building CXX object src/plugins/directoryvalue/CMakeFiles/elektra-directoryvalue.dir/directoryvalue.cpp.o
[172/627] Building CXX object src/plugins/directoryvalue/CMakeFiles/elektra-directoryvalue.dir/directoryvalue_delegate.cpp.o
[173/627] Building C object src/plugins/doc/CMakeFiles/elektra-doc.dir/doc.c.o
[174/627] Building C object src/plugins/dpkg/CMakeFiles/elektra-dpkg.dir/dpkg.c.o
[175/627] Building CXX object src/plugins/dump/CMakeFiles/elektra-dump.dir/dump.cpp.o
[176/627] Building C object src/plugins/error/CMakeFiles/elektra-error.dir/error.c.o
[177/627] Building C object src/plugins/fcrypt/CMakeFiles/elektra-fcrypt.dir/__/crypto/gpg.c.o
[178/627] Building C object src/plugins/fcrypt/CMakeFiles/elektra-fcrypt.dir/fcrypt.c.o
[179/627] Building C object src/plugins/file/CMakeFiles/elektra-file.dir/file.c.o
[180/627] Building C object src/plugins/filecheck/CMakeFiles/elektra-filecheck.dir/filecheck.c.o
../src/plugins/filecheck/filecheck.c: In function 'checkFile':
../src/plugins/filecheck/filecheck.c:212:17: warning: initialization of 'iconv_t' {aka 'long int'} from 'void *' makes integer from pointer without a cast [-Wint-conversion]
  iconv_t conv = NULL;
                 ^~~~
[181/627] Building C object src/plugins/fstab/CMakeFiles/elektra-fstab.dir/fstab.c.o
[182/627] Building C object src/plugins/glob/CMakeFiles/elektra-glob.dir/glob.c.o
[183/627] Building C object src/plugins/gopts/CMakeFiles/elektra-gopts.dir/gopts.c.o
[184/627] Building C object src/plugins/hexcode/CMakeFiles/elektra-hexcode.dir/hexcode.c.o
[185/627] Building C object src/plugins/hexnumber/CMakeFiles/elektra-hexnumber.dir/hexnumber.c.o
[186/627] Building C object src/plugins/hidden/CMakeFiles/elektra-hidden.dir/hidden.c.o
[187/627] Building C object src/plugins/hosts/CMakeFiles/elektra-hosts.dir/hosts-get.c.o
[188/627] Building C object src/plugins/hosts/CMakeFiles/elektra-hosts.dir/hosts-set.c.o
[189/627] Building C object src/plugins/hosts/CMakeFiles/elektra-hosts.dir/keymetaformatting.c.o
[190/627] Building C object src/plugins/iconv/CMakeFiles/elektra-iconv.dir/iconv.c.o
[191/627] Building C object src/plugins/unit/CMakeFiles/elektra-unit.dir/unit.c.o
[192/627] Building C object src/plugins/ini/CMakeFiles/elektra-ini.dir/ini.c.o
[193/627] Building C object src/plugins/ini/CMakeFiles/elektra-ini.dir/inih-r29/inih.c.o
[194/627] Building C object src/plugins/ipaddr/CMakeFiles/elektra-ipaddr.dir/ipaddr.c.o
[195/627] Building C object src/plugins/uname/CMakeFiles/elektra-uname.dir/uname.c.o
[196/627] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig.dir/kconfig.cpp.o
[197/627] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig.dir/kconfig_delegate.cpp.o
[198/627] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig.dir/kconfig_parser.cpp.o
[199/627] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig.dir/kconfig_parser_exception.cpp.o
[200/627] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig.dir/kconfig_serializer.cpp.o
[201/627] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig.dir/file_utility.cpp.o
[202/627] Building C object src/plugins/keytometa/CMakeFiles/elektra-keytometa.dir/keytometa.c.o
[203/627] Building C object src/plugins/line/CMakeFiles/elektra-line.dir/line.c.o
[204/627] Building C object src/plugins/lineendings/CMakeFiles/elektra-lineendings.dir/lineendings.c.o
[205/627] Building C object src/plugins/list/CMakeFiles/elektra-list.dir/list.c.o
[206/627] Building C object src/plugins/logchange/CMakeFiles/elektra-logchange.dir/logchange.c.o
[207/627] Building C object src/plugins/macaddr/CMakeFiles/elektra-macaddr.dir/macaddr.c.o
[208/627] Building C object src/plugins/mathcheck/CMakeFiles/elektra-mathcheck.dir/mathcheck.c.o
[209/627] Building C object src/plugins/mathcheck/CMakeFiles/elektra-mathcheck.dir/floathelper.c.o
[210/627] Building C object src/plugins/mini/CMakeFiles/elektra-mini.dir/mini.c.o
[211/627] Building C object src/plugins/mmapstorage/CMakeFiles/elektra-mmapstorage.dir/dynarray.c.o
[212/627] Building C object src/plugins/mmapstorage/CMakeFiles/elektra-mmapstorage.dir/mmapstorage.c.o
[213/627] Building C object src/plugins/mmapstorage/CMakeFiles/elektra-mmapstorage_crc.dir/dynarray.c.o
[214/627] Building C object src/plugins/mmapstorage/CMakeFiles/elektra-mmapstorage_crc.dir/mmapstorage.c.o
[215/627] Building C object src/plugins/mozprefs/CMakeFiles/elektra-mozprefs.dir/mozprefs.c.o
[216/627] Building C object src/plugins/network/CMakeFiles/elektra-network.dir/network.c.o
[217/627] Building C object src/plugins/ni/CMakeFiles/elektra-ni.dir/ni.c.o
[218/627] Building C object src/plugins/ni/CMakeFiles/elektra-ni.dir/nickel-1.1.0/src/buf.c.o
[219/627] Building C object src/plugins/ni/CMakeFiles/elektra-ni.dir/nickel-1.1.0/src/hash.c.o
../src/plugins/ni/nickel-1.1.0/src/hash.c: In function 'hashbig':
../src/plugins/ni/nickel-1.1.0/src/hash.c:1057:6: warning: this statement may fall through [-Wimplicit-fallthrough=]
    c += k[11];
    ~~^~~~~~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1058:3: note: here
   case 11:
   ^~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1059:6: warning: this statement may fall through [-Wimplicit-fallthrough=]
    c += ((uint32_t) k[10]) << 8;
    ~~^~~~~~~~~~~~~~~~~~~~~~~~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1060:3: note: here
   case 10:
   ^~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1061:6: warning: this statement may fall through [-Wimplicit-fallthrough=]
    c += ((uint32_t) k[9]) << 16;
    ~~^~~~~~~~~~~~~~~~~~~~~~~~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1062:3: note: here
   case 9:
   ^~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1063:6: warning: this statement may fall through [-Wimplicit-fallthrough=]
    c += ((uint32_t) k[8]) << 24;
    ~~^~~~~~~~~~~~~~~~~~~~~~~~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1064:3: note: here
   case 8:
   ^~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1065:6: warning: this statement may fall through [-Wimplicit-fallthrough=]
    b += k[7];
    ~~^~~~~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1066:3: note: here
   case 7:
   ^~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1067:6: warning: this statement may fall through [-Wimplicit-fallthrough=]
    b += ((uint32_t) k[6]) << 8;
    ~~^~~~~~~~~~~~~~~~~~~~~~~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1068:3: note: here
   case 6:
   ^~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1069:6: warning: this statement may fall through [-Wimplicit-fallthrough=]
    b += ((uint32_t) k[5]) << 16;
    ~~^~~~~~~~~~~~~~~~~~~~~~~~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1070:3: note: here
   case 5:
   ^~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1071:6: warning: this statement may fall through [-Wimplicit-fallthrough=]
    b += ((uint32_t) k[4]) << 24;
    ~~^~~~~~~~~~~~~~~~~~~~~~~~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1072:3: note: here
   case 4:
   ^~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1073:6: warning: this statement may fall through [-Wimplicit-fallthrough=]
    a += k[3];
    ~~^~~~~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1074:3: note: here
   case 3:
   ^~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1075:6: warning: this statement may fall through [-Wimplicit-fallthrough=]
    a += ((uint32_t) k[2]) << 8;
    ~~^~~~~~~~~~~~~~~~~~~~~~~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1076:3: note: here
   case 2:
   ^~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1077:6: warning: this statement may fall through [-Wimplicit-fallthrough=]
    a += ((uint32_t) k[1]) << 16;
    ~~^~~~~~~~~~~~~~~~~~~~~~~~~~
../src/plugins/ni/nickel-1.1.0/src/hash.c:1078:3: note: here
   case 1:
   ^~~~
[220/627] Building C object src/plugins/ni/CMakeFiles/elektra-ni.dir/nickel-1.1.0/src/io.c.o
[221/627] Building C object src/plugins/ni/CMakeFiles/elektra-ni.dir/nickel-1.1.0/src/nickel.c.o
[222/627] Building C object src/plugins/noresolver/CMakeFiles/elektra-noresolver.dir/noresolver.c.o
[223/627] Building C object src/plugins/null/CMakeFiles/elektra-null.dir/null.c.o
[224/627] Building C object src/plugins/passwd/CMakeFiles/elektra-passwd.dir/passwd.c.o
[225/627] Building C object src/plugins/path/CMakeFiles/elektra-path.dir/path.c.o
[226/627] Building C object src/plugins/process/CMakeFiles/elektra-process.dir/process.c.o
[227/627] Building C object src/plugins/profile/CMakeFiles/elektra-profile.dir/profile.c.o
[228/627] Building C object src/plugins/quickdump/CMakeFiles/elektra-quickdump.dir/quickdump.c.o
[229/627] Building C object src/plugins/range/CMakeFiles/elektra-range.dir/range.c.o
[230/627] Building C object src/plugins/reference/CMakeFiles/elektra-reference.dir/reference.c.o
[231/627] Building C object src/plugins/reference/CMakeFiles/elektra-reference.dir/referencegraph.c.o
[232/627] Building C object src/plugins/rename/CMakeFiles/elektra-rename.dir/rename.c.o
[233/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_uhb_xb.dir/resolver.c.o
[234/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_uhb_xb.dir/filename.c.o
[235/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xhp_x.dir/resolver.c.o
[236/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xhp_x.dir/filename.c.o
[237/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xp_x.dir/resolver.c.o
[238/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xp_x.dir/filename.c.o
[239/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_pb_b.dir/resolver.c.o
[240/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_pb_b.dir/filename.c.o
[241/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hp_b.dir/resolver.c.o
[242/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hp_b.dir/filename.c.o
[243/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_b_b.dir/resolver.c.o
[244/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_b_b.dir/filename.c.o
[245/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hpu_b.dir/resolver.c.o
[246/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hpu_b.dir/filename.c.o
[247/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hb_b.dir/resolver.c.o
[248/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hb_b.dir/filename.c.o
[249/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xb_x.dir/resolver.c.o
[250/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xb_x.dir/filename.c.o
[251/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_ub_x.dir/resolver.c.o
[252/627] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_ub_x.dir/filename.c.o
[253/627] Building C object src/plugins/rgbcolor/CMakeFiles/elektra-rgbcolor.dir/rgbcolor.c.o
[254/627] Building C object src/plugins/shell/CMakeFiles/elektra-shell.dir/shell.c.o
[255/627] Building C object src/plugins/spec/CMakeFiles/elektra-spec.dir/spec.c.o
[256/627] Building C object src/plugins/specload/CMakeFiles/elektra-specload.dir/specload.c.o
[257/627] Building C object src/plugins/sync/CMakeFiles/elektra-sync.dir/sync.c.o
[258/627] Building C object src/plugins/syslog/CMakeFiles/elektra-syslog.dir/syslog.c.o
[259/627] Building CXX object src/plugins/tcl/CMakeFiles/elektra-tcl.dir/tcl.cpp.o
[260/627] Building CXX object src/plugins/tcl/CMakeFiles/elektra-tcl.dir/action.cpp.o
In file included from ../src/plugins/tcl/action.cpp:18:
/openwrt/staging_dir/hostpkg/include/boost/bind.hpp:41:1: note: #pragma message: The practice of declaring the Bind placeholders (_1, _2, ...) in the global namespace is deprecated. Please use <boost/bind/bind.hpp> + using namespace boost::placeholders, or define BOOST_BIND_GLOBAL_PLACEHOLDERS to retain the current behavior.
 )
 ^
[261/627] Building CXX object src/plugins/tcl/CMakeFiles/elektra-tcl.dir/printer.cpp.o
[262/627] Building C object src/plugins/template/CMakeFiles/elektra-template.dir/template.c.o
[263/627] Building C object src/plugins/timeofday/CMakeFiles/elektra-timeofday.dir/timeofday.c.o
[264/627] Building C object src/plugins/tracer/CMakeFiles/elektra-tracer.dir/tracer.c.o
[265/627] Building C object src/plugins/type/CMakeFiles/elektra-type.dir/type.c.o
[266/627] Building C object src/plugins/type/CMakeFiles/elektra-type.dir/types.c.o
[267/627] Building C object src/plugins/validation/CMakeFiles/elektra-validation.dir/validation.c.o
[268/627] Building C object src/plugins/validation/CMakeFiles/elektra-validation.dir/lookupre.c.o
[269/627] Building C object src/plugins/wresolver/CMakeFiles/elektra-wresolver.dir/wresolver.c.o
[270/627] Building CXX object src/plugins/xerces/CMakeFiles/elektra-xerces.dir/xerces.cpp.o
[271/627] Building CXX object src/plugins/xerces/CMakeFiles/elektra-xerces.dir/deserializer.cpp.o
[272/627] Building CXX object src/plugins/xerces/CMakeFiles/elektra-xerces.dir/serializer.cpp.o
[273/627] Building C object src/plugins/xmltool/CMakeFiles/elektra-xmltool.dir/xmltool.c.o
[274/627] Building C object src/plugins/xmltool/CMakeFiles/elektra-xmltool.dir/stream.c.o
[275/627] Building C object src/plugins/xmltool/CMakeFiles/elektra-xmltool.dir/kdbtools.c.o
[276/627] Building C object src/plugins/xmltool/CMakeFiles/elektra-xmltool.dir/kscompare.c.o
[277/627] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl.dir/yajl.c.o
[278/627] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl.dir/iterator.c.o
[279/627] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl.dir/yajl_gen.c.o
[280/627] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl.dir/yajl_gen_open.c.o
[281/627] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl.dir/yajl_gen_close.c.o
[282/627] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl.dir/yajl_parse.c.o
[283/627] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl.dir/name.c.o
[284/627] Building CXX object src/plugins/yamlcpp/CMakeFiles/elektra-yamlcpp.dir/yamlcpp.cpp.o
[285/627] Building CXX object src/plugins/yamlcpp/CMakeFiles/elektra-yamlcpp.dir/read.cpp.o
[286/627] Building CXX object src/plugins/yamlcpp/CMakeFiles/elektra-yamlcpp.dir/write.cpp.o
[287/627] Building CXX object src/plugins/yamlsmith/CMakeFiles/elektra-yamlsmith.dir/yamlsmith.cpp.o
[288/627] Building C object src/plugins/zeromqrecv/CMakeFiles/elektra-zeromqrecv.dir/zeromqrecv.c.o
[289/627] Building C object src/plugins/zeromqrecv/CMakeFiles/elektra-zeromqrecv.dir/subscribe.c.o
[290/627] Building C object src/plugins/zeromqsend/CMakeFiles/elektra-zeromqsend.dir/zeromqsend.c.o
[291/627] Building C object src/plugins/zeromqsend/CMakeFiles/elektra-zeromqsend.dir/publish.c.o
[292/627] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/backend.cpp.o
[293/627] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/backendbuilder.cpp.o
[294/627] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/backendparser.cpp.o
[295/627] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/backends.cpp.o
[296/627] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/helper/comparison.cpp.o
[297/627] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/helper/keyhelper.cpp.o
[298/627] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/automergeconfiguration.cpp.o
[299/627] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/automergestrategy.cpp.o
[300/627] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/importmergeconfiguration.cpp.o
[301/627] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/interactivemergestrategy.cpp.o
[302/627] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/mergeconflictstrategy.cpp.o
[303/627] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/mergeresult.cpp.o
[304/627] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/mergingkdb.cpp.o
[305/627] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/metamergestrategy.cpp.o
[306/627] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/newkeystrategy.cpp.o
[307/627] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/onesidemergeconfiguration.cpp.o
[308/627] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/onesidestrategy.cpp.o
[309/627] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/onesidevaluestrategy.cpp.o
[310/627] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/overwritemergeconfiguration.cpp.o
[311/627] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/threewaymerge.cpp.o
[312/627] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/modules.cpp.o
[313/627] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/plugin.cpp.o
[314/627] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/plugindatabase.cpp.o
[315/627] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/plugins.cpp.o
[316/627] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/pluginspec.cpp.o
[317/627] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/specreader.cpp.o
[318/627] Building CXX object src/libs/tools/examples/CMakeFiles/merging.dir/merging.cpp.o
[319/627] Building CXX object src/libs/tools/examples/CMakeFiles/backend.dir/backend.cpp.o
[320/627] Building CXX object src/libs/tools/benchmarks/CMakeFiles/benchmark_plugins.dir/benchmark_plugins.cpp.o
[321/627] Building C object src/libs/ease/CMakeFiles/elektra-ease-objects.dir/array.c.o
[322/627] Building C object src/libs/ease/CMakeFiles/elektra-ease-objects.dir/conversion.c.o
[323/627] Building C object src/libs/ease/CMakeFiles/elektra-ease-objects.dir/functional.c.o
[324/627] Building C object src/libs/ease/CMakeFiles/elektra-ease-objects.dir/keyname.c.o
[325/627] Building C object src/libs/ease/CMakeFiles/elektra-ease-objects.dir/reference.c.o
[326/627] Building C object src/libs/globbing/CMakeFiles/elektra-globbing-objects.dir/globbing.c.o
[327/627] Building C object src/libs/proposal/CMakeFiles/elektra-proposal-objects.dir/proposal.c.o
[328/627] Building C object src/libs/meta/CMakeFiles/elektra-meta-objects.dir/meta.c.o
[329/627] Building C object src/libs/plugin/CMakeFiles/elektra-plugin-objects.dir/plugin.c.o
[330/627] Building C object src/libs/pluginprocess/CMakeFiles/elektra-pluginprocess-objects.dir/pluginprocess.c.o
[331/627] Building C object src/libs/utility/CMakeFiles/elektra-utility-objects.dir/text.c.o
[332/627] Building C object src/libs/io/CMakeFiles/elektra-io-objects.dir/io.c.o
[333/627] Building C object src/libs/io/adapter/dbus/CMakeFiles/io-adapter-dbus.dir/dbus.c.o
[334/627] Building C object src/libs/io/adapter/zeromq/CMakeFiles/io-adapter-zeromq.dir/zeromq.c.o
[335/627] Building C object src/libs/invoke/CMakeFiles/elektra-invoke-objects.dir/invoke.c.o
[336/627] Building C object src/libs/highlevel/CMakeFiles/elektra-highlevel-objects.dir/elektra.c.o
[337/627] Building C object src/libs/highlevel/CMakeFiles/elektra-highlevel-objects.dir/elektra_array_value.c.o
[338/627] Building C object src/libs/highlevel/CMakeFiles/elektra-highlevel-objects.dir/elektra_error.c.o
[339/627] Building C object src/libs/highlevel/CMakeFiles/elektra-highlevel-objects.dir/elektra_value.c.o
[340/627] Building C object src/libs/merge/CMakeFiles/elektra-merge-objects.dir/kdbmerge.c.o
[341/627] Building C object src/libs/opts/CMakeFiles/elektra-opts-objects.dir/opts.c.o
[342/627] Building C object src/libs/elektra/CMakeFiles/elektra-kdb.dir/backend.c.o
[343/627] Building C object src/libs/elektra/CMakeFiles/elektra-kdb.dir/kdb.c.o
[344/627] Building C object src/libs/elektra/CMakeFiles/elektra-kdb.dir/mount.c.o
[345/627] Building C object src/libs/elektra/CMakeFiles/elektra-kdb.dir/plugin.c.o
[346/627] Building C object src/libs/elektra/CMakeFiles/elektra-kdb.dir/split.c.o
[347/627] Building C object src/libs/elektra/CMakeFiles/elektra-kdb.dir/trie.c.o
[348/627] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/errors.c.o
[349/627] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/global.c.o
[350/627] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/internal.c.o
[351/627] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/kdbenum.c.o
[352/627] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/key.c.o
[353/627] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/keyhelpers.c.o
[354/627] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/keymeta.c.o
[355/627] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/keyname.c.o
[356/627] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/keyset.c.o
[357/627] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/keytest.c.o
[358/627] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/keyvalue.c.o
[359/627] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/nolog.c.o
[360/627] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/owner.c.o
[361/627] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/proposal.c.o
[362/627] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/rand.c.o
[363/627] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/__/loader/dl.c.o
[364/627] Linking C shared library lib/libelektra-core.so.0.9.2
[365/627] Creating library symlink lib/libelektra-core.so.4 lib/libelektra-core.so
[366/627] Linking C shared library lib/libelektra-ease.so.0.9.2
[367/627] Creating library symlink lib/libelektra-ease.so.4 lib/libelektra-ease.so
[368/627] Linking C shared library lib/libelektra-globbing.so.0.9.2
[369/627] Creating library symlink lib/libelektra-globbing.so.4 lib/libelektra-globbing.so
[370/627] Linking C shared library lib/libelektra-proposal.so.0.9.2
[371/627] Creating library symlink lib/libelektra-proposal.so.4 lib/libelektra-proposal.so
[372/627] Linking C shared library lib/libelektra-meta.so.0.9.2
[373/627] Creating library symlink lib/libelektra-meta.so.4 lib/libelektra-meta.so
[374/627] Linking C shared library lib/libelektra-plugin.so.0.9.2
[375/627] Creating library symlink lib/libelektra-plugin.so.4 lib/libelektra-plugin.so
[376/627] Linking C shared module lib/libelektra-base64.so
[377/627] Linking C shared module lib/libelektra-c.so
[378/627] Linking CXX shared module lib/libelektra-ccode.so
[379/627] Linking C shared module lib/libelektra-conditionals.so
[380/627] Linking C shared module lib/libelektra-constants.so
[381/627] Linking C shared module lib/libelektra-counter.so
[382/627] Linking CXX shared module lib/libelektra-cpptemplate.so
[383/627] Linking C shared module lib/libelektra-date.so
[384/627] Linking C shared module lib/libelektra-dbus.so
[385/627] Linking C shared module lib/libelektra-desktop.so
[386/627] Linking CXX shared module lib/libelektra-directoryvalue.so
[387/627] Linking C shared module lib/libelektra-dpkg.so
[388/627] Linking CXX shared module lib/libelektra-dump.so
[389/627] Linking C shared module lib/libelektra-error.so
[390/627] Linking C shared module lib/libelektra-fcrypt.so
[391/627] Linking C shared module lib/libelektra-file.so
[392/627] Linking C shared module lib/libelektra-filecheck.so
[393/627] Linking C shared module lib/libelektra-fstab.so
[394/627] Linking C shared module lib/libelektra-glob.so
[395/627] Linking C shared module lib/libelektra-hexcode.so
[396/627] Linking C shared module lib/libelektra-hexnumber.so
[397/627] Linking C shared module lib/libelektra-hidden.so
[398/627] Linking C shared module lib/libelektra-hosts.so
[399/627] Linking C shared module lib/libelektra-iconv.so
[400/627] Linking C shared module lib/libelektra-unit.so
[401/627] Linking C shared module lib/libelektra-ini.so
[402/627] Linking C shared module lib/libelektra-ipaddr.so
[403/627] Linking C shared module lib/libelektra-uname.so
[404/627] Linking C shared module lib/libelektra-iterate.so
[405/627] Linking CXX shared module lib/libelektra-kconfig.so
[406/627] Linking C shared module lib/libelektra-keytometa.so
[407/627] Linking C shared module lib/libelektra-line.so
[408/627] Linking C shared module lib/libelektra-lineendings.so
[409/627] Linking C shared module lib/libelektra-logchange.so
[410/627] Linking C shared module lib/libelektra-macaddr.so
[411/627] Linking C shared module lib/libelektra-mathcheck.so
[412/627] Linking C shared module lib/libelektra-mmapstorage.so
[413/627] Linking C shared module lib/libelektra-mmapstorage_crc.so
[414/627] Linking C shared module lib/libelektra-network.so
[415/627] Linking C shared module lib/libelektra-ni.so
[416/627] Linking C shared module lib/libelektra-noresolver.so
[417/627] Linking C shared module lib/libelektra-null.so
[418/627] Linking C shared module lib/libelektra-passwd.so
[419/627] Linking C shared module lib/libelektra-path.so
[420/627] Linking C shared module lib/libelektra-profile.so
[421/627] Linking C shared module lib/libelektra-quickdump.so
[422/627] Linking C shared module lib/libelektra-range.so
[423/627] Linking C shared module lib/libelektra-reference.so
[424/627] Linking C shared module lib/libelektra-rename.so
[425/627] Linking C shared module lib/libelektra-resolver_fm_uhb_xb.so
[426/627] Linking C shared module lib/libelektra-resolver_fm_xhp_x.so
[427/627] Linking C shared module lib/libelektra-resolver_fm_xp_x.so
[428/627] Linking C shared module lib/libelektra-resolver_fm_pb_b.so
[429/627] Linking C shared module lib/libelektra-resolver_fm_hp_b.so
[430/627] Linking C shared module lib/libelektra-resolver_fm_b_b.so
[431/627] Linking C shared module lib/libelektra-resolver_fm_hpu_b.so
[432/627] Linking C shared module lib/libelektra-resolver_fm_hb_b.so
[433/627] Linking C shared module lib/libelektra-resolver_fm_xb_x.so
[434/627] Linking C shared module lib/libelektra-resolver_fm_ub_x.so
[435/627] Linking C shared module lib/libelektra-rgbcolor.so
[436/627] Linking C shared module lib/libelektra-shell.so
[437/627] Linking C shared module lib/libelektra-spec.so
[438/627] Linking C shared module lib/libelektra-sync.so
[439/627] Linking C shared module lib/libelektra-syslog.so
[440/627] Linking CXX shared module lib/libelektra-tcl.so
[441/627] Linking C shared module lib/libelektra-template.so
[442/627] Linking C shared module lib/libelektra-timeofday.so
[443/627] Linking C shared module lib/libelektra-tracer.so
[444/627] Linking C shared module lib/libelektra-type.so
[445/627] Linking C shared module lib/libelektra-validation.so
[446/627] Linking C shared module lib/libelektra-wresolver.so
[447/627] Linking CXX shared module lib/libelektra-xerces.so
[448/627] Linking C shared module lib/libelektra-xmltool.so
[449/627] Linking C shared module lib/libelektra-yajl.so
[450/627] Linking CXX shared module lib/libelektra-yamlcpp.so
[451/627] Linking CXX shared module lib/libelektra-yamlsmith.so
[452/627] Linking C shared module lib/libelektra-zeromqsend.so
[453/627] Linking C shared library lib/libelektra-utility.so.0.9.2
[454/627] Creating library symlink lib/libelektra-utility.so.4 lib/libelektra-utility.so
[455/627] Linking C shared module lib/libelektra-mini.so
[456/627] Linking C shared module lib/libelektra-mozprefs.so
[457/627] Linking C shared library lib/libelektra-merge.so.0.9.2
[458/627] Creating library symlink lib/libelektra-merge.so.4 lib/libelektra-merge.so
[459/627] Linking C shared library lib/libelektra-opts.so.0.9.2
[460/627] Creating library symlink lib/libelektra-opts.so.4 lib/libelektra-opts.so
[461/627] Linking C shared module lib/libelektra-gopts.so
[462/627] Linking C shared library lib/libelektra-kdb.so.0.9.2
[463/627] Creating library symlink lib/libelektra-kdb.so.4 lib/libelektra-kdb.so
[464/627] Linking C shared module lib/libelektra-cache.so
[465/627] Linking C shared module lib/libelektra-csvstorage.so
[466/627] Linking C shared module lib/libelektra-doc.so
[467/627] Linking CXX shared library lib/libelektratools.so.0.9.2
[468/627] Creating library symlink lib/libelektratools.so.2 lib/libelektratools.so
[469/627] Linking CXX executable bin/merging
[470/627] Linking CXX executable bin/backend
[471/627] Linking CXX executable bin/benchmark_plugins
[472/627] Linking C shared library lib/libelektra-invoke.so.0.9.2
[473/627] Creating library symlink lib/libelektra-invoke.so.4 lib/libelektra-invoke.so
[474/627] Linking C shared module lib/libelektra-blockresolver.so
[475/627] Linking C shared module lib/libelektra-crypto.so
[476/627] Linking C shared module lib/libelektra-list.so
[477/627] Linking C shared module lib/libelektra-specload.so
[478/627] Linking C shared library lib/libelektra-pluginprocess.so.0.9.2
[479/627] Creating library symlink lib/libelektra-pluginprocess.so.4 lib/libelektra-pluginprocess.so
[480/627] Linking C shared module lib/libelektra-process.so
[481/627] Linking C shared library lib/libelektra-io.so.0.9.2
[482/627] Creating library symlink lib/libelektra-io.so.4 lib/libelektra-io.so
[483/627] Linking C shared module lib/libelektra-dbusrecv.so
[484/627] Linking C shared module lib/libelektra-zeromqrecv.so
[485/627] Linking C shared library lib/libelektra-highlevel.so.0.9.2
[486/627] Creating library symlink lib/libelektra-highlevel.so.4 lib/libelektra-highlevel.so
[487/627] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_cascading.dir/cpp_cascading.cpp.o
[488/627] Linking CXX executable bin/cpp_cascading
[489/627] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_dup.dir/cpp_example_dup.cpp.o
[490/627] Linking CXX executable bin/cpp_example_dup
[491/627] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_get.dir/cpp_example_get.cpp.o
[492/627] Linking CXX executable bin/cpp_example_get
[493/627] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_set.dir/cpp_example_set.cpp.o
[494/627] Linking CXX executable bin/cpp_example_set
[495/627] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_userio.dir/cpp_example_userio.cpp.o
[496/627] Linking CXX executable bin/cpp_example_userio
[497/627] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_hello.dir/cpp_example_hello.cpp.o
[498/627] Linking CXX executable bin/cpp_example_hello
[499/627] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_hierarchy.dir/cpp_example_hierarchy.cpp.o
[500/627] Linking CXX executable bin/cpp_example_hierarchy
[501/627] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_iter.dir/cpp_example_iter.cpp.o
[502/627] Linking CXX executable bin/cpp_example_iter
[503/627] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_io.dir/cpp_example_io.cpp.o
[504/627] Linking CXX executable bin/cpp_example_io
[505/627] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_iter_name.dir/cpp_example_iter_name.cpp.o
[506/627] Linking CXX executable bin/cpp_example_iter_name
[507/627] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_ks.dir/cpp_example_ks.cpp.o
[508/627] Linking CXX executable bin/cpp_example_ks
[509/627] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_ordering.dir/cpp_example_ordering.cpp.o
[510/627] Linking CXX executable bin/cpp_example_ordering
[511/627] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_userexception.dir/cpp_example_userexception.cpp.o
[512/627] Linking CXX executable bin/cpp_example_userexception
[513/627] Building CXX object src/bindings/cpp/benchmarks/CMakeFiles/benchmark_thread.dir/benchmark_thread.cpp.o
[514/627] Linking CXX executable bin/benchmark_thread
[515/627] Building CXX object src/bindings/cpp/benchmarks/CMakeFiles/benchmark_sync.dir/benchmark_sync.cpp.o
[516/627] Linking CXX executable bin/benchmark_sync
[517/627] Generating ../../../../include/gen/templates.hpp
[518/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/ansicolors.cpp.o
[519/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/cache.cpp.o
[520/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/cmdline.cpp.o
[521/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/cmerge.cpp.o
[522/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/command.cpp.o
[523/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/complete.cpp.o
[524/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/convert.cpp.o
[525/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/cp.cpp.o
[526/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/editor.cpp.o
[527/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/export.cpp.o
[528/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/external.cpp.o
[529/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/file.cpp.o
[530/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/find.cpp.o
[531/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/gen.cpp.o
[532/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/gen/highlevel/common.cpp.o
[533/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/gen/highlevel/enums.cpp.o
[534/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/gen/highlevel/highlevel.cpp.o
[535/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/gen/highlevel/structs.cpp.o
[536/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/gen/template.cpp.o
[537/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/get.cpp.o
[538/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/globalmount.cpp.o
[539/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/globalumount.cpp.o
[540/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/import.cpp.o
[541/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/listcommands.cpp.o
[542/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/ls.cpp.o
[543/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/main.cpp.o
[544/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/merge.cpp.o
[545/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/mergehelper.cpp.o
[546/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/metaget.cpp.o
[547/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/metals.cpp.o
[548/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/metaremove.cpp.o
[549/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/metaset.cpp.o
[550/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/mount.cpp.o
[551/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/mountbase.cpp.o
[552/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/mv.cpp.o
[553/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/plugincheck.cpp.o
[554/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/plugininfo.cpp.o
[555/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/pluginlist.cpp.o
[556/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/remount.cpp.o
[557/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/rm.cpp.o
[558/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/set.cpp.o
[559/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/sget.cpp.o
[560/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/shell.cpp.o
[561/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/showmeta.cpp.o
[562/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/specmount.cpp.o
[563/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/test.cpp.o
[564/627] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/umount.cpp.o
[565/627] Linking CXX executable bin/kdb
[566/627] Building C object examples/CMakeFiles/set_key.dir/set_key.c.o
[567/627] Linking C executable bin/set_key
[568/627] Building C object examples/CMakeFiles/keyBasename.dir/keyBasename.c.o
[569/627] Linking C executable bin/keyBasename
[570/627] Building C object examples/CMakeFiles/kdbopen.dir/kdbopen.c.o
[571/627] Linking C executable bin/kdbopen
[572/627] Building C object examples/CMakeFiles/optsSnippets.dir/optsSnippets.c.o
[573/627] Linking C executable bin/optsSnippets
[574/627] Building C object examples/CMakeFiles/kdbget_error.dir/kdbget_error.c.o
[575/627] Linking C executable bin/kdbget_error
[576/627] Building C object examples/CMakeFiles/reference.dir/reference.c.o
[577/627] Linking C executable bin/reference
[578/627] Building C object examples/CMakeFiles/kdbget.dir/kdbget.c.o
[579/627] Linking C executable bin/kdbget
[580/627] Building C object examples/CMakeFiles/hello.dir/hello.c.o
[581/627] Linking C executable bin/hello
[582/627] Building C object examples/CMakeFiles/keyNew.dir/keyNew.c.o
[583/627] Linking C executable bin/keyNew
[584/627] Building C object examples/CMakeFiles/keyCopy.dir/keyCopy.c.o
[585/627] Linking C executable bin/keyCopy
[586/627] Building C object examples/CMakeFiles/ksIterate.dir/ksIterate.c.o
[587/627] Linking C executable bin/ksIterate
[588/627] Building C object examples/CMakeFiles/functional.dir/functional.c.o
[589/627] Linking C executable bin/functional
[590/627] Building C object examples/CMakeFiles/keyNewExample.dir/keyNewExample.c.o
[591/627] Linking C executable bin/keyNewExample
[592/627] Building C object examples/CMakeFiles/keyMetaKeySet.dir/keyMetaKeySet.c.o
[593/627] Linking C executable bin/keyMetaKeySet
[594/627] Building C object examples/CMakeFiles/cascading.dir/cascading.c.o
[595/627] Linking C executable bin/cascading
[596/627] Building C object examples/CMakeFiles/gopts.dir/gopts.c.o
[597/627] Linking C executable bin/gopts
[598/627] Building C object examples/CMakeFiles/keyName.dir/keyName.c.o
[599/627] Linking C executable bin/keyName
[600/627] Building C object examples/CMakeFiles/kdbintro.dir/kdbintro.c.o
[601/627] Linking C executable bin/kdbintro
[602/627] Building C object examples/CMakeFiles/opts.dir/opts.c.o
[603/627] Linking C executable bin/opts
[604/627] Building C object examples/CMakeFiles/iterate.dir/iterate.c.o
[605/627] Linking C executable bin/iterate
[606/627] Building C object examples/CMakeFiles/kdbset.dir/kdbset.c.o
[607/627] Linking C executable bin/kdbset
[608/627] Building C object examples/CMakeFiles/helloElektra.dir/helloElektra.c.o
[609/627] Linking C executable bin/helloElektra
[610/627] Building C object examples/CMakeFiles/keyset.dir/keyset.c.o
[611/627] Linking C executable bin/keyset
[612/627] Building C object examples/CMakeFiles/meta.dir/meta.c.o
[613/627] Linking C executable bin/meta
[614/627] Building C object examples/CMakeFiles/ksCut.dir/ksCut.c.o
[615/627] Linking C executable bin/ksCut
[616/627] Building C object examples/CMakeFiles/ksNewExample.dir/ksNewExample.c.o
[617/627] Linking C executable bin/ksNewExample
[618/627] Building C object examples/CMakeFiles/optsCommands.dir/optsCommands.c.o
[619/627] Linking C executable bin/optsCommands
[620/627] Building C object examples/CMakeFiles/ksLookupPop.dir/ksLookupPop.c.o
[621/627] Linking C executable bin/ksLookupPop
[622/627] Building C object examples/CMakeFiles/keyMeta.dir/keyMeta.c.o
[623/627] Linking C executable bin/keyMeta
[624/627] Building C object examples/CMakeFiles/ksNew.dir/ksNew.c.o
[625/627] Linking C executable bin/ksNew
[626/627] Building C object examples/CMakeFiles/namespace.dir/namespace.c.o
[627/627] Linking C executable bin/namespace
ninja: Entering directory `/openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/build'
[0/1] Install the project...
-- Install configuration: "Release"
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/share/doc/elektra/LICENSE.md
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/cmake/Elektra/ElektraConfig.cmake
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/cmake/Elektra/ElektraConfigVersion.cmake
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/pkgconfig/elektra.pc
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/benchmark-createtree
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/upgrade-bootstrap
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/mountpoint-info
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/check-env-dep
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/configure-firefox
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/change-resolver-symlink
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/change-storage-symlink
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/stash
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/restore
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/reset
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/reset-elektra
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/umount-all
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/ffconfig/writeConfigFiles
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/ffconfig/setupConfig
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/ffconfig/setupProxy
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/ffconfig/setupHomepage
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/backup
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/elektrify-getenv
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/elektrify-open
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/list-tools
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/cmerge-config-files
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/find-tools
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/install-config-file
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/mount-augeas
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/mount-info
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/mount-kde
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/mount-list-all-files
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/mount-openicc
-- Up-to-date: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/mountpoint-info
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/update-snippet-repository
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/elektra/tool_exec/install-sh-completion
-- Installing symlink: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib//libelektra-storage.so -> libelektra-ini.so
-- Installing symlink: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib//libelektra-resolver.so -> libelektra-resolver_fm_pb_b.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-base64.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-blockresolver.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-c.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-cache.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-ccode.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-conditionals.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-constants.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-counter.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-cpptemplate.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-crypto.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-csvstorage.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-date.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-dbus.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-dbusrecv.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-desktop.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-directoryvalue.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-doc.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-dpkg.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-dump.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-error.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-fcrypt.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-file.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-filecheck.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-fstab.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-glob.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-gopts.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-hexcode.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-hexnumber.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-hidden.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-hosts.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-iconv.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-ini.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-ipaddr.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-iterate.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-kconfig.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-keytometa.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-line.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-lineendings.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-list.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-logchange.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-macaddr.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-mathcheck.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-mini.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-mmapstorage_crc.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-mmapstorage.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-mozprefs.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-network.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-ni.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-noresolver.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-null.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-passwd.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-path.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-process.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-profile.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-quickdump.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-range.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-reference.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-rename.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-resolver_fm_pb_b.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-resolver_fm_b_b.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-resolver_fm_hb_b.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-resolver_fm_hp_b.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-resolver_fm_ub_x.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-resolver_fm_xb_x.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-resolver_fm_xp_x.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-resolver_fm_xhp_x.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-resolver_fm_uhb_xb.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-resolver_fm_hpu_b.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-rgbcolor.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-shell.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-spec.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-specload.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-sync.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-syslog.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-tcl.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-template.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-timeofday.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-tracer.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-type.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-uname.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-unit.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-validation.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-wresolver.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-xerces.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-xmltool.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-yajl.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-yamlcpp.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-yamlsmith.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-zeromqrecv.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-zeromqsend.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/backend.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/backendbuilder.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/backendparser.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/backends.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/modules.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/plugin.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/plugindatabase.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/plugins.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/pluginspec.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/specreader.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/toolexcept.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/helper/comparison.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/helper/keyhelper.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/automergeconfiguration.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/automergestrategy.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/importmergeconfiguration.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/interactivemergestrategy.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/mergeconfiguration.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/mergeconflict.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/mergeconflictstrategy.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/mergeresult.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/mergetask.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/mergingkdb.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/metamergestrategy.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/newkeystrategy.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/onesidemergeconfiguration.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/onesidestrategy.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/onesidevaluestrategy.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/overwritemergeconfiguration.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/merging/threewaymerge.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektratools.so.0.9.2
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektratools.so.2
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektratools.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-ease.so.0.9.2
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-ease.so.4
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-ease.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-globbing.so.0.9.2
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-globbing.so.4
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-globbing.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-proposal.so.0.9.2
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-proposal.so.4
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-proposal.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-meta.so.0.9.2
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-meta.so.4
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-meta.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-plugin.so.0.9.2
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-plugin.so.4
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-plugin.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-pluginprocess.so.0.9.2
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-pluginprocess.so.4
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-pluginprocess.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-utility.so.0.9.2
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-utility.so.4
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-utility.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-io.so.0.9.2
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-io.so.4
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-io.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/pkgconfig/elektra-io.pc
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-invoke.so.0.9.2
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-invoke.so.4
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-invoke.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-highlevel.so.0.9.2
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-highlevel.so.4
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-highlevel.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/pkgconfig/elektra-highlevel.pc
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/pkgconfig/elektra-codegen.pc
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-merge.so.0.9.2
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-merge.so.4
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-merge.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/pkgconfig/elektra-merge.pc
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-opts.so.0.9.2
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-opts.so.4
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-opts.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-core.so.0.9.2
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-core.so.4
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-core.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-kdb.so.0.9.2
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-kdb.so.4
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-kdb.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/cmake/Elektra/ElektraTargetsLibelektra.cmake
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/cmake/Elektra/ElektraTargetsLibelektra-release.cmake
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdb.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbcontext.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbexcept.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbio.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbplugin.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbthread.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbtimer.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbvalue.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/key.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/keyexcept.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/keyio.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/keyset.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/keysetget.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/keysetio.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/bin/kdb
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbextension.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbmeta.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbease.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbtypes.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbhelper.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdb.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbmodule.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbos.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbopts.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbplugin.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbpluginprocess.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbprivate.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbproposal.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbinvoke.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbutility.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbio.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbnotification.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbglobbing.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbversion.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/elektra.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbendian.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbmacros.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/kdbmerge.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/elektra/error.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/elektra/conversion.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/include/elektra/elektra/types.h
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-core/usr/lib/libelektra-io.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-core/usr/lib/libelektra-highlevel.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-core/usr/lib/libelektra-pluginprocess.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-core/usr/lib/libelektra-merge.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-core/usr/lib/libelektra-ease.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-core/usr/lib/libelektra-kdb.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-core/usr/lib/libelektra-invoke.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-core/usr/lib/libelektra-plugin.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-core/usr/lib/libelektra-ni.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-core/usr/lib/libelektra-sync.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-core/usr/lib/libelektra-opts.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-core/usr/lib/libelektra-resolver_fm_pb_b.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-core/usr/lib/libelektra-meta.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-core/usr/lib/libelektra-ini.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-core/usr/lib/libelektra-core.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-core/usr/lib/libelektra-proposal.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-core/usr/lib/libelektra-mmapstorage.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-core/usr/lib/libelektra-cache.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-core/usr/lib/libelektra-globbing.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-core/usr/lib/libelektra-utility.so.0.9.2: shared object
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-core into /openwrt/bin/packages/mips_24kc/packages/libelektra-core_0.9.2-2_mips_24kc.ipk
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/elektra-kdb/usr/bin/kdb: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/elektra-kdb/usr/lib/libelektratools.so.0.9.2: shared object
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/elektra-kdb into /openwrt/bin/packages/mips_24kc/packages/elektra-kdb_0.9.2-2_mips_24kc.ipk
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-resolvers/usr/lib/libelektra-resolver_fm_hpu_b.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-resolvers/usr/lib/libelektra-noresolver.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-resolvers/usr/lib/libelektra-resolver_fm_uhb_xb.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-resolvers/usr/lib/libelektra-resolver_fm_b_b.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-resolvers/usr/lib/libelektra-wresolver.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-resolvers/usr/lib/libelektra-resolver_fm_hp_b.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-resolvers/usr/lib/libelektra-resolver_fm_hb_b.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-resolvers/usr/lib/libelektra-resolver_fm_xb_x.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-resolvers/usr/lib/libelektra-resolver_fm_xhp_x.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-resolvers/usr/lib/libelektra-resolver_fm_xp_x.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-resolvers/usr/lib/libelektra-resolver_fm_ub_x.so: shared object
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-resolvers into /openwrt/bin/packages/mips_24kc/packages/libelektra-resolvers_0.9.2-2_mips_24kc.ipk
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-filecheck.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-csvstorage.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-mini.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-iconv.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-line.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-ipaddr.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-rgbcolor.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-syslog.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-list.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-hidden.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-path.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-lineendings.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-date.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-network.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-shell.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-quickdump.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-reference.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-hosts.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-hexcode.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-keytometa.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-hexnumber.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-conditionals.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-null.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-uname.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-profile.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-validation.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-range.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-macaddr.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-mathcheck.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-file.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-unit.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-type.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-glob.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins/usr/lib/libelektra-base64.so: shared object
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-plugins into /openwrt/bin/packages/mips_24kc/packages/libelektra-plugins_0.9.2-2_mips_24kc.ipk
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-boost/usr/lib/libelektra-tcl.so: shared object
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-boost into /openwrt/bin/packages/mips_24kc/packages/libelektra-boost_0.9.2-2_mips_24kc.ipk
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-cpp/usr/lib/libelektra-dump.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-cpp/usr/lib/libelektra-directoryvalue.so: shared object
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-cpp/usr/lib/libelektra-ccode.so: shared object
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-mips_24kc/libelektra-cpp into /openwrt/bin/packages/mips_24kc/packages/libelektra-cpp_0.9.2-2_mips_24kc.ipk
cp: cannot stat '/openwrt/build_dir/target-mips_24kc_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-curlget.so': No such file or directory
make[3]: *** [Makefile:440: /openwrt/bin/packages/mips_24kc/packages/libelektra-curlget_0.9.2-2_mips_24kc.ipk] Error 1
```
